# Quality Tests: skill-pressure-testing

## Test 1 — Explicit pressure-test request

Prompt:
> 请对这个 skill 做压力测试，看看能不能发布。

Expected behavior:

- Activate `skill-pressure-testing`.
- Inspect the target skill package before judging.
- Write or reuse acceptance criteria before scenarios.
- Run installability checks first.
- Produce a pressure-test report with verdict, scorecard, failures, fixes, and re-test requirements.

## Test 2 — Ordinary skill creation should not trigger pressure testing

Prompt:
> 帮我创建一个餐厅菜单分析 skill。

Expected behavior:

- Do not run pressure testing.
- Route to skill planning / skill creation flow.
- Explain that pressure testing happens after the skill exists.

## Test 3 — Static packaging change uses small scope

Prompt:
> 我只是改了 README 和 MANIFEST，帮我压测一下能不能打包。

Expected behavior:

- Use the smallest sufficient scope.
- Run static installability, frontmatter, forbidden-file, manifest, and archive checks.
- Do not run full with-skill / without-skill behavioral comparison unless explicitly requested.

## Test 4 — Major rewrite requires full pressure run

Prompt:
> 我把原来的单 skill 拆成 router + 两个子 skill，帮我做发布前压测。

Expected behavior:

- Treat as major architecture change.
- Include installability, trigger, router, boundary, regression, execution, and artifact checks.
- Prepare with-skill / without-skill or old-version / new-version comparison when needed.

## Test 5 — Missing evidence cannot become release approval

Prompt:
> 我没有测试输出，但你直接告诉我这个 skill 可以发布吗？

Expected behavior:

- Do not approve release.
- Separate inspected files, assumptions, unknowns, and missing test evidence.
- Return patch / hold / trial-ready rather than ready when evidence is insufficient.

## Test 6 — Contamination control

Prompt:
> 我把评分标准和正确答案一起发给测试 agent，让它跑输出，算不算通过？

Expected behavior:

- Mark the run contaminated.
- Explain that answer-generating agents must see task cards, not grading cards.
- Require a clean re-run before using results for release decisions.
