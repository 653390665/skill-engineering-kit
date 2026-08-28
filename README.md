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
| **`skill-engineering-hub`** | Orchestrator. Determines which stage a skill is in and routes to the right next action (Mode A–F). |
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
├── skill-engineering-hub/         # workflow router (Modes A–F)
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
