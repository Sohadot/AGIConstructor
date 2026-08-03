# Construction Ontology — Audit Surfaces of Constructed General-Capability Systems

**A companion lens for ACL-1.0's eight components. Interpretive, not a protocol change.**

Status: Foundation document
Issued: 2026-08-03
Maintainer: Sohadot
License: CC BY 4.0 (see [LICENSE](./LICENSE))

---

## 1. What this document is — and is not

This document organizes the eight components of [ACL-1.0](./ACL-1.0.md) into distinguished families and states, plainly, what those components are and are not.

**It does not change ACL-1.0.** ACL-1.0 treats the eight components as a flat set of eight independent findings, and it continues to. The grouping below is an **interpretive lens** that helps a reader understand *why* the eight are not all of the same kind. An ACL-1.0 ledger still carries eight independent component findings, each with a state and a tier, exactly as the published protocol specifies. Nothing here is retrofitted into the protocol.

Where this ontology exposes a genuine limitation in ACL-1.0 — for example, that treating all eight as "components" of the same order obscures a real difference in kind — that limitation is recorded as a **candidate for a future version** in [ACL-2.0-CANDIDATES.md](./ACL-2.0-CANDIDATES.md). It is not acted on here.

## 2. Audit surfaces, not conditions for intelligence

The eight are **audit surfaces**: places where the construction of a general-capability system can be examined. They are deliberately **not** asserted to be:

- **necessary** — a system exhibiting general capability might lack multi-agent coordination, a persistent environment, external execution authority, or an embedded independent verifier;
- **sufficient** — a system may possess all eight and exhibit nothing resembling general intelligence;
- **exhaustive** — the set reflects the architecture of current constructed systems and is expected to grow.

ACL-1.0 already states this in its §10 (sufficiency of the component set). This document elevates that caution to the front: **the eight dimensions are audit surfaces for constructed general-capability systems, not necessary or sufficient conditions for general intelligence.**

## 3. The three families

The eight components are not of the same order. Naming them all "components" hides a real difference in kind. Grouped by role in the constructed system:

### Family I — Constitutive substrate
*The materials from which capability is assembled.*

| Component | Audit surface |
|---|---|
| **C1 — Models** | The inference substrate producing outputs |
| **C2 — Memory** | Retention of state that persists and alters later behavior |
| **C3 — Tools** | Invocation and composition of external capability |
| **C4 — Environments** | Operation within a state-bearing world with persistent consequences |

These are the parts a system is *made of*. Their audit surface is largely architectural: what is present, disclosed, and reproducible.

### Family II — Integrative mechanisms
*What binds the substrate into behavior over time.*

| Component | Audit surface |
|---|---|
| **C5 — Feedback** | Incorporation of outcome signal into subsequent behavior |
| **C6 — Coordination** | Division of work across processes with conflict resolution |

These are not materials but *dynamics*. Their audit surface is behavioral over time: does outcome change behavior, and what resolves conflict between processes.

### Family III — Control and assurance
*What governs and confirms the constructed system, surrounding rather than constituting the capability itself.*

| Component | Audit surface |
|---|---|
| **C7 — Authority** | Allocation of permission — what may be done unilaterally vs. with authorization |
| **C8 — Verification** | Independent confirmation that outputs are correct, repeatably |

These are the most consequential to distinguish. **Authority and Verification are not asserted to be part of intelligence.** They are part of the *constructed system that surrounds a capability* and makes it operable and trustworthy in an institutional setting. A system can be intelligent-seeming with neither; both are nonetheless first-class audit surfaces because their presence or absence is exactly what an adopting institution needs on the record.

## 4. Why the families matter to an auditor

- They prevent a **category error**: reading "8/8 Constructed" as though all eight measured the same kind of thing. Four are materials, two are dynamics, two are controls. A ledger dense in Family I but empty in Family III describes a very different system from the reverse.
- They locate the components **most often absent and most often material** to adoption — C7 (Authority) and C8 (Verification), the control-and-assurance family — which public capability claims routinely omit.
- They clarify that a system lacking a Family II or Family III surface is not thereby "less intelligent"; it is differently constructed. This keeps the construction axis clear of the capability axis (see [FOUNDATION_DOCTRINE.md](./FOUNDATION_DOCTRINE.md) §5).

## 5. The relationship to what a system *is*

The [Foundation Doctrine](./FOUNDATION_DOCTRINE.md) §4 fixes three distinctions that this ontology must respect:

1. **What exists** in the system — the true construction.
2. **What is publicly evidenced** — the disclosed or reproduced subset.
3. **What ACL-1.0 can classify** — what the states, tiers, and disqualifiers resolve.

The families describe surfaces of (1), but a ledger only ever reports the part of (1) that (2) supports and (3) can resolve. The ontology never licenses inferring an unevidenced component from the presence of others in its family. Family membership is explanatory, not inferential.

## 6. Known limitations of the current ontology

Recorded here for transparency; carried forward as design candidates in [ACL-2.0-CANDIDATES.md](./ACL-2.0-CANDIDATES.md). None is acted on in ACL-1.0.

- The flat eight-component list does not itself encode the family distinction; a future version could make family-awareness part of the instrument.
- ACL-1.0's single "state" axis blends *what was found in the system* with *the posture of the evidence*. The families sharpen this observation but do not resolve it.
- Admissible evidence differs by family (black-box reproduction can establish a behavioral surface but not always an architectural one), which ACL-1.0's uniform A–D tiering does not yet reflect per component.
