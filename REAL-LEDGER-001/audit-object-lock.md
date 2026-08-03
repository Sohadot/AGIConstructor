# Audit Object Lock — REAL-LEDGER-001

**The exact object this audit binds to. A ledger is invalid if the object shifts.**

This extends ACL-1.0 §6.1 ("Fix the object") for a compositional agentic system, where a
product name and release number do **not** uniquely identify what is being audited. The
audit does not begin until every field below is set. Fields marked `[UNSET — requires
pinned deployment]` cannot be filled from documentation; they require an actual, pinned
install and are the reason this ledger is still in the object-definition phase.

## Lock

```
Product family:        OpenHands
Distribution:          OpenHands OSS (MIT)          # NOT Cloud, NOT Enterprise
Artifact:              [RE-PIN REQUIRED — see source-pin.md]
                       # VERIFIED: GitHub tag v1.8.0 (c7a765d) = @openhands/agent-canvas
                       #   (GUI orchestrator), NOT the openhands CLI.
                       # The "CLI surface" belongs to PyPI openhands-ai (Python agent).
                       # Object A: openhands-ai (Python CLI/agent) @ [version TBD]
                       # Object B: @openhands/agent-canvas v1.8.0 (GUI orchestrator)
Release tag:           [RE-PIN — depends on Artifact above]
Release date:          [RESOLVED per artifact: openhands-ai 1.8.0 = 2026-06-10 (PyPI);
                        agent-canvas v1.8.0 GitHub tag = later date]
Deployment surface:    OpenHands OSS Application CLI   # implies Object A (openhands-ai)
Execution mode:        Local Docker runtime          # sandbox settings to pin
Commit SHA:            [UNSET — requires pinned deployment]
Container image+digest:[UNSET — requires pinned deployment]
Agent SDK version:     [UNSET — requires pinned deployment]
Model backend:         [UNSET — provider/model/version; injected via LiteLLM, not fixed
                        by the product]
Tool set / MCP servers:[UNSET — exact enabled MCP servers and built-in tools]
Confirmation policy:   [UNSET — e.g. AlwaysConfirm() | never | LLM-approve]
Security analyzer:     [UNSET — enabled/disabled; which analyzer]
Sub-agent delegation:  [UNSET — enabled/disabled]
Iteration/budget caps: [UNSET — exact values]
Configuration hash:    [UNSET — SHA-256 of the full resolved configuration]
Audit window:          [UNSET — start/end dates]
```

## Explicitly excluded from this object

- OpenHands Cloud (multi-tenant SaaS)
- OpenHands Cloud Self-hosted
- OpenHands Enterprise (SAML/RBAC, LLM gateway & budgeting, observability, plugin marketplace)
- Any release other than the one pinned above
- Unpinned `main`-branch code
- Any model backend, tool set, or policy configuration not listed above

## Binding rule

> Any material change to the object defined above creates a **new audit object**, not an
> update to REAL-LEDGER-001. A new object requires a new ledger (REAL-LEDGER-002, …).

Rationale: the same OpenHands release can present different C1 (inference substrate), C3
(tools), C4 (environment), C6 (coordination), and C7 (authority) surfaces depending on the
resolved configuration. Without a locked configuration hash, a component finding cannot be
attributed to "OpenHands" at all — only to one configuration of it. Whether the locked
object contains a qualifying **C8** verification mechanism remains **unresolved** and must
be established separately: the security analyzer gates action risk (C7), it does not verify
output correctness.
