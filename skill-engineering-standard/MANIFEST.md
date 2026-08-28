# Manifest

## Root Files

- `SKILL.md` — operating instructions for this standard as a skill.
- `README.md` — overview and recommended workflow.
- `QUICK_START.md` — short usage guide.
- `SKILL_ENGINEERING_STANDARD.md` — full standard.
- `QUALITY_TESTS.md` — tests for this standard package.
- `MANIFEST.md` — this file.

## Templates

- `templates/skill_brief.md`
- `templates/skill_audit_brief.md`
- `templates/skill_architecture_decision.md`
- `templates/trigger_contract.md`
- `templates/output_contract.md`
- `templates/quality_test_plan.md`
- `templates/release_gate.md`
- `templates/regression_log.md`
- `templates/versioning_record.md`

## References

- `references/skill_lifecycle_standard.md`
- `references/skill_types_and_split_rules.md`
- `references/directory_standard.md`
- `references/frontmatter_standard.md`
- `references/testing_standard.md`
- `references/packaging_standard.md`
- `references/security_and_governance.md`
- `references/toolchain_workflow.md`

## Examples

- `examples/example_skill_brief.md`
- `examples/example_architecture_decision_reality_project.md`
- `examples/example_trigger_contract.md`
- `examples/example_release_gate.md`

## Scripts

- `scripts/lint_skill_package.py` — lightweight package linter.
- `scripts/build_clean_package.py` — creates a clean install zip with common cache/log exclusions.

## Clean Package Policy

Install packages should not include:

- `__MACOSX/`
- `.DS_Store`
- `__pycache__/`
- `*.pyc`
- `pressure-runs/`
- `codex-run.log`
- local absolute paths

- `CHANGELOG.md` — version history and release-scope notes.
