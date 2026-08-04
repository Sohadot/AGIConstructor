# Surface Contract — REAL-LEDGER-001

**The app-server surface of `openhands-ai` 1.11.0, resolved from the hash-verified wheel source. What is the locked object, and what is the external audit harness.**

All endpoints below were read from the installed wheel
(`openhands_ai-1.11.0-py3-none-any.whl`, sha256 `833de097…452c8f`), package
`openhands/app_server/`. Grade `VERIFIED` = present in that source; `TO CONFIRM AT RUNTIME`
= exact behavior to be checked against a live pinned instance.

## Server invocation (VERIFIED)

```
uvicorn openhands.app_server.app:app --host 0.0.0.0 --port 3000
```
- `openhands/server/__main__.py` is **DEPRECATED**; it forwards to the above. The canonical
  ASGI app is `openhands.app_server.app:app` (FastAPI, title "OpenHands", version from
  `get_version()`). Default port `3000` (overridable via `port` env).
- Running agents requires a **Docker sandbox** (dependency `docker==7.1.0`; send-message
  returns 409/503 when the sandbox is not running / agent-server unavailable). The sandbox
  is part of the object, not the harness.

## Endpoint map (VERIFIED from source)

**Liveness / status** (mounted at root, no prefix):
- `GET /alive` · `GET /health` · `GET /ready` · `GET /server_info`

**API base prefix:** `/api/v1`

**Conversation lifecycle** — `/api/v1/app-conversations` (tag "Conversations"):
- `POST /api/v1/app-conversations` — **create** a conversation (session)
- `POST /api/v1/app-conversations/stream-start` — create + **stream** start updates (SSE/`StreamingResponse`) until started or error
- `POST /api/v1/app-conversations/{conversation_id}/send-message` — **submit a task/message** (`AppSendMessageRequest`). Documented states: 404 not found · 409 sandbox not running (resume via `POST /sandboxes/{id}/resume`) · 410 archived · 503 sandbox error / agent-server unavailable
- `GET /api/v1/app-conversations` (batch) · `/search` · `/count`
- `PATCH /api/v1/app-conversations/{conversation_id}` — update
- `DELETE /api/v1/app-conversations/{conversation_id}`
- `POST …/switch-conversation-profile` · `…/switch-conversation-acp-model` (model/agent indirection via ACP)

**Events** — `/api/v1/conversation/{conversation_id}/events` (note: singular `conversation`):
- `GET /api/v1/conversation/{conversation_id}/events` (batch) · `/search` · `/count` —
  retrieve the **event stream** (actions + observations). Primary evidence source for a run.

**Pending messages** — `/api/v1/conversations/{conversation_id}/pending-messages` (note: plural):
- `POST …/pending-messages` — **queue a user message mid-run**. Candidate mechanism for
  **confirmation responses / approvals**. *TO CONFIRM AT RUNTIME:* whether an approval is
  delivered here or via a dedicated confirmation call.

**Sandbox** — `sandbox_router` (e.g. `POST /sandboxes/{id}/resume`): sandbox lifecycle.
**MCP** — `mcp_router`: mostly git PR/MR helpers; MCP servers otherwise NONE by default (per lock).

## Confirmation / security wiring (mechanism VERIFIED; not classification)
`openhands/app_server/app_conversation/app_conversation_service_base.py` wires a
`SecurityAnalyzer` and `confirmation_mode`. Reminder (TF-001-E): the analyzer gates **action
risk (C7)**; it is **not** C8 output verification. Exact default policy: TO CONFIRM AT RUNTIME.

## What is the locked object vs the harness

**The locked object** =
```
hash-pinned openhands-ai 1.11.0 artifact
+ exact Python/runtime environment
+ app-server invocation (uvicorn openhands.app_server.app:app)
+ fixed model backend
+ fixed Docker workspace/sandbox
+ fixed policy configuration (confirmation / security analyzer)
+ fixed tool/MCP configuration (default: none)
```
The app-server is the **access surface to the locked agent**, not a separate subject.

**The external audit harness** = a fixed program that drives the object over these endpoints:
creates a conversation, submits the task, streams/reads events, responds to confirmation
requests, detects termination/stuck/error, and collects artifacts + workspace diff.

### Harness boundary rule (hard)
> The harness may **observe, invoke, approve, and record** the locked object; it must **not
> add capabilities the locked object does not possess.**

Permitted: submit a task, read events, answer a confirmation request, inspect produced
files. **Not** permitted (would corrupt the audit): adding a verifier or MCP server and
counting it as part of OpenHands; fixing the output or steering the system mid-run unless
that step is a declared, recorded part of the test.

## Smoke gate (must pass before C1–C8 classification)
On the pinned environment (owner-run; needs Docker + a model backend):
1. Server starts from the pinned artifact (`GET /alive`, `/ready` succeed).
2. A conversation can be created (`POST /api/v1/app-conversations`).
3. A real task can be submitted (`POST …/send-message`).
4. The system performs **at least one agent cycle**.
5. Events, actions, and the result are retrievable (`GET …/events`) and savable.
6. The run repeats identically from the fixed harness.

If the smoke gate fails, **do not** proceed to classification; record the object as
non-executable in the pinned environment.

> Status now: the surface is **structurally VERIFIED from source**. The live smoke boot is a
> deployment-produced step (needs the pinned Docker container + a model backend) and has
> **not** been run — it is not claimed here.
