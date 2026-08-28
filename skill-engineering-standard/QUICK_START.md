# Quick Start

## If You Want To Create A New Skill

Start here:

1. `templates/skill_brief.md`
2. `templates/skill_architecture_decision.md`
3. `templates/trigger_contract.md`
4. `templates/output_contract.md`
5. `templates/quality_test_plan.md`

Then pass those artifacts to `skill-creator`.

## If You Want To Optimize An Existing Skill

Start here:

1. `templates/skill_audit_brief.md`
2. `templates/trigger_contract.md`
3. `templates/output_contract.md`
4. `templates/release_gate.md`

Then run `skill-pressure-testing`.

## If You Are Unsure Whether To Split A Skill

Use:

- `templates/skill_architecture_decision.md`
- `references/skill_types_and_split_rules.md`

Rule of thumb:

- Split into multiple skills when workflows, triggers, outputs, or safety boundaries differ.
- Use agents / role cards when the same workflow needs multiple perspectives.
- Use shared gates when multiple skills need the same rule.
- Use scripts when the task is deterministic and repeatable.

## If You Want A Clean Release Package

Use:

- `templates/release_gate.md`
- `references/packaging_standard.md`
- `scripts/lint_skill_package.py`
- `scripts/build_clean_package.py`

## Minimal Creation Flow

```text
Skill Brief
↓
Architecture Decision
↓
Trigger Contract
↓
Output Contract
↓
Quality Tests
↓
skill-creator
↓
writing-skill
↓
skill-pressure-testing
↓
Release Gate
```
