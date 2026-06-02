# CarScout — Global EV-First Car Buying Platform
## Product Requirements Document (PRD)

**Date:** June 1, 2026
**Version:** 1.0 — Initial Research Draft
**Prepared by:** Hermes Product Research Agent
**Research Coverage:** US, Europe (Germany, France, UK, Norway), China, India, Australia

---

## Executive Summary

We are building **CarScout** — an AI-powered, EV-first comprehensive car buying companion for first-time buyers. Not a marketplace. Not a listing site. A complete car buying companion that helps users undertake *everything about a car* before they buy.

**Core Insight from Global Research:** No existing platform anywhere in the world has a complete EV buying companion experience. The biggest white spaces are:
1. **Battery health transparency** — zero platforms disclose State-of-Health for used EVs
2. **Real-world range data** — all use EPA/WLTP lab numbers, not real-owner data
3. **EV-native TCO calculators** — none stack federal + state incentives automatically
4. **Charging readiness assessment** — no platform tells you if you can charge at home
5. **Cross-border buying guide** — Europeans can't easily buy German cars from Netherlands

**Target:** First-time car buyers globally, EV-first positioning, targeting the 5 key markets: US, Europe, China, India, Australia.

**Moat:** The platform that gets battery health data, real-world range data, and TCO tools right first will own this category.

---

## 1. Product Overview

### 1.1 Product Name: CarScout

### 1.2 Tagline
*"Know everything about your car before you buy."*

### 1.3 Product Type
Global SaaS platform — web + mobile app (progressive web app initially)

### 1.4 Core Value Proposition

CarScout is the only platform that helps first-time EV buyers:
- **Understand the complete picture** — specs, real-world range, ownership costs, charging options, incentives, financing, insurance, and resale value — all in one place
- **Make a confident decision** — AI-powered recommendation engine + transparent data (battery health, real range, true cost) builds trust
- **Complete the purchase** — buy, finance, trade-in, register — all without leaving the platform

### 1.5 Target Market

| Market | Priority | EV Share (2025) | Notes |
|--------|----------|-----------------|-------|
| **US** | High | ~18-20% | Largest EV market after China, strong incentives |
| **Europe (Germany/UK/France)** | High | ~20-25% | Multiple markets, cross-border opportunity |
| **China** | Medium | ~35-40% | World's largest, but local players dominant |
| **India** | Medium | ~2-3% | Early stage, massive growth potential |
| **Australia** | Medium | ~8-12% | Small but growing, incentive gaps |

**Primary User:** First-time car buyer, 25-45 years old, researching a new or used EV (or considering EV vs. ICE), wants transparency and confidence before spending significant money.

---

## 2. Problem Statement

### 2.1 The Problem

First-time car buyers face a broken, fragmented experience:

| Pain Point | Current Reality |
|------------|-----------------|
| **Too much to research** | Must visit 10+ websites (manufacturer, dealer, review sites, forums, financing, insurance, government sites) |
| **No battery health transparency** | No platform tells you the actual health of a used EV's battery |
| **Range anxiety** | EPA/WLTP numbers are optimistic; real-world range can be 20-30% lower |
| **Incentive confusion** | Federal, state, local incentives — no platform aggregates eligibility |
| **Charging uncertainty** | Will I be able to charge at home? Where are the chargers? How much does it cost? |
| **True cost unknown** | Monthly payment ≠ true cost. Financing, insurance, maintenance, energy, depreciation |
| **Trust deficit** | Car dealerships have a trust problem globally; buyers fear being cheated |
| **Overwhelming choices** | 30+ EV models available, first-time buyers don't know where to start |

### 2.2 Problem Evidence

From global research across 5 markets:

- **US:** No platform has battery health data for used EVs. Carvana's 7-day return is good but doesn't address the "do I trust the battery?" question.
- **Europe:** No platform explains cross-border buying (saving €5,000-15,000). AutoScout24 has 19 countries but no buying guide.
- **China:** DongCheDi has video reviews but no battery health transparency. NIO has it but only for NIO vehicles.
- **India:** Most first-time buyers have never owned a car. No platform addresses the two-wheeler to four-wheeler transition needs.
- **Australia:** No platform shows real-world range in Australian conditions, nor state incentive eligibility.

---

## 3. Market Analysis

### 3.1 Global EV Market (2025-2026)

| Metric | Value |
|--------|-------|
| **Global EV sales (2025)** | ~18-20M units |
| **Global EV market share** | ~20-22% of total car sales |
| **TAM (Total Addressable Market)** | $2.4T global automotive market |
| **SAM (Serviceable Available Market)** | $400B (digital car buying platforms) |
| **SOM (Serviceable Obtainable Market)** | $5-20B (our realistic share in 5 years) |

**Sources:** IEA Global EV Outlook 2025, BloombergNEF EV Outlook 2025

### 3.2 Market Trends & Drivers

1. **Battery costs crossed $100/kWh** (2024-2025) — EVs now purchase-price-competitive with ICE in many markets
2. **Government incentives still matter** — but are evolving (EU subsidy cuts, US credit reform)
3. **Charging infrastructure improving** — but still the #1 barrier to EV adoption in emerging markets
4. **Direct-to-consumer sales models** — Tesla, BYD, OLA proving no dealerships needed for EVs
5. **AI-powered personalization** — ByteDance/DongCheDi algorithm is changing expectations

### 3.3 Market Risks

1. **Policy uncertainty** — EV incentives can be cut突然ly (Germany ended subsidies Dec 2023)
2. **Battery supply chain** — lithium/cobalt price volatility affects EV prices
3. **Charging infrastructure gaps** — especially in India, Southern Europe, rural Australia
4. **Adoption ceiling** — without affordable EV options, market growth may slow

---

## 4. Target Users

### 4.1 Primary Persona: "The Cautious First-Timer"

| Attribute | Description |
|-----------|-------------|
| **Name** | Priya Sharma |
| **Age** | 32 |
| **Location** | Mumbai, India (or Sydney, Australia, or Berlin, Germany) |
| **Income** | ₹15 lakh/year ($18k) / A$90k / €55k |
| **Car History** | Has never owned a car (two-wheeler user, or public transport) |
| **Goals** | Buy a reliable, affordable car that won't cost too much to run |
| **Pain Points** | Overwhelmed by choices, doesn't trust dealers, doesn't understand EVs |
| **Tech Comfort** | High — comfortable buying expensive things online |
| **Key Need** | Confidence that she's making the right choice at the right price |

### 4.2 Secondary Persona: "The Upgrade Seeker"

| Attribute | Description |
|-----------|-------------|
| **Name** | James Chen |
| **Age** | 40 |
| **Location** | California, US |
| **Income** | $120k/year |
| **Car History** | Currently drives a 2018 Toyota Camry, considering first EV |
| **Goals** | Switch to EV for savings + environmental reasons, but worried about range |
| **Pain Points** | Doesn't know if EV will work for his commute + occasional road trips |
| **Key Need** | "Will this EV actually save me money? Show me the math." |

### 4.3 Tertiary Persona: "The Tech Early Adopter"

| Attribute | Description |
|-----------|-------------|
| **Name** | Lena Müller |
| **Age** | 28 |
| **Location** | Berlin, Germany |
| **Income** | €65k/year |
| **Car History** | Has owned cars before, wants the latest tech |
| **Goals** | Get the best EV with the most tech features |
| **Pain Points** | Wants cross-border shopping to get better deals, doesn't know how |
| **Key Need** | "Help me compare across brands + show me what €50k gets me in Germany vs. Netherlands vs. France." |

---

## 5. Competitive Landscape

### 5.1 Direct Competitors

| Competitor | Strengths | Weaknesses | CarScout Advantage |
|------------|-----------|-----------|-------------------|
| **Tesla.com** | Best-in-class configurator, direct sales, Supercharger network | Only Tesla, no cross-shopping, no battery health for others | Multi-brand + battery health + TCO |
| **AutoScout24 (Europe)** | Multi-country, large inventory | No real EV tools, no battery health, no TCO | EV-native tools, battery SOH, TCO calculator |
| **CarDekho (India)** | EMI calculator, large traffic | No real EV tools, no battery health | Battery health, real range, EV TCO |
| **DongCheDi (China)** | Video reviews, AI recommendations | No cross-brand configurator, no battery health | Multi-brand configurator, battery SOH |
| **CarsGuide (Australia)** | Car recommendation quiz | No EV range data, no TCO, no state incentive finder | Real range data, TCO calculator, state incentive mapper |
| **Carvana (US)** | 7-day return, at-home delivery | No battery health, no real range data, no EV-native TCO | Battery SOH, real range, EV TCO |

### 5.2 Competitive Differentiation Strategy

1. **Battery Health First** — Be the first platform globally to show battery State-of-Health on every used EV listing
2. **Real-World Range** — Aggregate owner-reported range data, show "real range" not lab numbers
3. **EV TCO Calculator** — Show true cost of ownership including all incentives automatically
4. **Charging Readiness** — Tell buyers if they can charge at home + what it will cost
5. **Cross-Border Guide** — Help European buyers save €5,000+ by buying from the right country

---

## 6. Product Vision

### 6.1 Vision Statement

> "Every car buyer deserves the same level of information transparency that a Tesla engineer has about their car."

### 6.2 Mission Statement

> "Build the world's most comprehensive car buying companion — one that helps first-time buyers understand everything about a car before they buy, making the transition to EVs confident, transparent, and accessible."

### 6.3 Principles

1. **Transparency above all** — Show the good and the bad. If an EV has poor real-world range, say so. If battery health is degraded, show it.
2. **Data-driven decisions** — Every recommendation is backed by real data, not marketing copy.
3. **Simplicity** — First-time buyers are overwhelmed. We make the complex simple.
4. **Global but local** — One platform, locally adapted. EV incentives, charging infrastructure, and buying processes differ by country — we adapt to each market.
5. **Trust through verification** — We verify everything. Battery health, range data, incentive eligibility, dealer reviews — all verified.

---

## 7. Feature Requirements

### 7.1 MVP Features (P0 — Must Have for Launch)

#### P0-1: Multi-Brand EV Catalog
- **What:** Search and browse all EV models available in your country
- **Why:** First-time buyers need to see all options, not just one brand
- **Scope:** All new EVs from all major manufacturers (BEV only for MVP, PHEV later)

#### P0-2: AI Car Recommendation Engine
- **What:** "What car should I buy?" quiz — input budget, lifestyle, priorities → get ranked recommendations with reasoning
- **Why:** First-time buyers don't know where to start
- **Implementation:** Rule-based quiz initially, AI-enhanced in v2

#### P0-3: EV TCO Calculator
- **What:** Calculate true monthly cost of EV vs. ICE
- **Inputs:** Purchase price, federal incentives, state incentives, annual mileage, home electricity cost, financing terms
- **Outputs:** Monthly cost comparison, 3-year total cost, 5-year total cost, break-even point
- **Key differentiator:** Automatically pulls incentive eligibility based on user's location/state

#### P0-4: Battery Health Grade (for used EVs)
- **What:** Show battery State-of-Health (SOH) as a letter grade (A-F) for every used EV listing
- **Implementation:** Partner with Aviloo (Europe/US), Recurrent (US), NIO API (China), or require OBD reporting from sellers
- **Why:** The #1 trust gap in used EV market

#### P0-5: Charging Readiness Assessment
- **What:** Input your home address + housing type → get charging options + installation cost estimate + available rebates
- **Why:** First-time EV buyers don't know if they can charge at home
- **Scope:** US, Europe, Australia initially (India later as charging infrastructure matures)

#### P0-6: State/Federal Incentive Eligibility Checker
- **What:** Auto-detect user's location → show all incentives they qualify for with exact dollar amounts
- **Why:** Most buyers don't know all the incentives available to them
- **Coverage:** All US states, major European countries, Australia states

#### P0-7: Real-World Range Database
- **What:** Owner-reported real-world range data per model (summer, winter, highway, city)
- **Why:** EPA/WLTP numbers are misleading — real range is 15-25% lower
- **Implementation:** Crowdsourced owner reports + data partnerships

#### P0-8: Trade-in Value Estimator
- **What:** Input current car → get instant trade-in offer or estimate
- **Why:** Buyers want to know what their current car is worth before shopping
- **Implementation:** Integrate with Kelley Blue Book (US), AutoScout24 (Europe), etc.

#### P0-9: Financing Comparison
- **What:** Compare loan offers from multiple banks/lenders in one place
- **Why:** First-time buyers don't know if they're getting a good financing deal
- **Implementation:** API partnerships with banks/lenders per market

#### P0-10: Multi-Brand EV Configurator
- **What:** Configure any EV from any brand in one place (colors, options, packages)
- **Why:** Buyers want to compare options across brands without visiting 10 different websites
- **Implementation:** Build/configurator per OEM, aggregated in one interface

### 7.2 P1 Features (Should Have — Post MVP)

| Feature | Description | Priority Rationale |
|---------|-------------|-------------------|
| **Used EV Listings with Battery SOH** | Full inventory of used EVs with battery health grades | Core to trust differentiation |
| **Insurance Comparison** | Compare EV-specific insurance premiums | Completes the ownership cost picture |
| **Charging Network Map** | Integrated charging station map with real-time availability | Addresses range anxiety |
| **Cross-Border Buying Guide** | Step-by-step guide for EU cross-border car buying | Major value add for European buyers |
| **360° Vehicle Inspection Reports** | Verified inspection data for used EVs | Trust builder for used car purchases |
| **Service Network Quality by Location** | Show dealer/service center quality scores | Helps buyers choose which brand to buy |
| **EV vs. ICE Depreciation Model** | Show expected depreciation curve for EVs vs. ICE | First-to-market insight |
| **V2G Earnings Estimator** | Show how much buyers could earn from vehicle-to-grid | Tech-forward buyer appeal |

### 7.3 P2 Features (Nice to Have — Future Roadmap)

| Feature | Description |
|---------|-------------|
| **Battery-as-a-Service Aggregation** | Show BaaS options from NIO and others |
| **EV Subscription Aggregator** | Compare all-brand EV subscriptions in one place |
| **Live Stream Car Sales** | DongCheDi-style live commerce for car buying |
| **AR Car Configurator** | Place car in real-world environment (Autohome-style) |
| **Social Proof Engine** | Show what friends/contacts bought + their reviews |
| **AR Test Drive** | VR/Mixed reality test drive experience |
| **AI Negotiation Assistant** | AI that helps negotiate with dealers |

---

## 8. User Experience

### 8.1 User Flow

```
Landing Page
    ↓
"What car should I buy?" Quiz → AI Recommendations
    ↓
Browse EVs (all brands, filtered by quiz results)
    ↓
Compare EVs (side-by-side specs, range, price, TCO)
    ↓
Select EV → Configure (colors, options, packages)
    ↓
Used vs. New path:
  - Used: View battery health grade + inspection report
  - New: Configure + see incentives
    ↓
Calculate Ownership Cost (TCO Calculator)
    ↓
Get Trade-in Value (for current car)
    ↓
Apply Financing (compare lenders)
    ↓
Apply Insurance (compare EV insurance)
    ↓
Calculate Total Cost (incentives + taxes + fees)
    ↓
Purchase (buy/finance/instant trade-in)
    ↓
Post-Purchase: Charging setup guide, service scheduling, ownership tools
```

### 8.2 Key Screens

| Screen | Purpose | Key Elements |
|--------|---------|--------------|
| **Home / Quiz** | Entry point, orient first-time buyers | Quiz CTA, popular EVs, incentives highlight |
| **Browse / Search** | Find all EVs | Filters (range, price, brand, body type), sort, compare toggle |
| **EV Detail** | Complete car info | Specs, real-world range, TCO, incentives, battery health (used), reviews |
| **Compare** | Side-by-side comparison | 2-4 EVs, all specs, cost comparison, recommendation highlight |
| **Configure** | Build your car | Color picker, options, packages, total price with OTD cost |
| **Ownership Calculator** | TCO + incentives | Monthly cost, 3yr/5yr total, incentive breakdown |
| **Purchase** | Complete the deal | Financing application, trade-in, delivery/pickup options |
| **My Garage** | Post-purchase | Charging guide, service schedule, resale value tracker |

### 8.3 Onboarding

1. **Quiz first** — Don't dump 100 EVs on new users. Start with 5 questions → personalized recommendations.
2. **Incentive highlight** — On day 1, show "You may qualify for $X in incentives" based on location.
3. **Charging reality check** — Early in journey, ask "Where will you charge?" → set realistic expectations.

---

## 9. Technical Approach

### 9.1 Tech Stack (MVP)

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Frontend** | React + Next.js (web), React Native (mobile) | Fast development, good developer ecosystem |
| **Backend** | Node.js / Python FastAPI | Reliable, scalable |
| **Database** | PostgreSQL (relational) + MongoDB (documents) | Vehicle specs (relational), user data (document) |
| **Search** | Algolia | Fast car search with faceted filters |
| **AI/ML** | OpenAI / Anthropic APIs | Recommendation engine, content generation |
| **Hosting** | Vercel (frontend) + AWS/GCP (backend) | Scalable, global CDN |
| **Payments** | Stripe | Financing integration, payment processing |

### 9.2 Key Technical Decisions

| Decision | Choice | Trade-offs |
|----------|--------|-----------|
| **Build vs. buy vehicle data** | Partner with EVDB/EVKX + OEM APIs | Faster time-to-market vs. data dependency |
| **Battery health integration** | Partner with Aviloo/Recurrent | They have the OBD hardware + data |
| **Charging network data** | Open Charge Map API | Free, global, but slow real-time data |
| **Maps** | Mapbox or Google Maps API | Mapbox is cheaper, Google has better coverage |

### 9.3 Data Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  OEM APIs   │────▶│  Vehicle    │────▶│  Search     │
│  (specs)    │     │  Database   │     │  Index      │
└─────────────┘     └─────────────┘     └─────────────┘
                          │                    │
                          ▼                    ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Battery    │────▶│  User       │────▶│  TCO        │
│  Health API │     │  Profiles   │     │  Calculator│
└─────────────┘     └─────────────┘     └─────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Purchase   │
                    │  Flow       │
                    └─────────────┘
```

### 9.4 API Design

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/vehicles` | GET | Search/filter EVs |
| `/api/vehicles/:id` | GET | Full vehicle detail |
| `/api/vehicles/:id/specs` | GET | Technical specifications |
| `/api/vehicles/:id/real-range` | GET | Real-world range data |
| `/api/battery-health/:vin` | GET | Battery SOH grade + details |
| `/api/calculate-tco` | POST | TCO calculation with inputs |
| `/api/incentives` | GET | All incentives for location |
| `/api/charging-readiness` | POST | Home charging assessment |
| `/api/trade-in` | POST | Trade-in value estimate |
| `/api/financing/quotes` | POST | Get financing quotes |

### 9.5 Third-Party Services

| Service | Purpose | Est. Monthly Cost |
|---------|---------|------------------|
| **EVDB / EVKX** | Vehicle spec data | $500-2,000/month |
| **Aviloo API** | Battery health data | $0.10/report or revenue share |
| **Open Charge Map** | Charging station data | Free (donations) |
| **Algolia** | Search | $500-2,000/month |
| **Mapbox** | Maps | $500-1,500/month |
| **OpenAI** | AI features | $1,000-5,000/month |
| **AWS/GCP** | Hosting | $2,000-10,000/month |
| **Total** | | **$5,000-22,000/month** |

---

## 10. Launch Plan

### 10.1 MVP Scope (Target: 6 months to launch)

**In Scope:**
- Multi-brand EV catalog (US + Germany initially)
- AI recommendation quiz
- EV TCO calculator (US + Germany)
- Battery health grade (US + Europe via Aviloo)
- Charging readiness assessment (US)
- Federal/state incentive checker (US)
- Real-world range database (owner-reported)
- Trade-in value estimator (US via KBB)
- Financing comparison (US — partnerships)
- Multi-brand configurator (top 10 brands)
- Responsive web app (mobile-first)

**Out of Scope (v2):**
- Used EV inventory (just links to dealer listings)
- Insurance comparison
- Charging network map
- Cross-border buying guide
- 360° inspection reports
- Post-purchase tools

### 10.2 Launch Milestones

| Milestone | Target | Deliverables |
|-----------|--------|--------------|
| **Kickoff** | Month 1 | Design system, tech stack, data partnerships |
| **Alpha** | Month 3 | Working prototype, internal testing |
| **Beta (Private)** | Month 5 | 100 real users in US + Germany |
| **Public Launch** | Month 6 | Full MVP, marketing campaign |
| **v1.1** | Month 9 | Insurance, charging map, used EVs |
| **v1.2** | Month 12 | India, Australia, UK launches |
| **v2** | Month 18 | China, cross-border guide, V2G tools |

### 10.3 Go-to-Market (GTM)

| Channel | Strategy | Target |
|---------|----------|--------|
| **Content Marketing** | "First-time EV buyer guide" + SEO | Organic traffic from search |
| **Community** | EV owner communities (Reddit, forums, Facebook groups) | Word-of-mouth + reviews |
| **Partnerships** | OEM partnerships for data + co-marketing | Credibility + data |
| **Influencers** | YouTube/TikTok EV reviewers | Reach first-time buyers |
| **Paid Search** | "EV buying" keywords | Capture high-intent users |
| **Referral** | "Tell a friend" + incentives | Viral growth |

---

## 11. Success Metrics

### 11.1 North Star Metric

| Metric | Definition | Target (12 months) |
|--------|------------|-------------------|
| **Decisions Enabled** | Number of users who complete TCO calculation and either save to garage or submit financing inquiry | 50,000 users |

### 11.2 Key Metrics (KPIs)

| Metric | Baseline | Target (6 months) | Target (12 months) |
|--------|----------|-------------------|-------------------|
| **Monthly Active Users** | 0 | 10,000 | 100,000 |
| **Quiz Completion Rate** | N/A | 40% | 50% |
| **TCO Calculator Users** | 0 | 5,000/month | 50,000/month |
| **Battery Health Lookup** | 0 | 2,000/month | 20,000/month |
| **Financing Inquiries** | 0 | 500/month | 5,000/month |
| **NPS Score** | N/A | 40+ | 55+ |
| **Conversion (MAU → paid)** | N/A | 1% | 3% |

### 11.3 Funnel Metrics

```
Awareness (SEO + paid + referral)
    ↓ 10% click-through
Landing Page
    ↓ 40% start quiz
Quiz Started
    ↓ 50% complete
Quiz Completed
    ↓ 30% browse EVs
EV Browse
    ↓ 20% use TCO calculator
TCO Calculator
    ↓ 10% save to garage
Garage (Intent)
    ↓ 5% submit financing
Financing Inquiry
    ↓ (track to purchase once purchase flow live)
Purchase Complete
```

---

## 12. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **OEM data partnerships fail** | Medium | High | Build scraper fallback + EVDB backup |
| **Battery health API unreliable** | Medium | Medium | Only show grade if data quality is high; else show "no data" |
| **Aviloo/Recurrent exclusivity deals** | Low | High | Sign partnership agreements early; build alternative data sources |
| **Competitor (Tesla, BYD) builds this first** | Medium | High | Move fast + focus on multi-brand (they won't) |
| **Incentive policies change drastically** | Medium | Medium | Build flexible incentive engine; update data frequently |
| **Low user trust in early days** | Medium | High | Focus on transparency + verify everything; seed with real owner reviews |
| **Charging infrastructure gaps cause range anxiety** | High | Medium | Be honest about charging limitations; set realistic expectations |

---

## 13. Appendix

### 13.1 Glossary

| Term | Definition |
|------|------------|
| **BEV** | Battery Electric Vehicle (plug-in, no ICE) |
| **PHEV** | Plug-in Hybrid Electric Vehicle |
| **SOH** | State of Health — battery capacity relative to new |
| **TCO** | Total Cost of Ownership |
| **TAM** | Total Addressable Market |
| **SAM** | Serviceable Available Market |
| **SOM** | Serviceable Obtainable Market |
| **EPA** | US Environmental Protection Agency (range ratings) |
| **WLTP** | Worldwide Harmonized Light Vehicle Test Procedure (EU range ratings) |
| **OBD** | On-Board Diagnostics (car diagnostic port) |
| **BaaS** | Battery-as-a-Service |
| **V2G** | Vehicle-to-Grid |
| **ICE** | Internal Combustion Engine |
| **MSRP** | Manufacturer's Suggested Retail Price |
| **OTD** | Out-the-Doors (total cost including taxes/fees) |

### 13.2 Research Sources

| Market | Source |
|--------|--------|
| **US** | 2026-06-01-us-market.md (full research file) |
| **Europe** | 2026-06-01-europe-market.md (full research file) |
| **China** | 2026-06-01-china-market.md (full research file) |
| **India** | 2026-06-01-india-market.md (full research file) |
| **Australia** | 2026-06-01-australia-market.md (full research file) |
| **Global Trends** | 2026-06-01-global-ev-trends.md (full research file) |

All research files located at: `~/career-ml/research/car-search-agent/`

### 13.3 Competitive Feature Matrix (Global)

| Feature | Tesla | Carvana | AutoScout24 | CarDekho | DongCheDi | CarsGuide | CarScout |
|---------|-------|---------|-------------|----------|-----------|-----------|----------|
| Multi-brand search | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Real-world range | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Battery SOH | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| TCO calculator | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Charging readiness | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Incentive auto-detect | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |
| AI recommendations | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Cross-brand configurator | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Cross-border guide | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| V2G estimator | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

---

**Document Status:** Draft — Research Complete, PRD Initialized

**Last Updated:** June 1, 2026

**Next Steps:**
1. Review with stakeholders
2. Prioritize features (P0 vs. P1 vs. P2)
3. Technical architecture design
4. Data partnership negotiations
5. Design system setup