# Skill Types And Split Rules

## Skill vs Agent vs Template vs Script

### Skill

A skill owns a workflow or capability.

Use a skill when users directly ask for a distinct task.

### Agent Role Card

An agent owns a perspective inside a workflow.

Use an agent when the same workflow needs multiple viewpoints.

Do not create one skill per role unless each role has a standalone user-facing workflow.

### Template

A template owns an output shape.

Use templates for repeatable deliverables.

### Shared Gate

A shared gate owns a reusable rule.

Use shared gates when multiple skills need the same evidence, safety, routing, or output rules.

### Script

A script owns deterministic work.

Use scripts for linting, packaging, scoring, converting, parsing, or running repeatable tests.

## Split Into Multiple Skills When

- There are separate user intents.
- The outputs are materially different.
- The workflows have different stages.
- Safety boundaries differ.
- One part is exploratory and another is execution-oriented.
- Clean handoff is needed.
- A single skill becomes too large or unreliable.

## Do Not Split When

- Only the role perspective changes.
- Only the output template changes.
- The steps are part of one cohesive workflow.
- A shared rule can solve the repetition.
- A script can handle deterministic work.

## Recommended Patterns

### Router + Two Skills

Use when one lightweight entry point routes into deep workflows.

Example:

```text
project-discussion-lite → project-cocreation → project-launch
```

### Skill + Agents

Use when a workflow needs roundtable thinking.

Example:

```text
cocreation skill
├─ user researcher agent
├─ product manager agent
├─ risk reviewer agent
└─ facilitator agent
```

### Skill + Shared Gates

Use when multiple skills share quality rules.

Example:

```text
shared/evidence_rubric.md
shared/actionability_gate.md
shared/anti_hallucination_gate.md
```

### Skill + Scripts

Use when release checks or packaging can be automated.
