# Fact-discrimination coverage (FDC): criterion, catalogs and Qwen pilot

Start with [report.md](report.md) (the answer and the main tables), then [criterion.md](criterion.md) (the
definition) and [findings.md](findings.md) (every reviewed run, with links). Later corrections to the held-fact evidence are in
[corrections.md](corrections.md). Manual research work; no automated
test-generation claim.

Follow-up: [fact_coverage_02](../fact_coverage_02/README.md) turns the pilot into a test-design method. It runs the
method at 3 trials on the pilot's facts and on new facts in all four domains, and reruns this pilot's cover cases at
3 trials.

| Path | Contents |
|---|---|
| [catalog/](catalog/) | Curated fact inventories ([facts.py](catalog/facts.py)), builder with full column/relationship accounting ([build.py](catalog/build.py)), per-domain requirement catalogs (`<domain>.json`), [counts.md](catalog/counts.md) |
| [fdc.py](fdc.py) | Reference-query language, fact mutations (DROP, SUB, SPLIT, LEVEL, REPLACE) and the credit check |
| [pilot/cases_*.py](pilot/) | Case designs: packed cover cases per domain, and experimental controls (target flips, isolated near-misses, plain vs alternative contrast, absence-permitted, far misses, wording) |
| [pilot/cases/](pilot/cases/) | Built cases (solver-visible prompt, acting user, seed; private references, claims, cards, task specs) |
| [pilot/coverage.json](pilot/coverage.json), [pilot/checks.json](pilot/checks.json) | Credited requirements per cover case; per-claim mechanical results |
| [pilot/runs/](pilot/runs/) | Every attempt kept: `qwen_*` solver runs, `qwen38_slack_bridge*` Slack reruns, `prepare_*` no-model fixture checks. Each attempt's `execution_summary.json` records its status and usage; console `.log` files stay local (git ignores them) |
| [pilot/results.json](pilot/results.json), [pilot/fact_table.md](pilot/fact_table.md) | Aggregated outcomes (with [manual corrections](pilot/manual_labels.json)) and per-fact table |

## Reproduce (from the worktree root)

```bash
python3 -m grounding.runs.fact_coverage_01.catalog.build          # catalogs and counts (checks accounting)
python3 -m grounding.runs.fact_coverage_01.pilot.build            # cases, mechanical credit checks, coverage
# fixture check without model calls, then a solver run (new --out each time):
python -m grounding.runs.fact_coverage_01.pilot.run --out <new dir> --cases BOX-01 --prepare-only
python -m grounding.runs.fact_coverage_01.pilot.run --out <new dir> --cases BOX-01 --concurrency 4
python3 -m grounding.runs.fact_coverage_01.pilot.results <run dirs> --json out.json   # provisional outcomes
python3 -m grounding.runs.fact_coverage_01.pilot.fact_table <run dirs>                # per-fact table
python3 -m grounding.runs.fact_coverage_01.pilot.report_data                          # report tables and evidence links
python3 -m grounding.runs.fact_coverage_01.pilot.held                                 # strict / lenient fact counts
python3 -m grounding.runs.fact_coverage_01.pilot.slack_suite_map                      # 57-case Slack suite vs catalog
python3 -m grounding.runs.fact_coverage_01.pilot.show <attempt dir>                   # read one trajectory
```

Solver runs need the environment in [solver/README.md](../../solver/README.md) (local backend on 18001, database,
executor image, shared Purdue limiter, `GENAI_API_KEY`). Box/Calendar/Linear seeds are installed by
[custom_runtime.py](../../integrations/agentdiff/custom_runtime.py); Slack reruns use the unchanged Purdue runner
through [pilot/slack_bridge.py](pilot/slack_bridge.py). Model: `qwen3.8:27b` (the recorded `qwen3.6:27b` is no longer
served).

Automatic attribution (which near-miss a run acted on, from the state diff) is provisional. Failures cited in the
report were read manually; corrections are in [pilot/manual_labels.json](pilot/manual_labels.json).
