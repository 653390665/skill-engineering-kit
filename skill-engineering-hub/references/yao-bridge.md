# Yao Meta Skill Bridge

Bidirectional integration contract between this kit and
[`yaojingang/yao-meta-skill`](https://github.com/yaojingang/yao-meta-skill)
(YAO = Yielding AI Outcomes).

## What yao-meta-skill is

YAO is a "Skill OS": a platform-neutral intermediate representation (Skill IR),
multi-target compilers (OpenAI / Claude / VS Code / generic), an Output Eval Lab
(trigger cases, adversarial, holdout, blind A/B), a Review Studio 2.0 release
gate page, and SkillOps telemetry.

This kit is the **design discipline layer**: contracts, gates, and regression
evidence that force authors to think before writing files.

## Division of labor

| Stage | This kit | yao-meta-skill |
|---|---|---|
| 1–5 Design contracts | Skill Brief → Architecture Decision → Trigger Contract → Output Contract → Quality Test Plan | — |
| 6 Model once | — | Skill IR (`skill-ir.json`, schema 2.0.0) |
| 7 Compile | — | Compiler / cross-packager → per-platform packages |
| 8 Evaluate | pressure-testing (scenario runs) | Output Eval Lab (trigger cases, adversarial, holdout, blind A/B) |
| 9 Govern | Release Gate (release/patch/hold/rollback) | Review Studio 2.0, promotion policy, trust reports |
| 10 Remember | Regression Log | failures library, drift telemetry |

## Contract → IR field mapping

Export a skill from kit contracts into Skill IR 2.0 (`templates/skill_ir.json`):

| Kit artifact | IR field (schema 2.0.0) | Notes |
|---|---|---|
| Skill Brief → purpose | `job_to_be_done` | The recurring job, not the platform |
| Skill Brief → name/owner | `name`, `title`, `governance.owner` | |
| Trigger Contract → positive | `trigger_surface.should_trigger[]` | Copy verbatim, one string each |
| Trigger Contract → negative | `trigger_surface.should_not_trigger[]` | Copy verbatim |
| Trigger Contract → ambiguous + neighbors | `trigger_surface.edge_cases[]` | Ambiguous triggers + neighbor-skill routing rules |
| Trigger Contract → trigger tests | `eval_plan.trigger[]` | Prompts + expected route |
| Output Contract → required/forbidden | `eval_plan.output[]` | Assertions derived from required + forbidden outputs |
| Quality Test Plan → unsafe/boundary/regression | `eval_plan.adversarial[]` | Negative trigger, safety, boundary, execution pressure cases |
| Quality Test Plan → without-skill baseline | `eval_plan.baseline` | Baseline prompt shape used for A/B |
| Architecture Decision | `workflow.steps[]`, `workflow.decision_points[]`, `workflow.failure_modes[]` | |
| Package structure | `resources.references[]`, `resources.scripts[]`, `resources.assets[]`, `resources.reports[]` | Only files that exist |
| Release Gate decision | `governance.maturity` | scaffold / production / library / governed |
| Security & boundary review | `risk.output_risk`, `risk.execution_risk`, `risk.trust_boundary` | low/medium/high; personal/team/external |
| Governance cadence | `governance.review_cadence`, `governance.review_due` | |
| Target platforms | `targets[]` | e.g. `claude`, `openai`, `codex`, `generic` (optional) |
| Source contracts | `source_files[]` | Paths of the kit contract files that produced this IR (optional) |

## Handoff protocol (kit → yao)

1. Complete kit Steps 1–5 (all five contracts must exist).
2. Generate `skill-ir.json` from `templates/skill_ir.json`.
3. Validate against yao schema 2.0.0:
   `python3 scripts/validate_ir.py skill-ir.json`
4. Hand off to yao-meta-skill: compile, run trigger/output evals, run Review Studio.
   ```text
   # inside yao-meta-skill
   python3 scripts/compile_skill.py --ir skill-ir.json
   python3 scripts/yao.py trigger-eval --self
   python3 scripts/yao.py output-exec --self
   python3 scripts/yao.py review-studio --self
   ```

## Return protocol (yao → kit)

Pull yao outputs back into kit artifacts:

| yao output | Kit destination |
|---|---|
| `evals/trigger_cases.json` | Seed `tests/scenarios/<skill>/scenarios.yaml` |
| `evals/output/` assertions + failures | Quality Test Plan "Regression" group |
| `failures/*` failure library | Regression Log entries (each failure → future test) |
| Review Studio 2.0 verdict / promotion policy | Release Gate evidence input |
| Compiled package per platform | `skill-creator` output comparison / install checklist |

## Shared principles

- Never invent IR fields from thin air; leave empty or use explicit
  low-confidence defaults (yao authoring rule).
- A skill that cannot be exported to IR is probably not designed yet —
  go back to contracts.
- Kit stays dependency-free; yao is the optional heavy backend. Neither
  replaces the other.
