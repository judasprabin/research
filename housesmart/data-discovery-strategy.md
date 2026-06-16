# 🎯 HouseSmart AI Agent — Data Discovery Strategy

**Date:** 2026-06-03  
**Goal:** Identify which open Australian data sources can power HouseSmart modules  
**Timeline:** 48-72 hours to prototype agent loop

---

## 📋 HouseSmart Modules → Required Data

### Module 1: Smart Scan (Core)
**What it needs:** Receipt OCR + Structured extraction  
**Data sources:** NONE (built with Google Cloud Vision + Claude LLM — no external data)  
**Status:** ✅ Already architected

---

### Module 2: Grocery Brain (Purchase History + Repurchase Prediction)
**What it needs:**
- Historical grocery receipt data (for pattern learning)
- Typical purchase intervals by product type (to train repurchase predictor)

**Candidate data sources:**
| Source | Data | Usefulness | Why |
|--------|------|-----------|-----|
| NSW Open Data | Supermarket locations + permit data | ⭐⭐ | Only schema, not purchases |
| Consumer surveys | Typical grocery purchase patterns | ⭐⭐⭐ | Good for initialization |
| CSIRO Food/Agri data | Seasonal produce patterns | ⭐⭐⭐ | Helps predict fresh items |
| ABS Economic data | Household consumption by category | ⭐⭐⭐ | Can set priors |

**Best path:** Start with **user-collected data** (agent learns from scans) + seed from **ABS consumption patterns**.

---

### Module 3: Price Scout (Cross-Store Price Intelligence)
**What it needs:**
- Real-time supermarket prices
- Historical pricing trends
- Store locations + postcodes

**Candidate data sources:**
| Source | Data | Usefulness | Why | Access |
|--------|------|-----------|-----|--------|
| **Woolworths Price API** | Real-time prices + weekly specials | ⭐⭐⭐⭐⭐ | Official, fresh | Public (no auth) |
| **Coles Price Scraper** | Shelf prices (requires web scraping) | ⭐⭐⭐⭐⭐ | Complete coverage | Scrape from coles.com.au |
| **ALDI Pricing** | Weekly circular data | ⭐⭐⭐⭐ | Direct + accurate | ALDI publishes HTML |
| **NSW Open Data** | Supermarket locations | ⭐⭐⭐ | Merchant addresses | API available |
| **DataVic** | Victoria supermarket locations | ⭐⭐⭐ | Merchant addresses | API available |
| **Google Maps** | Store locations + hours | ⭐⭐⭐⭐ | Fallback for IGA/independent | Google Places API |
| **ABS Inflation Data** | CPI by food category | ⭐⭐ | Historical context | Public |

**Best path:** **Woolworths + Coles + ALDI scraping** = 75% of market. Use **NSW/VIC portals for merchant schemas**.

> ⚠️ **Legal risk note — read before building any scraper.** Web scraping
> Coles/ALDI shelf prices and any undocumented use of a Woolworths internal/public
> endpoint sits in a legal grey area: most retailer sites' Terms of Use prohibit
> automated scraping outright, and unauthenticated access to a non-public API can
> implicate the Copyright Act and, in aggressive cases, unauthorised-access
> provisions of the Criminal Code Act. Treat this as a **decision the founder must
> make explicitly, not a default engineering choice**:
> - Before building any scraper, check the target site's `robots.txt` and Terms of
>   Use, and prefer an official affiliate/data feed if one exists (ask Woolworths/
>   Coles developer relations directly — some retailers offer affiliate product
>   feeds with broader usage rights than scraping).
> - Treat any production-facing Price Scout feature built on scraped data as a
>   **build risk to revisit before Phase 2 launch** (`roadmap.md` 2.1), not a settled
>   architecture decision — a cease-and-desist or IP block would remove the feature
>   entirely with no fallback unless the "from your own scan data" path (already the
>   Phase 1 design in `PRD.md` §2 Module 3) is fully functional independently.
> - The 72-hour prototype (`AGENT-PLAN.md`) is the place to validate feasibility and
>   risk cheaply — do not invest in scraper reliability/scale until a legal read is
>   done.

---

### Module 4: Nutrition Lens (Diet Analysis)
**What it needs:**
- Product nutrient databases (barcode → macros + micronutrients)
- Australian Dietary Guidelines (ADG) recommendations
- Food substitutes / alternatives

**Candidate data sources:**
| Source | Data | Usefulness | Why | Access |
|--------|------|-----------|-----|--------|
| **Open Food Facts** | Global food database + barcodes | ⭐⭐⭐⭐⭐ | 1M+ products, AU coverage | Free API |
| **USDA FoodData Central** | Nutrient profiles for generic foods | ⭐⭐⭐⭐ | Fresh produce + backup | Free API |
| **ABS Health Data** | ADG-compliant recommendations | ⭐⭐⭐⭐ | Official AU guidelines | Public data |
| **NCCR (Nutrient Content)**| AU food composition | ⭐⭐⭐ | Hyperlocal accuracy | Limited access |
| **CQLR Database** | AU commercial foods | ⭐⭐ | Retail-specific | Academic |

**Best path:** **Open Food Facts (primary)** + **USDA FoodData (fresh produce fallback)** + **ABS guidelines (targets)**.

---

### Module 5: Money Map (Open Banking + Full Expense Tracking)
**What it needs:**
- Bank transaction categories + descriptions
- Merchant master data
- Utility/subscription pricing baselines

**Candidate data sources:**
| Source | Data | Usefulness | Why |
|--------|------|-----------|-----|
| **Open Banking (CDR)** | Bank transactions | ⭐⭐⭐⭐⭐ | Core requirement — use Basiq SDK |
| **Basiq** | 120+ AU institutions + categorization | ⭐⭐⭐⭐⭐ | Already categorizes transactions |
| **ABS CPI Data** | Average household utility costs | ⭐⭐⭐ | Set expectations for "normal" |
| **data.gov.au Utilities** | Energy rebate + pricing data | ⭐⭐ | Reference data |

**Best path:** **Basiq CDR (already in your roadmap)** + **ABS baselines for anomaly detection**.

---

## 🚀 **PRIORITY RANKING: What to Focus on FIRST**

### Phase 1 (Week 1): Data Source Assessment
**Goal:** Validate which sources are accessible and fresh enough

#### Top 3 to Research Immediately:

1. **Woolworths Price API** 
   - ✅ Public access (no auth needed)
   - ✅ Real-time prices
   - ❓ **Action:** Test data freshness + coverage
   - 📍 **Time:** 2 hours to validate

2. **Open Food Facts API**
   - ✅ Free API with Australian product data
   - ✅ 1M+ products + nutrient data
   - ❓ **Action:** Check AU barcode coverage
   - 📍 **Time:** 2 hours to test integration

3. **ABS APIs** (Census + Consumption Data)
   - ✅ Official, authoritative
   - ✅ State-level breakdowns for NSW/VIC
   - ❓ **Action:** Understand data latency + structure
   - 📍 **Time:** 3 hours to explore

---

## 🤖 **AI AGENT Architecture (HouseSmart Agent)**

Your agent should run these loops in this order:

```
┌─────────────────────────────────────────────┐
│  HOUSESMART AI AGENT                        │
├─────────────────────────────────────────────┤
│                                             │
│  1. User uploads receipt image              │
│     ↓                                        │
│  2. [Claude Vision] → Extract line items    │
│     ↓                                        │
│  3. [Agent Loop A] Grocery Brain            │
│     • Check historical patterns (user DB)   │
│     • Predict repurchase dates              │
│     ↓                                        │
│  4. [Agent Loop B] Price Scout              │
│     • Query Woolworths API                  │
│     • Query Coles scraper                   │
│     • Compare ALDI prices                   │
│     ↓                                        │
│  5. [Agent Loop C] Nutrition Lens           │
│     • Barcode → Open Food Facts             │
│     • Calculate macros/micros               │
│     • Compare to ABS guidelines             │
│     ↓                                        │
│  6. [Agent Loop D] Money Map                │
│     • Fetch user's Open Banking data (CDR)  │
│     • Reconcile receipt ↔ bank transaction  │
│     • Detect anomalies vs ABS baselines     │
│     ↓                                        │
│  7. Return consolidated insight to user     │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 📊 **Data Quality Checklist**

For each data source, validate:

- [ ] **Freshness:** How often updated?
- [ ] **Coverage:** NSW/VIC full coverage?
- [ ] **Accuracy:** Match your quality bars?
- [ ] **API Latency:** Response time < 500ms?
- [ ] **Cost:** Free/paid/rate-limited?
- [ ] **Terms:** Can you use in production?

---

## 🎯 **Recommended 72-Hour Sprint**

### Day 1: Validate Top 3 Sources
1. **Woolworths API** — Pull 50 products, check schema
2. **Open Food Facts** — Search 20 AU barcodes, test nutrient extraction
3. **ABS API** — Query consumption patterns NSW/VIC

### Day 2: Data Pipeline Proof of Concept
1. Build **Price Scout** pipeline (Woolworths → Agent → User)
2. Build **Nutrition Lens** pipeline (Barcode → Open Food Facts → Agent → User)
3. Test with a single receipt

### Day 3: Agent Integration Test
1. Connect **Claude API** to loop through all 4 data sources
2. Run **end-to-end test:** Receipt → Agent → 4 insights
3. Document findings + next steps

---

## 📝 **Final Recommendation**

**DON'T browse all 14 data sources.** Focus on **these 5 ONLY** for HouseSmart:

1. **Woolworths Price API** (public)
2. **Open Food Facts API** (free)
3. **ABS Data APIs** (free)
4. **Coles web scraper** (legal grey area — validate first)
5. **Basiq CDR** (already budgeted)

**Everything else is secondary.** This 72-hour focus will unblock your agent prototype.

---

## 💡 **Why Product-First Wins Here**

✅ You already have **HouseSmart defined** → clear data requirements  
✅ You can **validate with real data** in 48 hours  
✅ You can **build & iterate** with customers immediately  
✅ You avoid **analysis paralysis** on 100K datasets  

**Next step:** Pick one module (suggest **Grocery Brain**), find 2-3 data sources, build agent loop, test with real receipt. 🚀

**Default fallback if scraping is ruled out or blocked:** Price Scout ships with
"savings from your own scan data only" (already the Phase 1 design) as the
permanent baseline, with crowdsourced opt-in pricing (`roadmap.md` 3.1) as the
scalable long-term replacement for scraping — not a stopgap, but the actual
intended Phase 3 architecture regardless of how the scraping question resolves.
