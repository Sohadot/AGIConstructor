# Source Pin — REAL-LEDGER-001

**Resolving the exact source of the locked object. Resolved-where-verifiable; blockers stated plainly.**

Object: **OpenHands OSS Application, CLI surface, release 1.8.0** (see `audit-object-lock.md`).
This file separates what is *verified from public sources* from what *requires a pinned
deployment or repository access to confirm*. A value is not treated as pinned until its
status is `VERIFIED`.

## Application release

| Item | Value | Status | Source / method |
|---|---|---|---|
| Distribution | OpenHands OSS (MIT) | VERIFIED | enterprise-vs-oss docs |
| Canonical repo | `OpenHands/OpenHands` (formerly All-Hands-AI/OpenHands) | LIKELY — confirm org rename | GitHub URLs; DeepWiki still uses All-Hands-AI |
| Release tag | `v1.8.0` | LIKELY | GitHub releases page |
| Release commit SHA | `c7a765d900df294cbbf0f405ae26c9cbbd0fcc29` | UNVERIFIED — confirm with `git rev-list -n1 v1.8.0` on the pinned checkout | GitHub releases page (single-source) |
| Release date | **DISCREPANCY** — GitHub releases page indicates late-July 2026; an earlier PyPI-derived search indicated 2026-06-10 | UNRESOLVED | reconcile GitHub tag date vs PyPI `openhands-ai` upload date |

## Sub-component versions (separately versioned — this is TF-001-A in concrete form)

The 1.8.0 application release bundles independently-versioned components. These are part of
the object identity and must be pinned:

| Component | Version (per release notes) | Status |
|---|---|---|
| agent-server | 1.39.1 | UNVERIFIED — confirm at checkout |
| automation | 1.5.0 | UNVERIFIED |
| typescript-client | 1.36.1 | UNVERIFIED |
| PyPI `openhands-ai` | version mapping to app 1.8.0 | UNRESOLVED — `openhands-ai` lineage ≠ app tag; must be reconciled |

> **Provenance caution (TF-001-A / evidence-provenance discipline).** "OpenHands 1.8.0 the
> application" is not the same artifact as "`openhands-ai` 1.8.0 on PyPI" or "the Agent SDK
> paper (arXiv:2511.03690)." Do not attribute an Agent-SDK-only capability to the CLI
> application unless it is present in the pinned application build.

## Docker / runtime image

| Item | Value | Status |
|---|---|---|
| Official image name | not captured from docs excerpt | BLOCKED — resolve from the CLI-mode / installation docs and repo `docker-compose` / Dockerfile at `v1.8.0` |
| Image digest (sha256) | — | BLOCKED — obtain via `docker buildx imagetools inspect <image>` or `docker inspect --format='{{index .RepoDigests 0}}'` after pull; **tag alone is not a pin** |
| Host architecture | — | TO SET at deployment (amd64/arm64) |

## Feature provenance (does the feature exist in *this* object?)

| Feature (cited in findings) | Present in OSS CLI 1.8.0? | Status | Source |
|---|---|---|---|
| Confirmation policy: default always-confirm | Yes | VERIFIED | cli-mode docs |
| `--always-approve` (auto-approve) | Yes | VERIFIED | cli-mode docs |
| `--llm-approve` (LLM security analyzer, risk-gating) | Yes (CLI flag) | LIKELY — confirm flag exists in v1.8.0 build, not only newer SDK | cli-mode docs |
| Security analyzer = risk classification, **not** output verification | Yes (by definition) | VERIFIED (definitional) | SDK security docs |
| MCP servers add/enable/disable | Yes (command palette; card interface per 1.8.0 notes) | LIKELY | cli-mode docs; v1.8.0 notes |
| Sub-agent delegation | Exists in architecture | UNVERIFIED for CLI default | SDK paper (arch); confirm in app |
| Model backend via LiteLLM / env override | Yes | VERIFIED | LLM config docs |

## Remaining blockers to a fully pinned source

1. Confirm the org rename (`OpenHands/OpenHands` vs `All-Hands-AI/OpenHands`).
2. Confirm `v1.8.0` commit SHA against a real checkout (single-source currently).
3. Reconcile the release-date discrepancy and the app-tag ↔ PyPI-`openhands-ai` mapping.
4. Resolve the official Docker image name **and digest** (tag is not a pin).
5. Confirm `--llm-approve`, MCP controls, and delegation exist in the *v1.8.0 application*,
   not only in SDK docs.

None of these is resolvable without repository/registry access to the pinned build. Until
they are `VERIFIED`, classification of C1–C8 does not begin.
