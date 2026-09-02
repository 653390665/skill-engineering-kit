# Tool Responsibility Matrix

| Tool / Skill | Primary job | Should not do |
|---|---|---|
| skill-engineering-hub | Coordinate planning, audit, pressure-test preparation, result interpretation, release decisions, and Skill IR export (Mode G) | Generate full skill files when skill-creator is expected |
| skill-engineering-standard | Define reusable standards and templates | Run behavioral pressure tests |
| skill-creator | Create skill files and directory structure | Decide release readiness |
| writing-skill | Improve wording, README, examples, and documentation clarity | Define architecture or safety boundaries alone |
| skill-pressure-testing | Run pressure tests, regression checks, security checks, release checks | Replace creation planning |
| yao-meta-skill (creation mainline) | Author, compile, eval, and govern skills via Skill IR (quickstart → skill-ir → compile-skill → output-eval → review-studio) | Design skills for you — it consumes kit contracts via Mode G, it does not replace the design discipline |

## Kit ↔ yao handoff

- Kit owns Steps 1–5 (design contracts) and Step 10 (Regression Log).
- yao owns Steps 6–9 engineering: IR modeling, compilation, evals, Review Studio.
- The handoff artifact is `skill-ir.json` (schema 2.0.0), generated and validated by Mode G.
- Return artifacts: `evals/trigger_cases.json` → kit scenarios; eval failures → regression group; failures library → Regression Log; Review Studio verdict → Release Gate evidence.
