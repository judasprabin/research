# SmartCart — Product Requirements Document (v2.0)

_Prepared: May 5, 2026 | Updated: June 2, 2026_
_Version: 2.0 — Research-Ready Draft_

---

## 🧠 Concept Overview

SmartCart is an all-in-one household intelligence app that combines:

- 📸 Grocery receipt scanning (computer vision + OCR)
- 🛒 Weekly shopping suggestions (AI-driven, based on purchase history)
- 💰 Cross-store price comparison (personalised, from your own scan data)
- 🥦 Nutritional analysis from grocery purchases (household-level, not meal-level)
- 🏦 Bank transaction tracking (Open Banking integration)

No single app currently offers this combination in one place. SmartCart's differentiator is **linking what you buy to what you need** — bridging expense tracking, nutrition, and smart purchasing.

---

## 📊 Market Opportunity

| Metric | Value |
|--------|-------|
| AU Grocery Retail Market | ~AU$125B/year (2025) |
| Households in AU | ~10.4M |
| Digital Grocery Penetration | ~15% and growing |
| Open Banking Users in AU | ~2M (growing) |
| Avg Household Annual Grocery Spend | ~AU$14,400 |
| SmartCart SAM (AU urban, 18–55) | ~AU$28B/year |
| SmartCart TAM (global, phased) | ~AU$800B/year |

---

## 🎯 Target Audience

**Primary:** Urban Australian households, ages 25–50, dual-income or busy single professionals with digital fluency. They shop at Coles/Woolworths/ALDI weekly and want to spend smarter.

**Secondary:** Health-motivated individuals interested in nutrition tracking who find existing calorie-counter apps too burdensome (no meal logging).

**Tertiary:** Budget-conscious students and young families who actively compare prices across stores.

---

## 🏁 North Star Metric (NSM)

> **"Weekly Active Users whose grocery spend SmartCart has analysed ≥ 1 receipt for, who receive ≥ 1 personalised suggestion per week, and who act on it (add to list or save money)"**

---

## ✅ Success Metrics

### Primary KPIs (Week 1–12 after launch)
| Metric | Target (Month 3) | Target (Month 6) |
|--------|----------------|-----------------|
| Signed-up users | 2,000 | 8,000 |
| Weekly Active Users (WAU) | 600 | 3,200 |
| Receipts scanned per WAU/week | ≥ 2 | ≥ 3 |
| Weekly suggestions generated | ≥ 1/user | ≥ 1/user |
| Suggestion CTR (tap/add) | ≥ 15% | ≥ 20% |
| User-reported savings identified | ≥ $8 avg/week | ≥ $12 avg/week |
| NPS score | ≥ 30 | ≥ 40 |

### Secondary KPIs
| Metric | Target |
|--------|--------|
| Bank connection rate (of signups) | ≥ 40% |
| Nutrition report opens | ≥ 50% of active users |
| 30-day retention | ≥ 35% |
| 90-day retention | ≥ 20% |
| Free → Paid conversion | ≥ 5% |

### North Star Metric Formula
```
SmartCart NSM = Σ(Users who scanned ≥ 1 receipt in 7 days 
                 AND received ≥ 1 suggestion 
                 AND had ≥ 1 positive action) / WAU
```
Target: ≥ 25% of WAU hitting full NSM by Month 6.

---

## 📦 MVP Feature Specifications (Phase 1)

### F1: Receipt Scanning
- **Input:** Camera photo of paper receipt (any Australian supermarket)
- **Processing:** Google Cloud Vision API OCR → structured extraction
- **Extracted fields:** store name, date, line items (name, qty, price, total)
- **Output:** Purchase saved to personal purchase history, categorised
- **Accuracy target:** ≥ 92% item-level extraction accuracy
- **Supported stores:** Woolworths, Coles, ALDI, IGA, Costco (Phase 1)
- **Edge cases:** hand-written receipts (reject gracefully), partial scans (prompt rescan), non-grocery receipts (categorise as other)

### F2: Purchase History & Dashboard
- **Views:** 7-day / 30-day / custom range spending by category
- **Categories:** groceries, utilities, dining out, transport, health, other
- **Charts:** Bar chart (weekly spend), pie chart (category split), line chart (trend over time)
- **Export:** CSV download for power users

### F3: Weekly Shopping List (Smart Suggestions)
- **Algorithm:** Per-item repurchase frequency (days between purchases) calculated from scan history
- **Prediction window:** 7 days ahead
- **Output:** "You're likely to run out of [item] in ~[N] days. Add to list?"
- **Manual override:** Users can add/remove items, mark as "already have"
- **Quantity hint:** Based on last purchase quantity × household size

### F4: Basic Nutrition Summary
- **Data source:** Open Food Facts API (free, AU-compatible)
- **Mapping:** Receipt item names → Open Food Facts products (fuzzy match, confidence threshold)
- **Output:** Weekly totals per household for: Energy (kJ), Protein, Carbs, Fat, Fibre, Sugar
- **Display:** Simple card per week — "Your cart this week vs. WHO recommended daily average × 7"
- **Limitations:** Packaged foods only; fresh produce relies on USDA data; restaurants/ bakery not included

### F5: User Account & Data
- **Auth:** Email + password, or Google/Apple sign-in
- **Data storage:** Supabase (PostgreSQL + Row Level Security)
- **Export:** Full data export as JSON (GDPR/Privacy Act compliance)
- **Delete:** Full account + data deletion (one tap)

---

## 🗺️ Product Roadmap

### Phase 1 — MVP (Months 1–3, Ship to Test Market)
- [ ] Receipt scanning (camera, manual entry fallback)
- [ ] Purchase history + basic dashboard
- [ ] Weekly shopping list (frequency-based)
- [ ] Basic nutrition summary (Open Food Facts)
- [ ] User accounts (email + OAuth)

### Phase 2 — Growth (Months 4–6, Full AU Launch)
- [ ] Cross-store price comparison (from scan data)
- [ ] Bank transaction sync (Basiq integration — AU)
- [ ] Price alert: "Buy X at Y instead of Z, save $N"
- [ ] Vitamin/mineral deficiency flags (Iron, Vitamin D, Calcium, etc.)
- [ ] Suggestion: "Add spinach to fix your Iron gap"
- [ ] Push notifications for weekly digest

### Phase 3 — Engagement (Months 7–12)
- [ ] Crowdsourced pricing layer (anonymised, opt-in)
- [ ] Recipe suggestions linked to predicted purchases
- [ ] Household multi-user support (share cart with partner)
- [ ] Price prediction: "Wait 3 days, this item historically drops"
- [ ] Apple Watch / wearable companion

### Phase 4 — Monetisation & Scale (Year 2)
- [ ] Freemium tier launch (free = core scan + list; premium = nutrition + price compare + bank sync)
- [ ] Affiliate links to partner supermarkets
- [ ] Anonymised data insights product for FMCG brands
- [ ] White-label licensing (Woolworths, health insurers)
- [ ] UK/CA/NZ expansion (Open Banking compatible markets)

---

## 💡 Monetisation

### Tiered Model
| Feature | Free | Premium (AU$6.99/month) |
|---------|------|----------------------|
| Receipt scanning | ✅ | ✅ |
| Purchase history | 30 days | ✅ |
| Weekly shopping list | Basic | ✅ AI-enhanced |
| Nutrition summary | Basic macros | ✅ Full + deficiency alerts |
| Price comparison | ❌ | ✅ |
| Bank sync | ❌ | ✅ |
| Vitamin alerts | ❌ | ✅ |
| Crowdsourced pricing | ❌ | ✅ |
| Data export | ❌ | ✅ |

### Alternative Revenue Streams
1. **Affiliate commissions:** "Order through Coles/Woolworths from SmartCart list" — ~2–5% commission per order
2. **FMCG insights:** Anonymised, aggregated shopping trend reports sold to CPG brands (e.g., "AU households buy 40% more rice brand X when on promotion")
3. **White-label:** Licence SmartCart tech to health insurers (Bupa, Medibank) for wellness programs
4. **In-app ads:** Non-intrusive sponsored product suggestions (targeted by purchase history)

---

## 🛠 Tech Stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Mobile (iOS + Android) | React Native / Expo | Single codebase, fast iteration |
| OCR | Google Cloud Vision API | Best accuracy for receipts, easy API |
| Receipt parser (ML) | Claude API (Anthropic) | Structured extraction from OCR raw text |
| Nutrition DB | Open Food Facts API (free) | AU products, crowdsourced, no cost |
| Bank sync (AU) | Basiq API | Leading AU Open Banking aggregator |
| Backend | Supabase | PostgreSQL + Auth + Edge Functions, low cost |
| AI / Suggestions | Claude API (Anthropic) | Weekly list generation, nutrition analysis |
| Hosting | Vercel (frontend) + Supabase (backend) | Zero-ops, free tier available |
| Analytics | PostHog (own infrastructure) | Product analytics + funnel tracking |
| Error tracking | Sentry | Mobile error monitoring |
| CI/CD | GitHub Actions | Automated builds for iOS + Android |

---

## ⚠️ Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| OCR accuracy too low for ALDI receipts | Medium | High | Test ALDI early; build manual entry fallback |
| Basiq API pricing changes | Low | High | Negotiate cap; have Deeloe as backup |
| Users won't scan receipts regularly | High | High | In-app nudge cadence; gamification; quick-scan shortcut |
| Open Food Facts AU coverage gaps | Medium | Medium | Hybrid with USDA FoodData Central; manual mapping table |
| Privacy concerns with bank access | Medium | High | Transparent data policy; read-only access; onboard with trust walkthrough |
| Slow freemium → paid conversion | High | High | Focus on price comparison feature as premium hook (concrete savings) |
| AU Open Banking rollout delays | Low | Medium | Build without bank sync first; add when available |

---

## 🔐 Privacy & Compliance (AU)

- **Privacy Act 1988 (Cth):** SmartCart collects personal financial data — must be minimised, stored securely, not sold
- **Consumer Data Right (CDR):** Bank data covered under ACCC CDR rules; Basiq handles compliance
- **APP compliance:** APP 3 (collection minimisation), APP 6 (use/disclosure), APP 11 (security), APP 13 (correction)
- **Data retention:** Delete on user request within 30 days; purge inactive accounts after 2 years
- **Notifiable Data Breaches:** Incident response plan required (documented separately)
- **Age gate:** Users must be 16+ (in-app check)

---

## 🧪 Testing & Validation Strategy

### Phase 1 Validation (Pre-MVP)
- 20-user prototype test (InVision prototype)
- Goal: Validate receipt scan UX, willingness to scan receipts weekly
- Success criteria: ≥ 70% complete a full scan-to-list flow without support

### Phase 2 Validation (Beta Launch)
- 500-user closed beta (TestFlight + Google Play internal)
- Goal: Validate retention, suggestion quality, willingness to connect bank
- Success criteria: Week 4 retention ≥ 30%; NPS ≥ 20

### Phase 3 Validation (Soft Launch)
- 2,000-user public beta in Sydney/Melbourne
- Goal: Validate paid conversion funnel, unit economics
- Success criteria: ≥ 5% free → paid conversion within 30 days

---

## 📁 File Inventory

This research repo contains the following SmartCart files:

| File | Description |
|------|-------------|
| `PRD.md` | This document — full product requirements |
| `market-research-au.md` | Australian grocery market analysis |
| `competitor-analysis.md` | Deep dive competitor landscape |
| `user-research.md` | Personas, jobs-to-be-done, validation plan |
| `technical-research-report.md` | Technical architecture, APIs, infrastructure |
| `gtm-plan.md` | Go-to-market and testing strategy |
| `financial-model.md` | Cost structure, revenue projections, unit economics |
| `README.md` | Project overview and getting started |
