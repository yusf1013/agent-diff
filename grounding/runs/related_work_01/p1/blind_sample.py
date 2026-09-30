"""P1's blind sample: trials drawn at random from the run's cases folder before the run (autogen_02's drawer), labelled
by hand before reading any judge verdict.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.p1.blind_sample CASES_DIR RUN N SEED
"""
from pathlib import Path

from grounding.runs.autogen_02.kit import blind_sample

if __name__ == "__main__":
    blind_sample.STUDY = Path(__file__).resolve().parent
    (blind_sample.STUDY / "eval").mkdir(exist_ok=True)
    blind_sample.main()
