"""Judge v2 on this study's runs, with each test's answer key read from the keyed suites.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.judge \
        run --trials TRIALS.json --out JUDGED_DIR [--concurrency 4]

judge2 (autogen_02) unchanged, with one input added: the triage refreshes a case's references from the current
cases folders (`fact_coverage_02/analyze.py`, `current`, when the prompt and seed are the same), and this study's
keyed suites are added to those folders. Each attempt keeps the copy of its case taken when it started; the refresh
makes every attempt graded with the final answer key, including the one key corrected after the runs began
(SN0M-CAL-T05: the replica's id for an edited occurrence). Nothing is written into an attempt.
"""
from pathlib import Path

from grounding.runs.autogen_02.kit import judge2
from grounding.runs.fact_coverage_02 import analyze

HERE = Path(__file__).resolve().parent
analyze.SOURCES = list(analyze.SOURCES) + [HERE / "runs" / "suite_sn0m_01", HERE / "runs" / "suite_sn1m_01"]

if __name__ == "__main__":
    judge2.main()
