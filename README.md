# skill-engineering-kit

**A governance methodology for building AI agent skills that don't rot.**

Three coordinated skills that turn skill authoring from "write a prompt and hope"
into a staged process with contracts, gates, and regression evidence.

> **Who this is for**: people who *write* agent skills — platform engineers,
> prompt engineers, anyone maintaining a skill library.
>
> Looking for something else? This is part of a three-repo family:
> [`skill-eval`](https://github.com/653390665/skill-eval) (the scoring tool) · **this repo** (methodology) ·
> [`reality-project-skills`](https://github.com/653390665/reality-project-skills) (a business skill suite).

## The problem

A skill is a Markdown file. It has no compiler, no test suite, and no release
gate — so it degrades silently: triggers drift, outputs get sloppy, a rewrite
quietly drops a capability that used to work.

This kit supplies the missing process.

## The three skills

| Skill | Role |
|---|---|
| **`skill-engineering-hub`** | Orchestrator. Determines which stage a skill is in and routes to the right next action (Mode A–G). |
| **`skill-engineering-standard`** | The rulebook. Lifecycle, required design artifacts, packaging rules, release gates. |
| **`skill-pressure-testing`** | The gate. Scenario design, regression/contamination control, and release readiness. |

They are designed to be installed together and invoke each other by name.

## The workflow

```
 1. Skill Brief                  ← what is this for, who triggers it, what must never happen
 2. Architecture Decision        ← one skill? several? role cards? shared gates? scripts?
 3. Trigger Contract             ← positive / negative / ambiguous triggers
 4. Output Contract              ← required outputs, forbidden outputs, evidence rules
 5. Quality Test Plan            ← written BEFORE the skill exists
 6. Generate files               ← via skill-creator (external)
 7. Polish docs                  ← via writing-skill (external)
 8. Pressure test                ← via skill-pressure-testing + skill-eval
 9. Release Gate                 ← release / patch / hold / rollback
10. Regression Log               ← every failure becomes a future test case
```

The core rule: **do not start from `SKILL.md`.** Steps 1–5 are the design
contract; the file is an implementation detail that comes later.

### Bridge to the mainline (Mode G)

The hub's Mode G exports the five contracts into **Skill IR 2.0**
(`skill-ir.json`) and hands them into the yao mainline — which compiles IR to
platform packages, runs trigger/output evals and blind A/B, and gates release
through Review Studio 2.0. Evidence flows back: trigger cases → test
scenarios, eval failures → regression log, review verdict → release gate.
See [`references/yao-bridge.md`](skill-engineering-hub/references/yao-bridge.md).

## Positioning: this kit vs yao-meta-skill

**Update (2026-09-03): yao-meta-skill is the creation mainline; this kit is the
supplementary discipline layer.** The two slot together as one pipeline — not
as competitors, and not as an "either/or" toolchain.

`yao-meta-skill` (YAO = Yielding AI Outcomes) is the Skill OS: intent dialogue →
Skill IR → multi-target compilers → Output Eval Lab → Review Studio 2.0. It is
where skills are actually authored, compiled, evaluated, and governed.

This kit supplies the **design discipline and regression memory** around that
mainline: the five contracts make authors think before the mainline models the
skill, and the Regression Log keeps every mainline eval failure as a future
test case.

| | **yao-meta-skill (mainline)** | **this kit (supplement)** |
|---|---|---|
| Job | Author, compile, eval, and govern skills | Make authors **think first** — contracts before files; remember failures |
| Flow | `quickstart → skill-ir → compile-skill → output-eval → review-studio` | Contracts (Mode A) → Mode G bridge → Regression Log |
| Core principle | Model once, compile for many targets | Do not start from `SKILL.md` |
| Form | Python toolchain + IR schema + compilers + eval lab | 3 self-contained Markdown skills, zero runtime deps |
| Where it wins | Full skill lifecycle, multi-platform packaging, governance | Authoring discipline, regression memory, team process |
| Ecosystem fit | Engineering mainline (how to ship) | Discipline front-end (what to build) + memory back-end |

**The niche statement:** this kit is the *discipline supplement* to the yao
mainline. yao asks "given a contract, how do I compile, evaluate, and ship it?"
This kit asks the harder question upstream: "how do I know the contract is
worth compiling?" — and downstream it answers "what did last release teach
us?" Mode G is the engineered bridge between the two: the five contracts
export into Skill IR 2.0, and yao eval/review evidence flows back into the
Regression Log and Release Gate.

Integration is verified against yao `@main`: a kit-generated IR resolves via
yao's `find_skill_ir`, passes official schema validation, and compiles for
`claude` + `generic` with 0 failures / 0 warnings (2026-09-03).

### Mainline quick reference

When the user says "create a skill" / "improve this skill", the mainline is:

```bash
# inside yao-meta-skill (Python 3.10+; use python3.13 on macOS)
python3 scripts/yao.py quickstart <skill_dir>        # intent dialogue → package
python3 scripts/yao.py skill-ir <skill_dir>          # model once (Skill IR 2.0)
python3 scripts/yao.py compile-skill <skill_dir> --target claude --target generic
python3 scripts/yao.py output-eval <skill_dir>       # trigger + output evals
python3 scripts/yao.py review-studio <skill_dir>     # one-page release gate
```

Before step 1 (or when a skill keeps failing review), run the kit supplement:

```bash
# inside skill-engineering-kit — five contracts first
skill-engineering-hub → Mode A (Skill Brief / Architecture Decision /
                       Trigger Contract / Output Contract / Quality Test Plan)
skill-engineering-hub → Mode G (export contracts → skill-ir.json → mainline)
```

See `skill-engineering-hub/references/yao-bridge.md` for the full field-level
mapping and verified constraints.

## Prerequisites

Two collaborator skills are referenced by the workflow but are **not included
here** (see [PREREQUISITES.md](PREREQUISITES.md)):

- `skill-creator` — generates the skill files and directory structure
- `writing-skill` — polishes README, examples, and user-facing wording

For step 8 you also need the scoring tool:

```bash
pip install skill-eval
```

## Repository layout

```
skill-engineering-kit/
├── skill-engineering-standard/    # lifecycle + contracts + packaging rules
├── skill-engineering-hub/         # workflow router (Modes A–G) + Skill IR export
├── skill-pressure-testing/        # scenario design + release gate
├── tests/scenarios/               # acceptance criteria + scenarios for the 3 skills
├── evidence/                      # controlled with/without behaviour runs
│   ├── scenarios/                 # task cards + grading cards
│   └── runs/                      # collected outputs
├── SKILL_SUITE_BEHAVIOR_CONTRAST_REPORT_2026-05-16.md
├── PREREQUISITES.md
└── LICENSE
```

## Evidence

`SKILL_SUITE_BEHAVIOR_CONTRAST_REPORT_2026-05-16.md` records a controlled run of
20 scenarios across five skill targets:

| Mode | Passed | Failed |
|---|---:|---:|
| `with_skill` | 20 | 0 |
| `without_skill` | 0 | 20 |

**Read this carefully**: that is a *controlled harness result* produced by this
project's own test rig. It demonstrates the suite has executable regression
evidence — it is **not** an independent third-party benchmark, and the
`without_skill` baseline is a generic no-skill answer path, not a judgement
about any specific model.

## Install

Copy the skill folders you need into your agent's skills directory. Each folder
is self-contained (no `../shared/` cross-references between them).

```bash
cp -R skill-engineering-standard skill-engineering-hub skill-pressure-testing ~/.claude/skills/
```

## License

MIT — see [LICENSE](LICENSE).
