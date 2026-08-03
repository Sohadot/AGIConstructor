# Audit Object Lock — REAL-LEDGER-001

**The exact object this audit binds to. A ledger is invalid if the object shifts.**

Object (human name): **OpenHands Python Agent App Server — `openhands-ai` 1.11.0**
Formal: *PyPI distribution `openhands-ai` version 1.11.0, **app-server surface**, executed
in a pinned local containerized environment and exercised through a fixed programmatic audit
harness.* Surface details: [`surface-contract.md`](./surface-contract.md).

This extends ACL-1.0 §6.1 ("Fix the object") for a compositional agentic system. The
**published PyPI artifacts (wheel/sdist + SHA-256) are the primary release identity.** A
matching git commit is desirable provenance but is **not** required to run a hash-verified
official artifact. `1.11.0` was current at lock time and remains the immutable audited
version regardless of later releases — "latest" is a timestamped note, not the identity.

## Lock

```
Package ecosystem:     PyPI
Distribution:          openhands-ai
Version:               1.11.0                      # current at lock time; immutable hereafter
Wheel filename:        openhands_ai-1.11.0-py3-none-any.whl
Wheel SHA-256:         833de097150d498ffc7e175869df4723aec4a6b3c0be27545ca37089e6452c8f   # VERIFIED
Sdist filename:        openhands_ai-1.11.0.tar.gz
Sdist SHA-256:         95bf563bd3d34876ea6284e28321c034fa44491a46b21e32bf5cc54d118bbf78   # VERIFIED
Artifact upload date:  2026-07-09                  # PyPI (VERIFIED)
Python requirement:    >=3.12,<3.14                # VERIFIED (pyproject/metadata)
Python patch version:  [SET at deployment — exact x.y.z used]
Invocation:            uvicorn openhands.app_server.app:app --host 0.0.0.0 --port 3000
                       # VERIFIED. openhands/server/__main__.py is DEPRECATED and forwards
                       # here. No `openhands` console script exists (project.scripts empty).
                       # Surface = app-server; see surface-contract.md.
Pinned sub-distributions: openhands-sdk==1.34.0 (agent core + LLM config; wheel
                       35f7012f1e09c9edd6c5be3797daea4ed9f23751b2b802107ce2f3b069aef85b),
                       openhands-agent-server==1.34.0, openhands-tools==1.34.0,
                       litellm==1.84.1, openai==2.33.0, docker==7.1.0   # VERIFIED (== pins)
Dependency lock:       [PRODUCE at install — full resolution with hashes (uv/pip); 85
                       declared deps]
Runner image digest:   [SET at deployment — pin by digest]
Workspace image digest:[SET at deployment — pin by digest if distinct]
Model backend:         openai/gpt-5-2025-08-07  (OpenAI direct; VERIFIED in the object's
                       VERIFIED_OPENAI_MODELS). temp=0.0, reasoning_effort=medium,
                       num_retries=2, timeout=180s  # verbosity omitted (absent in sdk 1.34.0)
Confirmation policy:   always-confirm
Security analyzer:     disabled   # informs C7 risk-gating only, not C8
MCP servers:           none (explicit)
Sub-agent delegation:  disabled
Iteration/budget caps: max_iterations=15, max_budget_per_task=USD 2.00   # VERIFIED fields
Configuration hash:    [SHA-256 over the full resolved configuration]
Git commit mapping:    UNRESOLVED — no v1.11.0 tag in the flagship repo (which now holds
                       Agent Canvas); openhands-ai Python source location TBD. Not a
                       blocker: identity rests on the hash-verified PyPI artifacts.
Audit window:          [SET at deployment]
```

### Surface resolution (RESOLVED → app-server)

The documented terminal **"CLI surface"** (`openhands -t …`, `--llm-approve`,
`--always-approve`) is **NOT present in `openhands-ai` 1.11.0**: those flag strings appear in
zero files and there is no `openhands` console script (`project.scripts` empty). Resolution:
REAL-LEDGER-001 binds to the artifact's **verified app-server surface**
(`uvicorn openhands.app_server.app:app`), not a documented interface projected onto the
installed object. The confirmation, security-analyzer, MCP, and delegation mechanisms are
present under `openhands/app_server/…`. Full surface in
[`surface-contract.md`](./surface-contract.md); rationale in `source-pin.md` →
object-resolution history.

## Explicitly excluded from this object

- `@openhands/agent-canvas` (the GUI orchestrator; GitHub tag `v1.8.0`)
- OpenHands Cloud, Cloud Self-hosted, Enterprise
- SDK-only capabilities not present in the installed distribution
- Any `openhands-ai` version other than 1.11.0
- Unpinned dependencies
- Undocumented plugins or MCP servers
- Any model backend or policy configuration not listed above

## Binding rule

> Any material change to the object defined above creates a **new audit object**, not an
> update to REAL-LEDGER-001. A new object requires a new ledger.

Rationale: the same OpenHands release can present different C1 (inference substrate), C3
(tools), C4 (environment), C6 (coordination), and C7 (authority) surfaces depending on the
resolved configuration. Whether the locked object contains a qualifying **C8** verification
mechanism remains **unresolved** and must be established separately: the security analyzer
gates action risk (C7), it does not verify output correctness.
