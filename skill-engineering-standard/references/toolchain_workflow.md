# Toolchain Workflow

## Recommended Toolchain

```text
skill-engineering-standard
↓
skill-creator
↓
writing-skill
↓
skill-pressure-testing
↓
release package
```

## Roles

### skill-engineering-standard

Plans:

- purpose
- architecture
- triggers
- output contracts
- quality tests
- release gate

### skill-creator

Builds:

- SKILL.md
- directories
- prompts
- templates
- examples
- scripts

### writing-skill

Polishes:

- README
- QUICK_START
- MANIFEST
- examples
- wording
- user-facing explanations

### skill-pressure-testing

Tests:

- installability
- route accuracy
- output quality
- safety
- regressions
- package cleanliness

## Important Rule

Do not let downstream tools invent upstream design decisions.

If skill-creator or writing-skill reveals an architecture issue, return to the Architecture Decision artifact.

If pressure testing reveals a repeated failure, update the Trigger Contract, Output Contract, or Quality Test Plan.
