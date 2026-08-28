# Pressure Grading Card: split_decision_roles_vs_skills

Mode: with_skill

## User Prompt

这个 skill 里有产品、技术、商业、风险四个角色，是不是要拆成四个 skill？

## Expected Route

architecture_decision

## Expected Output Type

split_recommendation

## Required Patterns

- workflow
- agent
- shared
- Architecture Decision

## Forbidden Patterns

- 每个角色都应该拆成独立 skill

## Assertions



## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
