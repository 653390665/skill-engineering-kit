# Pressure Grading Card: creation_decoy

Mode: with_skill

## User Prompt

帮我创建一个餐厅菜单分析 skill，从零开始生成。

## Expected Route

skill_planning_or_creation

## Expected Output Type

route_explanation_or_creation_brief

## Required Patterns

- 创建
- 规划
- 压力测试

## Forbidden Patterns

- Scenario Results
- with-skill
- without-skill

## Assertions

- trigger_precision: does not use pressure testing before a skill exists

## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
