"""Roadmap 6b's suite: the accepted scenarios of the generation runs (runs/gen_*) with opaque ids and test-side clocks, built as
openclaw_eval_01/opaque_suite.py built 6a's (the discussion after 6a, 2026-09-28). No model or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.completion_01.suite

For each accepted scenario (skipped: those runs/gen_01 did not accept, and those the known-defects list leaves out):
1. **The recorded suite:** the frozen derivation (`derive.suite_with_dropped`) of the accepted case must equal the
   suite the orchestrator wrote (runs/gen_01/cases/), test by test.
2. **Opaque ids:** one mapping per scenario (`autogen_01/kit/opaque_ids.py`). The derivation from the obfuscated case
   must equal the obfuscated suite, test by test, with the same drops, and every test passes `opaque_ids.check`.
3. **The clock** (not Calendar's, whose tests run on June 17, 2018): the moment the accepted version was written
   (the scenario's last writer call in runs/gen_01/calls.jsonl), or, when its data has a later event, a day after
   that event. An event is a timestamp of something done: a field named created, updated, modified, completed,
   canceled, archived, resolved, trashed, deleted, edited, started or last seen (with `_at`, `At` or nothing), and a
   Slack message's timestamp. Plans are not events: due and target dates, a cycle's or project's start and end, an
   event's start and end, expiry times.

Writes suite/: cases/<domain>/, cases/suite.json (the index), ids/<scenario>.json (old id -> new id), check.json.
Any failure stops before anything is written.
"""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, opaque_ids
from grounding.runs.autogen_01.kit.derive import digest
from grounding.runs.openclaw_eval_01 import materialize, rulings

HERE = Path(__file__).resolve().parent
GENS = sorted((HERE / "runs").glob("gen_*"))
OUT = HERE / "suite"
EVENT = re.compile(r"^(created|updated|modified|completed|canceled|cancelled|archived|resolved|trashed|deleted|edited|"
                   r"started|last_?seen|content_created|content_modified)(_at|At)?$", re.I)


def parse_time(value) -> datetime | None:
    if not isinstance(value, str) or not re.match(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        t = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo else t.replace(tzinfo=timezone.utc)


def events(case: dict) -> list[datetime]:
    out = []
    for table, rows in case["seed"].items():
        for row in rows if isinstance(rows, list) else []:
            if not isinstance(row, dict):
                continue
            for k, v in row.items():
                t = parse_time(v) if EVENT.match(k) else None
                if t:
                    out.append(t)
            if case["domain"] == "slack" and table == "messages" and re.fullmatch(r"\d{9,10}\.\d+", str(row.get("message_id", ""))):
                out.append(datetime.fromtimestamp(float(row["message_id"]), timezone.utc))
    return out


def written_at(gen: Path) -> dict[str, datetime]:
    """scenario -> the time of its last writer call in one generation run."""
    out = {}
    for line in (gen / "calls.jsonl").read_text().splitlines():
        call = json.loads(line)
        if call.get("role") == "writer":
            t = datetime.fromisoformat(call["utc"])
            out[call["label"]] = max(out.get(call["label"], t), t)
    return out


def clock_for(case: dict, written: datetime) -> dict | None:
    if case["domain"] == "calendar":
        return None
    latest = max(events(case), default=None)
    if latest and latest > written:
        return {"now": (latest + timedelta(days=1)).isoformat().replace("+00:00", "Z"),
                "why": f"a day after the latest event in its data ({latest.isoformat()}), which is after it was written"}
    return {"now": written.isoformat().replace("+00:00", "Z"), "why": "the moment its accepted version was written"}


def main():
    check = {"scenarios": 0, "tests": 0, "dropped": [], "ids_replaced": 0, "clocks": {}, "skipped": {}, "failures": []}
    fail = check["failures"].append
    tests_out, index, mappings = [], [], {}
    for case_path in sorted(p for gen in GENS for p in gen.glob("*/case.json")):
        folder = case_path.parent
        GEN, written = folder.parent, written_at(folder.parent)
        outcome = json.loads((folder / "outcome.json").read_text())
        sid = outcome["scenario_id"]
        if outcome.get("status") != "accepted":
            check["skipped"][sid] = outcome.get("status")
            continue
        action = rulings.actions().get(sid, "keep")
        if action.startswith("leave out"):
            check["skipped"][sid] = f"known defect: {action}"
            continue
        case = json.loads(case_path.read_text())
        check["scenarios"] += 1
        kept, gone = derive.suite_with_dropped(case)
        recorded = {p.stem: p for p in (GEN / "cases" / case["domain"]).glob("*.json")
                    if p.stem == sid or re.sub(r"^(FP|P)-", "", p.stem).startswith(sid + "-")}
        for test, _ in kept:
            path = recorded.get(test["case_id"])
            if path is None or path.read_text() != materialize.text(test):
                fail(f"{test['case_id']}: differs from the recorded suite")
        mapping = opaque_ids.mapping_for(sid, [case] + [t for t, _ in kept])
        mappings[sid] = {"scenario": sid, "domain": case["domain"], "ids": mapping}
        check["ids_replaced"] += len(mapping)
        try:
            opaque_case = opaque_ids.obfuscate(case, sid, mapping)
        except ValueError as exc:
            fail(str(exc))
            continue
        kept_o, gone_o = derive.suite_with_dropped(opaque_case)
        derived = {t["case_id"]: t for t, _ in kept_o}
        if {t["case_id"] for t, _ in gone_o} != {t["case_id"] for t, _ in gone}:
            fail(f"{sid}: the obfuscated case drops different tests")
        check["dropped"] += [t["case_id"] for t, _ in gone]
        clock = clock_for(case, written[sid]) if sid in written else None
        if case["domain"] != "calendar" and clock is None:
            fail(f"{sid}: no writer call recorded for its clock")
        if clock:
            check["clocks"][sid] = clock
        for test, meta in kept:
            check["tests"] += 1
            opaque = opaque_ids.obfuscate(test, sid, mapping)
            problems = opaque_ids.check(test, opaque, mapping)
            if derived.get(test["case_id"]) != opaque:
                problems.append(f"derivation does not commute: {materialize.differences(opaque, derived.get(test['case_id'], {}))[:6]}")
            for p in problems:
                fail(f"{test['case_id']}: {p}")
            if clock:
                opaque = {**opaque, "clock": {"now": clock["now"]}}
                opaque["case_sha256"] = digest({k: v for k, v in opaque.items() if k != "case_sha256"})
            tests_out.append(opaque)
            index.append({"case_id": test["case_id"], "domain": case["domain"], **meta,
                          "source": f"completion_01/runs/{GEN.name}", "ran_on_qwen": False,
                          "case_sha256": opaque["case_sha256"]})
    print(json.dumps({k: v for k, v in check.items() if k not in ("failures", "clocks")}, indent=1))
    if check["failures"]:
        for f in check["failures"][:60]:
            print("FAIL", f)
        raise SystemExit(f"{len(check['failures'])} failures; nothing written")
    for sub in ("cases", "ids"):  # the units (policy_units.py) stay
        if (OUT / sub).exists():
            shutil.rmtree(OUT / sub)
    for t in tests_out:
        path = OUT / "cases" / t["domain"] / f"{t['case_id']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n")
    (OUT / "cases" / "suite.json").write_text(json.dumps(sorted(index, key=lambda m: m["case_id"]), indent=1) + "\n")
    for sid, m in mappings.items():
        path = OUT / "ids" / f"{sid}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(m, indent=1) + "\n")
    (OUT / "check.json").write_text(json.dumps(check, indent=1) + "\n")
    print(f"{len(tests_out)} tests from {check['scenarios']} scenarios -> {OUT.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
