# ACL-2.0 Design Candidates

**A register of limitations identified after ACL-1.0 publication. Candidates only — none is in force.**

Status: Open register (design input, not a specification)
Opened: 2026-08-03
Maintainer: Sohadot

---

## Purpose and rules

ACL-1.0 is **published and frozen**. Its §11 commits that "ACL-1.0 will not be silently modified; substantive changes are issued as ACL-1.1 or later." This file is where post-publication observations are recorded so that the frozen text is respected while nothing is lost.

**Rules for this register:**

1. Nothing here is in force. ACL-1.0 is the only current instrument.
2. Nothing here is retrofitted into `ACL-1.0.md`.
3. Several candidates below are **breaking changes** (they alter states, axes, or component structure). Breaking changes cannot ship as ACL-1.1; they require **ACL-2.0**, issued with 1.0 remaining retrievable.
4. A candidate is not a commitment to adopt it. Some may be rejected in the 2.0 design phase. The prerequisite for that phase is a stable foundation (doctrine + ontology) and at least one real-system trial of ACL-1.0.

---

## C-01 — Separate the "construction finding" axis from the "evidence posture" axis
**Type: breaking (states).** ACL-1.0's four states (`Constructed / Partial / Claimed / Absent`) mix two different things: *what was found in the system* and *the posture of the evidence*. `Claimed`, in particular, is an evidence-posture verdict sitting on the same axis as `Constructed`, which is a construction verdict. A component genuinely built inside a closed system, with only Tier C evidence public, is recorded `Claimed` — not because it is unbuilt, but because it is unproven. A future version could split this into two orthogonal axes:
- **Construction finding:** demonstrated / partial / not demonstrated / demonstrably absent
- **Evidence posture:** Tier A / B / C / D / no admissible evidence

## C-02 — Add an explicit `Undetermined / access-limited` state
**Type: breaking (states).** ACL-1.0 routes closed-system, untestable components to `Claimed` with an access-limit note (B-06). But a component that is closed, carries *no explicit claim*, and *cannot be inspected* is neither `Claimed` nor `Absent`. A dedicated `Undetermined` finding would stop auditors from assigning an inaccurate state merely to fill all eight rows. (Partially mitigated in 1.0 by the access-limit note; a first-class state is cleaner.)

## C-03 — Make the family structure part of the instrument
**Type: additive-to-breaking (reporting).** The [Construction Ontology](./CONSTRUCTION_ONTOLOGY.md) groups the eight into three families (capability substrate & operational interfaces / integrative mechanisms / control and assurance). ACL-1.0's flat list does not encode this. A future version could make family-awareness part of the report so "8/8" cannot be read as eight measurements of the same kind.

## C-04 — Per-component admissible evidence, not a uniform A–D ladder
**Type: breaking (evidence).** ACL-1.0 applies one A–D tier ladder to all eight components. But admissible evidence differs by component: black-box independent reproduction (nominally Tier A) can establish a *behavioral* surface (e.g., C2 Memory alters later behavior) yet cannot establish an *architectural* one (e.g., C1 model composition, C7 authority enforced at the execution layer, C8 verifier independence). Reproduction proves behavior, not internal structure. A future version could define admissible evidence per component rather than one global ladder.

## C-05 — Record evidence *attributes* separately from a single tier letter
**Type: breaking (evidence).** Rather than collapsing evidence quality into one letter, a future version could record attributes independently: source independence, access level, reproducibility, version-match, recency, and declared conflict of interest. The tier could then be derived from attributes rather than asserted.

## C-06 — Add a "claim-object mismatch" check *before* component assessment
**Type: additive (procedure).** Some ACL-1.0 disqualifiers (e.g., C1's "ensemble routing presented as single-model generality") are really about the *object of the claim shifting* (from a model to a system), not about the component being absent. A future version could add an explicit **"fix the object"** disqualifier stage — detecting claim-object mismatch — ahead of per-component assessment. ACL-1.0 already has "fix the object" as procedure step 1; this would strengthen it into a first-class check.

## C-07 — Sharpen the C3 (Tools) audit-question wording
**Type: editorial (deferred).** ACL-1.0's C3 asks whether the system can "select, sequence, and recover from failure across tools it was not scripted for." "Not scripted for" can be misread as invoking tools the system was neither provisioned nor authorized to use. The intended sense is *authorized* tools whose *selection and sequencing were not pre-determined*. Because it is a wording change to the frozen text, it is deferred to a versioned release, not patched in place.

## C-08 — Reconsider the short name "ACL"
**Type: naming (partially decided).** "ACL" collides with the well-established "Access Control List," and ACL-1.0's own C7 component is *Authority* — a genuine source of confusion. **Decision applied in this phase:** technical artifacts use the `AGICL` namespace (e.g., `schema/agicl-1.0.schema.json`) to reduce collision, while the **published human-readable protocol name remains `ACL-1.0`** to preserve provenance. A full rename of the protocol, if ever adopted, is a 2.0-era decision and is not made here.

---

## Prerequisites before any ACL-2.0 design begins

1. Foundation Doctrine and Construction Ontology stable (this phase).
2. At least one **real** ACL-1.0 ledger run end-to-end (the current example is illustrative only).
3. A decision, per candidate above, to adopt / defer / reject — recorded before drafting.
