# Example Trigger Contract: Skill Pressure Testing

## 1. Skill Name

- `skill-pressure-testing`

## 2. Positive Triggers

Should trigger when the user asks for:

- pressure test this skill
- run a regression test
- compare with-skill and without-skill behavior
- release gate check
- evaluate installability
- check trigger accuracy

## 3. Negative Triggers

Should not trigger when the user asks for:

- create a new skill from scratch
- write a README
- polish wording
- brainstorm a product idea
- execute the business workflow of a skill

## 4. Ambiguous Triggers

| Prompt Pattern | Route |
|---|---|
| Is this skill good? | If package is provided, use light audit; if user asks for pressure test, use pressure-testing. |
| Help me optimize this skill | Use engineering standard first unless explicit pressure test requested. |

## 5. Neighbor Skills

| Neighbor Skill | Overlap | Boundary Rule |
|---|---|---|
| skill-creator | Both handle skills | Creator builds; pressure-testing evaluates. |
| writing-skill | Both improve docs | writing-skill polishes; pressure-testing audits behavior. |
| skill-engineering-standard | Both discuss skill quality | engineering-standard plans; pressure-testing tests. |
