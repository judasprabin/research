#!/usr/bin/env python3
"""
AU Visa Source Registry — main orchestrator.

Usage:
  python main.py              # full run: crawl + upsert to Notion
  python main.py --dry-run    # crawl + validate without writing to Notion
  python main.py --check-only # only re-check existing URLs for changes

Environment:
  NOTION_TOKEN        — Notion integration token (required)
  NOTION_DATABASE_ID  — existing Notion database ID (optional)
  NOTION_PARENT_PAGE  — page ID where the database lives (for run logs)

Config: config.yaml (domains, categories, caps, logging)
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path

import yaml
from dotenv import load_dotenv

from crawler import SourceRecord, VisaSourceCrawler
from notion_registry import NotionRegistry

LOG_FORMAT = "%(asctime)s [%(levelname)-7s] %(name)s — %(message)s"
LOG_DATE_FMT = "%Y-%m-%d %H:%M:%S"


def setup_logging(log_cfg: dict, project_root: Path) -> logging.Logger:
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_cfg.get("level", "INFO"), "INFO"))
    root_logger.handlers.clear()

    stdout = logging.StreamHandler(sys.stdout)
    stdout.setFormatter(logging.Formatter(LOG_FORMAT, LOG_DATE_FMT))
    root_logger.addHandler(stdout)

    log_path = project_root / log_cfg.get("file", "logs/au-visa-crawler.log")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fh = RotatingFileHandler(
        str(log_path),
        maxBytes=log_cfg.get("max_bytes", 5_242_880),
        backupCount=log_cfg.get("backup_count", 3),
    )
    fh.setFormatter(logging.Formatter(LOG_FORMAT, LOG_DATE_FMT))
    root_logger.addHandler(fh)

    return logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="AU Visa Source Registry — discover and track visa-related sources"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Crawl and print without writing to Notion")
    parser.add_argument("--check-only", action="store_true",
                        help="Only re-check existing URLs for changes/dead links")
    parser.add_argument("--config", default="config.yaml",
                        help="Path to config.yaml")
    args = parser.parse_args()

    load_dotenv()
    project_root = Path(__file__).resolve().parent
    config_path = project_root / args.config

    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"ERROR: Config issue: {e}", file=sys.stderr)
        return 1

    log_cfg = config.get("log", {})
    logger = setup_logging(log_cfg, project_root)
    logger.info("=== AU Visa Source Registry ===")
    logger.info("Dry run: %s | Check-only: %s", args.dry_run, args.check_only)

    notion_token = os.getenv("NOTION_TOKEN", "").strip()
    notion_db_id = os.getenv("NOTION_DATABASE_ID", "").strip()
    notion_parent_page = os.getenv("NOTION_PARENT_PAGE", "").strip() or notion_db_id

    if not args.dry_run and not notion_token:
        logger.critical("NOTION_TOKEN not set. Export it or use --dry-run.")
        return 1

    # ── Notion setup ────────────────────────────────────────────────────
    notion = NotionRegistry(
        token=notion_token if not args.dry_run else "",
        database_id=notion_db_id,
        database_name=config.get("notion", {}).get("database_name", "AU Visa Source Registry"),
        rate_limit_rps=config.get("notion", {}).get("rate_limit_rps", 2.8),
        dry_run=args.dry_run,
    )

    if not args.dry_run:
        try:
            db_id = notion.ensure_database()
            notion.database_id = db_id
            logger.info("Notion database ready: %s", db_id)
        except Exception:
            logger.critical("Failed to init Notion", exc_info=True)
            return 1

    # ── Load existing records ───────────────────────────────────────────
    existing = notion.load_existing_urls()
    existing_urls = set(existing.keys())
    logger.info("Existing records in registry: %d", len(existing_urls))

    # ── Crawler ─────────────────────────────────────────────────────────
    crawler_cfg = config.get("crawler", {})
    crawler = VisaSourceCrawler(
        domains_cfg=config.get("domains", []),
        max_total_pages=crawler_cfg.get("max_pages_per_run", 200),
        max_per_domain=crawler_cfg.get("max_pages_per_domain", 30),
        request_delay=crawler_cfg.get("request_delay_seconds", 1.5),
        timeout=crawler_cfg.get("timeout_seconds", 20),
        user_agent=crawler_cfg.get("user_agent", "AU-Visa-Source-Registry/1.0"),
    )

    if args.check_only:
        logger.info("Check-only mode: re-verifying %d existing URLs", len(existing_urls))
        # Convert existing dict entries to SourceRecords for the crawler
        existing_records = []
        for url, data in existing.items():
            existing_records.append(SourceRecord(
                title=data.get("title", ""),
                url=url,
                source_authority=data.get("source_authority", ""),
                category=data.get("category", "other"),
                status=data.get("status", ""),
                change_log=data.get("change_log", ""),
                page_hash=data.get("page_hash", ""),
                last_checked=data.get("last_checked", ""),
            ))
        changed = crawler.check_existing(existing_records)
        logger.info("Check complete: %d changed (updated/dead)", len(changed))
        new_records = [r.to_dict() for r in changed]
    else:
        logger.info(
            "Crawling %d domains (max %d pages total, %d per domain)...",
            len(config["domains"]),
            crawler_cfg.get("max_pages_per_run", 200),
            crawler_cfg.get("max_pages_per_domain", 30),
        )
        records = crawler.crawl_all(existing_urls)
        new_records = [r.to_dict() for r in records]

        # Also check a sample of existing records for changes
        # (Only the first ~50 most recently checked records)
        if existing and not args.dry_run:
            existing_sample = []
            for url, data in list(existing.items())[:50]:
                existing_sample.append(SourceRecord(
                    title=data.get("title", ""),
                    url=url,
                    source_authority=data.get("source_authority", ""),
                    category=data.get("category", "other"),
                    status=data.get("status", ""),
                    change_log=data.get("change_log", ""),
                    page_hash=data.get("page_hash", ""),
                    last_checked=data.get("last_checked", ""),
                ))
            changed = crawler.check_existing(existing_sample)
            logger.info("Re-checked %d existing — %d changed", len(existing_sample), len(changed))
            for r in changed:
                new_records.append(r.to_dict())

    # ── Output / Upsert ─────────────────────────────────────────────────
    if args.dry_run:
        _print_dry_run(new_records, existing)
        return 0

    logger.info("Upserting %d records to Notion...", len(new_records))
    counts = notion.upsert_batch(new_records, existing)

    # Build notable changes for run log
    notable = []
    for rec in new_records:
        status = rec.get("Status", "")
        if status == "dead":
            notable.append(f"Dead link: {rec.get('URL', '')}")
        elif status == "updated" and rec.get("Change log"):
            notable.append(f"Updated: {rec.get('Title', rec.get('URL', ''))} — {rec.get('Change log', '')}")

    # Write run log
    run_url = notion.write_run_log(counts, notable[:10], notion_parent_page)

    # ── Summary ─────────────────────────────────────────────────────────
    logger.info("=== Run complete ===")
    logger.info("  Created: %d  |  Updated: %d  |  Skipped: %d  |  Dead: %d  |  Failed: %d",
                counts.get("created", 0), counts.get("updated", 0),
                counts.get("skipped", 0), counts.get("dead", 0),
                counts.get("failed", 0))
    if run_url:
        logger.info("  Run log: %s", run_url)

    # Write JSON summary
    _write_summary(project_root, counts, new_records, notable)

    if counts.get("failed", 0) > 0 and counts.get("created", 0) == 0:
        return 3
    return 0


def _print_dry_run(records: list[dict], existing: dict) -> None:
    print("=" * 72)
    print("DRY-RUN — No data written to Notion")
    print("=" * 72)
    print(f"Existing records: {len(existing)}")
    print(f"New/changed records this run: {len(records)}")

    by_status: dict[str, int] = {}
    for r in records:
        s = r.get("Status", "new")
        by_status[s] = by_status.get(s, 0) + 1
    for status, count in by_status.items():
        print(f"  {status}: {count}")

    print(f"\nSample records (first 10):")
    for i, r in enumerate(records[:10]):
        print(f"\n  [{i+1}] {r.get('Title', 'N/A')}")
        print(f"      URL:        {r.get('URL', 'N/A')}")
        print(f"      Authority:  {r.get('Source authority', 'N/A')}")
        print(f"      Category:   {r.get('Category', 'N/A')}")
        subs = r.get("Related visa subclasses", [])
        if subs:
            print(f"      Visas:      {', '.join(subs)}")
        print(f"      Tier:       {r.get('Reliability tier', 'N/A')}")
        print(f"      Status:     {r.get('Status', 'N/A')}")

    print(f"\n{'─' * 72}")
    print(f"All records have URLs: {all(bool(r.get('URL')) for r in records)}")
    print("=" * 72)


def _write_summary(
    project_root: Path,
    counts: dict[str, int],
    records: list[dict],
    notable: list[str],
) -> None:
    import json

    d = project_root / "logs" / "summaries"
    d.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    p = d / f"run_{ts}.json"

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "counts": counts,
        "total_records": len(records),
        "sources": [
            {"title": r.get("Title", ""), "url": r.get("URL", ""),
             "authority": r.get("Source authority", ""),
             "category": r.get("Category", ""), "status": r.get("Status", "")}
            for r in records[:50]
        ],
        "notable": notable[:20],
    }
    with open(p, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    logging.getLogger(__name__).info("Summary written to %s", p)


if __name__ == "__main__":
    sys.exit(main())