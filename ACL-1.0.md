# ACL-1.0 — AGI Component Ledger

**A component-level audit protocol for general capability claims.**

Version: 1.0
Status: Published
Issued: 2026-08-01
Maintainer: AGIConstructor.com

---

## Governing Sentence

> Whatever form general intelligence takes, it will have been constructed. Every component is auditable.

---

## 1. Purpose

ACL exists to replace a question that cannot be answered with a question that can.

The unanswerable question is *"Is this AGI?"* — it depends on a definition no two parties share, and it resolves into argument rather than evidence.

The answerable question is *"Which components does this system demonstrably possess, at what evidentiary standard, and which are absent?"*

ACL does not predict arrival. It does not rank systems. It does not issue verdicts on generality. It produces a **ledger**: a component-by-component record of what has been constructed, what is partial, what is merely claimed, and what is missing.

An ACL audit is complete when every component carries a state and a stated evidence tier. It is not complete when it carries a conclusion.

## 2. Scope

**In scope.** Any system, product, research artifact, or public claim asserting general, autonomous, or open-ended capability.

**Out of scope.** Narrow systems making narrow claims. Benchmark performance as such. Capability forecasting. Safety evaluation. Commercial or ethical judgment of the system or its developer.

ACL is a **construction ledger**, not a safety assessment. A system may score highly on ACL and be unsafe. A system may be safe and score low. The two axes are independent and must not be conflated in reporting.

## 3. The Eight Components

Each component carries: a definition, the audit question, and the disqualifiers that prevent a **Constructed** state regardless of claim strength.

### C1 — Models
*The inference substrate producing outputs.*

**Audit question:** What model or models perform inference, and is the composition disclosed?

**Disqualifiers:** Undisclosed composition where the claim depends on it; ensemble routing presented as single-model generality.

### C2 — Memory
*Retention of state that persists across tasks and sessions and demonstrably alters later behavior.*

**Audit question:** Does information acquired in one task change behavior in a later, separate task without being re-supplied?

**Disqualifiers:** Context window length alone. Retrieval over a static corpus. Session state that resets at evaluation boundaries. Memory that is written but never demonstrably read.

### C3 — Tools
*Invocation of external capability, including composition of multiple tools toward a single goal.*

**Audit question:** Can the system select, sequence, and recover from failure across tools it was not scripted for?

**Disqualifiers:** Fixed pipelines presented as autonomous selection. Single-tool invocation. Human selection of the tool with the system only filling arguments.

### C4 — Environments
*Operation within a state-bearing world where actions have persistent consequences.*

**Audit question:** Does the system act on an environment whose state its own prior actions have changed?

**Disqualifiers:** Stateless request-response. Simulated environments reset between every trial where the claim implies persistence.

### C5 — Feedback
*Incorporation of outcome signal into subsequent behavior.*

**Audit question:** Does outcome information change behavior, and on what timescale — training-time only, or during operation?

**Disqualifiers:** Training-time feedback presented as runtime adaptation. Self-critique loops with no external outcome signal. Feedback whose effect is not measured.

### C6 — Coordination
*Division of work across multiple agents or processes with resolution of conflict between them.*

**Audit question:** When two processes produce incompatible outputs, what resolves the conflict, and is that resolution mechanism disclosed?

**Disqualifiers:** Sequential prompting described as multi-agent. Coordination with no conflict-resolution path. Orchestration performed by a human operator.

### C7 — Authority
*The allocation of permission — what the system may do unilaterally, what requires authorization, and who holds it.*

**Audit question:** Is there an explicit boundary between actions the system takes on its own and actions requiring external authorization, and is that boundary enforced or advisory?

**Disqualifiers:** Boundary defined only in prompt text. Boundary present in documentation but not enforced in execution. No named holder of authorization.

*Note: C7 is the component most frequently absent from public capability claims and most frequently material to institutional adoption.*

### C8 — Verification
*Independent confirmation that outputs are correct, and repeatable performance of that confirmation.*

**Audit question:** Who or what verifies the output, is that verifier independent of the generator, and does verification hold across repetitions?

**Disqualifiers:** Self-verification by the same model without independent check. One-time demonstration. Verification against a benchmark the system was optimized on.

## 4. Classification States

| State | Symbol | Condition |
|---|---|---|
| **Constructed** | ● | Component demonstrated at Tier A or B evidence, repeatably, with no disqualifier present |
| **Partial** | ◐ | Component present but bounded — limited domain, limited persistence, or degrades under repetition |
| **Claimed** | ○ | Asserted by the developer at Tier C or D evidence only, or contradicted by a disqualifier |
| **Absent** | — | Not present, or present only as stated intent |

**Repeatability requirement.** No component reaches **Constructed** on a single demonstration. A component that performs once and degrades on repetition is **Partial**. This requirement is the operational core of ACL: construction means the transformation can be performed reliably, not that it has been performed once.

## 5. Evidence Tiers

| Tier | Source |
|---|---|
| **A** | Independent reproduction by a party with no commercial interest in the result |
| **B** | Developer disclosure with reproducible method, code, or open evaluation artifacts |
| **C** | Developer disclosure without reproducible method — technical report, system card, blog post |
| **D** | Marketing material, demonstration video, executive statement, press briefing |

**Rule.** A component's state is capped by its best available evidence tier. Tier C and D evidence cannot support **Constructed** regardless of how specific or confident the claim.

Every component in a published ledger must carry both a state and a tier. A state without a tier is not an ACL result.

## 6. Audit Procedure

1. **Fix the object.** Name the exact system and version under audit. A ledger is invalid if the object shifts between components.
2. **Collect the claim set.** Record what is publicly asserted about each of the eight components, with source and date.
3. **Assign evidence tiers.** Tier each claim before assessing it, not after.
4. **Apply disqualifiers.** For each component, check the listed disqualifiers first. A disqualifier caps the state at **Claimed**.
5. **Test repeatability** where access permits. Where access does not permit, record this as an access limit — not as absence.
6. **Assign states.**
7. **Record boundary cases.** Any component whose classification was contested during audit is recorded in the ledger with its reasoning.
8. **Publish with limits.** No ledger is published without Section 10 attached.

## 7. Boundary Cases

Boundary cases are the validation surface of this protocol. A classification scheme that has not been tested against its hard cases has not been tested.

**B-01 — Memory that exists but is never read.**
A system writes persistent state but no demonstration shows retrieval altering behavior. *Resolution:* **Claimed**, not Partial. Writing is not memory; retrieval altering behavior is memory.

**B-02 — Tool use with human selection.**
A human chooses the tool; the system fills arguments and executes. *Resolution:* **Partial** at most. Selection is the audited capability, not execution.

**B-03 — Coordination that is sequential prompting.**
Multiple "agents" are the same model called in sequence with different instructions, with no conflict-resolution mechanism. *Resolution:* **Claimed**. Role labels are not coordination.

**B-04 — Authority declared in the system prompt.**
Permission boundaries exist in prompt text but nothing enforces them. *Resolution:* **Claimed**. An advisory boundary is not an authority structure.

**B-05 — Verification by the same model.**
The generator critiques its own output with no independent check. *Resolution:* **Partial** at most, and only where the critique demonstrably changes the output on measured cases.

**B-06 — Access-limited components.**
The auditor cannot test because the system is closed. *Resolution:* Record as **Claimed** with an explicit access-limit note. Inaccessibility is never recorded as **Absent** — absence is a finding, and a finding requires evidence.

**B-07 — Component present in one domain only.**
Full capability in a narrow domain, none outside it. *Resolution:* **Partial**, with the domain named. Generality is the subject of the audit and cannot be assumed from a single domain.

## 8. Reporting Format

A published ACL ledger contains, at minimum:

```
System:        [name, version]
Audit date:    [date]
Protocol:      ACL-1.0
Auditor:       [name or organization]

C1 Models          [state] [tier]  [one-line basis]
C2 Memory          [state] [tier]  [one-line basis]
C3 Tools           [state] [tier]  [one-line basis]
C4 Environments    [state] [tier]  [one-line basis]
C5 Feedback        [state] [tier]  [one-line basis]
C6 Coordination    [state] [tier]  [one-line basis]
C7 Authority       [state] [tier]  [one-line basis]
C8 Verification    [state] [tier]  [one-line basis]

Boundary cases:    [any contested classification and its reasoning]
Access limits:     [components the auditor could not test]
```

A ledger presented without access limits is incomplete. Most audits of closed systems will carry several, and stating them plainly strengthens rather than weakens the result.

## 9. Independent Use

ACL-1.0 may be applied, cited, reproduced, and published by any party without permission or notification. Derived ledgers need not be shared with the maintainer.

The only condition for calling a result an ACL audit is procedural: all eight components carry a state and a tier, boundary cases are recorded, and limits are published.

## 10. Limits of This Protocol

ACL does not measure, and must not be reported as measuring:

- **Safety, alignment, or risk.** Independent axis. Not assessed here.
- **Capability level.** A system with eight Constructed components is not thereby more capable than one with five. The ledger records construction, not performance.
- **Proximity to general intelligence.** ACL takes no position on what threshold, if any, constitutes generality. A complete ledger is not a claim that the system is or is not AGI.
- **Component quality.** Constructed means present, repeatable, and evidenced — not good.
- **Sufficiency of the component set.** The eight components reflect current system architecture as of this version. They are not asserted to be exhaustive or permanent. Additions are expected.

A ledger is a record of what was found. It is not a conclusion about what the system is.

## 11. Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-01 | Initial publication. Eight components, four states, four evidence tiers, seven boundary cases. |

Version numbers are stable references. ACL-1.0 will not be silently modified; substantive changes are issued as ACL-1.1 or later, with prior versions remaining retrievable.

## 12. Citation

> ACL-1.0 — AGI Component Ledger. AGIConstructor.com, 2026.
