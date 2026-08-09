"""
Crawler module: discover authoritative Australian visa-related pages across
in-scope government domains. Uses sitemaps + key-path crawling with polite
rate limiting. Extracts metadata, detects changes via content hash, and
classifies pages by category and visa subclass.

Excludes: forums, blogs, migration agent marketing, Reddit, news aggregators.
"""

from __future__ import annotations

import hashlib
import logging
import re
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

# ── Visas subclass patterns ──────────────────────────────────────────────────
_VISA_PATTERNS: dict[str, str] = {
    r"\bsubclass\s*189\b": "189",
    r"\bsubclass\s*190\b": "190",
    r"\bsubclass\s*491\b": "491",
    r"\bsubclass\s*494\b": "494",
    r"\bsubclass\s*482\b": "482",
    r"\bsubclass\s*186\b": "186",
    r"\bsubclass\s*187\b": "187",
    r"\bsubclass\s*494\b": "494",
    r"\bsubclass\s*500\b": "500",
    r"\bsubclass\s*485\b": "485",
    r"\bsubclass\s*407\b": "407",
    r"\bsubclass\s*408\b": "408",
    r"\bsubclass\s*400\b": "400",
    r"\bsubclass\s*417\b": "417",
    r"\bsubclass\s*462\b": "462",
    r"\bsubclass\s*476\b": "476",
    r"\bsubclass\s*820\b": "820",
    r"\bsubclass\s*801\b": "801",
    r"\bsubclass\s*309\b": "309",
    r"\bsubclass\s*100\b": "100",
    r"\bsubclass\s*300\b": "300",
    r"\bsubclass\s*600\b": "600",
    r"\bsubclass\s*601\b": "601",
    r"\bsubclass\s*651\b": "651",
    r"\bsubclass\s*870\b": "870",
    r"\bsubclass\s*884\b": "884",
    r"\bsubclass\s*887\b": "887",
    r"\bsubclass\s*888\b": "888",
    r"\bsubclass\s*890\b": "890",
    r"\bsubclass\s*132\b": "132",
    r"\bsubclass\s*188\b": "188",
    r"\bsubclass\s*888\b": "888",
    r"\bskilled.*independent.*\(?189\)?": "189",
    r"\bskilled.*nominated.*\(?190\)?": "190",
    r"\bskilled.*regional.*\(?491\)?": "491",
    r"\btemporary.*skill.*shortage.*\(?482\)?": "482",
    r"\bemployer.*nomination.*scheme.*\(?186\)?": "186",
    r"\bstudent.*visa.*\(?500\)?": "500",
    r"\bpartner.*visa.*\(?820\)?": "820",
    r"\bpartner.*visa.*\(?309\)?": "309",
}

# ── Category classification ──────────────────────────────────────────────────
_CATEGORY_PATTERNS: dict[str, list[str]] = {
    "visa subclass page": [
        r"/visa-listing/", r"/visas/", r"/visa/", r"subclass-\d",
        r"/skilled-visa", r"/skilled-migration",
        r"/skilled-migrants", r"/visa-options",
        r"/nomination-options", r"/skilled-nominated",
        r"/skilled-independent", r"/skilled-regional",
        r"/temporary-graduate", r"/student-visa",
        r"/skills-in-demand", r"/tss-",
        r"/employer-sponsored", r"/working-holiday",
    ],
    "state nomination": [
        r"/skilled-migrants", r"/nomination", r"/state-nomination",
        r"skilled.*occupation.*list", r"/visa-nomination",
        r"/business-migration", r"/migrate/",
    ],
    "legislation": [
        r"/legislation", r"/Details/", r"/Series/", r"migration-act",
        r"migration-regulations", r"legislative-instrument",
    ],
    "policy": [
        r"/policy", r"/discussion-paper", r"/consultation",
        r"/migration-program", r"/planning-level",
    ],
    "processing times": [
        r"/processing-times", r"/visa-processing",
    ],
    "fees": [
        r"/fees", r"/visa-fees", r"/charges",
    ],
    "occupation list": [
        r"/skilled-occupation", r"/occupation-list",
        r"/sol", r"/csol", r"/skills-occupation",
        r"/occupation-shortage", r"/occupation-ceiling",
    ],
    "announcement": [
        r"/news", r"/media-release", r"/announcement",
        r"/archive", r"/latest-news", r"/news-events",
    ],
    "form": [
        r"/form/", r"/forms/", r"form-\d", r"\.pdf",
        r"/form-listing/",
    ],
    "tribunal decision": [
        r"/decisions", r"/migration-and-refugee", r"/art-decisions",
        r"/aat-decisions", r"/migration-decisions",
    ],
    "annual report": [
        r"/annual-report", r"/reports-and-publications",
    ],
    "planning levels": [
        r"/planning-level", r"/migration-program-planning",
    ],
    "consumer guide": [
        r"/consumer-guide", r"/mara", r"/agent-regulations",
    ],
    "statistics": [
        r"/statistics", r"/data/", r"/abs",
    ],
    "settlement info": [
        r"/why-", r"/about-", r"/discover", r"/regions",
        r"/live-in", r"/move-to", r"/contact-us",
        r"/help", r"/events", r"/before-applying",
        r"/work-in", r"homepage", r"/$",
    ],
    "invitation rounds": [
        r"/invitation-round", r"/skillselect", r"/eoi",
    ],
    "health & character": [
        r"/health", r"/character", r"/english-language",
        r"/meeting-our-requirements",
    ],
}


# ── Source record ─────────────────────────────────────────────────────────────


@dataclass
class SourceRecord:
    """A single visa-related page record matching the Notion schema."""

    title: str = ""
    url: str = ""                    # canonical URL (dedup key)
    source_authority: str = ""
    category: str = "other"
    visa_subclasses: list[str] = field(default_factory=list)
    published_date: str = ""         # ISO date or empty
    summary: str = ""                # 2–3 sentences
    reliability_tier: int = 3        # 1=legislation, 2=official guidance, 3=supporting
    status: str = "new"              # new / updated / unchanged / dead
    change_log: str = ""             # what changed (for updated records)
    last_checked: str = ""           # ISO date
    page_hash: str = ""              # content hash for change detection

    def to_dict(self) -> dict[str, Any]:
        return {
            "Title": self.title,
            "URL": self.url,
            "Source authority": self.source_authority,
            "Category": self.category,
            "Related visa subclasses": self.visa_subclasses,
            "Published / last updated": self.published_date,
            "Summary": self.summary,
            "Reliability tier": self.reliability_tier,
            "Status": self.status,
            "Change log": self.change_log,
            "Last checked": self.last_checked,
            "Page hash": self.page_hash,
        }

    def is_valid(self) -> bool:
        return bool(self.url.strip()) and bool(self.title.strip())


# ── Crawler ──────────────────────────────────────────────────────────────────


class VisaSourceCrawler:
    """Crawl in-scope Australian government domains for visa-related pages."""

    def __init__(
        self,
        domains_cfg: list[dict[str, Any]],
        max_total_pages: int = 200,
        max_per_domain: int = 30,
        request_delay: float = 1.5,
        timeout: int = 20,
        user_agent: str = "AU-Visa-Source-Registry/1.0",
    ):
        self.domains_cfg = domains_cfg
        self.max_total_pages = max_total_pages
        self.max_per_domain = max_per_domain
        self.request_delay = request_delay
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-AU,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        })
        self._last_request = 0.0
        # Browser-like UA pool for CDN-unblocking retries
        self._fallback_uas = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15",
        ]

    def _throttle(self) -> None:
        elapsed = time.monotonic() - self._last_request
        if elapsed < self.request_delay:
            time.sleep(self.request_delay - elapsed)
        self._last_request = time.monotonic()

    def _fetch(self, url: str) -> tuple[int, str, str]:
        """Fetch a URL with CDN-block detection and browser-UA retry.
        Returns (status_code, final_url, html_text)."""
        self._throttle()
        result = self._fetch_inner(url)
        status, final_url, html = result
        
        # Detect CDN blocks (Akamai/EdgeSuite Access Denied)
        is_blocked = (
            status == 403 or
            (html and ("Access Denied" in html[:500] or "Reference #" in html[:500]))
        )
        
        if is_blocked:
            for ua in self._fallback_uas:
                time.sleep(2.0)  # polite delay before retry
                logger.info("CDN block detected for %s — retrying with browser UA", urlparse(url).netloc)
                old_ua = self.session.headers["User-Agent"]
                self.session.headers["User-Agent"] = ua
                try:
                    result = self._fetch_inner(url)
                    s2, _, h2 = result
                    if s2 == 200 and h2 and "Access Denied" not in h2[:500]:
                        logger.info("CDN unblock succeeded for %s", urlparse(url).netloc)
                        # Keep the working UA for subsequent requests
                        return result
                finally:
                    self.session.headers["User-Agent"] = old_ua
            logger.warning("CDN block persisted for %s after %d retries — giving up on this URL", 
                          urlparse(url).netloc, len(self._fallback_uas))
        
        return result
    
    def _fetch_inner(self, url: str) -> tuple[int, str, str]:
        """Core HTTP fetch. Returns (status_code, final_url, html_text)."""
        try:
            resp = self.session.get(
                url,
                timeout=(10, self.timeout),
                allow_redirects=True,
                headers={"Accept": "text/html,application/xhtml+xml,*/*"},
            )
            ct = resp.headers.get("content-type", "")
            if "text/html" in ct or not ct:
                return resp.status_code, resp.url, resp.text
            return resp.status_code, resp.url, ""
        except requests.RequestException as e:
            logger.debug("Request failed for %s: %s", url, e)
            return 0, url, ""

    def _extract_links(self, html: str, base_url: str) -> list[str]:
        """Extract unique, same-domain links from HTML."""
        links: list[str] = []
        try:
            soup = BeautifulSoup(html, "html.parser")
            base_domain = urlparse(base_url).netloc
            for a in soup.find_all("a", href=True):
                href = a["href"]
                full = urljoin(base_url, href)
                parsed = urlparse(full)
                # Only same-domain, no fragments, no mailto/javascript
                if parsed.netloc == base_domain and parsed.scheme in ("http", "https"):
                    clean = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                    if clean not in links and not parsed.path.endswith((".jpg", ".png", ".pdf", ".css", ".js")):
                        links.append(clean)
        except Exception:
            pass
        return links

    def _is_visa_related(self, url: str, title: str, html: str) -> bool:
        """Check if a page is visa/migration related."""
        combined = f"{url.lower()} {title.lower()} {html[:5000].lower()}"
        keywords = [
            "visa", "migration", "migrant", "subclass", "immigra",
            "skilled occupation", "nomination", "sponsor", "partner visa",
            "student visa", "temporary graduate", "working holiday",
            "humanitarian", "refugee", "protection visa", "citizenship",
            "permanent resident", "temporary resident", "bridging visa",
            "mara", "migration agent", "skill assessment", "english test",
            "character requirement", "health requirement", "visa condition",
            "migration program", "planning level", "migration act",
            "migration regulations", "legislative instrument",
            "settle in", "move to", "live in", "work in",  # state migration sites
            "skilled migrant", "business migration", "state nomination",
        ]
        return any(kw in combined for kw in keywords)

    def _classify_category(self, url: str, html: str) -> str:
        """Classify a page into a category."""
        combined = f"{url.lower()} {html[:2000].lower()}"
        for category, patterns in _CATEGORY_PATTERNS.items():
            for pat in patterns:
                if re.search(pat, combined):
                    return category
        return "other"

    def _extract_visa_subclasses(self, html: str) -> list[str]:
        """Extract mentioned visa subclass numbers."""
        found: set[str] = set()
        text = html[:10000]  # first 10k chars is enough
        for pattern, subclass in _VISA_PATTERNS.items():
            if re.search(pattern, text, re.IGNORECASE):
                found.add(subclass)
        return sorted(found)

    def _compute_reliability(self, url: str, category: str) -> int:
        """Assign reliability tier based on domain and category."""
        domain = urlparse(url).netloc.lower()
        if "legislation.gov.au" in domain:
            return 1
        if category == "legislation":
            return 1
        if category in ("policy", "processing times", "fees", "occupation list", "planning levels", "annual report"):
            return 2
        if "homeaffairs.gov.au" in domain or "immi.homeaffairs.gov.au" in domain:
            return 2
        # State/territory, edu, jobs sites
        return 3

    def _extract_title(self, html: str) -> str:
        """Extract page title."""
        try:
            soup = BeautifulSoup(html, "html.parser")
            title_tag = soup.find("title")
            if title_tag:
                t = title_tag.get_text(strip=True)
                # Clean common suffixes
                for suffix in [
                    " | Department of Home Affairs",
                    " — Department of Home Affairs",
                    " | homeaffairs.gov.au",
                    " | immi.homeaffairs.gov.au",
                    " — immi.homeaffairs.gov.au",
                ]:
                    t = t.replace(suffix, "")
                return t.strip()[:300]
            h1 = soup.find("h1")
            if h1:
                return h1.get_text(strip=True)[:300]
        except Exception:
            pass
        return ""

    def _extract_date(self, html: str) -> str:
        """Try to extract published/modified date from meta tags or visible dates."""
        try:
            soup = BeautifulSoup(html, "html.parser")
            # Meta tags
            for meta in soup.find_all("meta"):
                prop = meta.get("property", "").lower()
                name = meta.get("name", "").lower()
                content = meta.get("content", "")
                if ("date" in prop or "modified" in prop or "modified" in name) and content:
                    return content[:10]
            # Look for date patterns in visible text
            text = soup.get_text()[:2000]
            patterns = [
                r"(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d{2})",
                r"(?:updated|published|last modified|last updated)[:\s]*(\d{1,2}[/-]\d{1,2}[/-]20\d{2})",
            ]
            for pat in patterns:
                m = re.search(pat, text, re.IGNORECASE)
                if m:
                    return m.group(1)
        except Exception:
            pass
        return ""

    def _generate_summary(self, title: str, html: str) -> str:
        """Generate a 2-3 sentence descriptive summary."""
        try:
            soup = BeautifulSoup(html, "html.parser")
            # Get first meaningful paragraph content
            for tag in soup.find_all(["p", "div"], class_=re.compile(r"intro|summary|lead|abstract", re.I)):
                text = tag.get_text(strip=True)
                if len(text) > 50:
                    return text[:400]

            # Fallback: first 2-3 <p> tags
            paragraphs = soup.find_all("p")
            texts = []
            for p in paragraphs:
                t = p.get_text(strip=True)
                if len(t) > 30:
                    texts.append(t)
                    if len(" ".join(texts)) > 300:
                        break
            summary = " ".join(texts[:3])
            return summary[:400] if summary else title
        except Exception:
            return title

    def _compute_hash(self, html: str) -> str:
        """Content hash for change detection."""
        # Hash the first 50k chars (body content only)
        try:
            soup = BeautifulSoup(html, "html.parser")
            body = soup.find("body")
            text = body.get_text(" ", strip=True)[:50000] if body else html[:50000]
        except Exception:
            text = html[:50000]
        return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()[:16]

    # ── Public API ──────────────────────────────────────────────────────

    def crawl_all(self, existing_urls: set[str]) -> list[SourceRecord]:
        """
        Crawl all in-scope domains. Skip URLs already in `existing_urls`.
        Returns up to max_total_pages new/updated records.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        all_records: list[SourceRecord] = []
        seen_this_run: set[str] = set()

        for domain_cfg in self.domains_cfg:
            if len(all_records) >= self.max_total_pages:
                break

            base_url = domain_cfg["base_url"]
            authority = domain_cfg["authority"]
            key_paths = domain_cfg.get("key_paths", [])

            logger.info("Crawling %s (%s)", authority, base_url)
            domain_records = self._crawl_domain(
                base_url, authority, key_paths, existing_urls, seen_this_run, today
            )
            all_records.extend(domain_records)
            logger.info("  → %d new records from %s", len(domain_records), authority)

        return all_records

    def _crawl_domain(
        self,
        base_url: str,
        authority: str,
        key_paths: list[str],
        existing_urls: set[str],
        seen_this_run: set[str],
        today: str,
    ) -> list[SourceRecord]:
        """Crawl one domain for visa-related pages. Bounded by max_per_domain."""
        records: list[SourceRecord] = []
        checked_urls: set[str] = set()

        # 1. Seed URLs from key paths
        seed_urls: list[str] = []
        for path in key_paths:
            full = urljoin(base_url, path)
            if full not in checked_urls and full not in existing_urls:
                seed_urls.append(full)
                checked_urls.add(full)

        # 2. Add sitemap URLs
        for su in self._discover_sitemap(base_url)[:30]:
            if su not in checked_urls and su not in existing_urls:
                seed_urls.append(su)
                checked_urls.add(su)

        # 3. Crawl seeds, collect child links
        child_links: list[str] = []
        for url in seed_urls[:self.max_per_domain * 2]:
            if len(records) >= self.max_per_domain:
                break

            status, final_url, html = self._fetch(url)
            if status == 0:
                continue
            if status == 404:
                if url in existing_urls:
                    records.append(SourceRecord(
                        title=f"[DEAD] {urlparse(url).path.split('/')[-1] or url}",
                        url=url, source_authority=authority,
                        status="dead", last_checked=today,
                    ))
                continue

            title = self._extract_title(html)
            if not self._is_visa_related(final_url, title, html):
                continue

            if final_url in existing_urls or final_url in seen_this_run:
                continue
            seen_this_run.add(final_url)

            rec = SourceRecord(
                title=title,
                url=final_url,
                source_authority=authority,
                category=self._classify_category(final_url, html),
                visa_subclasses=self._extract_visa_subclasses(html),
                published_date=self._extract_date(html),
                summary=self._generate_summary(title, html),
                reliability_tier=self._compute_reliability(final_url, self._classify_category(final_url, html)),
                status="new",
                last_checked=today,
                page_hash=self._compute_hash(html),
            )
            if rec.is_valid():
                records.append(rec)

            # Collect child links (to crawl if we have room)
            if len(records) + len(child_links) < self.max_per_domain * 3:
                for cl in self._extract_links(html, final_url):
                    if cl not in checked_urls and cl not in existing_urls:
                        child_links.append(cl)
                        checked_urls.add(cl)

        # 4. Crawl children if under limit
        for cl in child_links[:self.max_per_domain]:
            if len(records) >= self.max_per_domain:
                break

            status, final_url, html = self._fetch(cl)
            if status != 200 or final_url in existing_urls or final_url in seen_this_run:
                continue
            seen_this_run.add(final_url)

            title = self._extract_title(html)
            if not self._is_visa_related(final_url, title, html):
                continue

            rec = SourceRecord(
                title=title,
                url=final_url,
                source_authority=authority,
                category=self._classify_category(final_url, html),
                visa_subclasses=self._extract_visa_subclasses(html),
                published_date=self._extract_date(html),
                summary=self._generate_summary(title, html),
                reliability_tier=self._compute_reliability(final_url, self._classify_category(final_url, html)),
                status="new",
                last_checked=today,
                page_hash=self._compute_hash(html),
            )
            if rec.is_valid():
                records.append(rec)

        return records

    def _discover_sitemap(self, base_url: str) -> list[str]:
        """Try to find and parse sitemap.xml for a domain."""
        urls: list[str] = []
        sitemap_url = urljoin(base_url, "/sitemap.xml")
        try:
            status, _, xml = self._fetch(sitemap_url)
            if status != 200:
                # Try common alternatives
                for alt in ["/sitemap", "/sitemap_index.xml", "/sitemap-index.xml"]:
                    alt_url = urljoin(base_url, alt)
                    status, _, xml = self._fetch(alt_url)
                    if status == 200:
                        break
                if status != 200:
                    return urls

            soup = BeautifulSoup(xml, "xml")
            for loc in soup.find_all("loc"):
                url_text = loc.get_text(strip=True)
                if url_text:
                    urls.append(url_text)
            logger.debug("Found %d URLs in sitemap for %s", len(urls), base_url)
        except Exception as e:
            logger.debug("Sitemap not found for %s: %s", base_url, e)
        return urls

    def check_existing(self, records: list[SourceRecord]) -> list[SourceRecord]:
        """
        For existing records, re-fetch to detect changes and dead links.
        Returns records that changed (with updated status/hash/change_log).
        """
        today = datetime.now().strftime("%Y-%m-%d")
        changed: list[SourceRecord] = []

        for rec in records:
            status, final_url, html = self._fetch(rec.url)
            rec.last_checked = today

            if status == 404 or status == 410:
                rec.status = "dead"
                rec.change_log = f"{today}: link dead (HTTP {status})"
                changed.append(rec)
                continue

            if final_url != rec.url:
                # Redirect — update to new canonical URL
                rec.change_log = f"{today}: URL redirected from {rec.url} to {final_url}"
                rec.url = final_url

            new_hash = self._compute_hash(html)
            if new_hash != rec.page_hash:
                rec.status = "updated"
                rec.page_hash = new_hash
                rec.change_log = (rec.change_log + "; " if rec.change_log else "") + f"{today}: content changed"
                # Update title if it changed
                new_title = self._extract_title(html)
                if new_title and new_title != rec.title:
                    rec.change_log += f"; title updated"
                    rec.title = new_title
                changed.append(rec)
            else:
                rec.status = "unchanged"

        return changed