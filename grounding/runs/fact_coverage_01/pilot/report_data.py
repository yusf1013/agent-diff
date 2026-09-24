"""Regenerate the numbers and evidence links used in ../report.md (no model or service calls).

    python3 -m grounding.runs.fact_coverage_01.pilot.report_data > /tmp/report_data.md

Reads results.json (from results.py, with manual_labels.json applied), the case files and attempt directories.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPORT_DIR = HERE.parent
rows = json.loads((HERE / "results.json").read_text())


def attempt_dir(run, cid):
    """Latest completed attempt for (run, case), relative to the report."""
    dirs = sorted((HERE / "runs" / run / cid).glob("attempt-*"))
    for d in reversed(dirs):
        if json.loads((d / "execution_summary.json").read_text()).get("status") == "completed":
            return d.relative_to(REPORT_DIR)
    return None


def condition(r):
    cid = r["case_id"]
    if cid.startswith("WRD-"):
        return "wording"
    if cid.startswith("CON-"):
        return "contrast-plain" if cid.endswith("-plain") else "contrast-alt"
    if cid.startswith("ALT-"):
        return "alt-sweep"
    if cid.endswith("-TOLD"):
        return "told-packed"
    if cid.endswith("-FAR"):
        return "far"
    if cid.endswith("-PLAIN"):
        return "presupposing-plain"
    if r.get("isolated"):
        return "presupposing-isolated"
    return "present" if r["design"] == "present" else "presupposing-packed"


PRESUPPOSING = {"presupposing-packed", "presupposing-isolated", "presupposing-plain", "far"}
SCENARIO = re.compile(r"(BOX|CAL|LIN)-\d+")


def scenario(r):
    """The cover or arrangement case that a variant was derived from."""
    case = json.loads((HERE / "cases" / r["domain"] / f"{r['case_id']}.json").read_text())
    return (SCENARIO.search(r["case_id"]) or SCENARIO.search(case.get("variant_of") or "")).group(0)


def distinct_bugs(done):
    """One bug per requirement whose near-miss was selected in a fact-sensitive form; failures on presupposed
    no-target requests are one policy bug (report section 7.8)."""
    trials = Counter(r["case_id"] for r in done)
    print("\n## Distinct cases and bugs\n")
    print(f"distinct cases {len(trials)} from {len({scenario(r) for r in done})} scenarios; "
          f"cases by number of trials {dict(sorted(Counter(trials.values()).items()))}")
    failing = [r for r in done if r["outcome"] in ("incorrect", "recovered")]
    sensitive = [r for r in failing if condition(r) not in PRESUPPOSING]
    by_fact = defaultdict(list)
    for r in sensitive:
        for fact in r["exposed"]:
            by_fact[fact].append(r)
    print(f"fact-sensitive failing episodes {len(sensitive)} in {len({r['case_id'] for r in sensitive})} cases; "
          f"distinct requirements {len(by_fact)}")
    for fact, rs in sorted(by_fact.items(), key=lambda item: -len(item[1])):
        paths = "; ".join(f"{attempt_dir(r['run'], r['case_id'])} ({r['outcome']})" for r in rs)
        print(f"- {fact} ({rs[0]['domain']}): {len(rs)} | {paths}")
    presupposing = [r for r in failing if condition(r) in PRESUPPOSING]
    touched = {fact for r in presupposing for fact in r["exposed"]}
    print(f"presupposing failing episodes {len(presupposing)} (one policy bug); requirements touched {len(touched)}, "
          f"of which never failed when fact-sensitive {len(touched - set(by_fact))}")


def main():
    done = [r for r in rows if r.get("status") == "completed" and r["reference"].endswith(".r1")]
    print("## Episodes\n")
    print(f"scored (run, case) episodes: {len({(r['run'], r['case_id']) for r in done})}")
    table = defaultdict(lambda: defaultdict(Counter))
    for r in done:
        o = r["outcome"]
        k = "acted" if o == "incorrect" else "ok" if o in ("correct", "correct_absent", "recovered") else "other"
        table[condition(r)][r["domain"]][k] += 1
    print("\n## Outcomes by condition and domain (acted on a wrong record / acted+ok; other = unclear, "
          "not established, incomplete, invalid)\n")
    for cond, doms in table.items():
        tot = sum((d for d in doms.values()), Counter())
        cells = "; ".join(f"{dom} {v['acted']}/{v['acted'] + v['ok']} (+{v['other']})" for dom, v in sorted(doms.items()))
        print(f"- {cond}: total {tot['acted']}/{tot['acted'] + tot['ok']} (+{tot['other']} other) | {cells}")
    distinct_bugs(done)
    print("\n## Evidence links (latest completed attempt)\n")
    for r in sorted(done, key=lambda x: (condition(x), x["case_id"], x["run"])):
        path = attempt_dir(r["run"], r["case_id"])
        final = (r.get("final") or "").replace("\n", " ")[:160]
        print(f"- {condition(r)} | {r['case_id']} | {r['run']} | {r['outcome']} | {r['exposed']} | {path} | {final}")


if __name__ == "__main__":
    main()
