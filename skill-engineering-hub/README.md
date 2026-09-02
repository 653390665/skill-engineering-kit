# Skill Engineering Hub v1.2

`skill-engineering-hub` is an orchestration skill for the full skill engineering workflow.

It does **not** replace:

- `skill-creator` — creates files and directories;
- `writing-skill` — improves documentation and prose;
- `skill-pressure-testing` — runs pressure tests and release checks;
- `skill-engineering-standard` — defines the standard;
- `yao-meta-skill` — optional heavy backend for IR compilation, evals, and governed release.

It coordinates them.

## Core question it answers

> What stage is this skill in, what artifact is missing, and which tool should be used next?

## When to use

Use this skill for:

- planning a new skill before creation;
- auditing an existing skill against a standard;
- preparing pressure-test scenarios;
- interpreting pressure-test reports;
- creating optimization roadmaps;
- deciding whether a skill is ready for release;
- coordinating skill-creator, writing-skill, and skill-pressure-testing;
- exporting a designed skill to yao-meta-skill via Skill IR (Mode G).

## Workflow

```text
Skill idea or existing skill
↓
Skill Engineering Hub
↓
Skill Brief / Architecture Decision / Trigger Contract / Output Contract
↓
skill-creator if files need to be created
↓
writing-skill if docs and examples need editing
↓
skill-pressure-testing if behavior and release quality must be tested
↓
Release Gate / Regression Log
```

### Optional: yao-meta-skill handoff (Mode G)

For multi-platform distribution, provider evals, or governed release, export the
five contracts to `skill-ir.json` (schema 2.0.0) and hand off to yao-meta-skill:

```text
five contracts → skill-ir.json (validate_ir.py) → yao compile + evals + Review Studio
                                     ↓
                    trigger_cases.json → scenarios.yaml
                    eval failures → regression log
                    review verdict → release gate evidence
```

See `references/yao-bridge.md` for the full field mapping and protocols.

## Important distinction

This skill is not the pressure tester itself. It prepares, interprets, and governs pressure testing.

For actual scenario execution, use `skill-pressure-testing`.

## Included artifacts

- planning templates;
- audit templates;
- pressure-test preparation templates;
- optimization report templates;
- release gate templates;
- Skill IR 2.0 export template + validator (`templates/skill_ir.json`, `scripts/validate_ir.py`);
- lightweight scripts for static package linting and report scaffolding.
