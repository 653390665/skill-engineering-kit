# Quick Start

## I want to create a new skill

Use this order:

1. Use `skill-engineering-hub` to generate:
   - Skill Brief
   - Architecture Decision
   - Trigger Contract
   - Output Contract
   - Quality Test Plan
2. Use `skill-creator` to create the skill files.
3. Use `writing-skill` to polish README, examples, and user-facing docs.
4. Use `skill-pressure-testing` to pressure test.
5. Use `skill-engineering-hub` again to interpret failures and decide release status.

## I already have a skill and want to optimize it

Use this order:

1. Use `skill-engineering-hub` for standard audit.
2. Use `skill-pressure-testing` for behavior and regression tests.
3. Use `skill-engineering-hub` to convert failures into a P0/P1/P2 optimization roadmap.
4. Use `writing-skill` or `skill-creator` to apply fixes.
5. Re-run pressure testing.

## I only want to run tests

Use `skill-pressure-testing` directly.

## I only want to improve documentation

Use `writing-skill` directly.

## I only want to create files from an already-approved brief

Use `skill-creator` directly.

## I want to hand a designed skill to yao-meta-skill (compile / evals / release)

1. Make sure the skill has completed all five contracts:
   Skill Brief, Architecture Decision, Trigger Contract, Output Contract, Quality Test Plan.
2. Use `skill-engineering-hub` in **Mode G — Skill IR Export & Yao Handoff**.
3. It generates `skill-ir.json` (schema 2.0.0) and validates it with `scripts/validate_ir.py`.
4. Hand off to `yao-meta-skill`: compile targets, run trigger/output evals, Review Studio 2.0.
5. Pull evidence back: trigger cases → your scenarios, eval failures → regression log,
   Review Studio verdict → release gate.

> Principle: kit designs, yao engineers. Export only after contracts exist — a skill
> that cannot be exported to IR is probably not designed yet.
