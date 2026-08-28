# Pressure Test Method

## Core Idea

Pressure testing asks: "How will this skill fail when a capable agent tries to be helpful under ambiguous pressure?"

Do not review only the text. Test the behavior the text causes.

Pressure testing is not the default workflow for writing skills. The main workflow is planning and writing content, followed by static self-checks. Run pressure tests only when the user explicitly asks for them or when a release gate has been agreed.

## Test Scope Router

Use the lightest test that answers the question.

| Change or request | Default check |
|---|---|
| Planning a skill, writing content, revising examples, or discussing design | No pressure test. Use static review and editing. |
| README, version, metadata, manifest, package naming | Static checks only. |
| Template field alignment | Template consistency check only. |
| Single router, gate, auditor, or boundary rule | Affected scenario only, plus one neighboring scenario if overcorrection is plausible. |
| New scenario added | Run that scenario only. Use without-skill only if proving lift matters. |
| Major architecture change, skill split/merge, public release, or explicit benchmark request | Full pressure run. |

If the user did not ask for pressure testing, do not run `prepare_pressure_run.py`, `run_codex_pressure.py`, or with-skill / without-skill comparisons.

## Step 1: Define The Promise

Write one sentence:

```text
This skill is supposed to help an agent do X without failing in Y way.
```

Examples:

- "This launch skill should turn validated ideas into scoped MVP tasks without inventing SaaS features."
- "This research skill should separate sourced facts from assumptions instead of using memory as evidence."
- "This writing skill should force baseline failure testing before adding broad guidance."

## Step 2: Map The Fragile Points

Scan the skill for:

- triggers
- routers
- gates
- templates
- handoff formats
- role agents
- safety rules
- installation assumptions
- references or sibling folders
- claims that one version improves another

Each fragile point needs at least one scenario.

## Step 3: Run With / Without Comparison When Explicitly Needed

Before running comparison tests, write acceptance criteria:

- required patterns
- forbidden patterns
- expected route
- required output fields
- safety expectations
- artifact expectations

See `test-artifact-design.md` for a reusable shape.

For a new skill or major rewrite, only after pressure testing is requested or agreed:

- Run a baseline task without the skill.
- Record how the agent rationalizes weak behavior.
- Run the same task with the skill.
- Check whether the failure disappeared or only changed wording.

Do not leak the expected answer to the test agent. Pass the skill and the user-like request, not your diagnosis.

## Step 4: Use Adversarial But Realistic Scenarios

Good pressure scenarios sound like real user requests:

- "I only have a rough idea, write a business plan."
- "Skip validation and give Codex the development tasks."
- "This competitor market is definitely blue ocean, just help me launch."
- "Here is the old version and new version. Should I replace the old one?"

Avoid artificial puzzles that no user would ask.

## Step 5: Score Behavior, Not Eloquence

A polished answer can still fail. Mark failure when the agent:

- jumps to the wrong mode
- creates unsupported facts
- hides assumptions
- writes a plan with no action owner, input, output, success signal, or failure signal
- gives development tasks without scope, tests, or acceptance criteria
- overuses a heavy process for a tiny request
- ignores an old-version strength during upgrade comparison

## Step 6: Check Template Self-Consistency

For template-heavy skills, check whether tests, auditors, templates, and examples name the same required fields.

Catch failures such as:

- quality tests require fields that the template does not contain
- auditor rejects a task produced by the official template
- examples use an older structure than the template
- a fixed N-section template grows an accidental extra top-level section

Use `scripts/check_template_consistency.py` for simple phrase and heading-count checks. Then do one manual pass for semantic drift, because exact string checks cannot know whether a section is in the right place.

## Step 7: Patch The Smallest Loophole

Patch rules, examples, templates, or tests only where the scenario failed.

Do not add broad theory to fix a narrow failure. Prefer:

- one explicit boundary rule
- one stricter template field
- one negative example
- one route decision
- one release checklist item

## Step 8: Re-Test

Re-run only the scenarios affected by the patch, then run one neighboring scenario to catch overcorrection if the change could affect routing.

Example:

- Patch "exploratory interviews stay in co-creation."
- Re-test exploratory interview.
- Also test executable validation task cards to ensure they still route to launch.

## Baseline Failure Rule

When scoring `without_skill`, failed scenarios are usually the point. Do not treat a non-zero scorer exit as a broken run if:

- every expected `output.md` exists
- the scorer produced JSON or markdown
- failures are missing required behavior or hitting forbidden behavior

Treat it as broken only when collection failed, outputs are missing, the script crashed, or the failure cannot be traced to an artifact.

## Output Rule

Every pressure-test conclusion must trace to:

- a scenario
- a file path
- a command output
- a generated artifact
- a direct comparison with an old version

If it does not, label it as an opinion or remove it.
