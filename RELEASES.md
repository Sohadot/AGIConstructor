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

| Tag | Target commit (SHA) | Meaning |
|---|---|---|
| `ACL-1.0` | `3ddd4cf9118476c871a207af7010d155ce227233` | Stable, immutable reference to the AGI Component Ledger document as first introduced (commit "Add ACL-1.0 document for AGI audit protocol"). The document behind this tag will not change. |
| `v0.1.0` | `d5e3945a28d8b858285aacd39c3a63b4ced3f91d` | Initial repository publication complete — ACL-1.0.md, README.md, index.html. |
| `v0.2.0` *(planned)* | the eventual merge commit of PR #1 (foundation phase) | Adds doctrine, ontology, architecture, schema, templates, worked example, license, and governance files around the frozen ACL-1.0. Not yet known; set to the merge commit after PR #1 merges. |

> **Note on tag creation.** The `ACL-1.0` and `v0.1.0` tags mark the exact
> historical commits above — both already on `main`. They must be created
> pointing at those SHAs, **not** at any post-merge head, so the published
> protocol is anchored to its canonical history. The `ACL-1.0` tag deliberately
> points at commit `3ddd4cf` (where the protocol document was introduced),
> never at a later commit. This foundation-phase work lands via PR #1; the
> `v0.2.0` tag is applied to `main` only after that PR merges, at its merge
> commit. Creating these tags is a maintainer action on `main` and is
> intentionally not performed from the feature branch.

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
