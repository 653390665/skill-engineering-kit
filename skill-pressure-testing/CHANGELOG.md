# Changelog: skill-pressure-testing

## v1.0.2 — 2026-05-16

### Changed

- Added explicit frontmatter metadata for version tracking.
- Added `REGRESSION_MATRIX.md` for release-to-release comparison.

### Unchanged

- Activation rule remains explicit-only: pressure testing does not run for ordinary skill creation or prose editing.
- Scope router remains proportional: static checks for documentation/package changes, focused tests for local changes, full with/without benchmark for major releases or explicit benchmark requests.

### Regression Scope

Static validation plus inspection of `REGRESSION_MATRIX.md` is sufficient for this patch because no behavior, trigger, routing, or scoring rule changed.
