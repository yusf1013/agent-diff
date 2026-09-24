"""No-target cases with explicit permission to report absence (neutralizes the presupposition)."""
from __future__ import annotations

import copy
from functools import partial

from grounding.runs.fact_coverage_01.pilot import cases_box as B
from grounding.runs.fact_coverage_01.pilot import cases_calendar as C
from grounding.runs.fact_coverage_01.pilot import cases_linear as L
from grounding.runs.fact_coverage_01.pilot.variants import absent_of


def told(builder, plural=False):
    case = copy.deepcopy(builder())
    case["variant_of"] = case["case_id"]
    case["case_id"] += "-TOLD"
    case["prompt"] += " If there aren't any, just tell me." if plural else " If there isn't one, just tell me."
    for r in case["references"]:
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    return case


BOX = [(B.box_02, False), (partial(B.box_03, form="absent"), False), (partial(B.box_05, form="absent"), True),
       (B.box_06, False), (partial(B.box_07, form="absent"), False), (partial(B.box_08, form="absent"), False)]
LINEAR = [(L.lin_02, False), (L.lin_04, False)] + [
    (partial(lambda b: absent_of(b()), b), plural) for b, plural in
    [(L.lin_01, False), (L.lin_03, False), (L.lin_05, True), (L.lin_06, True), (L.lin_07, False), (L.lin_09, False)]] + [
    (partial(b, form="absent"), False) for b in (L.lin_10, L.lin_11, L.lin_12, L.lin_14)]
CALENDAR = [(partial(C.cal_01, form="absent"), False), (partial(C.cal_02, form="absent"), False), (C.cal_03, False),
            (partial(C.cal_04, form="absent"), False), (C.cal_05, False), (partial(C.cal_06, form="absent"), False),
            (partial(C.cal_07, form="absent"), False), (C.cal_08, False), (partial(C.cal_09, form="absent"), False)]
BOX += [(partial(B.box_09, form="absent"), False)]
LINEAR += [(partial(L.lin_15, form="absent"), False)]

CASES = [partial(told, b, p) for b, p in BOX + LINEAR + CALENDAR]

CASES += [partial(told, partial(L.lin_17, form="absent")), partial(told, partial(B.box_11, form="absent"))]
