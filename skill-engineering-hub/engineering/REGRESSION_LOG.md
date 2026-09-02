# Regression Log

Kit-origin failures and reflowed yao evaluation failures live here.
Columns follow `templates/regression_log.md`; rows with `Source: yao` are
reflowed per `references/yao_reflow.md` (channel 1).

| Date | Version | Failure | Root cause | Fix | Regression test |
|---|---|---|---|---|---|
| 2026-05-16 | 1.0.0 | Initial release | N/A | N/A | Root QUALITY_TESTS.md |

## Yao reflow rows (template)

Copy per failure from `reports/provider_output_evaluation.json`:

| Date | Version | Failure | Root cause | Fix | Regression test |
|---|---|---|---|---|---|
|  |  | Source: yao · case `<case_id>` · <one-line failure> (`provider_output_evaluation.json#failures[i]`) | trigger miss / output violation / evidence gap / safety edge / other | <fix; link contract section if changed> | <Quality Test Plan scenario id added> |
