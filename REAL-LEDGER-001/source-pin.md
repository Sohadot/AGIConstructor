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

## Feature / surface provenance (against the installed 1.11.0 artifact)

| Feature | Grade | Evidence |
|---|---|---|
| `openhands` **console-script CLI** | `NOT_PRESENT_IN_LOCKED_OBJECT` | no `entry_points.txt`; `project.scripts` empty; no `cli` module |
| App-server entry (`python -m openhands.server`) | `VERIFIED_IN_LOCKED_OBJECT` | `openhands/server/__main__.py` present |
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
