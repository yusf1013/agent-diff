"""Build attribution_01's development set: every hand-labelled trial, its owner (plan.md), and the judges' verdicts.

    python grounding/runs/attribution_01/build_devset.py

Owners are assigned by rule from the label's outcome, and by keywords in the label's note for `artifact` and
`not_established`; a note that says only "As t1" takes that trial's owner. OVERRIDES (below) record the assignments
made by reading notes the rules get wrong or cannot place, each with its reason. `also` names a second component the
note blames; `doubtful` marks an owner that a reasonable reader could assign differently (plan.md: scores are
reported with and without them). Each row also carries the known defect of its test, if any (roadmap_01's
known_defects.json, matched by test or by scenario). Writes devset.json. No model calls.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
A2 = RUNS / "autogen_02"
LABEL_FILES = sorted((A2 / "eval/labels_phase1").glob("*.json")) + \
              sorted(p for p in (A2 / "eval/labels_phase3").glob("*.json") if p.name != "attempts.json") + \
              sorted((A2 / "eval/labels_phase4").glob("*.json")) + [RUNS / "fact_coverage_02/manual_labels.json"]
JUDGES = {  # judge -> verdict folders; an earlier folder wins a key (the labelled attempt's verdicts come first)
    "v2": ["autogen_02/runs/judge2_phase3_attempt01", "autogen_02/runs/judge2_phase1", "autogen_02/runs/judge2_phase3",
           "autogen_02/runs/judge2_panel", "autogen_02/runs/judge2_phase4_policy", "autogen_02/runs/phase4/judged"],
    "v1_muse": ["autogen_02/runs/muse_judge_dev", "autogen_02/runs/judge1_phase1"],
    "v1_sonnet": ["autogen_01/runs/judge_dev_02", "autogen_01/runs/judge_test_01"],  # Claude Code Sonnet agents
}
AGENT = {"incorrect", "presented", "false_absence", "incomplete"}
NONE = {"correct", "correct_absent"}
RULES = [  # (owner, pattern over the lower-cased note), first match wins
    ("test-wording", r"^(defective|invalid) test"),
    ("test-construction", r"seed artifact|scenario artifact|non-uuid|invalid_name|reaction list rejects|trap|witness"),
    ("mock", r"replica artifact|replica ignores|ignores (the|that|box's|slack's)|ignored filter|filter.{0,40}ignor"
             r"|cannot return null|nested connection|projects query"),
    ("test-wording", r"defective test|invalid test|contestable|reasonabl|can .{0,20}mean|two readings|attach"),
    ("harness", r"timeout|timed out|turn limit|infrastructure|sandbox|container exited|rate limit"),
]
OLD_CLOCK = "the 480 s budget then counted the time spent waiting for Purdue (roadmap_01 clock_smoke: 65% of wall time)"
# Assignments made by reading the note (plan.md: before any scoring). Key pattern -> owner, also, doubtful, reason.
OVERRIDES = {
    r"/AT-AP-SLK-05-I13-I14$": ("agent", [], False, "the PI's ruling: the acting bot counts as a member"),
    r"/[HP]-BOX-31-I11$": ("test-wording", ["mock"], False, "the note: 'the ambiguous wording, not a missing target, "
                           "drives it'; the replica's ignored comment search is the second reason"),
    r"method_new/t\d/(P-)?SLK-21": ("test-construction", ["mock"], False, "the scenario asked for a reaction the "
                                    "replica rejects; Slack itself accepts :white_check_mark:"),
    r"solve_absence_look1/t3/AT-AP2-CAL-02-I11$": ("harness", ["agent", "test-construction"], True,
        "timed out while guessing calendar ids; " + OLD_CLOCK + "; the near miss is not on the actor's calendar "
        "list (known defect of U-AP2-CAL-02)"),
    r"solve_absence_look1/t1/AT-AP2-SLK-03-I15$": ("harness", ["agent"], True,
        "timed out after 28 read-only steps of repeated searches; " + OLD_CLOCK),
    r"method_pilot/t2/P-LIN-09-I13$": ("agent", ["harness"], True, "the 40-turn limit is the agent's own budget "
                                       "(turns exclude waiting); it ran out without an answer or a write"),
    r"b1/t2/LIN-02-TOLD$": ("agent", [], False, "stopped after one schema error, claiming an authentication error"),
    # Reason corrected 2026-09-27 22:59 (plan.md amendments): the solver's prompt lists 19 Linear operations and
    # omits documents and projects; the owner stays as committed, and the trials are in contested.json.
    r"(FP-LIN-22-I12-I13-I14|P-LIN-07-I12)$": ("agent", [], False, "claimed Linear has no documents; the replica "
        "serves the documents query, and the solver's prompt lists 19 operations without documents or projects"),
    r"/U-G4-CAL-06-Calendar_data_owner$": ("agent", ["test-construction"], True, "moved one of four matches "
        "without asking; the scenario's seed gives every event a Los Angeles zone (known defect), which may bear on "
        "which calendars it took to be on New York time"),
}
# Test-level flaws, judged on the test and not on any outcome (the PI's rule). From the known defects' advice for new
# agents; the labels' test-wording and test-construction owners add the tests they name.
FLAWED_ADVICE = ("leave out", "fix the seed")
NOT_FLAWED = {"G4-BOX-05": "the PI's ruling: natural ambiguity, a valid test",
              "G4-LIN-02": "valid when it ran (before 2026-09-30); it depends on the run date only afterwards"}
KNOWN = json.loads((RUNS / "roadmap_01/known_defects.json").read_text())
DEFECTS = {e["id"]: e for part in ("curated", "from_the_witness_check") for e in KNOWN[part]}
FORM = re.compile(r"^(?:(?:AT|FP|P|U|H)-)?")


def scenario_of(test: str) -> str:
    """AT-AP2-CAL-02-I11 -> AP2-CAL-02; U-G4-CAL-06-Calendar_data_owner -> G4-CAL-06; SLK-21-A-I14 -> SLK-21."""
    m = re.match(r"((?:[A-Z]+\d?-)?[A-Z]{3}-\d+)", FORM.sub("", test))
    return m.group(1) if m else test


def defect_of(test: str) -> dict | None:
    e = DEFECTS.get(test) or DEFECTS.get(scenario_of(test))
    return {"id": e["id"], "kind": e["kind"], "for_new_agents": e["for_new_agents"]} if e else None


def labels():
    for f in LABEL_FILES:
        d = json.loads(f.read_text())
        for key, v in d.items():
            if key.startswith("_") or not isinstance(v, dict) or "outcome" not in v:
                continue
            yield f.relative_to(RUNS).as_posix(), key, v


def verdicts():
    out = {}
    for judge, folders in JUDGES.items():
        for folder in folders:
            for p in sorted((RUNS / folder).rglob("verdict.json")):
                v = json.loads(p.read_text())
                out.setdefault(judge, {}).setdefault(v["key"], {"outcome": v.get("outcome"),
                                                                "exposed": v.get("exposed", []),
                                                                "note": (v.get("note") or "")[:400],
                                                                "artifact_reason": v.get("artifact_reason") or "",
                                                                "folder": folder})
    return out


def owner_of(key: str, v: dict) -> dict:
    for pattern, (owner, also, doubtful, why) in OVERRIDES.items():
        if re.search(pattern, key):
            return {"owner": owner, "also": also, "doubtful": doubtful, "owner_basis": "override: " + why}
    o = v["outcome"]
    if o in AGENT:
        return {"owner": "agent", "also": [], "doubtful": False, "owner_basis": "rule: outcome " + o}
    if o in NONE:
        return {"owner": "none", "also": [], "doubtful": False, "owner_basis": "rule: outcome " + o}
    note = (v.get("note") or "").lower()
    m = re.match(r"as (t\d)\b", note)
    if m:
        return {"inherit": re.sub(r"/t\d/", f"/{m.group(1)}/", key)}
    for owner, pattern in RULES:
        if re.search(pattern, note):
            return {"owner": owner, "also": [], "doubtful": False,
                    "owner_basis": f"rule: {o} note matches /{pattern.split('|')[0]}.../"}
    return {"owner": "unassigned", "also": [], "doubtful": False, "owner_basis": f"no rule for outcome {o}"}


def main():
    vs = verdicts()
    rows = []
    for source, key, v in labels():
        test = key.split("/")[-1]
        row = {"key": key, "label_file": source, "outcome": v["outcome"], "exposed": v.get("exposed", []),
               "note": (v.get("note") or "")[:500], **owner_of(key, v), "test": test, "scenario": scenario_of(test),
               "test_defect": defect_of(test),
               "study": "fact_coverage_02" if "fact_coverage_02" in source else "autogen_02"}
        for judge, byk in vs.items():
            if key in byk:
                row["judge_" + judge] = byk[key]
        rows.append(row)
    by_key = {r["key"]: r for r in rows}
    for r in rows:
        if "inherit" in r:
            src = by_key[r.pop("inherit")]
            r.update(owner=src["owner"], also=src["also"], doubtful=src["doubtful"],
                     owner_basis=f"as {src['key'].split('/')[1]}: " + src["owner_basis"])
    flawed_by_label = {r["test"] for r in rows if r["owner"] in ("test-wording", "test-construction")}
    for r in rows:
        d = r["test_defect"]
        if d and d["id"] in NOT_FLAWED:
            r["test_flaw"], r["test_flaw_basis"] = None, NOT_FLAWED[d["id"]]
        elif d and d["for_new_agents"].startswith(FLAWED_ADVICE):
            r["test_flaw"], r["test_flaw_basis"] = "flawed", f"known defect {d['id']}: {d['kind']}"
        elif d and d["for_new_agents"].startswith("read before"):
            r["test_flaw"], r["test_flaw_basis"] = "doubt", f"known defect {d['id']}: {d['kind']}"
        elif r["test"] in flawed_by_label:
            r["test_flaw"], r["test_flaw_basis"] = "flawed", "a label of this test blames the test"
        else:
            r["test_flaw"], r["test_flaw_basis"] = None, ""
    (HERE / "devset.json").write_text(json.dumps({"_about": "attribution_01 development set (plan.md); built by "
                                                           "build_devset.py", "rows": rows}, indent=1) + "\n")
    print(len(rows), "labelled trials;", Counter(r["owner"] for r in rows))
    print("distinct tests per owner:", {o: len({r["test"] for r in rows if r["owner"] == o})
                                        for o in Counter(r["owner"] for r in rows)})
    print("doubtful:", [r["key"] for r in rows if r["doubtful"]])
    print("flawed tests:", sorted({(r["test"], r["test_flaw"]) for r in rows if r["test_flaw"]}))
    print("with a judge v2 verdict:", sum("judge_v2" in r for r in rows), "| v1 on Muse:",
          sum("judge_v1_muse" in r for r in rows), "| v1 on Sonnet:", sum("judge_v1_sonnet" in r for r in rows))
    for owner in ("test-wording", "test-construction", "mock", "harness", "unassigned"):
        rs = [r for r in rows if r["owner"] == owner]
        print(f"\n== {owner}: {len(rs)}")
        for r in rs:
            print(f"  [{r['outcome']}] {r['key']}: {r['note'][:160]}")


if __name__ == "__main__":
    main()
