# SmartCart — User Research

**Date:** June 2, 2026
**Scope:** User Personas, Jobs-to-be-Done, Validation Questions

---

## 👥 User Personas

### Persona 1: "Time-Poor Priya" — Dual-Income Professional
**Age:** 34 | **Location:** Melbourne (inner suburb) | **Income:** AU$145K household
**Devices:** iPhone 14, Apple Watch, MacBook

**Profile:** Priya and her husband both work full-time. They have a toddler and a dog. Grocery shopping happens Sunday morning (Woolworths, plus fortnightly ALDI run). Receipts go straight in the bin. They have a rough mental budget but no tracking. They偶尔 worry about whether they're eating healthily enough for the toddler.

**Grocery behaviour:**
- Shops Woolworths weekly + ALDI fortnightly
-，平均 weekly spend ~AU$280
- Uses Woolies online app for top-up shops mid-week
- Doesn't compare prices across stores systematically
- Buys organic milk and pre-cut vegetables (convenience over price on some items)

**Pain points:**
- "I always forget what we actually ran out of — end up improvising"
- "No idea if ALDI would actually save us money or just on some things"
- "I know I should track what we eat but I literally don't have 20 minutes to log food"
- "We waste so much produce that goes off before we use it"

**Quotes:**
- "I'd love to know if we're spending too much on groceries but tracking it sounds like a part-time job"
- "The nutritionist at the childcare centre keeps saying 'eat more iron' — but I have no idea if we are or aren't"

**SmartCart hooks:**
- [ ] Receipt scan — zero effort, just snap and done
- [ ] Weekly list — predicts what they're running low on
- [ ] Price comparison — shows which store saves them money per trip
- [ ] Nutrition — "You're low on Iron this week, here's 3 ideas to fix it"

**Churn risk:** If the app requires too much manual input after the initial excitement wears off. Must deliver suggestions automatically.

---

### Persona 2: "Fitness-Focused Marcus" — Health-Conscious Parent
**Age:** 42 | **Location:** Sydney (North Shore) | **Income:** AU$220K household
**Devices:** Pixel 8, Garmin Fenix, MacBook Pro

**Profile:** Marcus cycles 3x/week, weight training 2x/week. He and his wife are health-conscious but not obsessively so. They have two teenage kids. They shop at Coles + Costco monthly. Marcus uses MyFitnessPal but admits he only logs workouts, not food consistently. He's curious about nutrition but finds calorie counting tedious.

**Grocery behaviour:**
- Shops Coles weekly + Costco monthly bulk buy
- Buys protein-rich foods, whole grains, vegetables
- Costco run = bulk rice, pasta, protein supplements
- Spends ~AU$320/week
- Occasionally looks at unit prices but not systematically

**Pain points:**
- "I log about 40% of my meals in MyFitnessPal — mostly just to feel like I tried"
- "I know Costco is good value but some things there are a rip-off and I don't realise until later"
- "Is my family actually eating enough protein? No idea."
- "Every couple of weeks we throw out a whole bag of salad that went man根"

**Quotes:**
- "I want to eat better without having to think about it all the time"
- "The Macros are the thing I care about most — protein especially"

**SmartCart hooks:**
- [ ] Nutrition from receipt — weekly protein/carb/fat totals without logging
- [ ] Vitamin D / Iron flags — links to health goal (cycling = iron-deficiency risk)
- [ ] Costco price analysis — is the bulk buy actually saving?
- [ ] Price comparison — Coles vs Costco on staple items

**Churn risk:** Lower churn risk if nutrition hooks are strong. High risk if weekly nutrition reports are too basic.

---

### Persona 3: "Budget-Conscious Jess" — University Student
**Age:** 22 | **Location:** Perth (suburban) | **Income:** AU$38K part-time + HECS
**Devices:** Samsung A54, Windows laptop

**Profile:** Jess lives in a shared rental. She does the weekly grocery shop for herself (and sometimes her mum's place too). She's very price-conscious — checks the Coles/Woolworths catalogues every week, shops at ALDI for staples. She has a HECS debt and is trying to save for a post-graduation trip. Her phone is mid-range, not top-of-the-line.

**Grocery behaviour:**
- Shops ALDI primarily, Coles occasionally for specific items
- Weekly spend ~AU$70-90
- Reads catalogues, compares unit prices
- Uses HelloFresh occasionally when broke/tired
- Very price-sensitive on staples (rice, pasta, bread, milk)

**Pain points:**
- "Everything is so expensive now — I need to know I'm getting the best deal"
- "I comparison shop between Coles and ALDI but it takes so much time"
- "Sometimes I buy something at Coles and then see it cheaper at ALDI and feel so dumb"
- "I know my spending is out of control but I don't have a system to track it"

**Quotes:**
- "Show me the cheapest option and I'll probably use it — I don't care about brand"
- "I want to save money without having to become one of those extreme coupon people"

**SmartCart hooks:**
- [ ] Cross-store price comparison — ALDI vs Coles on everything she bought
- [ ] Savings tracker — "You overspent by AU$23 this week vs. your average"
- [ ] Weekly list — what she needs this week at the right store
- [ ] Budget alerts — "You're at 85% of weekly grocery budget with 4 days to go"

**Churn risk:** HIGH — if the free tier is too limited, she'll churn. Premium at AU$6.99/month is borderline for her budget. Consider student pricing (AU$3.99/month).

---

## 🪣 Jobs-to-be-Done (JTBD)

### JTBD 1: "When I come home from shopping, I want to quickly capture what I spent so I can understand my grocery patterns without doing any work myself"
**Core job:** Effortlessly record and understand grocery spend
**Metric:** Time to scan a receipt after shopping (target: <30 seconds)
**Acceptable outcome:** Historical view of spending by category and store
** exceptional outcome:** "I discovered I spend AU$800/year on snacks I didn't realise I was buying"

### JTBD 2: "When I'm about to do my weekly shop, I want to know exactly what I need so I don't forget anything or buy things I already have"
**Core job:** Get a personalised, accurate shopping list based on my household's actual consumption
**Metric:** % of list items that are actually needed (target: ≥ 80%)
**Acceptable outcome:** List of items predicted to run out this week
**Exceptional outcome:** "SmartCart reminded me to buy something I would have completely forgotten — like dishwashing tablets — and saved me a second trip"

### JTBD 3: "When I buy groceries, I want to know if I'm getting a good price compared to other stores so I don't feel like I'm being ripped off"
**Core job:** Get personalised price intelligence across stores I actually shop at
**Metric:** Number of price savings identified per week (target: ≥ 3)
**Acceptable outcome:** "Buy X at Y instead of Z — save $N"
**Exceptional outcome:** "SmartCart told me my average basket would cost $47 less at ALDI than Coles — I'm switching my main shop"

### JTBT 4: "I want to know if my family's grocery choices are actually healthy without having to count every meal"
**Core job:** Get household-level nutrition overview from existing purchasing behaviour
**Metric:** % of weekly nutrition recommendations that feel actionable
**Acceptable outcome:** Weekly macro summary (protein, carbs, fat)
**Exceptional outcome:** "My family was low on Vitamin D and Calcium and SmartCart suggested 3 affordable things to add — we actually did it"

### JTBD 5: "When I check my bank account, I want SmartCart to automatically show me where my grocery money went without me having to reconcile receipts"
**Core job:** Automatic receipt-to-transaction matching with zero effort
**Metric:** % of grocery transactions automatically matched (target: ≥ 75%)
**Acceptable outcome:** "Grocery spend this month: $1,240 across Coles, Woolies, ALDI"
**Exceptional outcome:** "One transaction didn't match — SmartCart showed me which receipt it was and I confirmed it — now the full picture is there"

---

## ⚠️ Key Assumptions & Validation Questions

### Must-Validate (Pre-MVP)
1. **Will people scan their receipts?** Assumption: habit can be formed. Validation: 20-user prototype, 70% complete scan-to-list flow
2. **Is there enough AU supermarket receipt data for good price comparison?** Assumption: sufficient UPC coverage in Open Food Facts. Validation: manually test 200 receipts — if >80% items map, proceed
3. **Will AU users pay AU$6.99/month for premium?** Assumption: price comparison concrete savings justify premium. Validation: free beta → paid conversion ≥ 5% at Month 3

### Should-Validate (Beta)
4. **Is bank connection rate ≥ 40%?** Depends heavily on trust and onboarding UX
5. **Does nutrition summary drive retention?** Hypothesis: nutrition weekly digest is the hook for health-motivated users
6. **Is 2,000-user target achievable in 3 months?** Depends on channel mix (see GTM plan)

### Key Risks to Validate Early
7. **ALDI receipt format** — ALDI receipts are notoriously minimal (few itemised products). Must confirm accuracy on ALDI receipts before building roadmap around this.
8. **Open Food Facts AU coverage** — Test coverage before claiming nutrition accuracy publicly
9. **Price comparison data sufficiency** — Need minimum ~50 receipts per user per store before suggestions are personalised enough to be valuable

---

## 🔄 Onboarding & Retention Mechanics

### Onboarding (Critical — first 5 minutes matter most)
1. **Email sign-in** (30 seconds)
2. **Quick scan prompt** (camera pre-opened) — "Snap your last receipt, we'll do the rest" (2 minutes)
3. **See first insight** — "You've spent AU$X over the last week. Here are your top 3 categories." (30 seconds)
4. **Weekly list preview** — "Based on your history, we think you'll run out of these 8 items this week" (1 minute)
5. **Nutriton summary teaser** — "See what your cart says about your nutrition" (30 seconds)
6. **Optional: Connect bank** — "Add your bank for automatic expense tracking" (not required for core use)

**Critical:** Every step must deliver immediate value. Zero dead-end screens.

### Retention Mechanics
| Mechanic | Target behavior | Frequency |
|----------|----------------|-----------|
| Weekly digest push | "Your week in groceries — 12 items scanned, $47 saved" | Weekly (Monday AM) |
| Shopping list reminder | "Your list is ready — 8 items predicted, 3 on sale this week" | Thursday AM |
| Price spike alert | "Eggs are up 20% at Coles this week — ALDI still cheaper" | Real-time |
| Nutrition weekly | "Your nutrition score: 74/100 — add more fibre this week" | Weekly (Sunday) |
| Milestone badges | "50 receipts scanned — you\'ve identified $340 in savings!" | Milestone |

---

## 📏 Success Metrics for User Research

| Validation Question | Success Criterion | Method |
|--------------------|-----------------|--------|
| Will users scan receipts? | ≥ 70% complete scan flow | Prototype test (20 users) |
| Will they keep scanning weekly? | ≥ 30% Week 4 retention | Closed beta (500 users) |
| Is the weekly list accurate? | ≥ 80% list accuracy rated "useful" | In-app feedback |
| Will they pay for premium? | ≥ 5% free→paid conversion | Public beta (2,000 users) |
| Is NSM achievable? | ≥ 25% of WAU hit full NSM | Product analytics |
