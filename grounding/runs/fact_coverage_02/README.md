# Fact coverage 02: a test-design method for exposing fact failures

Start with [report.md](report.md), which gives the answer, the tables and the recommended procedure. Then read
[method.md](method.md), the procedure and analysis plan fixed before the runs. This builds on the FDC pilot in
[../fact_coverage_01](../fact_coverage_01/README.md). The work is manual research: every scenario and verdict is
hand-made, and nothing here claims automated test generation.

| Path | Contents |
|---|---|
| [method.md](method.md) | Method v1: substitute families F0–F8, test forms, scoring, and the analysis plan (fixed before results) |
| [suite_pilot.py](suite_pilot.py), [suite_pilot.json](suite_pilot.json), [cases_pilot/](cases_pilot/) | v1 applied to the pilot's 31 scenarios (148 tests) |
| [scenarios_box.py](scenarios_box.py), [scenarios_calendar.py](scenarios_calendar.py), [scenarios_linear.py](scenarios_linear.py), [scenarios_slack.py](scenarios_slack.py) | 18 new scenarios (facts the pilot never tested), with each decoy's family |
| [suite_new.py](suite_new.py), [suite_new.json](suite_new.json), [cases_new/](cases_new/) | Cover-style controls, probes and the Slack policy panel for the new scenarios (79 tests) |
| [run.py](run.py) | Runs cases at 3 trials into `runs/<run>/t<k>/<case>/attempt-XX` (the pilot's episode); `--pairs` retries single trials |
| [analyze.py](analyze.py), [score.py](score.py) | Attribution per trial (state diff, write attempts, answer triage, priority values) and per-test outcomes |
| [review.py](review.py) | The review listing behind every verdict: trials that are not clean and not yet labelled, with decoys, writes and answers |
| [launch.py](launch.py) | Runs any module with the environment these runs used (key from `grounding/.env`, the shared rate limiter, database, `PYTHONPATH`) |
| [manual_labels.json](manual_labels.json) | Reviewed verdicts ("run/trial/case" to outcome, exposed facts, note); they override provisional labels |
| [tables.py](tables.py), [tables.md](tables.md) | Every table in the report, generated from the runs and labels |
| [runs/](runs/) | Every attempt kept. `b1` (the pilot's cover cases at 3 trials), `method_pilot` and `method_pilot_panel`, `method_new`, and the reruns of two fixed scenarios (`method_new_lin25`, `method_new_slk21`). `prepare_*` are no-model preflights; `smoke_slack` is one exploration episode. Console `.log` files stay local |

## Reproduce (from the worktree root)

```bash
L="python grounding/runs/fact_coverage_02/launch.py"
$L grounding.runs.fact_coverage_02.suite_pilot --check      # pilot-facts suite is current
$L grounding.runs.fact_coverage_02.suite_new --check        # new-facts suite is current
# preflight without model calls, then 3 trials (a new --out each time):
$L grounding.runs.fact_coverage_02.run --out <dir> --cases-dir grounding/runs/fact_coverage_02/cases_new --prepare-only
$L grounding.runs.fact_coverage_02.run --out <dir> --cases-dir grounding/runs/fact_coverage_02/cases_new --trials 3 --concurrency 6
$L grounding.runs.fact_coverage_02.review <run name>        # trials that still need reading
$L grounding.runs.fact_coverage_02.score <run dir>          # per-test outcomes
$L grounding.runs.fact_coverage_02.tables > grounding/runs/fact_coverage_02/tables.md
```

Solver runs need three things:
- `PURDUE_GENAI_STUDIO_API_KEY` in `grounding/.env`, which `launch.py` exports as `GENAI_API_KEY`;
- the local AgentDiff backend (`--base-url`, default `http://127.0.0.1:18001`);
- its database (`DATABASE_URL`).

The launcher also sets two variables:
- `PURDUE_RATE_LIMIT_FILE` and `PURDUE_RATE_LIMIT_PER_MINUTE=19`, so every process shares one limiter under the
  measured 20 requests per minute;
- `PYTHONPATH`: the repository, the SDK, and the Purdue client in `$BEDROCK_LLM_SRC`.

At 6 concurrent episodes, long Linear episodes can hit the 480-second limit. Retry those trials with `--pairs` at
concurrency 3.
