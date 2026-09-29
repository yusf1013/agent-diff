# report_01: evaluation and results, a paper stub

[report.md](report.md) is the stub for a paper's evaluation and results sections, written 2026-09-29 over the
studies before it: [fact_coverage_01](../fact_coverage_01/README.md) (the catalog and the credit rule),
[autogen_01](../autogen_01/README.md) and [autogen_02](../autogen_02/overview.md) (the generator, the judge and the
toy harness's runs), [openclaw_eval_01](../openclaw_eval_01/README.md) and [completion_01](../completion_01/README.md)
(roadmap 6a and 6b on OpenClaw), and [judge_baselines_01](../judge_baselines_01/README.md) (6c). Two sections
report studies on other branches: the generator baselines (`exp/baselines-01`) and step 5's extensions
(`exp/automation-01`).

| Path | What |
|---|---|
| [report.md](report.md) | The report |
| [report_concise.md](report_concise.md) | Shorter report: 1,006 methodology cases, final OpenClaw executions, combined writer groups, and estimated solver costs |
| [kit/](kit/) | One script per table group; each reads committed run records and writes one JSON file. No model calls, no agent runs |
| [numbers/](numbers/) | The scripts' outputs, which the report's tables cite |

Run a script from the repository root with the kit's Python (the backend's virtualenv):

```bash
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.coverage   # RQ1, RQ2 (first)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.generator  # RQ3
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.exposure   # RQ4 (needs coverage)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.judge      # RQ5
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.policy_space  # RQ6 (needs coverage)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.beyond     # RQ7
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.mechanisms # §10
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.scale      # §0.4
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.costs      # §12
python -m grounding.runs.report_01.kit.qwen_usage                                    # §0.4: exact Qwen/OpenClaw tokens, including RQ8
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.concise  # concise report: writes only numbers/concise.json
```

`concise.py` selects final executions, combines writers, filters the blind-label and judge-comparison samples,
and recomputes the equal-budget Muse comparison. It reads baseline summaries from `runs/baselines_01` or, if
still unmerged, `.claude/worktrees/baselines-01/grounding/runs/baselines_01`, and includes those summaries in its
output. The concise report's token estimate scales the historical average to 3,018 executions; it is not an
exact usage audit of that subset. Its price table states the rates, sources and calculation separately.

`numbers/awareness_full_03.json` and `numbers/awareness_full_04.json` come from openclaw_eval_01's
`test_awareness.py` on those runs.

`qwen_usage.py` uses only the Python standard library and reads the original proxy metadata, including cached
input and missing usage, without changing run evidence. It separates the main evaluation, RQ8's fresh baseline
and ablation runs, and stopped/smoke runs. If the baseline branch is still separate, pass
`--baselines-root .claude/worktrees/baselines-01/grounding/runs/baselines_01` from the repository root.
