# Acceptance Criteria: skill-engineering-standard

## Purpose

- Skill promise: force skill planning, architecture, triggers, outputs, tests, and release gates before creation or major refactor.
- Primary failure it should prevent: jumping straight to a finished `SKILL.md` without a design contract.

## Required Patterns

- Skill Brief
- Architecture Decision
- Trigger Contract
- Output Contract
- Quality Test Plan
- Release Gate
- confirmed requirements / assumptions / unknowns separated

## Forbidden Patterns

- immediately write final SKILL.md
- skip trigger contract
- skip output contract
- release ready without tests
- one skill per role by default

## Route Expectations

| User Request Type | Expected Route | Forbidden Route |
|---|---|---|
| New skill idea | create planning artifacts | final SKILL.md first |
| Existing skill inconsistent | audit brief + fixes | pure prose polish only |
| Split decision | architecture decision | one-role-one-skill default |
| Pressure test without contracts | mark design gap first | invent missing purpose silently |

## Artifact Expectations

- Must point to templates and references already in the package.
- Must not claim behavioral pressure tests passed unless run outputs exist.
