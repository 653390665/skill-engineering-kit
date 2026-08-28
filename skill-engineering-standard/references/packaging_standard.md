# Packaging Standard

## Two-Package Model

### Install Package

For actual use.

Include:

- SKILL.md
- README.md
- QUICK_START.md
- MANIFEST.md
- QUALITY_TESTS.md
- prompts/
- templates/
- references/
- examples/
- required scripts/

Exclude:

- pressure-runs/
- local logs
- codex-run.log
- __pycache__/
- __MACOSX/
- .DS_Store
- local paths

### Audit Package

For review and regression.

May include:

- PRESSURE_TEST_REPORT.md
- REVIEW_NOTES.md
- tests/
- scripts/
- pressure-runs/
- run logs

Still exclude:

- credentials
- API keys
- private local paths where possible

## Release Naming

Use clear names:

```text
skill-name-v1.0.0-install.zip
skill-name-v1.0.0-audit.zip
```

Avoid names like:

```text
v2(4).zip
new-final-final.zip
```

## Package Cleanliness Checklist

- [ ] version naming consistent
- [ ] no local paths
- [ ] no cache files
- [ ] no logs in install package
- [ ] manifest matches actual files
- [ ] examples match templates
- [ ] README describes package type
