"""openclaw_eval_01's runner, unchanged, for this study's suite: OpenClaw on the self-hosted Qwen, k trials per test.

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.run \
        --out grounding/runs/qwen_writer_01/runs/oc_01 --cases-dir grounding/runs/qwen_writer_01/suite/cases \
        --trials 3 --concurrency 16 [--retry-infrastructure]

At selection the run applies rulings_run.json, which leaves nothing out: every test runs, the probes of the 2 near
misses I ruled flawed included, so that the PI can overrule those rulings without a re-run. My rulings
(rulings.json, through rules.py) are applied in adjudication (adjudicate.py). The self-host proxy (port 18778)
must be up; openclaw_eval_01/run.py's docstring says how to start it.
"""
from grounding.runs.qwen_writer_01 import rules
from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.openclaw_eval_01 import run

RUN_RULINGS = rules.HERE / "rulings_run.json"
rulings.KNOWN_DEFECTS = RUN_RULINGS
run.KNOWN_DEFECTS = RUN_RULINGS
rulings._doc.cache_clear()

if __name__ == "__main__":
    run.main()
