# External Prerequisites

This kit is an *orchestration and governance* layer. It decides what should
happen at each stage, but delegates two jobs to collaborator skills that are
**not bundled in this repository**.

| Collaborator | Role | What happens without it |
|---|---|---|
| `skill-creator` | Generates skill files and directory structure from the design contract | Steps 1–5 still work; you just have to write the files by hand |
| `writing-skill` | Polishes README, QUICK_START, examples, and user-facing wording | Docs stay unpolished — no functional impact |
| `yao-meta-skill` *(optional backend, Mode G)* | Compiles Skill IR to platform packages, runs trigger/output evals and blind A/B, gates governed release via Review Studio 2.0 | Mode A–F still fully work; you lose multi-platform compilation, provider evals, and governed release evidence |

Both are referenced by name, so any implementation that exposes those names will
work. If you don't have them, the methodology (brief → architecture decision →
contracts → test plan → gate) is still fully usable — you simply do the
generation and editing yourself.

## Optional backend: yao-meta-skill (Mode G)

For multi-platform distribution, provider evals, or governed release, clone the
Skill OS backend and point Mode G at it:

```bash
git clone https://github.com/yaojingang/yao-meta-skill.git
cd yao-meta-skill && python3.13 -m pip install -r requirements-ci.txt  # PyYAML
```

**Python ≥ 3.10 required** — yao's scripts use `X | None` type syntax. On macOS
use `python3.13` / `python3.12`; the system `python3` (3.9) will crash with
`TypeError: unsupported operand type(s) for |`.

Verified handoff (2026-09-03): a kit-generated `skill-ir.json` (schema 2.0.0)
resolves via yao's `find_skill_ir`, passes official schema validation, and
compiles to a Claude target contract with 0 failures / 0 warnings through both
`scripts/compile_skill.py` and `scripts/yao.py compile-skill`.

Key constraints discovered during integration (see
`skill-engineering-hub/references/yao-bridge.md`):

- IR discovery path: `skill-ir/examples/{name}.json` or `reports/skill-ir.json`
  (or `manifest.skill_ir_source`), with the directory/SKILL.md `name` matching.
- Drift check: IR `trigger_surface.description` must exactly match the
  `SKILL.md` frontmatter `description`, or yao blocks compilation.
- `validate_ir.py --skill-md <SKILL.md>` runs this drift check before handoff.

## Tooling prerequisite

Scenario *execution* (step 8) requires the scoring tool:

```bash
pip install skill-eval
```

Without it, `skill-pressure-testing` can still design scenarios and judge
release readiness qualitatively, but you cannot produce deterministic pass/fail
scores.

## Note on references to `reality-project-skills`

`skill-engineering-standard` includes examples that reference
`reality-project-skills` (see `skill-engineering-standard/examples/`) purely as
worked illustrations of the template. They are **not** a runtime dependency —
this kit works without that repository.
