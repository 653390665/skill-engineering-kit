# Quality Tests For Skill Engineering Standard

## Test 1: New Skill Request

### Prompt

I want to create a new skill that helps users plan local marketing campaigns.

### Expected Behavior

- Do not immediately write final `SKILL.md`.
- Ask for or draft a Skill Brief.
- Recommend Architecture Decision, Trigger Contract, Output Contract, and Quality Test Plan.

## Test 2: Split Decision

### Prompt

This skill handles brainstorming, business plan writing, MVP validation, and Codex task creation. Should it be split?

### Expected Behavior

- Use `skill_architecture_decision.md`.
- Identify whether workflows, outputs, triggers, and safety boundaries differ.
- Recommend skill / agent / shared gate split rather than one-role-one-skill.

## Test 3: Trigger Confusion

### Prompt

My skill keeps triggering when users only ask for ordinary writing polish.

### Expected Behavior

- Create or update Trigger Contract.
- Define negative triggers and adjacent skill boundaries.
- Add trigger test cases.

## Test 4: Existing Skill Optimization

### Prompt

This skill works, but the README, examples, and tests are inconsistent.

### Expected Behavior

- Use Skill Audit Brief.
- Separate architecture issues from writing issues.
- Recommend writing-skill for docs after output contracts are stable.
- Recommend pressure test after edits.

## Test 5: Release Readiness

### Prompt

Can I release this skill package?

### Expected Behavior

- Use Release Gate.
- Check installability, frontmatter, clean package, tests, safety, regression.
- Return Release / Patch / Hold / Rollback.

## Test 6: Pressure Testing Timing

### Prompt

I want to pressure test this skill, but it has no Skill Brief, no trigger contract, and no output contract.

### Expected Behavior

- Do not invent missing intent during pressure testing.
- Mark missing design artifacts as a process gap.
- Recommend completing planning artifacts before high-confidence pressure testing.
