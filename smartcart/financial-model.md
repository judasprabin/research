# SmartCart — Financial Model

**Date:** June 2, 2026
**Version:** 1.0 — Pre-Revenue
**Assumptions:** AU market, 12-month projection, no external funding

---

## 💵 Cost Structure

### One-Time / Setup Costs
| Item | AUD | Notes |
|------|-----|-------|
| Domain + SSL | 50 | .app domain, Cloudflare |
| Logo + branding | 500 | Freelance designer |
| UI/UX design (Figma) | 2,000 | Freelance, ~20 screens |
| Landing page | 500 | Framer or simple custom |
| Total setup | **AU$3,050** | |

### Monthly Running Costs (at Phase 1 MVP, 1,000 MAU)
| Item | AUD/month | Notes |
|------|----------|-------|
| Supabase Pro | 25 | 500K row limit |
| Vercel (pro) | 20 | App + marketing site |
| Google Cloud Vision | 30 | 1,000 users × 4 scans/week × 4.3 weeks = 17,200 calls → ~AU$26 |
| Claude API (extraction + suggestions) | 30 | ~AU$0.0003/call × 50K calls |
| Open Food Facts | 0 | Free |
| Basiq API | 0 | Phase 2 only (free tier for MVP) |
| Sentry | 0 | Free tier |
| PostHog (self-hosted) | 0 | VPS ~AU$10/month (use for larger scale) |
| Email (SendGrid) | 0 | Free tier sufficient |
| Godaddy/AWS | 0 | Not needed yet |
| **Total monthly** | **~AU$105** | |

### Monthly Running Costs (at Phase 2 launch, 10,000 MAU)
| Item | AUD/month | Notes |
|------|----------|-------|
| Supabase Pro + add-ons | 75 | Overage on row limit |
| Vercel (pro) | 20 | |
| Google Cloud Vision | 300 | 10x users |
| Claude API | 200 | 10x users |
| Basiq API | 500 | ~100K transactions/month |
| PostHog (cloud) | 50 | Scale analytics |
| **Total monthly** | **~AU$1,145** | |

---

## 💰 Revenue Model

### Primary: Freemium Subscription
| Tier | Price | Features |
|------|-------|----------|
| Free | AU$0 | Receipt scan, 30-day history, basic list, basic nutrition |
| Premium | AU$6.99/month | All features + price compare + full nutrition + bank sync + export |

### Secondary Revenue Streams
| Stream | Potential | Realistic Year 1 |
|--------|----------|-----------------|
| Affiliate (Coles/Woolworths links) | 2–5% commission | ~AU$0 (not ready Y1) |
| FMCG data insights | AU$50K–200K/year (at scale) | ~AU$0 (Y1 too small) |
| White-label (insurers) | AU$20–100K/year (at scale) | ~AU$0 (Y1 focus on B2C) |

---

## 📈 User Growth Projections

| Month | Total Signups | WAU | WAU:Sigup ratio | Premium Users | Paying MRR |
|-------|-------------|-----|----------------|--------------|----------|
| 1 | 200 | 80 | 40% | 2 | AU$14 |
| 2 | 600 | 240 | 40% | 10 | AU$70 |
| 3 | 1,500 | 600 | 40% | 30 | AU$210 |
| 4 | 2,500 | 1,000 | 40% | 75 | AU$525 |
| 5 | 3,500 | 1,400 | 40% | 140 | AU$980 |
| 6 | 5,000 | 2,000 | 40% | 250 | AU$1,750 |
| 9 | 8,000 | 3,200 | 40% | 560 | AU$3,920 |
| 12 | 12,000 | 5,000 | 42% | 960 | AU$6,720 |

**Assumptions:**
- Free → Premium conversion: 5% of signups by Month 6, ramping to 8% by Month 12
- WAU:Signup ratio: 40% (consistent engagement)
- No paid acquisition in Year 1 (all organic + word-of-mouth)

---

## 📊 P&L Projection (12 Months)

### Revenue
| Month | Free Users | Paid Users | MRR (AU$) | Notes |
|-------|-----------|----------|---------|-------|
| 1 | 200 | 2 | 14 | Beta launch |
| 3 | 1,500 | 30 | 210 | Public beta |
| 6 | 5,000 | 250 | 1,750 | Soft launch |
| 9 | 8,000 | 560 | 3,920 | Growing |
| 12 | 12,000 | 960 | 6,720 | Full launch |

### Costs
| Month | Fixed Costs | API Costs | Total Costs | Cumulative |
|-------|------------|---------|-----------|-----------|
| 1–3 | ~AU$3,050 setup + AU$315/m × 3 = AU$3,995 | ~AU$105/m × 3 = AU$315 | **~AU$4,310** | AU$4,310 |
| 4–6 | AU$315/m × 3 = AU$945 | ~AU$200/m × 3 = AU$600 | **~AU$1,545** | AU$5,855 |
| 7–12 | AU$315/m × 6 = AU$1,890 | ~AU$600/m × 6 = AU$3,600 | **~AU$5,490** | AU$11,345 |

### Cumulative Position
| Milestone | Revenue | Costs | Net Position | Notes |
|-----------|---------|-------|-------------|-------|
| Month 6 | AU$1,750 × 6 months = ~AU$5,500 (total) | AU$5,855 | **-AU$355** | Near break-even |
| Month 12 | AU$6,720 × 12 months = ~AU$35,000 (total) | AU$11,345 | **+AU$23,655** | Profitable |

**Breakeven:** ~Month 6 at current growth rate.

---

## 🎯 Unit Economics

### Customer Acquisition Cost (CAC)
| Channel | CAC | Notes |
|---------|-----|-------|
| Organic (waitlist + Reddit + Product Hunt) | ~AU$2–5 | Content + time investment |
| Referral program | ~AU$8 | AU$5 credit + payment processing |
| Paid social (Meta/Google) | ~AU$15–25 | At scale, after PMF confirmed |

### Lifetime Value (LTV)
| Scenario | Monthly retention | Avg premium tenure | LTV | LTV:CAC |
|---------|-----------------|-------------------|-----|---------|
| Conservative | 70% month-over-month | 6 months | AU$42 | 2.8:1 |
| Base | 75% month-over-month | 8 months | AU$56 | 3.7:1 |
| Optimistic | 80% month-over-month | 12 months | AU$84 | 5.6:1 |

**Target:** LTV:CAC > 3:1 (conservative), > 5:1 (target for paid acquisition)

### LTV Calculation
```
LTV = ARPU × (1 / monthly churn)
    = AU$6.99 × (1 / 0.20)  [80% retention = 20% churn]
    = AU$6.99 × 5
    = AU$34.95 [conservative: 6 months avg tenure]

If monthly churn = 15% (85% retention):
LTV = AU$6.99 × (1/0.15) = AU$46.60
```

---

## 💡 Key Financial Insights

1. **API costs are the #1 variable cost** — Google Vision + Basiq scale with users/transactions. Monitor Basiq closely (potential surprise cost at scale).

2. **Premium conversion at 5% is the financial lever** — If conversion reaches 8%, MRR at Month 12 = AU$8,640 (28% higher). Focus product work here.

3. **Breakeven achievable at Month 6 without paid acquisition** — This is the key milestone. Before this, stay lean.

4. **Affiliate revenue is the upside** — At 10,000 MAU with 40% conversion to Coles/Woolies links, AU$200K/year potential (2% of AU$10M tracked spend). This is Year 2+ territory.

5. **Hiring is NOT planned for Year 1** — You (founder) build, plus AU$20K freelance budget for gaps. Keep fixed costs at ~AU$315/month until MRR hits AU$2,000.

---

## 🚨 Sensitivity Analysis

### What happens if premium conversion is only 3% (vs 5% base case)?
| Month 12 | Base Case | 3% Conversion |
|---------|----------|-------------|
| Paying users | 960 | 576 |
| MRR | AU$6,720 | AU$4,032 |
| Net position (12 months) | +AU$23,655 | +AU$13,500 |

Still profitable, but significantly lower. Conversion rate is the most important financial lever.

### What happens if Basiq costs 3x more at scale (10,000 users)?
| Basiq cost increase | Monthly ops cost increase |
|--------------------|--------------------------|
| AU$500 → AU$1,500 | AU$1,000/month |
| Year 2 extra cost | AU$12,000 |
| Impact | Reduces 12-month net by ~AU$9,000 |

Mitigation: Negotiate volume cap, have fallback provider (Akahu), build caching layer to reduce API calls.

### What happens if CAC increases to AU$25 (paid acquisition)?
- At AU$25 CAC and AU$46.60 LTV: LTV:CAC = 1.86:1 — not profitable for paid
- Paid acquisition only viable once LTV > AU$75 (i.e., after improving retention or raising price)
- Recommendation: Wait until Month 9+ before paid acquisition

---

## 📋 Financial Assumptions Summary

| Assumption | Value | Basis |
|-----------|-------|-------|
| Avg premium price | AU$6.99/month | Market rate (Netflix, Spotify AU) |
| Base free→paid conversion | 5% | Conservative for B2C freemium |
| Month 6 conversion | 5% | Target (confirmed by beta) |
| Month 12 conversion | 8% | Optimistic with better product |
| Monthly churn (paid) | 20% (base), 15% (good) | Freemium benchmarks |
| WAU:Signup ratio | 40% | Industry standard for utility apps |
| API cost per user/month | AU$0.15 (MVP) → AU$0.20 (Phase 2) | Google Vision + Claude |
| No external funding | — | Bootstrapped Year 1 |
