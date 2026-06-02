# HouseSmart — User Research

**Date:** June 2, 2026

---

## 1. User Personas

### Persona 1 — Priya, 34 (Melbourne) — Dual-Income Professional
**Grocery:** Woolworths weekly (AU$280/week). Too busy to compare prices or log nutrition.
**Primary hook:** Weekly grocery list + price savings identified automatically
**Churn risk:** High if app requires manual effort after setup

### Persona 2 — Marcus, 42 (Sydney) — Health-Focused Dad
**Grocery:** Coles + Costco (AU$320/week). Wants nutrition without meal logging.
**Primary hook:** Zero-effort nutrition from receipts — weekly family health summary
**Churn risk:** Low if nutrition reports are substantive; high if too basic

### Persona 3 — Jess, 22 (Perth) — Budget-Conscious Student
**Grocery:** ALDI primarily (AU$80/week). Very price-sensitive.
**Primary hook:** "ALDI saves you AU$14 this week vs Woolworths"
**Churn risk:** High if free tier is too limited; student pricing (AU$3.99/month) may help

---

## 2. Jobs-to-be-Done

1. **JTBD-1 (Scan):** "When I come home from shopping, I want to capture what I spent without doing any work so I have a complete purchase history."

2. **JTBD-2 (List):** "When I'm about to shop, I want to know exactly what I need based on what I actually buy so I never forget things or waste money on duplicates."

3. **JTBD-3 (Price):** "When I see my grocery bill, I want to know if I could have paid less and where, so I feel in control of my household costs."

4. **JTBD-4 (Nutrition):** "I want to know if my family's grocery choices are healthy without having to track every meal, so I can shop better without extra effort."

5. **JTBD-5 (Finance):** "I want my bank transactions and receipts to match up automatically so I have a real picture of where my household money goes."

---

## 3. Key Validation Questions

| Question | Validation Method | Success Threshold |
|---------|-----------------|-----------------|
| Will users scan receipts weekly? | 20-user prototype + 4-week beta | ≥ 70% scan ≥ 1/week |
| Is weekly list accurate enough? | In-app feedback ("Was this list useful?") | ≥ 80% "useful" rating |
| Will users pay AU$7.99? | Public beta free→paid conversion | ≥ 5% conversion at Month 3 |
| Is nutrition valuable without meal logging? | Feature engagement (report opens) | ≥ 50% of WAU open weekly |
| Will users connect their bank? | Beta bank connection rate | ≥ 40% of premium users |

---

## 4. Onboarding Flow

```
1. Welcome screen (value prop: 3 bullet points)
2. "Start with a recent receipt" → camera opens
3. Scan + result (first insight delivered in <3 min)
4. "Here's your weekly list preview" → 5 predicted items
5. "See your nutrition" → basic macro card
6. Optional: "Connect your bank for full picture"
7. Home screen — active, personalised, ready
```

**Principle:** Every onboarding step delivers immediate value. No dead ends.

---

## 5. Retention Mechanics

| Mechanic | Timing | Goal |
|----------|--------|------|
| Thursday grocery list push | Weekly (Thu 9am) | Drive weekly scan habit |
| Monday weekly recap | Weekly (Mon 8am) | Reflection + savings confirmation |
| Nutrition weekly digest | Sunday evening | Health awareness engagement |
| Price spike alert | Real-time | Urgency + savings ROI |
| Monthly milestone ("AU$120 saved!") | Monthly | Long-term value reinforcement |
| Streak counter ("6-week scan streak 🔥") | Ongoing | Gamification, habit formation |
