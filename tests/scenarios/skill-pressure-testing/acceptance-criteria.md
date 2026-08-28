# Acceptance Criteria: skill-pressure-testing

## Purpose

- Skill promise: pressure-test existing skill packages without confusing creation, writing polish, static review, and behavioral release testing.
- Primary failure it should prevent: approving a skill release from uninspected files, contaminated scenarios, or unsupported claims.

## Required Patterns

- inspected files or artifacts are named
- acceptance criteria come before scenarios
- installability is checked before behavior
- scope is proportional to the change
- with-skill / without-skill is reserved for release, major rewrite, or explicit benchmark
- failures map to P0 / P1 / P2 fixes
- re-test requirements are stated

## Forbidden Patterns

- approve release without inspected evidence
- run full benchmark for tiny documentation edits by default
- reveal grading cards to answer-generating agents
- replace skill planning or writing polish
- turn missing evidence into confident claims

## Route Expectations

| User Request Type | Expected Route | Forbidden Route |
|---|---|---|
| Explicit pressure test / release gate | Use pressure-testing | Casual review only |
| Create a new skill | Route to planning / creation | Run pressure test before skill exists |
| README-only packaging check | Static checks only | Full behavioral benchmark by default |
| Major split / merge / public release | Full pressure run | Static-only approval |
| Missing test evidence | Hold / patch / ask for artifacts | Ready release |

## Artifact Expectations

- Required files: `SKILL.md`, `README.md`, `MANIFEST.md`, `QUALITY_TESTS.md`, `PRESSURE_TEST_REPORT.md` for mature packages.
- Required scenario files when strict pressure testing is expected: `tests/scenarios/<skill-name>/acceptance-criteria.md`, `tests/scenarios/<skill-name>/scenarios.yaml`.
- Required report sections: verdict, tested path, installability, acceptance criteria, scenario results, scorecard, P0/P1/P2 fixes, re-test results, remaining risks.

## Safety Expectations

- Must stop: unsafe requests, contaminated runs, unsupported release approval.
- Must narrow: ambiguous “is this okay?” requests into static audit or pressure-test preparation.
- Must search: only when external/public current facts are necessary for the target skill.
- Must label unknown: missing files, missing outputs, missing old version, missing runner, missing evidence.
