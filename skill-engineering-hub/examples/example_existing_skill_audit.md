# Example: Existing Skill Audit

User request:

> Check this skill and tell me if it is complete.

Correct hub behavior:

- Inspect available files.
- Check against engineering standard.
- Report missing artifacts.
- Separate static compliance from behavioral testing.
- Recommend pressure-testing if behavior is unverified.

Sample finding:

| Priority | File | Issue | Fix |
|---|---|---|---|
| P1 | QUALITY_TESTS.md | No negative trigger scenarios | Add at least three negative trigger tests |
