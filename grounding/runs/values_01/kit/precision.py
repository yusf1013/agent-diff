"""Precision of each check, from the hand-read labels (eval/labels.jsonl) against the final flag set. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.precision

A label counts for a check when the execution is still flagged by that check in the final outputs; labels on flags a
later cycle removed are listed apart. Intervals: Wilson 95%. Writes data/precision.json.
"""
from __future__ import annotations

import json
import math
from collections import defaultdict

from grounding.runs.values_01.kit.common import DATA, HERE, executions, read
from grounding.runs.values_01.kit.counts import OK, family

STRATUM_CHECK = {"V:priority": "V:priority", "V:run-date": "V:run-date", "V:colour": "V:colour",
                 "V:reaction": "V:reaction", "V:paraphrase": "V:paraphrase", "S:other fields": "S:other fields",
                 "S:other records": "S:other records", "S:other tables": "S:other tables",
                 "S:replica effect": "S:replica effect", "restore": "T:write not in the final state"}


def check_of(stratum: str) -> str:
    base = stratum.split(" (")[0]
    return STRATUM_CHECK.get(base, base)


def flagged(e, v, w, r) -> set[str]:
    out = set()
    for x in v.get("values", []):
        f = family(x["field"], e["scenario"])
        if x["verdict"] == "keywords present":
            out.add("V:paraphrase")
        elif x["verdict"] not in OK:
            out.add({"Linear priority": "V:priority", "run-date dependent date": "V:run-date",
                     "Calendar colour": "V:colour", "Slack reaction": "V:reaction"}.get(f, f"V:{f}"))
    for k, name in (("other_fields", "S:other fields"), ("other_records", "S:other records"),
                    ("other_tables", "S:other tables"), ("replica_effects", "S:replica effect")):
        if v.get(k):
            out.add(name)
    if v.get("no_net_change") or w.get("not_in_diff"):
        out.add("T:write not in the final state")
    out |= {f["check"] for f in r.get("flags", [])}
    return out


def wilson(k: int, n: int) -> list[float]:
    if not n:
        return [0.0, 1.0]
    z, p = 1.96, k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(max(0.0, c - h), 3), round(min(1.0, c + h), 3)]


def main():
    ex = {e["key"]: e for e in executions()}
    values, writes, reply = read("values"), read("writes"), read("reply")
    final = {k: flagged(e, values[k], writes[k], reply[k]) for k, e in ex.items()}
    pop = defaultdict(int)
    for fl in final.values():
        for c in fl:
            pop[c] += 1
    labels = [json.loads(line) for line in (HERE / "eval/labels.jsonl").read_text().splitlines() if line.strip()]
    per = defaultdict(dict)
    dropped = defaultdict(list)
    for lab in labels:
        s = lab["stratum"]
        if s == "recall":
            continue
        c = check_of(s)
        if c not in final[lab["key"]]:
            dropped[c].append({"key": lab["key"], "label": lab["label"], "stratum": s})
            continue
        # One label per execution and check: the in-draw label wins over one read outside the draw.
        prev = per[c].get(lab["key"])
        if prev is None or ("outside" in prev["stratum"] and "outside" not in s):
            per[c][lab["key"]] = {"label": lab["label"], "stratum": s}
    out = {}
    for c in sorted(set(pop) | set(per)):
        labs = list(per[c].values())
        true = sum(1 for x in labs if x["label"] in ("true",) or x["label"].startswith(("restored", "created",
                                                                                         "no-op", "probe")))
        false = sum(1 for x in labs if x["label"].startswith("false"))
        other = len(labs) - true - false
        out[c] = {"flagged": pop.get(c, 0), "read": len(labs), "true": true, "false": false, "other": other,
                  "precision": round(true / (true + false), 3) if true + false else None,
                  "wilson95": wilson(true, true + false),
                  "other_labels": sorted({x["label"] for x in labs} - {"true", "false"}),
                  "dropped_by_later_cycles": dropped.get(c, [])}
    recall = [lab for lab in labels if lab["stratum"] == "recall"]
    out["_recall_sample"] = {"read": len(recall), "clean": sum(1 for x in recall if x["label"] == "clean"),
                             "missed": [x for x in recall if x["label"] != "clean"]}
    (DATA / "precision.json").write_text(json.dumps(out, indent=1) + "\n")
    for c, d in out.items():
        if c.startswith("_"):
            print(c, {k: (v if not isinstance(v, list) else len(v)) for k, v in d.items()})
            continue
        print(f"{c:32} flagged {d['flagged']:4}  read {d['read']:3}  true {d['true']:3}  false {d['false']:2}  "
              f"other {d['other']}  precision {d['precision']}  {d['wilson95']}  {d['other_labels']}  "
              f"dropped {len(d['dropped_by_later_cycles'])}")


if __name__ == "__main__":
    main()
