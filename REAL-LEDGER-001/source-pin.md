# Source Pin — REAL-LEDGER-001

**Object A: `openhands-ai` 1.11.0. PyPI artifacts are the primary release identity.**

Evidence grades: `VERIFIED`, `CONFIRMED`, `UNRESOLVED`, `PENDING` (deployment-produced).
Feature provenance: `VERIFIED_IN_LOCKED_OBJECT` / `NOT_PRESENT_IN_LOCKED_OBJECT` /
`SDK_ONLY` / `DOCUMENTATION_ONLY_UNCONFIRMED` / `NOT_APPLICABLE`.

## Object-resolution history

**OR-001 — GitHub tag `v1.8.0` + "CLI surface" (rejected).**
Initial candidate. Rejected because the tag resolves to `@openhands/agent-canvas` (a
TypeScript/Electron GUI orchestrator), while the CLI/agent belongs to the independently
distributed PyPI package `openhands-ai`. No state or tier was ever assigned. Superseded.

**OR-002 — `openhands-ai` 1.8.0 (not adopted).**
Considered only for number-continuity with OR-001. Rejected: no prior run or published
ledger requires 1.8.0, and the 1.8.0 choice originated from an artifact-name collision, not
provenance. Never classified.

**OR-003 — `openhands-ai` 1.11.0 (adopted).**
Current object. Latest at lock time; hash-verified PyPI artifacts. See lock below.

## Release identity (primary) — VERIFIED

| Item | Value | Status |
|---|---|---|
| Ecosystem / distribution | PyPI / `openhands-ai` | VERIFIED |
| Version | 1.11.0 | VERIFIED |
| Wheel | `openhands_ai-1.11.0-py3-none-any.whl` | VERIFIED (downloaded) |
| Wheel SHA-256 | `833de097150d498ffc7e175869df4723aec4a6b3c0be27545ca37089e6452c8f` | VERIFIED (recomputed = PyPI) |
| Sdist | `openhands_ai-1.11.0.tar.gz` | VERIFIED (downloaded) |
| Sdist SHA-256 | `95bf563bd3d34876ea6284e28321c034fa44491a46b21e32bf5cc54d118bbf78` | VERIFIED (recomputed = PyPI) |
| Upload date | 2026-07-09 | VERIFIED |
| Python requirement | `>=3.12,<3.14` | VERIFIED (pyproject + metadata) |
| Declared dependencies | 85 (docker==7.1.0, browsergym-core==0.13.3, anthropic[vertex], fastmcp<4,>=3.2, …) | VERIFIED (metadata) |
| Git commit mapping | **UNRESOLVED** — no `v1.11.0` tag in the flagship repo (now Agent Canvas); Python source location TBD. Not a blocker (artifact is hash-pinned). | UNRESOLVED |

## Org / repo identity — CONFIRMED

`All-Hands-AI/OpenHands` and `OpenHands/OpenHands` return identical tag SHAs
(`v1.7.0`=`04462a35…`, `v1.8.0`=`c7a765d…`) → same repository (rename). `openhands-ai`
declares this repo as its homepage, but the repo's tagged content is Agent Canvas (TS), so
the declared repo does not directly host the `openhands-ai` Python source at a matching tag.

## Pinned sub-distributions and model — VERIFIED

`openhands-ai` 1.11.0 pins the agent core and tools as separate distributions (`==`):

| Distribution | Version | Note |
|---|---|---|
| `openhands-sdk` | 1.34.0 | agent core + LLM config + `VERIFIED_MODELS`; wheel sha256 `35f7012f1e09c9edd6c5be3797daea4ed9f23751b2b802107ce2f3b069aef85b` (recomputed) |
| `openhands-agent-server` | 1.34.0 | agent server |
| `openhands-tools` | 1.34.0 | tools |
| `litellm` | 1.84.1 | LLM gateway |
| `openai` | 2.33.0 | OpenAI client |
| `docker` | 7.1.0 | sandbox runtime |

**Object identity spans multiple distributions** — component evidence (C1/C3/C8) largely
lives in `openhands-sdk`/`openhands-tools` 1.34.0, not the app wheel. Reinforces TF-001-A.

**Model verification (against `openhands-sdk` 1.34.0):**
- `gpt-5-2025-08-07` **is** in `VERIFIED_OPENAI_MODELS` → `VERIFIED_IN_LOCKED_OBJECT`.
  (So is `gpt-5-mini-2025-08-07`.)
- LLM config fields present: `temperature`, `num_retries` (default 5), `timeout` (default
  300), `reasoning_effort` (`low|medium|high|xhigh|none`). `verbosity` is
  `NOT_PRESENT_IN_LOCKED_OBJECT` — omitted from the run config.

## Feature / surface provenance (against the installed 1.11.0 artifact)

| Feature | Grade | Evidence |
|---|---|---|
| `openhands` **console-script CLI** | `NOT_PRESENT_IN_LOCKED_OBJECT` | no `entry_points.txt`; `project.scripts` empty; no `cli` module |
| App-server entry (`uvicorn openhands.app_server.app:app --port 3000`) | `VERIFIED_IN_LOCKED_OBJECT` | `openhands/app_server/app.py`; `openhands/server/__main__.py` is deprecated and forwards here |
| Endpoints (`/api/v1/app-conversations`, `…/send-message`, `…/events`, `…/pending-messages`, `/alive`,`/ready`) | `VERIFIED_IN_LOCKED_OBJECT` | FastAPI routers in `openhands/app_server/` — see surface-contract.md |
| `--llm-approve` flag | `NOT_PRESENT_IN_LOCKED_OBJECT` | 0 files in wheel source |
| `--always-approve` flag | `NOT_PRESENT_IN_LOCKED_OBJECT` | 0 files in wheel source |
| Confirmation mechanism | `VERIFIED_IN_LOCKED_OBJECT` (mechanism) | `confirmation` in 5 files; `ConfirmationMode` under `app_server` |
| Security analyzer mechanism | `VERIFIED_IN_LOCKED_OBJECT` (mechanism) | `security_analyzer` in 3 files; `SecurityAnalyzer` under `app_server` |
| MCP support | `VERIFIED_IN_LOCKED_OBJECT` (mechanism) | MCP references in 5 files; `fastmcp` dependency |
| Sub-agent delegation | `VERIFIED_IN_LOCKED_OBJECT` (mechanism) | delegation references in 3 files |
| Model backend via LiteLLM | `DOCUMENTATION_ONLY_UNCONFIRMED` | confirm against source at deployment |

**Key provenance result:** the *mechanisms* (confirmation, security analysis, MCP,
delegation) exist in 1.11.0, but the *documented terminal-CLI flag surface* does not. The
docs' CLI mode describes a different version/distribution. This is exactly the mismatch the
evidence-provenance discipline exists to catch, and it is a **verified** finding, not a guess.

## Deployment-produced items (PENDING, not blockers to pinning identity)

- Full dependency lock with hashes (`uv pip compile` / `pip freeze` at install).
- Runner + workspace container image digests (pin by digest).
- Exact Python patch version.
- Model backend choice (owner + cost/hardware).

Identity is already pinned by the two VERIFIED artifact hashes; the above are produced when
the pinned environment is built.
