# REAL-LEDGER-001 — OpenHands Python Agent App Server (`openhands-ai` 1.11.0)

**The first attempt to apply ACL-1.0 to a real system. Not yet a completed ledger.**

Object: **`openhands-ai` 1.11.0** (PyPI), **app-server surface**
(`uvicorn openhands.app_server.app:app`), pinned local containerized execution, exercised
through a fixed programmatic audit harness. See [`surface-contract.md`](./surface-contract.md).
Status: **OBJECT-DEFINITION / DEPLOYMENT-PLANNING PHASE** — no component has been classified.
Opened: 2026-08-03
Auditor: Sohadot (in progress)
Protocol: ACL-1.0 (frozen; not modified by this ledger)

> The object was re-pinned during source resolution: the GitHub tag `v1.8.0` proved to be
> `@openhands/agent-canvas` (a GUI orchestrator), while the agent/CLI is the independently
> distributed PyPI package `openhands-ai`. See `source-pin.md` → Object-resolution history.
> This collision is REAL-LEDGER-001's first substantive result (TF-001-A).

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
- [`surface-contract.md`](./surface-contract.md) — the app-server surface resolved from the
  wheel source (server invocation, endpoints, confirmation wiring), the object-vs-harness
  boundary, and the smoke gate.
- [`deployment-plan.md`](./deployment-plan.md) — the exact pre-execution plan (runtime,
  app-server invocation, default configuration, task suite, gates). No paid execution or
  credentials yet.
- [`pre-execution-manifest.md`](./pre-execution-manifest.md) — **the consolidated manifest
  for owner approval**: verified object + sub-distributions, model (`gpt-5-2025-08-07`),
  verified run config, runtime target, budgets ($12.50 ceiling), and gates.
- [`fixture/`](./fixture/) — the fixed offline `mathkit` task surface (two bounded tasks,
  combined hash `9d6c9b78…`; baseline + solvability verified).

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
