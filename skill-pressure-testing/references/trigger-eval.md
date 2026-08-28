# Trigger Evaluation

Trigger failures are common: the skill either fails to activate when needed, or activates when another skill would be better.

## Test Set

Create three groups.

### 1. Positive Triggers

Requests that should use the skill.

Examples:

- "Evaluate this skill before release."
- "Pressure test this prompt workflow."
- "Compare v1 and v2 of this skill."
- "Does this skill still fail under edge cases?"

### 2. Negative Triggers

Nearby requests that should not use the skill.

Examples:

- "Create a new skill from scratch." Use `skill-creator`.
- "Write a failing baseline before designing the skill." Use `writing-skills`.
- "Run tests for this app." Use testing skills.
- "Review this PR." Use code review.

### 3. Ambiguous Triggers

Requests where the agent should choose a light route or ask one question.

Examples:

- "Is this skill okay?"
- "Can we improve this prompt?"
- "Should this workflow become a skill?"

## Precision / Recall Table

```md
| Prompt | Expected | Actual | Result | Notes |
|---|---|---|---|---|
|  | use skill |  | PASS/FAIL |  |
|  | do not use skill |  | PASS/FAIL |  |
```

## Decoy Skill Method

When possible, include competing skills in the evaluation:

- `skill-creator`
- `writing-skills`
- `prompt-engineer`
- `testing`
- `code-reviewer`

Pass behavior:

- Uses `skill-pressure-testing` for evaluation, release, regression, and pressure scenarios.
- Uses `skill-creator` for structure and creation.
- Uses `writing-skills` for baseline RED/GREEN/REFACTOR.
- Uses domain skills for normal implementation or app testing.

## Failure Patterns

- Over-trigger: every "skill" request becomes pressure testing.
- Under-trigger: release or regression request is treated as casual review.
- Shortcut: agent reads the description and skips the full skill body.
- Wrong sibling: agent uses `writing-skills` when the task is post-build pressure testing.

## Fixes

- Add specific trigger words to the description.
- Add explicit adjacent non-use examples.
- Add route rules in `SKILL.md`.
- Add decoy scenarios to `QUALITY_TESTS.md`.
