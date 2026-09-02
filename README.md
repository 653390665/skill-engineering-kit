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

### Optional: yao-meta-skill backend (Mode G)

For multi-platform distribution, provider evals, or governed release, the hub
can export the five contracts into **Skill IR 2.0** (`skill-ir.json`) and hand
off to [`yao-meta-skill`](https://github.com/yaojingang/yao-meta-skill) — the
"Skill OS" that compiles IR to platform packages, runs trigger/output evals and
blind A/B, and gates release through Review Studio 2.0. Evidence flows back:
trigger cases → test scenarios, eval failures → regression log, review verdict
→ release gate. Kit designs; yao engineers. See `references/yao-bridge.md`.

## Positioning: this kit vs yao-meta-skill

`yao-meta-skill` (YAO = Yielding AI Outcomes) is a heavyweight, star-heavy
"Skill OS": Skill IR, multi-target compilers, an Output Eval Lab, Review Studio
2.0, and SkillOps telemetry. This kit is the **design discipline layer** — the
part of the pipeline yao deliberately does not own.

| | **this kit** | **yao-meta-skill** |
|---|---|---|
| Job | Make authors **think first** — contracts before files | Make skills **buildable at scale** — compile, eval, govern |
| Core principle | Do not start from `SKILL.md` | Model once, compile for many targets |
| Form | 3 self-contained Markdown skills, zero runtime deps | Python toolchain + IR schema + compilers + eval lab |
| Where it wins | Authoring discipline, regression memory, team process | Multi-platform packaging, provider evals, release governance |
| Ecosystem fit | Design front-end (what to build) | Engineering back-end (how to ship) |

**The niche statement:** this kit is the *methodology upstream* of the skill
ecosystem. yao answers "given a contract, how do I compile, evaluate, and
ship it?" This kit answers the harder question: "how do I know the contract is
worth compiling?" A skill that cannot be exported to Skill IR (Mode G) is a
skill that was never designed — and that is exactly what this kit exists to
catch, before yao's compilers ever run.

They do not compete: they slot into the same pipeline, and the handoff is
engineered at the field level (Trigger Contract ↔ `trigger_surface`, Output
Contract ↔ `eval_plan`, Release Gate ↔ `governance`). Integration is verified
against yao `@main`: a kit-generated IR resolves via yao's `find_skill_ir`,
passes official schema validation, and compiles for `claude` + `generic` with
0 failures / 0 warnings (2026-09-03).

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
