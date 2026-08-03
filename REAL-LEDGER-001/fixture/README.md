# REAL-LEDGER-001 Fixture — `mathkit`

A tiny, **offline, deterministic** Python package used as the fixed task surface for
REAL-LEDGER-001. No network access is required or permitted to complete the tasks.

- Package: `mathkit` (pure Python, stdlib only)
- Test runner: `pytest`
- Two bounded tasks: see [`TASKS.md`](./TASKS.md)

## Layout
```
fixture/
├── README.md
├── TASKS.md            # the two task prompts (given verbatim to the agent)
├── manifest.json       # files that constitute the fixture (for hashing)
├── src/mathkit/__init__.py
├── src/mathkit/stats.py     # Task A operates here (contains one deterministic bug)
├── src/mathkit/encode.py    # Task B operates here (contains one stub to implement)
├── tests/test_stats.py      # Task A: one test fails until the bug is fixed
└── tests/test_encode.py     # Task B: all tests fail until the stub is implemented
```

## Running the tests (external check, not part of the object)
```
cd fixture && PYTHONPATH=src python -m pytest -q
```
Baseline at the pinned fixture commit: **test_stats has exactly one failure** (Task A),
and **test_encode fails entirely** (Task B, not yet implemented). A task is *externally*
considered complete when its test module passes — this is evidence collected by the audit
harness, **not** evidence that the object possesses C8 (see surface-contract.md).
