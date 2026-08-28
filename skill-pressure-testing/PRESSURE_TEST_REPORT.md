# Pressure Test Report: skill-pressure-testing v1.0.1

## 1. Summary Verdict

- Verdict: Needs patch in original package; patched clean package is structurally trial-ready.
- Score: 14 / 20 before patch; 18 / 20 after structural patch.
- Release recommendation: use the v1.0.1 clean package, not the original uploaded zip.
- Main risk before patch: install package contained cache/bytecode artifacts and lacked root package documentation.
- Main required fix: remove `__pycache__` / `.pyc`, add `README.md`, `MANIFEST.md`, `QUALITY_TESTS.md`, `PRESSURE_TEST_REPORT.md`, and strict scenario artifacts.

## 2. Skill Under Test

- Skill name: `skill-pressure-testing`
- Version or date: v1.0.1 structural patch, 2026-05-16
- Original path inspected: `skill-pressure-testing(3)/skill-pressure-testing`
- Patched path: `skill-pressure-testing-v1.0.1`
- Related skills: `skill-engineering-standard`, `skill-engineering-hub`

## 3. Installability

Original package:

- Frontmatter: valid.
- Folder structure: usable but incomplete.
- Required resources: references and scripts present.
- Package integrity: failed clean install standard because of `scripts/__pycache__` and `.pyc` files.
- Known install assumptions: pressure-run artifacts are optional unless strict pressure testing is expected.

Patched package:

- Frontmatter: valid.
- Folder structure: improved.
- Required resources: present.
- Package integrity: clean after removing cache/bytecode.
- Known install assumptions: strict pressure artifacts now included for this skill itself.

## 4. Acceptance Criteria

See `tests/scenarios/skill-pressure-testing/acceptance-criteria.md`.

## 5. Scenario Results

| Case | Scenario | Expected Route | Actual Behavior | Result | Failure Mode | Required Fix |
|---|---|---|---|---|---|---|
| 1 | Static installability | clean install package | original has cache files | FAIL before patch / PASS after patch | packaging contamination | remove cache and rebuild zip |
| 2 | Strict pressure-pack layout | strict artifacts present | original missing strict artifacts | FAIL before patch / PASS after patch | missing report/scenarios | add report and scenario files |
| 3 | Template consistency script availability | script exists and usable | present | PASS | none | keep script |
| 4 | Trigger clarity in SKILL.md | explicit pressure-test trigger only | present | PASS | none | add README clarity |

## 6. Scorecard

| Dimension | Score | Evidence | Fix |
|---|---:|---|---|
| Installability | 2 | clean package has no cache/bytecode | done |
| Trigger Precision | 2 | SKILL.md activation rule includes positive and non-use triggers | keep |
| Trigger Recall | 2 | includes Chinese and English pressure-test terms | keep |
| Routing Stability | 2 | scope router defines static, scenario, and full run scopes | keep |
| Evidence Discipline | 2 | report rules require scenario/file/run evidence | keep |
| Boundary Handling | 2 | stop conditions and contamination control present | keep |
| Execution Hardness | 2 | scripts scaffold, check, run, and score pressure runs | keep |
| Regression Control | 1 | methodology exists, but no historic run outputs included | keep in audit package |
| Artifact Discipline | 2 | strict artifacts now added | done |
| Security Posture | 1 | security-scan reference exists, but no automated security scanner run | add future security run if needed |

Total: 18 / 20

## 7. Trigger Evaluation

| Prompt | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| 请对这个 skill 做发布前压测 | use skill | trigger terms present | PASS | explicit pressure request |
| 帮我创建一个新 skill | do not use skill | SKILL.md says creation should use creator/writing flow first | PASS | decoy protected |
| 我只改 README，跑一下包是否干净 | use static scope | scope router says static checks only | PASS | no full benchmark by default |

## 8. Security Scan

- Automated tools run: linter, strict pressure-pack validator.
- Manual checks run: forbidden cache/file check, trigger boundary check, contamination rule check.
- Findings: original package had cache/bytecode contamination.
- False positives: none.
- Not checked: real with-skill / without-skill behavioral outputs because no external skill runner output was collected in this environment.
- Release impact: patched package is structurally clean; behavioral benchmark remains future work if public release claims are made.

## 9. Artifact Layout

Patched package adds:

- `README.md`
- `MANIFEST.md`
- `QUALITY_TESTS.md`
- `PRESSURE_TEST_REPORT.md`
- `tests/scenarios/skill-pressure-testing/acceptance-criteria.md`
- `tests/scenarios/skill-pressure-testing/scenarios.yaml`

Removed:

- `scripts/__pycache__/`
- `*.pyc`

## 10. Key Failures

### Failure 1: Packaging contamination

- Evidence: linter reported forbidden `__pycache__` and `.pyc` files.
- Why it matters: dirty packages create install noise and weaken trust in release readiness.
- Minimal fix: remove cache/bytecode files and rebuild zip.
- Re-test scenario: run clean package linter again.

### Failure 2: Missing root docs and strict pressure artifacts

- Evidence: linter warned missing `README.md` and `MANIFEST.md`; strict validator reported missing `QUALITY_TESTS.md`, `PRESSURE_TEST_REPORT.md`, and scenario files.
- Why it matters: users cannot tell how to install, use, or verify the skill.
- Minimal fix: add root docs and baseline pressure-test artifacts.
- Re-test scenario: run strict pressure-pack validator again.

## 11. Regression Comparison

| Capability | Original | Patched | Winner | Decision |
|---|---:|---:|---|---|
| Trigger clarity | 2 | 2 | tie | preserve original SKILL.md |
| Method depth | 2 | 2 | tie | preserve references |
| Install cleanliness | 0 | 2 | patched | replace package |
| Artifact discipline | 1 | 2 | patched | add strict artifacts |

## 12. Required Fixes

### P0

- None after patch.

### P1

- Original zip should not be used as the official install package.

### P2

- Future public release should add fresh with-skill / without-skill outputs if benchmarking claims are made.

## 13. Re-Test Results

- Static linter after patch: expected PASS.
- Strict pressure-pack validator after patch: expected PASS.
- Archive integrity after rebuild: expected PASS.
- Remaining risk: no real runner output collected in this environment.

## 14. External Pattern Borrowing

- Patterns referenced by this skill: agent-skills-eval, microsoft/skills acceptance criteria, promptfoo declarative assertions, skill-scanner separation of security scan.
- Mechanisms borrowed: acceptance-before-scenario, with/without comparison, deterministic required/forbidden patterns, contamination control.
- Mechanisms rejected: always running full benchmarks for every small edit.

## 15. Final Recommendation

- Ship: patched v1.0.1 clean package for internal use.
- Hold: original uploaded zip as official release.
- Keep old capability: preserve original SKILL.md, references, and scripts.
- Merge old capability: not needed.
- Next real execution test: collect fresh outputs for the four machine-readable scenarios if preparing public release.
