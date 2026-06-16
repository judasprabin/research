---
name: housesmart
description: Use when answering questions about, editing, or extending the HouseSmart project (household financial + nutrition intelligence app) — covers product/PRD, market & competitor research, user personas, design concepts, technical architecture, GTM, financial model, roadmap, and the AI agent prototype plan. Triggers on "HouseSmart", "SmartCart", "BillScout", or requests to update/consult any of this project's research docs.
---

# HouseSmart Research Knowledge Base

HouseSmart is a household financial & nutrition intelligence app (AU market, Phase 1).
Tagline: "Scan once. Save money. Eat better." Built from the merger of two earlier
ideas: **BillScout** (bill/expense AI agent) and **SmartCart** (grocery intelligence).

Core loop: scan any receipt/bill → AI (Google Cloud Vision OCR + Claude API extraction)
→ cross-reference bank transactions → output grocery list, price savings, nutrition
gaps, and spend insights.

Five modules: **Smart Scan** (OCR/extraction core) · **Grocery Brain** (purchase
history + repurchase prediction) · **Price Scout** (cross-store price comparison) ·
**Nutrition Lens** (receipt → nutrient totals vs. Australian Dietary Guidelines) ·
**Money Map** (Open Banking via Basiq, categorisation, budgets, bill-change alerts).

## How to use this skill

All source docs live as flat `.md` files in the project root (same directory as this
skill). **Read the specific file(s) relevant to the question before answering** —
don't rely on the summary below for anything beyond a first orientation, since the
docs contain the authoritative numbers, schemas, and copy.

| File | Contents | Consult when... |
|---|---|---|
| `TODO.md` | **Prioritised engineering backlog** — phase-by-phase tasks with acceptance criteria, dependencies, estimates | Any "what should I build next" or sprint-planning question — this is the engineering entry point |
| `README.md` | Project overview, module table, key numbers, tech stack | Quick orientation, sharing project summary |
| `PRD.md` | Full requirements: 5 modules in detail, personas, NSM/KPIs, MVP scope, roadmap, monetisation tiers, risk register, compliance, §2A acceptance criteria & edge cases per module, §11 NFRs, §12 Definition of Done | Any product/feature/scope/metrics/acceptance-criteria question |
| `smartcart-original-PRD.md` | **Archived.** Original SmartCart concept doc (pre-merge) | Tracing feature origin only — do not implement against this |
| `brainstrom-original.md` | **Archived.** Raw early brainstorm bullets + provenance table of what survived | Earliest-stage idea provenance only |
| `market-research-au.md` | AU grocery + fintech + nutrition app market sizing, TAM/SAM, §9 research methodology/confidence levels | Market sizing, opportunity questions — check §9 confidence before citing any number externally |
| `competitor-analysis.md` | Comparison matrix vs Cooklist, MyFitnessPal, Frollo, YNAB, ReceiptHero, Pocketbook, §6 monitoring cadence & response triggers | Competitive positioning questions |
| `user-research.md` | 3 personas (Priya, Marcus, Jess), JTBD, churn risk, onboarding/retention notes, §6 validation status (personas are unvalidated hypotheses) | Persona-driven design or copy decisions |
| `design-concepts.md` | UX principles, screen flows, design system, visual direction, §7A interaction states (loading/empty/error/offline) + breakpoints + handoff process | UI/UX/design work |
| `technical-architecture.md` | System design, full API contracts (§5.1), webhook handling (§5.2), error/retry/idempotency (§2.1), async jobs (§2.2), migrations & data retention (§3), environments (§11), observability (§12), testing strategy (§13), CI/CD (§14) | Engineering/architecture questions, building features |
| `data-discovery-strategy.md` | Which open AU data sources power each module; data gaps; legal/ToS risk notes on scraping retailer prices | Sourcing data, evaluating new data providers — read the legal-risk callout before building any scraper |
| `AGENT-PLAN.md` | 72-hour throwaway prototype plan (receipt → multi-module insight) + mapping of prototype findings to real engineering tasks | Building/extending the agent prototype; understanding what's prototype-only vs production |
| `gtm-plan.md` | Launch phases, channels, §7 compliance/kill-criteria for marketing claims, §8 channel kill criteria | Launch/marketing planning |
| `financial-model.md` | Setup + running costs, revenue model, unit economics, 12-month P&L, §6 key assumptions & sensitivity/re-run triggers | Budget, pricing, unit economics questions |
| `roadmap.md` | Quarter-by-quarter plan with exit criteria, team/resourcing assumptions, cross-phase dependencies | Sequencing/prioritisation questions |

## Key facts (quick reference — verify against source files for anything load-bearing)

- **Market:** Australia first → NZ/UK/Canada later. Combined SAM ≈ AU$48B tracked spend (per README) / ~AU$146M ARR at scale (per market-research-au.md — these are different framings, check context).
- **Pricing:** Free tier + Premium AU$7.99/mo + Family AU$12.99/mo.
- **North Star Metric:** WAU who scanned ≥1 receipt AND got ≥1 personalised action AND acted on it. Target ≥25% of WAU by Month 6.
- **Tech stack:** React Native/Expo, Google Cloud Vision (OCR), Claude API (extraction/chat), Open Food Facts + USDA FoodData (nutrition), Basiq (AU Open Banking), Supabase (Postgres/Auth/Edge Functions), PostHog, Vercel.
- **MVP (Q3 2026):** Smart Scan + purchase history + weekly grocery list + basic nutrition macros. Price Scout and Money Map deferred to Q4 2026.
- **Compliance:** Privacy Act 1988, CDR (via Basiq), TGA (no medical claims on nutrition), ACL (substantiate savings claims), NDB Scheme (30-day breach notification).

## Working conventions for this project

- When adding a new research doc, also add a row to the table in `README.md` and to
  the table above in this SKILL.md so the index stays complete.
- Keep dollar figures in AU$ unless a doc is explicitly about another market.
- Treat `PRD.md` as the source of truth when other docs disagree on scope, metrics,
  or feature detail — older docs (`smartcart-original-PRD.md`, `brainstrom-original.md`)
  are historical/provenance only.
- When implementing a feature, check `TODO.md` for its task entry (acceptance
  criteria, dependencies) before starting, and check it off only once the
  Definition of Done in `PRD.md` §12 is actually met.
