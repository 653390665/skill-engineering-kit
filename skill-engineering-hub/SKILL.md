---
name: skill-engineering-hub
description: Use when the user wants to plan, standardize, audit, pressure-test, or optimize a skill engineering workflow. This skill coordinates skill-creator, writing-skill, skill-engineering-standard, and skill-pressure-testing by producing creation briefs, architecture decisions, trigger/output contracts, quality test plans, pressure-test briefs, optimization reports, and release decisions. It does not replace skill-creator for generating files, writing-skill for prose polishing, or skill-pressure-testing for scenario execution.
metadata:
  version: "1.0.0"
  updated: "2026-05-16"
---

# Skill Engineering Hub

## Purpose

This skill is the orchestration layer for a skill engineering workflow.

Use it to decide **what stage a skill is in**, choose the correct next action, and generate the correct planning, audit, pressure-test, or optimization artifact.

It coordinates four roles:

1. **skill-engineering-standard** — defines what a good skill must contain.
2. **skill-creator** — creates the skill files and directory structure.
3. **writing-skill** — improves documentation, examples, and user-facing wording.
4. **skill-pressure-testing** — runs pressure tests, regression checks, safety checks, and release gates.

This skill should not try to replace those tools. It decides when and how to use them.

---

## When to use this skill

Use this skill when the user asks to:

- create a new skill in a standardized way;
- plan a skill before using skill-creator;
- decide whether one skill should be split into multiple skills, role agents, shared gates, scripts, or templates;
- audit an existing skill against engineering standards;
- prepare a pressure-test plan for an existing skill;
- interpret pressure-test results and turn them into an optimization plan;
- decide whether a skill is ready for release;
- build a clean install package and/or audit package plan;
- coordinate skill-creator, writing-skill, and skill-pressure-testing.

---

## Do not use this skill when

Do not use this skill for:

- writing the full business content of a non-skill project;
- replacing skill-creator when the user directly asks to generate skill files;
- replacing writing-skill when the user only asks to polish README or examples;
- replacing skill-pressure-testing when the user only asks to execute a concrete scenario pressure run;
- modifying a target skill silently without producing an audit or optimization plan;
- making unsupported claims that a skill passed tests without inspecting files or test outputs.

---

## Core workflow router

Choose exactly one of these modes unless the user explicitly asks for an end-to-end workflow.

### Mode A — New Skill Planning

Use when the skill does not exist yet or the user only has an idea.

Output:

- Skill Brief
- Architecture Decision
- Trigger Contract
- Output Contract
- Quality Test Plan
- recommended next tool: skill-creator

Never start with SKILL.md directly unless the user already provided a brief.

### Mode B — Existing Skill Standard Audit

Use when a skill already exists and the user wants to know whether it is standard, complete, maintainable, or optimized.

Output:

- Engineering Compliance Report
- missing artifacts
- architecture risks
- trigger/output risks
- P0/P1/P2 fix list
- recommended next tool: writing-skill, skill-creator, or skill-pressure-testing depending on the problem

### Mode C — Pressure-Test Preparation

Use when the skill exists but pressure-test scenarios are missing or incomplete.

Output:

- Pressure Test Brief
- scenario matrix
- required/forbidden patterns
- pass/fail criteria
- regression seeds
- recommended next tool: skill-pressure-testing

### Mode D — Pressure-Test Result Interpretation

Use when the user already has a pressure-test report and wants to know what to fix.

Output:

- test result summary
- failure classification
- root cause analysis
- optimization roadmap
- regression updates
- release decision

### Mode E — Release Gate

Use when the user asks whether a skill can be released or packaged.

Output:

- release decision: release / patch / hold / rollback
- install package checklist
- audit package checklist
- versioning note
- regression log update

### Mode F — Toolchain Flow Design

Use when the user asks how skill-creator, writing-skill, pressure-testing, and standard/guideline skills should work together.

Output:

- stage-by-stage workflow
- tool responsibility table
- handoff artifacts
- failure recovery process

---

## Required standards

Always separate:

- user-confirmed facts;
- file-inspected facts;
- AI deductions;
- assumptions;
- unknowns.

Never say a package is installable, tested, or clean unless files or test results were inspected.

Every optimization recommendation must include:

- issue;
- why it matters;
- affected file or artifact;
- fix direction;
- priority: P0 / P1 / P2;
- regression test to add.

---

## Standard artifact sequence

For new skill creation, require this sequence:

1. Skill Brief
2. Architecture Decision
3. Trigger Contract
4. Output Contract
5. Quality Test Plan
6. skill-creator generation
7. writing-skill documentation pass
8. skill-pressure-testing run
9. Release Gate
10. Regression Log

---

## Output style

Be direct and operational. Prefer checklists, contracts, matrices, and P0/P1/P2 fix lists.

Do not over-generate. If the user asks for planning, do not create the full skill. If the user asks for pressure-test execution, do not rewrite the skill.
