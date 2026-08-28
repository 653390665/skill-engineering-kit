# Skill Lifecycle Standard

## Stage 0: Intake

Clarify the user need and current context.

Questions:

- What is the user trying to accomplish?
- Is this a skill, a prompt, a template, a script, or documentation?
- Is the need one workflow or multiple workflows?
- Is this for personal use, team use, or public release?

## Stage 1: Skill Brief

Create `templates/skill_brief.md`.

Do not write the final `SKILL.md` until the brief is clear.

## Stage 2: Architecture Decision

Create `templates/skill_architecture_decision.md`.

Decide whether to use:

- one skill
- multiple skills
- router skill
- agent role cards
- shared gates
- scripts
- audit package

## Stage 3: Trigger Contract

Create `templates/trigger_contract.md`.

A skill without negative triggers is not ready.

## Stage 4: Output Contract

Create `templates/output_contract.md`.

Define output structures before generating skill files.

## Stage 5: Quality Test Plan

Create `templates/quality_test_plan.md`.

Write tests before finalizing templates and examples.

## Stage 6: Build

Use skill-creator or manual creation to generate:

- SKILL.md
- README.md
- prompts/
- templates/
- references/
- examples/
- scripts/

## Stage 7: Writing Polish

Use writing-skill to improve clarity.

Do not let writing polish change core contracts unless the contracts are updated.

## Stage 8: Static Review

Check:

- frontmatter
- directory structure
- broken references
- cache/log files
- local paths
- missing examples

## Stage 9: Pressure Test

Use skill-pressure-testing.

Test:

- trigger behavior
- routing behavior
- output behavior
- safety
- regressions
- task execution quality

## Stage 10: Release Gate

Use `templates/release_gate.md`.

Release only if P0 is clear and P1 is acceptable or documented.

## Stage 11: Regression Memory

Every failure becomes a future test case.
