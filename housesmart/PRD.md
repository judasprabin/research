# HouseSmart — Product Requirements Document

**Version:** 1.0
**Date:** June 2, 2026
**Status:** Approved for Development
**Author:** Prabin Karki

---

## 1. Vision & Problem Statement

### Vision
> Give every Australian household a personal financial nutritionist in their pocket — one that works from what they already buy, not from what they remember to log.

### The Problem (5 Pains, One App)

| # | Pain | Current "fix" | Why it fails |
|---|------|--------------|-------------|
| 1 | "I forget what I need" | Mental list, notes app | No memory of purchase history |
| 2 | "Am I getting ripped off?" | Check catalogues manually | Time-consuming, not personalised |
| 3 | "I have no idea if we eat healthy" | MyFitnessPal | Requires meal logging (too much effort) |
| 4 | "I can't track all my spending" | Bank app / spreadsheet | Doesn't understand grocery line items |
| 5 | "My bills change and I don't notice" | Nothing | No proactive alerting |

**HouseSmart solves all five from a single scan.**

---

## 2. Product Modules & Feature Specs

### Module 1 — Smart Scan (Core Engine)
The foundational capability used by every other module.

**What it scans:** Any receipt or bill — groceries, utilities, dining, pharmacy, petrol, retail

**Technical flow:**
```
Camera photo → Google Cloud Vision (OCR) → Claude API (structured extraction)
→ ExpenseRecord { merchant, date, items[], totals, category, confidence }
→ Stored in Supabase
```

**Key specs:**
- Extraction fields: merchant name, date, line items (name + qty + price), subtotal, GST, total
- Confidence scoring per field (flag low-confidence fields for user review)
- Manual correction UI for fields < 80% confidence
- Fallback: manual entry for blurry/incomplete receipts
- Supported formats: PNG, JPG, HEIC, PDF (single page)
- Target accuracy: ≥ 92% item-level on Woolworths/Coles; ≥ 80% on ALDI

### Module 2 — Grocery Brain
The smart layer built exclusively on grocery receipts.

**Features:**
- **Purchase history:** Full searchable log of every grocery item bought, with store and price
- **Repurchase prediction:** Per-item rolling frequency (days between purchases) → "Milk runs out in ~2 days"
- **Weekly shopping list:** Auto-generated every Thursday from predictions, editable by user
- **Quantity hints:** Suggest quantity based on last purchase × household size
- **Smart categorisation:** Automatically groups into produce, dairy, meat, pantry, snacks, etc.

**Algorithm (repurchase prediction):**
```
For each item i:
  purchases = sorted list of purchase dates
  intervals = diff between consecutive dates
  avg_interval = mean(intervals, weighted toward recent)
  predicted_next = last_purchase_date + avg_interval
  days_until = predicted_next - today
  if days_until <= 7: add to weekly list
```

### Module 3 — Price Scout
Cross-store price intelligence from the user's own scan data.

**Phase 1 (from your data):**
- Builds price history per item per store from scanned receipts
- "You usually pay $3.50 for this at Coles — it's $2.80 at ALDI"
- Shows % and $ savings on current shopping list

**Phase 2 (crowdsourced + live):**
- Anonymised price contributions from all users (opt-in)
- Integration with Woolworths/Coles public price APIs
- Live shelf price data via web scraping pipeline
- "This item is on sale at Woolworths this week" alerts

**Savings calculation:**
```
For each item in weekly list:
  cheapest_store = store with lowest avg price in last 60 days
  current_store  = user's default store
  saving = current_store_price - cheapest_store_price
  total_weekly_saving = Σ savings where saving > 0.50 (threshold)
```

### Module 4 — Nutrition Lens
The differentiated feature. No other app does this from receipts.

**What it does:**
- Maps grocery receipt items → Open Food Facts / USDA FoodData Central products
- Calculates weekly household totals: Energy, Protein, Carbs, Fat, Fibre, Sugar, Iron, Calcium, Vitamin D, Folate
- Compares to Australian Dietary Guidelines (ADG) recommended weekly amounts
- Flags nutritional gaps: "Your cart is low on Iron and Fibre this week"
- Suggests additions: "Add spinach (AU$2.50 at Coles) to fix your Iron gap"

**Coverage & accuracy:**
- Packaged foods (barcoded): ≥ 85% match via Open Food Facts AU
- Fresh produce: USDA FoodData Central (generic nutrient profiles)
- Restaurant/bakery/deli: Estimated from category averages, labelled as "estimate"
- Precision caveat: Quantities estimated from pack size × purchase qty — not exactly how much consumed

**Key guardrail:** All suggestions framed as "general dietary guidance, not medical advice" — TGA compliance.

### Module 5 — Money Map
Full household expense picture via Open Banking.

**Core features:**
- Connect bank account via Basiq (120+ AU institutions)
- Auto-categorise transactions: groceries, dining, utilities, transport, subscriptions, health, entertainment, other
- Match bank transactions ↔ scanned receipts (reconciliation)
- Monthly household spend dashboard
- Budget tracking: set category budgets, alert at 80% + 100%
- Bill change detection: "Your electricity bill is 23% higher than last month"
- Subscription tracking: flags recurring charges with cancel suggestions

**Bank connection security:**
- Read-only access only (no payment capability)
- OAuth2 via Basiq (CDR-compliant)
- Access tokens encrypted AES-256 in Supabase
- User can revoke at any time

---

## 3. User Personas

### Priya, 34 — Dual-Income Professional (Melbourne)
Shops Woolworths weekly. Too busy to track nutrition or compare prices. Wants intelligence without effort.
**Primary hook:** Weekly grocery list + price comparison

### Marcus, 42 — Health-Focused Dad (Sydney)
Shops Coles + Costco. Uses MyFitnessPal inconsistently. Wants nutrition from receipts without logging.
**Primary hook:** Nutrition Lens — zero-effort macros + vitamin tracking

### Jess, 22 — Budget Student (Perth)
Shops ALDI primarily. Very price-conscious. Needs cross-store comparison to stretch every dollar.
**Primary hook:** Price Scout — "ALDI saves you $14 this week vs Coles"

---

## 4. North Star Metric

> **Weekly Active Users who scanned ≥ 1 receipt AND received ≥ 1 personalised action (list item, saving, or nutrition insight) AND acted on it**

Target: ≥ 25% of WAU hit full NSM by Month 6.

---

## 5. Success Metrics

### Product KPIs
| Metric | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|
| Total signups | 1,500 | 5,000 | 12,000 |
| WAU | 600 | 2,000 | 5,000 |
| Receipts/WAU/week | ≥ 2 | ≥ 3 | ≥ 3.5 |
| Week-4 retention | ≥ 25% | ≥ 30% | ≥ 35% |
| Paying users | 30 | 300 | 1,100 |
| MRR (AU$) | 240 | 2,400 | 8,800 |
| NPS | ≥ 20 | ≥ 35 | ≥ 45 |
| Price savings identified/WAU/week | — | ≥ 3 | ≥ 5 |

### Feature-Level KPIs
| Feature | Metric | Target |
|---------|--------|--------|
| Smart Scan | OCR accuracy (item-level) | ≥ 92% on Woolies/Coles |
| Grocery Brain | Weekly list accuracy rating | ≥ 80% "useful" |
| Price Scout | Avg weekly savings identified | ≥ AU$8 |
| Nutrition Lens | Weekly nutrition report opens | ≥ 50% of active users |
| Money Map | Bank connection rate | ≥ 40% of signups |

---

## 6. MVP Scope (Phase 1 — Months 1–3)

**Build:**
- [x] Smart Scan: camera OCR + structured extraction
- [x] Purchase history dashboard (groceries)
- [x] Grocery Brain: weekly list (frequency-based)
- [x] Basic Nutrition Lens: weekly macro summary
- [x] User auth (email + Google/Apple OAuth)
- [x] Expense categorisation (all receipt types)

**Defer to Phase 2:**
- Price Scout (needs accumulated scan data)
- Money Map / bank sync (Basiq integration)
- Vitamin/deficiency alerts
- Crowdsourced pricing
- AI chat interface

---

## 7. Product Roadmap

### Q3 2026 — MVP (July–September)
**Theme:** Scan → Learn → List
- Receipt scanning (Woolworths, Coles, ALDI, IGA, pharmacies, utilities)
- Purchase history + expense dashboard
- Weekly shopping list (frequency prediction)
- Basic nutrition summary (macros from receipt)
- User accounts + onboarding
- TestFlight + Play Store beta (500 users)

**Exit criteria:** Week-4 retention ≥ 25% in 500-user beta

### Q4 2026 — AU Market Launch (October–December)
**Theme:** Save → Compare → Connect
- Price Scout Phase 1 (from user's own data)
- Money Map / bank sync (Basiq)
- Freemium tier launch (free + premium AU$7.99/month)
- Vitamin/deficiency alerts
- Push notification digest (weekly)
- Product Hunt launch
- 5,000 user target

**Exit criteria:** Free → paid conversion ≥ 5%

### Q1 2027 — Engagement & Depth
**Theme:** Smarter → Social → Sticky
- Crowdsourced pricing (opt-in, anonymised)
- AI chat interface ("How much did I spend on meat last month?")
- Multi-user household sharing
- Recipe suggestions from predicted grocery list
- Price spike alerts ("Eggs up 20% at Coles — ALDI still cheaper")
- Referral program (AU$5 credit)

**Exit criteria:** 30-day retention ≥ 30%

### Q2 2027 — Scale & Revenue
**Theme:** Monetise → Expand → Partner
- Affiliate links (Woolworths/Coles partner orders)
- FMCG data insights product (B2B)
- White-label discussions (Bupa, Medibank wellness programs)
- NZ market preparation (bank + supermarket research)
- UK market research (Open Banking, Tesco/Sainsbury/ASDA)

**Exit criteria:** MRR ≥ AU$15,000; LTV:CAC ≥ 4:1

### 2028 — Global Platform
- NZ launch (Countdown/Pak'nSave/New World + Akahu bank sync)
- UK launch (Tesco/Sainsbury/ASDA + TrueLayer bank sync)
- Canada launch (Loblaws/Metro/Sobeys + Flinks bank sync)
- Household subscription (family plan AU$12.99/month)

---

## 8. Monetisation Strategy

### Freemium Tiers
| Feature | Free | Premium (AU$7.99/mo) | Family (AU$12.99/mo) |
|---------|------|---------------------|---------------------|
| Smart Scan | ✅ (10/month) | ✅ Unlimited | ✅ Unlimited |
| Purchase history | 30 days | ✅ Full | ✅ Full |
| Grocery Brain list | Basic (top 5) | ✅ Full AI list | ✅ Full |
| Price Scout | ❌ | ✅ | ✅ |
| Nutrition Lens | Macros only | ✅ Full + alerts | ✅ Full |
| Money Map bank sync | ❌ | ✅ 1 account | ✅ Up to 4 |
| AI chat | ❌ | ✅ | ✅ |
| Multi-user | ❌ | ❌ | ✅ (5 members) |

### Additional Revenue (Year 2+)
1. **Affiliate commissions:** 2–5% on orders placed via HouseSmart partner links
2. **FMCG data insights:** Anonymised aggregate shopping trend reports (AU$30–100K/year per brand)
3. **White-label licensing:** Health insurers, supermarket loyalty programs
4. **In-app sponsored suggestions:** Non-intrusive, targeted by purchase history

---

## 9. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Low receipt scanning habit formation | High | Critical | Weekly nudges, shortcut widget, gamification streaks |
| ALDI receipt accuracy poor | Medium | High | Test pre-launch; add manual entry fallback; specific ALDI prompt engineering |
| Open Food Facts AU coverage gaps | Medium | Medium | Supplement with USDA; maintain manual item mapping table |
| Basiq cost spike at scale | Low | High | Volume pricing negotiation; daily (not real-time) sync; Akahu fallback |
| Privacy backlash (bank data) | Medium | High | Read-only, CDR-compliant, transparent UX, "what we access" explainer |
| Slow free→paid conversion | High | High | Price comparison is the key premium hook — concrete $ saved per week |
| Coles/Woolworths builds in-house | Low-Medium | Medium | First-mover data moat; cross-store feature they structurally cannot offer |

---

## 10. Compliance & Privacy

- **Privacy Act 1988 (Cth)** — 13 APPs, data minimisation, user deletion rights
- **Consumer Data Right (CDR)** — Basiq handles accreditation; read-only bank access
- **Australian Dietary Guidelines** — Nutrition framed as guidance, not medical advice
- **TGA** — No health/disease claims; disclaimer on all nutrition output
- **ACL** — Savings claims must be substantiated from real scan data
- **App Store / Play Store** — Privacy policy, age gate 16+, transparent subscription terms
- **NDB Scheme** — 30-day notification to OAIC on qualifying breach; incident plan required
