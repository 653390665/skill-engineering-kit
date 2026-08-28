# Test Artifact Design

This skill borrows its test artifact shape from GitHub skill/eval projects:

- `agent-skills-eval`: with-skill / without-skill comparison and durable run artifacts.
- `microsoft/skills`: acceptance criteria before scenarios, with expected and forbidden patterns.
- `promptfoo`: declarative tests and assertions.
- `skill-scanner`: security scanning as a separate layer with clear limitations.

## Recommended Files

For a complex skill package, create or expect:

```text
QUALITY_TESTS.md
PRESSURE_TEST_REPORT.md
TEST_RUN_YYYY-MM-DD.md
```

Run the local structure checker when available:

```bash
scripts/validate_pressure_pack.py <path-to-skill-or-package>
scripts/validate_pressure_pack.py <path-to-skill-or-package> --strict
```

Run the deterministic pattern scorer after collecting outputs:

```bash
scripts/prepare_pressure_run.py tests/scenarios/<skill-name>/scenarios.yaml pressure-runs/iteration-1
scripts/check_pressure_run.py pressure-runs/iteration-1 --markdown pressure-runs/iteration-1/RUN_STATUS.md
scripts/run_codex_pressure.py pressure-runs/iteration-1 --skill-package <path-to-skill-package>
scripts/score_scenarios.py tests/scenarios/<skill-name>/scenarios.yaml pressure-runs/iteration-1 \
  --mode with_skill \
  --json pressure-runs/iteration-1/with_skill-grading.json \
  --markdown pressure-runs/iteration-1/with_skill-report.md
scripts/score_scenarios.py tests/scenarios/<skill-name>/scenarios.yaml pressure-runs/iteration-1 \
  --mode without_skill \
  --json pressure-runs/iteration-1/without_skill-grading.json \
  --markdown pressure-runs/iteration-1/without_skill-report.md
```

For template-heavy skills, also run a consistency check:

```bash
scripts/check_template_consistency.py <template.md> <example.md> \
  --heading-count 13 \
  --field "Objective" \
  --field "Acceptance Criteria" \
  --field "Done Definition"
```

For an automated harness, use a layout like:

```text
tests/
└── scenarios/
    └── <skill-name>/
        ├── acceptance-criteria.md
        └── scenarios.yaml

pressure-runs/
└── iteration-1/
    ├── meta.json
    ├── benchmark.json
    ├── <scenario-id>/
    │   ├── with_skill/
    │   │   ├── task.md
    │   │   ├── grading-card.md
    │   │   ├── output.md
    │   │   ├── grading.json
    │   │   └── timing.json
    │   └── without_skill/
    │       ├── task.md
    │       ├── grading-card.md
    │       ├── output.md
    │       ├── grading.json
    │       └── timing.json
    └── report/
        └── index.html
```

Use markdown-only files when the project does not have an automated harness yet. Keep the same concepts: criteria, scenarios, outputs, grading, report.

Do not show `grading-card.md`, required patterns, forbidden patterns, expected routes, or assertions to the answer-generating agent. Show only `task.md`.

If an output only passes after the answer-generating agent saw the grading card, previous failure notes, or expected route, mark the run contaminated and re-run it.

## Acceptance Criteria Shape

Write this before running scenarios.

```md
# Acceptance Criteria: <skill-name>

## Purpose

- Skill promise:
- Primary failure it should prevent:

## Required Patterns

- 

## Forbidden Patterns

- 

## Route Expectations

| User Request Type | Expected Route | Forbidden Route |
|---|---|---|
|  |  |  |

## Artifact Expectations

- Required files:
- Required sections:
- Required fields:
- Required validation:

## Safety Expectations

- Must stop:
- Must narrow:
- Must search:
- Must label unknown:
```

## Scenario YAML Shape

Use this shape if writing machine-readable tests.

```yaml
config:
  model: gpt-4.1
  temperature: 0.3
  modes:
    - with_skill
    - without_skill

scenarios:
  - id: missing_evidence_bp
    name: Missing evidence business plan pressure
    prompt: |
      I only have a rough idea. Write a formal business plan.
    expected_route: "skeleton_or_questions"
    required_patterns:
      - "unknown"
      - "assumption"
      - "next validation"
    forbidden_patterns:
      - "market size is"
      - "users will pay"
    assertions:
      - type: route
        value: "does not produce formal BP"
      - type: evidence
        value: "separates facts from assumptions"
    tags:
      - missing-evidence
      - boundary
```

## Scenario Card Shape

Use this shape for manual reports.

```md
## Case N: <name>

- User prompt:
- Expected route:
- Expected output type:
- Required patterns:
- Forbidden patterns:
- Actual behavior:
- Result:
- Failure mode:
- Patch:
- Re-test:
```

## Design Rules

- One scenario should test one main failure.
- Expected and forbidden patterns must be concrete enough to inspect.
- Do not rely only on LLM judge scoring when deterministic checks are possible.
- Deterministic pattern checks are not semantic grading; use them as a first pass.
- Preserve run artifacts so future versions can be compared.
- Treat security scans as necessary but insufficient.
- For skills that generate executable tasks, add at least one execution replay when feasible: generate a task pack, hand it to a fresh coding agent, implement the smallest artifact, then verify against the task's own test cases.
