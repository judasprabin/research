# BillScout Agent

> AI-powered personal finance agent — scan bills, sync bank transactions, track expenses, find better prices nearby.

## Features

- 📷 **Receipt OCR** — Snap a photo, get structured expense data
- 🏦 **Bank Sync** — Connect via Basiq (120+ AU institutions) or Plaid
- 💰 **Expense Tracking** — Auto-categorized, tagged, budget-tracked
- 🏷️ **Price Comparison** — See if you're paying too much and find cheaper alternatives nearby
- 📊 **Weekly Digests** — Automated summaries delivered to Discord

## Tech Stack

- **Agent:** Hermes Agent (subagent-driven)
- **OCR:** Tesseract / Google Cloud Vision
- **Open Banking:** Basiq API (AU), Plaid (international)
- **DB:** SQLite (dev) / PostgreSQL (prod)
- **Price Data:** Web scrapers + public price APIs
- **Geocoding:** OpenStreetMap / Nominatim

## Quick Start

```bash
# Clone & enter
git clone https://github.com/your-org/bill-scout-agent.git
cd bill-scout-agent

# Copy env and fill in keys
cp .env.example .env

# Start with Docker
docker compose up -d

# Or local dev
pip install -r requirements.txt
python scripts/init_db.py
python -m src.agent
```

## Project Structure

```
bill-scout-agent/
├── skills/          # Attach to Hermes for each capability
├── src/             # Python source
│   ├── agent.py     # Main orchestrator
│   ├── ocr/        # Receipt scanning
│   ├── bank/        # Bank sync (Basiq/Plaid)
│   expenses/       # Expense models + repo
│   ├── price/       # Price scraping + comparison
│   └── geo/         # Geocoding + POI lookups
├── tests/           # Unit + integration tests
└── docs/            # API docs, deployment guide
```

## Documentation

- [PRD](./2026-06-02-BillScout-PRD.md) — Full product spec
- [API Docs](./docs/api.md)
- [Bank Setup](./docs/bank-setup.md)
- [Deployment](./docs/deployment.md)

## Status

**Current:** Planning / M1 not started

**Roadmap:** See PRD milestones
