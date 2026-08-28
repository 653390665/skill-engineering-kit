# Example Release Gate

## 1. Version

- Package name: `reality-project-skills`
- Current version: `2.2.2`
- Previous version: `2.2.1`
- Release type: minor documentation enhancement

## 2. Installability

- [x] `SKILL.md` exists.
- [x] Frontmatter is valid.
- [x] Folder name is correct.
- [x] Required files are present.
- [x] Referenced files exist.

## 3. Package Cleanliness

- [x] No `__MACOSX/`.
- [x] No `.DS_Store`.
- [x] No `__pycache__/`.
- [x] No `*.pyc`.
- [x] No local absolute paths.
- [x] No logs in install package.
- [x] No pressure runs in install package.
- [x] No credentials or API keys.

## 4. Behavior Tests

- [x] Trigger tests passed.
- [x] Negative trigger tests passed.
- [x] Ambiguous trigger tests passed.
- [x] Output contract tests passed.
- [x] Safety tests passed.
- [x] Regression tests passed.

## 5. Documentation

- [x] README exists.
- [x] QUICK_START exists.
- [x] MANIFEST exists.
- [x] Examples match templates.
- [x] Version naming is consistent.

## 6. Regression

Old strengths preserved:

- two-skill architecture
- roundtable agents
- 13-section Codex task pack
- clean handoff

Known tradeoffs:

- more complex than personal lightweight version

## 7. Decision

- [x] Release

## 8. Required Fixes

### P0

- none

### P1

- none

### P2

- add audit package later

## 9. Release Notes

v2.2.2 adds quick start, shared index, structure router, pre-task checklist, and end-to-end child handwriting AI example.
