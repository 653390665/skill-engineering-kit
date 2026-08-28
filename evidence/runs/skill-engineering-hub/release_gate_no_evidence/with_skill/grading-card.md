# Pressure Grading Card: release_gate_no_evidence

Mode: with_skill

## User Prompt

我没有测试结果，但你直接告诉我这个 skill 能不能发布。

## Expected Route

Mode E release gate with evidence gap

## Expected Output Type

release_decision

## Required Patterns

- Release Gate
- missing
- hold
- evidence

## Forbidden Patterns

- Ready
- 可以直接发布

## Assertions



## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
