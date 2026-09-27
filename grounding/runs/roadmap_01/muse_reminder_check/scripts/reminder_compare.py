"""The Muse reminder check: for batch 1's 30 blind-labelled trials, the verdicts with the reminder on (runs/phase4/judged)
and off (roadmap_01/muse_reminder_check/judged): outcome and exposed facts per trial; and calls, tokens, cost and time
from both runs' call logs (the earlier run's rows matched by label). Writes comparison_with_reminders_on.json."""
import json
from pathlib import Path

W = Path("/home/yusf/PyProj/agent-diff/.claude/worktrees/autogen-02/grounding/runs")
ON = W / "autogen_02/runs/phase4/judged"
OFF = W / "roadmap_01/muse_reminder_check/judged"
trials = json.loads((W / "roadmap_01/muse_reminder_check/trials.json").read_text())


def verdict(root: Path, t: dict):
    d = root / t["run"] / t["trial"] / t["case_id"]
    res = sorted(d.glob("*judge.result.json"))
    if not res:
        return None
    so = json.loads(res[-1].read_text()).get("structured_output") or {}
    return {"outcome": so.get("outcome"), "facts": sorted(so.get("exposed") or []),
            "acted_on": sorted(str(x) for x in so.get("acted_on") or []), "mechanism": so.get("mechanism")}


rows, same_outcome, same_facts = [], 0, 0
for t in trials:
    key = f"{t['run']}/{t['trial']}/{t['case_id']}"
    a, b = verdict(ON, t), verdict(OFF, t)
    so = a and b and a["outcome"] == b["outcome"]
    sf = a and b and a["facts"] == b["facts"]
    same_outcome += bool(so)
    same_facts += bool(sf)
    rows.append({"trial": key, "reminders_on": a, "reminders_off": b, "same_outcome": bool(so), "same_facts": bool(sf),
                 "same_acted_on": bool(a and b and a["acted_on"] == b["acted_on"]),
                 "same_mechanism": bool(a and b and a["mechanism"] == b["mechanism"])})


def calls(path: Path, labels: set):
    out = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    return [r for r in out if r.get("label") in labels and not r.get("failed")]


labels = {f"{t['run']}/{t['trial']}/{t['case_id']}" for t in trials}
on_rows, off_rows = calls(ON / "calls.jsonl", labels), calls(OFF / "calls.jsonl", labels)
if not on_rows:  # label format may differ: fall back to case ids
    ids = {t["case_id"] for t in trials}
    on_rows = [r for r in calls(ON / "calls.jsonl", set()) if False]
    allon = [json.loads(line) for line in (ON / "calls.jsonl").read_text().splitlines() if line.strip()]
    print("label examples in the earlier log:", [r.get("label") for r in allon[:3]])


def stats(rs):
    if not rs:
        return {}
    secs = sorted(r["seconds"] for r in rs)
    return {"calls": len(rs), "input_tokens": sum(r["input_tokens"] + r.get("cache_read_input_tokens", 0) for r in rs),
            "cached": sum(r.get("cache_read_input_tokens", 0) for r in rs),
            "output_tokens": sum(r["output_tokens"] for r in rs),
            "list_usd": round(sum(r.get("cost_usd_list_price", 0) for r in rs), 3),
            "billed_usd": round(sum(r.get("cost_usd_billed", 0) for r in rs), 4),
            "median_seconds": secs[len(secs) // 2]}


summary = {"trials": len(trials), "same_outcome": same_outcome, "same_exposed_facts": same_facts,
           "with_exposed_facts": sum(1 for r in rows if r["reminders_on"] and r["reminders_on"]["facts"]),
           "same_acted_on": sum(r["same_acted_on"] for r in rows),
           "same_mechanism": sum(r["same_mechanism"] for r in rows),
           "reminders_on": stats(on_rows), "reminders_off": stats(off_rows),
           "different": [r for r in rows if not (r["same_outcome"] and r["same_facts"])]}
(OFF / "comparison_with_reminders_on.json").write_text(json.dumps({**summary, "per_trial": rows}, indent=1))
print(json.dumps({k: v for k, v in summary.items() if k != "different"}, indent=1))
for r in summary["different"]:
    print("DIFFERENT:", r["trial"], r["reminders_on"], "->", r["reminders_off"])
