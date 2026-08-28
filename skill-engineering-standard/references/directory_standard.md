# Directory Standard

## Minimum Skill

```text
skill-name/
├─ SKILL.md
└─ README.md
```

## Mature Workflow Skill

```text
skill-name/
├─ SKILL.md
├─ README.md
├─ QUICK_START.md
├─ MANIFEST.md
├─ QUALITY_TESTS.md
├─ prompts/
├─ templates/
├─ references/
├─ examples/
└─ scripts/
```

## Multi-Skill System

```text
system-name/
├─ README.md
├─ QUICK_START.md
├─ MANIFEST.md
├─ shared/
├─ skill-one/
│  ├─ SKILL.md
│  └─ ...
└─ skill-two/
   ├─ SKILL.md
   └─ ...
```

## Audit Package

```text
audit-package/
├─ PRESSURE_TEST_REPORT.md
├─ REVIEW_NOTES.md
├─ tests/
├─ scripts/
└─ pressure-runs/
```

## Clean Install Exclusions

Exclude:

- `__MACOSX/`
- `.DS_Store`
- `__pycache__/`
- `*.pyc`
- local logs
- pressure runs
- local absolute paths
- credentials
