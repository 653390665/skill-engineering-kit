# Pressure Grading Card: static_only_doc_patch

Mode: without_skill

## User Prompt

我只改了 README 和 MANIFEST，帮我压测一下包是否干净。

## Expected Route

static_installability_check

## Expected Output Type

static_audit

## Required Patterns

- README
- MANIFEST
- installability
- smallest scope

## Forbidden Patterns

- full benchmark
- without-skill comparison is required

## Assertions

- scope_control: uses static checks rather than unnecessary full benchmark

## Instructions For Evaluator

- Do not show this grading card to the answer-generating agent.
- Score `output.md` against required and forbidden patterns.
- Use assertions for human review or semantic grading.
