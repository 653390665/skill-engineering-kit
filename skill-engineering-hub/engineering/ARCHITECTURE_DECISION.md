# Architecture Decision

## Decision
Use one coordination skill, not a merged pressure-testing mega-skill.

## Rationale
The workflow has distinct responsibilities:

- standard definition;
- skill creation;
- documentation optimization;
- behavioral pressure testing;
- release decision.

The hub coordinates these responsibilities without duplicating their core logic.

## Rejected option: merge with skill-pressure-testing
Rejected because pressure testing is a post-creation behavior check, while the hub also handles pre-creation planning and post-test interpretation.

## Rejected option: replace skill-creator
Rejected because the hub's job is to produce planning contracts, not generate all skill files by default.
