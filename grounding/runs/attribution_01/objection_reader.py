"""Source 4: a Muse reader that decides whether a failed trial's request supports the solver's reading (plan.md).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.attribution_01.objection_reader select
    AUTOGEN_BACKEND=muse python ... objection_reader run [--concurrency 4]
    python ... objection_reader score

It runs because sources 1-3 flag none of the development set's test-wording trials. The reader gets the judge's own
bundle for the trial (the request, the author's targets and decoys, the solver's steps and answer) and the
instruction in prompts/objection_reader.md, written once before any reading and not revised on the results.

Selected trials (by rule, before any reading):
- positives: every trial owned by `test-wording`;
- negatives: every agent-owned failure whose final answer states a reading or an objection (the regex MARK),
  plus the trials the PI ruled natural ambiguity (AT-AP-SLK-05-I13-I14).
A `test_wording` reading is the flag. Writes objection_reader/ (readings, calls.jsonl) and source4_objection.json.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROMPT = HERE / "prompts" / "objection_reader.md"
OUT = HERE / "objection_reader"
WORKSPACES = Path("/tmp/attribution-01/ws/objection")
MARK = re.compile(r"assum|interpret|typo|not exactly|however|one note|note:|although|didn.t match|doesn.t match|"
                  r"does not match|rather than|closest|likely|ambigu|unclear|I took|I treated|reading|"
                  r"two (events|files|channels|issues|calendars|messages)|several|multiple", re.I)
RULED = re.compile(r"/AT-AP-SLK-05-I13-I14$")
SCHEMA = {
    "type": "object",
    "properties": {
        "author_reading": {"type": "string"},
        "solver_reading": {"type": "string"},
        "solver_stated_it": {"type": "boolean"},
        "reading": {"type": "string", "enum": ["test_wording", "natural_ambiguity", "solver_error"]},
        "reason": {"type": "string"},
    },
    "required": ["author_reading", "solver_reading", "solver_stated_it", "reading", "reason"],
}


def final_answer(att: Path) -> str:
    traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
    return str(json.loads(traj.read_text()).get("final") or "")


def select() -> list[dict]:
    from grounding.runs.attribution_01 import scan_traces as st
    atts = st.attempts()
    rows = json.loads((HERE / "devset.json").read_text())["rows"]
    items = []
    for r in rows:
        att = atts[r["key"]]
        if r["owner"] == "test-wording":
            group = "positive"
        elif r["owner"] == "agent" and (RULED.search(r["key"]) or (
                r["outcome"] != "not_established" and MARK.search(final_answer(att)))):
            group = "negative"
        else:
            continue
        items.append({"key": r["key"], "group": group, "attempt": str(att)})
    return items


def read_one(item: dict, calls_log: Path) -> dict:
    from grounding.runs.autogen_01.kit import agent, bundle
    from grounding.runs.autogen_02.kit import judge2
    dest = OUT / item["key"]
    path = dest / "reading.json"
    if path.exists():
        return json.loads(path.read_text())
    att = Path(item["attempt"])
    run, trial = att.parent.parent.parent.name, att.parent.parent.name
    case, summary, tri = judge2.triage(run, trial, att)
    targets = len(case["references"][0]["expected"])
    form = judge2.form_of(case["case_id"]) or (
        "cover (target and all decoys)" if targets else "no-target test with all of the scenario's decoys")
    text = bundle.build(case, att, form, tri, summary)
    result = agent.run(agent.Call(
        role="reader", workspace=WORKSPACES / item["key"].replace("/", "-"), log_dir=dest, calls_log=calls_log,
        tools=[], schema=SCHEMA, system_append=PROMPT.read_text(), label=item["key"],
        prompt=text + "\n\nGive your reading of this trial against its request."))
    reading = agent.structured(result) or {}
    reading.update(key=item["key"], group=item["group"], attempt=item["attempt"],
                   backend=result.get("backend", "claude"))
    dest.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(reading, indent=1, ensure_ascii=False) + "\n")
    return reading


def run(concurrency: int):
    OUT.mkdir(parents=True, exist_ok=True)
    frozen = OUT / "reader_prompt.md"
    if frozen.exists() and frozen.read_text() != PROMPT.read_text():
        raise SystemExit("objection_reader/ was read with another prompt version; move it aside first")
    frozen.write_text(PROMPT.read_text())
    items = json.loads((OUT / "selected.json").read_text())
    calls_log = OUT / "calls.jsonl"
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(read_one, it, calls_log): it for it in items}
        for n, fut in enumerate(as_completed(futures), 1):
            it = futures[fut]
            try:
                r = fut.result()
                print(f"[{n}/{len(items)}] {it['group']:8} {it['key']}: {r.get('reading')}", flush=True)
            except Exception as exc:  # recorded; a rerun resumes
                print(f"[{n}/{len(items)}] {it['key']}: FAILED {type(exc).__name__}: {exc}", flush=True)


def score():
    readings = [json.loads(p.read_text()) for p in sorted(OUT.rglob("reading.json"))]
    rows = {r["key"]: r for r in json.loads((HERE / "devset.json").read_text())["rows"]}
    tab = Counter((r["group"], r.get("reading")) for r in readings)
    pos = [r for r in readings if r["group"] == "positive"]
    neg = [r for r in readings if r["group"] == "negative"]
    by_test = {}
    for r in pos:
        by_test.setdefault(rows[r["key"]]["test"], []).append(r.get("reading") == "test_wording")
    out = {"table": {f"{g}/{v}": n for (g, v), n in sorted(tab.items())},
           "recall_trials": [sum(r.get("reading") == "test_wording" for r in pos), len(pos)],
           "recall_tests_any_trial": [sum(any(v) for v in by_test.values()), len(by_test)],
           "false_alarms": [sum(r.get("reading") == "test_wording" for r in neg), len(neg)],
           "flags_on_negatives": [{"key": r["key"], "solver_reading": r.get("solver_reading"),
                                   "reason": r.get("reason")} for r in neg if r.get("reading") == "test_wording"],
           "missed_positives": [{"key": r["key"], "reading": r.get("reading"), "reason": r.get("reason")}
                                for r in pos if r.get("reading") != "test_wording"]}
    calls = [json.loads(l) for l in (OUT / "calls.jsonl").read_text().splitlines()] if (OUT / "calls.jsonl").exists() \
        else []
    out["usage"] = {"calls": len(calls), "list_usd": round(sum(c.get("cost_usd_list_price") or 0 for c in calls), 3),
                    "billed_usd": round(sum(c.get("cost_usd_billed") or 0 for c in calls), 4),
                    "input_tokens": sum(c.get("input_tokens") or 0 for c in calls),
                    "cache_read_input_tokens": sum(c.get("cache_read_input_tokens") or 0 for c in calls),
                    "output_tokens": sum(c.get("output_tokens") or 0 for c in calls)}
    (HERE / "source4_objection.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in ("flags_on_negatives", "missed_positives")}, indent=1))
    for f in out["flags_on_negatives"]:
        print("  FA", f["key"], "|", (f["solver_reading"] or "")[:160])
    for m in out["missed_positives"]:
        print("  MISS", m["key"], m["reading"], "|", (m["reason"] or "")[:160])


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("select")
    r = sub.add_parser("run")
    r.add_argument("--concurrency", type=int, default=4)
    sub.add_parser("score")
    a = p.parse_args()
    if a.cmd == "select":
        items = select()
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "selected.json").write_text(json.dumps(items, indent=1) + "\n")
        print(Counter(i["group"] for i in items))
    elif a.cmd == "run":
        run(a.concurrency)
    else:
        score()


if __name__ == "__main__":
    main()
