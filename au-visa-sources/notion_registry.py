"""
Notion registry: create/verify AU Visa Source Registry database, upsert source
records with canonical URL dedup, and write run log summaries.

Dedup: match on canonical URL (exact). If found → check hash for changes →
update if changed; if not found → create.

Additionally writes a "Run Log" page to track each run's summary.
"""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from typing import Any

from notion_client import Client, APIResponseError
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

# ── Database property schema ─────────────────────────────────────────────────
DATABASE_PROPERTIES: dict[str, dict[str, Any]] = {
    "Title": {"title": {}},
    "URL": {"url": {}},
    "Source authority": {
        "select": {
            "options": [
                {"name": "Department of Home Affairs", "color": "blue"},
                {"name": "Australian Government Legislation", "color": "red"},
                {"name": "Administrative Appeals Tribunal", "color": "orange"},
                {"name": "Administrative Review Tribunal", "color": "orange"},
                {"name": "Office of the MARA", "color": "yellow"},
                {"name": "Australian Government — Study Australia", "color": "green"},
                {"name": "Jobs and Skills Australia", "color": "green"},
                {"name": "The Treasury", "color": "gray"},
                {"name": "Australian Government Budget", "color": "gray"},
                {"name": "NSW Government", "color": "purple"},
                {"name": "Victorian Government", "color": "purple"},
                {"name": "Queensland Government", "color": "purple"},
                {"name": "Western Australia Government", "color": "purple"},
                {"name": "South Australia Government", "color": "purple"},
                {"name": "Australian Bureau of Statistics", "color": "brown"},
            ]
        }
    },
    "Category": {
        "select": {
            "options": [
                {"name": "visa subclass page", "color": "blue"},
                {"name": "state nomination", "color": "purple"},
                {"name": "legislation", "color": "red"},
                {"name": "policy", "color": "orange"},
                {"name": "processing times", "color": "yellow"},
                {"name": "fees", "color": "yellow"},
                {"name": "occupation list", "color": "green"},
                {"name": "invitation rounds", "color": "blue"},
                {"name": "announcement", "color": "purple"},
                {"name": "form", "color": "gray"},
                {"name": "tribunal decision", "color": "pink"},
                {"name": "annual report", "color": "brown"},
                {"name": "planning levels", "color": "blue"},
                {"name": "consumer guide", "color": "green"},
                {"name": "statistics", "color": "gray"},
                {"name": "settlement info", "color": "green"},
                {"name": "health & character", "color": "pink"},
                {"name": "other", "color": "default"},
            ]
        }
    },
    "Related visa subclasses": {"multi_select": {"options": []}},
    "Published / last updated": {"rich_text": {}},
    "Summary": {"rich_text": {}},
    "Reliability tier": {
        "select": {
            "options": [
                {"name": "1 — legislation / official policy", "color": "red"},
                {"name": "2 — official guidance", "color": "orange"},
                {"name": "3 — official supporting material", "color": "green"},
            ]
        }
    },
    "Status": {
        "select": {
            "options": [
                {"name": "new", "color": "blue"},
                {"name": "updated", "color": "yellow"},
                {"name": "unchanged", "color": "gray"},
                {"name": "dead", "color": "red"},
            ]
        }
    },
    "Change log": {"rich_text": {}},
    "Last checked": {"date": {}},
    "Page hash": {"rich_text": {}},
}


def _is_rate_limited(exception: BaseException) -> bool:
    return isinstance(exception, APIResponseError) and exception.status == 429


class NotionRegistry:
    """Manage the AU Visa Source Registry Notion database and run logs."""

    def __init__(
        self,
        token: str,
        database_id: str = "",
        database_name: str = "AU Visa Source Registry",
        rate_limit_rps: float = 2.8,
        dry_run: bool = False,
    ):
        self.token = token
        self.database_id = database_id
        self.database_name = database_name
        self.rate_limit_rps = rate_limit_rps
        self.dry_run = dry_run
        self.client = Client(auth=token) if not dry_run else None
        self._last_request = 0.0

    def _throttle(self) -> None:
        min_interval = 1.0 / max(self.rate_limit_rps, 0.1)
        elapsed = time.monotonic() - self._last_request
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        self._last_request = time.monotonic()

    @retry(
        retry=_is_rate_limited,
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=1, max=30),
        before_sleep=lambda rs: logger.warning(
            "Notion rate-limited (attempt %d/5)", rs.attempt_number
        ),
    )
    def _api(self, fn, *args: Any, **kwargs: Any) -> Any:
        self._throttle()
        return fn(*args, **kwargs)

    # ── Database management ──────────────────────────────────────────────

    def ensure_database(self) -> str:
        """Return valid database_id. Create if missing or points to a page."""
        if self.dry_run:
            return "dry-run-db-id"

        if self.database_id:
            try:
                db = self._api(self.client.databases.retrieve, self.database_id)
                logger.info(
                    "Using existing database: %s (%s)",
                    self.database_id,
                    db.get("title", [{}])[0].get("plain_text", "Untitled"),
                )
                return self.database_id
            except APIResponseError as e:
                if e.status == 404:
                    logger.warning("Database %s not found — creating", self.database_id)
                elif e.status == 400 and "not a database" in str(e).lower():
                    logger.info("ID is a page — creating database inside it")
                    return self._create_db(self.database_id)
                else:
                    raise

        return self._create_db(self._get_workspace_page())

    def _get_workspace_page(self) -> str:
        results = self._api(self.client.search, page_size=1).get("results", [])
        if results:
            return results[0]["id"]
        raise RuntimeError("No Notion pages accessible to this integration.")

    def _create_db(self, parent_page_id: str) -> str:
        logger.info("Creating '%s' database in page %s", self.database_name, parent_page_id)
        db = self._api(
            self.client.databases.create,
            parent={"type": "page_id", "page_id": parent_page_id},
            title=[{"type": "text", "text": {"content": self.database_name}}],
            properties=DATABASE_PROPERTIES,
        )
        new_id = db["id"]
        logger.info("Created database: %s", new_id)
        return new_id

    # ── Load existing records ────────────────────────────────────────────

    def load_existing_urls(self) -> dict[str, dict[str, Any]]:
        """Load all existing records keyed by canonical URL."""
        if self.dry_run:
            return {}

        url_map: dict[str, dict[str, Any]] = {}
        try:
            cursor = None
            while True:
                kwargs: dict[str, Any] = {"database_id": self.database_id, "page_size": 100}
                if cursor:
                    kwargs["start_cursor"] = cursor
                result = self._api(self.client.databases.query, **kwargs)
                for page in result.get("results", []):
                    props = page["properties"]
                    url_val = props.get("URL", {}).get("url", "")
                    if url_val:
                        url_map[url_val] = {
                            "page_id": page["id"],
                            "title": _get_title(props),
                            "page_hash": _get_rich_text(props.get("Page hash", {})),
                            "status": _get_select(props.get("Status", {})),
                            "source_authority": _get_select(props.get("Source authority", {})),
                            "category": _get_select(props.get("Category", {})),
                            "last_checked": _get_date(props.get("Last checked", {})),
                            "change_log": _get_rich_text(props.get("Change log", {})),
                            "subclasses": _get_multi_select(props.get("Related visa subclasses", {})),
                        }
                if not result.get("has_more"):
                    break
                cursor = result.get("next_cursor")
            logger.info("Loaded %d existing records from Notion", len(url_map))
        except Exception as e:
            logger.warning("Failed to load existing records: %s", e)

        return url_map

    # ── Upsert ───────────────────────────────────────────────────────────

    def upsert(
        self,
        record: dict[str, Any],
        existing: dict[str, Any] | None,
    ) -> str:
        """
        Upsert a source record. Returns 'created', 'updated', 'skipped', or 'dry_run'.

        If existing is not None, checks hash for changes. If changed, updates.
        If unchanged, skips.
        """
        url = record.get("URL", "")
        title = record.get("Title", "")

        if self.dry_run:
            logger.info("[DRY-RUN] Would upsert: %s (%s)", title, url)
            return "dry_run"

        if existing:
            old_hash = existing.get("page_hash", "")
            new_hash = record.get("Page hash", "")
            if new_hash and old_hash and new_hash == old_hash:
                # Also bump last checked
                try:
                    self._api(
                        self.client.pages.update,
                        existing["page_id"],
                        properties={"Last checked": {"date": {"start": record.get("Last checked", "")}}},
                    )
                except Exception:
                    pass
                return "skipped"

            # Update existing page
            self._update_page(existing["page_id"], record, existing)
            return "updated"

        # Create new page
        self._create_page(record)
        return "created"

    def _create_page(self, record: dict[str, Any]) -> str:
        properties = self._build_properties(record)
        result = self._api(
            self.client.pages.create,
            parent={"database_id": self.database_id},
            properties=properties,
        )
        return result["id"]

    def _update_page(
        self,
        page_id: str,
        record: dict[str, Any],
        existing: dict[str, Any],
    ) -> None:
        # Only send changed properties
        properties: dict[str, Any] = {}
        properties["Last checked"] = {"date": {"start": record.get("Last checked", "")}}
        properties["Status"] = {"select": {"name": record.get("Status", "updated")}}
        properties["Page hash"] = _rich_text(record.get("Page hash", ""))

        change_log = record.get("Change log", "")
        if change_log:
            old_log = existing.get("change_log", "")
            full_log = f"{old_log}; {change_log}" if old_log else change_log
            properties["Change log"] = _rich_text(full_log[:2000])

        title_val = record.get("Title", "")
        if title_val:
            properties["Title"] = {"title": [{"type": "text", "text": {"content": title_val}}]}

        try:
            self._api(self.client.pages.update, page_id, properties=properties)
            logger.info("Updated page: %s", record.get("Title", record.get("URL", "")))
        except APIResponseError as e:
            logger.warning("Failed to update page %s: %s", page_id, e)

    def upsert_batch(
        self,
        records: list[dict[str, Any]],
        existing_urls: dict[str, dict[str, Any]],
    ) -> dict[str, int]:
        """Upsert a batch of records. Returns counts."""
        counts: dict[str, int] = {"created": 0, "updated": 0, "skipped": 0, "dry_run": 0, "failed": 0}
        for record in records:
            try:
                url = record.get("URL", "")
                existing = existing_urls.get(url)
                result = self.upsert(record, existing)
                counts[result] += 1
            except Exception:
                logger.exception("Failed to upsert: %s", record.get("URL", ""))
                counts["failed"] += 1
        return counts

    # ── Run log ──────────────────────────────────────────────────────────

    def write_run_log(
        self,
        counts: dict[str, int],
        notable: list[str],
        parent_page_id: str,
    ) -> str:
        """Write a run log page under the parent page. Returns page URL."""
        if self.dry_run:
            logger.info("[DRY-RUN] Would write run log with counts=%s", counts)
            return ""

        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        notable_text = "\n".join(f"• {n}" for n in notable) if notable else "None"
        content = (
            f"**Run:** {ts}\n\n"
            f"**Results:**\n"
            f"• New sources: {counts.get('created', 0)}\n"
            f"• Updated: {counts.get('updated', 0)}\n"
            f"• Skipped (unchanged): {counts.get('skipped', 0)}\n"
            f"• Dead links: {counts.get('dead', 0)}\n"
            f"• Failed: {counts.get('failed', 0)}\n\n"
            f"**Notable changes:**\n{notable_text}"
        )

        try:
            page = self._api(
                self.client.pages.create,
                parent={"type": "page_id", "page_id": parent_page_id},
                properties={
                    "title": [{"type": "text", "text": {"content": f"Run Log — {ts}"}}],
                },
                children=[
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{"type": "text", "text": {"content": content}}]
                        },
                    }
                ],
            )
            logger.info("Run log written: %s", page.get("url", ""))
            return page.get("url", "")
        except Exception as e:
            logger.warning("Failed to write run log: %s", e)
            return ""

    # ── Property builders ────────────────────────────────────────────────

    def _build_properties(self, record: dict[str, Any]) -> dict[str, Any]:
        props: dict[str, Any] = {}

        # Title
        t = record.get("Title", "Untitled")
        props["Title"] = {"title": [{"type": "text", "text": {"content": str(t)[:2000]}}]}

        # URL
        url = record.get("URL", "")
        if url:
            props["URL"] = {"url": str(url)}

        # Source authority (select)
        auth = record.get("Source authority", "")
        if auth:
            props["Source authority"] = {"select": {"name": str(auth)}}

        # Category (select)
        cat = record.get("Category", "")
        if cat:
            props["Category"] = {"select": {"name": str(cat)}}

        # Related visa subclasses (multi_select)
        subs = record.get("Related visa subclasses", [])
        if isinstance(subs, str):
            subs = [s.strip() for s in subs.split(",") if s.strip()]
        if subs:
            props["Related visa subclasses"] = {"multi_select": [{"name": str(s)} for s in subs]}

        # Published date (rich_text)
        pd = record.get("Published / last updated", "")
        if pd:
            props["Published / last updated"] = _rich_text(str(pd))

        # Summary (rich_text)
        summary = record.get("Summary", "")
        if summary:
            props["Summary"] = _rich_text(str(summary)[:2000])

        # Reliability tier (select)
        tier = record.get("Reliability tier", 3)
        tier_map = {
            1: "1 — legislation / official policy",
            2: "2 — official guidance",
            3: "3 — official supporting material",
        }
        tier_name = tier_map.get(tier, tier_map[3])
        props["Reliability tier"] = {"select": {"name": tier_name}}

        # Status (select)
        status = record.get("Status", "new")
        props["Status"] = {"select": {"name": str(status)}}

        # Change log (rich_text)
        cl = record.get("Change log", "")
        if cl:
            props["Change log"] = _rich_text(str(cl)[:2000])

        # Last checked (date)
        lc = record.get("Last checked", "")
        if lc:
            props["Last checked"] = {"date": {"start": str(lc)}}

        # Page hash (rich_text)
        ph = record.get("Page hash", "")
        if ph:
            props["Page hash"] = _rich_text(str(ph))

        return props


# ── Helpers ──────────────────────────────────────────────────────────────────


def _get_title(props: dict[str, Any]) -> str:
    title_arr = props.get("Title", {}).get("title", [])
    return title_arr[0].get("plain_text", "") if title_arr else ""


def _get_rich_text(prop: dict[str, Any]) -> str:
    rt_arr = prop.get("rich_text", [])
    return rt_arr[0].get("plain_text", "") if rt_arr else ""


def _get_select(prop: dict[str, Any]) -> str:
    sel = prop.get("select")
    return sel["name"] if sel else ""


def _get_date(prop: dict[str, Any]) -> str:
    d = prop.get("date")
    return d["start"] if d else ""


def _get_multi_select(prop: dict[str, Any]) -> list[str]:
    return [m["name"] for m in prop.get("multi_select", [])]


def _rich_text(text: str) -> dict[str, Any]:
    return {"rich_text": [{"type": "text", "text": {"content": text}}]}