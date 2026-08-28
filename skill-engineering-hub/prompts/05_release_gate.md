# Release Gate

Use this mode to decide whether a skill can be released.

## Release decisions

- Release: no P0/P1 issues; P2 issues are documented.
- Patch: no P0 issues, but P1 issues must be fixed before broad use.
- Hold: P0 issues exist.
- Rollback: new version regresses against prior accepted version.

## Required checks

- frontmatter valid;
- required files present;
- package clean;
- triggers defined;
- output contract defined;
- tests exist;
- pressure results reviewed if available;
- safety boundaries clear;
- versioning and regression logs updated.
