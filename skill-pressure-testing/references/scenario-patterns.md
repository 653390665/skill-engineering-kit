# Scenario Patterns

Use these patterns to design tests. Select the smallest set that attacks the skill's real risk.

Before writing cases, create acceptance criteria with concrete required and forbidden patterns. For machine-readable tests, mirror `test-artifact-design.md`.

## 1. Installability Scenario

Purpose: catch package failures before behavior testing.

Checks:

- frontmatter has only allowed fields
- `name` matches folder name
- required files exist
- referenced resources exist
- sibling folders are documented
- zip or package passes integrity test

Failure examples:

- top-level `version` or `updated` breaks installation
- skill references `../shared` but install instructions omit shared folder
- generated package misses examples or templates

## 2. Trigger Scenario

Purpose: test whether the skill activates at the right time.

Use:

- one obvious trigger
- one adjacent non-trigger
- one ambiguous request

Pass behavior:

- obvious trigger uses the skill
- adjacent non-trigger uses a better skill or no skill
- ambiguous request asks one clarifying question or chooses the lighter route

## 3. Router Scenario

Purpose: test internal mode selection.

Use when the skill has modes such as quick/deep, co-creation/launch, research/write, scan/fix.

Pressure examples:

- user asks for a large output too early
- user asks for execution before evidence exists
- user mixes exploratory and executable language

Pass behavior:

- selects the right route
- states why briefly
- does not run the whole workflow when one step is enough

## 4. Missing Evidence Scenario

Purpose: stop confident claims from weak inputs.

Pressure examples:

- "Write a formal BP from this one-sentence idea."
- "This market has no competitors, help me price it."
- "Users will definitely pay, design the MVP."

Pass behavior:

- separates user-confirmed facts, AI deductions, assumptions, unknowns, and search-needed facts
- outputs a skeleton, validation plan, or search brief instead of pretending certainty

## 5. Boundary Scenario

Purpose: test refusal, narrowing, or safer alternatives.

Pressure examples:

- growth hacks that imply spam
- medical, legal, financial, or child-related claims
- requests to skip consent, validation, or data handling constraints

Pass behavior:

- names the blocked behavior
- gives a safe alternative route
- avoids laundering the same action through softer wording

## 6. Regression Scenario

Purpose: compare new version against old strengths.

Use when:

- replacing a first version
- splitting one skill into multiple skills
- adding agent roles or routers
- merging two workflows

Pass behavior:

- identifies old strengths worth preserving
- identifies new strengths
- names tradeoffs
- patches the new version when it loses execution quality, speed, or clarity

## 7. Execution Scenario

Purpose: test whether output can be acted on.

Use when the skill produces:

- development task packs
- product specs
- validation tasks
- research briefs
- checklists
- implementation plans

Pass behavior:

- has scope and non-scope
- has inputs and outputs
- has states and errors where relevant
- has test cases
- has acceptance criteria
- can be handed to a fresh agent without re-explaining intent

## 7.1 Execution Replay Scenario

Purpose: test whether an execution artifact survives actual implementation, not just inspection.

Use when the skill produces development tasks, scripts, specs, or operational runbooks.

Flow:

1. Use the skill to generate the task pack or spec.
2. Give only that artifact to a fresh coding agent.
3. Ask it to implement the smallest version.
4. Run the task's own test cases or acceptance criteria.
5. Record where the implementer had to guess.

Pass behavior:

- the implementer can proceed without hidden context
- the artifact names scope, non-scope, inputs, outputs, states, errors, tests, and done definition
- verification can be run without inventing new acceptance criteria

## 8. Template Consistency Scenario

Purpose: catch drift between tests, auditors, templates, and examples.

Pressure examples:

- tests require a `Done Definition`, but the template omits it
- auditor demands `state design`, but examples do not show it
- a 13-section task template has a stray top-level appendix that looks like section 14

Pass behavior:

- required fields appear in every relevant file
- fixed section counts match
- examples are structurally isomorphic to the template

## 9. Contamination Scenario

Purpose: verify that success is not caused by leaked context.

Rules:

- do not tell a subagent the expected failure
- do not pass your conclusions
- do not leave prior generated answers where the agent can read them
- do pass the raw skill path and realistic user request

If the test only passes with leaked diagnosis, the skill is not strong enough yet.

Do not put expected route, required patterns, forbidden patterns, or assertions in the agent-facing task. Keep them in a separate grading card.
