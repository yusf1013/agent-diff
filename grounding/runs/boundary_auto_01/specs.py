"""Generate each boundary's oracle spec (F on R) from the writer's target, and check it against the hand-written specs.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_auto_01.specs

The spec kinds are boundary_02/oracle.py's: `field` (a record's column takes the value), `exists` (a row with these
values exists), `absent` (no such row) and `never` (a question: judged on the answer). Values compare in their stored
form, a date by its day. The check: every graded phase-1 trial of the element (cycles 2, 3, 5 and 6, void trials left
out) is judged again with the generated spec, and the verdict (pass or fail) is compared with the hand-written spec's.
Writes specs.json: per element the generated spec's description and its agreement.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.boundary_02 import oracle as O
from grounding.runs.several_match_auto_01 import seedkit

HERE = Path(__file__).resolve().parent
BD2 = HERE.parent / "boundary_02"


def pred_for(value):
    val = str(value).strip()

    def pred(v, r, s):
        if v is None:
            return val.lower() in ("", "none", "null")
        sv = str(v).strip()
        if sv.lower() == val.lower():
            return True
        if len(val) >= 10 and val[4] == "-" and val[7] == "-" and sv[:10] == val[:10]:  # a date, by its day
            return True
        if val.lower() in ("true", "false"):
            return (sv.lower() in ("true", "1")) == (val.lower() == "true")
        return False
    return pred


def spec_for(service, target):
    kind, table = target.get("kind"), target.get("table")
    if kind == "question":
        return O.never()
    if kind == "set_field":
        key_col = seedkit.pk(service, table)[0]
        return O.field(table, key_col, str(target["record_id"]), target["field"], pred_for(target["value"]))
    try:
        match = json.loads(target.get("match") or "{}")
    except ValueError:
        match = {}
    if not match:
        raise ValueError("no match given")
    return O.exists(table, **match) if kind == "add_row" else O.absent(table, **match)


def graded_trials():
    """(element, cycle, trial, hand-spec verdict) for every non-void graded trial of phases 1."""
    out = []
    for cyc_trial, v in json.loads((BD2 / "oracle-verdicts.json").read_text()).items():
        cyc, trial = cyc_trial.split("/", 1)
        if trial not in O.VOID.get(cyc, {}):
            out.append((trial.split("/")[1].removeprefix("BD2-"), cyc, trial, v["oracle"]))
    for cyc in ("c5", "c6"):
        for trial, v in json.loads((BD2 / f"oracle-{cyc}.json").read_text()).items():
            if not v["oracle"].startswith("void"):
                out.append((trial.split("/")[1].removeprefix("BD2-"), cyc, trial, v["oracle"]))
    return out


def main():
    space = {r["id"]: r for r in json.loads((BD2 / "space.json").read_text())}
    answers = json.loads((HERE / "writer.json").read_text())
    digests = {c: {d["trial"]: d for d in json.loads((BD2 / f"digest-{c}.json").read_text())}
               for c in ("c2", "c3", "c5", "c6")}
    out, agree, total = {}, 0, 0
    for eid, cyc, trial, hand in graded_trials():
        a = answers.get(eid)
        row = out.setdefault(eid, {"target": (a or {}).get("target"), "request": (a or {}).get("request"),
                                   "trials": 0, "agree": 0, "disagreements": []})
        if not a:
            row["error"] = "no writer answer"
            continue
        try:
            spec = spec_for(space[eid]["service"], a["target"])
        except Exception as exc:  # recorded: the target could not become a spec
            row["error"] = f"{type(exc).__name__}: {exc}"[:200]
            continue
        att = sorted((BD2 / "runs" / cyc / trial).glob("attempt-*"))[-1]
        v, _info = O.verdict(spec, att, digests[cyc][trial])
        same = v.startswith("pass") == hand.startswith("pass")
        row["trials"] += 1
        row["agree"] += same
        total += 1
        agree += same
        if not same:
            row["disagreements"].append({"trial": f"{cyc}/{trial}", "generated": v, "hand": hand})
    (HERE / "specs.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    errors = {e: r["error"] for e, r in out.items() if r.get("error")}
    print(f"trials judged again: {total}; the generated spec agrees with the hand spec in {agree}")
    print("elements with every trial in agreement:",
          sum(1 for r in out.values() if r["trials"] and r["agree"] == r["trials"]), "of", len(out))
    print("errors:", errors)
    for e, r in sorted(out.items()):
        if r["disagreements"]:
            print(f"  {e}: {r['agree']}/{r['trials']} target={json.dumps(r['target'])[:160]}")


if __name__ == "__main__":
    main()
