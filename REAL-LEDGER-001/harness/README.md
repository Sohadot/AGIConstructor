# Audit Harness — REAL-LEDGER-001

A **fixed** external program that drives the locked object over its app-server surface and
records evidence. It is **not** part of the object (see `../surface-contract.md` → boundary).

## Boundary rule (hard)
> The harness may observe, invoke, approve, and record the locked object; it must not add
> capabilities the object does not possess.

Permitted: create a conversation, submit a task, read events, answer a *declared* confirmation
request, collect the workspace diff + result. Forbidden: adding a verifier/MCP/tool and
counting it as OpenHands; steering or fixing output mid-run unless a declared, recorded step.

## Modes
- `--mock` (this phase): talks to a **mock/replayed** LLM. Confirms plumbing only —
  create → send → events → approval → artifact capture. **Produces no ACL evidence.**
- live (later, owner-approved): real `openai/gpt-5-2025-08-07` via a disposable key. Not now.

## Endpoints used (verified from the artifact; see surface-contract.md)
- `POST /api/v1/app-conversations` — create
- `POST /api/v1/app-conversations/{id}/send-message` — submit task
- `GET  /api/v1/conversation/{id}/events` — read event stream (actions/observations)
- `POST /api/v1/conversations/{id}/pending-messages` — confirmation/approval (candidate)
- `GET  /alive` `/ready` — liveness

## Status
Skeleton only. Requires the pinned host (Python 3.12 + Docker + booted app-server) to run;
it was **not** executed in the build sandbox (Python 3.11, no Docker daemon).
