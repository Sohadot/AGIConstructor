# Trial Findings — REAL-LEDGER-001 (OpenHands)

**Methodological findings from applying ACL-1.0, not component results and not protocol changes.**

These emerged while *fixing the object* (ACL-1.0 §6.1) and preparing to assign evidence
tiers. Each is tied to a verifiable, documented fact about OpenHands. None asserts a
capability, a state, or a tier. Whether any finding warrants a future protocol change is
**deferred to a package review after the trial is complete**; the "provisional read" below
is a first impression only.

After the first pass, the findings reorganize under **two central discoveries** rather than
six independent ones — this deliberately avoids inflating the count of apparent protocol
gaps before the trial completes.

Legend: **Execution note** — handled within the ledger (e.g. via the object lock), no
protocol change implied. **Candidate protocol gap** — may indicate a real ACL-1.0
limitation; overlaps with `ACL-2.0-CANDIDATES.md` are noted, not acted on.

---

## Evidence-provenance discipline (applies to all findings below)

A single rule governs this ledger and is stated once here: **do not mix evidence across
objects.** Evidence admissible for *OpenHands OSS Application, CLI surface* is not
interchangeable with evidence drawn from:

- the **Agent SDK / agent-server** as a library (separately versioned — see `source-pin.md`),
- **OpenHands Cloud**, **Cloud Self-hosted**, or **Enterprise**,
- or a **different release** than the one locked.

A documented feature is only admissible for this ledger if it is present in the *locked
object* (OSS Application, the pinned release, the CLI surface), not merely in newer SDK
docs or another distribution. Feature provenance is resolved per feature in `source-pin.md`.

---

## TF-001 — Audit identity resolves at the configuration level

**Central discovery.** For a compositional agentic system, several ACL-1.0 components are
properties of a *resolved deployment configuration*, not of the named product. A component
finding cannot be attributed to "OpenHands" — only to one configuration of it. The
sub-findings below are facets of this one discovery, each pointing at a required field of
the Audit Object Lock.

### TF-001-A — Distribution and artifact lineage (now VERIFIED, concretely)
"OpenHands" names at least three distributions — OSS (MIT), Cloud (multi-tenant SaaS +
self-hosted), Enterprise. Read-only source inspection then surfaced a stronger, verified
fact: the *number* "1.8.0" itself names **distinct artifacts** built from different sources:

- **GitHub tag `v1.8.0`** (`OpenHands/OpenHands`, commit `c7a765d…`, lightweight tag) =
  **`@openhands/agent-canvas` v1.8.0** — a TypeScript/Electron *control-center UI* that
  orchestrates other agents (OpenHands, Claude Code, Codex, Gemini via ACP). Not the agent,
  not the `openhands` CLI.
- **PyPI `openhands-ai` 1.8.0** (uploaded 2026-06-10) = the **Python agent framework / CLI**
  (deps include `anthropic`, `browsergym`). Latest is actually **1.11.0**. Its source commit
  is unresolved: the declared repo at tag `v1.8.0` is Agent Canvas, so the Python source
  pre-dates the repo's pivot.
- Plus separately-versioned sub-components (agent-server 1.39.1, automation 1.5.0,
  typescript-client 1.36.1).

The `All-Hands-AI/OpenHands` → `OpenHands/OpenHands` rename is confirmed (identical tag
SHAs). *Lock fields: Distribution + Artifact (Agent Canvas vs openhands-ai) + Release +
source commit + sub-component versions.* **Candidate protocol gap** (overlaps
`ACL-2.0-CANDIDATES.md` C-06). See `source-pin.md` for the full evidence table. This is the
object-identity trap caught in practice, before any classification.

### TF-001-B — Execution surface
Within OSS, OpenHands runs as a local GUI (Agent Canvas), a CLI, and an SDK/headless
library; defaults and available controls differ. *Lock field: Deployment surface.*
**Execution note.**

### TF-001-C — Injected model backend (C1)
The model is wrapped by LiteLLM and selected by configuration (`LLM_MODEL`, base URL,
`--override-with-envs`), not fixed by the release. C1's audit question — "what model
performs inference?" — is answered by the configuration. *Lock field: Model backend.*
**Candidate protocol gap.**

### TF-001-D — Authority configuration (C7)
The CLI's confirmation policy is a dial: default **always-confirm**, `--always-approve`
(auto-approve), or `--llm-approve`. Whether an action executes unilaterally or requires
approval, and whether the boundary is enforced, is set at configuration time. This is
squarely the **C7 Authority** surface. *Lock field: Confirmation policy + enforcement.*
**Candidate protocol gap** (config-resolved C7).

### TF-001-E — Security analysis is not ACL verification (correction to the earlier draft)
The OpenHands **security analyzer** (`--llm-approve`) classifies *action risk before
execution* (LOW/MEDIUM/HIGH/UNKNOWN) and feeds the confirmation policy. It does **not**,
by itself, independently verify that outputs are *correct*. Therefore it is a support layer
for **C7 Authority / risk-gating**, **not** ACL-1.0 **C8 Verification**, which requires
independent confirmation of output correctness, repeatably, by a verifier independent of
the generator.

> The earlier draft conflated the security analyzer with C8. Corrected: confirmation policy
> and security analyzer inform C7; C8 remains **unresolved** until an actual
> correctness-verification mechanism is identified and tested against the locked object —
> e.g. independent tests run on the output, a verifier separate from the generator, a
> genuinely independent evaluator agent, or repeatable verification of a fix/solution.
> Its absence may later map to Absent / Claimed / Partial depending on evidence; **not
> classified now.**

### TF-001-F — Pluggable tools (C3)
MCP servers can be added/enabled/disabled; the built-in tool set varies by configuration.
C3 presence depends on which servers/tools are enabled. *Lock field: Tool set / MCP
servers.* **Execution note.**

### TF-001-G — Optional coordination / delegation (C6)
Sub-agent delegation is an auxiliary service off the event stream (enable/disable), so C6
presence is per-configuration. *Lock field: Sub-agent delegation.* **Execution note.**

---

## TF-002 — Evidence type and proposition mismatch

**Central discovery (second).** Even for a fully open, executable OSS target, the *kind* of
evidence differs by component and by proposition. Independent **behavioral** reproduction
(nominally Tier A) can establish propositions like "tool use occurs" or "memory alters
later behavior," yet cannot by itself establish **architectural/internal** propositions —
model composition (C1), verifier independence (C8), or where authority is enforced (C7).
For an open target some of those are instead established by **source inspection**, which is
a different evidence character than reproduction and is not cleanly placed on the A–D
ladder. Openness therefore yields *material that can support* a tier for a *specific
proposition*, not a blanket tier for a component.

**Effect on ACL-1.0.** The uniform A–D ladder does not distinguish behavioral from
architectural/source evidence, nor bind evidence to the specific proposition it supports.

**Trial resolution.** Record, per component, both the proposition and the evidence
character; do not force onto the A–D ladder prematurely. **Candidate protocol gap**
(instantiates `ACL-2.0-CANDIDATES.md` C-04 and C-05).

---

## Package summary (for review, not decision)

| ID | Facet | Lock field | Provisional read | Overlap |
|---|---|---|---|---|
| TF-001-A | Distribution / release / sub-component lineage | Distribution, Release, sub-versions | Candidate gap | C-06 |
| TF-001-B | Execution surface | Deployment surface | Execution note | — |
| TF-001-C | Injected model backend (C1) | Model backend | Candidate gap | — |
| TF-001-D | Authority configuration (C7) | Confirmation policy | Candidate gap | — |
| TF-001-E | Security analysis ≠ C8 verification | (Security analyzer under C7) | Correction; C8 unresolved | — |
| TF-001-F | Pluggable tools (C3) | Tool set / MCP | Execution note | — |
| TF-001-G | Optional coordination (C6) | Sub-agent delegation | Execution note | — |
| TF-002 | Evidence type vs proposition | (evidence recording) | Candidate gap | C-04, C-05 |

**Common thread.** Two central discoveries, not eight problems: (1) audit identity resolves
at configuration level; (2) evidence type must be matched to the specific proposition.
Nothing is promoted to a protocol change until the trial completes and the package is
reviewed whole.

## Sources

- Enterprise vs. Open Source — docs.openhands.dev/enterprise/enterprise-vs-oss (2026-08-03)
- CLI mode (confirmation modes, `--always-approve`, `--llm-approve`, MCP palette) — docs.openhands.dev/usage/how-to/cli-mode (2026-08-03)
- Security & Action Confirmation (SDK) — docs.openhands.dev/sdk/guides/security (2026-08-03)
- LLM Configuration & Provider Support — OpenHands docs / DeepWiki (2026-08-03)
- OpenHands SDK paper — arXiv:2511.03690 (2026-08-03)
- GitHub releases (tag v1.8.0 → c7a765d…; sub-component bumps) — github.com/OpenHands/OpenHands/releases (2026-08-03)
