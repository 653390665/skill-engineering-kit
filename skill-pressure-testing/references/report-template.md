# Pressure Test Report Template

Use this structure for `PRESSURE_TEST_REPORT.md` or an equivalent release note.

```md
# Pressure Test Report

## 1. Summary Verdict

- Verdict:
- Score:
- Release recommendation:
- Main risk:
- Main required fix:

## 2. Skill Under Test

- Skill name:
- Version or date:
- Path:
- Compared version, if any:
- Related skills:

## 3. Installability

- Frontmatter:
- Folder structure:
- Required resources:
- Package integrity:
- Known install assumptions:

## 4. Acceptance Criteria

- Required patterns:
- Forbidden patterns:
- Route expectations:
- Artifact expectations:
- Safety expectations:

## 5. Scenario Results

| Case | Scenario | Expected Route | Actual Behavior | Result | Failure Mode | Required Fix |
|---|---|---|---|---|---|---|
| 1 |  |  |  | PASS/FAIL/PARTIAL |  |  |

## 6. Scorecard

| Dimension | Score | Evidence | Fix |
|---|---:|---|---|
| Installability |  |  |  |
| Trigger Precision |  |  |  |
| Trigger Recall |  |  |  |
| Routing Stability |  |  |  |
| Evidence Discipline |  |  |  |
| Boundary Handling |  |  |  |
| Execution Hardness |  |  |  |
| Regression Control |  |  |  |
| Artifact Discipline |  |  |  |
| Security Posture |  |  |  |

Total:

## 7. Trigger Evaluation

| Prompt | Expected | Actual | Result | Notes |
|---|---|---|---|---|
|  | use skill |  | PASS/FAIL |  |
|  | do not use skill |  | PASS/FAIL |  |

## 8. Security Scan

- Automated tools run:
- Manual checks run:
- Findings:
- False positives:
- Not checked:
- Release impact:

## 9. Artifact Layout

- Output files inspected:
- Run logs:
- Grading files:
- Package files:
- Missing artifacts:

## 10. Key Failures

### Failure 1

- Evidence:
- Why it matters:
- Minimal fix:
- Re-test scenario:

## 11. Regression Comparison

| Capability | Old Version | New Version | Winner | Decision |
|---|---:|---:|---|---|
| Trigger clarity |  |  |  |  |
| Execution quality |  |  |  |  |
| Safety |  |  |  |  |

## 12. Required Fixes

### P0

- 

### P1

- 

### P2

- 

## 13. Re-Test Results

- Scenario:
- Before:
- Patch:
- After:
- Remaining risk:

## 14. External Pattern Borrowing

- GitHub or ecosystem projects checked:
- Mechanisms borrowed:
- Mechanisms rejected:
- Reason:

## 15. Final Recommendation

- Ship:
- Hold:
- Keep old version:
- Merge old capability:
- Next real execution test:
```

## Severity Rules

- **P0**: install failure, safety failure, data loss, destructive action, or core route unusable.
- **P1**: major quality loss, weak execution template, serious regression, or repeated unsupported claims.
- **P2**: clarity, examples, documentation, edge cases, or useful polish.

## Verdict Labels

- **Ready**: install passes, core scenarios pass, no P0/P1 open.
- **Trial-ready**: no P0 open, P1 risks named, real users can test with caution.
- **Needs patch**: P0 or multiple P1 issues.
- **Do not ship**: unsafe behavior, unreliable install, or false confidence under pressure.
