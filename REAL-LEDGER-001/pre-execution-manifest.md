# Pre-Execution Manifest — REAL-LEDGER-001

**Everything fixed before the first paid run. Presented for owner approval. No API key entered, no paid run started, no C1–C8 classification performed.**

Status legend: `VERIFIED` (from hash-pinned artifacts/source), `SET` (chosen target),
`PENDING@BUILD` (produced when the pinned container is built — cannot be fabricated here).

## 1. Object identity (VERIFIED)

| Field | Value | Status |
|---|---|---|
| Distribution | PyPI `openhands-ai` 1.11.0 | VERIFIED (wheel `833de097…`, sdist `95bf563b…`) |
| Surface | app-server (`uvicorn openhands.app_server.app:app --host 0.0.0.0 --port 3000`) | VERIFIED |
| Pinned sub-distributions | `openhands-sdk==1.34.0` (wheel `35f7012f…`), `openhands-agent-server==1.34.0`, `openhands-tools==1.34.0` | VERIFIED (`==` pins in metadata; sdk hash recomputed) |
| Key pinned deps | `litellm==1.84.1`, `openai==2.33.0`, `docker==7.1.0`, `browsergym-core==0.13.3`, `fastmcp>=3.2,<4`, `mcp>=1.25` | VERIFIED (metadata) |
| Python | `>=3.12,<3.14` | VERIFIED |
| Agent core / LLM config location | `openhands-sdk` 1.34.0 (`openhands/sdk/llm/llm.py`) — **not** the app wheel | VERIFIED |

> Note: the agent core and LLM configuration live in `openhands-sdk` 1.34.0, a separately
> versioned distribution pinned by `openhands-ai` 1.11.0. Component evidence (C1/C3/C8) will
> largely be found there and in `openhands-tools` 1.34.0.

## 2. Model backend (VERIFIED against the object's verified-models list)

| Field | Value | Status |
|---|---|---|
| Provider | OpenAI API, **direct** (not OpenRouter, not a model proxy) | SET |
| Model | `openai/gpt-5-2025-08-07` (fixed snapshot) | SET |
| In object's `VERIFIED_OPENAI_MODELS`? | **Yes** — `gpt-5-2025-08-07` is listed | VERIFIED (openhands-sdk 1.34.0) |
| Provider response model-id capture | record `response.model` from each call | SET |

## 3. LLM / run configuration (fields VERIFIED to exist in `openhands-sdk` 1.34.0)

| Setting | Target | Field status |
|---|---|---|
| `temperature` | `0.0` | VERIFIED field (`llm.py`) |
| `reasoning_effort` | `medium` | VERIFIED field — `Literal["low","medium","high","xhigh","none"]` |
| `verbosity` | **omitted** | VERIFIED **absent** — no `verbosity` field in `openhands-sdk` 1.34.0 LLM config |
| `num_retries` | `2` | VERIFIED field (default 5) |
| `timeout` | `180` s | VERIFIED field (default 300) |
| `max_iterations` | `15` per run | VERIFIED setting (conversation settings) |
| `max_budget_per_task` | `2.00` USD | VERIFIED setting field |
| MCP servers | none | SET (explicit empty) |
| Sub-agent delegation | disabled | SET |
| Security analyzer | disabled | SET (informs C7 only; not C8) |
| Confirmation mode | always-confirm | SET |

Exact config wire-path (where each value is passed into a conversation `create_request`) to
be pinned in the harness code and included in the configuration hash.

## 4. Runtime target (SET)

```
Architecture:     amd64 / x86_64
OS:               Ubuntu 24.04 LTS
CPU:              4 vCPU
RAM:              16 GB
Free disk:        40 GB
GPU:              none
Python:           3.12.x   [PENDING@BUILD — pin exact patch]
Docker Engine:    [PENDING@BUILD — record exact version]
Network:          outbound limited to OpenAI API + package/registry pulls; recorded
```

## 5. Deployment-produced identity

- **DONE — full hashed dependency lock:** `build/openhands-ai-1.11.0.lock.txt`
  (319 packages, 3913 sha256 hashes; lock sha256 `7222056aec4d51ff24459c3fe7164daa50754b288bd2d2c34150c8f3785c01d7`; py3.12/linux-x86_64). Carries all verified pins incl. `agent-client-protocol==0.12.0` (ACP).
- **PENDING@HOST** — base Python / runner / workspace image digests (need Docker daemon; see `build-runbook.md` §4).
- **PENDING@HOST** — exact Python patch + Docker Engine versions.
- Fixture content hash fixed: `9d6c9b78…` (`fixture/manifest.json`); git commit SHA on merge.
- **Configuration hash** = SHA-256 over: {app wheel/sdist hashes + sub-dist versions + **lock hash `7222056a…`** + image digests + model id + full run config + MCP set + caps + fixture combined hash + task manifest}.

Companion docs: `build-runbook.md` (exact non-paid build/boot/health commands),
`security-review.md` (secret handling — keys held as `SecretStr`, redacting profile store,
no env dumps; telemetry + bind-address cautions), `harness/` (mock-mode plumbing skeleton).

## 6. Task suite (fixed; see `fixture/`)

Offline `mathkit` fixture, combined hash `9d6c9b78…`:
- **Task A** — deterministic bug repair (`median`, one file). Solvable, verified.
- **Task B** — bounded feature implementation (`run_length_encode`, one file). Solvable, verified.

Per task: **repeat 3×**, clean reset + new conversation each time, no mid-run steering beyond
declared confirmation responses. → **6 audit runs**.

## 7. Budgets (hard caps)

| Run type | Iterations | Budget/run | Count | Subtotal |
|---|---|---|---|---|
| Smoke (non-classifying) | 5 | 0.50 | 1 | 0.50 |
| Audit (Task A ×3, Task B ×3) | 15 | 2.00 | 6 | 12.00 |
| **Phase ceiling** | | | | **USD 12.50** |

Smoke run validates the harness only (server starts, model connects, workspace runs, events
saved, approvals work, diff/result extractable). It **never** supports a `Constructed` state.

## 8. Artifact retention (per run)

`runs/<task>/<n>/`: exact submitted task, resolved config + configuration hash, event stream
(`GET …/events`), tool-call records, workspace diff, final result, provider `response.model`
ids, token/cost metrics, timestamps, and the harness pytest result (external check).

## 9. Evidence boundary (reminder)

- Tests run by OpenHands *inside* the workspace → may bear on C3/C4/C5.
- Tests run by the *audit harness* after completion → external quality evidence only.
- **C8** counts only if a verifier independent of the generator, inside the object, confirms
  correctness repeatably. pytest passing does not grant the object C8.

## 10. Gates before any paid run (all PENDING owner approval)

1. Section 5 items produced (image digests, hashed lock, versions, fixture commit, config-hash).
2. Smoke gate passes on the pinned container (surface-contract.md §smoke gate).
3. Owner approves this manifest and the $12.50 ceiling.

Until then: **no API key, no paid call, no classification.**
