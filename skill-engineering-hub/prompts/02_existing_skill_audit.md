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
