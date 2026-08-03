# Build Runbook — REAL-LEDGER-001 (non-paid)

**Exact commands to build and structurally validate the pinned object with NO API key and NO paid model request.** Steps needing the pinned host (Docker daemon, amd64/Ubuntu, Python 3.12) are marked `@HOST`; what was already produced here is marked `DONE`.

## 0. Environment (this sandbox vs pinned host)
- This sandbox: Python 3.11, no Docker daemon → cannot boot the app-server here.
- Pinned host required: amd64 Ubuntu 24.04, Python 3.12.x, Docker Engine. Record exact
  `python --version` and `docker version` into the configuration hash.

## 1. Hashed dependency lock — DONE
Produced with `uv` for py3.12 / linux-x86_64:
```
uv pip compile oh-requirements.in --generate-hashes \
  --python-version 3.12 --python-platform x86_64-unknown-linux-gnu \
  -o build/openhands-ai-1.11.0.lock.txt
```
- File: `build/openhands-ai-1.11.0.lock.txt` (319 pinned packages, 3913 hashes).
- Lock sha256: `7222056aec4d51ff24459c3fe7164daa50754b288bd2d2c34150c8f3785c01d7`.
- Contains the verified pins: `openhands-ai==1.11.0`, `openhands-sdk==1.34.0`,
  `openhands-agent-server==1.34.0`, `openhands-tools==1.34.0`, `litellm==1.84.1`,
  `openai==2.33.0`, `docker==7.1.0`, `agent-client-protocol==0.12.0` (ACP, via sdk).

## 2. Create the pinned venv and install with hashes — @HOST
```
uv venv --python 3.12 .venv && . .venv/bin/activate
uv pip sync build/openhands-ai-1.11.0.lock.txt      # hash-checked install
python -c "import openhands, importlib.metadata as m; print(m.version('openhands-ai'))"  # -> 1.11.0
```

## 3. Record runtime versions — @HOST
```
python --version                 # pin 3.12.x
docker version --format '{{.Server.Version}}'
uname -srm                       # kernel + arch (amd64)
```

## 4. Pin container images by DIGEST — @HOST
Resolve the runner/workspace image the object uses, then pin by digest (never tag):
```
docker pull <runner-image>:<tag>
docker inspect --format='{{index .RepoDigests 0}}' <runner-image>:<tag>
docker buildx imagetools inspect <runner-image>:<tag>   # cross-check
```
Record base Python image, runner image, and workspace image digests + host arch.

## 5. Boot the app-server (NO key needed) — @HOST
```
# bind to loopback per security-review F5
uvicorn openhands.app_server.app:app --host 127.0.0.1 --port 3000
```

## 6. Health checks (NO key) — @HOST
```
curl -fsS http://127.0.0.1:3000/alive
curl -fsS http://127.0.0.1:3000/ready
curl -fsS http://127.0.0.1:3000/health
curl -fsS http://127.0.0.1:3000/server_info
```
Expect success without any model configured. This proves the surface is up; it is **not**
ACL evidence.

## 7. Harness plumbing with a MOCK model — @HOST
Use `harness/` in mock mode (see `harness/README.md`) to exercise create-conversation →
send-message → read-events against a **mock/replayed** LLM. Confirms plumbing, event capture,
approval flow, and artifact retention. **No ACL component evidence** — mocks do not represent
the object's behavior.

## 8. Telemetry / egress hardening — @HOST (security-review F4/F5)
Disable `posthog`/`lmnr` telemetry via env/config; restrict outbound egress by allowlist to
the OpenAI API and package/registry hosts only; verify no telemetry leaves during boot.

## 9. STOP
Do not enter an API key or make any live model request. The decision to create a disposable,
project-scoped key and run the smoke gate + audit runs is a separate, later, owner-approved
step (see `pre-execution-manifest.md` §10 and `security-review.md`).
