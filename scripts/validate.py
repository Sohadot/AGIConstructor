#!/usr/bin/env python3
"""Validate AGICL ledgers against the ACL-1.0 schema and enforce ACL-1.0 immutability.

Checks:
  1. The schema itself is a valid JSON Schema (draft 2020-12).
  2. The worked example and every tests/valid/*.json validate.
  3. Every tests/invalid/*.json is rejected (e.g. Constructed at Tier C).
  4. Blank JSON template parses.
  5. ACL-1.0.md is unchanged (sha256 matches tests/ACL-1.0.md.sha256).

Exit code 0 on success, 1 on any failure. Requires: jsonschema.
"""
import hashlib
import json
import pathlib
import sys

try:
    import jsonschema
except ImportError:
    sys.exit("jsonschema not installed; run: pip install jsonschema")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "agicl-1.0.schema.json"

failures = []


def load(path):
    return json.loads(path.read_text())


def rel(path):
    return path.relative_to(ROOT)


schema = load(SCHEMA_PATH)
jsonschema.Draft202012Validator.check_schema(schema)
validator = jsonschema.Draft202012Validator(schema)
print(f"PASS schema: {rel(SCHEMA_PATH)} is a valid draft 2020-12 schema")


def expect_valid(path):
    error = jsonschema.exceptions.best_match(validator.iter_errors(load(path)))
    if error is None:
        print(f"PASS valid: {rel(path)}")
    else:
        failures.append(f"expected VALID but failed: {rel(path)} -> {error.message}")
        print(f"FAIL valid: {rel(path)} -> {error.message}")


def expect_invalid(path):
    error = jsonschema.exceptions.best_match(validator.iter_errors(load(path)))
    if error is None:
        failures.append(f"expected INVALID but passed: {rel(path)}")
        print(f"FAIL invalid (passed): {rel(path)}")
    else:
        print(f"PASS invalid (rejected): {rel(path)} -> {error.message[:80]}")


# 2. valid documents
expect_valid(ROOT / "examples" / "example-ledger.json")
for p in sorted((ROOT / "tests" / "valid").glob("*.json")):
    expect_valid(p)

# 3. invalid fixtures
for p in sorted((ROOT / "tests" / "invalid").glob("*.json")):
    expect_invalid(p)

# 4. blank template parses (it is a fill-in form, not a valid ledger)
json.loads((ROOT / "templates" / "ledger-blank.json").read_text())
print("PASS parse: templates/ledger-blank.json")

# 5. ACL-1.0 immutability
acl = ROOT / "ACL-1.0.md"
digest = hashlib.sha256(acl.read_bytes()).hexdigest()
expected = (ROOT / "tests" / "ACL-1.0.md.sha256").read_text().split()[0].strip()
if digest == expected:
    print(f"PASS immutable: ACL-1.0.md sha256 matches ({digest[:12]}...)")
else:
    failures.append(
        f"ACL-1.0.md CHANGED: expected {expected}, got {digest}. "
        "ACL-1.0 is frozen; if this change is intentional it must be a new protocol version."
    )
    print(f"FAIL immutable: ACL-1.0.md sha256 {digest} != expected {expected}")

if failures:
    print("\nFAILURES:")
    for f in failures:
        print("  - " + f)
    sys.exit(1)

print("\nAll checks passed.")
