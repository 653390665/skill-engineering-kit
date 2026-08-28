---
name: skill-pressure-testing
description: Use only when the user explicitly asks to pressure test, stress test, run scenarios, benchmark, compare with/without skill, or prepare a release gate for a skill. Do not use for ordinary skill planning, writing, editing, or static review.
metadata:
  version: "1.0.2"
  updated: "2026-05-16"
---

# Skill Pressure Testing

## Purpose

Stress-test a skill before it becomes a trusted workflow. Look for the ways an agent still fails after reading the skill: wrong trigger, wrong route, premature output, weak task pack, unsafe workaround, missing install dependency, or regression against an older version.

## Activation Rule

Do not run pressure tests unless the user explicitly asks for pressure testing.

Skill creation's default rhythm is:

1. plan the skill
2. write or edit the content
3. do static self-checks
4. package or hand off

Pressure testing is an explicit extra step, not the default rhythm.

Trigger pressure testing only when the user says or clearly asks for:

- 压力测试 / 压测
- 跑场景
- with-skill / without-skill comparison
- benchmark / eval / regression run
- release gate / 发布前压测

If the user asks to create, optimize, or revise a skill without asking for pressure testing, use `skill-creator` or `writing-skills` first. You may suggest a pressure-test plan, but do not run it.

## Scope Router

When pressure testing is explicitly requested, choose the smallest scope that proves the claim:

| Situation | Test scope |
|---|---|
| Documentation, README, version, metadata, packaging, or manifest change | Static checks only |
| One router, gate, template, auditor, or boundary rule changed | Run only the affected scenario and one neighboring scenario if needed |
| New scenario added | Run only that scenario in with-skill mode; run without-skill only if measuring skill lift |
| Major rewrite, skill split/merge, public release, or claim that a new version beats an old version | Full pressure run |

Full with-skill / without-skill comparison is a release or major-change gate. Do not use it as a routine editing check.

Use this with `skill-creator` and `writing-skills`:
- `skill-creator`: create or update the skill structure.
- `writing-skills`: prove the skill teaches something by comparing behavior with and without it.
- `skill-pressure-testing`: prove the skill stays stable under realistic misuse, missing information, old-version comparison, and execution pressure.

## Quick Workflow

1. Identify the skill under test and its intended user-facing promise.
2. Read only the skill files needed to understand triggers, routers, gates, templates, and bundled resources.
3. Write acceptance criteria before scenarios: required patterns, forbidden patterns, route expectations, and artifact expectations.
4. Design pressure scenarios that attack the skill's promises, not its wording.
5. Run the installation and metadata checks first.
6. Run with-skill / without-skill comparison only when the user requested it, or when preparing a major release or rewrite evaluation.
7. Test at least one happy path, one missing-information path, one unsafe or out-of-scope path, one regression path, and one execution path.
8. For template-heavy skills, run a template consistency check across tests, auditors, templates, and examples before judging behavior.
9. Record exact failure modes, including phrases or structures that reveal weak behavior.
10. Patch the skill with the smallest fix that closes the observed loophole.
11. Re-run the affected scenarios and update the pressure test report.

## What To Read

- For the full method, read `references/pressure-test-method.md`.
- For scenario patterns, read `references/scenario-patterns.md`.
- For GitHub and ecosystem patterns to borrow, read `references/external-patterns.md`.
- For the scenario schema and artifact layout, read `references/test-artifact-design.md`.
- For scoring, read `references/grading-rubric.md`.
- For trigger precision and recall tests, read `references/trigger-eval.md`.
- For skill security scanning, read `references/security-scan.md`.
- For the report format, read `references/report-template.md`.
- Before release or handoff, read `references/release-checklist.md`.

## Required Test Categories

For complex skills, cover these categories:

- **Installability**: frontmatter, folder names, required resources, package integrity.
- **Trigger accuracy**: the skill activates for real use cases and stays silent for nearby non-use cases.
- **Routing stability**: routers choose the right mode, depth, template, agent, or next skill.
- **Evidence discipline**: facts, assumptions, unknowns, and search-needed claims stay separated.
- **Boundary pressure**: unsafe, premature, or out-of-scope requests are stopped or narrowed.
- **Regression pressure**: new versions do not lose old strengths.
- **Execution hardness**: generated task packs, specs, or plans can be acted on without re-guessing intent.
- **Template self-consistency**: tests, auditors, templates, and examples use the same required fields and structure.
- **External pattern scan**: relevant GitHub skill/eval/security projects have been checked or consciously skipped.
- **Contamination control**: test agents do not receive expected answers, hidden fixes, or prior conclusions.

## Minimum Output

When reporting results, include:

- Summary verdict.
- Tested version and path.
- Score by dimension.
- Scenarios run.
- Acceptance criteria used.
- Artifact layout or files inspected.
- Pass/fail table.
- Exact failure modes.
- Required fixes by P0/P1/P2.
- Re-test results after fixes.
- Remaining risks.

## Stop Conditions

Do not approve the skill for release if:

- It cannot install cleanly.
- It relies on sibling resources without documenting the required folder layout.
- It converts missing evidence into confident claims.
- It produces executable tasks without scope, inputs, outputs, tests, and acceptance criteria.
- A new version removes an important capability from the older version without naming that tradeoff.
- The pressure report contains conclusions that were not backed by a scenario, artifact, run log, or direct file inspection.

## Deterministic Tooling (skill-eval)

This skill delegates deterministic checks to the standalone tool **`skill-eval`** (a separate repository in this project family). Install it before executing scenario runs:

```bash
pip install skill-eval
```

| Command | Use it to |
|---|---|
| `validate-pressure-pack <skill-package>` | Confirm a package ships `QUALITY_TESTS.md`, `PRESSURE_TEST_REPORT.md`, acceptance criteria, and scenarios. |
| `prepare-pressure-run <scenarios.yaml> <run-dir>` | Create with-skill / without-skill task cards, grading cards, and run metadata before collecting outputs. Give agents `task.md`, not `grading-card.md`. |
| `check-pressure-run <run-dir>` | List which task cards still need `output.md`. |
| `run-codex-pressure <run-dir> --skill-package <path>` | Collect real with-skill / without-skill outputs via `codex exec`. Optional — requires the `codex` CLI. |
| `score-scenarios <scenarios.yaml> <outputs-dir>` | Run deterministic required/forbidden pattern checks; writes JSON or Markdown reports. |
| `check-template-consistency <files...> --field <field>` | Keep tests, auditors, templates, and examples aligned. Use `--heading-count N` for fixed numbered structures. |

Common scoring commands:

```bash
score-scenarios tests/scenarios/<skill-name>/scenarios.yaml pressure-runs/iteration-1 \
  --mode with_skill \
  --json pressure-runs/iteration-1/with_skill-grading.json \
  --markdown pressure-runs/iteration-1/with_skill-report.md

score-scenarios tests/scenarios/<skill-name>/scenarios.yaml pressure-runs/iteration-1 \
  --mode without_skill \
  --json pressure-runs/iteration-1/without_skill-grading.json \
  --markdown pressure-runs/iteration-1/without_skill-report.md
```

`without_skill` failures are usually valid baseline evidence, not a tool failure. Treat them as evidence that the skill adds value unless outputs are missing or the tool crashes.

`score-scenarios` exits `0` only when every scenario passes, so it can be wired directly into CI as a release gate.
