# Existing Skill Standard Audit

Use this mode when a skill already exists and the user wants optimization.

## Inspect

- SKILL.md frontmatter and activation rules;
- README and usage guidance;
- MANIFEST completeness;
- prompts/templates/references/scripts/examples presence;
- engineering artifacts if present;
- trigger and output contracts;
- quality tests;
- release and regression docs;
- packaging cleanliness.

## Yao reflow check (only if the skill has yao eval reports)

If the skill directory contains yao artifacts (`reports/provider_output_evaluation.json`,
`reports/review-studio.json`) and the skill has kit contracts (it entered yao
via Mode G):

1. Read `references/yao_reflow.md` for the mapping rules.
2. For every entry in the latest eval report's `failures[]`, verify the
   Regression Log has a matching row (source `yao`, case id) and the Quality
   Test Plan has a matching scenario. Missing rows are audit findings (P1;
   P0 if the same failure has recurred more than once).
3. Verify the latest Release Gate records the yao `summary.decision` and maps
   `blockers[]` to P0 fixes. A release/patch decision made while a yao blocker
   is open is a P0 audit finding.

## Output

Use `templates/standard_audit_report.md`.

Every issue must include:

- priority: P0/P1/P2;
- affected file;
- problem;
- why it matters;
- fix direction;
- test to add.

## Do not

- claim behavioral correctness from static files alone;
- silently rewrite the skill;
- ignore missing engineering docs if the package is intended for team use.
