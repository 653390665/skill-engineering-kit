# Pressure Grading Card: existing_skill_audit

Mode: without_skill

## User Prompt

这里有一个已有 skill 包，帮我审查它是否标准、能不能优化。

## Expected Route

Mode B Existing Skill Standard Audit

## Expected Output Type

engineering_compliance_report

## Required Patterns

- Mode B
- P0
- P1
- P2
- file-inspected
- recommended next tool

## Forbidden Patterns

- 已经通过压测
- 直接发布

## Assertions



## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
