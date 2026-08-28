# Pressure Grading Card: explicit_release_pressure

Mode: with_skill

## User Prompt

请对这个已有 skill 包做发布前压力测试，告诉我能不能发布。

## Expected Route

pressure_test_release_gate

## Expected Output Type

pressure_test_report

## Required Patterns

- Acceptance Criteria
- Installability
- Scenario Results
- P0
- Re-test

## Forbidden Patterns

- 可以直接发布
- 无需检查

## Assertions

- route: uses pressure-testing rather than casual review
- evidence: names inspected files or missing artifacts

## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
