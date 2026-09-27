"""CAL-02 and CAL-11 with weekly series the Calendar replica can list (run on both harnesses).

    python -m grounding.runs.openclaw_transfer_01.cases_repaired      # writes cases/calendar/*.json

The pilot seeds start these weekly series on 2018-05-01. The replica's events.list defaults timeMin to its
fixed now (2018-06-17) and drops a recurring series whose *first* occurrence ended before timeMin, so every
list call without an early timeMin returns nothing in both the toy harness and OpenClaw, and the agent never
sees the series or its occurrences. Here each series starts on its first occurrence in the case week instead.
Prompts, occurrences, targets and claims are otherwise unchanged; every claim is re-checked mechanically.
See ../fact_coverage_01/corrections.md for the effect on the pilot's evidence.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from functools import partial
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot import cases_calendar as C
from grounding.runs.fact_coverage_01.pilot.cases_altsweep import build as alt_build
from grounding.runs.fact_coverage_01.pilot.cases_told import told
from grounding.runs.fact_coverage_01.pilot.common import finish

HERE = Path(__file__).resolve().parent
FIRST_DAY = {"TU": "2018-06-19", "WE": "2018-06-20"}
RENAME = re.compile(r"\b(CAL-\d\d)(?=\b|-|\.)")


def repaired(builder):
    case = copy.deepcopy(builder())
    for key in ("case_id", "variant_of"):
        if key in case:
            case[key] = RENAME.sub(r"\1R", case[key], count=1)
    for ref in case["references"]:
        ref["id"] = RENAME.sub(r"\1R", ref["id"], count=1)
    for event in case["seed"]["calendar_events"]:
        rule = " ".join(event.get("recurrence") or [])
        if "BYDAY=" in rule and str(event.get("start_datetime", "")).startswith("2018-05-01"):
            day = FIRST_DAY[rule.split("BYDAY=")[1][:2]]
            for key in ("start_datetime", "end_datetime"):
                event[key] = day + event[key][10:]
            for key in ("start", "end"):
                event[key] = dict(event[key], dateTime=day + event[key]["dateTime"][10:])
    case["notes"] = (case.get("notes", "") + " Repaired seed: each weekly series starts on its first occurrence "
                     "in the case week so the replica's events.list returns it.").strip()
    return case


def builders():
    absent = partial(repaired, partial(C.cal_02, form="absent"))
    yield partial(repaired, C.cal_02)
    yield absent
    yield partial(told, absent)
    base = absent()
    for ci, claim in enumerate(base["references"][0]["claims"]):
        if claim.get("alternative"):
            yield partial(alt_build, absent, 0, ci)
    yield partial(repaired, C.cal_11)


def main() -> None:
    out = HERE / "cases" / "calendar"
    out.mkdir(parents=True, exist_ok=True)
    for builder in builders():
        case, results, errors = finish(builder())
        if errors:
            raise SystemExit(f"{case['case_id']}: {errors}")
        credited = sorted({c["requirement"] for r in results for c in r["claims"] if c["credited"]})
        case["coverage_claims"] = credited
        case["case_sha256"] = hashlib.sha256(json.dumps({k: v for k, v in case.items() if k != "case_sha256"},
                                                        sort_keys=True).encode()).hexdigest()
        (out / f"{case['case_id']}.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
        print(case["case_id"], "credited:", credited)


if __name__ == "__main__":
    main()
