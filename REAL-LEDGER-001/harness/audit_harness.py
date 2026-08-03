#!/usr/bin/env python3
"""REAL-LEDGER-001 audit harness (skeleton).

Drives the openhands-ai 1.11.0 app-server surface over HTTP and records evidence.
Stdlib only. This is the EXTERNAL harness, not part of the locked object.

BOUNDARY: observe, invoke, approve, record only. Never add capabilities to the object.

Phase status: MOCK plumbing only. In --mock mode, evidence produced is NOT ACL evidence.
Live runs (real model, disposable key) are a separate, owner-approved step and are gated
off here. No API key is read or required by this skeleton.
"""
from __future__ import annotations

import argparse
import json
import time
import urllib.request
import urllib.error

BASE = "http://127.0.0.1:3000"
API = f"{BASE}/api/v1"


def _req(method: str, path: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        path, data=data, method=method,
        headers={"Content-Type": "application/json"} if data else {},
    )
    with urllib.request.urlopen(req, timeout=30) as r:  # nosec - localhost only
        return json.loads(r.read() or b"{}")


def wait_healthy(retries: int = 30) -> bool:
    for _ in range(retries):
        try:
            urllib.request.urlopen(f"{BASE}/ready", timeout=5)
            return True
        except urllib.error.URLError:
            time.sleep(1)
    return False


def create_conversation() -> str:
    resp = _req("POST", f"{API}/app-conversations", {})  # payload pinned at build
    return resp["id"]  # exact field confirmed against live server


def submit_task(conversation_id: str, task_text: str) -> None:
    _req("POST", f"{API}/app-conversations/{conversation_id}/send-message",
         {"content": task_text})  # AppSendMessageRequest shape pinned at build


def read_events(conversation_id: str) -> list:
    return _req("GET", f"{API}/conversation/{conversation_id}/events", None).get("items", [])


def answer_confirmation(conversation_id: str, message: str) -> None:
    # Candidate approval path (surface-contract): queue a pending message.
    _req("POST", f"{API}/conversations/{conversation_id}/pending-messages",
         {"content": message})


def run_once(task_text: str, out_dir: str, mock: bool) -> None:
    """One clean-reset run. Records events/result to out_dir. Mock => plumbing only."""
    assert mock, "Live runs are gated: use the owner-approved live procedure, not this skeleton."
    if not wait_healthy():
        raise SystemExit("app-server not healthy; see build-runbook.md §5-6")
    cid = create_conversation()
    submit_task(cid, task_text)
    # poll events until terminal/stuck/error; answer only DECLARED confirmation requests
    # (loop, termination detection, artifact + workspace-diff capture: pinned at build)
    _ = cid, out_dir  # retention wiring finalized on the pinned host


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--mock", action="store_true", help="plumbing only; no ACL evidence")
    p.add_argument("--task", required=True)
    p.add_argument("--out", default="runs/tmp")
    a = p.parse_args()
    if not a.mock:
        raise SystemExit("Refusing to run live: no key handling in this skeleton. Use --mock.")
    run_once(a.task, a.out, mock=True)


if __name__ == "__main__":
    main()
