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

### 2.1 Error Handling & Retry Policy

Every external call in the pipeline can fail independently. Treat the pipeline as a
saga, not a single transaction — partial success must still produce a usable result.

| Failure point | Detection | Behaviour |
|---|---|---|
| Image upload fails (no network) | Client-side upload error | Queue locally (expo-sqlite), retry with exponential backoff (1s, 2s, 4s, max 5 attempts), show "Saved — will upload when online" |
| Google Vision OCR fails/times out | HTTP error or >8s response | Retry once; on second failure, fall back to manual entry screen with a pre-filled blank receipt form |
| Google Vision returns low-quality text (garbled/empty) | Heuristic: <20 alphanumeric chars in response | Skip Claude call (saves cost), route straight to manual entry |
| Claude extraction fails/times out | HTTP error or >10s response | Retry once with same prompt; on second failure, store raw OCR text only, mark receipt `status='needs_review'`, surface in a "fix these" queue in-app |
| Claude returns invalid JSON | JSON.parse failure | Retry once with a corrective follow-up message ("Your last response was not valid JSON, return only the JSON object"); after 2 failures, fall back to `needs_review` |
| Claude returns low per-field confidence (<0.8) | Confidence score in response | Accept the receipt, but flag specific fields for inline user correction (not a full re-scan) |
| Open Food Facts lookup fails/no match | HTTP error or 404 | Mark item `food_id = null`, exclude from nutrition totals, lower that week's `coverage_pct`, do not block the rest of the pipeline |
| Bank transaction match fails to find a candidate | No transaction within ±AU$2 / ±3 days | Leave `matched_receipt_id = null` — this is an expected, non-error outcome, not a failure |

**Idempotency:** every `/scan` request carries a client-generated `idempotency_key`
(UUID v4, generated once per image at capture time, stored in the offline queue with
the image). The Edge Function upserts on `(user_id, idempotency_key)` so a retried
upload after a flaky network never creates a duplicate receipt.

**Cost control on `/scan`:** Vision + Claude calls cost money per call. Rate-limit to
20 scans/user/day (well above any real usage) at the Edge Function layer to contain
abuse, and reject images >8MB or >4096px on the client before upload.

### 2.2 Async Job Processing

Step 6 cannot run inline in the `/scan` request — it would blow the 5-second P95
target (see §9). Supabase Edge Functions have no native queue, so:

- `/scan` writes the receipt synchronously, then fires-and-forgets a call to a
  `process-receipt` Edge Function (via `fetch` with no `await`, or a `pg_cron`-polled
  `job_queue` table if at-least-once delivery is required).
- **MVP (low volume):** fire-and-forget is acceptable; a failed downstream job just
  means a slightly stale nutrition/price view until the next receipt triggers a
  recompute.
- **Phase 2+ (after bank sync, higher volume):** replace fire-and-forget with a real
  queue (`job_queue` Postgres table + `pg_cron` worker, or migrate to Inngest/Trigger.dev)
  so failed jobs are retried and observable instead of silently dropped.
- Every async job writes a row to `job_runs (job_name, entity_id, status, error, attempts)`
  so failures are queryable, not just logged.

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

### Migration Strategy

- All schema changes go through `supabase/migrations/*.sql`, generated via
  `supabase db diff`, committed to version control — never edited directly via the
  Supabase dashboard in staging/production.
- CI runs every migration against a throwaway database on each PR (`supabase db
  reset` + migrate) to catch broken migrations before merge.
- Additive changes (new nullable column, new table) ship same-day. Breaking changes
  (column drop/rename, NOT NULL on existing column) require a two-step migration:
  add new shape → backfill + dual-write in app code → remove old shape in a
  follow-up release, never in one step, since the mobile app cannot be force-updated
  instantly on iOS/Android.

### Data Retention & Deletion

| Data | Retention | Deletion trigger |
|---|---|---|
| Receipt images (Supabase Storage) | 12 months, then auto-purged by scheduled job (image no longer needed once `extracted_data` is confirmed) | Scheduled `pg_cron` job + user-initiated delete |
| `receipts` / `receipt_items` / `purchase_history` rows | Indefinite while account active (this *is* the product's core asset) | Full CASCADE delete on account deletion |
| `bank_transactions` | Indefinite while bank connection active | Deleted on disconnect (CDR requires honouring revocation promptly) + CASCADE on account deletion |
| Raw OCR text (`receipts.raw_ocr_text`) | 30 days, then nulled out (debugging window only, not needed long-term and is the most sensitive raw field) | Scheduled job |
| Account deletion request | Full purge within 30 days (NDB/Privacy Act 1988 compliance) | User-initiated via Settings → "Delete my data", confirmed via email |

This must be implemented before public launch (Phase 2), not deferred — the Privacy
Act 1988 deletion-rights obligation already applies during closed beta once any
non-test user data is collected.

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
| `/bank/webhook` | POST | Receives Basiq async transaction-sync notifications |
| `/billing/webhook` | POST | Receives Stripe subscription lifecycle events |
| `/chat` | WS | AI chat (Claude) for natural language queries |
| `/digest/weekly` | POST | Generate + push weekly digest notification |

All endpoints are versioned under `/v1/` (e.g. `/v1/scan`) from day one — breaking
response-shape changes ship as `/v2/...` rather than mutating `/v1/` in place, since
the mobile client cannot be force-upgraded.

### 5.1 Request/Response Contracts (MVP-critical endpoints)

**`POST /v1/scan`**
```jsonc
// Request
{
  "image_base64": "...",
  "idempotency_key": "uuid-v4",      // required, see §2.1
  "captured_at": "2026-06-02T08:14:00Z"
}
// Response 200
{
  "receipt_id": "uuid",
  "status": "confirmed" | "needs_review",
  "store_name": "Woolworths",
  "store_type": "grocery",
  "purchase_date": "2026-06-02",
  "items": [
    { "id": "uuid", "name": "Milk 2L", "quantity": 1, "unit_price": 2.80, "confidence": 0.97 }
  ],
  "subtotal": 84.20, "gst": 8.42, "total": 87.40,
  "low_confidence_fields": ["items[3].name"]
}
// Response 422 (unrecoverable — route client to manual entry)
{ "error": "extraction_failed", "raw_ocr_text": "..." }
```

**`PATCH /v1/scan/confirm`**
```jsonc
// Request
{ "receipt_id": "uuid", "corrections": [{ "item_id": "uuid", "name": "Full Cream Milk 2L" }] }
// Response 200
{ "receipt_id": "uuid", "status": "confirmed" }
```

**`GET /v1/nutrition/summary?week_start=2026-06-01`**
```jsonc
// Response 200
{
  "week_start": "2026-06-01",
  "coverage_pct": 78.5,              // % of items successfully mapped to a food DB
  "macros": { "energy_kj": 48200, "protein_g": 312, "carbs_g": 880, "fat_g": 240, "fibre_g": 95, "sugar_g": 410 },
  "micros_pct_of_adg": { "iron": 35, "calcium": 88, "vitamin_d": 18, "folate": 102 },
  "low_flags": ["iron", "vitamin_d"],
  "disclaimer": "General dietary guidance only, not medical advice."
}
```

Every endpoint returns a consistent error envelope on failure —
`{ "error": "<machine_code>", "message": "<human readable>", "retryable": true|false }`
— so the client can branch on `retryable` instead of parsing HTTP status alone.

### 5.2 Webhook Handling

`/bank/webhook` (Basiq) and `/billing/webhook` (Stripe) are public, unauthenticated-by-design
endpoints, so they need their own controls distinct from the JWT-protected user endpoints:

- **Signature verification first, before any parsing** — reject with 401 if the
  Stripe `Stripe-Signature` header or Basiq webhook signature doesn't validate.
- **Idempotent processing** — store `(provider, event_id)` in a `webhook_events` table
  with a unique constraint; if the event was already processed, return 200 immediately
  without reprocessing (both providers retry on anything other than a fast 2xx).
- **Fast ack, slow process** — acknowledge within 3 seconds, do heavy work (e.g. full
  transaction re-sync) in the same async job pattern as §2.2, not inline in the
  webhook handler, or the provider will time out and retry, causing duplicate events.

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

---

## 11. Environments

| Environment | Purpose | Supabase project | Notes |
|---|---|---|---|
| `local` | Engineer's machine | Supabase CLI local stack (Docker) | Seed data via `supabase/seed.sql`; no real API keys — mocked OCR/Claude/Basiq responses |
| `staging` | Internal QA, TestFlight internal track | Dedicated Supabase project | Real third-party APIs but sandboxed accounts (Basiq sandbox, Stripe test mode) |
| `production` | Real users | Dedicated Supabase project | Production API keys, real billing |

Secrets (Anthropic key, Google Vision key, Basiq secret, Stripe secret) live only in
Supabase Edge Function env vars per environment — never committed, never present in
the Expo client bundle. The mobile app only ever holds the Supabase anon key (safe to
expose, constrained entirely by RLS).

## 12. Observability

| Concern | Tool | What to track |
|---|---|---|
| Crash reporting | Sentry (mobile + edge functions) | Uncaught exceptions, with `user_id` and `receipt_id` breadcrumbs |
| Product analytics | PostHog | Funnel: app open → scan tap → scan success → list viewed → premium upgrade |
| Structured logs | Supabase Edge Function logs (JSON format) | Every external API call logged with `{ provider, endpoint, latency_ms, status, cost_estimate }` |
| Pipeline health | Custom dashboard (PostHog or Supabase SQL views) | OCR success rate, Claude JSON-parse success rate, % receipts landing in `needs_review`, per-store accuracy |
| Cost monitoring | Manual weekly review (MVP) → billing alerts (post-MVP) | Vision + Claude + Basiq spend vs forecast in `financial-model.md` |
| Uptime | Better Uptime / UptimeRobot (free tier) | Ping `/v1/health` every 5 min |

**Alerting thresholds (set before public launch):** OCR success rate <90% over 1hr,
`needs_review` rate >15% over 1hr, any Edge Function error rate >5% over 15 min,
Claude API cost >2× daily forecast.

## 13. Testing Strategy

| Layer | Tooling | Scope |
|---|---|---|
| Unit | Jest (mobile), Deno test (edge functions) | Repurchase-prediction algorithm, price-saving calculation, nutrition aggregation — all pure functions, test against fixed input/output tables |
| Golden receipt set | Custom harness, run in CI | 30 real (redacted) receipt images across Woolworths/Coles/ALDI/IGA/pharmacy/utility, asserting extraction accuracy stays ≥ target (§ PRD success metrics) on every PR touching the extraction prompt |
| Integration | Supabase local stack + Jest | `/scan` → DB write → downstream job, run against local Postgres, third-party calls mocked |
| E2E (mobile) | Detox or Maestro | Scan → result → list flow on a real/simulated device, run nightly, not on every PR (slow) |
| Manual QA | Pre-release checklist | Full regression on iOS + Android before each TestFlight/Play submission |

The golden receipt set is the single most important test asset in this project —
extraction-accuracy regressions are silent and directly determine retention (PRD §5).
Build it in Phase 0 (week 1–2) before writing the production prompt, not after.

## 14. CI/CD & Release Process

- **Branching:** trunk-based, short-lived feature branches, PR required to merge to `main`.
- **CI (every PR):** lint, typecheck, unit tests, migration dry-run (§3 Migration Strategy), golden receipt set.
- **CD:** `main` auto-deploys Edge Functions + migrations to `staging`. Production
  deploy is a manual promotion (`supabase functions deploy --project-ref prod`) gated
  on a green staging smoke test, run by whoever is on call that week.
- **Mobile releases:** EAS Build (Expo) → TestFlight/Play internal track → staged
  rollout (10% → 50% → 100%) via App Store Connect / Play Console phased release,
  not big-bang, so a bad build only hits a fraction of users before halt.
- **Submit to app stores 2 weeks before any hard launch date** (per `roadmap.md`
  risk-adjusted timeline) — review times are unpredictable, especially for an app
  requesting camera + financial-account permissions.
