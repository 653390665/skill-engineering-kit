# Skill IR Export & Yao Handoff (Mode G)

Use this prompt when the user asks to export a designed skill to
`yao-meta-skill`, build a Skill IR contract, compile for multiple platforms,
run yao evals, or pull yao release evidence back.

## Pre-flight

Confirm all five contracts exist for the target skill:

- [ ] Skill Brief
- [ ] Architecture Decision
- [ ] Trigger Contract
- [ ] Output Contract
- [ ] Quality Test Plan

If any is missing, stop and route back to New Skill Planning (Mode A) or
Existing Skill Standard Audit (Mode B). Never export an undesigned skill.

## Steps

1. **Read contracts.** Load the five contract files from the target skill's
   `engineering/` directory (or equivalent).

2. **Generate IR.** Fill `templates/skill_ir.json` (schema 2.0.0) using the
   field mapping in `references/yao-bridge.md`:
   - Skill Brief → `job_to_be_done`, `governance.owner`
   - Trigger Contract → `trigger_surface` (positive / negative / edge cases)
   - Trigger tests → `eval_plan.trigger[]`
   - Output Contract → `eval_plan.output[]` (required + forbidden assertions)
   - Quality Test Plan → `eval_plan.adversarial[]`, `eval_plan.baseline`
   - Architecture Decision → `workflow` (steps / decision points / failure modes)
   - Package layout → `resources` (only files that exist)
   - Release Gate → `governance.maturity`
   - Security review → `risk` (output / execution / trust boundary)

3. **Validate.** Run `scripts/validate_ir.py skill-ir.json`. Fix all errors
   before handoff. The script enforces required fields and enums from yao
   schema 2.0.0 and rejects leftover `TODO` placeholders.

4. **Handoff checklist.** Produce a short checklist of what yao will do:
   - compile targets (claude / openai / codex / generic — only requested ones);
   - trigger evals from `eval_plan.trigger[]`;
   - output evals + blind A/B from `eval_plan`;
   - Review Studio 2.0 gate and promotion decision.

5. **Return-map.** State which yao outputs feed back into kit artifacts:
   - `evals/trigger_cases.json` → `tests/scenarios/<skill>/scenarios.yaml`
   - output eval failures → Quality Test Plan "Regression" group
   - `failures/*` → Regression Log entries
   - Review Studio verdict → Release Gate evidence

## Rules

- Never invent IR fields from thin air; empty arrays are fine, fabricated
  content is not.
- If `validate_ir.py` is unavailable, validate required fields manually against
  the mapping table — but do not claim validation without running the check.
- Do not run yao compiler/evals yourself unless the yao-meta-skill package is
  present in the environment; otherwise hand off with the checklist.

## Output shape

```text
IR Export: <skill-name> (schema 2.0.0)
Contracts used: brief / architecture / trigger / output / quality-test-plan
Validation: VALID (scripts/validate_ir.py)  # or list errors
Yao handoff:
  - compile: [targets]
  - evals: trigger / output+blind-A/B / adversarial
  - gate: Review Studio 2.0 + promotion
Return map:
  - trigger_cases.json → scenarios.yaml
  - eval failures → regression group
  - failures library → regression log
  - review verdict → release gate
Next action: <hand off to yao-meta-skill or await user>
```
