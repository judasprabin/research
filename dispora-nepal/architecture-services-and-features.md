# Saathi — Features & Components (Agent-First Service Architecture)

**Project:** Saathi — Visa Utility Tool for Nepalese Migrants in Australia
**Date:** July 12, 2026 (v1.1 — decisions D1/D2/D6/D7 resolved; agent-first reframe)
**Status:** Synthesis — reconciles PRD v2.0, Market Research, and the Doc-Scan Architecture into one service map
**Author:** Prabin Karki

> **What this document is.** The single reconciled source of truth for
> **features → services → components**. v1.1 reframes Saathi as an
> **agent-first product**: a central Saathi Agent (Claude tool-use loop) is the
> core of the system, and each feature is a **skill/tool** the agent invokes.
> **Skill #1 is visa form-filling** — fill-only, from the user's own documents,
> with **no suggestions**.
>
> **Source docs reconciled:** [`PRD.md`](PRD.md) (v2.0, scope reset) ·
> [`docs/MARKET-RESEARCH.md`](docs/MARKET-RESEARCH.md) ·
> [`architecture-doc-scan-form-fill.md`](architecture-doc-scan-form-fill.md) ·
> [`legal-memo.md`](legal-memo.md) · GCP build in `karki-labs-infra`.

---

## 1. Decisions locked in this version

| # | Decision | Resolution |
|---|----------|-----------|
| D1 | Data layer | **GCP-native**: Cloud SQL for PostgreSQL (+ pgvector), Cloud Storage. Supabase dropped. |
| D2 | Form-fill scope | **Promoted to the first main agentic skill.** The agent scans the user's documents and fills the form — **fill-only, no suggestions**: it transcribes values found in the user's own documents into the matching fields; it never proposes an answer for a field whose value isn't present in those documents, and never advises what a user *should* answer. Confirm this boundary with `legal-memo.md` before public launch (build proceeds now). |
| D6 | Devanagari → Latin transliteration | **In scope** — required component of the form-fill skill (most AU government AcroForms are Latin-1 only). |
| D7 | Cheap alternatives | **Comparison done** — see §6 Model & Cost Strategy. Per-stage model assignment instead of one model everywhere. |
| — | Architecture style | **Agent-first**: build the whole service around a central agentic AI; features ship as agent skills, not standalone apps. |

Earlier reconciliation (v1.0) still applies: PRD v2.0 feature numbering is
canonical; Market Research's ~15 extra features remain **deferred**; GCP is the
deployment target.

---

## 2. Canonical feature set (as agent skills)

| ID | Feature → Skill | Scope tier | Uses LLM? | Notes |
|----|-----------------|-----------|-----------|-------|
| **F4b** | **Form-Fill Skill** — scan user docs → extract → validate → fill AcroForm PDF | **Skill #1 — build first** | Yes (Claude Vision + agent loop) | Fill-only, **no suggestions** (D2). Includes Devanagari→Latin transliteration (D6). |
| **F4a** | **Form-Explain Skill** — explain each form field in plain Nepali | MVP core | Yes | Explanation ≠ suggestion: describes what a field asks, never what to answer. |
| **F1** | **Visa Tracker Skill** — visa record, expiry, conditions, reminders; news/processing-time/rule ingestion | MVP core | Optional (Nepali summaries) | |
| **F2** | **Points Calculator Skill** — deterministic GSM score vs SkillSelect rounds | MVP core | No | Rule-based; agent invokes it as a tool. |
| **F3** | **Document Checklist Skill** — branching checklist per visa type | MVP core | No | Content + branching; cited. |
| — | Marketplace/Connect, community, timeline projection, directory, content hub, etc. | **Deferred** (PRD §9) | — | Only after core skills have traction. |

> **Regulatory guardrail (PRD §5), sharpened by D2:** the agent may *transcribe*
> (copy a value from the user's document into a form field), *explain* (what a
> field means), *calculate* (deterministic points), and *track* (user-entered
> dates). It may **not** suggest answers, assess eligibility, recommend a
> pathway, or lodge anything. Any field whose value can't be sourced from the
> user's own documents is left blank and flagged for the user — with the MARN
> handoff line where the answer depends on their legal situation. This rule is
> **server-enforced in the agent's system prompt and tool design**, not just UI copy.

---

## 3. Agent-first topology

The core is **saathi-agent**: a Cloud Run service running a Claude **tool-use
loop** (FastAPI + Anthropic SDK — we host the loop; Claude API + custom tools,
per-tool gating stays in our hands). Every feature is a tool the agent can call.

```
                          ┌────────────────────┐
   Users (Sydney/Melb) ──►│   fe (Next.js PWA) │  bilingual EN/NP chat + review UI
                          └─────────┬──────────┘
                                    │
                        ┌───────────▼────────────┐
                        │     authenticator      │  identity, sessions, consent
                        └───────────┬────────────┘
                                    │
                        ┌───────────▼────────────┐
                        │      saathi-agent      │  Claude tool-use loop (Opus/Sonnet)
                        │  system prompt = guard │  guardrail + skill routing
                        └───────────┬────────────┘
              ┌──────────┬──────────┼───────────┬─────────────┐
              ▼          ▼          ▼           ▼             ▼
        ┌──────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────────┐
        │ scan     │ │ form-   │ │ tracker │ │ calc +   │ │ knowledge    │
        │ tools    │ │ fill    │ │ tools   │ │ checklist│ │ (RAG +       │
        │(classify,│ │ tools   │ │ (F1)    │ │ tools    │ │  citations)  │
        │ extract, │ │(map,fill│ │         │ │ (F2, F3) │ │              │
        │ validate)│ │translit)│ │         │ │          │ │              │
        └────┬─────┘ └────┬────┘ └────┬────┘ └────┬─────┘ └──────┬───────┘
             └────────────┴─────┬─────┴───────────┴──────────────┘
                                ▼        (private IP / VPC connector)
                  Cloud SQL (Postgres + pgvector) · Cloud Storage (docs/PDFs)
                  Secret Manager (Claude key) · Audit log
```

**Deployment reality (solo builder):** three Cloud Run services to start —
1. **scan-service** — already the CI/CD walking skeleton; grows into the scan tools.
2. **saathi-agent** — the agent loop + form-fill skill (calls scan-service; form-fill tools live in-process here initially).
3. **fe** (+ Identity Platform for auth — authenticator logic can live inside the agent service at first).

Tracker/calculator/checklist start as **in-process tools** of saathi-agent and
extract into their own services only when load or team size justifies it. The
tool interfaces below are designed so extraction is a move, not a rewrite.

---

## 4. Skill/tool specifications

### 4.1 Form-Fill Skill (F4b) — **skill #1, build first**

The agentic pipeline from `architecture-doc-scan-form-fill.md`, executed as an
agent loop rather than a fixed pipeline — the agent decides per-document which
tools to call and when to stop and ask the user.

**Tools exposed to the agent:**

| Tool | What it does | Backing |
|------|--------------|---------|
| `classify_document` | Doc type from image (7 types) | Claude Vision (Haiku — §6) |
| `extract_schema` | Per-doc-type structured JSON + confidence | Claude Vision (Sonnet — §6) |
| `extract_open` | Second pass, all name-value pairs | Claude Vision (Haiku — §6) |
| `validate_fields` | MRZ checksum, date plausibility, ABN/BSB format, cross-doc consistency | Deterministic code |
| `transliterate` | Devanagari → Latin (D6), with user confirmation required | Deterministic + Claude assist |
| `map_to_form` | `passport.full_name → Form80.AT01_GivenNames` via field manifest | Deterministic mapping table |
| `fill_pdf` | Write **confirmed** values to AcroForm fields; annotate; audit | pypdf/pdf-lib |
| `ask_user` | Surface a field for confirmation/manual entry (MED/LOW confidence, or value not found) | fe review UI |

**Hard rules encoded in tool design (D2 — no suggestions):**
- `fill_pdf` only accepts values with provenance: each value must reference the extraction (document + region) it came from, or an explicit user entry. The agent *cannot* fabricate a fill value.
- Fields with no sourced value → `ask_user`, never a guess.
- Confidence tiers unchanged from the architecture doc: HIGH pre-fill / MED confirm / LOW manual.
- Every fill is audit-logged (who/what/when/source/confidence).

**Data owned:** `documents`, `extractions`, `field_manifests`, `field_mappings`, `filled_forms`, `audit_log`.
**GCP:** scan tools in scan-service (Cloud Run); fill tools in saathi-agent; docs/PDFs in GCS (user-scoped, AU region); Claude key in Secret Manager.

### 4.2 Form-Explain Skill (F4a)

Per-field plain-Nepali explanation grounded in the knowledge service; MARN
disclaimer appended server-side. Explains *what is asked*, never *what to answer*.

### 4.3 Visa Tracker Skill (F1)

Visa CRUD, conditions reference (cited), reminders (180/90/30/7d) via Cloud
Scheduler + push; ingest worker for news/processing times/rule changes with
optional Claude-generated Nepali summaries (Batch API — §6).

### 4.4 Points Calculator Skill (F2)

Deterministic rule engine + SkillSelect round data (source + date). No LLM. The
agent calls it as a tool and relays results verbatim with the disclaimer.

### 4.5 Document Checklist Skill (F3)

Branching-logic engine over cited checklist content; printable output.

### 4.6 knowledge-service — grounding & citations

Scheduled ingest of Home Affairs/SkillSelect/ATO with change detection; pgvector
retrieval; every fact carries source URL + "last verified" date. Feeds F4a, F3,
and tracker summaries.

### 4.7 fe / authenticator

As before: Next.js PWA (bilingual, review UI with side-by-side extracted value ↔
source snippet); Identity Platform for auth + consent/retention record (PII gate
before any document upload).

---

## 5. Feature → Skill → Component matrix

| Feature | Skill entry point | Tools/components | LLM calls |
|---------|-------------------|------------------|-----------|
| F4b Form-Fill | saathi-agent loop | classify, extract×2, validate, transliterate, map, fill, ask_user | classify + 2 extraction passes per doc |
| F4a Form-Explain | saathi-agent loop | knowledge retrieval + explainer | 1 per field/question |
| F1 Tracker | tool + cron | CRUD, reminders, ingest worker | optional summaries (batch) |
| F2 Calculator | tool | rule engine, SkillSelect data | none |
| F3 Checklist | tool | branching engine, cited content | none |

---

## 6. Model & cost strategy (D7)

Per-stage model assignment. Current Claude pricing (per 1M tokens, standard):

| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| Claude Opus 4.8 (`claude-opus-4-8`) | $5.00 | $25.00 | Most capable Opus tier |
| Claude Sonnet 5 (`claude-sonnet-5`) | $3.00 *(intro $2.00 to 31 Aug 2026)* | $15.00 *(intro $10.00)* | Near-Opus on agentic work |
| Claude Haiku 4.5 (`claude-haiku-4-5`) | $1.00 | $5.00 | Fastest/cheapest; vision-capable |

**Recommended per-stage assignment:**

| Pipeline stage | Recommended | Why | Cheap fallback |
|----------------|-------------|-----|----------------|
| **Agent loop** (saathi-agent orchestration) | **Opus 4.8** | Skill routing + guardrail adherence is the product's trust core; adaptive thinking | Sonnet 5 once prompts are tuned + eval'd |
| Document classification (7 types) | **Haiku 4.5** | Simple closed-set task; ~5× cheaper than Sonnet | — |
| Schema extraction (passport MRZ, payslips, Devanagari) | **Sonnet 5** | Accuracy-critical; strong multilingual vision; intro pricing now | Haiku for clean/typed PDFs, Sonnet only for photos/handwriting |
| Open extraction (2nd pass) | **Haiku 4.5** | Recall pass; schema pass is the authority on conflict | — |
| F4a field explanations (Nepali) | **Sonnet 5** | Nepali generation quality | Cache-heavy: explanations per form field are reusable across users → generate once, store, serve from DB |
| Tracker news summaries | **Haiku 4.5 via Batch API** | Non-interactive | — |
| Knowledge ingest/embedding | **Batch API** | Scheduled, not latency-sensitive | — |

**Rough per-document scan cost** (image ≈ 1.6K tokens + prompts; estimates, verify with `count_tokens`):
classify (Haiku) ~$0.003 + schema extract (Sonnet) ~$0.015–0.02 + open pass
(Haiku) ~$0.006 ≈ **$0.02–0.03 per document**, so a typical 5-document
form-fill session ≈ **$0.10–0.15** in extraction + agent-loop tokens on top.
Consistent with the architecture doc's $0.01–0.05/doc estimate.

**Cost levers (in order of impact):**
1. **Prompt caching** — the agent's system prompt + tool definitions and the per-doc-type extraction schemas are stable; cache them (reads ≈ 0.1× input price). Note minimum cacheable prefix: 4096 tokens on Opus 4.8/Haiku 4.5 — keep the cached prefix chunky, volatile content last.
2. **Batch API (50% off)** for everything non-interactive: knowledge ingest, news summaries, pre-generating F4a field explanations.
3. **Pre-generate & store** F4a explanations per form field (they don't vary per user) — turns an LLM call into a DB read.
4. **Cost ceiling per user/session** — track spend per user (architecture doc §9 Q6); hard-cap scans per free-tier user.

**Non-Claude cheap alternatives** (from architecture doc §3.2, unchanged):
Google **Document AI** is the strongest non-LLM option for standardized forms
(per-page pricing; verify current GCP rates) but weaker on Nepali/Devanagari and
adds a second extraction stack; **Tesseract 5** is free but too brittle for MVP
(no layout understanding, weak Devanagari) — keep as an offline fallback only.
Recommendation stands: Claude Vision per-stage-tiered as above beats both on
Devanagari + layout for this workload; revisit Document AI if volume makes
per-page pricing win at scale.

---

## 7. Cross-cutting concerns

| Concern | How it's handled | Owner |
|---------|------------------|-------|
| **No-suggestion guardrail (D2)** | Provenance-required `fill_pdf`; `ask_user` for unsourced fields; system-prompt rules; server-appended MARN disclaimer | saathi-agent |
| Bilingual EN/NP | Bilingual labels/explanations; NP-only toggle | fe + knowledge |
| PII & retention (passports, financials) | AU-region storage only; user-scoped encrypted GCS; consent gate; deletion policy (D4 open); audit every access | scan/agent + authenticator |
| Claude data retention / DPA | Confirm with Anthropic for PII workloads (D5 open) | Prabin |
| Confidence handling | HIGH auto / MED confirm / LOW manual — never auto-fill low confidence | scan tools + fe |
| Audit log | Every extraction, transliteration, and fill: who/what/when/source/confidence | agent + scan |
| Citations & freshness | Source + "last verified" on every fact | knowledge-service |
| Cost tracking | Per-user token spend; session caps | saathi-agent |

---

## 8. Build sequence (agent-first)

| Stage | What | Notes |
|-------|------|-------|
| **0** | scan-service walking skeleton → full CI/CD to Cloud Run | In progress (karki-labs-infra) |
| **1** | authenticator + fe shell (chat + upload UI) | Identity Platform; consent gate |
| **2** | **saathi-agent core** — Claude tool-use loop, guardrail system prompt, audit log | Opus 4.8; tool registry; per-tool gating |
| **3** | **Form-Fill Skill (F4b)** — classify/extract/validate tools in scan-service; map/transliterate/fill tools in agent; review UI in fe | **The first main skill.** Prereq: Form 80 + 1221 field manifests (D3) |
| **4** | knowledge-service (ingest + citations) | Unblocks grounded explanations |
| **5** | Form-Explain Skill (F4a) | Pre-generate per-field explanations |
| **6** | Checklist (F3) + Calculator (F2) tools | Deterministic, fast to add as tools |
| **7** | Tracker (F1) — accounts, reminders, ingest | Cloud Scheduler + push |
| Later | Deferred features | Only after core traction (PRD §9) |

---

## 9. Open decisions

| ID | Decision | Status | Blocks |
|----|----------|--------|--------|
| D1 | Data layer | ✅ **Resolved — GCP-native** (Cloud SQL + pgvector, GCS) | — |
| D2 | Form-fill scope | ✅ **Resolved — skill #1, fill-only, no suggestions**; legal confirms boundary pre-launch | — |
| D3 | Form 80 / 1221 AcroForm field names (inspect in Acrobat) | 🔴 Open — **prerequisite for stage 3** | form-fill mapping |
| D4 | PII retention period + access policy | 🔴 Open | scan upload go-live |
| D5 | Claude data-retention / DPA for sensitive PII | 🔴 Open | F4b public launch |
| D6 | Devanagari → Latin transliteration | ✅ **Resolved — in scope** (form-fill skill component) | — |
| D7 | Cheap-alternative comparison | ✅ **Resolved — §6** (per-stage tiering: Haiku/Sonnet/Opus + batch + caching) | — |

---

## 10. References

- [`PRD.md`](PRD.md) — canonical features & scope reset (v2.0)
- [`docs/MARKET-RESEARCH.md`](docs/MARKET-RESEARCH.md) — competitor blueprint, deferred features
- [`architecture-doc-scan-form-fill.md`](architecture-doc-scan-form-fill.md) — F4b pipeline detail (now executed agent-style)
- [`legal-memo.md`](legal-memo.md) — form-fill legality; confirms the fill-only boundary
- `karki-labs-infra/docs/infra-setup.md` — GCP infra + scan-service walking skeleton

*v1.0 compiled July 11, 2026 · v1.1 (decisions + agent-first) July 12, 2026*
