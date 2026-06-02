# SmartCart — Research

> 🛒 Household intelligence app: scan receipts, save money, eat better.

**Status:** Research Phase — Ready for Development
**Market:** Australia (Phase 1), Global (Phase 2+)
**Prepared by:** Prabin Karki

---

## 🧠 What is SmartCart?

SmartCart is an all-in-one household intelligence app that turns your grocery receipts into real savings and nutrition insights — automatically.

### The Problem
- 65% of people bin receipts immediately — no purchase history
- No app tracks real prices across Australian supermarkets
- Nutrition tracking requires meal logging (high friction, low adherence)
- Budget apps don't understand grocery patterns

### The Solution
SmartCart combines five features no single app currently offers in one place:

1. **📸 Receipt Scanning** — Snap your receipt, we extract everything (items, prices, store, date)
2. **🛒 Weekly Shopping List** — AI learns your purchase rhythm and predicts what you need
3. **💰 Cross-Store Price Comparison** — Shows where you save money (Coles vs Woolworths vs ALDI)
4. **🥦 Nutrition from Grocery** — Household-level vitamin/nutrient summary from what you bought
5. **🏦 Bank Transaction Tracking** — Open Banking sync for automatic expense reconciliation

---

## 📁 Research Files

| File | Purpose |
|------|---------|
| `PRD.md` | Full product requirements: features, metrics, roadmap, risks, tech stack |
| `market-research-au.md` | Australian grocery market analysis, Open Banking, regulatory environment |
| `competitor-analysis.md` | Deep dive on Cooklist, MyFitnessPal, Frollo, AnyList, and others |
| `user-research.md` | 3 personas, jobs-to-be-done, onboarding design, validation plan |
| `technical-research-report.md` | Architecture, APIs, database schema, security, cost estimates |
| `gtm-plan.md` | Launch strategy: beta → soft launch → full launch → paid acquisition |
| `financial-model.md` | Cost structure, revenue model, unit economics, P&L projection |

---

## 📊 Key Numbers

| Metric | Value |
|--------|-------|
| AU Grocery Market | AU$125B/year |
| Households in AU | ~10.4M |
| SAM (target segment) | ~AU$46B/year |
| MVP Development Cost | ~AU$20–25K (freelance + time) |
| MRR at Month 12 (base case) | ~AU$6,720 |
| Breakeven | ~Month 6 |
| Premium Price | AU$6.99/month (free tier available) |

---

## 🗺️ Roadmap

| Phase | Timeline | Focus |
|-------|---------|-------|
| **Phase 1** | Months 1–3 | MVP: Receipt scan + list + basic nutrition |
| **Phase 2** | Months 4–6 | AU launch: Price compare + bank sync + vitamin alerts |
| **Phase 3** | Months 7–12 | Engagement: Crowdsourced pricing + recipes + multi-user |
| **Phase 4** | Year 2 | Monetisation + NZ/UK expansion |

---

## 🔑 SmartCart's Differentiator

> **The only app calculating nutrition from what you bought — not what you logged.**

| Feature | SmartCart | MyFitnessPal | Cooklist |
|---------|----------|-------------|---------|
| Receipt scan | ✅ | ❌ | ❌ |
| Cross-store price compare | ✅ | ❌ | ❌ |
| Nutrition from grocery | ✅ | ❌ (meals only) | ❌ |
| AU bank sync | ✅ | ❌ | ❌ |
| Zero-effort nutrition | ✅ | ❌ | ❌ |

---

## 🛠 Tech Stack (Selected)

| Layer | Choice |
|-------|--------|
| Mobile | React Native / Expo |
| OCR | Google Cloud Vision API |
| AI extraction | Claude API (Anthropic) |
| Nutrition DB | Open Food Facts (free) + USDA |
| Bank sync (AU) | Basiq API |
| Backend | Supabase |
| Hosting | Vercel + Supabase |

Full technical details → `technical-research-report.md`

---

## 🚀 Next Steps

1. **Prototype test** — 20-user test of core scan → list flow (Week 1–4)
2. **Build Phase 1 MVP** — Receipt scan + list + basic nutrition (Months 1–3)
3. **Closed beta** — 500-user TestFlight + Play Store beta (Month 3)
4. **Public beta** — 2,000-user public launch + Product Hunt (Month 4)
5. **Soft launch** — Full AU market, referral program, paid acquisition (Month 6+)

---

## 📞 Contact

Built by **Prabin Karki** — reach out on [LinkedIn](https://linkedin.com/in/judasprabin) or via GitHub issues.

If you want to contribute research, open a PR or issue.
