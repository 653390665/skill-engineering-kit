# Skill Engineering Standard v1.0

A lightweight engineering standard for planning, creating, reviewing, testing, and releasing skills.

It is designed to work with:

- `skill-creator` — generates the skill package after planning is complete.
- `writing-skill` — polishes README, examples, docs, and output wording.
- `skill-pressure-testing` — validates triggers, routing, safety, output quality, and release readiness.

## Why This Exists

Without a standard, skill creation becomes a loop of improvised steps:

```text
idea → generate SKILL.md → notice boundary issues → add templates → add tests → discover trigger conflicts → patch → retest → patch again
```

This package changes the workflow to:

```text
Skill Brief → Architecture Decision → Trigger Contract → Output Contract → Quality Test Plan → Build → Polish → Pressure Test → Release Gate
```

## Recommended Use

Use this package before creating or heavily modifying a skill.

1. Fill `templates/skill_brief.md`.
2. Fill `templates/skill_architecture_decision.md`.
3. Fill `templates/trigger_contract.md`.
4. Fill `templates/output_contract.md`.
5. Fill `templates/quality_test_plan.md`.
6. Ask `skill-creator` to generate files based on those artifacts.
7. Ask `writing-skill` to polish docs and examples.
8. Run `skill-pressure-testing` before release.
9. Fill `templates/release_gate.md`.
10. Record failures in `templates/regression_log.md`.

## Package Contents

```text
skill-engineering-standard-v1.0/
├─ SKILL.md
├─ README.md
├─ QUICK_START.md
├─ MANIFEST.md
├─ SKILL_ENGINEERING_STANDARD.md
├─ QUALITY_TESTS.md
├─ templates/
├─ references/
├─ examples/
└─ scripts/
```

## Core Rule

Do not write the final skill before defining its contract.

A skill contract includes:

- what triggers it
- what must not trigger it
- what it outputs
- what it must never output
- what tests it must pass
- how it will be released

## Relationship to Other Tools

| Tool / Skill | Role | What it should do | What it should not do |
|---|---|---|---|
| skill-engineering-standard | Architect / standard setter | Plan, split, define triggers, outputs, tests, release gates | Replace creator or pressure testing |
| skill-creator | Builder | Generate the package and file structure | Decide architecture alone |
| writing-skill | Editor | Improve clarity, examples, README, narrative | Change core architecture silently |
| skill-pressure-testing | QA / release gate | Test, score, compare, audit | Invent missing product intent |

## Version

v1.0 — first stable planning standard.
