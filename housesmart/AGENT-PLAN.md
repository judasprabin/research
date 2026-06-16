# 🤖 HOUSESMART AI AGENT — 72-HOUR ACTION PLAN

**Status:** Ready to build  
**Date:** 2026-06-03  
**Goal:** Functional AI agent prototype that reads receipts and returns multi-module insights

> **Scope note (read before starting):** this is a **throwaway research prototype**,
> not a first slice of the production app. It exists to de-risk two unknowns before
> committing engineering budget: (1) does multi-source enrichment (price + nutrition)
> actually produce insights good enough to be worth shipping, and (2) which of the
> data sources in `data-discovery-strategy.md` are realistically usable. It is a
> Python script, not React Native/Supabase, and its code is not meant to be carried
> forward — only its *findings* are. See "How this feeds the real build" at the end
> of this document for exactly how prototype output maps to `roadmap.md` /
> `TODO.md` engineering tasks. Do not let this prototype's stack choices (Python,
> ad-hoc scrapers, no DB) leak into production architecture decisions, which are
> owned by `technical-architecture.md`.

---

## 🎯 Why HouseSmart + AI Agents?

AI agents are **perfect** for HouseSmart because:

1. **Multi-step reasoning:** Receipt → OCR → Price check → Nutrition → Bank reconciliation → Insights
2. **Real-time data integration:** Agent can query Woolworths API, Open Food Facts, ABS simultaneously
3. **Adaptive behavior:** Learn from user corrections to improve extraction accuracy
4. **Natural language output:** "You're overpaying 12% vs ALDI for milk. This week you're low on Iron — add spinach"

---

## 📊 Data Sources Status

### ✅ READY NOW
- **Open Food Facts API** — Barcode → Nutrition data
- **ABS Public Data** — Demographics + consumption benchmarks

### ⚠️ NEEDS 1-2 HOURS
- **Woolworths Prices** — Reverse-engineer API or contact
- **Coles Scraper** — Build Selenium scraper
- **ALDI Circular** — Parse HTML or contact

### 🚀 ALREADY PLANNED
- **Basiq CDR** — Open Banking (in your roadmap)

---

## 🛠️ 72-HOUR BUILD PLAN

### Day 1: Foundation (6-8 hours)

**Goal:** Standalone modules working independently

1. **Module Setup** (2h)
   ```bash
   mkdir housesmart-agent
   python3 -m venv venv
   pip install anthropic openai supabase python-dotenv requests
   ```

2. **Smart Scan Module** (1h)
   - Use Claude Vision to extract receipt items
   - Parse: merchant, date, items[], quantities, prices
   - Test with 2-3 sample receipts

3. **Nutrition Module** (2h)
   - Integrate Open Food Facts API
   - Test: barcode → macros/micros
   - Build fallback for unmatched items (category averages)

4. **ABS Integration** (1h)
   - Query household consumption data
   - Build consumption benchmarks (target macros/micros)

**Deliverable:** 3 working modules, tested individually

---

### Day 2: Agent Loop + Price Integration (6-8 hours)

**Goal:** Agent orchestrates modules + price data flows

1. **Price Scout Module** (3h)
   - Build Woolworths API scraper (or reverse-engineer)
   - Test price lookup for 10 common items
   - Fallback: historical prices from user receipts

2. **Agent Orchestration** (3h)
   ```python
   # Pseudocode
   agent = HouseSmart(claude_client, data_sources)
   
   for receipt_image in test_receipts:
       insight = agent.analyze(receipt_image)
       # insight.groceries → Module 2 (repurchase)
       # insight.prices → Module 3 (savings)
       # insight.nutrition → Module 4 (diet)
   ```

3. **End-to-End Test** (1h)
   - Run agent on 1 receipt
   - Verify all 4 insights appear
   - Debug any failures

**Deliverable:** Functional agent loop, real receipt → 4 outputs

---

### Day 3: Polish + Documentation (4-6 hours)

**Goal:** Ready to demo / hand off to dev team

1. **Test Suite** (2h)
   - 5 receipts (Woolworths, Coles, ALDI, supermarket, pharmacy)
   - Validate accuracy per module
   - Document edge cases

2. **Error Handling** (1h)
   - Graceful failures (missing barcode, blocked API, etc.)
   - Fallback strategies

3. **Documentation** (2h)
   - Agent architecture diagram
   - Data flow chart
   - Integration guide for dev team
   - Roadmap for Phases 2-3 (Money Map, Repurchase Prediction)

**Deliverable:** Polished agent, docs, test results

---

## 💻 Code Structure

```
housesmart-agent/
├── agent.py              # Main Claude agent loop
├── modules/
│   ├── __init__.py
│   ├── scan.py          # Vision-based receipt parsing
│   ├── nutrition.py     # Barcode → Open Food Facts
│   ├── prices.py        # Woolworths/Coles/ALDI lookup
│   └── money_map.py     # Bank data (Phase 2)
├── data_sources/
│   ├── open_food_facts.py
│   ├── abs_data.py
│   ├── woolworths.py
│   ├── coles.py
│   └── aldi.py
├── tests/
│   ├── test_receipts/   # Sample images
│   └── test_agent.py
├── .env.example
└── README.md
```

---

## 🚀 Success Criteria

✅ Agent receives receipt image  
✅ Extracts 10+ line items correctly  
✅ Looks up prices for 8/10 items  
✅ Calculates nutrition profile  
✅ Returns 4-insight output:
- "You bought milk for $3.50 (usually $4.20 — good deal!)"
- "Predicts you need milk again in ~5 days"
- "Your weekly nutrition: 15% low on Iron"
- "Weekly spend on groceries: $142"

---

## 📝 Next Steps (For You)

1. **Decide:** Start Day 1 or gather more requirements?
2. **Resources:** Do you have Claude API key + Basiq ready?
3. **Team:** Building solo or bringing in dev partner?
4. **Timeline:** Start this week or next?

---

## 💡 Product Advice

**This MVP is NOT the full HouseSmart.** It's proof:
- ✅ AI agents can integrate multiple data sources
- ✅ Receipt parsing + enrichment works
- ✅ Users see real value immediately (Price Scout alone is valuable)
- ✅ You can collect real usage data to guide full build

After successful 72h prototype, next prioritization:
1. **Money Map** (Open Banking) — Most valuable for retention
2. **Repurchase Prediction** — Keeps users returning
3. **Nutrition Alerts** — Differentiator vs competitors

---

**Ready to build?** 🚀

---

## How This Feeds the Real Build

The prototype's job is to produce evidence, not code. Concretely:

| Prototype output | Feeds into |
|---|---|
| Receipt extraction accuracy per store (Woolworths/Coles/ALDI/pharmacy) | Validates or revises the ≥92%/≥80% accuracy targets in `PRD.md` §2 Module 1 and the Phase 0 exit criteria in `roadmap.md` |
| Whether Woolworths/Coles price lookups are reliably accessible | Go/no-go input for `data-discovery-strategy.md` §"Top 3 to Research" — if scraping proves unreliable or legally risky (see that doc's updated legal-risk notes), Price Scout's Phase 1 plan in `PRD.md` §2 Module 3 must fall back to "from your own scan data only" sooner than planned |
| Open Food Facts AU coverage on real receipts | Confirms or revises the ≥85% packaged-food match assumption in `PRD.md` §2 Module 4 |
| Claude prompt that reliably returns valid structured JSON | Becomes the starting point (not final version) for the production prompt in `technical-architecture.md` §2, "Claude Extraction Prompt (v1)" |
| Edge cases hit during the 5-receipt test suite | Should be added to the edge-case tables in `PRD.md` §2A before engineering scopes Phase 1 |

**Explicitly out of scope for this prototype, deferred to the real build:** auth,
persistence beyond local test files, RLS/security, retry/idempotency logic, any UI.
Building those here would be wasted effort — they belong to the Supabase/React
Native stack in `technical-architecture.md`.

