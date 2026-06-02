# SmartCart — Australian Grocery Market Research

**Date:** June 2, 2026
**Prepared for:** SmartCart Product Assessment
**Scope:** Australian Grocery Retail Market — Digital Trends, Consumer Behaviour, Competitive Landscape, Regulatory Environment

---

## 📊 Australian Grocery Market at a Glance

| Metric | Value (2025) | Trend |
|--------|-------------|-------|
| Total Grocery Retail (AU$G) | ~AU$125B/year | +3.2% YoY |
| supermarket/拗汁 grocery share | ~65% of retail food spend | Stable |
| Online grocery penetration | ~15% (~AU$18.75B) | +22% YoY |
| Grocery delivery subscriber households | ~3.2M | Growing |
| Avg weekly household grocery spend | ~AU$277 (~AU$14,400/year) | +5% YoY |
| Annual household food waste | ~AU$3,000 in discarded food | Cost opportunity |
| Smart shopping app adoption | ~18% of households | Growing |

**Sources:** Woolworths Annual Report 2025, IBISWorld Grocery Retailing in Australia 2025, Statista 2025.

---

## 🏪 Major Players & Market Share

### Market Share (2025, supermarket channel)
| Retailer | Est. Share | Stores | Positioning |
|----------|-----------|--------|-------------|
| Woolworths | ~37% | ~1,050 | Premium, widest range |
| Coles | ~28% | ~850 | Value, convenience |
| ALDI | ~12% | ~590 | Low price, limited range |
| IGA/Metcash | ~10% | ~1,400 | Independent, local |
| Costco | ~4% | ~15 | Bulk, membership |
| Others | ~9% | — | Harris Farm, Foodland, etc. |

**Key insight:** The duopoly (Woolies + Coles) controls ~65% of the market. ALDI is the primary price-disruptor. Price comparison between these stores is the highest-value feature for SmartCart users.

### Private Label Growth
- Woolworths "Everyday" and Coles "Smart Buy" private labels now account for ~28% of units sold
- ALDI exclusively private label — strong price anchor
- Private label margin is 20–30% higher than branded goods — supermarket data on what people buy is commercially sensitive

---

## 🛒 Consumer Behaviour & Pain Points

### How Australians Shop
- **Frequency:** 2.3 trips/week to supermarket (Woolworths/Coles data)
- **Spontaneous purchasing:** ~43% of basket is unplanned (choice overload, in-store placement)
- **Price awareness:** 71% of Australians actively check for specials before shopping (Roy Morgan 2025)
- **Multi-store shopping:** ~38% of households shop at 2+ stores to get the best price
- **Receipt retention:** ~65% of consumers bin receipts immediately; ~20% keep briefly for warranty; <5% track historically

### Key Consumer Pain Points
1. **"I always forget what I need"** — No unified view of pantry/what's running low
2. **"Prices are different everywhere"** — No tool tracks real across-store prices
3. **"Nutrition tracking is too much effort"** — Existing apps require meal logging (behavioral barrier)
4. **"I don't know if I'm getting good value"** — No context on whether a deal is actually good
5. **"Bank transactions don't match receipts"** — Manual reconciliation is painful

**SmartCart's addressable pain:** All five. This is why the "receipt → insight → action" loop is the core product loop.

---

## 📱 Digital Grocery & App Landscape in Australia

### Current Digital Grocery Adoption
- **Woolworths Online:** ~2M active customers, ~AU$2.8B revenue (2025)
- **Coles Online:** ~1.5M active customers, ~AU$1.9B revenue (2025)
- **Direct-to-consumer grocery apps:** <3% market share (Amazon Fresh, Ezzentials)
- **Grocery list/meal planning apps:** ~18% penetration among smartphone users

### Relevant Adjacent App Categories
| Category | Leading Apps | Monthly Active Users (AU) |
|----------|-------------|------------------------|
| Budget/Expense tracking | YNAB, Lunar, Frollo | ~500K combined |
| Meal planning | HelloFresh, Mayr, Cooklist | ~300K |
| Nutrition tracking | MyFitnessPal, Lose It! | ~800K |
| Receipt scanning | Fetch Rewards (US), ReceiptHero | <100K |

**Opportunity:** The intersection of expense tracking + nutrition + smart shopping lists has no dominant player in AU.

---

## 🔓 Open Banking in Australia

### Regulatory Framework
- **Consumer Data Right (CDR):** Mandated by ACCC, phased rollout
- **Banking sector:** Opened to CDR from July 2020; Basiq, Illion, Frollo are accredited
- **Required for SmartCart:** Bank transaction sync (Feature 5, Phase 2)

### Basiq API — AU Open Banking
Basiq is the leading aggregator for AU fintech apps:
- Connects 90%+ of AU financial institutions (300+ institutions)
- Handles consent, token refresh, transaction categorisation
- Pricing: ~AU$0.02–0.05 per transaction (tiered volume pricing)
- CDR-compliant out of the box

**Alternative:** Akahu (NZ, some AU banks), Plaid (primarily US/UK, limited AU)

**SmartCart recommendation:** Basiq as primary, Akahu as secondary. Build abstraction layer so bank provider is swappable.

---

## 📐 Regulatory Environment

### Privacy & Data (AU)
- **Privacy Act 1988 (Cth):** 13 Australian Privacy Principles (APPs) govern collection, use, storage, disclosure
- **Sensitive information:** Financial data is not "sensitive" but is regulated — must be minimised, secured, not shared without clear consent
- **Notifiable Data Breaches (NDB) scheme:** Must notify OAIC within 30 days of qualifying breach
- **Spam Act 2003:** Push notifications require explicit opt-in consent

### Consumer Law
- **Australian Consumer Law (ACL):** App must not make misleading claims (e.g., "save $X" must be substantiated)
- **Genuine vs. puffery:** Any savings claims must be verifiable
- **Food claims:** If app makes nutrition suggestions, must not claim to diagnose or treat health conditions — qualifies as "health advice" regulated by TGA

### Food / Nutrition
- **TGA:** App cannot claim to diagnose, treat, or cure disease through nutrition suggestions
- **Safe Food Australia / FSANZ:** Not applicable to app (only food manufacturers)
- **Workaround:** Frame suggestions as "general dietary guidance" not medical advice; include disclaimer

### App Store Compliance
- **Apple App Store / Google Play:** AU privacy policies, age restrictions (16+), no deceptive practices
- **In-app purchases:** Must clearly disclose subscription terms

---

## 💡 SmartCart-Specific Market Opportunity

### Total Addressable Market (TAM) Calculation

**AU Urban Households (18–55, digitally active):**
- AU urban population ~20M → ~8.5M households → target segment ~3.2M households

**Annual spend on groceries for target segment:** ~AU$14,400/household × 3.2M = **~AU$46B/year**

**SmartCart addressable (receipt scanning opportunity):**
- Even at 10% penetration = AU$4.6B in tracked spend
- At 0.5% commission on affiliate = AU$23M revenue potential
- At AU$6.99/month premium × 5% conversion × 160K paying users = **~AU$670K ARR**

### Seasonal / Cyclical Patterns
- **January:** Health/nutrition resolution bump — highest signup potential
- **EOFY (June):** Budget/finance app interest rises
- **Pre-Christmas (Nov–Dec):** High grocery spend — highest price-comparison value
- **Back-to-school (Jan/Feb):** Family budget focus — strong for household nutrition features

### Competitive Moat Building (Timing Advantage)
- Open Banking in AU is maturing — Basiq only launched 2019, CDR is still <5 years old
- No app currently combines receipt scan + price compare + nutrition from scan data
- **First mover advantage:** If SmartCart achieves 50K users scanning weekly before Coles/Woolworths build in-house, the data moat becomes defensible

---

## 🌍 International Expansion Potential

After AU validation (Phase 4), priority expansion markets:

| Market | Rationale | Priority |
|--------|----------|----------|
| New Zealand | Similar retail landscape, Basiq covers NZ banks | 1st |
| United Kingdom | Open Banking mature (Plaid UK, TrueLayer), large grocery market | 2nd |
| Canada | Open Banking emerging, Similar grocery landscape | 3rd |
| Singapore | High digital adoption, open banking in progress | 4th |

---

## 🔑 Key Market Insights Summary

1. **AU$125B market, 2-player duopoly** — Coles + Woolworths own 65% of supermarket spend; price comparison between them is highest-value feature
2. **18% app adoption is low** — massive headroom for smart grocery tools
3. **38% multi-store shoppers** — cross-store price comparison has strong latent demand
4. **Open Banking is live in AU** — Basiq makes bank sync feasible today
5. **No dominant player** in the receipt → insight → action space for AU grocery
6. **Privacy compliance is manageable** — Privacy Act + CDR; well-documented, Basiq handles bank compliance
7. **January signup spike** — health resolution market is highest-ROI launch window
8. **First-mover data moat** — if SmartCart gets 50K weekly scanners first, competitor imitation becomes costly
