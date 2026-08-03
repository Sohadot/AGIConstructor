# Source Pin — REAL-LEDGER-001

**Resolving the exact source of the locked object. Read-only inspection at the pinned tag; statuses are evidence-graded.**

Evidence grades: `VERIFIED` (confirmed against the repository/registry), `CONFIRMED`,
`UNRESOLVED`, `BLOCKED`, `PENDING RE-PIN`. Feature provenance uses:
`VERIFIED_IN_LOCKED_OBJECT` / `NOT_PRESENT_IN_LOCKED_OBJECT` / `SDK_ONLY` /
`DOCUMENTATION_ONLY_UNCONFIRMED` / `NOT_APPLICABLE`.

> **Headline finding (verified): the object was mis-specified.** Read-only inspection shows
> the GitHub tag `v1.8.0` is **Agent Canvas** — a TypeScript/Electron *control-center UI*
> that orchestrates other agents — **not** the OpenHands Python agent and **not** the
> `openhands` CLI. "1.8.0" names at least two distinct artifacts. The object requires a
> re-pin decision (see bottom). This is the object-identity trap (TF-001-A) caught before
> any classification.

## Item 1 — Organization identity: CONFIRMED

| Fact | Value | Status | Method |
|---|---|---|---|
| Repo A | `github.com/OpenHands/OpenHands` | CONFIRMED | git |
| Repo B (historical) | `github.com/All-Hands-AI/OpenHands` | CONFIRMED | git |
| Same repository? | **Yes** — identical tag SHAs (`v1.7.0`=`04462a35…`, `v1.8.0`=`c7a765d…`) in both | VERIFIED | `git ls-remote` on both |

Name difference is a provenance fact, not an operational blocker.

## Item 2 — Tag → commit: VERIFIED (with a twist)

| Fact | Value | Status | Method |
|---|---|---|---|
| Tag | `v1.8.0` | VERIFIED | `git ls-remote` |
| Tag type | **lightweight** (no `^{}` peel; points straight at a commit) | VERIFIED | `git ls-remote` |
| Commit SHA | `c7a765d900df294cbbf0f405ae26c9cbbd0fcc29` | VERIFIED | shallow checkout `git rev-parse HEAD` |
| **Repo content at that commit** | **`@openhands/agent-canvas` v1.8.0** — TS/React/Electron; `package.json name=@openhands/agent-canvas`; bin `agent-canvas`; "run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent" | VERIFIED | checked out source |
| Python packaging at that commit | **None** at repo root (no `pyproject.toml`/`setup.py`) | VERIFIED | `ls` of checkout |

**Implication:** the GitHub `v1.8.0` lineage is the **GUI orchestrator**, not the agent.

## Item 3 — PyPI lineage: operationally relevant and DISTINCT

| Fact | Value | Status | Method |
|---|---|---|---|
| Package | `openhands-ai` — the Python agent framework / `openhands` CLI | VERIFIED | PyPI JSON |
| Latest version | **1.11.0** (not 1.8.0) | VERIFIED | PyPI JSON |
| `openhands-ai` **1.8.0** upload date | **2026-06-10** (wheel + sdist) | VERIFIED | PyPI JSON |
| Requires Python | `>=3.12,<3.14` | VERIFIED | PyPI JSON |
| Sample deps | `anthropic[vertex]`, `browsergym-core==0.13.3`, `aiohttp`, `boto3`, … | VERIFIED | PyPI JSON |
| Declared repository | `github.com/OpenHands/OpenHands` | VERIFIED | PyPI JSON |
| Source commit for `openhands-ai` 1.8.0 | **UNRESOLVED** — the declared repo at tag `v1.8.0` is Agent Canvas (TS), not this Python source; the repo evidently pivoted to Agent Canvas between the 2026-06-10 PyPI cut and the later GitHub `v1.8.0` tag | UNRESOLVED | cross-check |

**Conclusion:** `openhands-ai` is the artifact behind the **CLI surface**; it is a *different
lineage* from Agent Canvas that happens to share the number "1.8.0."

## Item 4 — Docker image / digest: PENDING RE-PIN

Deferred: the correct image differs entirely for Agent Canvas vs `openhands-ai`. Resolve
after the object is re-pinned. When resolved: pin by **digest**, not tag; if no fixed
official image exists, build from the pinned source and record Dockerfile path, base-image
digests, lockfile hashes, resulting local image digest, host arch, and build timestamp.

## Item 5 — Feature provenance: PENDING RE-PIN

The CLI features cited (`openhands`, `-t/-f`, default always-confirm, `--always-approve`,
`--llm-approve` security analyzer, MCP controls, sub-agent delegation) belong to
**`openhands-ai`** (Python), **not** Agent Canvas. They must be verified against
`openhands-ai` source/`--help` at the chosen version, not against Agent Canvas or current
docs. Current grade for all: `DOCUMENTATION_ONLY_UNCONFIRMED` until the Python object is pinned.

## Item 6 — Date discrepancy: RESOLVED

The earlier "2026-06-10" was the **`openhands-ai` 1.8.0** PyPI upload date; the GitHub
`v1.8.0` (Agent Canvas) tag is a later, separate date. Two artifacts, two dates, one number
— which is itself concrete evidence for TF-001-A.

## Re-pin decision required (blocks classification)

The current lock ("OpenHands OSS Application **CLI** @ release **v1.8.0**") is inconsistent:
`v1.8.0` (GitHub) = Agent Canvas GUI orchestrator; "CLI surface" = `openhands-ai` Python.
Two coherent objects are possible:

- **Object A — Python agent via CLI:** pin `openhands-ai` at a specific version (e.g. 1.8.0
  to match the intended lineage, or 1.11.0 latest), resolve its true source commit, then
  proceed. This matches the "CLI surface" intent.
- **Object B — Agent Canvas v1.8.0:** audit the orchestrator UI itself. Very different ACL
  shape — it *runs other agents* (OpenHands/Claude Code/Codex/Gemini via ACP), so its C1/C6
  surfaces are about orchestration, not a single agent.

These are different audit objects and cannot share one ledger (binding rule). Owner decision
needed before Items 4–5 and any C1–C8 classification.
