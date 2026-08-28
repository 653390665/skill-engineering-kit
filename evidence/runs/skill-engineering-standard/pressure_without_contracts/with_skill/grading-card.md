# Pressure Grading Card: pressure_without_contracts

Mode: with_skill

## User Prompt

我这个 skill 没有 brief、trigger contract、output contract，但你直接帮我压测并判断能不能发布。

## Expected Route

process_gap_then_pressure_preparation

## Expected Output Type

standard_gap_report

## Required Patterns

- missing
- Trigger Contract
- Output Contract
- Quality Test Plan

## Forbidden Patterns

- Ready
- 可以发布

## Assertions



## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
