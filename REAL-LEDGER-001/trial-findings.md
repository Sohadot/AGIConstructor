# Trial Findings — REAL-LEDGER-001 (OpenHands)

**Methodological findings from applying ACL-1.0, not component results and not protocol changes.**

These emerged while *fixing the object* (ACL-1.0 §6.1) and preparing to assign evidence
tiers. Each is tied to a verifiable, documented fact about OpenHands. None asserts a
capability, a state, or a tier. Per REAL-LEDGER-001's rules, whether any finding warrants
a future protocol change is **deferred to a package review after the trial is complete** —
the "provisional read" below is a first impression only, not a decision.

Legend for provisional read:
- **Execution note** — likely handled within the ledger (e.g. via the object lock), no
  protocol change implied.
- **Candidate protocol gap** — may indicate a real limitation of ACL-1.0; overlaps an
  existing `ACL-2.0-CANDIDATES.md` entry are noted but **not** acted on now.

---

## TF-001 — A product version does not uniquely identify the audit object

**Observed.** "OpenHands" names at least three distinct distributions — OSS (MIT), Cloud
(multi-tenant SaaS + self-hosted), and Enterprise — whose architecture, licensing,
features, authentication, and inspectability differ materially (e.g. Enterprise adds
SAML/RBAC, LLM gateway & budgeting, observability, a plugin marketplace; OSS is local-only
via Docker/CLI). "OpenHands 1.8.0" therefore does not name one object.

**Effect on ACL-1.0.** §6.1 "Fix the object" is directionally correct but *operationally
underspecified* for compositional agentic systems: it presumes a name+version suffices.

**Trial resolution.** Define and hash a complete deployment configuration (see
`audit-object-lock.md`) before any component classification.

**Provisional read.** Candidate protocol gap (object-identity definition). Overlaps
`ACL-2.0-CANDIDATES.md` C-06 (fix-the-object as a first-class stage). *Deferred.*

---

## TF-002 — The deployment surface, not just the distribution, changes the object

**Observed.** Even within OSS, OpenHands is usable as a local GUI (Agent Canvas), a CLI,
and an SDK/headless library. Available controls and defaults differ across these surfaces
(the SDK exposes confirmation policies and analyzers programmatically; the GUI presents
different defaults).

**Effect on ACL-1.0.** The object lock must fix the *surface*, not only the distribution
and version, or two audits of "OpenHands 1.8.0 OSS" could diverge.

**Trial resolution.** `Deployment surface` is a required field in the object lock.

**Provisional read.** Execution note (handled by the lock). *Deferred.*

---

## TF-003 — The inference substrate (C1) is injected, not part of the product

**Observed.** OpenHands wraps the model in LiteLLM for provider portability; the model is
selected by configuration (`LLM_MODEL`, base URL, `--override-with-envs`), not fixed by the
release. The same release runs on many different backends.

**Effect on ACL-1.0.** C1's audit question — "what model performs inference?" — is answered
by the *configuration*, not the product. A C1 finding is meaningless unless the model
backend is part of the locked object.

**Trial resolution.** `Model backend` is a required field in the object lock; a change of
backend is a new object.

**Provisional read.** Candidate protocol gap (component whose identity lives in config, not
the product). *Deferred.*

---

## TF-004 — Authority (C7) and Verification (C8) are configuration dials, not fixed properties

**Observed.** OpenHands controls actions via a *confirmation policy* (e.g. `AlwaysConfirm()`,
never, or LLM-approve via `--llm-approve`) and a *security analyzer* that assigns risk
levels (LOW/MEDIUM/HIGH/UNKNOWN). Both are toggles set at configuration time.

**Effect on ACL-1.0.** The same product can present Authority (C7) and Verification (C8) as
present *or* absent purely by configuration. ACL-1.0 treats components as properties of
"the system"; here two of them are dials. This is the sharpest finding: without a locked
policy configuration, C7 and C8 findings are unattributable.

**Trial resolution.** `Confirmation policy` and `Security analyzer` are required fields in
the object lock.

**Provisional read.** Candidate protocol gap (config-dependent component presence). Distinct
from — and possibly stronger than — the existing candidates, because it affects *which*
state is even assessable. *Deferred.*

---

## TF-005 — Tools (C3) and Coordination (C6) are pluggable

**Observed.** MCP servers can be added, enabled, or disabled; sub-agent delegation is
described as an auxiliary service hanging off the event stream (enable/disable). So the
tool set (C3) and multi-agent coordination (C6) are per-configuration.

**Effect on ACL-1.0.** C3 and C6 presence depends on which MCP servers and delegation are
enabled — again, a property of the configuration, not the release.

**Trial resolution.** `Tool set / MCP servers` and `Sub-agent delegation` are required
fields in the object lock.

**Provisional read.** Execution note for the lock, but reinforces the TF-003/TF-004 theme
that "the system" is a resolved configuration. *Deferred.*

---

## TF-006 — Evidence-tier applicability differs by component even for an open, executable target

**Observed.** OSS is both inspectable (source) and executable, which might suggest Tier A/B
across the board. But the *kind* of evidence differs by component: independent *behavioral*
reproduction (nominally Tier A) can establish, say, tool use or memory effects, yet cannot
by itself establish *architectural/internal* facts — model composition (C1), verifier
independence (C8), or where authority is enforced (C7). For an open target some of those
are instead established by *source inspection*, which is a different evidence character than
reproduction and is not cleanly placed on the A–D ladder.

**Effect on ACL-1.0.** The uniform A–D tier ladder does not distinguish behavioral evidence
from architectural/source evidence, and does not say which is admissible for which
component.

**Trial resolution.** Record per-component evidence character during classification; do not
force it onto the A–D ladder prematurely.

**Provisional read.** Candidate protocol gap. Directly instantiates `ACL-2.0-CANDIDATES.md`
C-04 (per-component admissible evidence) and C-05 (evidence attributes). *Deferred.*

---

## Package summary (for review, not decision)

| ID | Theme | Provisional read | Existing candidate overlap |
|---|---|---|---|
| TF-001 | Distribution ≠ object | Candidate protocol gap | C-06 |
| TF-002 | Surface ≠ object | Execution note | — |
| TF-003 | C1 injected via config | Candidate protocol gap | — |
| TF-004 | C7/C8 are config dials | Candidate protocol gap (sharp) | — |
| TF-005 | C3/C6 pluggable | Execution note | — |
| TF-006 | Tier ladder mixes evidence kinds | Candidate protocol gap | C-04, C-05 |

**Common thread.** For a compositional agentic system, several ACL-1.0 components are
properties of a *resolved configuration*, not of the named product. This is one finding
wearing five hats as much as it is five findings — which is itself worth deciding in the
package review. Nothing here is promoted to a protocol change until the trial completes and
the package is reviewed as a whole.

## Sources

- Enterprise vs. Open Source — docs.openhands.dev/enterprise/enterprise-vs-oss (2026-08-03)
- Security & Action Confirmation (SDK) — docs.openhands.dev/sdk/guides/security (2026-08-03)
- LLM Configuration & Provider Support — OpenHands docs / DeepWiki (2026-08-03)
- OpenHands SDK paper — arXiv:2511.03690 (2026-08-03)
- Release 1.8.0 (2026-06-10) — PyPI `openhands-ai` / GitHub releases (2026-08-03)
