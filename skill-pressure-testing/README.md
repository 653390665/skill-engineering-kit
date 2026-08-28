# Skill Pressure Testing v1.0.1

This skill is used when a user explicitly asks to pressure test, stress test, benchmark, compare with/without skill behavior, run regression scenarios, or prepare a release gate for a skill package.

It is not a general skill-creation or writing-polish skill. Its job is to prove whether an existing skill behaves correctly under realistic pressure.

## Core Use

Use this skill after a skill package already exists and after its basic intent, trigger boundary, output contract, and quality tests are at least partially defined.

The normal flow is:

1. Inspect the target skill package.
2. Define the target skill's promise.
3. Write acceptance criteria before scenarios.
4. Design realistic pressure scenarios.
5. Run installability and metadata checks first.
6. Run with-skill / without-skill only for release, major rewrite, or explicit benchmark requests.
7. Score outputs against required and forbidden patterns.
8. Patch the smallest observed loophole.
9. Re-test affected scenarios.
10. Record release decision and remaining risks.

## Included Resources

- `SKILL.md`: trigger rules, scope router, required test categories, and release stop conditions.
- `references/`: pressure-test method, scenario patterns, grading rubric, trigger evaluation, security scan, report template, and release checklist.
- `scripts/`: deterministic helpers for package validation, run scaffolding, output status, scoring, and template consistency checks.
- `tests/scenarios/skill-pressure-testing/`: baseline acceptance criteria and machine-readable scenarios for this skill itself.
- `QUALITY_TESTS.md`: human-readable quality tests.
- `PRESSURE_TEST_REPORT.md`: current optimization report.

## Clean Package Rule

Do not include macOS metadata, `__pycache__`, `.pyc`, run logs, or local absolute paths in the install package.

Use a separate audit or pressure-run package for large logs and historical outputs.
