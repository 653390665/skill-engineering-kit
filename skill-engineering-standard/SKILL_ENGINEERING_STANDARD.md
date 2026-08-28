# Skill Engineering Standard v1.0

## 1. Purpose

This standard defines a repeatable workflow for creating, optimizing, testing, and releasing skills.

The goal is to prevent skill creation from becoming a sequence of improvised patches.

A well-engineered skill should have:

- clear trigger boundaries
- clear non-trigger boundaries
- defined output contracts
- explicit failure modes
- test scenarios before release
- package cleanliness
- release decision records
- regression memory

## 2. Core Lifecycle

```text
Intake
↓
Skill Brief
↓
Architecture Decision
↓
Trigger Contract
↓
Output Contract
↓
Quality Test Plan
↓
Build
↓
Writing Polish
↓
Static Review
↓
Pressure Test
↓
Release Gate
↓
Regression Memory
```

## 3. Required Planning Artifacts

Before building or rewriting a skill, create:

1. `skill_brief.md`
2. `skill_architecture_decision.md`
3. `trigger_contract.md`
4. `output_contract.md`
5. `quality_test_plan.md`

For existing skills, also create:

6. `skill_audit_brief.md`
7. `release_gate.md`
8. `regression_log.md`

## 4. Skill Types

### 4.1 Capability Skill

A skill that performs a defined capability.

Examples:

- create a spreadsheet
- generate a slide deck
- edit a PDF
- transform a project idea into a BP draft

### 4.2 Workflow Skill

A skill that controls a multi-step process.

Examples:

- project co-creation
- product launch planning
- legal document review workflow

### 4.3 Router Skill

A skill that classifies intent and routes to other skills or modes.

Example:

- quick project discussion / triage skill

### 4.4 QA / Pressure Skill

A skill that tests other skills.

Example:

- skill-pressure-testing

### 4.5 Agent Role Card

A role inside a workflow skill, not necessarily a standalone skill.

Examples:

- user researcher
- product manager
- risk reviewer
- investor judge

### 4.6 Shared Gate

A reusable rule used by multiple skills.

Examples:

- evidence rubric
- anti-hallucination gate
- actionability gate
- output structure router

## 5. Split Rules

Split into multiple skills when:

- user intent differs sharply
- trigger phrases differ sharply
- outputs differ sharply
- safety boundaries differ sharply
- upstream thinking and downstream execution need different workflows
- one skill becomes too large to reliably trigger or maintain
- separate teams or phases need clean handoff

Do not split when:

- the only difference is a role perspective
- the only difference is an output template
- the steps belong to the same workflow
- a shared rule can solve the repetition

## 6. Standard Directory

Recommended package structure:

```text
skill-name/
├─ SKILL.md
├─ README.md
├─ QUICK_START.md
├─ MANIFEST.md
├─ QUALITY_TESTS.md
├─ prompts/
├─ templates/
├─ references/
├─ examples/
└─ scripts/
```

Minimum package structure:

```text
skill-name/
├─ SKILL.md
└─ README.md
```

But mature workflow skills should include tests, examples, and manifest files.

## 7. SKILL.md Standard

`SKILL.md` should include:

- frontmatter
- purpose
- when to use
- when not to use
- default workflow
- what to read
- output rules
- stop conditions
- handoff rules, if applicable

It should not include every large template. Use progressive disclosure:

- core rules in `SKILL.md`
- deeper explanation in `references/`
- reusable outputs in `templates/`
- behavior examples in `examples/`
- deterministic checks in `scripts/`

## 8. Frontmatter Standard

Use minimal safe frontmatter:

```yaml
---
name: skill-name
description: Use when ...
---
```

Optional metadata is allowed only if the target environment supports it.
If compatibility is uncertain, keep version information inside README and MANIFEST, not in frontmatter.

## 9. Trigger Contract Standard

Every skill should define:

- positive triggers
- negative triggers
- ambiguous triggers
- adjacent skills
- trigger tests
- examples of wrong triggers

A skill is not ready if it cannot explain when not to trigger.

## 10. Output Contract Standard

Every skill should define:

- required sections
- forbidden sections
- quality bar
- evidence labels
- success signals
- failure signals
- preferred structures

Outputs should be designed before the skill is generated.

## 11. Testing Standard

A skill should have tests for:

- happy path
- missing information
- wrong trigger
- ambiguous trigger
- unsafe request
- output contract failure
- regression against previous version
- execution pressure, if task-oriented

## 12. Release Standard

Before release, verify:

- installability
- valid frontmatter
- clean package
- no local logs
- no cache files
- no local absolute paths
- trigger behavior
- output behavior
- safety behavior
- regression behavior

## 13. Clean Package Standard

Install packages should exclude:

- `__MACOSX/`
- `.DS_Store`
- `__pycache__/`
- `*.pyc`
- logs
- pressure runs
- local absolute paths
- credentials
- API keys

Audit packages may include logs and test runs, but should still remove credentials and sensitive local paths.

## 14. Governance Rule

Every pressure test failure should become one of:

- a trigger contract update
- an output contract update
- a template update
- a test scenario
- a release gate condition
- a regression log entry

If the same failure happens twice, the standard should be updated.
