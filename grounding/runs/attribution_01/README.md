# attribution_01

Roadmap step 5, first investigation: when a trial fails, which component owns the failure? The candidates are the
agent, the test's wording, the test's construction, the mock, and the harness. The study scores four evidence
sources against 722 hand-labelled trials.

- **Start with:** [report.md](report.md) (results, contested cases, recommendation), then [plan.md](plan.md) (the
  pre-registered plan and its dated amendments).
- **For the PI:** [contested.json](contested.json) lists four questions (C1–C4) that decide 29 trials' owners.

Reproduce, from the repository root (the kit's Python; see `grounding/runs/fact_coverage_02/launch.py`):

```bash
python grounding/runs/attribution_01/build_devset.py        # devset.json (no model calls)
python grounding/runs/attribution_01/score_judge.py         # source 1: the judges' artifact calls
python grounding/runs/fact_coverage_02/launch.py grounding.runs.attribution_01.precheck    # source 2 (local replica)
python grounding/runs/attribution_01/scan_traces.py         # source 3: the trace scan
python grounding/runs/fact_coverage_02/launch.py grounding.runs.attribution_01.objection_reader score   # source 4
```

Source 4's readings are cached in objection_reader/. Rerunning `objection_reader run` without them calls Muse (about
$2.50 at list for 58 trials).
