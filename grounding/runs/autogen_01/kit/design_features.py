"""Design features of every single-decoy probe, hand-built and generated, next to Qwen's outcomes.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.design_features

Probes:
- hand-built: fact_coverage_02's pilot-fact probes (method_pilot) and new-fact probes (method_new and its reruns),
  with the manual labels; the new-fact probes also ran again in autogen_01's same-day control;
- generated: autogen_01's Arm R, Arm P and v2 probes, with my adjudication applied. Decoys I judged contestable or
  invalid, and invalid tests, are left out.

Features come from each probe's own case.json (the request, the seed after the target is removed, the reference query
and the decoy's claim). Nothing here reads a trajectory. Writes eval/design_features.json and prints summaries.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from grounding.runs.autogen_01.kit.judge import COLLAPSE
from grounding.runs.fact_coverage_02.followups import _conditions
from grounding.runs.fact_coverage_02.tables import load as fc2_load

STUDY = Path(__file__).resolve().parents[1]
RUNS = STUDY / "runs"
FC2_RUNS = STUDY.parent / "fact_coverage_02" / "runs"
OUT = STUDY / "eval" / "design_features.json"
SUFFIX = re.compile(r"\s*If there (isn't one|aren't any), just tell me\.\s*$")
NAME_FIELDS = {"name", "title", "summary", "subject", "channel_name", "identifier", "key", "login", "email", "username",
               "display_name", "real_name", "displayName", "summaryOverride", "summary_override"}
HINTS = re.compile(r"\b(directly|not counting|itself|its own|actual|excluding|top-level|rather than|not the)\b", re.I)


def last_case(run_dir: Path, trial: str, case_id: str):
    attempts = sorted((run_dir / trial / case_id).glob("attempt-*"))
    return json.loads((attempts[-1] / "case.json").read_text()) if attempts else None


def nodes(query, path=()):
    """Every node of a reference query with its path of edge keys from the root."""
    yield path, query
    for e in query.get("edges", []):
        yield from nodes(e["node"], path + (e.get("key"),))


def tested(query, claim):
    """The filters (with their node path and table) and edges that carry the claim's fact."""
    fact = claim["requirement"]
    target = (claim.get("mutation") or {}).get("target")
    found = []
    for path, node in nodes(query):
        for f in node.get("filters", []):
            if f.get("fact") == fact or (target and f.get("key") == target):
                found.append(("filter", path, node["table"], f))
        for e in node.get("edges", []):
            if e.get("fact") == fact or (target and e.get("key") == target):
                found.append(("edge", path, node["table"], e))
    return found


def lure(seed, table, field, value):
    """Where the requested string value appears in the probe's seed (the target is already removed)."""
    if not isinstance(value, str) or len(value.strip()) < 3:
        return "not a text value"
    v = value.strip().lower()
    same, name, other = False, False, False
    for t, rows in seed.items():
        if not isinstance(rows, list):
            continue
        for row in rows:
            if not isinstance(row, dict):
                continue
            for k, x in row.items():
                if isinstance(x, str) and v in x.lower():
                    if t == table and k == field:
                        same = True
                    elif k in NAME_FIELDS:
                        name = True
                    else:
                        other = True
    if same:
        return "contains the value in the tested field"
    if name:
        return "the value in a name field"
    if other:
        return "the value only in another field"
    return "the value nowhere"


def features(case, claim):
    prompt = SUFFIX.sub("", case["prompt"])
    query = case["references"][0]["query"]
    seed = case["seed"]
    hits = tested(query, claim)
    root_filters = query.get("filters", [])
    tested_keys = {h[3].get("key") for h in hits}
    root_named = any(f.get("field") in NAME_FIELDS and f.get("key") not in tested_keys for f in root_filters)
    tested_on_root = any(h[1] == () and h[0] == "filter" for h in hits)
    lures = sorted({lure(seed, h[2], h[3].get("field"), h[3].get("value")) for h in hits if h[0] == "filter"})
    witness_table = query["table"]
    return {
        "chars": len(prompt), "conditions": _conditions(query), "root_filters": len(root_filters),
        "root_named_other": root_named, "tested_on_root": tested_on_root,
        "lure": lures[0] if len(lures) == 1 else ("; ".join(lures) if lures else "a relation or structure"),
        "hint_words": sorted({m.lower() for m in HINTS.findall(prompt)}),
        "rows_in_root_table": len(seed.get(witness_table, []) or []),
        "prompt": prompt,
    }


def handbuilt():
    out = []
    control = json.loads((RUNS / "solve_control.score.json").read_text())
    today = {t["case_id"]: t for t in control["tests"]}
    for runs, origin in ((["method_pilot"], "hand-built, pilot facts"),
                         (["method_new", "method_new_lin25", "method_new_slk21"], "hand-built, new facts")):
        for t in fc2_load(runs):
            if t.get("form") != "probe":
                continue
            trials = dict(t["trials"])
            first = next(iter(sorted(trials)))
            case = last_case(FC2_RUNS / t["run"], first, t["case_id"])
            if not case:
                continue
            claim = case["references"][0]["claims"][0]
            contestable = any(x.get("contestable") for x in trials.values())
            row = {"origin": origin, "case_id": t["case_id"], "scenario": t.get("scenario"), "fact": t.get("fact"),
                   "family": t.get("family") or claim.get("family"), "failures_3": t["failures"],
                   "established_3": t["established"], "contestable": contestable, **features(case, claim)}
            c = today.get(t["case_id"])
            if c:
                outs = [COLLAPSE.get(r["outcome"]) for r in c["trials"].values()]
                row["failures_today"] = sum(o == "fail" for o in outs)
                row["established_today"] = sum(o in ("fail", "pass") for o in outs)
            out.append(row)
    return out


def generated():
    review = json.loads((STUDY / "eval" / "judge_review.json").read_text())
    validity = json.loads((STUDY / "eval" / "validity.json").read_text())
    bad = {(sid, w) for sid, v in validity.items() if not sid.startswith("_")
           for w, d in v["decoys"].items() if d.split(":")[0].split(";")[0].strip() in ("contestable", "invalid")}
    invalid_tests = {c for sid, v in validity.items() if not sid.startswith("_") for c in v.get("invalid_tests", [])}
    out = []
    for run, origin in (("solve_arm_r", "generated, Arm R"), ("solve_arm_p", "generated, Arm P"),
                        ("solve_arm_p_v2", "generated, v2")):
        score = json.loads((RUNS / f"{run}.score.json").read_text())
        for t in score["tests"]:
            if t.get("form") != "probe" or t["case_id"] in invalid_tests:
                continue
            case = last_case(RUNS / run, "t1", t["case_id"])
            if not case:
                continue
            claim = case["references"][0]["claims"][0]
            if (t.get("scenario"), str(claim["witness"])) in bad:
                continue
            fails = est = 0
            for trial, r in t["trials"].items():
                rv = review.get(f"{run}/{trial}/{t['case_id']}", {})
                outcome = rv.get("outcome", r["outcome"]) if rv.get("review") == "override" else r["outcome"]
                c = COLLAPSE.get(outcome)
                fails += c == "fail"
                est += c in ("fail", "pass")
            out.append({"origin": origin, "case_id": t["case_id"], "scenario": t.get("scenario"), "fact": t.get("fact"),
                        "family": t.get("family"), "failures_3": fails, "established_3": est, "contestable": False,
                        **features(case, claim)})
    return out


def summarize(rows, key, label):
    print(f"\n### Exposure by {label}\n")
    print("| Group | " + " | ".join(ORIGINS) + " |")
    print("|---|" + "---|" * len(ORIGINS))
    groups = defaultdict(lambda: defaultdict(list))
    for r in rows:
        groups[key(r)][r["origin"]].append(r)
    for g in sorted(groups, key=str):
        cells = []
        for o in ORIGINS:
            rs = groups[g][o]
            if not rs:
                cells.append("–")
                continue
            exposed = sum(r["failures_3"] > 0 for r in rs)
            rate = sum(r["failures_3"] for r in rs) / max(1, sum(r["established_3"] for r in rs))
            cells.append(f"{exposed}/{len(rs)} (rate {rate:.2f})")
        print(f"| {g} | " + " | ".join(cells) + " |")


ORIGINS = ["hand-built, pilot facts", "hand-built, new facts", "generated, Arm R", "generated, Arm P", "generated, v2"]


def main():
    rows = [r for r in handbuilt() + generated() if not r["contestable"]]
    OUT.write_text(json.dumps(rows, indent=1) + "\n")
    print(f"{len(rows)} probes (contestable or invalid decoys left out); cells: probes exposing at 3 trials / probes"
          " (failure rate over established trials)")
    summarize(rows, lambda r: "all", "origin")
    summarize(rows, lambda r: r["lure"], "where the requested value sits in the probe's seed")
    summarize(rows, lambda r: r["family"], "family")
    summarize(rows, lambda r: ("1-2" if r["conditions"] <= 2 else "3-4" if r["conditions"] <= 4 else
                               "5-6" if r["conditions"] <= 6 else "7+"), "conditions in the request")
    summarize(rows, lambda r: "names the target by another name-like field" if r["root_named_other"] else "does not",
              "whether the request also names the target")
    summarize(rows, lambda r: "tested fact on the acted-on record" if r["tested_on_root"] else
              "tested fact on a related record", "where the tested fact sits")
    summarize(rows, lambda r: "hint words: " + ", ".join(r["hint_words"]) if r["hint_words"] else "no hint words",
              "hint words in the request")
    summarize(rows, lambda r: ("1-2" if r["rows_in_root_table"] <= 2 else "3-5" if r["rows_in_root_table"] <= 5 else
                               "6-10" if r["rows_in_root_table"] <= 10 else "11+"), "records in the acted-on table")


if __name__ == "__main__":
    main()
