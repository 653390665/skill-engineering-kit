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
