# Changelog

All notable changes to this repository are recorded here. This is the
*repository* changelog. The **ACL protocol** has its own version history
(ACL-1.0.md §11), and protocol versions are frozen once published; see
[RELEASES.md](./RELEASES.md).

Format loosely follows [Keep a Changelog](https://keepachangelog.com/).
Dates are ISO 8601.

## [Unreleased] — Foundation and reference infrastructure

Additive foundation phase. **ACL-1.0 is treated as frozen and immutable: its
wording, states, components, evidence tiers, boundary cases, and published
status are unchanged.** No ACL-2.0 is drafted.

### Added
- `FOUNDATION_DOCTRINE.md` — AGI Construction as a classificatory (not
  predictive) position; the canonical relationship between AGIConstructor and
  ACL; the three distinctions (exists / evidenced / classifiable); independence
  from the safety and capability axes.
- `CONSTRUCTION_ONTOLOGY.md` — the eight audit surfaces grouped into three
  families (capability substrate & operational interfaces / integrative
  mechanisms / control and assurance), stated explicitly as neither necessary
  nor sufficient conditions
  for AGI. Interpretive companion to ACL-1.0; does not change the protocol.
- `ARCHITECTURE.md` — the layer stack: Foundation Doctrine → Construction
  Ontology → ACL-1.0 instrument → Ledgers → Validator/Registry (future).
- `ACL-2.0-CANDIDATES.md` — register of post-publication limitations recorded as
  candidates for a future protocol version; none retrofitted into ACL-1.0.
- `schema/agicl-1.0.schema.json` — JSON Schema (draft 2020-12) faithfully
  encoding ACL-1.0 (eight components, four states, four tiers). AGICL technical
  namespace; no new methodology.
- `templates/ledger-blank.json`, `templates/ledger-blank.yaml`,
  `templates/ledger-blank.csv` — blank ledger templates.
- `examples/example-ledger.md` and `examples/example-ledger.json` — one fully
  worked, explicitly **fictional/illustrative** example (ORCHESTRA-7) with
  sources, evidence tiers, boundary cases, and access limits. Validates against
  the schema.
- `LICENSE` — dual license: CC BY 4.0 for written standards/doctrine, MIT for
  machine-readable artifacts and code.
- `CHANGELOG.md` and `RELEASES.md` — this changelog and the release/versioning
  policy.

### Changed
- `README.md` — added a map of the new reference infrastructure and the layer
  stack. ACL-1.0's content and status are unchanged.

### Unchanged (intentionally)
- `ACL-1.0.md` — frozen. Not modified in any respect.
- `index.html` — untouched. Frontend and repository hardening are deferred to a
  separate, later pull request.

## [0.1.0] — 2026-08-01
### Added
- Initial publication of `ACL-1.0.md` (AGI Component Ledger), `README.md`, and
  `index.html`.
