# Mode Router

Classify the user's request into exactly one mode:

1. New Skill Planning
2. Existing Skill Standard Audit
3. Pressure-Test Preparation
4. Pressure-Test Result Interpretation
5. Release Gate
6. Toolchain Flow Design
7. Skill IR Export & Yao Handoff

## Routing rules

- If the skill does not exist yet, use New Skill Planning.
- If the skill exists and the user asks what is missing, use Existing Skill Standard Audit.
- If the user asks to design test cases, use Pressure-Test Preparation.
- If the user provides test results and asks what they mean, use Pressure-Test Result Interpretation.
- If the user asks whether to publish, use Release Gate.
- If the user asks how multiple skill tools should work together, use Toolchain Flow Design.
- If the user asks to export a skill to yao-meta-skill, build Skill IR, compile for multiple platforms, run yao evals, or pull yao release evidence, use Skill IR Export & Yao Handoff.

## Ambiguity rule

If the user asks to "optimize a skill", first decide whether they mean:

- optimize the design standard;
- optimize documentation;
- optimize behavior through pressure-test failures;
- optimize package/release quality.

When unclear, give a concise recommendation and proceed with Existing Skill Standard Audit.

## Mode G pre-check

Before exporting to Skill IR, confirm all five contracts exist:

- Skill Brief
- Architecture Decision
- Trigger Contract
- Output Contract
- Quality Test Plan

If any contract is missing, route back to New Skill Planning or Existing Skill Standard Audit first. Never export a skill that has not been designed.
