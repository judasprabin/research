# HouseSmart — Financial Model

**Version:** 1.0 | June 2, 2026

---

## 1. Cost Structure

### Setup Costs (One-off)
| Item | AUD |
|------|-----|
| Domain + SSL | AU$50 |
| Branding + logo | AU$500 |
| UI/UX design (20 screens) | AU$2,000 |
| Landing page | AU$500 |
| **Total setup** | **AU$3,050** |

### Monthly Running Costs

| Scale | 1K MAU | 5K MAU | 10K MAU |
|-------|--------|--------|--------|
| Supabase | AU$25 | AU$75 | AU$100 |
| Vercel | AU$20 | AU$20 | AU$20 |
| Google Vision | AU$30 | AU$150 | AU$300 |
| Claude API | AU$25 | AU$125 | AU$200 |
| Basiq | AU$0 | AU$250 | AU$500 |
| PostHog | AU$0 | AU$30 | AU$50 |
| Stripe fees | AU$0 | AU$70 | AU$250 |
| **Total/month** | **AU$100** | **AU$720** | **AU$1,420** |

---

## 2. Revenue Model

### Freemium Subscriptions
| Tier | Price | Target conversion |
|------|-------|-----------------|
| Free | AU$0 | 94% of users |
| Premium | AU$7.99/month | 5% by Month 6 |
| Family | AU$12.99/month | 1% by Month 9 |

### 12-Month Revenue Projection
| Month | Total Users | Paying | MRR (AU$) | Costs | Net |
|-------|------------|--------|----------|-------|-----|
| 1 | 200 | 0 | 0 | 100 | -100 |
| 2 | 500 | 5 | 40 | 100 | -60 |
| 3 | 1,500 | 30 | 240 | 150 | +90 |
| 4 | 2,500 | 75 | 600 | 200 | +400 |
| 5 | 3,500 | 140 | 1,120 | 350 | +770 |
| 6 | 5,000 | 300 | 2,400 | 720 | +1,680 |
| 9 | 8,000 | 600 | 4,800 | 900 | +3,900 |
| 12 | 12,000 | 1,100 | 8,800 | 1,420 | +7,380 |

**Breakeven: Month 3** (costs covered by revenue)
**First MRR milestone (AU$2K): Month 6**

---

## 3. Unit Economics

| Metric | Value |
|--------|-------|
| ARPU (premium) | AU$7.99/month |
| Monthly churn (paid) | 18% (target <15%) |
| Avg premium tenure | 6–8 months |
| LTV (base) | AU$7.99 / 0.18 = AU$44 |
| LTV (optimistic 12% churn) | AU$66 |
| CAC (organic, Month 6) | AU$5 |
| CAC (paid, Year 2) | AU$18 |
| LTV:CAC (organic) | **8.8:1** |
| LTV:CAC (paid, Year 2) | **2.4:1 → 3.7:1 as churn improves** |

---

## 4. 3-Year Revenue Scenarios

| Scenario | Year 1 MRR | Year 2 MRR | Year 3 MRR |
|---------|-----------|-----------|-----------|
| Conservative (3% conversion) | AU$3,600 | AU$12,000 | AU$25,000 |
| Base (5% conversion) | AU$8,800 | AU$24,000 | AU$55,000 |
| Optimistic (8% + affiliate) | AU$14,000 | AU$48,000 | AU$130,000 |

**Year 2+ upside:** FMCG data insights AU$30–100K/year + affiliate 2–5% commission.

---

## 5. Budget Allocation (First 12 Months)

| Category | AUD | % |
|----------|-----|---|
| Development (time + freelancers) | 20,000 | 47% |
| APIs + infrastructure | 5,000 | 12% |
| Design (UI/UX, branding) | 3,500 | 8% |
| Marketing + launch | 10,000 | 23% |
| Legal (privacy policy, T&Cs) | 1,500 | 4% |
| Buffer | 2,500 | 6% |
| **Total** | **AU$42,500** | 100% |

Within AU$50K bootstrap budget. ✅

---

## 6. Key Assumptions & Sensitivity

Every projection above rests on assumptions that have **not yet been validated**
with real users — treat the 12-month projection as a planning baseline to be
revisited monthly against actuals, not a forecast to manage toward rigidly.

| Assumption | Value used | Where it's validated |
|---|---|---|
| Free→paid conversion | 5% by Month 6 | `user-research.md` §3 Key Validation Questions — beta conversion rate |
| Paid monthly churn | 18%, improving to <15% | Needs a real cohort to measure; revisit this model the first month real subscriber data exists |
| Vision/Claude cost per scan | Implied ~AU$0.003 (Vision) + ~AU$0.0025 (Claude) per scan at 1K MAU scale | Validate against actual per-call pricing and average receipt length once the golden receipt set (`technical-architecture.md` §13) is in use — receipt length directly drives Claude token cost |
| Basiq cost scaling (AU$0 → AU$250 → AU$500 across MAU tiers) | Per-connection pricing assumed | Confirm actual Basiq pricing tier breakpoints before Phase 2 — `PRD.md` §9 Risk Register already flags this as a risk; this model is the place that risk gets re-priced when real numbers arrive |
| Setup cost (AU$3,050) | Excludes founder's own time | If design/branding is done in-house rather than contracted, reallocate that AU$2,500 to extended runway or paid acquisition testing |

**Trigger for re-running this model:** any of (a) Month-3 actual conversion <3%
(below even the conservative scenario), (b) Basiq quotes a per-MAU price >20%
above the assumption above, or (c) average Claude tokens/receipt exceeds estimate
by >50% (e.g. due to longer prompts after extraction-quality tuning).
