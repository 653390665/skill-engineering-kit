# Mode Router

Classify the user's request into exactly one mode:

1. New Skill Planning
2. Existing Skill Standard Audit
3. Pressure-Test Preparation
4. Pressure-Test Result Interpretation
5. Release Gate
6. Toolchain Flow Design

## Routing rules

- If the skill does not exist yet, use New Skill Planning.
- If the skill exists and the user asks what is missing, use Existing Skill Standard Audit.
- If the user asks to design test cases, use Pressure-Test Preparation.
- If the user provides test results and asks what they mean, use Pressure-Test Result Interpretation.
- If the user asks whether to publish, use Release Gate.
- If the user asks how multiple skill tools should work together, use Toolchain Flow Design.

## Ambiguity rule

If the user asks to "optimize a skill", first decide whether they mean:

- optimize the design standard;
- optimize documentation;
- optimize behavior through pressure-test failures;
- optimize package/release quality.

When unclear, give a concise recommendation and proceed with Existing Skill Standard Audit.
