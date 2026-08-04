# AGIConstructor.com

**A reference layer for the auditable construction of general-capability systems.**

It publishes doctrine, ontology, audit instruments and evidence ledgers for recording what has been constructed — without declaring whether a system is AGI. Component-level audit (via ACL) is one instrument within that layer, not the whole of it.

---

> Whatever form general intelligence takes, it will have been constructed. Every component is auditable.

---

## The Position

Public discussion of artificial general intelligence runs on a question that cannot be settled: *has it arrived?* The question depends on a definition no two parties share, and it resolves into argument rather than evidence.

This asset takes a different position. General capability is not announced — it is assembled, from models, memory, tools, environments, feedback, coordination, authority and verification. Each of those is a component. Each component can be examined. What has been built, at what evidentiary standard, is a matter of record rather than opinion.

**AGIConstructor.com publishes that record's method.**

## What Is Here

AGIConstructor is a layered reference asset. Each layer presupposes the one above it — see [ARCHITECTURE.md](./ARCHITECTURE.md) for the full stack.

| Layer | Document | Role |
|---|---|---|
| Foundation | **[FOUNDATION_DOCTRINE.md](./FOUNDATION_DOCTRINE.md)** | Why construction is a classificatory position, not a prediction; the AGIConstructor↔ACL relationship |
| Ontology | **[CONSTRUCTION_ONTOLOGY.md](./CONSTRUCTION_ONTOLOGY.md)** | The audit surfaces, grouped into families; neither necessary nor sufficient conditions for AGI |
| Instrument | **[ACL-1.0.md](./ACL-1.0.md)** | The AGI Component Ledger — eight components, four states, four evidence tiers, seven boundary cases (frozen) |
| Ledgers | [schema/](./schema/) · [templates/](./templates/) · [examples/](./examples/) | Machine-readable schema, blank templates (JSON/YAML/CSV), one worked illustrative example |
| Registry | *future* | Machine validation and a versioned public registry of published ledgers |

**[ACL-1.0](./ACL-1.0.md)** is the audit instrument at the centre of the asset: a published protocol with eight components, four classification states, four evidence tiers, seven boundary cases, and an explicit statement of what it does not measure.

ACL is designed to be applied by others without permission. An analyst, journalist, evaluation researcher, or diligence team can run a ledger on a real system and publish the result. That is its intended use. Start from a blank template in [templates/](./templates/) and validate against [schema/agicl-1.0.schema.json](./schema/agicl-1.0.schema.json).

Governance: [DECISION_LOG.md](./DECISION_LOG.md) (append-only decision record) · [LICENSE](./LICENSE) (dual: CC BY 4.0 for standards, MIT for artifacts) · [CHANGELOG.md](./CHANGELOG.md) · [RELEASES.md](./RELEASES.md) · [ACL-2.0-CANDIDATES.md](./ACL-2.0-CANDIDATES.md) (post-publication design candidates; ACL-1.0 stays frozen).

## What This Is Not

- Not a prediction of AGI timelines
- Not a safety or alignment assessment
- Not a ranking or leaderboard
- Not a verdict on whether any system is or is not AGI

The protocol classifies. It does not conclude.

## Applying ACL

1. Read [ACL-1.0](./ACL-1.0.md), Sections 3–7.
2. Fix the object: name the exact system and version.
3. Work component by component. Assign an evidence tier before assigning a state.
4. Check disqualifiers before accepting any claim.
5. Publish with access limits and boundary cases attached.

No registration, notification, or attribution beyond citation is required.

## Provenance

AGIConstructor.com is developed and maintained by **Sohadot** — an independent practice building governed reference assets from premium domain properties, using a doctrine-first methodology: foundation, thesis, standard, reference.

Related published standards from the same practice include the **Evidence Posture Standard** at Hoax.ai, which governs the separation between classifying evidence and performing a verdict. ACL applies the same separation to capability claims.

Contact: agent@sohadot.com

## Status

| | |
|---|---|
| Protocol | ACL-1.0 |
| Status | Published |
| Issued | 2026-08-01 |
| Maintainer | Sohadot |

Substantive revisions are issued under new version numbers. Published versions remain retrievable.
