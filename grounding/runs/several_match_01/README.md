# several_match_01

*A pilot, superseded by [../several_match_02](../several_match_02) (2026-09-28). It measured Qwen on hand-built
tests and does not answer the design question.*

Roadmap step 5, second investigation: when a request asks to act on every record that matches, does the agent act
on all of them and on nothing else? The study uses 8 hand-written plural scenarios with 4 targets each, placed on or
off the natural retrieval route, plus 3 near misses each. It ran on the self-hosted Qwen, at 3 trials per test.

- **Start with:** [report.md](report.md), then [plan.md](plan.md).
- **Result:** 22 of 24 trials acted on exactly the target set, with no near miss acted on. There was one pagination
  miss (Linear, default page, no filter) and one harness failure (API calls from a Python script bypass the
  executor's proxy).

Reproduce, from the repository root:

```bash
python grounding/runs/several_match_01/scenarios.py                                   # scenarios/, placements.json
python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_01.build   # cases/, checks/ (local replica)
SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.solve \
    --cases-dir grounding/runs/several_match_01/cases --out grounding/runs/several_match_01/runs/NEW --trials 3 --concurrency 8
python grounding/runs/several_match_01/grade.py grounding/runs/several_match_01/runs/NEW
```
