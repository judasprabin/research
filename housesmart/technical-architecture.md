# HouseSmart — Technical Architecture

**Version:** 1.0 | June 2, 2026
**Status:** Architecture Design — Ready for Engineering

---

## 1. System Overview

HouseSmart is a mobile-first platform with a React Native client, a Supabase-hosted backend, and AI pipelines powered by Google Cloud Vision + Claude API. All five product modules share a single data layer.

```
┌──────────────────────────────────────────────────────────────────┐
│                    HouseSmart Mobile (React Native/Expo)          │
│   iOS + Android │ Camera │ Offline-first │ Push notifications    │
└─────────────────────────┬────────────────────────────────────────┘
                          │  HTTPS / WebSocket
┌─────────────────────────▼────────────────────────────────────────┐
│              Supabase Edge Functions (API Layer)                   │
│  /scan  /list  /nutrition  /prices  /bank  /chat  /digest         │
└──────┬──────────────┬────────────────┬────────────────┬──────────┘
       │              │                │                │
┌──────▼──────┐ ┌─────▼──────┐ ┌──────▼─────┐ ┌──────▼──────┐
│ Google Cloud│ │ Claude API │ │ Open Food  │ │ Basiq API   │
│ Vision OCR  │ │(Anthropic) │ │ Facts + USDA│ │(AU Banking) │
└─────────────┘ └────────────┘ └────────────┘ └─────────────┘
                          │
┌─────────────────────────▼────────────────────────────────────────┐
│                   Supabase (PostgreSQL)                            │
│  users │ receipts │ items │ purchases │ lists │ nutrition         │
│  transactions │ subscriptions │ bank_connections │ price_history  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. Receipt Processing Pipeline

The core AI pipeline used by all five modules:

```
Step 1: Image capture (expo-camera)
     ↓  base64 + metadata
Step 2: Supabase Edge Function /scan
     ↓  image → Google Cloud Vision API (Document Text Detection)
Step 3: Raw OCR text → Claude API
     Prompt: "Extract: {store, date, items[{name, qty, unit_price}], total, gst}"
     Output: JSON (structured receipt)
     ↓
Step 4: Confidence scoring
     - Per-field confidence from Claude response
     - Low-confidence fields (<80%) → flagged for user review
     ↓
Step 5: Store to Supabase
     - receipts table (raw + structured)
     - receipt_items table (line items)
     - purchase_history table (deduplicated, searchable)
     ↓
Step 6: Downstream processing (async)
     - Nutrition mapping (Open Food Facts lookup)
     - Price history update
     - Repurchase frequency recalculation
     - Bank transaction match attempt
```

### Claude Extraction Prompt (v1)
```
You are a receipt parser. Extract the following from this OCR text.
Return ONLY valid JSON. Use null for missing fields.

Schema: {
  "store_name": string,
  "store_type": "grocery|dining|pharmacy|utility|retail|other",
  "purchase_date": "YYYY-MM-DD",
  "items": [{"name": string, "quantity": number, "unit_price": number}],
  "subtotal": number,
  "gst": number,
  "total": number,
  "confidence": 0.0-1.0
}

OCR text: {{raw_text}}
```

---

## 3. Database Schema

### Core Tables

```sql
-- Users
CREATE TABLE users (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email        TEXT UNIQUE NOT NULL,
  auth_provider TEXT DEFAULT 'email',
  household_size INTEGER DEFAULT 1,
  postcode     TEXT,
  premium_tier TEXT DEFAULT 'free', -- 'free' | 'premium' | 'family'
  created_at   TIMESTAMPTZ DEFAULT now(),
  updated_at   TIMESTAMPTZ DEFAULT now()
);

-- Receipts (raw scan records)
CREATE TABLE receipts (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id        UUID REFERENCES users(id) ON DELETE CASCADE,
  store_name     TEXT NOT NULL,
  store_type     TEXT NOT NULL,
  purchase_date  DATE NOT NULL,
  raw_ocr_text   TEXT,
  extracted_data JSONB,
  total_amount   DECIMAL(10,2),
  gst_amount     DECIMAL(10,2),
  confidence_score DECIMAL(3,2),
  image_url      TEXT, -- Supabase Storage URL
  created_at     TIMESTAMPTZ DEFAULT now()
);

-- Receipt line items
CREATE TABLE receipt_items (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  receipt_id   UUID REFERENCES receipts(id) ON DELETE CASCADE,
  item_name    TEXT NOT NULL,
  item_name_normalised TEXT, -- cleaned for matching
  quantity     DECIMAL(8,3) DEFAULT 1,
  unit_price   DECIMAL(10,2),
  total_price  DECIMAL(10,2),
  category     TEXT, -- 'produce'|'dairy'|'meat'|'pantry'|'snacks'|...
  food_id      TEXT, -- Open Food Facts barcode / USDA food ID
  confidence   DECIMAL(3,2)
);

-- Deduplicated purchase history
CREATE TABLE purchase_history (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id      UUID REFERENCES users(id) ON DELETE CASCADE,
  item_name_normalised TEXT NOT NULL,
  store_name   TEXT NOT NULL,
  purchase_date DATE NOT NULL,
  quantity     DECIMAL(8,3),
  unit_price   DECIMAL(10,2),
  receipt_id   UUID REFERENCES receipts(id)
);

-- Weekly shopping lists
CREATE TABLE shopping_lists (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id      UUID REFERENCES users(id) ON DELETE CASCADE,
  week_start   DATE NOT NULL,
  generated_at TIMESTAMPTZ DEFAULT now(),
  status       TEXT DEFAULT 'active' -- 'active'|'completed'|'archived'
);

CREATE TABLE shopping_list_items (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  list_id          UUID REFERENCES shopping_lists(id) ON DELETE CASCADE,
  item_name        TEXT NOT NULL,
  predicted_run_out DATE,
  quantity_hint    DECIMAL(8,3),
  cheapest_store   TEXT,
  cheapest_price   DECIMAL(10,2),
  saving_vs_default DECIMAL(10,2),
  status           TEXT DEFAULT 'pending' -- 'pending'|'added'|'skipped'
);

-- Nutrition summaries (weekly)
CREATE TABLE nutrition_summaries (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID REFERENCES users(id) ON DELETE CASCADE,
  week_start    DATE NOT NULL,
  energy_kj     DECIMAL(10,1),
  protein_g     DECIMAL(8,1),
  carbs_g       DECIMAL(8,1),
  fat_g         DECIMAL(8,1),
  fibre_g       DECIMAL(8,1),
  sugar_g       DECIMAL(8,1),
  iron_mg       DECIMAL(6,2),
  calcium_mg    DECIMAL(8,1),
  vitamin_d_mcg DECIMAL(6,2),
  folate_mcg    DECIMAL(8,1),
  coverage_pct  DECIMAL(5,2), -- % of items successfully mapped
  UNIQUE(user_id, week_start)
);

-- Bank connections (Basiq)
CREATE TABLE bank_connections (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id            UUID REFERENCES users(id) ON DELETE CASCADE,
  basiq_user_id      TEXT NOT NULL,
  basiq_connection_id TEXT NOT NULL,
  institution_name   TEXT,
  last_synced_at     TIMESTAMPTZ,
  status             TEXT DEFAULT 'active',
  token_encrypted    TEXT -- AES-256 encrypted via pgcrypto
);

-- Bank transactions
CREATE TABLE bank_transactions (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id            UUID REFERENCES users(id) ON DELETE CASCADE,
  bank_connection_id UUID REFERENCES bank_connections(id),
  transaction_date   DATE NOT NULL,
  description        TEXT,
  amount             DECIMAL(10,2) NOT NULL,
  category           TEXT,
  matched_receipt_id UUID REFERENCES receipts(id),
  basiq_txn_id       TEXT UNIQUE
);

-- Subscriptions (Stripe)
CREATE TABLE subscriptions (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID REFERENCES users(id) ON DELETE CASCADE UNIQUE,
  stripe_sub_id   TEXT UNIQUE,
  tier            TEXT NOT NULL, -- 'premium'|'family'
  status          TEXT NOT NULL, -- 'active'|'cancelled'|'past_due'
  current_period_end TIMESTAMPTZ,
  cancelled_at    TIMESTAMPTZ
);
```

### Key Indexes
```sql
CREATE INDEX idx_receipts_user_date ON receipts(user_id, purchase_date DESC);
CREATE INDEX idx_receipt_items_name ON receipt_items(item_name_normalised);
CREATE INDEX idx_purchase_history_user_item ON purchase_history(user_id, item_name_normalised, purchase_date DESC);
CREATE INDEX idx_nutrition_user_week ON nutrition_summaries(user_id, week_start DESC);
CREATE INDEX idx_transactions_user_date ON bank_transactions(user_id, transaction_date DESC);
```

### Row Level Security
```sql
-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE receipts ENABLE ROW LEVEL SECURITY;
-- (all tables)

-- Policy: users can only access their own data
CREATE POLICY "user_own_data" ON receipts
  FOR ALL USING (user_id = auth.uid());
-- Repeat for all tables
```

---

## 4. Mobile Architecture

### Framework: React Native + Expo (Managed Workflow)

**App structure:**
```
housesmart/
├── app/                     # Expo Router (file-based navigation)
│   ├── (tabs)/
│   │   ├── scan.tsx         # Smart Scan tab
│   │   ├── list.tsx         # Grocery Brain tab
│   │   ├── prices.tsx       # Price Scout tab
│   │   ├── nutrition.tsx    # Nutrition Lens tab
│   │   └── money.tsx        # Money Map tab
│   ├── onboarding/
│   └── _layout.tsx
├── components/
│   ├── ScanCamera.tsx
│   ├── ReceiptCard.tsx
│   ├── GroceryList.tsx
│   ├── NutritionWidget.tsx
│   └── PriceComparison.tsx
├── lib/
│   ├── supabase.ts          # Supabase client
│   ├── api.ts               # Edge function calls
│   └── store.ts             # Zustand state
└── hooks/
    ├── useReceipts.ts
    ├── useNutrition.ts
    └── usePredictions.ts
```

### State Management: Zustand + React Query
- **Zustand:** Local UI state + user preferences
- **React Query (@tanstack/react-query):** Server state, caching, background refresh

### Offline Strategy
- SQLite cache (expo-sqlite) for last 30 days of receipts
- Optimistic UI: show extracted data immediately, reconcile with server async
- Upload queue: if scan fails (no internet), queues for retry on reconnect

### Key Dependencies
| Package | Purpose |
|---------|---------|
| expo-camera | Receipt camera |
| expo-sqlite | Local cache |
| @supabase/supabase-js | Backend client |
| @tanstack/react-query | Data fetching + caching |
| zustand | State management |
| expo-notifications | Push notifications |
| react-native-reanimated | Smooth animations |
| posthog-react-native | Analytics |
| @sentry/react-native | Crash reporting |

---

## 5. Edge Functions (Backend)

All backend logic runs in Supabase Edge Functions (Deno runtime).

| Function | Method | Description |
|----------|--------|-------------|
| `/scan` | POST | OCR + Claude extraction, returns structured receipt |
| `/scan/confirm` | PATCH | User-confirmed corrections to extracted data |
| `/list/generate` | POST | Generate weekly shopping list for user |
| `/nutrition/summary` | GET | Weekly nutrition summary for user |
| `/prices/compare` | POST | Price comparison for list of items |
| `/bank/connect` | POST | Initiate Basiq OAuth flow |
| `/bank/sync` | POST | Fetch + categorise new transactions |
| `/chat` | WS | AI chat (Claude) for natural language queries |
| `/digest/weekly` | POST | Generate + push weekly digest notification |

---

## 6. AI Chat Interface (Phase 3)

Natural language interface powered by Claude API with function calling.

**Capabilities:**
- "How much did I spend on groceries last month?"
- "What am I running low on?"
- "Am I getting enough protein?"
- "Where should I shop this week to save the most?"
- "What's changed in my spending vs last month?"

**Architecture:**
```
User message → Claude API (tools enabled)
Available tools: get_expenses, get_nutrition, get_shopping_list,
                 compare_prices, get_budget_status
Claude selects tool → execute against Supabase → return result
Claude generates natural language response → display to user
```

---

## 7. Security Architecture

| Layer | Approach |
|-------|---------|
| Auth | Supabase Auth (JWT) + Google/Apple OAuth |
| Transport | HTTPS everywhere, HSTS |
| DB | Row Level Security — all tables, all queries |
| Bank tokens | AES-256 via pgcrypto before storage |
| API keys | Only in Edge Function env vars (never in client) |
| Images | Supabase Storage, user-scoped access policies |
| Data deletion | CASCADE delete, full account purge on request |

---

## 8. Infrastructure & Costs

### Phase 1 (1,000 MAU)
| Service | Cost/month |
|---------|-----------|
| Supabase Pro | AU$25 |
| Vercel Pro | AU$20 |
| Google Cloud Vision | ~AU$30 (17K images) |
| Claude API | ~AU$25 |
| Open Food Facts | Free |
| Sentry | Free |
| PostHog (self-hosted) | AU$10 (VPS) |
| **Total** | **~AU$110** |

### Phase 2 (10,000 MAU, bank sync enabled)
| Service | Cost/month |
|---------|-----------|
| Supabase Pro | AU$100 |
| Vercel | AU$20 |
| Google Cloud Vision | AU$300 |
| Claude API | AU$200 |
| Basiq API | AU$500 |
| PostHog Cloud | AU$50 |
| Stripe | 2.9% + 30c per transaction |
| **Total** | **~AU$1,170 + Stripe fees** |

---

## 9. Performance Targets

| Operation | Target P95 |
|-----------|-----------|
| Receipt scan → result displayed | < 5 seconds |
| Weekly list generation | < 2 seconds |
| Nutrition summary load | < 1 second (cached) |
| App cold start (iOS) | < 2 seconds |
| App cold start (Android) | < 3 seconds |
| API response time | < 500ms |
| Bank sync (background) | < 30 seconds |

---

## 10. Scalability Path

| Scale | Architecture | Key change |
|-------|-------------|-----------|
| 0–10K users | Supabase Pro | No changes needed |
| 10K–100K users | Supabase + read replicas | Add read replica, Redis cache |
| 100K–1M users | Dedicated Postgres + workers | Extract to dedicated cloud, queue-based processing |
| 1M+ users | Multi-region | CDN, regional DB replicas, background job workers |
