# External Patterns To Borrow

Before inventing a new testing shape for a complex skill, check whether GitHub or adjacent eval tools already contain a pattern worth borrowing. Do not copy whole frameworks by default. Extract the smallest useful mechanism.

## Search Targets

Use these query shapes:

- `github agent skills eval with_skill without_skill`
- `github agent skill tests acceptance criteria scenarios.yaml`
- `github prompt eval red team agent skills`
- `github skill scanner prompt injection agent skills`
- `github skill benchmark trigger validation`

## Patterns Worth Borrowing

## Borrowed Design Decisions For This Skill

This skill adopts five design choices from the ecosystem:

- Acceptance criteria are written before scenarios.
- Scenarios include required and forbidden patterns.
- Major rewrites use with-skill / without-skill comparison.
- Reports preserve run artifacts or at least cite exact inspected files and outputs.
- Security scanning is a separate release layer, not a substitute for behavior testing.

### 1. With-Skill / Without-Skill Comparison

Borrow from agent skill eval tools such as:

- `darkrishabh/agent-skills-eval`
- `caohaotiantian/agent-skills-eval`

Use when the question is: "Did the skill actually improve behavior?"

Apply as:

- same prompt
- same model or agent harness
- one run with the skill
- one run without the skill
- same assertions
- compare not just score, but exact failure mode

Do not treat a better-looking answer as improvement unless it fixes the targeted failure.

### 2. Acceptance Criteria + Scenario Files

Borrow from repositories such as:

- `microsoft/skills`

Use when the skill produces code, product specs, task packs, or other structured artifacts.

Apply as:

- create an acceptance criteria file that names correct and incorrect patterns
- create scenario cases for basic usage, error handling, and advanced usage
- score generated outputs against criteria rather than general quality

For non-code skills, translate "correct import patterns" into the domain's equivalent: correct route, correct template, correct evidence label, correct refusal, or correct handoff.

### 3. Red-Team And Prompt Eval Harnesses

Borrow from tools such as:

- `promptfoo/promptfoo`

Use when the skill governs prompts, agents, RAG, safety behavior, or user-facing AI workflows.

Apply as:

- define adversarial prompts
- define assertions
- compare variants
- keep reports as artifacts
- add CI only after the scenario set is stable

Do not use generic jailbreak suites alone. Skill tests need domain-specific failures.

### 4. Skill Security Scanning

Borrow from tools such as:

- `cisco-ai-defense/skill-scanner`
- `snyk/agent-scan`
- `getsentry/skills/skills/skill-scanner`
- `skill-issue`

Use when installing, publishing, or reviewing skills from another source.

Apply as:

- scan for prompt injection
- scan for credential access
- scan for network exfiltration
- scan scripts for dangerous commands
- inspect hidden characters or obfuscated text when suspicion exists

A clean scan is not proof of safety. Treat it as one input, then still read high-risk files.

### 5. Real Task Benchmarks

Borrow from benchmark-style work such as SWE skill benchmarks and task-verifier harnesses.

Use when the skill claims practical execution value.

Apply as:

- pin a real task
- define acceptance criteria before running
- let the agent produce an artifact
- verify with tests, file inspection, or a domain-specific checker

For development skills, at least one pressure test should result in code that is actually built or tested.

## When To Skip External Search

Skip or keep it light when:

- the skill is tiny and single-purpose
- the user asked for a quick local edit
- no release or broad reuse is planned
- the skill has no safety, routing, execution, or handoff risk

If skipped, say why in the pressure report.

## Source Discipline

When citing an external pattern in a report:

- include repository or documentation URL
- name the borrowed mechanism
- state what was not adopted
- avoid claiming the external project proves your skill is good

External projects inspire test design. Your own scenarios prove the skill.
