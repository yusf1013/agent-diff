"""Calendar isolated one-near-miss variants of absent-form cases."""
from __future__ import annotations

from functools import partial

from grounding.runs.fact_coverage_01.pilot import cases_calendar as C
from grounding.runs.fact_coverage_01.pilot.variants import isolate

ABSENT = [partial(C.cal_01, form="absent"), partial(C.cal_02, form="absent"), C.cal_03, C.cal_05,
          partial(C.cal_06, form="absent"), partial(C.cal_07, form="absent")]


def _iso(builder, k):
    return isolate(builder(), 0, k)


CASES = [partial(_iso, b, k) for b in ABSENT for k in range(len(b()["references"][0]["claims"]))]
