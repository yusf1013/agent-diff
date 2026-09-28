"""The blind sample for judging this study's runs: trials drawn at random from a cases folder before the run, which I
label by hand before reading any verdict on them. autogen_02's drawer, with this study as its home.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.blind_sample CASES_DIR RUN_NAME N SEED

Writes eval/blind_<RUN_NAME>.json here. The draw uses only the cases folder, so it cannot depend on any outcome.
"""
from pathlib import Path

from grounding.runs.autogen_02.kit import blind_sample

if __name__ == "__main__":
    blind_sample.STUDY = Path(__file__).resolve().parent
    (blind_sample.STUDY / "eval").mkdir(exist_ok=True)
    blind_sample.main()
