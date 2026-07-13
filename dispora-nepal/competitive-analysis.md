# Saathi — Competitive Analysis & Strategic Re-assessment

**Project:** Saathi / Manaslu (scan & visa form-fill agent service)
**Date:** July 13, 2026
**Status:** Decision record — re-assessment triggered by discovery of competing visa-AI tools
**Author:** Prabin Karki
**Supersedes nothing; updates:** `docs/MARKET-RESEARCH.md` (June 28) with the July 2026 landscape

---

## 1. Why this document exists

Ten visa-AI tools were identified in the wild, several doing AI form-filling
today. This document answers: **is Saathi/manaslu still worth building, and if
so, in what form?**

**Verdict up front:** the idea survives **only in its original wedge form**
(Nepali-language, community-trusted, journey-long). The horizontal version —
a generic English "AI fills your visa PDF" service — is already commoditized
and should not be built.

---

## 2. Landscape (July 2026)

| Tool | What it actually is | Market | Threat |
|------|--------------------|--------|--------|
| [Instafill.ai](https://instafill.ai/) | Generic AI PDF filler. **Has a dedicated [Form 80 page](https://instafill.ai/forms/80)** (840 fields / 19 pages, "filled in under a minute") + an Australian-immigration category. Extracts from source docs; reports per-field source & reasoning. US-based, horizontal (legal/insurance/healthcare/immigration) | Global, B2B+B2C | 🔴 **Highest** — commoditizes the mechanical fill, incl. our exact form |
| [Migraide](https://migraide.com) | Upload passport/docs → AI fills forms + cover letters + checklists. Schengen (29 countries) today; UK/US/Canada/**Australia planned**. Individual + agency dashboards | Schengen → expanding | 🟠 Closest business-model match; wrong forms so far |
| [Visix](https://visix.me/) | Generic visa form automation, 150+ countries, $0/$29/$99 tiers, tourist/study/transit tilt | Global | 🟠 Breadth play, shallow per-form depth |
| [AustraliaVisa.ai](https://australiavisa.ai/) | AU-specific **eligibility checker** — "personalized visa recommendations", scored assessments | AU | 🟡 Different product; does what Saathi legally refuses to do (see §4.3) |
| [Famsia](https://famsia.ai/) | Eligibility checks 190+ countries, itineraries, cover letters | Global | 🟡 Thin/generic |
| [Fillwise](https://fillwise.ai/blog/travel-agents-guide.html) | Chrome extension for **travel agents**: passport photo → Schengen/UK/ESTA/eTA forms, batch mode, 100+ languages | Travel-agent B2B | 🟡 Short-stay visas, agent workflow — not AU migration |
| [Visas.AI](https://visas.ai/) | Platform for **US immigration attorneys** ($100–130/seat/mo); AI paralegal, briefs, RFEs | US legal B2B | ⚪ Different country & buyer |
| [Torly.ai](https://torly.ai/) | UK Innovator Founder Visa business-plan builder (£24–79/mo) | UK founders | ⚪ Unrelated niche |
| [Quillio](https://quillio.au/) | AI legal assistant for AU **lawyers** (contracts, chronologies, case law) — not a visa tool | AU legal B2B | ⚪ Not a competitor |
| nuronai.org | Dead (404) | — | ⚪ — |

**Also found:** [FormMate 80](https://formmate80.com.au/) — a **free** AU-specific
Form 80 web filler; [formli.ai](https://formli.ai/en/forms/australia-form80) —
step-by-step Form 80 guide; plus generic PDF fillers (pdfFiller, PDFliner,
SignNow) all offering Form 80 templates.

**Checked and confirmed absent:** any Nepali-language AU-immigration product.
The only Nepali-language support found anywhere is official — Home Affairs'
[digital assistant](https://immi.homeaffairs.gov.au/help-support/tools/digital-assistant)
with TIS interpreter phone access, and
[AUSCO settlement PDFs](https://immi.homeaffairs.gov.au/settling-in-australia/ausco/information-in-your-language/nepali).

---

## 3. Findings

### F1 — The mechanical fill is commoditized
"AI extracts your documents and fills a visa PDF" exists today at every price
point including **free** (FormMate 80). Instafill fills Form 80 specifically.
Competing on fill speed, form breadth, or price is a lost race against
better-resourced horizontals. **Any version of Saathi whose headline value is
"we fill the form" is dead on arrival.**

### F2 — The original PRD wedge is still unoccupied
Nobody has: a Nepali-language layer, community-trust distribution, bilingual
field-by-field explanation, AU-migration depth (MRZ/cross-doc validation,
Home Affairs field semantics, cited freshness), or a **persistent migrant
profile** reused across the multi-year journey (500 → 485 → 189/190). Every
competitor is transactional, English-only, and journey-blind.

### F3 — Compliance posture is a moat, not a constraint
Eligibility-assessment tools (AustraliaVisa.ai, Famsia) operate near the
Migration Act's definition of "immigration assistance" without apparent MARA
registration. Saathi's fill-only / no-suggestions / MARN-handoff design is the
position a community can trust, a regulator can't easily kill, and competitors
structured around "recommendations" cannot copy without rebuilding.

---

## 4. Decision

### 4.1 Proceed — as the wedge product, not the horizontal one

Keep building manaslu (the headless scan/fill agent engine): the components
already designed are exactly where the defensible value lives —

| Differentiator | Manaslu component | Who else has it |
|----------------|-------------------|-----------------|
| Persistent provenance-tracked profile (fill once, next form ~free) | Profile-facts vault (docs 03/08) | Nobody — all competitors are one-shot |
| Bilingual explain-while-fill (every field in Nepali at confirmation) | Bilingual field manifests + review events (docs 03/06) | Nobody |
| AU-migration depth | MRZ/ABN/BSB validators, cross-doc consistency, Form-80 semantics | Generic fillers can't justify single-country depth |
| Trust/compliance | Fill-only tool contracts, audit annex, MARN handoff | Structurally absent in "recommendation" products |
| Distribution | Nepali FB groups, community word-of-mouth (Majority playbook) | Unreachable for horizontal tools |

### 4.2 Repositioning (what changes in messaging & priority)

- Headline is **"understand and complete your visa forms in your own language, from your own documents"** — not "AI form filler".
- The **vault + bilingual explanation** move from nice-to-have to core MVP; the raw fill is table stakes.
- Monetization cannot be per-fill (price floor is $0) — it's the journey: free first form, premium vault/multi-form/PDF history, later MARN-agent referrals (per PRD §7).

### 4.3 Explicitly not doing

- English-first horizontal form filler (F1).
- Eligibility scoring / visa recommendations (legal boundary + crowded).
- Competing on number of supported forms.

---

## 5. Kill criteria (honest tripwires)

1. **Community validation fails** — the Nepali landing-page/FB-group test (§6) produces < ~100 genuinely interested users or no engagement on real questions → stop or pivot audience.
2. **Instafill/Migraide ships a Nepali-localized AU-migration flow with a persistent profile** → the wedge is gone; do not fight it.
3. **Legal memo review concludes even fill-only transcription is MARA-restricted** → product as designed is not shippable; only the explain/checklist layer survives.
4. **Unit economics fail** — cost per completed form-fill session persistently > ~$0.50 with no willingness to pay for premium → engine is a hobby, not a business.

## 6. Cheap validation before more code (2 weeks, ≪ $500)

1. Nepali landing page ("फारम भर्न सहयोग, आफ्नै भाषामा") + waitlist; small FB-group seeding. Target: 100+ signups.
2. Two weeks of question harvesting in Nepali-in-Australia FB groups (PRD's own next step) — count Form-80/document questions specifically.
3. 5 concierge form-fills done manually with real community members — measures trust, extraction difficulty, and time-to-value before automation exists.
4. 3–5 MARN agent conversations — validates the referral leg of monetization.

Build continues in parallel only on wedge-critical components (vault, manifest,
bilingual explain data model); anything horizontal waits for validation.

---

## 7. Sources

visas.ai · famsia.ai · fillwise.ai · instafill.ai (+ /forms/80) ·
australiavisa.ai · visix.me · quillio.au · nuronai.org (dead) · torly.ai ·
migraide.com · formmate80.com.au · formli.ai · immi.homeaffairs.gov.au
(digital assistant, Nepali AUSCO resources). Fetched/searched July 13, 2026.

*Related: `PRD.md` (v2.0) · `docs/MARKET-RESEARCH.md` (June 28) ·
`architecture-services-and-features.md` (v1.1) · `legal-memo.md` ·
manaslu `docs/architecture/`*
