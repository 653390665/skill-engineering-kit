# Release Checklist

Use this before calling a skill package ready.

## Structure

- [ ] `SKILL.md` has valid frontmatter.
- [ ] `name` uses lowercase letters, digits, and hyphens.
- [ ] `description` says when to use the skill, not just what it contains.
- [ ] Required references, scripts, assets, or sibling folders exist.
- [ ] Skill does not include unnecessary README, changelog, or process clutter unless the package intentionally needs user-facing docs outside the skill folder.

## Installation

- [ ] Run the available skill validator.
- [ ] Run `scripts/validate_pressure_pack.py <path>` when pressure-test artifacts are expected.
- [ ] Only run scenario collection if pressure testing was explicitly requested or agreed for this release.
- [ ] If running scenarios, run `scripts/prepare_pressure_run.py <scenarios.yaml> <run-dir>` before collecting with/without outputs.
- [ ] If running scenarios, run `scripts/check_pressure_run.py <run-dir>` and confirm all required `output.md` files exist before scoring.
- [ ] If running scenarios, run `scripts/run_codex_pressure.py <run-dir> --skill-package <path>` or otherwise collect fresh-agent outputs without exposing grading cards.
- [ ] If scenario outputs exist, run `scripts/score_scenarios.py <scenarios.yaml> <outputs-dir>`.
- [ ] If templates, tests, auditors, and examples share required fields, run `scripts/check_template_consistency.py`.
- [ ] If distributed as zip, run an archive integrity test.
- [ ] If the skill depends on sibling folders, document the exact install layout.
- [ ] If scripts exist, run at least a representative sample.

## Behavior

- [ ] Acceptance criteria were written before scenarios.
- [ ] Trigger precision and recall were tested with positive, negative, and ambiguous prompts.
- [ ] Obvious trigger scenario passes.
- [ ] Adjacent non-trigger scenario does not over-trigger.
- [ ] Missing-information scenario avoids false certainty.
- [ ] Boundary scenario stops or narrows unsafe requests.
- [ ] Execution scenario produces a directly usable artifact.
- [ ] For task-generating skills, at least one execution replay was run or explicitly deferred.
- [ ] Regression scenario preserves old-version strengths or names the tradeoff.
- [ ] Relevant GitHub or ecosystem eval/security patterns were checked, borrowed, or consciously skipped.
- [ ] Scorecard was filled using `grading-rubric.md`.

## Security

- [ ] Automated skill/security scanner was run or explicitly marked unavailable.
- [ ] Manual credential, exfiltration, destructive command, and prompt-injection checks were run.
- [ ] Scripts were inspected before execution.

## Evidence

- [ ] Claims in the report point to scenarios, files, command output, or artifacts.
- [ ] `without_skill` failures are recorded as baseline evidence when outputs exist and scorer results are valid.
- [ ] Unsupported judgments are labeled as assumptions.
- [ ] External or current-world claims are searched or marked unknown.

## Release Decision

- [ ] All P0 fixes are closed.
- [ ] P1 risks are fixed or explicitly accepted.
- [ ] Remaining P2 items are listed as follow-up.
- [ ] A `PRESSURE_TEST_REPORT.md` or equivalent summary exists for complex skills.
