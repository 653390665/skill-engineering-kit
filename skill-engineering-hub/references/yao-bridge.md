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

## Division of labor — yao is the mainline, kit is the supplement

`yao-meta-skill` is the **creation mainline** (author → compile → eval →
govern). This kit is the **supplementary discipline layer**: it makes authors
design before the mainline models, and it remembers what releases teach.

| Stage | yao-meta-skill (mainline) | this kit (supplement) |
|---|---|---|
| 0 Design discipline | — | Skill Brief → Architecture Decision → Trigger Contract → Output Contract → Quality Test Plan (Mode A, before modeling) |
| 1 Model once | Skill IR (`skill-ir.json`, schema 2.0.0) | Mode G bridge: export the five contracts into IR |
| 2 Compile | Compiler / cross-packager → per-platform packages | — |
| 3 Evaluate | Output Eval Lab (trigger cases, adversarial, holdout, blind A/B) | pressure-testing (scenario runs) feeds scenarios; eval failures → Regression Log |
| 4 Govern | Review Studio 2.0, promotion policy, trust reports | Release Gate (release/patch/hold/rollback) consumes review evidence |
| 5 Remember | failures library, drift telemetry | Regression Log (every failure → future test) |

Start here: `python3 scripts/yao.py quickstart <skill_dir>` is the mainline
entry point. Use kit Mode A before it when the idea is vague, and Mode G to
hand contracts over.

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

## Handoff protocol (kit → yao mainline)

1. (Optional but recommended) Complete kit Mode A contracts when the idea is
   vague — the five contracts are the discipline front-end.
2. Generate `skill-ir.json` from `templates/skill_ir.json`.
3. Validate against yao schema 2.0.0:
   `python3 scripts/validate_ir.py skill-ir.json`
4. Place the IR where yao's resolver expects it (see constraints below).
5. Hand off to yao-meta-skill (Python 3.10+ required — yao scripts use `X | None`
   type syntax; on macOS use `python3.13` / `python3.12`, not system `python3` 3.9):
   ```text
   # inside yao-meta-skill — both entry points work; the unified CLI is preferred
   python3 scripts/yao.py compile-skill <skill_dir> --target claude --output-json out.json
   python3 scripts/yao.py skill-ir <skill_dir> --validate-only
   python3 scripts/yao.py output-eval <skill_dir>
   python3 scripts/yao.py review-studio <skill_dir>
   ```

## Verified integration constraints (tested against yao repo @ main)

These were discovered by real handoff testing, not from docs alone:

| # | Constraint | Detail |
|---|---|---|
| 1 | IR discovery path | yao resolves IR from, in order: `manifest.json` → `skill_ir_source`, `reports/skill-ir.json`, or `skill-ir/examples/{name}.json`. The directory name must equal the skill name. |
| 2 | Name identity | IR `name` must equal the directory name AND `SKILL.md` frontmatter `name`. Mismatch → `name-mismatch` error. |
| 3 | **Description drift check** | IR `trigger_surface.description` must **exactly match** (normalized) `SKILL.md` frontmatter `description`. Mismatch → `description-mismatch` error and compile is blocked. Keep them in sync — put the same sentence in both places. |
| 4 | Targets declared | Compiler warns if `--target` is not listed in IR `targets[]`. Declare your targets in the IR. |
| 5 | Python version | Requires Python 3.10+. macOS system `python3` is often 3.9 → use `python3.13`/`python3.12`. |
| 6 | Schema strictness | `schema.json` uses `additionalProperties: false` — no unknown top-level fields. `targets[]` and `source_files[]` are legal optional arrays. |

Verified end-to-end: kit `example_skill_ir.json` (restaurant-menu-analysis) passed
`find_skill_ir` schema validation and compiled to a Claude target contract with
0 failures / 0 warnings via both `compile_skill.py` and `yao.py compile-skill`.

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
