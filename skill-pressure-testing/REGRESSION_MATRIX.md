# Regression Matrix: skill-pressure-testing

Use this matrix after every patch, split, merge, or release-candidate pressure run.

| Version | Change Scope | Scenario / Check | Previous Result | Current Result | Regression? | Required Fix | Re-test Evidence |
|---|---|---|---|---|---|---|---|
| v1.0.1 → v1.0.2 | metadata + governance template | frontmatter parse | pass | pass | no | none | static validation |
| v1.0.1 → v1.0.2 | regression governance | matrix exists | n/a | pass | no | none | file inspection |

## Required Regression Questions

1. Did the patch change trigger behavior?
2. Did the patch change scope routing between static checks, focused scenario tests, and full benchmark runs?
3. Did the patch weaken contamination control?
4. Did the patch make release approval easier without more evidence?
5. Did the patch remove any required report section?
6. Did the patch introduce hidden external dependencies?

## Minimum Evidence Before Release

- Package integrity check passes.
- `SKILL.md` frontmatter parses.
- Required docs are present: `README.md`, `MANIFEST.md`, `QUALITY_TESTS.md`, `PRESSURE_TEST_REPORT.md`.
- Changed files are listed with reason.
- Affected scenarios are re-run or consciously scoped out with justification.

## Decision Vocabulary

- **pass**: no regression observed.
- **patch**: regression exists but can be fixed locally.
- **hold**: release evidence is insufficient.
- **rollback**: patch removes an essential capability from the previous version.
