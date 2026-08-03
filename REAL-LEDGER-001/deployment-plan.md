# Deployment Plan — REAL-LEDGER-001

**What will be run, exactly, before any classification. No paid execution, no credentials, no final model chosen yet.**

Target object: **OpenHands OSS Application · CLI surface · local Docker runtime · release
`v1.8.0`** (pending `source-pin.md` blockers). The guiding rule: **use the documented
default configuration wherever possible.** Optional MCP servers, sub-agent delegation, and
extra security policies are **not** enabled merely to make components appear present.

## 1. Runtime and image

```
Runtime:            local Docker
Image:              [BLOCKED — resolve official image name from source-pin.md]
Image digest:       [BLOCKED — pin by sha256 digest, not tag]
Host architecture:  [SET at deployment: amd64 | arm64]
Network:            [default; record egress posture]
```

## 2. CLI invocation (surface = CLI)

```
Launch:             openhands            # interactive CLI
Task modes:         openhands -t "<task>"   |   openhands -f <taskfile>
Config access:      Ctrl+P (LLM config, MCP palette)
```

## 3. Configuration (documented defaults; explicit, not maximal)

```
Confirmation policy:   DEFAULT = always-confirm   # do NOT pass --always-approve or --llm-approve
                       (a second, separate run MAY vary this to observe the C7 surface —
                        recorded as a distinct object, per the binding rule)
Security analyzer:     off by default (only active via --llm-approve)  # informs C7, not C8
MCP servers:           NONE                # explicit empty set, not left open
Sub-agent delegation:  DISABLED unless proven to be a documented default of this object
Model backend:         [CANDIDATES only, no key: e.g. a hosted model or a local/OSS model]
                       # final choice deferred until cost/hardware requirements are documented
Iteration/budget caps: [SET explicit values before any run]
```

Rationale: enabling MCP or delegation "to score components" would fabricate presence. The
first ledger records the **default** object. Configuration variants are separate objects
(`audit-object-lock.md` binding rule).

## 4. Task suite and repetition

```
Task suite:      [DEFINE a small, fixed, public, reproducible set — e.g. bounded coding
                  tasks on a pinned throwaway repo; no private data, no secrets]
Repeat count:    [>= the ACL-1.0 repeatability requirement — a component reaches
                  Constructed only across repetition, never a single demonstration]
```

## 5. Configuration hash and artifacts

```
Configuration hash:  SHA-256 over the full resolved config (image digest + CLI flags +
                     model id + MCP set + caps + task suite manifest)
Artifacts to save:   exact commands, resolved config JSON, per-run transcripts/event logs,
                     tool-call records, outputs, timestamps, and the config hash
```

## 6. Explicit pre-execution gates (must all pass before running)

1. `source-pin.md` blockers resolved to `VERIFIED` (commit SHA, image digest, feature provenance).
2. Cost and hardware requirements documented; a model chosen and justified.
3. Credentials handling defined (no keys committed; secrets never enter the ledger).
4. Task suite fixed and public; repeat count set.
5. Configuration hash procedure fixed.

Until every gate passes: **no paid execution, no API key entered, no C1–C8 classification.**

## 7. Known blockers carried forward

- Docker image name + digest (from `source-pin.md`).
- v1.8.0 commit SHA confirmation.
- App-tag ↔ PyPI-`openhands-ai` reconciliation.
- Feature provenance for CLI vs SDK-only.
- Model/cost/hardware decision (owner input needed).
