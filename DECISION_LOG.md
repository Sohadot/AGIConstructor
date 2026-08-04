# Decision Log

**The sovereign, append-only record of governance decisions for AGIConstructor.**

This is the single source of truth for *why* the asset is shaped as it is. It is
**append-only**: a decision is never edited away. When a decision changes, a **new** entry
is added with `Supersedes: DEC-XXX`, and the old entry's `Status` is set to `Superseded`
(the old text is retained). Decisions recorded here are cross-referenced to the pull
requests and commit SHAs that carried them out.

Allowed `Status` values: `Proposed` · `Ratified` · `Superseded` · `Rejected` · `Paused`.

This log records decisions only. It is **not** an ACL audit, and nothing here classifies any
system's components. ACL-1.0 remains frozen (see [ACL-2.0-CANDIDATES.md](./ACL-2.0-CANDIDATES.md)).

---

## DEC-001 — Canonical category thesis

- Date: 2026-08-03
- Status: Ratified
- Scope: Whole asset
- Decision: Adopt the thesis that **general intelligence is constructed, not discovered** —
  whatever form it takes, it will have been assembled from auditable components.
- Rationale: Replaces the unanswerable "is this AGI?" with the answerable, evidence-based
  "which components are demonstrably present, at what evidentiary standard?"
- Alternatives considered: Capability/benchmark framing (invites ranking and advocacy);
  timeline-prediction framing (unfalsifiable, ages badly).
- Consequences: Instruments derived from the thesis classify; they do not conclude.
- Evidence / references: [FOUNDATION_DOCTRINE.md](./FOUNDATION_DOCTRINE.md); PR #1.
- Reversibility: Foundational; reversal would redefine the asset.
- Supersedes: —
- Recorded by: Sohadot

## DEC-002 — AGIConstructor is the reference layer; ACL is one instrument

- Date: 2026-08-03
- Status: Ratified
- Scope: Whole asset
- Decision: Treat **AGIConstructor** as the reference layer for the AGI-construction category
  (doctrine → ontology → instruments → ledgers → registry), and **ACL-1.0** as *one* audit
  instrument within it, not the whole asset.
- Rationale: Prevents the audit tool from becoming the definition of the category.
- Alternatives considered: ACL as the entire asset (rejected — collapses the category into a
  single tool).
- Consequences: Foundation doctrine, ontology, and architecture layers added around ACL.
- Evidence / references: [ARCHITECTURE.md](./ARCHITECTURE.md), [FOUNDATION_DOCTRINE.md](./FOUNDATION_DOCTRINE.md); PR #1.
- Reversibility: Structural; reversible only by re-scoping the asset.
- Supersedes: —
- Recorded by: Sohadot

## DEC-003 — Freeze ACL-1.0; no ACL-2.0 before a real application

- Date: 2026-08-03
- Status: Ratified
- Scope: ACL protocol
- Decision: Keep **ACL-1.0 frozen and immutable**; record post-publication limitations as
  candidates only; do **not** draft ACL-2.0 until at least one real application is complete.
- Rationale: Published instruments must be stable references; breaking changes require a new
  version, not silent edits.
- Alternatives considered: Immediate ACL-2.0 to fix identified gaps (rejected — premature,
  and would jump to a protocol before the foundation is exercised).
- Consequences: Limitations tracked in ACL-2.0-CANDIDATES.md; CI drift-checks ACL-1.0.md.
- Evidence / references: [ACL-1.0.md](./ACL-1.0.md) §11, [ACL-2.0-CANDIDATES.md](./ACL-2.0-CANDIDATES.md); PR #1.
- Reversibility: A future ACL-2.0 is expected, but only after the prerequisites are met.
- Supersedes: —
- Recorded by: Sohadot

## DEC-004 — No conceptual expansion before REAL-LEDGER-001 is published

- Date: 2026-08-03
- Status: Ratified
- Scope: Roadmap
- Decision: Halt further methodology/documentation expansion until the first real ledger is
  produced, to prevent documentation from running ahead of production.
- Rationale: The next useful review must be on a near-locked object, not on more prose.
- Alternatives considered: Continue elaborating doctrine/ontology (rejected — diminishing
  returns without a real application).
- Consequences: Effort redirected to applying ACL-1.0 to a real system.
- Evidence / references: REAL-LEDGER-001 (PR #2).
- Reversibility: Lifts once REAL-LEDGER-001 reaches a published state.
- Supersedes: —
- Recorded by: Sohadot

## DEC-005 — OpenHands as the first ACL-1.0 target

- Date: 2026-08-03
- Status: Ratified
- Scope: REAL-LEDGER-001
- Decision: Select **OpenHands** as the first system for a real ACL-1.0 application.
- Rationale: A current, installable, inspectable, compositional agentic system — a strong
  proof-of-use for the protocol.
- Alternatives considered: A closed/hosted system (weaker inspectability for a first run).
- Consequences: Opened REAL-LEDGER-001 in object-definition phase.
- Evidence / references: REAL-LEDGER-001/ (PR #2).
- Reversibility: Reversible; a different first target could be chosen.
- Supersedes: —
- Recorded by: Sohadot

## DEC-006 — Audit-object identity resolves at artifact + configuration level

- Date: 2026-08-03
- Status: Ratified
- Scope: Method (via REAL-LEDGER-001)
- Decision: For compositional agentic systems, the audit object is fixed by **artifact +
  configuration** (distribution, version, artifact hashes, surface, sub-distribution
  versions, model backend, policy/tool configuration), **not** by product name and version.
- Rationale: Findings are attributable only to a resolved configuration; a product name +
  version does not uniquely identify what is audited.
- Alternatives considered: Pin by product name + version (rejected — demonstrably ambiguous).
- Consequences: Introduced the Audit Object Lock; recorded as trial finding TF-001-A
  (candidate for a future ACL version, not retrofitted into 1.0).
- Evidence / references: REAL-LEDGER-001/audit-object-lock.md, trial-findings.md (PR #2).
- Reversibility: Method-level; expected to inform ACL-2.0 design.
- Supersedes: —
- Recorded by: Sohadot

## DEC-007 — Reject GitHub `v1.8.0` (Agent Canvas); do not conflate with `openhands-ai`

- Date: 2026-08-03
- Status: Ratified
- Scope: REAL-LEDGER-001
- Decision: The GitHub tag `v1.8.0` resolves to `@openhands/agent-canvas` (a GUI
  orchestrator), which is **not** the agent/CLI; reject it as the object and do not mix its
  evidence with the PyPI `openhands-ai` lineage.
- Rationale: Verified by read-only source inspection (identical org tag SHAs; TS/Electron app
  at that tag; no Python packaging).
- Alternatives considered: Audit Agent Canvas itself (deferred — a different, orchestration-
  shaped audit; possible future REAL-LEDGER-00X).
- Consequences: Recorded as object-resolution history OR-001.
- Evidence / references: REAL-LEDGER-001/source-pin.md (OR-001) (PR #2).
- Reversibility: Agent Canvas may be a separate future ledger.
- Supersedes: —
- Recorded by: Sohadot

## DEC-008 — Pin `openhands-ai` 1.11.0, app-server surface

- Date: 2026-08-03
- Status: Ratified
- Scope: REAL-LEDGER-001
- Decision: Adopt **PyPI `openhands-ai` 1.11.0** as the object, exercised through its
  **app-server** surface (`uvicorn openhands.app_server.app:app`) in a pinned local
  containerized environment; do not chase a historical version merely to obtain a terminal
  CLI (which is absent from 1.11.0).
- Rationale: 1.11.0 is current and hash-verified; the audit target is the agent artifact, not
  a particular UI form. Rejected `openhands-ai` 1.8.0 (OR-002) — its only appeal was
  number-continuity from an artifact-name collision.
- Alternatives considered: `openhands-ai` 1.8.0 (rejected, OR-002); re-pin to a CLI-bearing
  version (rejected — surface form should not drive object choice).
- Consequences: Verified artifact hashes, sub-distribution pins (openhands-sdk/agent-server/
  tools 1.34.0), surface contract, model/config, hashed lock, fixture.
- Evidence / references: REAL-LEDGER-001/audit-object-lock.md, source-pin.md, surface-contract.md (PR #2).
- Reversibility: A material change to the object creates a new audit object, not an update.
- Supersedes: —
- Recorded by: Sohadot

## DEC-009 — Security analyzer supports C7, not C8

- Date: 2026-08-03
- Status: Ratified
- Scope: Method (via REAL-LEDGER-001)
- Decision: Treat the OpenHands security analyzer (action-risk gating pre-execution) as
  support for **C7 Authority / risk-gating**, **not** as ACL-1.0 **C8 Verification**; leave
  C8 unresolved until an independent output-correctness mechanism is identified and tested.
- Rationale: C8 requires independent confirmation of output correctness, repeatably; risk
  classification is not verification.
- Alternatives considered: Count the analyzer as C8 (rejected — conflates risk-gating with
  correctness verification).
- Consequences: Corrected the earlier draft; C8 remains unresolved in the pre-execution record.
- Evidence / references: REAL-LEDGER-001/trial-findings.md (TF-001-E) (PR #2).
- Reversibility: C8 status to be established at classification time.
- Supersedes: —
- Recorded by: Sohadot

## DEC-010 — No API key or paid model before a Docker host and separate authorization

- Date: 2026-08-03
- Status: Ratified
- Scope: REAL-LEDGER-001 execution
- Decision: Do not create, store, or use an OpenAI API key, and make no live/paid model
  request, until a suitable Docker host is available, the non-paid build/health checks pass,
  and the owner separately authorizes a single smoke run with a disposable, project-scoped key.
- Rationale: API keys are secrets carrying financial and exfiltration risk; a live run adds
  nothing to the reference structure and is unnecessary until warranted.
- Alternatives considered: Run immediately with a key (rejected — premature, avoidable risk/cost).
- Consequences: Non-paid build completed (hashed lock, security review, runbook, harness);
  execution gates split into pre-smoke and pre-audit.
- Evidence / references: REAL-LEDGER-001/security-review.md, build-runbook.md, pre-execution-manifest.md (PR #2).
- Reversibility: Lifts upon a Docker host + explicit owner authorization.
- Supersedes: —
- Recorded by: Sohadot

## DEC-011 — Freeze PR #2 as a non-paid pre-execution record

- Date: 2026-08-03
- Status: Ratified
- Scope: REAL-LEDGER-001
- Decision: Freeze **PR #2** (Sohadot/AGIConstructor#2) as a paused, non-paid pre-execution
  record — kept open and draft, not merged, not closed — at frozen head
  `d60e8dbcb0811811dd6b003b49b15c0a72ef2df4`.
- Rationale: Everything provable without a Docker host or a paid model has been extracted and
  verified; continuing would be documentation ahead of production.
- Alternatives considered: Merge now (rejected — incomplete object, no execution); close
  (rejected — it is the live retention point for resumed work).
- Consequences: Work resumes from build-runbook.md when a Docker host is available.
- Evidence / references: PR #2 @ `d60e8db…`; REAL-LEDGER-001/README.md (status: PAUSED).
- Reversibility: Resumable at the frozen head; superseded only by a later resumption decision.
- Supersedes: —
- Recorded by: Sohadot
