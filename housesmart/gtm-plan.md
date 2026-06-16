# HouseSmart — Go-to-Market Plan

**Date:** June 2, 2026 | **Market:** Australia (Phase 1)

---

## 1. Launch Sequence

| Phase | Timeline | Users | Channel Focus |
|-------|---------|-------|--------------|
| Phase 0 — Waitlist | Jul 2026 | 200+ | Personal network, Reddit |
| Phase 1 — Closed Beta | Aug–Sep 2026 | 500 | TestFlight, Waitlist |
| Phase 2 — Public Beta | Oct 2026 | 1,000 | Product Hunt, Reddit |
| Phase 3 — Soft Launch | Nov 2026 | 5,000 | Social, referral, PR |
| Phase 4 — Growth | Jan 2027+ | 12,000+ | Paid + referral |

---

## 2. Pre-Launch (July 2026)

### Waitlist Landing Page
- **URL:** housesmart.app
- **Headline:** "Scan once. Save money. Eat better."
- **Sub-headline:** "The only app that turns your grocery receipts into real savings and nutrition insights — automatically."
- **CTA:** "Join the waitlist — get 3 months free premium on launch"
- **Tool:** Framer (fast, great mobile preview)
- **Target:** 200 signups in 4 weeks

### Social Presence Setup
- Instagram @housesmartapp — product demo reels
- Twitter/X @housesmartapp — product updates + AU grocery data
- LinkedIn company page — PR + investor + talent

---

## 3. Beta Launch (Aug–Sep 2026)

### Channel Mix
| Channel | Effort | Expected users |
|---------|--------|---------------|
| Personal/professional network | Low | 50 |
| Reddit (r/ausfinance, r/australia) | Medium | 150 |
| LinkedIn post (founder story) | Low | 50 |
| Facebook groups (budget living AU) | Medium | 100 |
| Instagram DM to micro-influencers | High | 150 |
| **Total** | | **500** |

### Reddit Strategy (Organic, Non-Spammy)
- Post: "I built a receipt scanner that predicts your weekly grocery list — here's what I found after tracking 3 months of receipts"
- Thread: r/ausfinance — "Does anyone actually track grocery spending? Here's what ours looked like"
- Comment: Participate authentically, mention app when relevant only

---

## 4. Public Launch (Oct–Nov 2026)

### Product Hunt Launch
- **Target:** Top 5 Product of the Day
- **Prep:** 50+ hunters lined up for Day-1 upvotes, rich gallery, 60-second demo video
- **Timing:** Tuesday launch (highest traffic day)
- **Expected:** 500–1,000 signups from PH alone

### PR Outreach
| Target | Angle |
|--------|-------|
| SmartCompany.au | "AU startup building the smart grocery app" |
| StartupAUS | New launch story |
| Business Insider AU | "How this app can save Australian families AU$800/year on groceries" |
| Mama Mia / Kidspot | Nutrition Lens angle (family health) |

---

## 5. Growth Phase (Jan 2027+)

### Paid Acquisition (starts after AU$2K MRR)
| Channel | Target CAC | Targeting |
|---------|-----------|----------|
| Meta (Instagram) | AU$15–20 | Lookalike of beta users, interest: grocery, budgeting, health |
| Google App Install | AU$10–15 | Keywords: receipt scanner, grocery tracker, grocery list |
| TikTok | AU$8–12 | Demo videos, "how much I saved" content |

### Referral Program (Phase 3)
- **Mechanic:** Share referral link → referee gets 1 week free premium → referrer gets AU$5 premium credit
- **Target:** 15% of new installs from referral by Month 9

---

## 6. Metrics Dashboard

| KPI | Month 3 | Month 6 | Month 12 |
|-----|---------|---------|---------|
| Total signups | 1,500 | 5,000 | 12,000 |
| WAU | 600 | 2,000 | 5,000 |
| Receipts/WAU/week | 2 | 3 | 3.5 |
| MRR | AU$240 | AU$2,400 | AU$8,800 |
| NPS | 20 | 35 | 45 |
| CAC (organic) | AU$3 | AU$5 | AU$8 |
| LTV (premium) | AU$40 | AU$50 | AU$60 |

---

## 7. Compliance & Kill Criteria for Marketing Claims

- Any "AU$X saved" claim in marketing (ads, App Store copy, PR pitches like the
  Business Insider "AU$800/year" angle in §4) must be substantiated by real
  aggregate user data per the ACL requirement in `PRD.md` §10 — do not publish a
  projected/illustrative savings number as if it were measured, even pre-launch.
  Track this explicitly: don't finalise the Business Insider/SmartCompany pitch
  numbers until beta data exists to back them.
- Referral program (§5) terms must state credit value, expiry, and "not redeemable
  for cash" clearly in-app before launch — required for both app store policy and
  ACL.
- Each waitlist/beta promotional offer (e.g. "3 months free premium") needs an
  explicit expiry and eligibility rule decided before the landing page ships, to
  avoid an open-ended liability against the financial model in `financial-model.md`.

## 8. Channel Kill Criteria

Don't keep funding a channel past its validation point — define the bar before spending:

| Channel | Kill/scale signal |
|---|---|
| Reddit organic (§3) | If 2 posts generate <20 combined signups, stop and reallocate to influencer DMs |
| Product Hunt (§4) | This is a one-shot event — failure to crack Top 10 is not a reason to delay growth phase, just lowers Day-1 signup expectations |
| Paid Meta/Google/TikTok (§5) | Kill any channel where realised CAC exceeds 1.5× the target CAC in the table above for 2 consecutive weeks, rather than letting it run on hope |
| Referral program (§5) | If referral share of installs is <5% by Month 6 (vs 15% target by Month 9), revisit the incentive size before Month 9, don't wait for the deadline to pass |
