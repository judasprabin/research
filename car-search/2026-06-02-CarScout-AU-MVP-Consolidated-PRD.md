# CarScout — Consolidated PRD (v2.0)
## AU MVP + Global Platform

**Date:** June 2, 2026 | **Version:** 2.0 | **Status:** Draft
**Sources:** 6-region global research + AU MVP Notion doc

---

## Executive Summary

**We are building CarScout** — an AI-powered, EV-first comprehensive car buying companion. Not a marketplace. A complete pre-purchase companion that gives buyers the same information transparency a Tesla engineer has.

**Core problem:** First-time EV buyers face a fragmented, trust-freezing experience — no battery health data, inflated range claims, scattered incentives, and no way to know if they can charge at home.

**5 Global White Spaces (CarScout owns first globally):**
1. Battery health transparency — SOH grades for used EVs
2. Real-world range database — owner-reported, not EPA/WLTP lab numbers
3. EV-native TCO calculator — incentives stacked automatically
4. Charging readiness assessment — can I charge at home?
5. Cross-border buying guide

**AU MVP Scope:** Australia-first, then US + Germany. 10 P0 features. Private beta Month 6, public launch Month 7.

**Moat:** First platform globally to integrate battery health + real-world range + EV-native TCO. No competitor has all three anywhere in the world.

---

## 1. Product Overview

**Product Name:** CarScout
**Tagline:** *"Know everything about your car before you buy."*
**Type:** Web platform (PWA) + mobile-first design

### 1.1 Vision
Every car buyer deserves the same level of information transparency that a Tesla engineer has about their car.

### 1.2 Mission
Build the world's most comprehensive car buying companion — helping first-time buyers understand everything about a car before they buy, making the transition to EVs confident, transparent, and accessible.

### 1.3 Core Principles
1. **Transparency above all** — show the good and the bad
2. **Data-driven decisions** — every recommendation backed by real data
3. **Simplicity** — make the complex simple for first-time buyers
4. **Global but local** — adapt to each market's incentives, charging infra, buying processes
5. **Trust through verification** — verify everything, no marketing fluff

### 1.4 Target Markets (Phased)
| Phase | Market | Priority |
|-------|--------|----------|
| Phase 1 (MVP) | **Australia** | P0 |
| Phase 2 | **US + Germany** | P1 |
| Phase 3 | India, UK, France | P2 |

---

## 2. Problem Statement

First-time car buyers face a broken, fragmented experience:

| Pain Point | Current Reality |
|------------|-----------------|
| Too much to research | Must visit 10+ websites (OEM, dealer, reviews, forums, financing, insurance, government) |
| No battery health transparency | No platform discloses State-of-Health for used EVs |
| Range anxiety | EPA/WLTP optimistic; real-world can be 20-30% lower |
| Incentive confusion | Federal, state, territory — no platform aggregates eligibility |
| Charging uncertainty | Will I be able to charge at home? Where are nearby chargers? |
| True cost unknown | Monthly payment ≠ true cost |
| Trust deficit | Dealerships have a trust problem globally |
| Overwhelmed by choices | 30+ EV models; first-time buyers don't know where to start |

### AU-Specific Context
- EV market growing (~8-12% share) but no AU platform has battery health, real-world range, or TCO tools
- No national EV subsidy; some state/territory rebates exist (NSW $3k, VIC $3k, SA $3k, WA stamp duty exempt)
- Charging infrastructure lagging — apartment dwellers can't easily install home chargers
- CarsGuide and CarExpert are listings-only; neither has EV-native tools

---

## 3. Market Analysis (AU Focus)

### 3.1 AU EV Market
| Metric | Value |
|--------|-------|
| EV share of new sales | ~8-12% (2025) |
| YoY growth | ~30-40% |
| EV models available in AU | 50+ |
| Public charging stations | ~10,000 |
| Key brands | Tesla, BYD, MG, Polestar, Kia, Hyundai, BMW |

### 3.2 AU Competitive Landscape
| Platform | Multi-brand | Battery SOH | Real Range | TCO | Charging Readiness |
|----------|------------|-------------|------------|-----|-------------------|
| CarsGuide | YES | NO | NO | NO | NO |
| CarExpert | YES | NO | NO | NO | NO |
| Tesla AU | NO | NO | NO | NO | NO |
| **CarScout** | **YES** | **YES** | **YES** | **YES** | **YES** |

**Key takeaway:** No AU platform has battery health + real-world range + TCO. First to ship these three wins.

### 3.3 AU Incentive Landscape
| Incentive | Amount | Eligibility |
|-----------|--------|-------------|
| VIC ZEV subsidy | $3,000 | <$70k vehicle, residents |
| NSW EV rebate | $3,000 | <$68k vehicle, stamp duty exemption |
| SA rebate | $3,000 | <$68k vehicle |
| WA Stamp duty | Exempt | All EVs |
| AU prices | 20-30% higher than US/EU | Import opportunity |

---

## 4. Target Users

### 4.1 Primary Persona
| Field | Description |
|-------|-------------|
| Role | First-time EV buyer, 28-45, suburban homeowner or apartment dweller |
| Goals | Understand true cost of ownership; find a reliable EV; feel confident |
| Pain Points | Can't verify battery health; doesn't know real range; confused by incentives |
| Alternatives | Google, Reddit, CarsGuide, dealer websites |

### 4.2 Secondary Personas
| Persona | Priority |
|---------|----------|
| ICE-to-EV switcher (trade-in vs TCO) | P1 |
| Apartment dweller (charging readiness) | P1 |
| Used EV buyer (battery health grade) | P1 |

---

## 5. Competitive Landscape

### 5.1 Global Competitors
| Competitor | Multi-brand | Battery SOH | Real Range | TCO | Charging Readiness |
|------------|------------|-------------|------------|-----|-------------------|
| Tesla Configurator | NO | NO | NO | NO | Partial |
| Carvana (US) | YES | NO | NO | NO | NO |
| AutoScout24 (EU) | YES | NO | NO | NO | NO |
| CarDekho (IN) | YES | NO | NO | NO | NO |
| CarsGuide (AU) | YES | NO | NO | NO | NO |
| **CarScout** | **YES** | **YES** | **YES** | **YES** | **YES** |

### 5.2 Our Moat
First platform globally to integrate **all three**: battery health data + real-world range + EV-native TCO calculator. No competitor has all three anywhere in the world.

---

## 6. Feature Requirements

### 6.1 P0 Features — MVP (Must Have for AU Launch)

#### F1: Multi-Brand EV Catalog
- **What:** Browse/search all EV models in AU — every brand, one place
- **Filters:** Body type, price range, real range, brand, seats, drivetrain
- **EV-native:** Charging curve shape, battery chemistry, efficiency (Wh/km)
- **Data source:** EVDB / EVKX API
- **Acceptance:** At least 50 AU EV models; 5+ EV-native filters

#### F2: AI Recommendation Quiz
- **What:** "What car should I buy?" — 5-question conversational quiz
- **Output:** Top 3 recommendations ranked with TCO and key specs
- **Tech:** Rule-based (MVP); LLM enhancement in v1.1
- **Acceptance:** Quiz completes in <2 minutes; recs are relevant to AU

#### F3: EV TCO Calculator
- **What:** True monthly cost of ownership vs. ICE comparison
- **Inputs:** Purchase price, incentives (auto-detected from postcode), financing rate, annual km, electricity cost, insurance, maintenance
- **AU incentive auto-detect:** NSW, VIC, SA rebates based on postcode
- **Acceptance:** TCO shown on every EV detail page

#### F4: Battery Health Grade (Used EVs)
- **What:** State-of-Health (SOH) letter grade (A/B/C/D/F) for used EVs
- **Data source:** Aviloo API (primary), Recurrent (secondary)
- **Acceptance:** Every used EV listing shows a battery grade if data available

#### F5: Charging Readiness Assessment
- **What:** "Can I charge at home?" — 3-minute assessment
- **Questions:** Dwelling type, parking situation, electrical panel age, electricity plan
- **Output:** Readiness score (1-10) + recommendations
- **Data source:** Open Charge Map API (public charging density)
- **Acceptance:** User sees score + actionable recommendations

#### F6: Real-World Range Database
- **What:** Owner-reported real range by model, season, climate
- **Display:** "Real range" badge on each EV + seasonal variation
- **Data:** Seeded from EVDB/EVKX; enhanced by user submissions
- **Acceptance:** At least 3 real-range data points per model at launch

#### F7: Incentive Eligibility Auto-Detect
- **What:** Auto-detect all applicable federal + state/territory incentives
- **Inputs:** Postcode, vehicle price, vehicle type
- **Output:** List of applicable incentives with amounts; net purchase price
- **Acceptance:** Correct incentive shown for any AU postcode

#### F8: Trade-in Value Estimator
- **What:** Instant estimate of current car value (VIN or details)
- **Data source:** CarsGuide data (AU estimates)
- **Acceptance:** User gets estimate in <60 seconds

#### F9: Financing Comparison
- **What:** Compare loan offers from multiple lenders in one place
- **Inputs:** Vehicle price, incentive-adjusted amount, credit profile
- **Output:** Monthly payment, APR, term, total interest — sorted
- **Acceptance:** Pre-qualification in <60 seconds; shown alongside TCO

#### F10: Multi-Brand Configurator
- **What:** Configure any EV across all brands; side-by-side mode
- **Acceptance:** Top 20 AU-available models configurable at launch

### 6.2 P1 Features — Post-MVP (v1.1)
| Feature | Description |
|---------|-------------|
| Charging Network Map | Real-time charging station map with availability |
| 360° Inspection Reports | Verified 150-point inspection for used EVs |
| Cross-Border Buying Guide | Import guide for AU buyers sourcing from US/EU |
| Insurance Comparison | Integrated insurance quotes alongside TCO |

### 6.3 P2 Features — Future
| Feature | Description |
|---------|-------------|
| LLM-powered Q&A | Chat with data about any EV |
| Auction/listing integration | Connect with dealer inventory feeds |
| Deeper battery analytics | Charging history, degradation curves |

---

## 7. Technical Approach

### 7.1 Tech Stack
| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | Next.js 14 (App Router) | SSR, fast SEO, React ecosystem |
| Mobile | PWA | Mobile-first, no app store barrier |
| Backend | FastAPI (Python) | Async, great for data/ML integrations |
| Database | PostgreSQL + Redis | Relational data + caching |
| Search | Algolia | Fast faceted search for EV catalog |
| Hosting | Vercel (frontend) + Railway (backend) | Fast deployment |

### 7.2 Key Third-Party APIs
| API | Purpose | Cost |
|-----|---------|------|
| EVDB / EVKX | Vehicle specs | Free tier / paid |
| Aviloo | Battery SOH | Pay-per-query |
| Open Charge Map | Charging stations | Free |
| Algolia | Search | Free tier → ~$50/mo |

---

## 8. MVP Launch Plan

### Phase 1: Build (Month 1-3)
| Month | Milestone | Deliverables |
|-------|-----------|--------------|
| Month 1 | Foundations | Tech stack; repo; design system; data partnerships (EVDB, Aviloo, Open Charge Map); domain |
| Month 2 | Core features | EV catalog + filters + compare; AI quiz; TCO calculator with AU incentives |
| Month 3 | Trust features | Battery health grades; real-world range DB; charging readiness; trade-in estimator |

### Phase 2: Beta (Month 4-6)
| Month | Milestone | Deliverables |
|-------|-----------|--------------|
| Month 4 | Beta prep | Financing comparison; mobile-responsive; 50+ AU EVs loaded |
| Month 5 | Private beta | 10-20 real AU users; feedback collection; bug fixes |
| Month 6 | Refined beta | 100 users; Algolia tuned; onboarding optimized |

### Phase 3: Launch (Month 7-12)
| Month | Milestone | Deliverables |
|-------|-----------|--------------|
| Month 7 | AU Public Launch | All P0 features live; SEO + community outreach |
| Month 8-9 | US + DE expansion | TCO adapted; incentive detection for US (federal + state) and DE |
| Month 10-12 | Growth | P1 features (charging map, inspection reports) |

### Go-to-Market (AU)
| Channel | Strategy |
|---------|----------|
| EV forums | Reddit r/AussieTesla, r/ElectricVehicles, Facebook EV groups |
| Content | "10 things to check before buying a used EV in AU" |
| SEO | Target: "used EV AU", "EV TCO calculator AU", "battery health EV" |
| Early beta | Direct outreach to EV owners via forums |

---

## 9. Success Metrics

### 9.1 North Star Metric
| Metric | Definition | Target (90 days post-launch) |
|--------|------------|-------------------------------|
| Monthly Active Buyers | Users who complete TCO + view 3+ EVs | 500 MABs |

### 9.2 Key Metrics (KPIs)
| Metric | Target (6mo) | Measurement |
|--------|-------------|-------------|
| Beta signups | 500 | Email waitlist |
| DAU (beta) | 100 | Analytics |
| Quiz completion rate | 60% | Funnel |
| TCO uses/user | 2.5 | Analytics |
| Battery grade views | 30% of used EV visitors | Analytics |
| Charging readiness completions | 40% of quiz completers | Analytics |
| NPS | 40+ | In-app survey |
| Waitlist → beta conversion | 25% | Email |

---

## 10. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Aviloo API not available in AU | Medium | High | Recurrent as backup; manual inspection partner |
| Data partnerships take time | High | Medium | Scrape + seed initially; negotiate API access |
| AU EV market slower than expected | Medium | Medium | Pivotal to US + Germany if AU traction is slow |
| Charging infrastructure gaps in AU | High | Medium | Build home charging assessment + public map early |
| Competitor adds battery health | Low | High | Speed to market; first-mover brand equity |

---

## 11. Refined 30-Day To-Do Plan

### Week 1 — Data Partnerships + Foundations
- [ ] Sign up with **EVDB or EVKX** for vehicle spec API
- [ ] Contact **Aviloo / Recurrent** for battery health API (query pricing)
- [ ] Set up **Open Charge Map API** account (free)
- [ ] Register **CarScout domain** + placeholder landing page (waitlist)
- [ ] Create **Figma design system** (colors, typography, components)
- [ ] **Choose tech stack** (Next.js + FastAPI) + set up GitHub repo

### Week 2 — Tech Architecture + Data
- [ ] Build **database schema** (vehicles, specs, battery data, incentives)
- [ ] Set up **Algolia** search index for EV catalog (free tier)
- [ ] Connect **EVDB/EVKX API** — seed top 50 AU EV models
- [ ] Build **AU incentive database** (NSW, VIC, SA, WA)
- [ ] Set up **Vercel + Railway** hosting
- [ ] Draft **EV catalog UI** — browse grid + 5 faceted filters

### Week 3 — Core Features (MVP Backbone)
- [ ] Build **AI recommendation quiz** (5 questions → top 3 recs with TCO)
- [ ] Integrate **EV TCO calculator** with AU incentive auto-detect
- [ ] Integrate **battery health grade** from Aviloo (with fallback UI)
- [ ] Build **charging readiness assessment** (3-min quiz + recommendations)
- [ ] Integrate **real-world range database** with EVDB seed data

### Week 4 — Beta Preparation + Launch Plan
- [ ] Build **trade-in estimator** UI (CarsGuide data for AU estimates)
- [ ] Integrate **financing comparison** (partner lenders list)
- [ ] Add **multi-brand configurator** for top 20 AU EV models
- [ ] Write **beta onboarding flow** (email capture + quiz → recs)
- [ ] Set up **analytics** (Pagefunnel: quiz start/complete, TCO use, battery grade view)
- [ ] Create **waitlist landing page** + start EV forum outreach
- [ ] **Private beta invite** — 10-20 real AU EV buyers

---

## 12. Appendix

### Research Sources
- `~/Workspace/research/car-search-agent/2026-06-01-us-market.md`
- `~/Workspace/research/car-search-agent/2026-06-01-europe-market.md`
- `~/Workspace/research/car-search-agent/2026-06-01-australia-market.md`
- `~/Workspace/research/car-search-agent/2026-06-01-india-market.md`
- `~/Workspace/research/car-search-agent/2026-06-01-china-market.md`
- `~/Workspace/research/car-search-agent/2026-06-01-global-ev-trends.md`
- `~/Workspace/research/car-search-agent/2026-06-01-car-search-agent-prd.md`
- Notion AU MVP doc: `372ca7dc-fe68-8164-bfdd-dbe5949beb84`

### Document History
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | June 1, 2026 | Initial PRD from 6-region global research |
| 2.0 | June 2, 2026 | Consolidated with AU MVP Notion doc; refined to-do plan; phased launch |
