# Naming Conventions — Karki Labs

This document is the standing naming convention for all Karki Labs projects. It exists so that names are assigned by a rule rather than invented ad hoc, and so that our naming survives a product pivot without a rename cascade.

Theme: **Nepal mountains, rivers, and lakes.**

---

## 1. Core principle

> **Theme the infrastructure, not the product.**

Names split into three layers by how likely they are to change:

| Layer | Changes on a pivot? | Naming style | Who sees it |
|---|---|---|---|
| **Product brand** | Yes — always | Benefit-driven, meaningful to users | End users |
| **Platform** | Rarely | One flagship peak | Internal + dev-facing |
| **Services** | Never (roles are permanent) | Geography theme, by architectural role | Internal |

The consumer brand is tied to *what the product does for users*, so it must be free to change. Services are tied to *architectural roles* — "the thing that stores data," "the thing that moves data" — which are identical in any product we ever build. Therefore the geography theme lives on services and the platform, and **never** on the public brand.

**Consequence:** when we pivot from one product to another, we rename exactly one thing — the product brand — and everything underneath stays valid.

---

## 2. The taxonomy rule

Every service name maps a geographic category to an architectural role. Name by the role a component plays **structurally**, never by the current product's domain (never "visa", "migration", etc.).

### Primary mapping

| Geographic category | Architectural role |
|---|---|
| **Peaks** (mountains) | Compute & logic — stateless brains, services, processing |
| **Rivers** | Data in motion — pipelines, buses, streaming, delivery |
| **Lakes** | Data at rest — databases, caches, session/state stores |

### Extension categories (for roles that aren't compute/move/store)

| Geographic category | Architectural role |
|---|---|
| **Passes** (e.g. Thorong La) | Ingress / egress — gateways, edges, the way in and out |
| **Viewpoints** (e.g. Kala Patthar) | Observation — monitoring, logging, tracing, dashboards |

Because the mapping targets *what the component does*, not *what the product is about*, every name stays correct forever. A retrieval service is a river whether it retrieves visa rules or recipe data.

---

## 3. Current name assignments

### Product brand
- **Saathi** — "companion." The visa guidance agent for the migration community. This is the only name end users see. Deliberately **not** a geography name so it is free to be replaced on a pivot. Requires trademark/domain clearance (see §5).

### Platform
- **Sagarmatha** — the Nepali name for Everest. The shared agentic foundation every Karki Labs product sits on. Only the product brand on top changes across products.

### Services

| Service role | Name | Category | Rationale |
|---|---|---|---|
| Agent orchestration / reasoning core | **Manaslu** | Peak | "Mountain of the Spirit" (*manasa* = intellect) — the thinking core |
| API gateway / edge | **Thorong** | Pass | Thorong La, the high pass — a pass *is* the way in and out |
| Auth / identity / accounts | **Annapurna** | Peak | Goddess of provision — provisions users and access |
| Guardrails / policy / safety | **Machapuchare** | Peak | Sacred peak legally forbidden to climb — enforces lines that cannot be crossed |
| Knowledge base / primary datastore | **Rara** | Lake | Largest, deepest lake — the big store of record |
| Session / conversation state (Redis) | **Tilicho** | Lake | High glacial lake — holds transient state "at altitude" |
| Ingestion pipeline | **Karnali** | River | Longest river — long pipelines carrying data from far upstream |
| Retrieval / RAG | **Gandaki** | River | Deepest gorge, carries fossils downstream — surfaces buried knowledge on demand |
| Event bus / SSE streaming | **Koshi** | River | Sapta Koshi = seven rivers converging — the message confluence |
| Notifications / delivery | **Trishuli** | River | Fast river named for Shiva's trident — pushes messages out quickly |
| Observability / monitoring | **Kala Patthar** | Viewpoint | The vantage you climb to watch the whole range — logs, traces, metrics |

---

## 4. How to name a new service

Follow these steps whenever you add a component.

1. **State the role in one structural sentence.** "It stores X," "it moves X from A to B," "it computes X," "it lets traffic in," "it watches the system." Ignore what the product is about.
2. **Pick the category** from the taxonomy in §2 that matches the verb — store → lake, move → river, compute → peak, ingress/egress → pass, observe → viewpoint.
3. **Choose an unused name** from that category (see the name bank in §6). Prefer names whose real-world characteristic echoes the role (longest river for the longest pipeline, deepest lake for the store of record) — a good echo makes the name self-documenting.
4. **Check it's not already taken** in this document and not easily confused with an existing name (avoid two names starting with the same syllable if you can).
5. **Register it** by adding a row to the table in §3, with the role, category, and a one-line rationale.
6. **Do not** encode the product domain in the name, and **do not** give it a name from a category that doesn't match its role, even if the name "sounds nicer." Consistency of the rule is worth more than any individual name.

### Anti-patterns to avoid
- Naming a datastore after a mountain because the mountain name is prettier. (Breaks the rule; the next person can't infer the role.)
- Putting "visa," "migration," or any product term in a service name. (Breaks portability — the whole point.)
- Theming the public product brand with a mountain name. (Locks a user-facing, trademark-bearing name into geography and couples it to a pivot.)

---

## 5. Trademark, domain & clearance

- **Only the product brand needs clearance.** Saathi is user-facing and trademark-bearing — verify availability of the name, matching domains, and app-store listing in Australia and any target market before committing. Note that "Saathi" is a common word, so clearance is not guaranteed; have a backup.
- **Codenames need no clearance.** Manaslu, Karnali, Rara, etc. are internal — users never see them, so there is nothing to trademark or register.
- **If a service name ever becomes public** (status page, dev docs, open-sourced repo), re-check it for conflicts at that point, not before.

---

## 6. Name bank (unused, reserved for future services)

Pull from these when registering a new service. Move a name into §3 when you claim it.

- **Peaks (compute/logic):** Dhaulagiri, Nuptse, Lhotse, Ama Dablam, Pumori, Cho Oyu, Gauri Shankar, Langtang, Makalu
- **Rivers (data in motion):** Bagmati, Marsyangdi, Bheri, Seti, Rapti, Kali, Arun, Tamur, Budhi Gandaki
- **Lakes (data at rest):** Phewa, Begnas, Gosaikunda, Shey Phoksundo, Rupa, Gokyo
- **Passes (ingress/egress):** Larke La, Cho La, Kongma La, Renjo La
- **Viewpoints (observation):** Poon Hill, Sarangkot, Chandragiri, Tengboche

---

## 7. Quick reference

- **Product = benefit name (Saathi), not geography, renamed on pivot.**
- **Platform = one flagship peak (Sagarmatha).**
- **Services = geography by role: peaks compute, rivers move, lakes store, passes gate, viewpoints observe.**
- **Never encode the product domain in a service name.**
- **Register every new name in §3; pull from §6.**
