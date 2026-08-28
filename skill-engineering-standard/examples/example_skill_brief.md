# Example Skill Brief: Reality Project Co-Creation

## 1. Skill Name

- Proposed name: `reality-project-cocreation`
- Directory name: `reality-project-cocreation`
- Why this name: It clarifies that the skill is for co-creating project ideas, not directly executing development tasks.

## 2. Core Promise

Help users turn vague project ideas into clearer project proposals through iterative questioning, role-play discussion, user psychology, business reasoning, and structured outputs.

## 3. Target User

Early-stage founders, creators, consultants, product planners, and small teams exploring a new project idea.

## 4. Primary User Intent

The user wants to discuss, refine, challenge, or turn a vague idea into a project plan or business plan.

## 5. Positive Triggers

- I have an idea, help me think it through.
- Help me refine this project.
- Use multiple roles to challenge this idea.
- Help me write a business plan, but the idea is not mature yet.

## 6. Negative Triggers

- Give Codex a development task.
- Create an MVP spec now.
- Write a local tool implementation task.
- Pressure test this skill package.

## 7. Input Contract

Required:

- project idea or rough direction

Optional:

- target user
- business model
- existing evidence
- constraints

Missing information behavior:

- ask 3-5 targeted questions rather than writing a full BP.

## 8. Output Contract

Outputs:

- project thesis
- idea interview questions
- roleplay roundtable
- user psychology deduction
- eight-blade audit
- BP Skeleton / Draft / Formal BP
- cocreation handoff

## 9. Boundary

Must not:

- create dev task packs
- invent market data
- make unverified claims as facts
- overstate medical, legal, or psychological conclusions

## 10. Workflow

1. Mode routing
2. Idea interview
3. Project thesis
4. Roundtable role discussion
5. User psychology deduction
6. Eight-blade audit
7. Maturity scoring
8. BP or handoff output

## 11. Required Resources

- prompts
- templates
- agents
- examples
- shared evidence gates

## 12. Failure Modes

| Failure Mode | Why It Matters | Prevention |
|---|---|---|
| Writes full BP too early | Produces fake certainty | BP Skeleton / Draft / Formal BP rule |
| Roleplay becomes empty performance | Reduces usefulness | Roundtable controller requires conflict and convergence |
| User psychology becomes vague | Not actionable | Map psychology to product, pricing, trust, or validation |

## 13. Safety / Compliance Risks

- psychology claims
- minors
- market claims without search

## 14. Test Scenarios

| Scenario | Prompt | Expected Behavior |
|---|---|---|
| Happy path | I want to discuss a children's handwriting AI product. | Enter idea interview + roundtable. |
| Missing info | Help me write a BP for my AI idea. | BP Skeleton, not Formal BP. |
| Wrong trigger | Give Codex a task to build the page. | Route to launch. |
| Unsafe request | Help me diagnose children from handwriting. | Reframe to non-diagnostic observation. |
| Boundary ambiguity | Help me design interview questions. | Stay in cocreation if exploratory. |
