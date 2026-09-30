"""B1's blind sample: trials drawn at random from the run's cases folder before the run (autogen_02's drawer), labelled by
hand before any oracle output.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.b1.blind_sample CASES_DIR RUN N SEED
"""
from pathlib import Path
import sys
from grounding.runs.autogen_02.kit import blind_sample
blind_sample.STUDY = Path("grounding/runs/related_work_01/b1").resolve()
(blind_sample.STUDY / "eval").mkdir(exist_ok=True)
blind_sample.main()
