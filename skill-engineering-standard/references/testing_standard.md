# Testing Standard

## Test Categories

### 1. Happy Path

The skill should trigger and produce the expected output.

### 2. Missing Information

The skill should ask targeted questions or produce a skeleton, not hallucinate.

### 3. Wrong Trigger

The skill should not trigger when another skill is more appropriate.

### 4. Ambiguous Trigger

The skill should either clarify or use the lightest safe path.

### 5. Unsafe Request

The skill should stop or redirect safely.

### 6. Output Contract Pressure

The skill should preserve required output structure.

### 7. Regression

New versions should preserve the strengths of older versions unless intentionally changed.

### 8. Execution Pressure

For task-producing skills, outputs should be directly usable.

## Test Artifact Format

Use this table:

| ID | Prompt | Expected Route | Required Patterns | Forbidden Patterns | Notes |
|---|---|---|---|---|---|

## With-Skill / Without-Skill Comparison

When possible, compare:

- baseline model response
- response with skill

A good skill should improve:

- route accuracy
- evidence discipline
- structure
- safety
- actionability

## Release Threshold

Suggested:

- P0 tests: 100% pass
- P1 tests: >= 90% pass or documented with patch plan
- P2 tests: tracked but not release-blocking
