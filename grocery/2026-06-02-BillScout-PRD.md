# BillScout Agent — Product Requirements Document

> **Version:** 0.1.0  
> **Date:** 2026-06-02  
> **Author:** Prabin Karki  
> **Platform Target:** Sydney/Melbourne/Perth, Australia (AUD)

---

## 1. Concept & Vision

**BillScout** is an AI-powered personal finance agent that eliminates manual expense tracking. Take a photo of any bill or receipt, and the agent parses it, enriches it with merchant data, syncs it against your bank transactions, and surfaces actionable insights — like when you're overpaying for something and a better option exists nearby.

The experience is frictionless: point, shoot, done. No manual entry. No spreadsheets. Just clarity.

---

## 2. Core Features

### 2.1 Bill Photo Scanning & OCR

- **Input:** Camera photo or gallery image of a bill/receipt
- **Processing:**
  - Receipt localization + perspective correction (deskew)
  - OCR via Tesseract or cloud vision (Google Cloud Vision / Azure Computer Vision)
  - Field extraction: merchant name, date, total, line items, tax, tip
- **Output:** Structured `ExpenseRecord` with confidence scores
- **Fallback:** Manual correction UI if confidence < 85%

### 2.2 Bank Transaction Sync

- **Australia-focused integrations:**
  - **Basiq** — Open Banking API (120+ financial institutions)
  - **Plaid** — international, some AU coverage
  - **Salt Edge** — open banking for AU/EU
- **Sync behavior:**
  - Auto-categorize transactions (food, transport, utilities, etc.)
  - Match scanned receipts against bank transactions (fuzzy + exact matching)
  - Flag unmatched transactions for review
- **Security:** OAuth2 + bank-grade encryption; no credential storage

### 2.3 Expense Tracking & Categorization

- **Categories:** groceries, dining, transport, utilities, entertainment, healthcare, shopping, travel, subscriptions, other
- **Tags:** custom user tags + AI-suggested tags
- **Budget tracking:** monthly budgets per category with alerts at 80%/100%
- **Reports:** weekly/monthly summaries, trend charts

### 2.4 Price Comparison & Nearby Suggestions

- **Merchant intelligence:** Look up the recognized merchant name and location
- **Price database:** Aggregate from:
  - Public price APIs (Supie, GroceryHunter AU, AusFoodPrices)
  - Web scraping for major retailers (Woolworths, Coles, Aldi, IGA)
  - User-contributed prices (privacy-preserving)
- **Nearby suggestions:**
  - Reverse geocode user's location (OpenStreetMap/Nominatim)
  - Query POI (points of interest) for cheaper alternatives within radius
  - Push notification or in-app card: "You bought X at $Y here, but Z has it for $Y-20% nearby"
- **Distance:** Configurable radius (default 5km, max 20km)

### 2.5 AI Agent Workflow

- Orchestrated by a ** Hermes subagent** (or equivalent orchestrator)
- **Skills (attachable):**
  - `receipt-ocr` — image → structured data
  - `bank-sync` — bank API → transactions
  - `expense-tracker` — CRUD + categorization
  - `price-lookup` — merchant/product price query
  - `geolocation-suggest` — nearby alternatives
  - `weekly-digest` — summary report generation
- **Conversation interface:** Natural language queries ("How much did I spend on groceries last month?", "Show me my biggest expense categories this quarter")

---

## 3. User Flows

### 3.1 Scan a Bill
```
User snaps photo → Agent extracts fields → User confirms/edits → Saved to expense log → Matched against bank transactions → Categorized
```

### 3.2 Bank Connection
```
User selects bank → OAuth redirect → Agent receives access token → Initial sync → Periodic background sync (daily)
```

### 3.3 Price Suggestion
```
User scans receipt → Merchant identified → Price looked up → If cheaper alternative within radius → Suggestion card shown
```

### 3.4 Weekly Digest
```
Scheduled job (cron) → Aggregate week's transactions → Generate summary → Post to Discord #job_market channel (or configurable)
```

---

## 4. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    BillScout Agent                          │
├──────────────┬──────────────┬──────────────┬───────────────┤
│  Receipt OCR │  Bank Sync   │  Expense     │  Price Engine │
│  (Vision API │  (Basiq/Plaid│  Tracker     │  (Scrapers +  │
│  / Tesseract)│  / Salt Edge)│  (SQLite/PG) │  POI queries) │
└──────┬───────┴──────┬───────┴──────┬───────┴───────┬───────┘
       │              │              │               │
       └──────────────┴──────────────┴───────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   Orchestrator     │
                    │  (Hermes subagent) │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │   Discord Bot UI   │
                    │  (BillScout home)  │
                    └───────────────────┘
```

---

## 5. Tech Stack

| Component | Technology |
|-----------|------------|
| Agent framework | Hermes Agent (subagent-driven) |
| OCR | Tesseract (local) or Google Cloud Vision |
| Open Banking | Basiq API (AU-native) |
| Database | SQLite (local dev), PostgreSQL (prod) |
| Price scraping | BeautifulSoup + Selenium/A Playwright |
| Geocoding | OpenStreetMap / Nominatim |
| Maps/POI | Overpass API (OSM) or Google Places |
| Deployment | Docker + Railway / Render / Fly.io |
| CI/CD | GitHub Actions |

---

## 6. Folder Structure

```
bill-scout-agent/
├── PRD.md
├── README.md
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── skills/                          # Agent skills
│   ├── receipt-ocr/
│   ├── bank-sync/
│   ├── expense-tracker/
│   ├── price-lookup/
│   ├── geolocation-suggest/
│   └── weekly-digest/
├── src/
│   ├── __init__.py
│   ├── agent.py                     # Main orchestrator
│   ├── ocr/
│   │   ├── __init__.py
│   │   ├── processor.py
│   │   └── parser.py
│   ├── bank/
│   │   ├── __init__.py
│   │   ├── basiq_client.py
│   │   └── transaction_matcher.py
│   ├── expenses/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── repository.py
│   │   └── categorizer.py
│   ├── price/
│   │   ├── __init__.py
│   │   ├── scraper.py
│   │   └── comparator.py
│   ├── geo/
│   │   ├── __init__.py
│   │   ├── geocoder.py
│   │   └── poi_finder.py
│   └── api/
│       ├── __init__.py
│       └── routes.py                # Optional REST API
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── scripts/
│   ├── init_db.py
│   └── seed_data.py
├── docs/
│   ├── api.md
│   ├── bank-setup.md
│   └── deployment.md
└── .env.example
```

---

## 7. Milestones

| Milestone | Description | Priority |
|-----------|-------------|----------|
| M1 | Receipt OCR + field extraction (MVP) | P0 |
| M2 | Manual expense entry + SQLite storage | P0 |
| M3 | Basiq bank sync + transaction matching | P1 |
| M4 | Price lookups + nearby suggestions | P2 |
| M5 | Weekly digest → Discord delivery | P2 |
| M6 | Category budgets + alerts | P3 |
| M7 | Natural language query interface | P3 |

---

## 8. Risks & Open Questions

- **Bank API rate limits:** Basiq has per-institution rate limits; need exponential backoff
- **Receipt quality:** Blurry/receipts with heavy shadows degrade OCR accuracy — may need image preprocessing pipeline
- **Price data freshness:** Web scraping is brittle; consider official retailer APIs where available
- **Privacy:** All bank data should be encrypted at rest; consider local-only mode
- **Multi-bank:** Need to handle multiple linked accounts per user

---

## 9. Success Metrics

- Receipt scan → structured data in < 5 seconds
- Bank transaction match rate > 90%
- Price suggestion accuracy: when shown, user clicks "helpful" > 70%
- Weekly digest open rate via Discord > 60%
