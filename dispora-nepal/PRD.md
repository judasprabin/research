# Saathi — Product Requirements Document

## AI Settlement & Immigration Companion for the Nepalese Diaspora in Australia

**Version:** 1.0 (Research-Complete — Ready for Validation Build)
**Date:** June 28, 2026
**Status:** Research complete — entering validation prototype phase
**Author:** Prabin Karki

> **Version History:** v0.1–v0.3 (June 10, 2026) — pre-validation draft & market scoping. v1.0 (June 28, 2026) — full research-complete revision incorporating: updated 2026 market data (Level 3, doubled 485 fee), mental health crisis findings, work exploitation patterns, fake-agent protection needs, skills assessment complexity, dual-country financial needs, competitive landscape update (Nepali lai kaam, Sam Nepali, MyAus App, Immigify), and 9 new feature domains not present in v0.3.

---

## 1. Executive Summary

**Saathi** (साथी — "companion" in Nepali) is a Nepali-language AI companion that helps Nepalese migrants in Australia navigate the full complexity of life between two countries: student visas, graduate visa transitions, tax, superannuation, skills assessments, rental rights, workplace rights, mental health support, and the long road to permanent residency. It reads your documents, explains them in plain Nepali, tells you exactly what to do next, tracks your deadlines, protects you from fake agents, and hands off the regulated parts to verified professionals.

**It is explicitly NOT a migration advice service.** Giving immigration assistance in Australia is a regulated activity (Migration Act 1958). Saathi provides _information, document understanding, organisation, crisis support, and referral_ only. This boundary is non-negotiable and defines the entire product.

**Why now (2026 update):** The Nepal-born population in Australia reached ~213,580 by June 2025 — roughly 5× its 2014 size — with ~68,500 Nepalese students in early 2026. In January 2026, Australia moved Nepal to **Assessment Level 3** for student visas (stricter documentation requirements), and the 485 Graduate Visa fee was **doubled to AUD 4,600** in March 2026. A mental health crisis is simultaneously escalating: community organisations have repatriated at least 5 bodies of Nepalese students who died by suicide in a two-month period. The community faces more complexity, higher costs, more documentation burden, and deeper distress than at any prior point — and has zero Nepali-language, grounded, AI-assisted tools to help them.

**Why a solo dev can win this:** It is a retrieval + document-understanding + in-language-explanation problem (founder's core strength), targeting a niche too small for VC-backed competitors but large enough to sustain a sustainable business, with an authentic community-distribution edge no generic competitor can replicate. The closest existing Nepalese-community apps in Australia ("Nepali lai kaam", "Sam Nepali") cover jobs and classifieds — not immigration, rights, or AI guidance.

**The wedge (MVP):** The **485 Graduate Visa transition**, now more painful than ever (Level 3, doubled fee, age limit 35) — done exceptionally well, grounded and cited in Nepali, before expanding.

---

## 2. Vision & Mission

**Vision:** Every Nepalese migrant in Australia understands every official document and process they face — in their own language — never makes a costly mistake out of confusion or bad information, knows their rights, is protected from exploitation, and feels less alone.

**Mission:** Build a trusted, grounded, in-language companion that turns opaque Australian bureaucracy into clear next steps, protects the community from exploitation and misinformation, provides a safety net in mental health crises, and connects people to the right registered professional at the right moment.

### Core Principles

1. **Grounded or silent** — every substantive answer is backed by an official source and cited; if the knowledge base can't support an answer, the agent says so rather than guessing.
2. **Information, not advice** — Saathi never recommends a specific visa pathway or makes a binding determination; it explains and refers.
3. **Trust is the product** — in a domain where errors ruin lives, conservatism and honesty beat helpfulness.
4. **In-language first** — plain Nepali (and English), not bureaucratic jargon.
5. **Safe harbour for the whole person** — immigration is a mental health event. Saathi treats the emotional dimension as seriously as the procedural one.
6. **Protection, not just information** — actively alert users to fake agents, scam patterns, and exploitation risks that the community is uniquely exposed to.
7. **Right-size the build** — validate demand before infrastructure; lightweight stack until traction is proven.

---

## 3. Problem Statement

### 3.1 Core Problem

A temporary-visa-heavy community faces a continuous churn of high-stakes, jargon-dense, English-language bureaucratic events. Each is expensive to get wrong, the rules change frequently (Level 3 change happened out-of-cycle in January 2026), and the realistic alternatives are poor.

| # | Pain | Current "fix" | Why it fails |
|---|------|---------------|--------------|
| 1 | "I don't understand this official letter/form" | Google Translate, ask a friend | Loses legal meaning; friends give wrong info |
| 2 | "Which documents do I need and by when?" | Forums, scattered checklists | Out of date, generic, missed deadlines |
| 3 | "Do I need a migration agent or can I do this myself?" | Pay $2–5k+ agent, or guess | Expensive, or dangerous DIY |
| 4 | "How does tax / super / Medicare actually work here?" | ATO website (dense English) | Not actionable in-language for specific situations |
| 5 | "Is the advice in this Facebook group right?" | Community FB groups | Confident, unverified, often wrong |
| 6 | "Is this migration agent real/legitimate?" | No easy check | Fake agents scam thousands; Level 3 fraud spike |
| 7 | "Am I being underpaid at work?" | Fair Work website (English only, hard to navigate) | Language barrier + fear of employer retaliation |
| 8 | "I'm struggling mentally — where do I go?" | Nothing Nepali-specific | Cultural stigma + language barrier + no bridge to services |
| 9 | "What happens to my super if I go back to Nepal?" | Nowhere | Zero clear Nepali-language guidance |
| 10 | "How do I maintain my NRN bank account in Nepal?" | NRNA website (patchy) | Fragmented, not actionable |

**Saathi addresses 1–10 directly, at different levels of depth across the product roadmap.**

### 3.2 The 2026 Urgency Layer (new since v0.3)

| Development | Impact on the community | Impact on Saathi |
|-------------|------------------------|------------------|
| Level 3 assessment (Jan 2026) | More docs, slower processing, higher refusal rate | Document prep help is more valuable |
| 485 fee doubled to AUD 4,600 | Financial pressure on already-stressed students | Cost transparency + fee calculator urgently needed |
| Age limit 35 on 485 | Many don't know until too late | Eligibility alert is potentially life-changing |
| Mental health crisis (suicide surge) | Community-level emergency | Safety net features are not optional polish |
| Fake-agent fraud spike (Nov–Dec 2025) | Students losing money + visa prospects | Agent verification tool is a trust feature |
| Assessment Level 3 document fraud risk | "Zero room for error" in 2026 | Guided document prep becomes mission-critical |

---

## 4. Market Analysis

### 4.1 The Community (Sources: DFAT/ABS, Home Affairs, ABS 2021 Census, ANU, CESLAM)

| Metric | Value |
|--------|-------|
| Nepal-born residents (June 2025) | ~213,580 |
| Nepalese students in Australia (2026) | ~68,500 |
| Growth rate | ~5× in a decade (42,900 in 2014 → 213,580 in 2025) |
| Rank in Australian migrant communities | 8th largest |
| Adults with bachelor's degree or higher | ~52% |
| Visa status | Majority on temporary visas (89% of new visas are temporary) |
| Concentration | NSW ~48% (Sydney-heavy); VIC ~25% |
| Median age | ~30 |
| Gender split | ~54% male, ~46% female |
| Remittances to Nepal from AU (2021) | ~US$466M |
| Permanent visas granted (2023–24) | 11,506 (95% skilled stream) |
| Desire for dual citizenship | 73% in survey data |

**Read:** Large, fast-growing, young, educated, mobile-first, mid-journey, and highly concentrated where the founder is. The 2026 regulatory tightening (Level 3, fee doubling) has increased the urgency and the demand for guidance — without increasing the supply of trusted Nepali-language resources. The community's mental health crisis and exploitation exposure add dimensions that no existing product addresses.

### 4.2 TAM & Business Scale

This is a **sustainable solo / small-team business**, not a venture-scale outcome. That is a feature, not a bug — it is small enough that incumbents ignore it, a solo founder can own it, and there is a clear template-replication path to other diaspora communities (Indian, Bangladeshi, Sri Lankan in Australia; Nepalese in UK, Canada, UAE) once the model is proven.

---

## 5. Target Users & Personas

### Primary — "Graduate in transition" (the wedge)

**Riya, 25, Sydney.** Nepalese graduate, student visa expiring in 4 months, needs to move onto a 485 graduate visa. The fee just went to AUD 4,600. She doesn't know she needs to be under 35 (she is 25, fine — but didn't know). She has no idea what "Level 3" means for her situation. She can't afford a $3k migration agent for what feels like a standard case, but she's terrified of getting it wrong. She asks her Facebook group; gets 6 different answers.

**Hook:** "Exactly what you need for your 485, in Nepali, with your deadlines tracked — and a clear answer on whether you actually need an agent."

### Secondary Personas

| Persona | Need | Priority |
|---------|------|----------|
| International student (new arrival) | Tax return, super, Medicare, settlement basics — what even is a TFN? | P1 |
| Skilled migrant (PR track) | Skills assessment (ACS/EA/VETASSESS), CDR preparation, document prep, PR pathway planner | P1 |
| Worker facing exploitation | Fair Work rights, underpayment check, reporting without fear | P1 |
| Family/partner visa applicant | Document understanding, evidence checklists, timeline expectations | P2 |
| Mental health crisis | Bridge to Beyond Blue / Lifeline / community support — in Nepali | P1 (safety) |
| NRN straddling two countries | Super portability, remittances, NRN banking in Nepal, Nepal tax | P2 |

### B2B Persona (later)

| Persona | Need |
|---------|------|
| Registered migration agent | Qualified, pre-prepared leads; client-facing front end; case workspace |
| Education agent | Value-add tool for recruited students; settlement layer on top of admissions |
| Accountant serving the community | Tax-return leads; pre-organised client documents |
| Community organisations (NRNA) | Resource / tool to distribute to members |

---

## 6. Competitive Landscape

### 6.1 Direct Alternatives (What Users Do Today)

| Alternative | In-Nepali | Grounded/Cited | Doc Reading | Deadline Tracking | Personalised | Mental Health | Exploitation Protection | Cost |
|-------------|-----------|----------------|-------------|-------------------|--------------|---------------|------------------------|------|
| Generic ChatGPT | Partial | No (hallucinates) | Partial | No | No | No | No | Low |
| Migration agent | Yes (some) | Yes | Yes | Yes | Yes | No | No | $2–5k+ |
| Community FB groups | Yes | No | No | No | No | No | No | Free |
| ATO / Home Affairs websites | No | Yes | No | No | No | No | No | Free |
| MyAus App | Partial (20 langs) | Partial | No | No | No | No | No | Free |
| **Saathi** | **Yes (Nepali-first)** | **Yes** | **Yes** | **Yes** | **Yes (info only)** | **Yes** | **Yes** | **Low/freemium** |

**The gap:** No product in the market is Nepali-language + grounded/cited + document-aware + deadline-tracking + mental health/crisis-aware + exploitation-protective + affordable. This is the exact space Saathi owns.

### 6.2 Existing Nepalese Community Apps in Australia

| App | What it does | What's missing | Saathi's angle |
|-----|-------------|----------------|----------------|
| **Nepali lai kaam** ("Australia's Largest Nepalese Community App") | Jobs, real estate listings, buy/sell, business directory, events | No immigration AI, no document help, no visa guidance, no mental health layer | Saathi is not a classifieds app — it's an immigration and settlement AI companion. These are complementary, not competing |
| **Sam Nepali** | Jobs + community | Same gap — no immigration or rights guidance | Same — complementary |
| **MyAus App** (AMES / Dept of Social Services) | Multilingual (20 languages) settlement info: housing, healthcare, employment | Generic (not Nepali-specific immigration), no AI, no document reading, no personalisation | Saathi is community-specific, AI-powered, and goes deeper on immigration |

**Key insight:** The existing apps prove the community will download and use Nepali-community apps. They also prove the gap: none of them does immigration AI, document reading, or visa guidance. Saathi is not competing with Nepali lai kaam — it's filling the gap it leaves.

### 6.3 Global Precedent Companies

| Company | What it is | Lesson for Saathi |
|---------|------------|-------------------|
| **Boundless** (US) | Immigration form prep + attorney handoff. ~$45M raised. **Acquired by Payoneer, Jan 2026** | Direct mechanic match: in-language + form prep + handoff. Acquisition proves the model has exit value |
| **Welcome Tech / SABEResPODER** (US) | Trusted in-language information → paid services. ~$70M raised | The Saathi arc: earn trust with information, then monetise adjacent services |
| **Majority** (US) | Migrant neobank for ONE community first. ~$83.5M raised | Go-to-market: own Nepalese-in-Sydney deeply before expanding |
| **Bloom Money** (UK) | Solo-ish, culturally rooted diaspora fintech. ~£1.5M | Closest founder/market shape. Proves modest-funding diaspora products work |
| **Immigify** (US) | AI immigration assistant, 2025 Techstars Accelerator | Proves AI immigration assistants are fundable and real — but US-focused |
| **LemFi** (UK) | Diaspora neobank, $53M Series B Jan 2025 | Diaspora fintech is still actively funded in 2025-26 |
| **Kredete** (US) | Immigrant financial identity (no credit history problem). $22M Series A 2025 | The "new arrival financial layer" problem is a funded space |

---

## 7. Product Scope & The Regulatory Guardrail

**This section governs every feature.** Every feature passes through this filter before it's built.

- ✅ **In scope:** explaining official documents and processes; generating document checklists; tracking deadlines; answering grounded, cited questions; translating/explaining in Nepali; referring to registered professionals; providing general rights information; mental health crisis bridging; fake-agent identification; fair work information.
- ❌ **Out of scope (regulated — do not build):** recommending which visa to apply for; assessing eligibility for a specific person; preparing/lodging visa applications; representing a person; personalised tax advice beyond general information; acting as a mental health service/crisis line (bridge only, never substitute).
- 🔁 **The handoff:** whenever a query crosses into regulated advice, Saathi stops, explains why, and refers to a registered migration agent / registered tax agent / mental health professional.

---

## 8. Feature Requirements

### 8.0 The Absolute Minimum (First User Test — Ship This First)

Four things to validate the core hypothesis ("will Nepali graduates trust and use a grounded, in-language AI companion?"):

1. **Grounded Q&A + guided explainer for ONE process** (485 in 2026: including Level 3 doc requirements, AUD 4,600 fee, age limit 35), in Nepali — retrieved from official sources, cited, refuses when unsupported.
2. **Document checklist** for 485 — what to gather in 2026 (updated for Level 3 requirements). High value, low build.
3. **Safety furniture** — per-answer citation + "last verified" date + persistent disclaimer. Non-deferrable.
4. **Thin referral handoff** — when a query crosses into advice, stop and point to a MARN-verified agent. For MVP: manual (one trusted agent's contact or a button to check MARN).

### 8.1 P0 — Core MVP

#### Module A: Immigration & Visa Guidance

| ID | Feature | Description | Acceptance |
|----|---------|-------------|------------|
| F1 | Process Explainer (485) | Grounded, cited, plain-Nepali walkthrough of the 485 Graduate Visa in 2026: Level 3 requirements, AUD 4,600 fee, age limit 35, timeline | Every answer cites Home Affairs source; refuses when unsupported |
| F2 | Document Reader | Upload/photograph a form, letter, or notice → plain-Nepali explanation of what it is and what it asks for | ≥90% correct identification on common Home Affairs/ATO docs |
| F3 | Document Checklist | For the chosen process, exact documents to gather, personalised by a few questions (including Level 3 bank statement + source-of-funds requirements) | Matches current official requirements; updated when rules change |
| F4 | Deadline Tracker | Record visa expiry & key dates; push reminders | Reminders fire; dates editable; age-limit alert (35) |
| F5 | Grounded Q&A | Ask anything about the process; RAG-grounded + cited, Nepali/English | No ungrounded answers; sources shown; Devanagari rendered correctly |
| F6 | Referral Handoff | Detect "this needs a professional" + directory of MARN-verified agents | Trigger fires on advice-type queries; disclaimer shown every session |

#### Module B: Agent Verification & Protection

| ID | Feature | Description | Acceptance |
|----|---------|-------------|------------|
| F7 | MARN Verification Tool | Enter a migration agent's name or MARN number → check against OMARA register; show current status (registered / not registered / suspended) | Live check against official OMARA register; clear "⚠️ Not Registered" warning |
| F8 | Fake Agent Alert Guide | Explained in plain Nepali: how to spot a fake agent, red flags, what to do if scammed | Covers all common scam patterns seen in 2025–26 fraud spike |
| F9 | Fee Transparency Tool | Show the full cost of the 485 journey: AUD 4,600 visa fee + health check + skills assessment + biometrics + agent fees (if any) | Accurate, cited, clearly labelled as "estimate — verify with Home Affairs" |

#### Module C: Workplace Rights

| ID | Feature | Description | Acceptance |
|----|---------|-------------|------------|
| F10 | Fair Work Rights Explainer | Plain-Nepali explanation of minimum wage, superannuation obligations, allowable work hours on student visa (48 hrs/fortnight during studies), right to join a union, right to complain without losing visa | Covers the most common exploitation patterns in the Nepalese community; cites Fair Work Act |
| F11 | Underpayment Self-Check | Enter your wage, industry, and hours → see if you might be underpaid based on award rates | Cites Fair Work Commission award; clearly disclaims "check with a Fair Work inspector or community legal centre for your case" |
| F12 | Anonymous Reporting Guide | Step-by-step (in Nepali): how to report underpayment to Fair Work, options for anonymous reporting, protections against visa cancellation for reporting | Based on actual Fair Work / Home Affairs protections; addresses the fear that reporting costs you your visa |

#### Module D: Tax, Super & Financial Basics

| ID | Feature | Description | Acceptance |
|----|---------|-------------|------------|
| F13 | Tax & Super Basics | Plain-Nepali explainer: TFN, how to lodge a tax return, what a tax refund is, what superannuation is, who must pay it, when you can access it | Goes beyond the ATO's Nepali page (which exists but is static); personalised by visa type |
| F14 | Departing Australia Superannuation Payment (DASP) Guide | Explained in plain Nepali: when you can claim super when leaving Australia, how to apply, how long it takes, tax implications | Frequently asked, rarely explained in-language; cites ATO DASP page |

### 8.2 P1 — Post-Validation Expansion

#### Module E: Mental Health & Crisis Support

| ID | Feature | Description | Priority |
|----|---------|-------------|----------|
| F15 | Crisis Safe Harbour | Detect crisis signals in conversation (mentions of self-harm, suicide, feeling hopeless) → immediately display in Nepali: "तपाईंको मनोस्थिति बुझ्दछौं। तत्काल सहयोगको लागि यहाँ सम्पर्क गर्नुहोस्:" + Lifeline (13 11 14), Beyond Blue (1300 22 4636), and Nepali-speaking counsellor contacts | Crisis detection + handoff fires reliably; displayed in Devanagari; tested with community workers |
| F16 | Mental Health Resource Hub | Plain-Nepali explanations of: what Medicare covers for mental health, how to access a Mental Health Treatment Plan, what therapy looks like in Australia, stigma normalisation content | All services explained in Nepali; links to services with Nepali-speaking counsellors |
| F17 | "You're Not Alone" Community Stories | Anonymised, moderated stories from Nepalese migrants in Australia who have sought mental health support. Normalises help-seeking in a community with high stigma | Community-contributed; moderated; published only with consent |

#### Module F: Skills Assessment

| ID | Feature | Description | Priority |
|----|---------|-------------|----------|
| F18 | Skills Assessment Navigator | Based on occupation and qualifications: which assessing body (ACS, Engineers Australia, VETASSESS, TRA), what the process looks like, approximate cost and timeline | Narrows to the correct body; cites correct assessing authority page |
| F19 | CDR Guide for Engineers | Plain-Nepali explanation of Competency Demonstration Report: what it is, what each episode requires, common rejection reasons, how to choose the right ANZSCO code | Covers post-Sep 2024 requirement (only EA-accredited qualifications for some pathways) |
| F20 | Skills Assessment Tracker | Track which stage of assessment you're at, upcoming deadlines, document submission reminders | Synced with Deadline Tracker (F4) |

#### Module G: Secure Document Vault

| ID | Feature | Description | Priority |
|----|---------|-------------|----------|
| F21 | Encrypted Document Vault | Store visa letters, passports, assessment letters, tax documents securely. Encrypted at rest and in transit. User-controlled deletion | Encryption at rest + in transit; deletion works; NDB-compliant |
| F22 | Document Expiry Alerts | Alert when stored documents are expiring (passport, visa, health insurance) | Alerts fire 90, 30, 7 days before expiry |

#### Module H: Settlement & Everyday Life

| ID | Feature | Description | Priority |
|----|---------|-------------|----------|
| F23 | Rental Rights Explainer | Plain-Nepali: bond rules (RTBA/NSW Fair Trading), tenant rights, common rental scams, what to do if landlord is exploiting you | Covers NSW and VIC (where 73% of community lives) |
| F24 | Medicare & Health Explainer | Which visa types get Medicare, how OSHC (student health cover) works, how to see a GP, mental health plans, bulk billing | Personalised by visa type |
| F25 | PR Pathway Planner | Based on visa type, occupation, and location: map the realistic pathways to permanent residency, approximate timelines, points score estimator | "Information only" framing; refer to agent for specific advice; cite Dept. of Home Affairs |

### 8.3 P2 — Future Features

| ID | Feature | Description |
|----|---------|-------------|
| F26 | Community Experiences | Moderated, real stories from Nepalese migrants about Australian visa processes, timelines, interview experiences. Sourced with consent from the community |
| F27 | Dual-Country Financial Guide | Remittance comparison, NRN bank account explainer, super portability when returning to Nepal, Nepal-Australia tax treaty basics |
| F28 | Voice Input (Nepali) | Speak questions in Nepali; useful for lower-literacy users and spoken Nepali variation |
| F29 | CV/Resume Localisation | Help skilled migrants adapt their Nepali/Indian CVs to Australian format and norms |
| F30 | Community Events Board | NRNA events, cultural gatherings, community legal clinics, settlement workshops — in one place |
| F31 | Child Education Guide | School enrollment for Nepalese families, NAPLAN, selective schools, TAFE pathways — in Nepali |
| F32 | Template Replication | Re-skin Saathi for other diaspora communities (Indian, Bangladeshi, Sri Lankan in Australia; Nepalese in UK, Canada) |

### 8.4 "Connect" — Agent Marketplace & Case Workspace (Phase 2)

> ⚠️ **Build only after Phase 1 has proven client demand and ≥3–5 founding agent relationships are confirmed.** The information wedge IS the client funnel that solves Connect's two-sided cold-start.

A two-sided layer connecting clients with registered migration agents — quoting, secure document exchange, and shared case status visible to both parties.

| ID | Feature | Description | Acceptance |
|----|---------|-------------|------------|
| C1 | Quote Request | Client submits a structured, info-only summary → matched registered agents return fixed-scope quotes | Client receives ≥2 quotes; platform gives no advice |
| C2 | Agent Matching & Verification | Match by visa type / specialty / language; MARN check at onboarding and on a schedule | Only currently-registered agents can quote; lapsed/suspended removed |
| C3 | Secure Document Transfer | Client shares documents with chosen agent: encrypted, consent-based, access-scoped, time-limited, audit-logged | Encrypted in transit & at rest; access revocable; full audit trail |
| C4 | Shared Case Status | One case timeline visible to both sides (Documents received → Drafting → Lodged → Decision) | Status changes reflected to both; kills "what's happening?" anxiety |
| C5 | Dual Interface | Client view (mobile PWA) + Agent portal (case dashboard) | Both roles operate on the same case object |
| C6 | In-Case Messaging | Scoped client ↔ agent messaging within a case | Logged; keeps relationship on-platform |

**Design tension to respect:** make the workspace genuinely useful to _both_ sides so neither has an incentive to take the relationship off-platform. On-platform workflow value, not a commission gate, is what retains the marketplace.

---

## 9. Technical Approach

> Deliberately lightweight. Validate on a thin stack first. Do not build full GCP/Kubernetes infra for an unvalidated product.

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | Next.js PWA (mobile-first) | Community is mobile-heavy; no app-store barrier |
| Backend | FastAPI (Python) | Async; fits ML/agent integrations |
| Agent orchestration | LangGraph | Founder's existing strength; multi-step grounded flows |
| LLM | Claude (claude-sonnet-4-6 / claude-opus-4-8) | Best-in-class Nepali Devanagari generation + document extraction |
| Document reading | Claude Vision API | Photo/PDF → structured understanding in Nepali |
| Retrieval | Hybrid search (lexical + vector) over official-source corpus, with citation tracking | **Founder's core moat**; grounding + citations |
| Vector/DB | Postgres + pgvector (Supabase) + Redis | Simple, cheap, sufficient for MVP |
| Hosting | Vercel (frontend) + Railway/Supabase (backend) | Fast, cheap, validation-appropriate |
| Knowledge pipeline | Scheduled ingestion of official sources, **versioned**, with change-detection | Rules change often — staleness is a safety risk |
| Crisis detection | Keyword + semantic classifier on incoming messages | Routes to F15 Safe Harbour before any other processing |
| MARN verification | Scheduled crawl of OMARA public register | Stored locally with TTL; daily freshness check |

**Critical architecture notes:**
- **Knowledge freshness is a safety system**, not polish. A stale corpus produces confidently wrong high-stakes answers. Version sources, timestamp answers, surface "last verified" dates.
- **Crisis detection must pre-empt everything.** If a message contains crisis signals, show Safe Harbour before any other response, regardless of what the user asked.
- **Devanagari rendering.** Test on actual Android/iOS devices used by the community before launch; do not assume rendering from desktop development.

---

## 10. Compliance & Regulatory (CRITICAL — existential)

> This product is legal and viable **only** if built as information + referral. Get written legal advice before launch. This section governs the entire product.

| Area | Requirement | Implication |
|------|-------------|-------------|
| **Immigration assistance** | Under the Migration Act 1958, giving immigration assistance for a specific person generally requires registration. Unregistered advice is an offence. | Saathi must stay strictly informational + refer. No eligibility assessment, no pathway recommendation, no lodgement. **Confirm exact statutory boundary with a lawyer.** |
| **Tax** | Personalised tax advice is regulated (Tax Practitioners Board) | General info only; refer to registered tax agents |
| **Mental health / crisis** | Saathi is NOT a mental health service. Crisis detection bridges to professional services; it does not provide crisis counselling. | F15 Safe Harbour bridges to Lifeline/Beyond Blue; never substitutes. Duty of care must be understood — get legal advice. |
| **Fair Work information** | General workplace rights information is not regulated. Specific advice about a person's case may be. | General info + refer to community legal centres / Fair Work Ombudsman. |
| **Referral fees** | Whether/how referral fees from migration agents or accountants can be taken is regulated | Research permitted models before relying on this revenue |
| **Privacy Act 1988 (APPs)** | Handling sensitive personal + visa documents | Data minimisation, explicit consent, encryption at rest, user deletion rights, clear "what we store" UX |
| **NDB (Notifiable Data Breach)** | Must have a breach response plan | Mandatory requirement before storing any personal/document data |
| **ACL (Australian Consumer Law)** | No misleading claims; substantiate | Disclaimers on every answer; "verify with a registered professional" |
| **Source terms of use** | Government sites have usage terms | Confirm permissibility of ingesting each official source |
| **Agent verification duty** _(Connect)_ | Only currently-registered agents may operate on the platform | MARN check at onboarding and on a recurring schedule |
| **Platform liability** _(Connect)_ | If an agent underperforms, Saathi's exposure | ToS positioning Saathi as conduit/platform; agent vetting; indemnity/insurance review |

**Product-level safeguards:** persistent disclaimer; per-answer citations + "last verified" date; refuse-to-guess behaviour; advice-detection → professional handoff; crisis detection → Safe Harbour; audit log of what the agent told each user.

---

## 11. Monetisation

Direct consumer subscription is weak at MVP stage (budget-constrained students; community expects free resources). The path runs: **referral → marketplace platform.** Start with referral (Phase 1), then the Connect module upgrades it into a platform business (Phase 2).

| Model | Description | Phase / Priority |
|-------|-------------|-----------------|
| **Referral / lead-gen** | Free triage + prep; refer regulated/complex cases to registered migration agents & accountants for a fee | Phase 1 — **primary** (sidesteps both regulatory and willingness-to-pay problems) |
| **Agent SaaS subscription** _(Connect)_ | Agents pay recurring fee for case workspace (quotes, secure docs, status, messaging) | Phase 2 — **most leakage-resistant**; recurring revenue |
| **Per-qualified-lead / per-quote fee** _(Connect)_ | Agents pay for each qualified client lead or quote opportunity | Phase 2 |
| **Thin consumer premium tier** | Power features (vault, unlimited Q&A, multi-process, reminders) once retention is proven | Phase 1–2 — tertiary |
| **B2B — Education agent licensing** | Education agents pay to offer Saathi as a value-add to recruited students | Phase 2–3 |

**Recommended blend:** agent **SaaS + per-lead fee**, not pure commission. Pure commission invites both sides to take the relationship off-platform. The marketplace's defensibility is the on-platform workflow value, not a payment gate.

---

## 12. Go-to-Market

The founder's unfair advantage. This is what flips the usual solo-dev distribution weakness.

| Channel | Strategy | Notes |
|---------|----------|-------|
| Nepali community Facebook groups | Large, active; post genuinely helpful content → validation + launch + word of mouth | Identify 3 largest groups + admins before launch |
| Student associations / unis | The 485 cohort lives here; ANU, UNSW, UTS Nepalese student clubs | Offer a free session on "485 in 2026: what changed" |
| SBS Nepali / community media | Credibility + reach; SBS Nepali radio and online audiences | Pitch as a community safety story (fake agents, mental health) |
| NRNA Australia | Existing network, trust anchor, potential distribution partner | Contact current president + Queensland chapter |
| Education agents | Distribution into the student pipeline at source | Pitch as value-add to students post-admission |
| Cultural & religious organisations | Trust anchors in the community | Dashain, Tihar community events as launch moments |

**Launch motion:** validate in FB groups → seed with 485 wedge → word-of-mouth within tight community → expand processes.
**Differentiation story:** "Built by a Nepalese migrant in Australia, for our community. Unlike ChatGPT, every answer is cited and grounded. Unlike Facebook groups, it's not going to give you someone's uncle's outdated opinion."

---

## 13. Success Metrics

### North Star
> Users who complete a full process milestone with Saathi's help (e.g., gathered every required 485 document in 2026 and/or referred to and engaged a verified registered agent).

### Supporting KPIs (Validation Phase → Early Launch)

| Metric | Why |
|--------|-----|
| % of answers users rate "clear and helpful" | Core value |
| % of sessions ending in a completed checklist | Wedge effectiveness |
| Grounding rate (answers with valid citation) | Safety / trust |
| Referral conversion (users → agent engagements) | Revenue signal |
| Week-4 retention through a process | Stickiness |
| "Would pay / would recommend" | Demand |
| Crisis Safe Harbour trigger rate | Safety signal — also indicates mental health burden |
| MARN Tool usage rate | Fake-agent protection usage |

**Connect Module KPIs (Phase 2):** quote-acceptance rate; cases transacted; take-rate / GMV; agent retention; on-platform completion rate (anti-disintermediation); document-transfer security incidents (target: zero).

---

## 14. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Crossing the migration-advice line | Medium | Critical | Strict info+referral scope; legal sign-off; advice-detection guardrail |
| Confidently wrong high-stakes answer | Medium | Critical | Grounded-or-silent; citations; refuse-to-guess; professional handoff |
| Knowledge base goes stale (Level 3 rules changed out-of-cycle) | High | High | Versioned ingestion pipeline; "last verified" dates; periodic review; change alerts |
| Crisis detection false negative (misses a user in crisis) | Low–Med | Critical | Conservative detection thresholds; always show resources proactively in immigration-stress contexts |
| Crisis detection false positive (floods safe harbour) | Medium | Medium | Calibrate; don't suppress resources — a false positive is less harmful than a miss |
| Low willingness to pay | High | High | Referral/B2B model, not consumer subscription |
| Nepali NLP / Devanagari quality gaps | Medium | Medium | Build eval set; human review of Nepali outputs; test on real devices |
| Community trust / one bad story | Medium | High | Conservatism, transparency, disclaimers, slow careful rollout |
| Employer IP / moonlighting clause | Low–Med | Medium | Check CarsGuide contract before building |
| Two-sided cold-start _(Connect)_ | Medium–High | High | Info wedge IS the client funnel; recruit founding agent cohort before opening marketplace |
| Live-case document breach _(Connect)_ | Medium | Critical | Encryption, minimal retention, scoped access, audit, NDB breach plan |
| Platform liability for agent conduct _(Connect)_ | Medium | High | ToS as conduit; MARN verification; agent vetting; indemnity/insurance review |
| Disintermediation _(Connect)_ | High | Medium | Favour SaaS + on-platform workflow value over pure commission |
| MARN checker data freshness | Medium | High | Daily OMARA crawl; "last checked" timestamp shown to user; flag any crawl failures |

---

## 15. Phased Plan & Validation Gate

### Phase 0 — Research & Validation (Weeks 1–8) ← **Complete — entering prototype phase**

Research complete as of June 28, 2026. Findings incorporated into this PRD.

**Validation Gate (must pass before Phase 1 build):**
- Do ≥70% of testers rate it clearly helpful?
- Do users complete the checklist / want to continue?
- Do agents confirm they'd take and pay for referred leads?
- Did legal scoping confirm an info-only product is viable?

→ **All yes:** proceed to Phase 1. **Mixed:** pivot the wedge. **No:** stop — you've saved months.

### Phase 1 — MVP Build & Soft Launch (~Months 2–4)

Build P0 features (F1–F14) properly. Soft-launch to one community channel. Referral pipeline live. Crisis Safe Harbour live from day one. MARN Tool live from day one (both are trust/safety features, not optional).

### Phase 2 — Expand + Launch Connect Marketplace (~Months 5–10)

Add P1 features (F15–F25). Build the Connect module once Phase 1 has confirmed (a) steady client flow and (b) ≥3–5 agents who've agreed to participate.

### Phase 3 — Scale, B2B & Replication (~Months 10–18)

Deepen marketplace; white-label for education agents; evaluate template replication to Indian-Australian or Bangladeshi-Australian communities.

---

## 16. Research & Collection Checklist

### 16A. Start Collecting Now (Pre-Build)

**Knowledge & source material (the retrieval moat)**
- [ ] 485 process corpus — every relevant Home Affairs page captured with URL + date + change-detection baseline (CRITICAL for Level 3 update)
- [ ] Level 3 assessment requirements for student visa — January 2026 Home Affairs update
- [ ] AUD 4,600 fee structure and all subsidiary costs — fee schedule page
- [ ] OMARA register access — for MARN verification tool
- [ ] Fair Work award rates for the industries most Nepalese students work in (hospitality, retail, aged care, cleaning)
- [ ] ATO: DASP process pages + Nepali-language ATO content (what already exists vs what Saathi adds)
- [ ] Beyond Blue + Lifeline + state-specific mental health services with Nepali-speaking counsellors
- [ ] Real questions from Nepali FB groups (anonymised) — harvest + classify by topic
- [ ] Plain-Nepali terminology glossary — bureaucratic English → clear Nepali
- [ ] Gold-standard eval set: ~50 real questions + correct cited answers

**Signals & relationships**
- [ ] Migration agent interviews: lead value, referral appetite, MARN verification cooperation
- [ ] Community mental health workers: what are the gaps they see?
- [ ] NRNA Australia contact: distribution partnership potential
- [ ] SBS Nepali contact: credibility partnership

### 16B. Legal Research (Before Any Build)

- [ ] Exact statutory definition of "immigration assistance" — what is allowed without registration
- [ ] Rules on referral fees from registered migration agents
- [ ] Tax Practitioners Board boundary: general info vs advice
- [ ] Fair Work: when does providing rights information become regulated?
- [ ] Mental health / crisis duty of care: what obligations arise from running a crisis detection feature?
- [ ] Privacy Act / APP obligations for visa/identity documents
- [ ] Terms of use / ingestion permissibility for official Australian government sources
- [ ] CarsGuide employment contract — IP, moonlighting, side-project clauses

---

## 17. Open Decisions

| Decision | Options | Recommendation |
|----------|---------|---------------|
| First wedge | 485 transition / student tax return / skills assessment | 485 — most acute pain in 2026 (Level 3, doubled fee) |
| Free vs paid wedge | Free (growth) vs paid (signal) | Free + referral revenue initially |
| Name | "Saathi" / other | Check trademark availability — "Saathi" is in use by other products globally |
| Dual citizenship feature | Include NRN/dual citizenship info or not | P2 — 73% of survey respondents want it, validates demand |
| Crisis detection threshold | Conservative (low threshold, more triggers) vs precise | Conservative — a false positive is far less harmful than a miss |
| Connect marketplace model | Agent SaaS / per-lead / commission / blend | SaaS + per-lead to resist disintermediation |
| NRNA partnership | Formal partnership / informal / none | Approach early as distribution + trust signal |

---

## 18. Complete Feature Index

### Phase 0 — MVP (Build First)
| ID | Feature | Module |
|----|---------|--------|
| F1 | 485 Process Explainer (Level 3, 2026) | Immigration |
| F2 | Document Reader (AI Vision) | Immigration |
| F3 | Personalised Document Checklist | Immigration |
| F4 | Deadline Tracker + Reminders + Age Alert | Immigration |
| F5 | Grounded Q&A (RAG, Cited, Nepali) | Immigration |
| F6 | MARN-Verified Referral Handoff | Immigration |
| F7 | MARN Agent Verification Tool | Protection |
| F8 | Fake Agent Alert Guide | Protection |
| F9 | Full-Cost Fee Calculator (485 journey) | Protection |
| F10 | Fair Work Rights Explainer | Workplace |
| F11 | Underpayment Self-Check | Workplace |
| F12 | Anonymous Reporting Guide | Workplace |
| F13 | Tax & Super Basics (by visa type) | Financial |
| F14 | DASP Guide (leaving Australia) | Financial |
| **F15** | **Crisis Safe Harbour (crisis detection → handoff)** | **Safety — Day 1** |

### Phase 1 — Post-Validation
| ID | Feature | Module |
|----|---------|--------|
| F16 | Mental Health Resource Hub | Mental Health |
| F17 | "You're Not Alone" Community Stories | Mental Health |
| F18 | Skills Assessment Navigator | Skills |
| F19 | CDR Guide for Engineers Australia | Skills |
| F20 | Skills Assessment Tracker | Skills |
| F21 | Encrypted Document Vault | Vault |
| F22 | Document Expiry Alerts | Vault |
| F23 | Rental Rights Explainer (NSW + VIC) | Settlement |
| F24 | Medicare & OSHC Explainer | Settlement |
| F25 | PR Pathway Planner | Settlement |

### Phase 2 — Future
| ID | Feature | Module |
|----|---------|--------|
| F26 | Community Experiences Section | Community |
| F27 | Dual-Country Financial Guide (NRN, remittances, super portability) | Financial |
| F28 | Voice Input (Nepali) | Accessibility |
| F29 | CV/Resume Localisation for AU Market | Employment |
| F30 | Community Events Board | Community |
| F31 | Child Education Guide | Family |
| F32 | Template Replication (other diaspora communities) | Growth |

### Connect Marketplace (Phase 2)
| ID | Feature | Module |
|----|---------|--------|
| C1 | Quote Request Flow | Marketplace |
| C2 | Agent Matching & MARN Verification | Marketplace |
| C3 | Secure Document Transfer | Marketplace |
| C4 | Shared Case Status | Marketplace |
| C5 | Dual Interface (Client + Agent Portal) | Marketplace |
| C6 | In-Case Messaging | Marketplace |

**Total features: 32 product features + 6 marketplace features = 38 features across 3 phases.**

---

## 19. Appendix — Sources

| Source | Notes |
|--------|-------|
| DFAT Nepal country brief | Population ~213,580 June 2025; remittances; student numbers |
| Dept. of Home Affairs Nepal country profile | Growth ~5×; median age; skill-stream rank; Level 3 update Jan 2026 |
| ABS 2021 Census / Cultural Atlas | Education levels; temporary-visa majority |
| ABS Overseas Migration 2024–25 | 89% temporary visas to Nepal nationals |
| ANU Diaspora Humanitarians Nepal Briefing | Dual citizenship 73%, investment barriers |
| CESLAM mental health crisis report | Suicide surge; 5+ repatriated bodies in 2-month period |
| NSW Government Nepali community mental health profile | Community-specific mental health data |
| Professional.edu.np / UniCoachify | Level 3 assessment change (Jan 2026); doubled 485 fee (Mar 2026) |
| R Associates (rassociates.com.au) | 485 age limit 35; Skills in Demand Visa 482 implications |
| Happy Panda Education / VisaHQ | Fake agent patterns; Level 3 document fraud spike |
| Fair Work Commission | Award rates; employee rights; complaint mechanisms |
| NRNA Australia (nrn.org.au) | Community organisation structure |
| ATO Nepali-language pages | What ATO already offers in Nepali |
| SBS Nepali | Superannuation in Nepali; community media reach |
| Google Play: Nepali lai kaam, Sam Nepali | Existing Nepalese community apps in AU |
| AMES Australia / MyAus App | Generic multilingual settlement app |
| Immigify (Techstars 2025) | AI immigration assistant precedent |
| LemFi ($53M Series B, Jan 2025) | Diaspora fintech still actively funded |
| Kredete ($22M Series A, 2025) | Immigrant financial identity |
| MDPI 2025 paper: Human-Centered AI for Migrant Integration | Academic validation of RAG-based migrant information systems |
| Boundless (Payoneer acquisition Jan 2026) | Direct mechanic precedent + acquisition proof |

---

### Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | June 10, 2026 | Initial pre-validation PRD + research checklist + validation gate |
| 0.2 | June 10, 2026 | Added Connect agent marketplace (8.4); platform model; marketplace compliance |
| 0.3 | June 10, 2026 | Added precedent companies; Minimum MVP (8.0); collection checklist (16A) |
| **1.0** | **June 28, 2026** | **Full research-complete revision: 2026 market data (Level 3, AUD 4,600 fee, age limit 35, mental health crisis, fake-agent fraud spike); 9 new feature modules (B: Protection, C: Workplace Rights, D: Financial, E: Mental Health/Crisis, F: Skills Assessment, G: Document Vault, H: Settlement); competitive landscape updated with Nepali lai kaam, Sam Nepali, MyAus App, Immigify, LemFi, Kredete; total 38 features across 3 phases; crisis detection elevated to Day 1 safety requirement; Phase 0 marked complete** |
