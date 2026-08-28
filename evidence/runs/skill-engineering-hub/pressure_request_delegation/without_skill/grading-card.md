# Pressure Grading Card: pressure_request_delegation

Mode: without_skill

## User Prompt

跑场景压力测试，看看这个 skill 会不会误触发和乱输出。

## Expected Route

Mode C pressure-test preparation or skill-pressure-testing

## Expected Output Type

pressure_test_brief

## Required Patterns

- Pressure Test Brief
- scenario
- acceptance
- skill-pressure-testing

## Forbidden Patterns

- 不用压测
- 直接改 README

## Assertions



## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
