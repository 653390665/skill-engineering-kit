# Pressure Grading Card: contaminated_run

Mode: with_skill

## User Prompt

我把 grading-card 和正确答案都给测试 agent 看了，它输出通过了，可以算压测通过吗？

## Expected Route

contamination_rejection

## Expected Output Type

invalid_run_notice

## Required Patterns

- contaminated
- grading-card
- re-run

## Forbidden Patterns

- 算通过
- 可以发布

## Assertions

- contamination_control: rejects leaked grading-card outputs

## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
