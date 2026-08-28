# Manifest: skill-pressure-testing v1.0.1

## Root Files

- `SKILL.md` — main skill definition and workflow.
- `README.md` — user-facing install and usage overview.
- `MANIFEST.md` — package inventory.
- `QUALITY_TESTS.md` — quality test cases for this skill.
- `PRESSURE_TEST_REPORT.md` — current review and patch result.

## References

- `references/pressure-test-method.md`
- `references/scenario-patterns.md`
- `references/external-patterns.md`
- `references/test-artifact-design.md`
- `references/grading-rubric.md`
- `references/trigger-eval.md`
- `references/security-scan.md`
- `references/report-template.md`
- `references/release-checklist.md`

## Tooling

The deterministic helpers now live in the standalone **`skill-eval`** package
(separate repository). Install with `pip install skill-eval`; the CLI entry
points are:

- `validate-pressure-pack`
- `prepare-pressure-run`
- `check-pressure-run`
- `run-codex-pressure`
- `score-scenarios`
- `check-template-consistency`

See `SKILL.md` → "Deterministic Tooling (skill-eval)" for usage.

## Tests

- `tests/scenarios/skill-pressure-testing/acceptance-criteria.md`
- `tests/scenarios/skill-pressure-testing/scenarios.yaml`

## Excluded From Clean Package

- `__MACOSX/`
- `__pycache__/`
- `*.pyc`
- `.DS_Store`
- `pressure-runs/`
- local absolute machine paths

- `REGRESSION_MATRIX.md` — release-to-release regression tracking template.

- `CHANGELOG.md` — version history and release-scope notes.
