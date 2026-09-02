# Quick Start

## I want to create a new skill (kit-first path)

Use this order when you want the design discipline layer to lead:

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

## I want to create a skill (yao mainline path)

`yao-meta-skill` is the creation mainline. When you just say "create a skill
from this workflow" or "improve this skill", the mainline is:

```bash
# inside yao-meta-skill (Python 3.10+; use python3.13 on macOS)
python3 scripts/yao.py quickstart <skill_dir>        # intent dialogue → package
python3 scripts/yao.py skill-ir <skill_dir>          # model once (Skill IR 2.0)
python3 scripts/yao.py compile-skill <skill_dir> --target claude --target generic
python3 scripts/yao.py output-eval <skill_dir>       # trigger + output evals
python3 scripts/yao.py review-studio <skill_dir>     # one-page release gate
```

Use this kit as the supplement around that mainline:

- idea vague? run `skill-engineering-hub` Mode A first (five contracts);
- contracts ready? run Mode G to export them into `skill-ir.json` for the mainline;
- review keeps failing? feed `output-eval` failures into the Regression Log,
  then re-run Mode A to tighten the contracts.

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
