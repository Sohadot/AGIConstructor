# REAL-LEDGER-001 — OpenHands (object-definition phase)

**The first attempt to apply ACL-1.0 to a real system. Not yet a completed ledger.**

Status: **OBJECT-DEFINITION PHASE** — no component has been classified.
Opened: 2026-08-03
Auditor: Sohadot (in progress)
Protocol: ACL-1.0 (frozen; not modified by this ledger)

---

## What this is

This directory is a *real* ACL-1.0 audit in progress, targeting **OpenHands**. It is
deliberately incomplete: it contains **no component states, no evidence tiers, and no
capability claims**. Under ACL-1.0 §6, an audit begins by *fixing the object*, and the
first pass revealed that "the object" for a compositional agentic system is not settled
by a product name and version number. That discovery is recorded before any
classification is attempted.

**Nothing here should be read as an assessment of OpenHands.** No finding about what
OpenHands can or cannot do has been made. This is the setup and methodology record only.

## Contents

- [`audit-object-lock.md`](./audit-object-lock.md) — the exact deployment configuration
  the audit will bind to. Deep-pin fields (commit SHA, container digest, model backend,
  configuration hash) are **unset**: they require an actual pinned deployment, which has
  not been performed. A real classification pass cannot begin until this file is complete.
- [`trial-findings.md`](./trial-findings.md) — methodological findings that emerged while
  fixing the object, reorganized under two central discoveries. These are *trial findings*
  about applying ACL-1.0, **not** protocol changes and **not** component results. Whether
  any warrants a future protocol change is deferred to a package review.
- [`source-pin.md`](./source-pin.md) — resolving the exact source (tag, commit, image
  digest, sub-component versions, feature provenance); resolved-where-verifiable, blockers
  stated.
- [`deployment-plan.md`](./deployment-plan.md) — the exact pre-execution plan (runtime,
  CLI, default configuration, task suite, gates). No paid execution or credentials yet.

## Rules for this ledger

1. **ACL-1.0 is not modified.** Limitations surfaced here are recorded as trial findings,
   not retrofitted into the protocol, and not opened as ACL-2.0 work mid-trial.
2. **No fabricated evidence.** No component receives a state or tier until it rests on
   real, version-matched evidence against the locked object.
3. **Object identity is load-bearing.** Any material change to the locked object (see
   `audit-object-lock.md`) creates a *new* audit object and a new ledger — never a silent
   update to this one.

## Sources consulted (object definition)

- OpenHands — Enterprise vs. Open Source, docs.openhands.dev/enterprise/enterprise-vs-oss (accessed 2026-08-03)
- OpenHands — Security & Action Confirmation (SDK), docs.openhands.dev/sdk/guides/security (accessed 2026-08-03)
- OpenHands release listing, PyPI `openhands-ai` / GitHub releases: 1.8.0 dated 2026-06-10 (accessed 2026-08-03)
- OpenHands SDK paper, arXiv:2511.03690 (event-stream architecture, auxiliary services) (accessed 2026-08-03)
