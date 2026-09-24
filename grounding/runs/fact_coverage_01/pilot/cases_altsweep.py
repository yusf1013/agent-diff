"""ALT sweep: every claim with a designated alternative, isolated (one near-miss, no target), absence permitted."""
from __future__ import annotations

import copy
from functools import partial

from grounding.runs.fact_coverage_01.pilot import cases_box as B
from grounding.runs.fact_coverage_01.pilot import cases_calendar as C
from grounding.runs.fact_coverage_01.pilot import cases_linear as L
from grounding.runs.fact_coverage_01.pilot.variants import absent_of, isolate

ABSENT_SOURCES = {
    "box": [partial(B.box_01, form="absent"), B.box_02, partial(B.box_03, form="absent"), B.box_04,
            partial(B.box_05, form="absent"), B.box_06, partial(B.box_07, form="absent"), partial(B.box_08, form="absent")],
    "calendar": [partial(C.cal_01, form="absent"), partial(C.cal_02, form="absent"), C.cal_03,
                 partial(C.cal_04, form="absent"), C.cal_05, partial(C.cal_06, form="absent"),
                 partial(C.cal_07, form="absent"), C.cal_08],
    "linear": [L.lin_02, L.lin_04] + [partial(lambda b: absent_of(b()), b)
                                      for b in (L.lin_01, L.lin_03, L.lin_05, L.lin_07, L.lin_09)],
}


def build(builder, ref_index, claim_index):
    case = isolate(builder(), ref_index, claim_index)
    kept = case["references"][ref_index]["claims"][0]
    case["case_id"] = f"ALT-{case['case_id']}"
    case["prompt"] += " If there isn't one, just tell me."
    case["altsweep"] = {"requirement": kept["requirement"], "alternative": kept.get("alternative")}
    for r in case["references"]:
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    return case


CASES = []
for domain, builders in ABSENT_SOURCES.items():
    for b in builders:
        base = b()
        for ri, ref in enumerate(base["references"]):
            if ref["expected"]:
                continue  # only no-target references
            for ci, c in enumerate(ref["claims"]):
                if c.get("alternative"):
                    CASES.append(partial(build, b, ri, ci))
