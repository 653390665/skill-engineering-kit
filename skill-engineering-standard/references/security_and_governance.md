# Security And Governance

## Why This Matters

A skill is not just documentation. It can influence when an AI system chooses a workflow, what files it reads, what claims it makes, and what actions it recommends.

## Governance Risks

- overbroad trigger descriptions
- hidden unsafe instructions
- duplicated skill names
- misleading descriptions
- unsafe tool-use instructions
- local paths or private logs in install packages
- examples that contradict templates
- pressure tests that are not reproducible

## Security Review Checklist

- [ ] No credentials.
- [ ] No API keys.
- [ ] No private local paths.
- [ ] No hidden destructive instructions.
- [ ] No instructions to bypass platform rules.
- [ ] No unsafe medical/legal/financial claims without boundaries.
- [ ] No overbroad trigger language.
- [ ] No irrelevant instructions that could hijack routing.

## Semantic Supply Chain Awareness

Skill names and descriptions influence discovery and routing.

Therefore:

- use precise names
- use narrow descriptions
- define negative triggers
- document adjacent skills
- avoid claiming broad authority

## Release Governance

Every release should record:

- version
- change type
- tests run
- known risks
- release decision
- rollback plan
