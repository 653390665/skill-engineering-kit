---
name: skill-engineering-standard
description: Use when planning, creating, splitting, refactoring, reviewing, or preparing to release a ChatGPT/Claude-style skill. This skill standardizes the lifecycle before skill-creator, writing-skill, and pressure-testing are used.
metadata:
  version: "1.0.1"
  updated: "2026-05-16"
---

# Skill Engineering Standard

This skill is a planning and governance layer for creating reliable, maintainable skills.

It should be used before `skill-creator`, before large rewrites, and before pressure testing. Its job is not to write the whole skill immediately; its job is to force a clear design contract first.

## Core Principle

Do not start from `SKILL.md`.

Start from:

1. Skill Brief
2. Architecture Decision
3. Trigger Contract
4. Output Contract
5. Quality Test Plan
6. Release Gate

Only after these are clear should `skill-creator` generate the skill files, `writing-skill` polish the documents, and `skill-pressure-testing` evaluate release readiness.

## Use This Skill When

Use this skill when the user asks to:

- create a new skill
- optimize an existing skill
- decide whether a skill should be split
- build a multi-agent / role-card workflow
- standardize skill creation
- define triggers, boundaries, outputs, or release criteria
- prepare a skill for skill-creator or writing-skill
- organize install packages and audit packages
- create a repeatable skill development process

## Do Not Use This Skill When

Do not use this skill when the user only wants:

- normal writing polish without skill architecture decisions
- pressure testing of a finished skill package
- coding unrelated to skill packaging
- ordinary product strategy unrelated to skill creation

For pressure testing, use `skill-pressure-testing`.
For initial file generation, use `skill-creator` after the planning artifacts are complete.
For wording, README, examples, and documentation polish, use `writing-skill` after architecture is stable.

## Default Workflow

### Step 1: Create Skill Brief

Use `templates/skill_brief.md`.
Clarify the skill's purpose, users, triggers, outputs, boundaries, and likely failure modes.

### Step 2: Make Architecture Decision

Use `templates/skill_architecture_decision.md`.
Decide whether the need should become:

- one skill
- multiple skills
- a router skill
- role cards / agents inside a skill
- shared gates / shared references
- scripts
- an audit companion package

### Step 3: Define Trigger Contract

Use `templates/trigger_contract.md`.
Define positive triggers, negative triggers, ambiguous triggers, adjacent skills, and trigger tests.

### Step 4: Define Output Contract

Use `templates/output_contract.md`.
Define required outputs, forbidden outputs, output structures, evidence rules, and quality bar.

### Step 5: Define Quality Test Plan

Use `templates/quality_test_plan.md`.
Write tests before building the skill:

- happy path
- missing information
- wrong trigger
- unsafe request
- boundary ambiguity
- execution pressure
- regression against previous version

### Step 6: Build With skill-creator

Only after Steps 1-5 are complete, ask `skill-creator` to generate the skill package.

### Step 7: Polish With writing-skill

Use `writing-skill` to polish README, QUICK_START, MANIFEST, examples, and output style.
Do not let writing polish change core architecture without updating the planning artifacts.

### Step 8: Pressure Test

Use `skill-pressure-testing` to test installation, triggers, routing, output quality, regressions, and release readiness.

### Step 9: Release Gate

Use `templates/release_gate.md`.
Decide:

- release
- patch
- hold
- rollback
- archive

### Step 10: Regression Memory

Use `templates/regression_log.md`.
Every failure should become a future test case.

## Skill Type Rules

Use `references/skill_types_and_split_rules.md`.

The most important rule:

> A skill owns a workflow or capability. An agent card owns a perspective. A template owns an output shape. A shared gate owns a reusable rule.

Do not create one skill per role unless each role has an independent user-facing workflow.

## Minimum Package Standard

A mature skill package should include:

```text
skill-name/
├─ SKILL.md
├─ README.md
├─ MANIFEST.md
├─ QUICK_START.md              # optional but recommended
├─ QUALITY_TESTS.md            # recommended
├─ prompts/                    # workflow prompts
├─ templates/                  # output templates
├─ references/                 # deeper guidance
├─ examples/                   # concrete examples
└─ scripts/                    # optional deterministic helpers
```

## Output Rules

When helping users create or optimize a skill, always separate:

- confirmed user requirements
- architecture decisions
- assumptions
- unresolved questions
- recommended files to create
- tests needed before release

Do not jump straight to a finished `SKILL.md` when the skill's purpose, trigger, output, or boundary is still unclear.
