# Worked Example — Illustrative ACL-1.0 Ledger

> ⚠️ **ILLUSTRATIVE AND FICTIONAL.** "ORCHESTRA-7" is not a real system. Every finding, source, and date below is invented to demonstrate how an ACL-1.0 ledger is filled in — including how disqualifiers, boundary cases, and access limits are recorded. **No claim is made about any real product, company, or system.** Do not cite this as an audit of anything.

This example accompanies the machine-readable version at [`example-ledger.json`](./example-ledger.json), which validates against [`schema/agicl-1.0.schema.json`](../schema/agicl-1.0.schema.json).

---

## Ledger

```
System:        ORCHESTRA-7 (fictional), v3.2
Audit date:    2026-08-03
Protocol:      ACL-1.0
Auditor:       Illustrative Example (not a real auditor)
```

### Source register (all fictional)

| ID | Title | Date | Type |
|---|---|---|---|
| S-01 | ORCHESTRA-7 System Card v3.2 | 2026-06-10 | Developer disclosure |
| S-02 | Independent Reproduction Report: Memory & Environments | 2026-07-04 | Independent reproduction |
| S-03 | Vendor Demonstration Video: "ORCHESTRA-7 Multi-Agent" | 2026-06-21 | Marketing |
| S-04 | ORCHESTRA-7 Tool Orchestration Config (published repo) | 2026-06-15 | Developer disclosure, reproducible |
| S-05 | Vendor Routing Description (secondary note) | 2026-05-30 | Developer disclosure |

### Findings

| # | Component | State | Tier | Src | Basis |
|---|---|---|---|---|---|
| C1 | Models | ○ Claimed | C | S-01, S-05 | System card calls it a "unified model," but a routing description presents ensemble routing as single-model generality — **disqualifier**; capped at Claimed. |
| C2 | Memory | ● Constructed | A | S-02 | Independent reproduction: information from one session demonstrably alters behavior in a later, separate session without re-supply; holds across repetition. |
| C3 | Tools | ◐ Partial | B | S-04, S-03 | Tool composition is reproducible from published config, but in every demonstration a human selects the tool and the system fills arguments (**B-02**). |
| C4 | Environments | — Absent | A | S-02 | Independent testing shows stateless request-response; no environment whose state the system's own prior actions changed, despite "persistent world" marketing. |
| C5 | Feedback | ○ Claimed | C | S-01 | Disclosure describes training-time feedback presented as runtime adaptation — **disqualifier**. No measured runtime effect shown. |
| C6 | Coordination | ○ Claimed | D | S-03 | "Multi-agent" is the same model prompted in sequence with role labels; no conflict-resolution mechanism (**B-03**). Evidence is a demo video only. |
| C7 | Authority | ◐ Partial | B | S-04 | A permission boundary is enforced at the execution layer for high-risk actions (reproducible from disclosed config), but is advisory-only for the rest. |
| C8 | Verification | ○ Claimed | C | S-01 | Vendor states an "independent verifier," but it is closed and its independence from the generator cannot be tested (**B-06**, access-limited). |

**Legend:** ● Constructed · ◐ Partial · ○ Claimed · — Absent · Tiers A–D per ACL-1.0 §5.

Tier assignment tracks the source type: independent reproduction (S-02) supports Tier A; reproducible developer disclosure (S-04) supports Tier B; non-reproducible disclosure (S-01, S-05) caps at Tier C; marketing/demo (S-03) caps at Tier D.

## Boundary cases

- **C3 — B-02 (tool use with human selection).** Human chooses the tool; the system fills arguments and executes. Selection is the audited capability, so the finding is capped at **Partial**, not Constructed.
- **C6 — B-03 (coordination that is sequential prompting).** Role-labeled sequential calls to one model with no conflict-resolution path. Resolved to **Claimed**; role labels are not coordination.
- **C8 — B-06 (access-limited component).** The verifier is closed; independence cannot be confirmed. Recorded as **Claimed** with an explicit access-limit note — never **Absent**, because absence is a finding and a finding requires evidence.

## Access limits

- **C1 (Models).** Internal composition is not inspectable; the ensemble-vs-unified question rests on a secondary description, not direct inspection.
- **C8 (Verification).** The verifier is a closed component; the auditor could not test whether it is independent of the generator or whether verification holds across repetitions.

## Notes on reading this ledger

- **This is a construction record, not a verdict.** ORCHESTRA-7's mix of states is not a score, a ranking, or a statement that it is or is not AGI (ACL-1.0 §10).
- **Constructed appears once (C2), at Tier A.** Under ACL-1.0 §5, Tier C/D evidence cannot support Constructed — which is why C1, C5, and C8 rest at Claimed regardless of how confident the underlying claim sounds.
- **Absent (C4) still carries evidence (Tier A).** Absence was *found* by independent testing, not assumed from silence.
