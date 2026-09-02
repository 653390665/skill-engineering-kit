# Yao Evidence Reflow Map

How `yao-meta-skill` evaluation and review artifacts flow back into this kit's
memory and gate artifacts. Direction 2 of the bidirectional bridge defined in
`yao-bridge.md` (Direction 1 is contract → IR export).

Read this together with `yao-bridge.md`. This file answers one question:
**"yao just ran its evals / review — what do I write back into the kit?"**

## Scope rule

Reflow applies only to skills that entered yao through kit Mode G (i.e. have
kit contracts). For skills born in yao without kit contracts, capture yao
failures in yao's own failures library; optionally adopt them into the kit's
Regression Log as historical context, clearly marked as non-kit-origin.

## Reflow channel 1: output-eval failures → Regression Log

Source artifacts (inside the yao skill dir):

- `reports/provider_output_evaluation.json`
  - `summary.failure_count` — nonzero means reflow is required
  - `failures[]` — each entry becomes one Regression Log row
  - `runs[]` — per-call records; use for root-cause context only
- `reports/provider-output-evaluation-analysis.md` — human-readable narrative

Target artifact: `skill-engineering-hub/engineering/REGRESSION_LOG.md`
(or the skill's own Regression Log, if it keeps one).

Row format (columns match `templates/regression_log.md`):

| Log column | Fill from |
|---|---|
| Date | eval run date (`generated_at` or report date) |
| Version | skill version under test (manifest/IR) |
| Failure | `failures[i]`: case id + one-line what happened + source ref (`provider_output_evaluation.json#failures[i]`) |
| Root cause | classify: trigger miss / output contract violation / evidence gap / safety edge / other |
| Fix | planned or applied fix (link contract section if it changes a kit contract) |

Regression test requirement: every reflowed failure must also be added to the
skill's Quality Test Plan as a scenario (usually a must-repeat negative case).
A Regression Log row without a test row is incomplete.

## Reflow channel 2: trigger cases → test scenarios

Source artifacts:

- yao trigger/holdout/adversarial cases under `evals/` (e.g. `holdout/`,
  `adversarial/`) and any `trigger_cases` files referenced by eval reports.

Target artifact: the kit's Quality Test Plan (Pressure-Test Preparation mode
uses it to build the scenario matrix).

Rules:

- yao trigger cases map 1:1 onto kit test scenarios: keep case id, input text,
  expected behavior (trigger or not-trigger).
- Adversarial cases become negative/ambiguous scenarios in the kit matrix.
- Holdout cases become must-pass regression scenarios (do not teach the skill
  their content afterward — same contamination rule as kit pressure-testing).
- If a yao case exposes a missing kit trigger contract row (a behavior yao
  tested that the kit Trigger Contract never specified), add a row to the
  Trigger Contract first, then to the test plan. Contract and tests must agree.

## Reflow channel 3: review-studio verdict → Release Gate

Source artifact:

- `reports/review-studio.json`
  - `summary.decision` — ship / review / hold / block
  - `gates[]` — per-gate `status` (pass/warn/fail) with `evidence` paths
  - `blockers[]` — must map to kit P0 fixes
  - `review_actions[]` — actionable items; each `next_step` is a candidate fix
  - `warnings[]` — candidate P1/P2 fixes

Target artifact: kit Release Gate (`templates/release_gate.md`) — add the
"yao review evidence" section (see template) before recording a decision.

Mapping rules:

- yao `blockers[]` → kit **P0** required fixes; no kit release/patch decision
  while any blocker is open.
- yao `review_actions[]` with `status: warn` → kit **P1**; informational
  actions → **P2**.
- yao `summary.decision` informs but does not replace the kit decision: the
  kit Release Gate still requires its own Installability/Behavior/Docs
  sections. A yao `ship` verdict does not auto-release in the kit; a yao
  `block` verdict always means kit `Hold`.
- Record the yao report path in the Release Gate so the decision is auditable.

## Minimal reflow checklist (run after every yao eval/review)

1. `summary.failure_count == 0`? If not → one Regression Log row per failure.
2. New trigger/holdout/adversarial cases since last reflow? → update Quality
   Test Plan (and Trigger Contract if behavior was unspecified).
3. review-studio `blockers` empty? If not → P0 fixes in Release Gate.
4. Record `summary.decision` + evidence path in the kit Release Gate.
5. Hub audit mode: when auditing a skill that has run yao evals, first check
   the Regression Log contains rows for every failure in the latest eval
   report. Missing rows are an audit finding.

## Version compatibility

Same contract as Direction 1: reflow tooling assumes yao report schemas
current as of yao-meta-skill 2.1.0 (`provider_output_evaluation.json`
`schema_version: 1.1-public`, `review-studio.json` gate/action structure).
If a newer yao version changes these shapes, update the mappings here and
note the verified pairing in `yao-bridge.md`.
