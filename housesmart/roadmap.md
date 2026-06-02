# HouseSmart — Product Roadmap

**Version:** 1.0 | June 2, 2026
**Format:** Quarter-by-quarter with milestones, exit criteria, and team responsibilities

---

## Roadmap Philosophy

1. **Validate before building** — prototype test before any code
2. **Core habit first** — scanning must stick before adding features
3. **Revenue enables scale** — reach AU$2K MRR before paid acquisition
4. **One platform at a time** — AU market proven before NZ/UK

---

## Current Status: Pre-Development

| Item | Status |
|------|--------|
| Product concept | ✅ Defined |
| Market research | ✅ Complete |
| Competitor analysis | ✅ Complete |
| Technical architecture | ✅ Designed |
| User research | ✅ Personas + JTBD |
| Financial model | ✅ Projected |
| GTM plan | ✅ Written |
| Design concepts | ✅ Defined |
| Prototype | 🔲 Not started |
| Development | 🔲 Not started |

---

## Phase 0 — Foundation (Weeks 1–4, July 2026)

### Goals
Validate the core assumption: **Will people scan receipts regularly?**

### Deliverables
| # | Task | Owner | Week |
|---|------|-------|------|
| 1 | Set up Expo + Supabase project skeleton | Dev | W1 |
| 2 | Build camera scan screen (expo-camera) | Dev | W1 |
| 3 | Integrate Google Cloud Vision OCR | Dev | W2 |
| 4 | Integrate Claude API for extraction | Dev | W2 |
| 5 | Build basic receipt result screen | Dev | W2-3 |
| 6 | Create InVision/Figma prototype | Design | W2 |
| 7 | Run 20-user prototype test | PM | W3-4 |
| 8 | Launch waitlist landing page | Dev+Design | W2 |
| 9 | Set up PostHog + Sentry | Dev | W1 |

### Exit Criteria
- ≥ 70% of 20-user prototype testers complete scan → result → list flow
- ≥ 200 waitlist signups
- OCR accuracy ≥ 85% on Woolworths receipts (manual test)
- ALDI receipt accuracy ≥ 70% (acceptable threshold)

---

## Phase 1 — MVP Build (August–September 2026)

### Theme: Scan → Learn → List

### Goals
Ship a working MVP on TestFlight + Play Store. Get 500 beta users. Validate week-4 retention.

### Deliverables
| # | Feature | Priority | Status |
|---|---------|---------|--------|
| 1.1 | Receipt scanning (camera + gallery) | P0 | 🔲 |
| 1.2 | Claude extraction + structured output | P0 | 🔲 |
| 1.3 | Purchase history dashboard (groceries) | P0 | 🔲 |
| 1.4 | Weekly shopping list (frequency prediction) | P0 | 🔲 |
| 1.5 | Basic nutrition summary (macros only) | P0 | 🔲 |
| 1.6 | User auth (email + Google/Apple OAuth) | P0 | 🔲 |
| 1.7 | Expense categorisation (all receipt types) | P1 | 🔲 |
| 1.8 | Monthly spend dashboard | P1 | 🔲 |
| 1.9 | Push notifications (weekly list reminder) | P1 | 🔲 |
| 1.10 | Onboarding flow (5 screens) | P0 | 🔲 |
| 1.11 | Manual entry fallback | P2 | 🔲 |
| 1.12 | Data export (JSON) | P2 | 🔲 |

### Technical Milestones
| Milestone | Target Date |
|-----------|------------|
| Supabase schema + RLS live | Aug Week 1 |
| Scan pipeline end-to-end working | Aug Week 2 |
| Weekly list algorithm working | Aug Week 3 |
| TestFlight beta live (50 users) | Aug Week 4 |
| 500-user closed beta open | Sep Week 2 |

### Exit Criteria
- Week-4 retention ≥ 25% in beta
- NPS ≥ 20
- Avg receipts scanned/user/week ≥ 2
- OCR accuracy ≥ 92% on Woolworths/Coles (in production)

---

## Phase 2 — AU Market Launch (October–December 2026)

### Theme: Save → Compare → Connect

### Goals
Public launch. Validate freemium conversion. Hit AU$2,400 MRR.

### Deliverables
| # | Feature | Priority |
|---|---------|---------|
| 2.1 | Price Scout Phase 1 (from user scan data) | P0 |
| 2.2 | Money Map / Basiq bank sync | P0 |
| 2.3 | Freemium tiers (free / premium AU$7.99) | P0 |
| 2.4 | Stripe subscription integration | P0 |
| 2.5 | Full vitamin/mineral tracking + deficiency alerts | P1 |
| 2.6 | Nutrition dietary suggestions ("Add spinach to fix Iron") | P1 |
| 2.7 | Weekly digest push notification | P1 |
| 2.8 | Budget tracking (categories + 80%/100% alerts) | P1 |
| 2.9 | Bill change detection ("electricity up 23%") | P2 |
| 2.10 | Subscription tracker (recurring charge detection) | P2 |

### Marketing Milestones
| Milestone | Target Date |
|-----------|------------|
| Product Hunt launch | Oct Week 1 |
| Reddit soft launch posts | Oct Week 2 |
| 1,000 users | Oct |
| 5,000 users | Dec |
| AU$2,400 MRR | Dec |

### Exit Criteria
- Free → paid conversion ≥ 5%
- Bank connection rate ≥ 40% of premium users
- 5,000 total signups by Dec 31
- MRR ≥ AU$2,400

---

## Phase 3 — Engagement & Depth (January–March 2027)

### Theme: Smarter → Social → Sticky

### Deliverables
| # | Feature | Priority |
|---|---------|---------|
| 3.1 | Crowdsourced pricing layer (opt-in, anonymised) | P0 |
| 3.2 | AI chat interface (Claude function calling) | P0 |
| 3.3 | Multi-user household sharing (family accounts) | P0 |
| 3.4 | Family plan tier (AU$12.99/month) | P0 |
| 3.5 | Referral program (AU$5 credit) | P1 |
| 3.6 | Recipe suggestions from predicted grocery list | P1 |
| 3.7 | Price spike alerts (real-time) | P1 |
| 3.8 | Woolworths/Coles live price API integration | P2 |
| 3.9 | Apple Watch companion (quick scan shortcut) | P2 |
| 3.10 | Widget (home screen shopping list preview) | P2 |

### Exit Criteria
- 30-day retention ≥ 30%
- 10,000 total users
- MRR ≥ AU$6,000
- AI chat WAU engagement ≥ 40%

---

## Phase 4 — Scale & Revenue (April–June 2027)

### Theme: Monetise → Expand → Partner

### Deliverables
| # | Task | Priority |
|---|------|---------|
| 4.1 | Affiliate links (Coles/Woolies partner ordering) | P0 |
| 4.2 | FMCG data insights product (B2B dashboard) | P0 |
| 4.3 | White-label pilot (approach Bupa/Medibank) | P1 |
| 4.4 | NZ market research + bank partner identification | P1 |
| 4.5 | UK Open Banking research (TrueLayer, Sainsbury) | P2 |
| 4.6 | Paid acquisition launch (Meta + Google) | P0 |

### Exit Criteria
- MRR ≥ AU$15,000
- LTV:CAC ≥ 4:1 on paid acquisition
- ≥ 1 FMCG data partner signed
- NZ launch feasibility confirmed

---

## 2028+ — Global Platform

| Market | Timeline | Prerequisite |
|--------|---------|-------------|
| New Zealand | H1 2028 | AU product-market fit + Akahu bank integration |
| United Kingdom | H2 2028 | Open Banking mature (TrueLayer), Tesco/Sainsbury APIs |
| Canada | 2029 | Flinks bank integration, Loblaws/Metro data |
| Singapore | 2029 | PayNow Open Banking |

---

## Risk-Adjusted Timeline

| Risk | Impact | Buffer |
|------|--------|--------|
| ALDI receipt accuracy issues | +1 week MVP | Pre-tested in Phase 0 |
| Basiq integration complexity | +2 weeks Phase 2 | Abstract bank layer early |
| App Store review delays | +1 week | Submit 2 weeks early |
| Stripe setup / AU compliance | +1 week | Start in Phase 1 |
| Claude API prompt engineering | +1 week | Sprint on extraction quality early |

**Total buffer:** 2 weeks built into each phase end date.

---

## Key Decisions Log

| Date | Decision | Rationale |
|------|---------|----------|
| Jun 2026 | Consolidate BillScout + SmartCart into HouseSmart | Shared engine (OCR + bank), different UX angles → one platform more defensible |
| Jun 2026 | Grocery-first, finance-second | Grocery is daily habit; finance is monthly review — build the daily habit first |
| Jun 2026 | React Native/Expo over Flutter | Larger ecosystem, better Basiq/Supabase SDKs, familiar for JS-stack teams |
| Jun 2026 | Supabase over Firebase | PostgreSQL + RLS is better for financial data; no vendor lock-in |
| Jun 2026 | Premium at AU$7.99 vs AU$5.99 | Concrete savings feature (price compare) justifies higher price; easy ROI demo |
