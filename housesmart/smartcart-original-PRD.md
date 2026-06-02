# SmartCart — App Idea Document

_Prepared on May 5, 2026_

---

## 🧠 Concept Overview

SmartCart is an all-in-one household intelligence app that combines:

- grocery receipt scanning
- weekly shopping suggestions
- cross-store price comparison
- nutritional analysis from grocery purchases
- bank transaction tracking

It brings together features that no single app currently offers in one place.

---

## 📸 Feature 1: Bill & Receipt Photo Scanning

**Status:** Exists in pieces, not unified

SmartCart uses your phone camera to scan paper bills or grocery receipts and extract:

- item names
- quantities
- prices
- store names
- purchase dates

The app then:

- auto-categorises spending (groceries, utilities, rent, etc.)
- builds a historical price database per item per store

### Benefits

- fast, automated expense capture
- searchable purchase history
- accurate item-level pricing trends

---

## 🛒 Feature 2: Weekly Grocery Shopping Suggestions

**Status:** Partially exists but not bill-driven — this is your differentiator

Based on scanned receipt history, SmartCart learns your household buying rhythm and predicts what’s running low this week.

### What it does

- detects purchase frequency for each item (for example, milk every 5 days)
- predicts what is likely running out in the next week
- generates a personalised weekly shopping list
- accounts for family size and past quantity habits

### Why it matters

- moves beyond recipe planners
- suggests what you actually need
- uses real purchase behavior instead of manual list creation

---

## 💰 Feature 3: Better Price Options at Alternative Shops

**Status:** Biggest gap in the market — almost nobody does this well

The app builds a real price comparison database from your own receipt history and shows where each item is cheapest.

### What it provides

- item × store price history based on your scans
- suggestions like “Buy this at Aldi instead of Coles — save $12 this week”
- cheapest total basket calculator across stores
- crowdsourced pricing from other users over time

### Competitive advantage

- personalised price savings
- data from your actual shopping behavior
- strong long-term moat if crowdsourced pricing grows

---

## 🥦 Feature 4: Total Vitamins & Nutrition Calculation from Grocery

**Status:** Genuinely novel — no app currently does this from grocery receipts

Instead of tracking meals, SmartCart calculates nutrition from what you bought and gives a household-level nutrition summary.

### What it calculates

- maps grocery items to nutrition databases (USDA / Open Food Facts)
- calculates weekly vitamin and mineral totals for the household
- flags deficiencies, for example:
  - “Your cart this week is low on Iron and Vitamin D”
- suggests additions such as:
  - “Add spinach or eggs to fix your Iron gap”

### Why it matters

- simplifies nutrition oversight for busy households
- links purchasing decisions to health outcomes
- supports smarter shopping, not just cooking

---

## 🏦 Feature 5: Banking Transaction Tracking

**Status:** Well established — easiest to integrate

SmartCart connects bank accounts through Open Banking APIs and matches transactions to receipts.

### Core functionality

- Open Banking API integration (Plaid, Basiq for Australia)
- auto-tags grocery, utilities, dining out, and other categories
- matches bank transactions to scanned receipts for reconciliation
- provides a monthly household spend dashboard

---

## 📊 Competitive Gap Analysis

| Feature                        | Cooklist | Rocket Money | MyFitnessPal | Groceries Tracker | SmartCart |
| ------------------------------ | :------: | :----------: | :----------: | :---------------: | :-------: |
| Receipt photo scan             |    ✅    |      ❌      |      ❌      |        ✅         |    ✅     |
| Weekly shop suggestions        |    ✅    |      ❌      |      ❌      |        ❌         |    ✅     |
| Price compare across stores    |    ❌    |      ❌      |      ❌      |      Partial      |    ✅     |
| Vitamin/nutrition from grocery |    ❌    |      ❌      |  Meals only  |        ❌         |    ✅     |
| Bank transaction tracking      |    ❌    |      ✅      |      ❌      |        ❌         |    ✅     |

---

## 🛠️ How to Build It Solo (AUD 50K Budget)

### Recommended Tech Stack

- Frontend: React Native (single codebase for iOS + Android)
- OCR / Receipt Scanning: Google Vision API or AWS Textract
- Nutrition Data: Open Food Facts API (free) or USDA FoodData Central
- Bank Sync: Plaid (US/UK) or Basiq (Australia)
- AI Suggestions: Claude API or OpenAI
- Backend: Supabase (fast, low cost)

### MVP Scope — Phase 1

- receipt photo scan and item extraction
- expense tracking dashboard
- weekly shopping list based on purchase history
- basic nutrition summary from cart

### Phase 2

- price comparison across stores
- bank transaction sync
- vitamin deficiency alerts and recommendations
- crowdsourced pricing from other users

### Estimated Budget Breakdown

- MVP development (freelancers + your time): AUD 15,000–25,000
- APIs & infrastructure (year 1): AUD 3,000–5,000
- marketing & launch: AUD 5,000–10,000
- buffer / iteration: AUD 10,000–15,000
- Total: within AUD 50,000

---

## 💼 Monetisation Ideas

- **Freemium:** free basic receipt scanning and expense tracking; premium tier (~$5–9/month) for nutrition insights, price comparisons, and bank sync
- **Affiliate:** earn commission when users buy groceries via partner stores
- **Data insights:** anonymised shopping trend reports sold to FMCG brands
- **White label:** licence technology to supermarkets or health insurers
