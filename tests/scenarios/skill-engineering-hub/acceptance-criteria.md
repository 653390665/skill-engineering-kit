# Acceptance Criteria: skill-engineering-hub

## Purpose

- Skill promise: coordinate skill-engineering-standard, skill-creator, writing-skill, and skill-pressure-testing without replacing them.
- Primary failure it should prevent: mixing planning, creation, pressure testing, documentation polish, and release decision into one uncontrolled answer.

## Required Patterns

- correct mode selection A-F
- user-confirmed facts / file-inspected facts / deductions / assumptions / unknowns separated
- P0 / P1 / P2 fixes for audits
- recommended next tool when appropriate
- no claim of passed tests without inspected files or outputs

## Forbidden Patterns

- replacing skill-creator for file generation by default
- replacing pressure-testing for actual scenario execution
- claiming clean install without inspection
- skipping release gate for publish decisions

## Route Expectations

| User Request Type | Expected Route | Forbidden Route |
|---|---|---|
| New skill idea | Mode A | full file generation first |
| Existing skill audit | Mode B | casual comment only |
| Pressure-test preparation | Mode C | unstructured scenario list |
| Interpret test report | Mode D | rewrite skill blindly |
| Publish decision | Mode E | unsupported ready claim |
| Toolchain design | Mode F | vague explanation |
