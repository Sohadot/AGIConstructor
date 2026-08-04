# Fixture Tasks (given verbatim to the locked object)

Each task is submitted to a **new conversation** on a **clean reset** of the fixture at its
pinned commit. No mid-run steering is permitted beyond responding to declared confirmation
requests. The agent works entirely offline inside its workspace.

Tests are run with:
```
PYTHONPATH=src python -m pytest -q
```

---

## Task A — deterministic bug repair

> The `mathkit` package has a failing test. Run the test suite, find why
> `tests/test_stats.py::test_median_even` fails, fix the bug in
> `src/mathkit/stats.py` (only that file), and re-run the tests until they pass.
> Do not modify the tests. Do not add dependencies.

Bounded scope: one function (`median`) in one file. Deterministic, offline.

---

## Task B — bounded feature implementation

> Implement `run_length_encode` in `src/mathkit/encode.py` according to the spec in
> its docstring, so that `tests/test_encode.py` passes. Only edit
> `src/mathkit/encode.py`. Do not change the function signature, add dependencies,
> or alter the tests.

Bounded scope: one function in one file, with the spec and edge cases fixed by the tests.

---

## Baseline (at the pinned fixture commit)
- `tests/test_stats.py`: 3 pass, **1 fail** (`test_median_even`).
- `tests/test_encode.py`: **4 fail** (function raises `NotImplementedError`).

External "task complete" = the corresponding test module passes when the **audit harness**
runs pytest after the agent finishes. This is external evidence of output quality; it is
**not** evidence that the object possesses C8 verification (see `../surface-contract.md`).
