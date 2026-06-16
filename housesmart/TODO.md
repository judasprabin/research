# HouseSmart — Engineering Backlog (Prioritised Task List)

**Status:** Pre-development → ready for Phase 0
**Audience:** engineers building HouseSmart (solo or small team)
**Source of truth for scope/requirements:** `PRD.md` (esp. §2A Acceptance Criteria),
`technical-architecture.md`, `design-concepts.md`, `roadmap.md`

## How to use this file

- Tasks are grouped by **Phase** (matches `roadmap.md`) and ordered top-to-bottom
  by the order you should actually do them — earlier tasks unblock later ones.
- **Priority:** P0 = blocks launch/exit criteria for that phase. P1 = should ship
  with the phase but a short slip is survivable. P2 = nice-to-have, cut first under
  time pressure.
- **Done means** the task meets the relevant acceptance criteria AND the Definition
  of Done checklist in `PRD.md` §12 — not just "code merged."
- Check off `[ ]` → `[x]` as you go. When a task reveals new edge cases or sub-tasks,
  add them inline rather than discovering them silently mid-build.
- Estimates assume **one full-time engineer** familiar with React Native + Postgres.
  If solo and also doing PM/design/QA, multiply by ~1.5–2× (see `roadmap.md` "Team &
  Resourcing Assumptions").

---

## Phase 0 — Foundation (Weeks 1–4)

**Goal:** prove people will scan receipts; validate OCR/extraction accuracy before
writing a line of production feature code. Nothing here is throwaway — this is the
core engine every later module depends on.

### P0-1. Repo & project skeleton
- [ ] Initialise Expo (React Native) app with the folder structure in
      `technical-architecture.md` §4 (`app/`, `components/`, `lib/`, `hooks/`).
- [ ] Initialise Supabase project (one for `local`, one for `staging` — see
      `technical-architecture.md` §11 Environments). Don't create `production` yet.
- [ ] Set up `supabase/migrations/` and confirm `supabase db diff` workflow works
      locally before any schema is written by hand.
- [ ] Wire up Sentry (mobile) and PostHog (mobile) skeleton, even with zero events
      yet — instrumentation added after the fact is always incomplete.
- **Acceptance:** a fresh clone + `npm install` + `supabase start` + `expo start`
  boots a blank app against a local Supabase instance with no manual steps undocumented.
- **Estimate:** 1–2 days. **Priority:** P0. **Depends on:** nothing.

### P0-2. Core schema (users, receipts, receipt_items, purchase_history)
- [ ] Implement the four tables from `technical-architecture.md` §3 needed for
      scanning (defer `nutrition_summaries`, `bank_*`, `subscriptions` to later phases).
- [ ] Enable RLS + `user_own_data` policy on every table from day one — retrofitting
      RLS after data exists is a much riskier migration.
- [ ] Add the indexes listed in §3 "Key Indexes" for the four tables in scope.
- **Acceptance:** a test user can only ever query their own rows, verified with two
  test accounts in the local stack, not just by reading the policy SQL.
- **Estimate:** 1 day. **Priority:** P0. **Depends on:** P0-1.

### P0-3. Camera capture screen
- [ ] Build the scan tab using `expo-camera` per `design-concepts.md` §3 (Home/Scan
      tab layout) and §5 (camera iris animation — can stub the animation for now).
- [ ] Implement the offline queue from `technical-architecture.md` §2.1: failed
      uploads persist locally (expo-sqlite) with a generated `idempotency_key`,
      retried with exponential backoff on reconnect.
- [ ] Enforce client-side image constraints (reject >8MB or >4096px) before upload.
- **Acceptance:** airplane-mode test — take a photo with no network, confirm it
  queues, re-enable network, confirm it uploads exactly once (not duplicated).
- **Estimate:** 2–3 days. **Priority:** P0. **Depends on:** P0-1.

### P0-4. `/v1/scan` Edge Function — OCR + Claude extraction
- [ ] Implement Google Cloud Vision call → Claude API extraction per the pipeline
      in `technical-architecture.md` §2, using the v1 prompt as a starting point.
- [ ] Implement the full error-handling matrix in §2.1 (OCR failure, garbled text,
      Claude timeout/invalid-JSON, low-confidence fields) — not just the happy path.
- [ ] Implement idempotency: upsert on `(user_id, idempotency_key)`.
- [ ] Implement the rate limit (20 scans/user/day) at the Edge Function layer.
- [ ] Return the response shape exactly as specified in §5.1 (including the
      `low_confidence_fields` array and the error envelope).
- **Acceptance:** run against the golden receipt set (see P0-6) — meets the
  accuracy bar before this task is called done, not just "looks right on one receipt."
- **Estimate:** 4–5 days (this is the highest-risk task in the whole phase —
  budget real time for prompt iteration). **Priority:** P0. **Depends on:** P0-2.

### P0-5. Receipt result screen + manual correction UI
- [ ] Build the post-scan screen per `design-concepts.md` §3 (items list, tap-to-correct).
- [ ] Implement all interaction states from `design-concepts.md` §7A relevant here:
      loading (skeleton, not spinner), low-confidence/partial (amber-flagged inline
      editable fields), error-recoverable (retry), error-unrecoverable (route to
      manual entry), offline.
- [ ] Implement `/v1/scan/confirm` per the contract in §5.1.
- [ ] Build the manual-entry fallback form (blank receipt form) for unrecoverable failures.
- **Acceptance:** a user can correct a flagged field without re-scanning, and a
  fully unreadable photo lands the user in manual entry with no dead end.
- **Estimate:** 3 days. **Priority:** P0. **Depends on:** P0-4.

### P0-6. Golden receipt test set + CI
- [ ] Collect 30 real (redacted of personal info) receipt images across
      Woolworths, Coles, ALDI, IGA, pharmacy, and one utility bill, per
      `technical-architecture.md` §13.
- [ ] Build the automated harness that runs extraction against this set and
      reports per-store accuracy.
- [ ] Wire into CI so any change to the extraction prompt/pipeline must pass this
      before merge.
- **Acceptance:** CI fails the build if Woolworths/Coles item-level accuracy drops
  below 92% or ALDI below 80% (the targets in `PRD.md` §2 Module 1).
- **Estimate:** 2 days (collection) + 1 day (harness). **Priority:** P0 — build
  this *before* finishing P0-4's prompt tuning, not after, per `technical-architecture.md` §13.
- **Depends on:** P0-4 (need a working pipeline to test against, but start
  collecting receipts in parallel with P0-4).

### P0-7. Waitlist landing page
- [ ] Build per `gtm-plan.md` §2 (Framer, headline/CTA copy already drafted there).
- [ ] Add basic analytics (signup count) wired to PostHog or a simple counter.
- **Acceptance:** live at the target domain, mobile-responsive, capturing emails to
  a real store (not a dead form).
- **Estimate:** 1–2 days. **Priority:** P1. **Depends on:** nothing (parallel track, design/founder-owned).

### P0-8. 20-user prototype test
- [ ] Recruit 20 users (ideally drawing on the persona-validation interviews
      recommended in `user-research.md` §6).
- [ ] Run the scan → result → list-preview flow with each; log completion rate and
      qualitative friction points.
- **Acceptance / exit criteria (from `roadmap.md` Phase 0):** ≥70% complete the
  full flow; ≥200 waitlist signups; OCR accuracy ≥85% on Woolworths (manual
  spot-check, can be the golden-set result from P0-6); ALDI ≥70%.
- **Estimate:** 1 week elapsed (calendar time, not engineering time).
  **Priority:** P0 (this is the actual gate to Phase 1). **Depends on:** P0-3, P0-4, P0-5, P0-7.

---

## Phase 1 — MVP Build (Months 2–3)

**Goal:** ship TestFlight/Play beta to 500 users; validate week-4 retention ≥25%.
Do not start Phase 1 features before Phase 0's exit criteria are actually met —
shipping a list/nutrition layer on top of an unreliable scan pipeline just compounds the risk.

### P1-1. Purchase history dashboard
- [ ] Searchable log of every scanned grocery item (store, price, date) per
      `PRD.md` §2 Module 2.
- [ ] Item name normalisation/fuzzy-matching (per `PRD.md` §2A edge case: "Full
      Cream Milk 2L" vs "Milk 2L Full Cream") with a manual "merge items" action.
- **Acceptance:** see acceptance criteria + edge cases in `PRD.md` §2A Module 2.
- **Estimate:** 3 days. **Priority:** P0. **Depends on:** P0-2, P0-4.

### P1-2. Repurchase prediction + weekly shopping list
- [ ] Implement the algorithm in `PRD.md` §2 Module 2, with the recency-weighting
      adjustment from §2A (one anomalous gap must not dominate the prediction).
- [ ] Gate predictions behind ≥2 historical purchases per item (§2A acceptance criteria).
- [ ] Implement the Thursday auto-generation job (`technical-architecture.md`
      `/v1/list/generate`, scheduled via `pg_cron`) + on-demand regeneration.
- [ ] Build the List tab UI per `design-concepts.md` §3, including the empty state
      for new users (§7A).
- **Acceptance:** `PRD.md` §2A Module 2 acceptance criteria + edge cases all pass;
  ≥80% "useful" rating is the beta exit bar, tracked via in-app feedback prompt.
- **Estimate:** 4 days. **Priority:** P0. **Depends on:** P1-1.

### P1-3. Basic nutrition summary (macros only)
- [ ] Open Food Facts lookup per item, aggregate weekly macros
      (`nutrition_summaries` table, `technical-architecture.md` §3).
- [ ] Implement `coverage_pct` tracking and the suppression rule from `PRD.md`
      §2A Module 4 (don't show deficiency claims below 50% coverage — macros-only
      MVP can ship without the deficiency-claim feature entirely, deferred to Phase 2 item 2.5).
- [ ] Add the TGA disclaimer to every nutrition screen (compliance acceptance criterion).
- [ ] Build the Nutrition tab UI per `design-concepts.md` §3.
- **Acceptance:** `PRD.md` §2A Module 4 acceptance criteria (≥85% packaged-item
  match rate, measured against real scan data, not Open Food Facts' own claimed coverage).
- **Estimate:** 4 days. **Priority:** P0. **Depends on:** P1-1.

### P1-4. User auth + onboarding flow
- [ ] Email + Google/Apple OAuth via Supabase Auth.
- [ ] Build the 5-screen onboarding (welcome → first scan → list preview →
      nutrition preview → household size) per `user-research.md` §4 — every step
      must deliver a real insight, not a placeholder, per that doc's stated principle.
- **Acceptance:** new user reaches first real insight (not a mock) within 3 minutes
  of signup, timed in a real test, not estimated.
- **Estimate:** 3 days. **Priority:** P0. **Depends on:** P0-1, P1-2, P1-3.

### P1-5. Expense categorisation (all receipt types) + monthly spend dashboard
- [ ] Categorise every receipt (not just grocery) into the categories in `PRD.md`
      §2 Module 5 (groceries, dining, utilities, transport, subscriptions, health,
      entertainment, other) using `store_type` + Claude classification.
- [ ] Build a basic monthly spend view (no bank sync yet — receipt-derived only).
- **Acceptance:** every receipt type in the golden set (P0-6) gets a non-"other"
  category where a clear one exists.
- **Estimate:** 2 days. **Priority:** P1. **Depends on:** P0-4.

### P1-6. Push notifications (weekly list reminder)
- [ ] `expo-notifications` setup + the Thursday list-ready push and Monday recap
      push from `user-research.md` §5 Retention Mechanics.
- **Acceptance:** both pushes fire on schedule in staging for a test account.
- **Estimate:** 1–2 days. **Priority:** P1. **Depends on:** P1-2.

### P1-7. Manual entry fallback + data export
- [ ] Manual entry form (already built as part of P0-5 — this task is about
      surfacing it as a first-class always-available option, not only an error fallback).
- [ ] JSON data export of a user's own data (simple, supports trust/transparency positioning).
- **Estimate:** 1–2 days. **Priority:** P2. **Depends on:** P0-5.

### P1-8. Observability, CI/CD, and pre-launch hardening
- [ ] Implement the alerting thresholds from `technical-architecture.md` §12
      before opening the beta to 500 users, not after.
- [ ] Set up the CI pipeline from §14 (lint, typecheck, unit tests, migration
      dry-run, golden receipt set) as a merge gate.
- [ ] Implement data deletion (`technical-architecture.md` §3 Data Retention) —
      this is a legal requirement (Privacy Act 1988) once any non-test user data
      exists, i.e. before closed beta, not before public launch.
- [ ] Run the full manual QA regression checklist (§13) on iOS + Android before
      each TestFlight/Play submission.
- **Acceptance:** all of the above are live before the 500-user closed beta opens.
- **Estimate:** 3–4 days. **Priority:** P0. **Depends on:** all prior Phase 1 tasks.

**Phase 1 exit criteria (from `roadmap.md`):** Week-4 retention ≥25%; NPS ≥20; avg
≥2 receipts scanned/user/week; OCR accuracy ≥92% on Woolworths/Coles in production.

---

## Phase 2 — AU Market Launch (Months 4–6)

**Goal:** public launch, freemium conversion ≥5%, MRR ≥AU$2,400. Start the Basiq
integration and legal/compliance prerequisites *early* in this phase — they have
the longest external lead time of anything in the roadmap (see `roadmap.md`
"Cross-Phase Dependencies").

### P2-1. Stripe subscription integration + freemium gating
- [ ] Implement `subscriptions` table + `/v1/billing/webhook` per
      `technical-architecture.md` §5.2 (signature verification, idempotent event processing).
- [ ] Gate every feature per the tier table in `PRD.md` §8, verified on both free
      and premium test accounts (Definition of Done item 6).
- **Priority:** P0. **Depends on:** Phase 1 complete.

### P2-2. Basiq bank connection (Money Map)
- [ ] Implement `/v1/bank/connect` (OAuth) and `/v1/bank/sync` +
      `/v1/bank/webhook` per `technical-architecture.md` §5.
- [ ] Implement `PRD.md` §2A Module 5 acceptance criteria + edge cases (read-only
      enforcement, last-synced timestamp fallback on sync failure, disconnect handling).
- [ ] Implement bank-transaction ↔ receipt matching per the edge case in §2A
      (closest match by date+amount, user-correctable above $2 variance).
- **Priority:** P0. **Depends on:** Basiq sandbox account + legal review of CDR
  consent flow (start this in parallel with Phase 1, per `roadmap.md` dependency note).

### P2-3. Price Scout Phase 1 (from user's own scan data)
- [ ] Implement the savings calculation in `PRD.md` §2 Module 3, gated by the
      minimum-data rule in §2A (≥2 stores × ≥2 receipts each in 60 days) — **this
      gate does not exist yet in the roadmap and must be added before launch.**
- [ ] Implement unit-price normalisation (per-litre/per-kg) before any
      cross-store comparison — flagged in `PRD.md` §2A as a "do not ship" bug class if skipped.
- **Priority:** P0. **Depends on:** P1-1, sufficient beta scan-data volume.

### P2-4. Budget tracking + bill-change detection + subscription tracker
- [ ] Category budgets with 80%/100% alerts (`PRD.md` §2 Module 5).
- [ ] Bill-change detection ("electricity up 23%") and recurring-charge flagging.
- **Priority:** P1/P2 per `roadmap.md` 2.8–2.10.

### P2-5. Vitamin/mineral tracking + deficiency alerts
- [ ] Extend nutrition pipeline beyond macros (P1-3) to micronutrients + ADG comparison.
- [ ] Apply the coverage-suppression rule from `PRD.md` §2A strictly — this is the
      feature most exposed to TGA/trust risk if shipped with low-coverage data.
- **Priority:** P1. **Depends on:** P1-3.

### P2-6. Pre-launch legal/compliance pass
- [ ] Privacy policy, T&Cs, age-gate (16+), subscription-terms transparency for
      App Store/Play Store (`PRD.md` §10).
- [ ] Confirm Price Scout savings claims are substantiated from real data before
      any public marketing copy ships (`gtm-plan.md` §7).
- **Priority:** P0 — blocks public launch regardless of feature completeness.

**Phase 2 exit criteria:** free→paid conversion ≥5%; bank connection rate ≥40% of
premium users; 5,000 signups by Dec 31; MRR ≥AU$2,400.

---

## Phase 3 — Engagement & Depth (Months 7–9)

Lighter detail at this distance — re-derive detailed tasks from `PRD.md`/
`roadmap.md` closer to the time, once Phase 2 actuals are in.

- [ ] **P3-1 (P0):** Crowdsourced pricing layer (opt-in, anonymised) — design the
      anonymisation approach with a privacy review *before* building (see
      `roadmap.md` dependency note); this is also the long-term replacement for any
      scraping approach flagged as risky in `data-discovery-strategy.md`.
- [ ] **P3-2 (P0):** AI chat interface (Claude function calling) per
      `technical-architecture.md` §6.
- [ ] **P3-3 (P0):** Multi-user household sharing + Family plan tier (AU$12.99/mo).
- [ ] **P3-4 (P1):** Referral program (AU$5 credit), with terms per `gtm-plan.md` §7.
- [ ] **P3-5 (P1):** Recipe suggestions from predicted grocery list.
- [ ] **P3-6 (P1):** Real-time price spike alerts.
- [ ] **P3-7 (P2):** Live Woolworths/Coles price API integration (subject to the
      legal review in `data-discovery-strategy.md`).
- [ ] **P3-8 (P2):** Apple Watch companion, home-screen widget.

**Exit criteria:** 30-day retention ≥30%; 10,000 users; MRR ≥AU$6,000.

## Phase 4 — Scale & Revenue (Months 10–12)

- [ ] **P4-1 (P0):** Affiliate ordering links (Coles/Woolworths).
- [ ] **P4-2 (P0):** FMCG data insights B2B product.
- [ ] **P4-3 (P0):** Paid acquisition launch (Meta + Google), gated on the channel
      kill-criteria framework in `gtm-plan.md` §8.
- [ ] **P4-4 (P1):** White-label pilot outreach (Bupa/Medibank).
- [ ] **P4-5 (P1):** NZ market research + Akahu feasibility.
- [ ] **P4-6 (P2):** UK Open Banking research (TrueLayer).

**Exit criteria:** MRR ≥AU$15,000; LTV:CAC ≥4:1 on paid acquisition; ≥1 FMCG
partner signed; NZ launch feasibility confirmed.

---

## Always-On / Cross-Cutting Tasks (not tied to one phase)

| Task | Cadence | Owner | Reference |
|---|---|---|---|
| Re-run competitor analysis | Quarterly + on trigger events | Founder/PM | `competitor-analysis.md` §6 |
| Re-run financial model against actuals | Monthly | Founder | `financial-model.md` §6 |
| Review golden receipt set accuracy trend | Every release touching extraction | Engineering | `technical-architecture.md` §13 |
| Review alerting/cost dashboards | Weekly | Engineering | `technical-architecture.md` §12 |
| Re-derive personas from real cohort data | Once per major beta milestone | Founder/PM | `user-research.md` §6 |
| Security/RLS audit (spot-check policies against new tables) | Every schema migration | Engineering | `technical-architecture.md` §7 |
