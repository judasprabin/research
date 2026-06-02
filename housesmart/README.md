# HouseSmart — Household Financial & Nutrition Intelligence Platform

> **"Scan once. Save money. Eat better."**

**Status:** Research Complete → Ready for Development
**Market:** Australia (Phase 1) → NZ / UK / CA (Phase 2+)
**Version:** 1.0 | June 2026

---

## 🧠 What Is HouseSmart?

HouseSmart is the single app that unifies everything a household does with money and food.

It replaces:
- Receipt scanning apps (that just scan, don't advise)
- Grocery list apps (that need manual input)
- Nutrition trackers (that require meal logging)
- Expense trackers (that don't understand groceries)
- Price comparison sites (that aren't personalised)

**Core loop:**
```
Snap any receipt or bill
      ↓
AI extracts items, prices, merchant, date
      ↓
Cross-references bank transactions automatically
      ↓
Tells you: what you need to buy, where it's cheapest,
           whether you're eating well, and what to cut
```

---

## 🔑 Five Core Modules

| Module | What It Does |
|--------|-------------|
| **📸 Smart Scan** | Camera-based OCR + AI extraction for ANY receipt or bill |
| **🛒 Grocery Brain** | Learns purchase rhythm → predicts weekly shopping list |
| **💰 Price Scout** | Shows where each item is cheapest across stores near you |
| **🥦 Nutrition Lens** | Calculates household vitamins/nutrients from grocery receipts — zero logging |
| **🏦 Money Map** | Open Banking sync → full household spend picture |

---

## 🌏 Origin Story

HouseSmart consolidates two product ideas:
- **BillScout** — AI finance agent: scan any bill, track all expenses, find cheaper options nearby
- **SmartCart** — Grocery intelligence: receipt → shopping list → cross-store price comparison → nutrition

Both ideas share the same core engine (receipt OCR + bank sync + price comparison). HouseSmart is the unified platform built on that engine — with grocery as the hero product and full household finance as the depth layer.

---

## 📁 Research Files

| File | Description |
|------|-------------|
| `PRD.md` | Full product requirements: features, MVP, roadmap, metrics, risks |
| `market-research-au.md` | Australian grocery + fintech market analysis |
| `competitor-analysis.md` | Cooklist, MyFitnessPal, Frollo, YNAB, Rocket Money and more |
| `user-research.md` | 3 personas, JTBD, onboarding, retention |
| `technical-architecture.md` | Full system design, APIs, DB schema, security |
| `design-concepts.md` | UX principles, screen flows, design system, visual direction |
| `gtm-plan.md` | Launch strategy: beta → soft launch → full launch |
| `financial-model.md` | Costs, revenue, unit economics, 12-month P&L |
| `roadmap.md` | Quarter-by-quarter roadmap with priorities and milestones |

---

## 📊 Key Numbers

| Metric | Value |
|--------|-------|
| AU Grocery Market | AU$125B/year |
| AU Household Finance App TAM | AU$2.8B/year |
| Combined SAM (HouseSmart) | ~AU$48B tracked spend |
| MVP Dev Budget | AU$20–25K |
| Breakeven | ~Month 7 |
| Target MRR (Month 12) | ~AU$8,500 |
| Premium Price | AU$7.99/month (free tier available) |

---

## 🗺️ Roadmap Summary

| Quarter | Focus | Ship |
|---------|-------|------|
| Q3 2026 | MVP | Scan + purchase history + grocery list + basic nutrition |
| Q4 2026 | AU Launch | Price comparison + bank sync + premium tier |
| Q1 2027 | Growth | Crowdsourced pricing + AI chat + multi-user |
| Q2 2027 | Scale | Referral + FMCG partnerships + NZ/UK prep |

---

## 🛠 Tech Stack

| Layer | Choice |
|-------|--------|
| Mobile | React Native + Expo |
| OCR | Google Cloud Vision API |
| AI extraction + chat | Claude API (Anthropic) |
| Nutrition DB | Open Food Facts + USDA FoodData |
| Bank sync | Basiq (AU Open Banking) |
| Backend | Supabase (PostgreSQL + Auth + Edge Functions) |
| Analytics | PostHog |
| Hosting | Vercel + Supabase |

---

## 🔗 Links

- GitHub: [judasprabin/research/housesmart](https://github.com/judasprabin/research/tree/main/housesmart)
- Built by: Prabin Karki
