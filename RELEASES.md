# Releases and Versioning

This document states how AGIConstructor versions its published artifacts, and
records the release tags that make published versions stable, retrievable
references.

## Two version tracks

1. **Protocol versions** (e.g., `ACL-1.0`) — the audit instrument itself.
   Published protocol versions are **frozen**: their text is not modified after
   publication. Substantive changes are issued under a new number (ACL-1.1 for
   compatible refinements, ACL-2.0 for breaking changes), with prior versions
   remaining retrievable. This is the commitment in ACL-1.0.md §11.

2. **Repository releases** (e.g., `v0.2.0`) — the state of this repository as a
   whole (docs, schema, templates, examples, site). Tracked in
   [CHANGELOG.md](./CHANGELOG.md). Repository releases may add supporting
   material around a protocol without ever altering a frozen protocol version.

## Tags

| Tag | Points at | Meaning |
|---|---|---|
| `ACL-1.0` | the published ACL-1.0 protocol | Stable, immutable reference to the AGI Component Ledger as first published (2026-08-01). The document behind this tag will not change. |
| `v0.1.0` | initial repository publication | ACL-1.0.md, README.md, index.html as first published. |
| `v0.2.0` *(planned)* | this foundation phase | Adds doctrine, ontology, architecture, schema, templates, worked example, license, and governance files around the frozen ACL-1.0. |

> **Note on tag creation.** The `ACL-1.0` and `v0.1.0` tags mark commits already
> on `main`. They are created on `main`, not on a feature branch, so that the
> published protocol is anchored to its canonical history. This foundation-phase
> work lands via its own pull request; the `v0.2.0` tag is applied to `main`
> only after that PR is merged. Creating the `ACL-1.0` tag is a maintainer
> action on `main` and is intentionally not performed from the feature branch.

## Immutability guarantee

- A published **protocol version** is never silently modified. If an error is
  found, it is corrected in a new version, and the correction is noted; the old
  version remains retrievable at its tag.
- Post-publication limitations are recorded in
  [ACL-2.0-CANDIDATES.md](./ACL-2.0-CANDIDATES.md), never patched into the frozen
  text.
- **Supersession policy:** when a new protocol version supersedes an older one,
  the older version's document gains a non-substantive header note pointing to
  the successor. The note records status; it does not alter the classificatory
  content of the superseded version.
