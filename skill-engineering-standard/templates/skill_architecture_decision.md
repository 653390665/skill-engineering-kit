# Skill Architecture Decision

## 1. Current Need

What user need are we trying to support?

- 

## 2. Candidate Structures

### Option A: Single Skill

Best when:

- one main workflow
- one main output type
- one trigger family
- one safety boundary

Pros:

- 

Cons:

- 

### Option B: Multiple Skills

Best when:

- upstream thinking and downstream execution differ
- trigger families differ
- outputs differ
- different safety boundaries apply
- clean handoff is needed

Pros:

- 

Cons:

- 

### Option C: Skill + Agent Role Cards

Best when:

- the same workflow needs multiple perspectives
- roles should debate or review
- roles should not be independently triggered by users

Pros:

- 

Cons:

- 

### Option D: Skill + Shared Gates

Best when:

- multiple skills need the same evidence, safety, routing, or output rules

Pros:

- 

Cons:

- 

### Option E: Skill + Scripts

Best when:

- validation, packaging, linting, parsing, generation, or testing can be deterministic

Pros:

- 

Cons:

- 

## 3. Decision

Chosen structure:

- 

## 4. Reason

Why this structure?

- 

## 5. Anti-Decision

Why not the other structures?

- 

## 6. Handoff Requirements

If multiple skills are used, what handoff is required?

- 

## 7. Directory Plan

```text
skill-or-system-name/
├─ ...
```

## 8. Risks

| Risk | Mitigation |
|---|---|
|  |  |
