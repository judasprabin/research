# SmartCart — Technical Research Report

**Date:** June 2, 2026
**Status:** Architecture Draft — Ready for Engineering Review
**Stack:** React Native, Google Vision, Claude API, Supabase, Basiq, Open Food Facts

---

## 🏗️ System Architecture Overview

SmartCart is a three-layer mobile application:

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: Mobile Client (React Native / Expo)       │
│  iOS + Android, camera access, offline-first         │
└──────────────────┬──────────────────────────────────┘
                   │ HTTPS (REST + WebSockets)
┌──────────────────▼──────────────────────────────────┐
│  Layer 2: Backend Services (Supabase Edge Functions)│
│  Auth, OCR processing, AI inference, notifications   │
└──────────────────┬──────────────────────────────────┘
                   │ 
┌──────────────────▼──────────────────────────────────┐
│  Layer 3: Data & Integrations                       │
│  Supabase (PostgreSQL), Basiq API, Open Food Facts  │
│  Claude API, Google Cloud Vision, PostHog           │
└─────────────────────────────────────────────────────┘
```

### Receipt Processing Flow
```
User scans receipt (camera)
    ↓
Google Cloud Vision API → OCR raw text
    ↓
Claude API → structured extraction (store, date, items, prices)
    ↓
Supabase → store in purchase history (PostgreSQL)
    ↓
AI suggestion engine → generate weekly list + nutrition summary
    ↓
Push to client (React Native)
```

---

## 📱 Mobile Client Architecture

### Framework: React Native + Expo (Managed Workflow)

**Why Expo:**
- Faster initial development (no native module compilation for Phase 1)
- Expo Go for instant beta testing
- Camera API built-in
- Can eject to bare workflow if custom native code needed later

**Why NOT React Native CLI (yet):**
- No Phase 1 need for custom native modules (Basiq, Google Vision have JS SDKs)
- Single codebase for iOS + Android from day 1
- Re红外 (EAS) for automated builds when needed

### Key Libraries (Phase 1)
| Library | Purpose | Version |
|---------|---------|---------|
| expo-camera | Receipt scanning | SDK 52+ |
| expo-image-picker | Gallery fallback | SDK 52+ |
| @react-navigation/native | Navigation | v7+ |
| @supabase/supabase-js | Backend client | v2+ |
| posthog-react-native | Analytics | v3+ |
| @sentry/react-native | Error tracking | v7+ |
| react-native-reanimated | Animations | v3+ |
| zustand | State management | v5+ |

### State Management: Zustand
- Lightweight, minimal boilerplate
- Good for local persistence (zustand/persist with AsyncStorage)
- Can migrate to Redux if complexity grows

### Offline Strategy (Phase 1 MVP)
- SQLite (expo-sqlite) for local receipt cache
- Optimistic UI: show extracted data immediately, reconcile with server on sync
- Queue failed uploads for retry on reconnect

---

## 🔮 AI / ML Pipeline

### Receipt Text Extraction (Google Cloud Vision + Claude)

**Step 1:** Google Cloud Vision API (Document Text Detection)
- Input: receipt image (base64 from camera)
- Output: raw OCR text (block-level)
- Cost: ~AU$1.50 per 1,000 images (V2 API, tiered)
- Accuracy: ~85–90% on clear receipts; lower on ALDI (no itemized breakdown)

**Step 2:** Claude API — Structured Extraction (Anthropic)
- Input: raw OCR text
- Prompt: structured extraction to JSON (store, date, items[])
- Model: claude-sonnet-4-20250514
- Cost: ~0.3 cents per receipt (input ~2K tokens, output ~0.5K tokens)
- **Critical:** Prompt engineering required per store format; ALDI requires custom handling

**Step 3:** Validation & Human-in-the-loop (Phase 1)
- Low-confidence items (<70%) flagged with "?" for user confirmation
- User corrections fed back to improve future extraction

### Weekly List Generation (Claude API)
- Input: user purchase history (last 90 days)
- Algorithm:
  1. Calculate days-since-last-purchase per item
  2. Predict repurchase date (rolling average + trend)
  3. Flag items predicted within next 7 days
  4. Generate personalised list with quantities
- Claude generates natural-language list from structured data
- Cost: ~0.2 cents per list generation per user per week

### Nutrition Mapping (Open Food Facts + USDA)
- Match receipt items → Open Food Facts products (fuzzy string match, score > 0.7)
- Open Food Facts coverage: ~75% of AU packaged foods (crowdsourced)
- Gap-filling: USDA FoodData Central for unmatched items (~15% of items)
- Remaining 10% (fresh produce, bakery) — flag as "estimated"

---

## 🏦 Bank Sync Architecture (Phase 2 — Basiq)

### Basiq API Integration
- **Consent flow:** Basiq hosted UI (iframe/redirect) for bank selection + credentials
- **Token management:** Basiq access token stored in Supabase (encrypted at rest)
- **Transaction pull:** Daily scheduled fetch + webhook on new transaction
- **Categorisation:** Basiq categories → SmartCart categories (custom mapping table)

### Transaction Matching
- Match bank transactions to scanned receipts by: store name + amount + date
- Fuzzy match window: ±2 days, ±5% amount tolerance
- Unmatched receipts: prompt user to confirm which transaction it belongs to
- Unmatched transactions: auto-suggest as uncategorised expense

### Data Flow
```
Bank → Basiq API → Supabase (transactions table)
        ↓
Receipt scan → Supabase (receipts table)
        ↓
Matching engine → transaction_receipt_links table
        ↓
User dashboard ← unified expense view
```

---

## 🗄️ Database Design (Supabase / PostgreSQL)

### Core Tables
```sql
-- Users
users (id, email, auth_provider, created_at, updated_at, household_size)

-- Receipts (scanned)
receipts (id, user_id, store_name, store_type, purchase_date, 
          raw_ocr_text, extracted_data JSONB, 
          total_amount, confidence_score, created_at)

-- Receipt line items
receipt_items (id, receipt_id, item_name, quantity, unit_price, 
               total_price, category, nutrition_food_id, confidence)

-- Purchase history (deduplicated, per item)
purchase_history (id, user_id, item_name, store_name, purchase_date, 
                  quantity, unit_price, created_at)

-- Weekly shopping lists
shopping_lists (id, user_id, week_start_date, generated_at)
shopping_list_items (id, shopping_list_id, item_name, predicted_date,
                     quantity_hint, added_by, status)

-- User nutrition summaries
nutrition_summaries (id, user_id, week_start_date, 
                     total_energy_kj, protein_g, carbs_g, fat_g, 
                     fibre_g, sugar_g, iron_mg, vitamin_d_mcg, calcium_mg)

-- Bank connections
bank_connections (id, user_id, basiq_connection_id, 
                   institution_name, last_synced_at, status)

-- Transactions (from bank)
bank_transactions (id, user_id, bank_connection_id, 
                   transaction_date, description, amount, category, 
                   basiq_category, matched_receipt_id)

-- Premium subscriptions
subscriptions (id, user_id, tier, started_at, renews_at, cancelled_at)
```

### Row Level Security (RLS)
- All tables have RLS enabled
- User can ONLY access their own rows (user_id = auth.uid())
- Bank connection tokens encrypted (pgcrypto) before storage

### Indexing Strategy
```sql
CREATE INDEX idx_purchase_history_user_item ON purchase_history(user_id, item_name, purchase_date DESC);
CREATE INDEX idx_receipts_user_date ON receipts(user_id, purchase_date DESC);
CREATE INDEX idx_transactions_user_date ON bank_transactions(user_id, transaction_date DESC);
```

---

## 🔐 Security Architecture

### Authentication
- **Primary:** Supabase Auth (email/password + magic link)
- **OAuth:** Google Sign-In + Apple Sign-In (expo-auth-session)
- **Session:** Supabase JWT tokens (1-hour expiry) + refresh tokens (30-day)

### Data Security
- **In transit:** HTTPS everywhere, HSTS preloading
- **At rest:** Supabase (AWS RDS, encrypted at rest by default)
- **Bank tokens:** Encrypted with pgcrypto AES-256 before storing in DB
- **API keys:** Stored in Supabase Edge Function environment variables (not in client code)

### Privacy Compliance
- **Consent:** Explicit opt-in for bank connection (Basiq consent screen)
- **Data minimisation:** Collect only what's needed for MVP
- **Retention:** Auto-delete receipts after 90 days (configurable)
- **Right to delete:** Full account deletion (auth + all tables, CASCADE)
- **Right to export:** Full data export as JSON (via /v1/export endpoint)

---

## ☁️ Infrastructure

### Frontend Hosting
| Option | Cost | Notes |
|--------|------|-------|
| Vercel (recommended) | Free tier + ~AU$20/month pro | Best DX, instant deploys |
| AWS Amplify | ~AU$50/month | More complex, more control |

**Decision:** Vercel for Phase 1. CDN auto-enabled, excellent React Native web support for any marketing pages.

### Backend Hosting
| Option | Cost | Notes |
|--------|------|-------|
| Supabase Pro | ~AU$25/month (500K DB rows) | Included Edge Functions + Auth |
| Railway | ~AU$20/month | Simpler, less integrated |
| Render | ~AU$20/month | Good Node.js hosting |

**Decision:** Supabase Pro for Phase 1. Handles auth, database, Edge Functions, storage all in one.

### Monitoring & Observability
| Tool | Purpose | Cost |
|------|---------|------|
| PostHog (self-hosted) | Product analytics, funnel tracking | ~AU$0 on own infra |
| Sentry | Error tracking + performance | ~AU$0 (free tier) |
| Supabase Dashboard | DB performance, edge function logs | Included |
| Cloudflare R2 | Receipt image storage | ~AU$0 (5GB free) |

---

## 💰 API Cost Estimates (Phase 1 MVP)

Assuming 1,000 MAU, avg 4 receipts/week:

| API | Calls/Month | Cost |
|-----|------------|------|
| Google Vision (OCR) | 16,000 images | ~AU$24 |
| Claude API (extraction + suggestions) | ~48,000 req | ~AU$12 |
| Open Food Facts | ~64,000 req | AU$0 (free) |
| Basiq API (Phase 2) | ~100,000 txns | ~AU$1,500 |
| Supabase | included in Pro | AU$25 |
| Vercel | | AU$0–20 |
| Sentry | | AU$0 |
| **Total** | | **~AU$61–1,561/month** |

Basiq is the big cost driver. Mitigation: throttle to daily sync, not real-time.

---

## ⚡ Performance Targets

| Metric | Target |
|--------|--------|
| Receipt scan → result displayed | < 5 seconds |
| Weekly list generation | < 2 seconds |
| App cold start (iOS) | < 2 seconds |
| App cold start (Android) | < 3 seconds |
| API response time (p95) | < 500ms |
| Offline capability | Core scan + view history |
