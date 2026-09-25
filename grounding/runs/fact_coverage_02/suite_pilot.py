"""Method v1 (method.md) applied to the pilot's 31 cover scenarios. No service calls.

    python -m grounding.runs.fact_coverage_02.suite_pilot [--check]

Writes cases_pilot/<domain>/<case_id>.json and suite_pilot.json (every test with its form, fact and substitute
family). The family table was fixed before any v1 test ran; it classifies each decoy by the rules in method.md.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from functools import partial
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot import cases_box as B
from grounding.runs.fact_coverage_01.pilot import cases_calendar as C
from grounding.runs.fact_coverage_01.pilot import cases_linear as L
from grounding.runs.fact_coverage_01.pilot.cases_told import BOX, CALENDAR, LINEAR
from grounding.runs.fact_coverage_01.pilot.common import finish
from grounding.runs.fact_coverage_01.pilot.variants import absent_of, cascade_remove, isolate

HERE = Path(__file__).resolve().parent
PILOT_CASES = HERE.parent / "fact_coverage_01" / "pilot" / "cases"

# Substitute family per decoy claim, keyed (scenario, "I<reference><claim>"). See method.md for the families.
FAMILY = {
    "BOX-01": {"I11": "F1", "I12": "F0", "I13": "F4", "I14": "F1", "I15": "F8", "I16": "F8"},
    "BOX-02": {"I11": "F5", "I12": "F1", "I13": "F0", "I14": "F8", "I15": "F0", "I16": "F0"},
    "BOX-03": {"I11": "F0", "I12": "F1", "I13": "F1", "I14": "F0", "I15": "F5", "I16": "F0"},
    "BOX-04": {"I11": "F1", "I12": "F5", "I13": "F2"},
    "BOX-05": {"I11": "F2", "I12": "F0", "I13": "F0", "I14": "F0"},
    "BOX-06": {"I11": "F1", "I12": "F1", "I13": "F5", "I14": "F4", "I15": "F0"},
    "BOX-07": {"I11": "F1", "I12": "F0", "I13": "F7", "I14": "F7"},
    "BOX-08": {"I11": "F5", "I12": "F0", "I13": "F0", "I14": "F7", "I15": "F1"},
    "BOX-09": {"I11": "F2", "I12": "F1", "I13": "F1", "I14": "F0"},
    "CAL-01": {"I11": "F5", "I12": "F0", "I13": "F1", "I14": "F7", "I15": "F8", "I16": "F6"},
    "CAL-02": {"I11": "F6", "I12": "F1", "I13": "F8", "I14": "F7"},
    "CAL-03": {"I11": "F7", "I12": "F2", "I13": "F8", "I14": "F8"},
    "CAL-04": {"I11": "F6"},
    "CAL-05": {"I11": "F1", "I12": "F0", "I13": "F0", "I14": "F0"},
    "CAL-06": {"I11": "F6", "I12": "F1", "I13": "F7"},
    "CAL-07": {"I11": "F1", "I12": "F0", "I13": "F5"},
    "CAL-08": {"I11": "F6", "I12": "F7"},
    "CAL-09": {"I11": "F2", "I12": "F1", "I13": "F7"},
    "LIN-01": {"I11": "F1", "I12": "F0", "I13": "F2", "I14": "F0", "I15": "F0"},
    "LIN-02": {"I11": "F0", "I12": "F1", "I13": "F2", "I14": "F8"},
    "LIN-03": {"I11": "F0", "I12": "F1", "I13": "F0", "I14": "F0"},
    "LIN-04": {"I11": "F3", "I12": "F0", "I13": "F8", "I14": "F0"},
    "LIN-05": {"I11": "F6", "I12": "F0", "I13": "F0", "I14": "F6", "I15": "F0", "I16": "F0"},
    "LIN-06": {"I11": "F0", "I12": "F0", "I13": "F0", "I14": "F5", "I15": "F4"},
    "LIN-07": {"I11": "F1", "I12": "F2", "I13": "F0"},
    "LIN-09": {"I11": "F5", "I12": "F0", "I13": "F1", "I14": "F2"},
    "LIN-10": {"I11": "F4", "I12": "F1", "I13": "F8"},
    "LIN-11": {"I11": "F1"},
    "LIN-12": {"I11": "F4", "I12": "F0", "I13": "F8"},
    "LIN-14": {"I11": "F4", "I12": "F0"},
    "LIN-15": {"I11": "F2", "I12": "F4", "I13": "F1", "I14": "F0"},
}

# Decoys that only mean something next to another row: the probe keeps that row (noted on the test).
KEEP = {("BOX-02", "I14"): ["2005"]}  # the empty namesake needs the Finance Archive copy that carries the comment

# Time or quantity facts whose pilot decoy is not a nearest value: add an F7 decoy that is (method.md).
NEAREST = [
    ("BOX-08", "I13", "box_tasks", "item_id", "due_at", "2026-10-01T09:00:00", "Due October 1, the boundary of 'before October 1'."),
    ("LIN-01", "I12", "issues", "id", "priority", 3, "Medium priority, the nearest below High."),
    ("LIN-05", "I13", "issues", "id", "estimate", 4, "Estimated at 4, the nearest below 5."),
    ("LIN-05", "I15", "issues", "id", "dueDate", "2026-09-23", "Due today, the boundary of 'past its due date'."),
]

# Scenarios whose answer is a set: they also get the scenario as written (target-present layer).
SET_VALUED = ["BOX-05", "CAL-04", "LIN-05", "LIN-06"]

# Policy panel per domain: P1 presupposed no-target, P2 one plain decoy presupposed, P3 underspecified twin target.
PANEL_EXISTING = {"box": ["BOX-01-A", "BOX-01-A-I12"], "calendar": ["CAL-06-A"], "linear": ["LIN-01-A", "LIN-01-A-I15"]}
TWINS = {  # scenario builder, new id, field changes for the clone of the (single) target
    "box": (partial(B.box_01), "1099", {"name": "Q3 cost summary.pdf"}),
    "calendar": (partial(C.cal_09), "ev_twin", {"summary": "Roadmap sync", "ical_uid": "ev_twin@northwind.example"}),
    "linear": (partial(L.lin_15), "i-w9", {"title": "Update empty states", "number": 99, "identifier": "WEB-99"}),
}


def sources():
    """Absent-form builder and plural flag per scenario, as in the pilot's 'just tell me' cases."""
    out = {}
    for builder, plural in BOX + [(partial(B.box_01, form="absent"), False), (B.box_04, False)] + LINEAR + CALENDAR:
        case = builder()
        scenario = case["case_id"].split("-A")[0]
        out.setdefault(scenario, (builder, plural))
    return out


def told(case, plural):
    case["prompt"] += " If there aren't any, just tell me." if plural else " If there isn't one, just tell me."
    return case


def rename(case, new_id):
    case["case_id"] = new_id
    for r in case["references"]:
        r["id"] = new_id + r["id"][r["id"].index("."):]
    return case


def keep_claims(case, ref_index, keep):
    """No target; keep only the decoys of the listed claim indices (packed plain test)."""
    case = copy.deepcopy(case)
    ref = case["references"][ref_index]
    drop = [str(x) for x in ref["expected"]] + [str(c["witness"]) for i, c in enumerate(ref["claims"]) if i not in keep]
    table = ref["query"]["table"]
    if table in case["seed"]:
        cascade_remove(case["seed"], case["domain"], table, drop)
    gone = set(drop)
    case["probes"] = [p for p in case.get("probes", []) if not any(g in json.dumps(p) for g in gone)]
    ref["expected"], ref["resolution"] = [], "absent"
    ref["claims"] = [c for i, c in enumerate(ref["claims"]) if i in keep]
    case["form"], case["mode"] = "absent", "absent"
    return case


def nearest_variant(case, ref_index, claim_index, table, key, field, value):
    case = copy.deepcopy(case)
    witness = str(case["references"][ref_index]["claims"][claim_index]["witness"])
    rows = [r for r in case["seed"][table] if str(r.get(key)) == witness]
    if len(rows) != 1:
        raise ValueError(f"{case['case_id']}: expected one {table} row with {key}={witness}, found {len(rows)}")
    rows[0][field] = value
    return case


def twin_case(builder, new_id, changes):
    case = copy.deepcopy(builder())
    ref = case["references"][0]
    table = ref["query"]["table"]
    target = str(ref["expected"][0])
    row = copy.deepcopy(next(r for r in case["seed"][table] if str(r["id"]) == target))
    row.update({"id": new_id, **changes})
    case["seed"][table].append(row)
    ref["expected"] = [ref["expected"][0], new_id]
    ref["resolution"] = "underspecified"
    case["form"], case["mode"] = "present", "underspecified"
    case["variant_of"] = case["case_id"]
    return rename(case, f"{case['case_id']}-TWIN")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def build():
    tests, cases = [], []

    def add(case, form, scenario, fact=None, family=None, note=""):
        case, results, errs = finish(case)
        if errs:
            raise SystemExit(f"{case['case_id']}: {errs}")
        case["coverage_claims"] = sorted({c["requirement"] for r in results for c in r["claims"] if c["credited"]})
        case["case_sha256"] = digest({k: v for k, v in case.items() if k != "case_sha256"})
        cases.append(case)
        tests.append({"case_id": case["case_id"], "domain": case["domain"], "form": form, "scenario": scenario,
                      "fact": fact, "family": family, "note": note})

    for scenario, (builder, plural) in sorted(sources().items()):
        base = builder()
        for ri, ref in enumerate(base["references"]):
            if ref["expected"]:
                continue
            plain = []
            for ci, claim in enumerate(ref["claims"]):
                key = f"I{ri + 1}{ci + 1}"
                family = FAMILY[scenario][key]
                keep = KEEP.get((scenario, key), ())
                probe = told(rename(isolate(base, ri, ci, keep), f"P-{scenario}-{key}"), plural)
                add(probe, "probe", scenario, claim["requirement"], family,
                    note=f"keeps {', '.join(keep)} for meaning" if keep else "")
                if family == "F0":
                    plain.append(ci)
            if len(plain) > 1:
                packed = told(rename(keep_claims(base, ri, set(plain)), f"PP-{scenario}"), plural)
                add(packed, "packed plain", scenario, None, "F0",
                    note="plain decoys: " + ", ".join(ref["claims"][i]["requirement"] for i in plain))
        for sc, key, table, match, field, value, note in NEAREST:
            if sc != scenario:
                continue
            ri, ci = int(key[1]) - 1, int(key[2]) - 1
            variant = nearest_variant(base, ri, ci, table, match, field, value)
            probe = told(rename(isolate(variant, ri, ci), f"PB-{scenario}-{key}"), plural)
            add(probe, "probe", scenario, base["references"][ri]["claims"][ci]["requirement"], "F7", note)
    for scenario in SET_VALUED:
        tests.append({"case_id": scenario, "domain": {"B": "box", "C": "calendar", "L": "linear"}[scenario[0]],
                      "form": "target-present layer", "scenario": scenario, "fact": None, "family": None,
                      "note": "the pilot cover case as written; its B1 runs are reused"})
    for domain, ids in PANEL_EXISTING.items():
        for cid in ids:
            tests.append({"case_id": cid, "domain": domain, "form": "policy panel", "scenario": cid.split("-A")[0],
                          "fact": None, "family": None, "note": "pilot case, presupposing wording"})
    cal05 = rename(isolate(C.cal_05(), 0, 3), "CAL-05-I14")  # P2 for Calendar: one plain decoy (location)
    add(cal05, "policy panel", "CAL-05", None, None, "one plain decoy, presupposing wording")
    for domain, (builder, new_id, changes) in TWINS.items():
        twin = twin_case(builder, new_id, changes)
        add(twin, "policy panel", twin["variant_of"], None, None, "two records fully match a singular request")
    return tests, cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    tests, cases = build()
    outputs = {HERE / "cases_pilot" / c["domain"] / f"{c['case_id']}.json": json.dumps(c, indent=1, ensure_ascii=False) + "\n"
               for c in cases}
    outputs[HERE / "suite_pilot.json"] = json.dumps(tests, indent=1) + "\n"
    if args.check:
        stale = [str(p.relative_to(HERE)) for p, t in outputs.items() if not p.exists() or p.read_text() != t]
        if stale:
            raise SystemExit("Stale: " + ", ".join(stale))
        print("suite current")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    forms = {}
    for t in tests:
        forms[t["form"]] = forms.get(t["form"], 0) + 1
    families = {}
    for t in tests:
        if t["form"] == "probe":
            families[t["family"]] = families.get(t["family"], 0) + 1
    print(json.dumps({"tests": len(tests), "by_form": forms, "probe_families": dict(sorted(families.items())),
                      "new_case_files": len(cases)}))


if __name__ == "__main__":
    main()
