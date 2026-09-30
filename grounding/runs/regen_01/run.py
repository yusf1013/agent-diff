"""openclaw_eval_01's runner, unchanged, for this study's cases folders: OpenClaw on the self-hosted Qwen, k trials per
test, leaving out what the rulings leave out. The only difference is that rules.py is imported first, so the rulings
recognize this study's near misses under their opaque ids.

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.run \
        --out grounding/runs/regen_01/runs/<run> --cases-dir grounding/runs/regen_01/runs/<run>_cases \
        [--trials 3] [--concurrency 24] [--retry-infrastructure]

Start the self-host proxy first (openclaw_eval_01/run.py's docstring), unless another session already serves it.
"""
from grounding.runs.regen_01 import rules  # noqa: F401  (before the runner reads the rulings)
from grounding.runs.openclaw_eval_01 import run

if __name__ == "__main__":
    run.main()
