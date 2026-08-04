# Deployment Plan — REAL-LEDGER-001

**Object: `openhands-ai` 1.11.0 (PyPI), pinned local containerized execution. No paid run, no credentials, no classification yet.**

Installs the hash-verified PyPI artifact into a pinned container and prepares a reproducible
run. Guiding rule: **use documented defaults**; do not enable MCP servers, sub-agent
delegation, or extra policies merely to make components appear present.

## 1. Install identity (from `source-pin.md`, VERIFIED)

```
Distribution:    openhands-ai == 1.11.0
Wheel:           openhands_ai-1.11.0-py3-none-any.whl
Wheel SHA-256:   833de097150d498ffc7e175869df4723aec4a6b3c0be27545ca37089e6452c8f
Sdist:           openhands_ai-1.11.0.tar.gz
Sdist SHA-256:   95bf563bd3d34876ea6284e28321c034fa44491a46b21e32bf5cc54d118bbf78
Python:          >=3.12,<3.14   (pin exact patch at build)
Install with hash pinning, e.g.:
  uv pip install "openhands-ai==1.11.0" --require-hashes   # or pip with a hashed lock
```

## 2. Runtime and images

```
Runtime:            local Docker
Base container:     [SET — python 3.12/3.13 slim; pin by digest]
Runner image:       [SET — openhands runtime/sandbox image; pin by DIGEST, not tag]
Workspace image:    [SET — if distinct]
Host architecture:  [SET — amd64 | arm64]
```
The runtime/sandbox image reference is defined inside the package (docker==7.1.0 is a
dependency); resolve its exact default image and pin by digest.

## 3. Invocation surface (RESOLVED → app-server; VERIFIED)

```
Entry point:        uvicorn openhands.app_server.app:app --host 0.0.0.0 --port 3000
                    # VERIFIED. openhands/server/__main__.py is deprecated and forwards here.
Surface:            app-server (FastAPI, /api/v1). Full contract: surface-contract.md.
NOTE:               openhands-ai 1.11.0 ships NO `openhands` console-script CLI, and the
                    documented --llm-approve / --always-approve flags are NOT present in
                    this artifact. The audit binds to the app-server surface, driven by a
                    fixed programmatic harness (see surface-contract.md, harness boundary).
```

## 4. Configuration (documented defaults; explicit, not maximal)

```
Confirmation policy:   always-confirm
Security analyzer:     disabled              # informs C7 risk-gating, NOT C8
MCP servers:           NONE (explicit empty set)
Sub-agent delegation:  DISABLED
Model backend:         openai/gpt-5-2025-08-07 (OpenAI direct)  # VERIFIED in object's list
                       temp=0.0, reasoning_effort=medium, num_retries=2, timeout=180s
Iteration/budget caps: max_iterations=15, max_budget_per_task=USD 2.00
```
See [`pre-execution-manifest.md`](./pre-execution-manifest.md) for the full consolidated
manifest (runtime target, budgets, task suite, gates) and
[`surface-contract.md`](./surface-contract.md) for the app-server surface.

## 5. Task suite, repetition, artifacts

```
Task suite:      fixture/ (mathkit, combined hash 9d6c9b78…) — Task A bug repair,
                 Task B feature impl; offline, deterministic, verified solvable
Repeat count:    3 per task (6 audit runs) + 1 non-classifying smoke run
Config hash:     SHA-256 over resolved config (image digests + dep-lock hash + model id +
                 MCP set + caps + task manifest)
Artifacts:       exact commands, resolved config, dep lock w/ hashes, per-run event logs,
                 tool-call records, outputs, timestamps
```

## 6. Pre-execution gates (all must pass before any run)

1. Surface decision resolved (app-server vs terminal-CLI re-pin).
2. Container base + runner/workspace image digests pinned; dep lock with hashes produced.
3. Cost + hardware documented; model chosen and justified.
4. Credentials handling defined (no keys committed; secrets never enter the ledger).
5. Task suite fixed and public; repeat count set; config-hash procedure fixed.

Until every gate passes: **no paid execution, no API key entered, no C1–C8 classification.**

## 7. Blockers carried forward

- Surface definition for 1.11.0 (app-server vs CLI re-pin) — owner.
- Runner/workspace image digests; full hashed dependency lock — deployment-produced.
- Model / cost / hardware decision — owner.
- Git commit mapping for `openhands-ai` 1.11.0 — provenance only, not blocking.
