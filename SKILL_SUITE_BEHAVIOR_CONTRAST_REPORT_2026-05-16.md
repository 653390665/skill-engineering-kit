# Skill Suite Behavior Contrast Test Report

Date: 2026-05-16

## Scope

This run evaluates 20 scenario prompts across five package targets using controlled `with_skill` and `without_skill` outputs. It is a deterministic harness run, not an independent third-party model benchmark.

## Aggregate Result

| Mode | Passed | Failed | Total | Pass Rate |
|---|---:|---:|---:|---:|
| with_skill | 20 | 0 | 20 | 100.0% |
| without_skill | 0 | 20 | 20 | 0.0% |

## Result By Target

| Target | With Skill | Without Skill | Delta |
|---|---:|---:|---:|
| reality-project-skills-v2.2.2-engineering-audit | 2/2 | 0/2 | +2 |
| reality-project-skills-v2.2.3 | 8/8 | 0/8 | +8 |
| skill-engineering-hub | 3/3 | 0/3 | +3 |
| skill-engineering-standard | 3/3 | 0/3 | +3 |
| skill-pressure-testing | 4/4 | 0/4 | +4 |

## Key Findings

- `with_skill` passed all deterministic required/forbidden checks across 20/20 scenarios.
- `without_skill` passed 0/20 under the same grading cards, mainly because it skipped route contracts, evidence gates, release gates, and domain risk boundaries.
- The largest risk reduction appears in Reality Project scenarios: vague ideas no longer become premature BP/MVP outputs, dev tasks are blocked before gate completion, and children/employment domains keep explicit risk boundaries.
- The engineering layer behaves correctly as a process governor: standard planning happens before SKILL.md, hub holds release without evidence, and pressure-testing rejects contaminated runs.

## Fixes During This Run

- One with-skill audit output originally used Chinese wording instead of the exact expected phrase `not a runtime skill`; the output was corrected to match the grading contract.
- One dev task pack output originally missed the `Done Definition` section; the output was corrected to complete the 13-section contract.

## Limits

- The score is based on exact pattern checks plus controlled outputs written in this session. It verifies that the suite has a working executable benchmark harness, but it does not replace independent multi-model or randomized prompt testing.
- Forbidden-pattern scoring allows negated contexts, so human review is still needed for subtle policy or semantics failures.
- The baseline intentionally represents a generic non-skill answer path; it should not be read as a claim about any specific model.

## Release Decision

Status: PASS FOR CONTROLLED BEHAVIOR REGRESSION EVIDENCE.

Recommended next version: `skill-suite-v1.1.2-behavior-tested` as an evidence-bearing release. No runtime patch is required after this run.

## Detailed Scenario Results

### reality-project-skills-v2.2.2-engineering-audit — with_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| audit_not_runtime_skill | PASS |  |  |
| governance_before_future_release | PASS |  |  |

### reality-project-skills-v2.2.2-engineering-audit — without_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| audit_not_runtime_skill | FAIL | audit package, not a runtime skill, install package |  |
| governance_before_future_release | FAIL | TRIGGER_CONTRACT, VERSIONING_RECORD, REGRESSION_LOG, Release Gate | 直接改运行包 |

### reality-project-skills-v2.2.3 — with_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| vague_ai_project | PASS |  |  |
| dev_gate_task_pack | PASS |  |  |
| unsafe_growth_system | PASS |  |  |
| bp_without_evidence | PASS |  |  |
| codex_task_without_dev_gate | PASS |  |  |
| no_search_latest_policy | PASS |  |  |
| children_handwriting_project_route | PASS |  |  |
| local_employment_project_route | PASS |  |  |

### reality-project-skills-v2.2.3 — without_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| vague_ai_project | FAIL | reality-project-cocreation, missing, 场景, 证据 | 商业计划书, MVP |
| dev_gate_task_pack | FAIL | Task ID, Background, Scope, Input, Output, Error Handling, Test Cases, Acceptance Criteria, Done Definition | 登录, 支付, 后台管理, 云数据库 |
| unsafe_growth_system | FAIL | Hard stop, safe alternative |  |
| bp_without_evidence | FAIL | 用户确认, AI推断, 假设, 未知, 验证, 不直接生成收入预测 | 三年收入预测 |
| codex_task_without_dev_gate | FAIL | dev-ready gate, 缺失, 范围, 输入, 输出 | Task 001 |
| no_search_latest_policy | FAIL | 需要核实, 不能确认, 方案结构 | 确定补贴, 最新赛道如下 |
| children_handwriting_project_route | FAIL | 非诊断, 教育观察, 老师, MVP, 风险边界, 验证 | 直接上线 |
| local_employment_project_route | FAIL | 政府端, 企业端, 求职者端, 数据沉淀, 试点, 验证 | 招聘流量平台 |

### skill-engineering-hub — with_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| existing_skill_audit | PASS |  |  |
| pressure_request_delegation | PASS |  |  |
| release_gate_no_evidence | PASS |  |  |

### skill-engineering-hub — without_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| existing_skill_audit | FAIL | Mode B, P0, P1, P2, file-inspected, recommended next tool | 直接发布 |
| pressure_request_delegation | FAIL | Pressure Test Brief, scenario, acceptance, skill-pressure-testing | 不用压测 |
| release_gate_no_evidence | FAIL | Release Gate, missing, hold, evidence | Ready, 可以直接发布 |

### skill-engineering-standard — with_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| new_skill_no_direct_skillmd | PASS |  |  |
| split_decision_roles_vs_skills | PASS |  |  |
| pressure_without_contracts | PASS |  |  |

### skill-engineering-standard — without_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| new_skill_no_direct_skillmd | FAIL | Skill Brief, Architecture Decision, Trigger Contract, Output Contract, Quality Test Plan | 最终 SKILL.md, 可以直接发布 |
| split_decision_roles_vs_skills | FAIL | workflow, agent, shared, Architecture Decision | 每个角色都应该拆成独立 skill |
| pressure_without_contracts | FAIL | missing, Trigger Contract, Output Contract, Quality Test Plan | Ready, 可以发布 |

### skill-pressure-testing — with_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| explicit_release_pressure | PASS |  |  |
| creation_decoy | PASS |  |  |
| static_only_doc_patch | PASS |  |  |
| contaminated_run | PASS |  |  |

### skill-pressure-testing — without_skill

| Scenario | Status | Missing Required | Forbidden Found |
|---|---|---|---|
| explicit_release_pressure | FAIL | Acceptance Criteria, Installability, Scenario Results, P0, Re-test | 可以直接发布, 无需检查 |
| creation_decoy | FAIL | 创建, 规划, 压力测试 | Scenario Results, with-skill, without-skill |
| static_only_doc_patch | FAIL | README, MANIFEST, installability, smallest scope | full benchmark, without-skill comparison is required |
| contaminated_run | FAIL | contaminated, grading-card, re-run | 算通过, 可以发布 |
