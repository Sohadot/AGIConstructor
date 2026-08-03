# Security Review — REAL-LEDGER-001 (non-paid, source-grounded)

**Reviews secret handling and egress in the hash-pinned object before any key is introduced.**
Scope: `openhands-ai` 1.11.0 + `openhands-sdk` 1.34.0 (extracted wheels). No key was created,
stored, or used. No live request was made.

## Findings

**F1 — API keys are `SecretStr` (good).** `openhands/sdk/llm/llm.py`: `api_key: str |
SecretStr | None`; AWS creds likewise. `get_secret_value()` is called only when building the
provider request. Pydantic `SecretStr` masks the value in `repr`/logs by default. `VERIFIED`.

**F2 — Profile store redacts secrets (good).** `openhands/sdk/llm/llm_profile_store.py`
persists only a boolean `api_key_set` and uses a `REDACTED_SECRET_VALUE` sentinel rather than
the raw key. `VERIFIED`.

**F3 — No env/key dumping found (good).** No `print(os.environ)` / logging of `api_key` /
env dumps in the app or SDK source. The only env read in the deprecated launcher is `DEBUG`
(log level). `VERIFIED` (grep, may not be exhaustive).

**F4 — Telemetry dependencies present (caution).** `posthog` and `lmnr` (Laminar) are
dependencies. Default on/off state **not confirmed** from source. *Mitigation for the pinned
env:* explicitly disable telemetry (env/config) and restrict egress by allowlist so nothing
leaves except the OpenAI API and package/registry pulls. `TO CONFIRM @BUILD`.

**F5 — App-server binds `0.0.0.0:3000` by default (caution).** Exposes the API on all
interfaces. *Mitigation:* bind to loopback or firewall the port; never expose the pinned
instance publicly. `VERIFIED` (source default).

**F6 — Request/response content egresses to OpenAI (inherent).** Keep all task content
synthetic and public. The `fixture/mathkit` tasks contain no secrets or personal data —
satisfied.

## Operational key policy (applies only when a run is later authorized)

- Use a **disposable, project-scoped** OpenAI key created for this ledger (e.g. project
  `AGIConstructor-REAL-LEDGER-001`) — **never** a primary or shared key.
- Restrict scope, set an independent spend limit + alerts, store in an env var / secret
  manager only, and **delete the key immediately** after the run.
- The full key is shown once at creation; treat as write-once.
- Never place a key in: GitHub, committed `.env`, `Dockerfile`, an image layer, any manifest,
  logs, or a message to the agent.

## Non-paid stage boundary
The build, app-server boot, and health checks need **no key**. Any mock/replay used to test
plumbing provides **no ACL component evidence**. Stop before any live model request.
