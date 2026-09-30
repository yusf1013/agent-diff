"""openclaw_eval_01's runner, unchanged, for this study's suite: OpenClaw on the self-hosted Qwen, k trials per test,
leaving out what this study's rulings leave out (rules.py is imported first; see there).

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.run \
        --out grounding/runs/qwen_writer_01/runs/oc_01 --cases-dir grounding/runs/qwen_writer_01/suite/cases \
        --trials 3 --concurrency 16 [--retry-infrastructure]

The self-host proxy (port 18778) must be up; openclaw_eval_01/run.py's docstring says how to start it.
"""
from grounding.runs.qwen_writer_01 import rules  # noqa: F401  (before the runner reads the rulings)
from grounding.runs.openclaw_eval_01 import run

if __name__ == "__main__":
    run.main()
