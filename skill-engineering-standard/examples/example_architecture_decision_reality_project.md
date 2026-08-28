# Example Architecture Decision: Reality Project Skills

## 1. Current Need

The user wants a system that can both:

1. discuss and refine vague project ideas
2. turn mature ideas into MVP, validation plans, product specs, and development tasks

## 2. Candidate Structures

### Option A: Single Skill

Rejected.

Reason: discussion, BP writing, validation, product spec, and development tasks have different triggers, outputs, and risk boundaries.

### Option B: Multiple Skills

Accepted.

Use:

- `reality-project-cocreation`
- `reality-project-launch`

### Option C: Skill + Agent Role Cards

Accepted inside `cocreation`.

Use agents:

- facilitator
- user researcher
- user psychologist
- product manager
- business model advisor
- market researcher
- competitor analyst
- investor judge
- risk reviewer
- execution PM

### Option D: Skill + Shared Gates

Accepted.

Use shared gates:

- evidence rubric
- actionability gate
- anti-hallucination gate
- structure router

### Option E: Skill + Scripts

Useful for audit packages, but not mandatory for install package.

## 3. Decision

Use a two-skill system with shared gates and agent role cards.

```text
Reality Project Skills
├─ shared/
├─ reality-project-cocreation/
└─ reality-project-launch/
```

## 4. Reason

`cocreation` owns exploration and project maturity.
`launch` owns validation, product spec, and development tasks.

## 5. Anti-Decision

Do not create one skill per role. Roles are perspectives inside the co-creation workflow, not standalone user-facing tasks.

## 6. Handoff Requirements

Use `cocreation_handoff.md` with:

- confirmed user facts
- AI deductions
- assumptions
- target users
- product direction
- business loop
- risks
- minimum developable task summary

## 7. Risks

| Risk | Mitigation |
|---|---|
| User does not know which skill to use | QUICK_START and router rules |
| Launch restarts business discussion | handoff reader + launch router |
| Development task too weak | 13-section task pack |
