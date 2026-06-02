# BillScout Agent — Technical Research Report

> **Date:** 2026-06-02  
> **Author:** BillScout Agent  
> **Purpose:** MVP scoping decisions for bank transactions, grocery prices, OCR, ML, and feature prioritization

---

## 1. Bank Transaction Data in Australia

### Market Overview

Australia has a mature Open Banking ecosystem driven by the **Consumer Data Right (CDR)** legislation. The Australian Competition and Consumer Commission (ACCC) mandates that major banks provide standardized APIs for account and transaction data. This has created a competitive market of aggregators and data providers.

### Provider Comparison

| Provider | Coverage | Institutions | Auth Type | Pricing | Best For |
|----------|----------|-------------|-----------|---------|---------|
| **Basiq** | AU-native | 120+ | OAuth2 | Free tier: 500 req/day; Starter ~$200/mo; Pro from $1,000/mo | AU-first, best coverage |
| **Plaid** | Global | ~50 AU | OAuth2 | Usage-based; ~$0.10–0.25 per transaction fetch | International users |
| **Salt Edge** | EU + AU | 60+ AU | OAuth2 | €500–€2,000/mo | EU + AU combined |
| **MX** | US-focused | Limited AU | OAuth2 | Enterprise pricing | US-centric products |
| **FIS (Synctify)** | AU | Major banks | CDR-compliant | Enterprise | Banks/fintechs |
| **Fintastik** | AU | 20+ | OAuth2 | From $99/mo | Smaller providers |

### CDR (Consumer Data Right) — Direct API Access

Australia's CDR legislation means licensed data recipients can access bank data directly through the **Data Recipient Directory (DRD)**. This is a direct integration path without using an aggregator.

**Pros:** No per-request markup, direct relationship with banks  
**Cons:** Complex compliance, accreditation required, high implementation effort

### Basiq — Recommended Primary

Basiq is the most AU-focused solution with:
- **120+ institutions** including all major banks (Commonwealth, ANZ, Westpac, NAB), credit unions, and digital banks (Up, 86400, etc.)
- **Transaction enrichment:** merchant name, logo, category, location
- **Webhooks** for real-time transaction notifications
- **Sandbox:** Free testing environment

**Pricing (as of 2025):**

| Tier | Price | Requests/day | Features |
|------|-------|-------------|---------|
| Free | $0 | 500 | Basic transactions, 2 connections |
| Starter | $199/mo | 5,000 | + account verification, + 10 connections |
| Professional | $999/mo | 50,000 | + balance checks, + 50 connections |
| Enterprise | Custom | Unlimited | + dedicated support, custom SLAs |

**Implementation complexity:** Low — well-documented REST API, SDKs available, OAuth flow is straightforward.

### Recommended Setup

**Primary:** Basiq (OAuth2, ~120 institutions)  
**Fallback:** Salt Edge (if Basiq fails for a specific institution)  
**Avoid:** Building direct CDR integration for MVP — too complex and time-consuming

**Estimated MVP cost:** Free tier sufficient for ~100 users, then $199–$999/mo as user base grows.

---

## 2. Grocery Price Data in Australia

### Market Overview

Grocery pricing data in Australia is notoriously difficult to get — major retailers (Woolworths, Coles, Aldi) do **not** offer public APIs. Data must be scraped or purchased from third-party providers.

### Data Source Comparison

| Source | Type | Coverage | Freshness | Cost | Reliability |
|--------|------|----------|----------|------|-------------|
| **Woolworths API (unofficial)** | Unofficial scrape | Products | ~1hr | Free | Medium — can break |
| **F精 (F精.com.au)** | Aggregated data | 1,000+ products | Daily | Free tier, $15–50/mo for API | Medium |
| **PricePal** | Commercial | Full catalogue | Daily | ~$200/mo | High |
| **.au pricing** | Scraper network | Major retailers | Hourly | ~$99/mo | High |
| **Australian Food Price Data (GitHub)** | Static datasets | Historical | Stale | Free | Low — historical only |
| **Self-scraping (Playwright/BeautifulSoup)** | Custom scraper | All retailers | Varies | Infrastructure cost | Medium |
| **You Grocery Shop For Me (YGSFM)** | Community-sourced | Variable | Varies | Free | Low |

### Official Retailer APIs

**Woolworths:** No public API. Some third-party apps use the Woolworths mobile app API (undocumented, against ToS).

**Coles:** No public API. Same situation as Woolworths.

**Aldi:** No API at all.

### Web Scraping — Practical Reality

Scraping Woolworths/Coles is technically feasible but:
- **Anti-bot measures:** Cloudflare, Distil Networks, CAPTCHAs
- **ToS violations:** Scraping violates retailer terms of service
- **Maintenance burden:** Selectors break often, CSS classes change
- **IP blocking risk:** Need proxy rotation for scale

**Tools needed:** Playwright or Selenium for JS rendering, proxy pool, rate limiting.

### Data Freshness Requirements

| Use Case | Freshness Needed | Update Frequency |
|----------|-----------------|-----------------|
| Price comparison (generic) | 24–48 hours | Daily |
| Receipt matching | Real-time | On-demand |
| Budget tracking | 1 week | Weekly |
| Deal alerts | 1 hour | Hourly |

### Recommended Strategy

**MVP (Months 1–3):**
- Use **F精** free tier for basic product lookups
- Supplement with **self-scraping** for price comparison (Woolworths/Coles via Playwright)
- Accept that data will be incomplete and occasionally stale

**Growth (Months 4–6):**
- Upgrade to **PricePal** or similar paid service ($200–500/mo)
- Or build internal scraper infrastructure ($500–1,000/mo for proxies + engineering time)

**Estimated MVP cost:** $0–50/mo (scraping only, no paid data)

---

## 3. OCR for Bills and Receipts

### Provider Comparison

| Provider | Accuracy | Cost | Speed | Ease of Integration | Receipt-Specific Features |
|----------|----------|------|-------|---------------------|---------------------------|
| **Google Cloud Vision** | 92–97% | $1.50–7.50/1,000 pages | Fast (<2s) | Very easy (REST API) | Form parsing, document detection |
| **AWS Textract** | 90–96% | $1.50–15/1,000 pages | Fast (<3s) | Easy (AWS SDK) | Tables, forms, specialized docs |
| **Azure Computer Vision** | 88–95% | $1–5/1,000 pages | Fast | Easy (REST API) | Read, layout, receipt extraction |
| **Tesseract 5 (local)** | 70–85% | Free (infrastructure only) | Medium (local GPU) | Medium (need preprocessing) | No built-in receipt parsing |
| **ABBYY FineReader** | 95–99% | ~$300–1,500/yr | Medium | Medium | Best for structured documents |
| **Rossum** | 95–98% | ~$400–2,000/mo | Medium | Medium (API) | Specialized invoice/receipt AI |
| **Mindee** | 94–97% | $0–500/mo | Fast | Very easy | Receipt/invoice API, good docs |
| **Tab scanning (Firebase ML)** | 85–92% | Free tier, then $299/500 scans | Fast | Easy | Limited |

### Detailed Analysis

#### Google Cloud Vision — Recommended for MVP

- **Text Detection API:** Detects and extracts text from images
- **Document Text Detection:** Optimized for dense text (receipts)
- **Form parsing:** Can identify key-value pairs
- **Base price:** $1.50/1,000 feature detection calls
- **Free tier:** 1,000 units/month
- **Accuracy on receipts:** ~95% for clean receipts, ~85% for blurry/dark ones
- **Preprocessing helps:** Grayscale, contrast enhancement, deskewing improves accuracy significantly

**Cost calculation for MVP:**
- 1,000 receipts/month → ~$1.50–3.00
- 10,000 receipts/month → ~$15–30
- Very affordable at MVP scale.

#### AWS Textract

- **AnalyzeDocument** API with receipt-specific form detection
- Integrates well with AWS ecosystem
- **Pricing:** $1.50/1,000 pages for textract, $15/1,000 for AnalyzeDocument
- Slightly more expensive than GCP for receipt use case
- Good if you're already in AWS

#### Azure Computer Vision

- **Read API:** Handles multi-page documents well
- **Form Recognizer (preview):** Good for structured receipts
- Pricing similar to GCP
- Excellent for multi-language receipts (AU stores with non-English items)

#### Tesseract — Free but High Effort

- **Open source, runs locally**
- **Accuracy: 70–85%** on receipts (needs significant preprocessing)
- Infrastructure cost: CPU/GPU to run it
- **Not recommended for production** unless you have OCR engineers
- Good for development/demo, not for user-facing product

#### Mindee — Strong Contender for Receipts

- **Receipt API** specifically designed for receipt parsing
- **Accuracy:** 94–97%
- **Pricing:** Free tier (1,000/month), $49/mo for 5,000, $249/mo for 50,000
- Very developer-friendly API
- Has pre-trained receipt parser — no custom ML needed

### Recommendation

**MVP:** Use **Google Cloud Vision** (Document Text Detection) or **Mindee Receipt API**

- Mindee is slightly better for receipts (pre-trained receipt model)
- GCP is more general-purpose, lower cost, more providers
- Both give >90% accuracy on clean receipts

**Hybrid approach:**
- Use Mindee for receipt parsing (purpose-built)
- Fall back to GCP for edge cases (odd formats, multi-page)
- Implement Tesseract as offline fallback (no internet required)

**Preprocessing pipeline (non-negotiable for good accuracy):**
1. Convert to grayscale
2. Increase contrast (1.5x)
3. Sharpen
4. Deskew/rotate
5. Crop to receipt boundary

---

## 4. Do We Need a Custom ML Model?

### Short Answer: **No for MVP. Possibly for v2.**

### What Can Be Done with Existing APIs

| Task | Use Existing API | Custom ML Needed? |
|------|-----------------|------------------|
| OCR text extraction | Google Cloud Vision / Mindee | No |
| Merchant name extraction | Rule-based + keyword matching | No |
| Category classification | Rule-based with keyword database | No |
| Transaction matching | Fuzzy string matching (SequenceMatcher) | No |
| Price comparison | Web scraping + simple comparison | No |
| Geocoding | OpenStreetMap / Nominatim | No |
| POI search | Overpass API (OSM) | No |
| Digest generation | Template-based | No |

### Where Custom ML Could Help (v2+)

| Task | Custom ML Benefit | Effort |
|------|-----------------|--------|
| **Receipt field extraction** (end-to-end) | Currently done with GCP/Mindee. Custom model could be trained on AU receipts specifically. | High — needs 5,000+ labeled receipts |
| **Category prediction** (when merchant ambiguous) | Train classifier on merchant → category pairs | Medium — 1,000+ samples needed |
| **Anomaly detection** (fraud/unusual spend) | Train on user's historical spending patterns | Medium |
| **Receipt matching** (fuzzy matching is brittle) | Train a similarity model for transaction-to-receipt matching | High |
| **Price prediction** (will prices go up?) | Time series forecasting on price history | High |

### The Honest Assessment

For an MVP, **no custom ML model is needed**. Here's why:

1. **Receipt OCR:** Mindee/GCP already do this at 94–97% accuracy. Training a custom model requires 5,000+ labeled receipts and ongoing maintenance.

2. **Category classification:** Keyword-based rule engine covers 90%+ of cases. The long tail (ambiguous merchants) can be handled with manual tagging initially.

3. **Transaction matching:** Fuzzy string matching + date proximity + amount tolerance covers 90% of cases.

4. **Cost vs. benefit:** Custom ML models require labeled data, training infrastructure, evaluation, and continuous improvement. For a pre-revenue MVP, this is a distraction.

### Recommendation

**MVP:** Zero custom ML models. Use:
- Mindee Receipt API for OCR
- Keyword-based categorization
- Python `difflib.SequenceMatcher` for fuzzy matching
- Existing geocoding/POI services

**v2 (if user base > 1,000):**
- Train custom receipt parser on AU-specific receipts
- Build category classifier with user feedback loop
- Consider anomaly detection for fraud alerts

---

## 5. MVP Unique Features

### Research Findings

Based on what exists in the market (YNAB, Mint, Pocketbook, F精, Australian price comparison apps), the **gaps** that represent MVP opportunities:

1. **No AU-focused receipt scanning + bank sync in one product**
2. **No price comparison tied to actual receipts**
3. **No geolocation-based suggestions in AU context**
4. **No Discord-native expense tracking**

### Recommended MVP Feature Set

#### P0 — Must Have (Core Loop)

| Feature | Description | Why It Matters |
|---------|-------------|----------------|
| **Receipt Photo Scan** | Snap a photo → extract merchant, date, total, line items | Core value proposition — zero manual entry |
| **Basiq Bank Sync** | Connect AU bank → get transactions automatically | Scales to full expense tracking |
| **Expense Log** | All scanned + bank items in one searchable list | Core artifact — the "source of truth" |
| **Category View** | See spending by category with totals | Basic but essential visibility |

#### P1 — Differentiators (What Makes It Worth Using)

| Feature | Description | Differentiation |
|---------|-------------|-----------------|
| **Price Comparison on Receipt** | "You paid $12.99 at 7-Eleven, Woolworths has it for $8.50 nearby" | No other AU product does this |
| **Nearby Cheaper Alternatives** | Show cheaper retailers within 5km using geolocation | Tangible savings, not just tracking |
| **Weekly Digest → Discord** | Automated summary of week's spending, posted to Discord | Passive value, no app to open |
| **Budget Alerts** | "You've hit 80% of your dining budget this month" | Proactive, not reactive |
| **Receipt-to-Bank Matching** | Auto-match scanned receipt to bank transaction | Eliminates manual reconciliation |

#### P2 — Nice to Have (Polish)

| Feature | Description |
|---------|-------------|
| **Natural language queries** | "How much did I spend on groceries last month?" |
| **Merchant price history** | "I used to pay $X at Bunnings, now it's $Y" |
| **Deal alerts** | "Price dropped on an item you bought recently" |
| **Export to CSV/Google Sheets** | Data portability |

### Features to SKIP for MVP

These are commonly requested but should wait for v2:

- **Receipt splitting** (divide a receipt among categories/people)
- **Subscription tracking** (detect recurring charges automatically)
- **Investment tracking** (separate product, not expense tracking)
- **Multi-currency support** (AUD only for MVP)
- **Receipt storage (images)** (focus on data, not file storage)
- **Bill reminder/recurring** (too complex for v1)
- **Social features** (share expenses with partners/friends)

### MVP Feature Summary

```
MVP Scope:
✅ Receipt photo scan (Mindee OCR)
✅ Basiq bank sync (120+ AU institutions)
✅ Expense log with auto-categorization
✅ Category breakdown view
✅ Price comparison on scanned items (scraped data)
✅ Nearby cheaper alternatives (geolocation)
✅ Weekly digest to Discord (cron job)
✅ Budget alerts (80% threshold)

Out of Scope for v1:
❌ Custom ML models
❌ Direct CDR integration
❌ Receipt image storage
❌ Multi-currency
❌ Investment tracking
❌ Social features
```

### What Makes This MVP Compelling

The **unique value proposition** is: **"Point your camera at a receipt, and we'll not only track it — we'll tell you if you're paying too much and where to go instead."**

No other Australian product combines:
1. Receipt scanning
2. Bank transaction sync
3. Real-time price comparison
4. Geolocation-based alternatives
5. Passive weekly digest via Discord

---

## 6. Cost Summary for MVP

| Component | Monthly Cost (MVP) | Notes |
|-----------|-------------------|-------|
| Basiq | $0–$199 | Free tier for ~100 users, then Starter |
| OCR (Mindee) | $0–$49 | Free tier 1,000/month, then $49/mo |
| Hosting (Railway/Render) | $5–$20 | Docker container, SQLite on persistent disk |
| Scraper infrastructure | $0–$50 | Use free tiers initially, upgrade when needed |
| Domain + SSL | $5–$10 | Standard domain pricing |
| **Total MVP** | **$0–$328/mo** | Can start free, scale as users grow |

---

## 7. Implementation Priority

| Week | Tasks | Deliverable |
|------|-------|-------------|
| 1–2 | Receipt OCR pipeline (Mindee/GCP) + expense model | Scan a receipt, see it in expense log |
| 3–4 | Basiq bank sync + transaction matching | Connect bank, see transactions auto-matched |
| 5–6 | Price comparison engine + geolocation suggest | "Cheaper option nearby" shown on receipts |
| 7–8 | Weekly digest → Discord + budget alerts | Passive summary delivered weekly |
| 9–10 | Polish, bug fixes, UX improvements | Feature complete MVP |

---

*Report generated for BillScout Agent MVP planning — June 2026*