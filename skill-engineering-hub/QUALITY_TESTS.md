# Quality Tests

## Test 1 — New skill idea should not directly create files

Prompt:
> I want to create a skill for restaurant menu analysis. Start.

Expected:
- Use New Skill Planning mode.
- Output Skill Brief questions or a draft brief.
- Do not directly generate a full skill package unless the user asks after approving the brief.

## Test 2 — Existing skill audit should produce standard compliance report

Prompt:
> Check this existing skill and tell me how to optimize it.

Expected:
- Use Existing Skill Standard Audit mode.
- Check presence of SKILL.md, README, MANIFEST, triggers, output contract, examples, tests.
- Output P0/P1/P2 recommendations.
- Do not claim pressure tests passed unless test results were provided or run.

## Test 3 — Pressure test request should delegate execution to pressure-testing

Prompt:
> Run scenario pressure tests for this skill.

Expected:
- Prepare or call `skill-pressure-testing` workflow.
- Output a pressure-test brief or interpret returned results.
- Do not merge pressure-testing logic into creation planning.

## Test 4 — Toolchain explanation

Prompt:
> How should skill-creator, writing-skill, and pressure-testing work together?

Expected:
- Use Toolchain Flow Design mode.
- Provide stage-by-stage workflow.
- Clearly state that this hub is the coordinator, not the replacement.

## Test 5 — Release gate

Prompt:
> Is this skill ready to publish?

Expected:
- Use Release Gate mode.
- Ask for or inspect package/test results.
- Output release / patch / hold / rollback.
- Include install, trigger, output, safety, regression, and packaging checks.

## Test 6 — Skill IR export requires contracts

Prompt:
> Export this skill to yao-meta-skill. Here is a half-finished idea only.

Expected:
- Use Skill IR Export & Yao Handoff mode.
- Refuse to export because the five contracts are missing.
- Route back to New Skill Planning (Mode A).
- Do not generate skill-ir.json from an undesigned skill.

## Test 7 — Skill IR export produces validated IR

Prompt:
> Here are the five contracts for my skill. Export it to yao for compilation.

Expected:
- Use Skill IR Export & Yao Handoff mode.
- Fill `templates/skill_ir.json` from the contracts.
- Validate with `scripts/validate_ir.py` and report the result honestly.
- Produce handoff checklist + return-map.
- Do not claim yao ran evals unless yao actually ran them.
