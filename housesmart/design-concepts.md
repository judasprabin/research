# HouseSmart — Design Concepts & UX Direction

**Version:** 1.0 | June 2, 2026
**Status:** Concept → Ready for Design Sprint

---

## 1. Design Philosophy

### Principle 1: "Intelligent Invisibility"
The best interface is one that disappears. HouseSmart should feel effortless — the AI does the work, the user just confirms. Maximum insight from minimum input.

### Principle 2: "Concrete Over Abstract"
Never show percentages or vague labels. Always translate to dollars saved, days of food left, deficiency in plain English. "AU$14 saved this week" beats "optimised spend".

### Principle 3: "One Action Per Screen"
Each screen has one primary action. No menu overload. No feature carousels. Reduce decision fatigue at every step.

### Principle 4: "Progressive Disclosure"
Show the summary. Let the user go deeper if they want. Don't front-load complexity.

---

## 2. Visual Identity

### Brand Personality
Warm, smart, trustworthy, Australian. Not clinical (MyFitnessPal) or playful-childish. Think: the friend who happens to be a financial planner AND a nutritionist, casually helping you out.

### Colour Palette
```
Primary:     #1B4332  — Deep Forest Green (trust, nature, money)
Accent:      #40916C  — Mid Green (interactive, calls to action)
Surface:     #F8FAF9  — Near-white warm tint (backgrounds)
Card:        #FFFFFF  — Pure white (cards, modals)
Highlight:   #D8F3DC  — Light mint (positive savings, wins)
Warning:     #FFF3CD  — Amber tint (budget alerts)
Error:       #FFE0E0  — Soft red (deficiencies, overspend)
Text:        #1B2A25  — Deep near-black
Text muted:  #6B7C77  — Warm grey
```

### Typography
- **Display:** Plus Jakarta Sans (700/800) — headlines, numbers
- **Body:** Inter (400/500) — all UI text
- **Mono:** JetBrains Mono — prices, amounts (makes numbers scannable)

### Iconography
- Custom line icons (Figma)
- 24px default, 32px for tab bar
- Rounded corners, 1.5px stroke
- No emoji in navigation (use sparingly in copy only)

### Elevation & Shadow
```
Card shadow: 0 2px 8px rgba(0,0,0,0.06)
Modal shadow: 0 8px 32px rgba(0,0,0,0.14)
Button press: scale(0.97) + shadow reduction
```

---

## 3. App Structure

### Navigation: 5-tab bottom bar
```
[ 📸 Scan ] [ 🛒 List ] [ 💰 Prices ] [ 🥦 Nutrition ] [ 💳 Money ]
```

The scan tab is always tab 1 — that's the habit we're building.

### Home / Scan Tab (default landing)
```
┌────────────────────────────────┐
│  Good morning, Priya 👋        │
│  Week 23 · 4 receipts scanned  │
├────────────────────────────────┤
│  ┌─────────────────────────┐  │
│  │  📸 TAP TO SCAN          │  │
│  │  Point at any receipt    │  │
│  └─────────────────────────┘  │
├────────────────────────────────┤
│  THIS WEEK'S SNAPSHOT          │
│  💰 AU$14 identified savings   │
│  🥦 Iron low this week         │
│  🛒 8 items predicted for Thur │
└────────────────────────────────┘
```

### Post-Scan Screen (receipt result)
```
┌────────────────────────────────┐
│  ✅ Woolworths · 2 Jun · $87.40 │
│  Scanned 14 items               │
├────────────────────────────────┤
│  ITEMS                          │
│  Milk 2L              $2.80    │
│  Chicken breast       $12.00   │
│  Eggs 12-pack         $5.50    │
│  ...                           │
│  [Tap item to correct]         │
├────────────────────────────────┤
│  PRICE INSIGHTS                │
│  🔴 Eggs: AU$1.20 cheaper ALDI │
│  🟢 Milk: best price here      │
├────────────────────────────────┤
│  [ Save & Close ]              │
└────────────────────────────────┘
```

### Grocery List Tab
```
┌────────────────────────────────┐
│  Your List · Week of 2 Jun     │
│  8 items · est. AU$64          │
├────────────────────────────────┤
│  PREDICTED LOW                 │
│  ○ Milk 2L         ~2 days    │
│  ○ Eggs 12pk       ~4 days    │
│  ○ Bread           ~1 day 🔴  │
├────────────────────────────────┤
│  YOU USUALLY BUY               │
│  ○ Chicken breast              │
│  ○ Rice 2kg                    │
├────────────────────────────────┤
│  [＋ Add item] [Share list]    │
└────────────────────────────────┘
```

### Nutrition Tab
```
┌────────────────────────────────┐
│  Nutrition Lens · Week 23      │
│  Based on 14 items scanned     │
├────────────────────────────────┤
│  MACROS          You / Weekly  │
│  Protein         ████░ 72%    │
│  Carbs           ████████ 95% │
│  Fat             █████░ 63%   │
├────────────────────────────────┤
│  ⚠️ LOW THIS WEEK              │
│  Iron            ██░░░ 35%    │
│  Vitamin D       █░░░░ 18%    │
├────────────────────────────────┤
│  💡 Add spinach + salmon       │
│     to fix Iron & Vitamin D    │
│  [Add to list AU$8.90]         │
└────────────────────────────────┘
```

### Money Map Tab
```
┌────────────────────────────────┐
│  Money Map · June 2026         │
├────────────────────────────────┤
│  TOTAL SPENT                   │
│  AU$1,840  ↑12% vs May         │
├────────────────────────────────┤
│  BY CATEGORY                   │
│  🛒 Groceries   AU$612  33%   │
│  🍽️ Dining      AU$289  16%   │
│  🚗 Transport   AU$210  11%   │
│  ⚡ Utilities   AU$318  17%   │
│  📦 Other       AU$411  22%   │
├────────────────────────────────┤
│  ⚠️ Electricity up AU$82 vs avg│
│  [View breakdown]              │
└────────────────────────────────┘
```

---

## 4. Key UX Flows

### Flow 1: First Scan (Onboarding)
```
Welcome screen (value proposition)
  → "Start with a recent receipt" [Scan now]
  → Camera opens full-screen
  → User scans receipt
  → Processing animation (2-4 seconds)
  → Result screen: items extracted, editable
  → "Here's what we found!" → savings insight + list preview
  → [Continue to set up weekly list] → prompt household size
  → Home screen with pre-populated data
```
**Goal:** Get user to their first insight within 3 minutes of signup

### Flow 2: Weekly Thursday List Push
```
Thursday 9am push: "Your list is ready — 8 items, est. AU$64"
  → Tap → Grocery Brain tab
  → Items sorted by: Running out soonest (top)
  → Each item shows: cheapest store + price
  → [Start shopping] → checks off as user goes
  → Post-shop: "Did you find everything?" → confirm/correct
  → Confirmation triggers: receipt scan prompt
```

### Flow 3: Bank Connection (Premium Onboarding)
```
[Upgrade to Premium] →
  → "Connect your bank for automatic expense tracking"
  → Trust walkthrough: "Read-only. Encrypted. You can disconnect anytime."
  → Basiq institution picker (search by bank name)
  → Basiq hosted OAuth → user authenticates
  → Return to app: "Syncing last 3 months..."
  → Money Map populated
  → Matched receipts highlighted: "12 receipts matched to transactions ✅"
```

---

## 5. Micro-interactions & Animations

| Trigger | Animation |
|---------|-----------|
| Scan button tap | Camera iris opening animation |
| OCR processing | Scanning line sweeping over receipt |
| Receipt saved | Items "fly" into history with satisfying pop |
| Savings identified | AU$ amount counts up (number ticker) |
| List item checked | Strike-through + slight green flash |
| Nutrition bar filling | Bar fills with easing on load |
| Push notification | Gentle bounce + haptic |

---

## 6. Component Library (Design System)

### Tokens
```
spacing-xs: 4px
spacing-sm: 8px
spacing-md: 16px
spacing-lg: 24px
spacing-xl: 32px

radius-sm:  8px
radius-md: 12px
radius-lg: 20px
radius-full: 9999px

font-display: Plus Jakarta Sans
font-body:    Inter
```

### Core Components
| Component | Notes |
|-----------|-------|
| `<ScanButton>` | Large circular, pulsing idle animation |
| `<ReceiptCard>` | Expandable, shows items accordion |
| `<GroceryListItem>` | Swipeable (left = delete, right = add note) |
| `<NutritionBar>` | Animated fill, colour-coded by coverage % |
| `<SavingsChip>` | Green pill: "Save AU$1.20 at ALDI" |
| `<InsightCard>` | Callout card with icon + CTA button |
| `<BudgetRing>` | Circular progress ring for budget tracking |

---

## 7. Design Deliverables (Phased)

### Phase 1 (Pre-MVP, 2 weeks)
- [ ] Brand identity: logo, colours, typography (Figma)
- [ ] Core screens: Scan, List, Nutrition, Home (hi-fi mockups)
- [ ] Component library: 20 core components in Figma
- [ ] Prototype: Scan → Result → List flow (InVision or Figma)

### Phase 2 (MVP launch, 4 weeks)
- [ ] Full screen set: all 5 tabs + onboarding (12+ screens)
- [ ] Dark mode variants
- [ ] Accessibility audit: WCAG 2.1 AA
- [ ] App Store screenshots (6 per platform)
- [ ] App icon (1024×1024)
- [ ] Splash screen

### Phase 3 (Post-launch iteration)
- [ ] A/B test: onboarding flow (3 variants)
- [ ] Price Scout UI (interactive map or list comparison)
- [ ] AI chat screen (conversational interface)
- [ ] Tablet/iPad optimised layout

---

## 8. Accessibility

- All interactive elements ≥ 44pt touch target
- Colour contrast ≥ 4.5:1 (WCAG AA) for all text
- All images have alt text / accessibility labels
- VoiceOver / TalkBack compatible
- No information conveyed by colour alone
- Font scaling support up to 200%

---

## 9. Marketing Design Assets

### App Store Listing
- **Tagline:** "Scan once. Save money. Eat better."
- **Screenshots (6):** Scan, Result with savings, Grocery list, Nutrition, Money Map, Weekly digest
- **Preview video:** 30-second screen-record showing core scan-to-insight loop
- **Icon concept:** Stylised shopping cart with leaf motif (grocery + health)

### Social Media
- Instagram: Clean product shots (phone mockups on lifestyle backgrounds)
- TikTok/Reels: Screen-record style "watch me save $X using this app"
- Twitter: Weekly "did you know?" grocery savings stats + product screenshots
