# Audit Object Lock — REAL-LEDGER-001

**The exact object this audit binds to. A ledger is invalid if the object shifts.**

Object (human name): **OpenHands Python Agent — `openhands-ai` 1.11.0**
Formal: *PyPI distribution `openhands-ai` version 1.11.0, executed in a pinned local
containerized environment.*

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
Invocation:            python -m openhands.server  # VERIFIED entry (app-server module)
                       # NOTE: no `openhands` console script exists in this artifact
                       # (project.scripts is empty) — see surface caveat below
Dependency lock:       [PRODUCE at install — full resolution with hashes (uv/pip); 85
                       declared deps incl. docker==7.1.0, browsergym-core==0.13.3,
                       anthropic[vertex], fastmcp<4,>=3.2]
Runner image digest:   [SET at deployment — pin by digest]
Workspace image digest:[SET at deployment — pin by digest if distinct]
Model backend:         [UNSET — injected via LiteLLM; provider/model/version]
Confirmation policy:   [SET at deployment — default per artifact, verified in source]
Security analyzer:     [SET at deployment — present as mechanism under app_server]
MCP servers:           NONE (explicit) unless part of a documented default
Sub-agent delegation:  DISABLED unless a documented default of this artifact
Iteration/budget caps: [SET explicit values]
Configuration hash:    [SHA-256 over the full resolved configuration]
Git commit mapping:    UNRESOLVED — no v1.11.0 tag in the flagship repo (which now holds
                       Agent Canvas); openhands-ai Python source location TBD. Not a
                       blocker: identity rests on the hash-verified PyPI artifacts.
Audit window:          [SET at deployment]
```

### Surface caveat (verified, must be resolved before classification)

The intended **terminal "CLI surface"** (`openhands -t …`, `--llm-approve`,
`--always-approve` per current docs) is **NOT present in `openhands-ai` 1.11.0**: those flag
strings appear in zero files and there is no `openhands` console script. 1.11.0 is
**app-server-oriented** (`python -m openhands.server`; confirmation/security under
`openhands/app_server/…`). The surface for this object is therefore the app-server /
programmatic interface, **not** the documented terminal CLI. Whether to (a) audit the
app-server surface of 1.11.0, or (b) re-pin to whichever `openhands-ai` version actually
ships the terminal CLI, is an owner decision — recorded, not silently resolved.

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
