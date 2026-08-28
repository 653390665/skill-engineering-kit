# External Prerequisites

This kit is an *orchestration and governance* layer. It decides what should
happen at each stage, but delegates two jobs to collaborator skills that are
**not bundled in this repository**.

| Collaborator | Role | What happens without it |
|---|---|---|
| `skill-creator` | Generates skill files and directory structure from the design contract | Steps 1–5 still work; you just have to write the files by hand |
| `writing-skill` | Polishes README, QUICK_START, examples, and user-facing wording | Docs stay unpolished — no functional impact |

Both are referenced by name, so any implementation that exposes those names will
work. If you don't have them, the methodology (brief → architecture decision →
contracts → test plan → gate) is still fully usable — you simply do the
generation and editing yourself.

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
