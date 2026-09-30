"""The two tables the report session lifts ("For the report" in the README): the funnel in report_01's Table 5 form
with the regenerated half beside the Sonnet and Muse columns, and the two halves compared. No model calls.

    python3 grounding/runs/regen_01/for_report.py

The regenerated column comes only from this study's files: eval/funnel.json, eval/review.json, eval/coverage.json,
eval/compare_regular.json, runs/gen_*/*/outcome.json, runs/full_01.adjudicated_quiet_host.json and
inputs/briefs_regen.json (the Sonnet briefs' 34 distinct fact sets). The Sonnet and Muse columns are
report_01's: the rows from scenarios on are summed from report_01/numbers/generator.json (as report_01's concise
Table 5 sums its arms) and checked against its published values; the brief-level rows (runs, acceptance, review) and
the policy units are report_01's published Table 5 and Table 6 values, which no numbers file holds; the writers'
coverage and exposure are report_01/numbers/concise.json's. Writes eval/for_report.json and prints the tables.
"""
from __future__ import annotations

import json
import statistics
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVAL = HERE / "eval"
REPORT = HERE.parent / "report_01" / "numbers"
ARMS = {"Sonnet": ("Sonnet R", "Sonnet P", "Sonnet P v2"), "Muse": ("Muse Phase 4", "Muse 6b")}
# report_01's published Table 5 (report.md, per arm, summed by writer as report_concise.md shows) and Table 6
# ("Sonnet parent", "Muse parent"): not in any numbers file.
PUBLISHED = {
    "Sonnet": {"briefs_run": 50, "accepted": 49, "rejected": 1, "failed": 0, "versions": "1 (5), 2 (5), 2 (6) by arm",
               "review": (42, 6, 1), "usable": 48, "absence_units": 116, "underspecified_units": 98},
    "Muse": {"briefs_run": 58, "accepted": 52, "rejected": 5, "failed": 1, "versions": "2 (7), – by arm",
             "review": (45, 7, 0), "usable": 52, "absence_units": 126, "underspecified_units": 95},
}
CONCISE_TABLE5 = {"Sonnet": {"near_misses": 185, "flawed": 7, "derived": 285, "dropped": 5, "left_out": 9, "valid": 271},
                  "Muse": {"near_misses": 192, "flawed": 3, "derived": 297, "dropped": 2, "left_out": 3, "valid": 292}}


def earlier(writer: str) -> dict:
    gen = json.loads((REPORT / "generator.json").read_text())
    rows = [gen[a] for a in ARMS[writer]]
    out = {"scenarios": sum(r["scenarios"] for r in rows), "near_misses": sum(r["near_misses"] for r in rows),
           "flawed": sum(r["flawed_near_misses"] for r in rows), "derived": sum(r["derived_total"] for r in rows),
           "dropped": sum(r["dropped_by_witness_check"] for r in rows),
           "left_out": sum(r["left_out_by_rulings"] for r in rows), "valid": sum(r["valid_total"] for r in rows)}
    for k, v in CONCISE_TABLE5[writer].items():
        assert out[k] == v, (writer, k, out[k], v)
    concise = json.loads((REPORT / "concise.json").read_text())["writers"][writer]
    out["facts_covered"] = sum(len(v) for v in concise["coverage"].values())
    out["exposure"] = concise["exposure"]
    return {**PUBLISHED[writer], **out}


def regenerated() -> dict:
    funnel = json.loads((EVAL / "funnel.json").read_text())
    review = {k: v for k, v in json.loads((EVAL / "review.json").read_text()).items() if not k.startswith("_")}
    coverage = json.loads((EVAL / "coverage.json").read_text())
    outcomes = [json.loads(p.read_text()) for p in sorted((HERE / "runs").glob("gen_*/G4-*/outcome.json"))]
    status = Counter(o["status"] for o in outcomes)
    versions = [o["versions"] for o in outcomes if o["status"] == "accepted"]
    heads = Counter(r["verdict"].split(":")[0] for r in review.values())
    # report_01's review categories: "flawed but usable" is a contestable near miss or contrived wording, so my
    # "weak but valid" (contrived; impossible times) falls there.
    valid, usable_flawed = heads["valid"], heads["weak but valid"] + heads["flawed but usable"]
    invalid = sum(v for k, v in heads.items() if k.startswith("invalid"))
    reg = funnel["regular"]
    return {"briefs": funnel["briefs"], "briefs_run": funnel["brief_attempts"], "accepted": status["accepted"],
            "rejected": status["rejected"], "failed": sum(v for k, v in status.items() if k not in ("accepted", "rejected")),
            "versions": f"{statistics.median(versions):g} ({max(versions)})", "review": (valid, usable_flawed, invalid),
            "review_mine": dict(heads), "usable": funnel["usable_scenarios"], "scenarios": status["accepted"],
            "near_misses": funnel["near_misses_declared"], "flawed": funnel["near_misses_flawed"],
            "derived": reg["derived_candidates"], "dropped": reg["dropped_by_witness_check"],
            "left_out": reg["left_out_by_rulings"], "valid": reg["valid"],
            "absence_units": funnel["absence"]["valid"], "underspecified_units": funnel["underspecified"]["valid"],
            "facts_covered": coverage["brief_facts_credited"], "brief_facts": coverage["brief_facts"],
            "of_sonnet_81": coverage["sonnet_credited_covered"],
            "cost": {k: funnel["cost"][k]["list_usd"] for k in ("generation", "drop_f", "judge", "all")}}


def main():
    s, m, r = earlier("Sonnet"), earlier("Muse"), regenerated()
    briefs = json.loads((HERE / "inputs" / "briefs_regen.json").read_text())
    s["fact_sets"] = sum(1 for b in briefs if b.get("sonnet"))  # the Sonnet briefs' distinct fact sets, one brief each
    cmp = json.loads((EVAL / "compare_regular.json").read_text())
    halves, the81 = cmp["halves"], cmp["the_81"]
    quiet = json.loads((HERE / "runs" / "full_01.adjudicated_quiet_host.json").read_text())["adjudicated"]
    pct = lambda a, b: f"{a} ({round(100 * a / b)}%)"  # noqa: E731
    t5 = [
        ("Briefs run", s["briefs_run"], m["briefs_run"], f"{r['briefs_run']} ({r['briefs']} briefs)"),
        ("Accepted scenarios", s["accepted"], m["accepted"], r["accepted"]),
        ("Rejected (no version accepted)", s["rejected"], m["rejected"], r["rejected"]),
        ("Failed (infrastructure)", s["failed"], m["failed"], r["failed"]),
        ("Versions per accepted scenario, median (max)", s["versions"], m["versions"], r["versions"]),
        ("Manual review: scenarios valid / flawed but usable / invalid", " / ".join(map(str, s["review"])),
         " / ".join(map(str, m["review"])), " / ".join(map(str, r["review"]))),
        ("Near misses declared", s["near_misses"], m["near_misses"], r["near_misses"]),
        ("… ruled flawed by the PI (rulings)", s["flawed"], m["flawed"], r["flawed"]),
        ("Regular tests derived (cover, probe, fact probe)", s["derived"], m["derived"], r["derived"]),
        ("… dropped by the witness check", s["dropped"], m["dropped"], r["dropped"]),
        ("… left out by the rulings", s["left_out"], m["left_out"], r["left_out"]),
        ("**Valid regular tests**", f"**{s['valid']}**", f"**{m['valid']}**", f"**{r['valid']}**"),
        ("Facts covered (RQ2)", s["facts_covered"], m["facts_covered"], f"{r['facts_covered']} of {r['brief_facts']}"),
    ]
    sh, rh = halves["Sonnet"]["all"], halves["Muse regenerated"]["all"]
    two = [
        ("Writer", "Sonnet (autogen_01's arms R, P, P v2)", "Muse (regen_01, the frozen pipeline)"),
        ("Briefs run (distinct fact sets)", f"{s['briefs_run']} ({s['fact_sets']})", f"{r['briefs_run']} ({r['briefs']})"),
        ("Accepted scenarios (usable after review)", f"{s['accepted']} ({s['usable']})", f"{r['accepted']} ({r['usable']})"),
        ("Near misses declared (ruled flawed)", f"{s['near_misses']} ({s['flawed']})", f"{r['near_misses']} ({r['flawed']})"),
        ("Valid regular tests", s["valid"], r["valid"]),
        ("Valid absence / underspecified units", f"{s['absence_units']} / {s['underspecified_units']}",
         f"{r['absence_units']} / {r['underspecified_units']}"),
        ("Facts covered", f"{s['facts_covered']}", f"{r['facts_covered']} (of them, {r['of_sonnet_81']} of Sonnet's {s['facts_covered']})"),
        ("Tests exposing a fact (OpenClaw, self-hosted Qwen, 3 trials)", pct(sh["tests_exposing"], sh["tests"]),
         pct(rh["tests_exposing"], rh["tests"])),
        ("Facts exposed at detect@3", sh["facts_detect3"], rh["facts_detect3"]),
        ("Facts exposed at detect@1", sh["facts_detect1"], rh["facts_detect1"]),
        (f"Of Sonnet's {the81['facts']} facts, exposed at detect@3", f"{the81['Sonnet']['exposed_detect3']}",
         f"{the81['Muse regenerated']['exposed_detect3']} ({len(the81['both'])} in both)"),
        ("Quiet-host reading (host-load timeouts re-run)", "not re-run",
         f"{quiet['tests_exposing']} tests, {quiet['facts_detect3']} facts @3, {quiet['facts_detect1']} @1"),
    ]
    assert (sh["tests"], sh["tests_exposing"], sh["facts_detect3"], sh["facts_detect1"]) == tuple(
        s["exposure"][k] for k in ("tests", "tests_exposing", "facts_detect3", "facts_detect1")), "Sonnet exposure"
    doc = {"_about": __doc__.split("\n\n")[0], "table5": {"columns": ["Sonnet", "Muse", "Muse regenerated"],
           "rows": [[str(x) for x in row] for row in t5]},
           "two_halves": [[str(x) for x in row] for row in two], "regenerated": r, "sonnet": s, "muse": m}
    (EVAL / "for_report.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print("| | Sonnet | Muse (Phase 4, 6b) | Muse, regenerated (regen_01) |\n|---|---:|---:|---:|")
    for row in t5:
        print("| " + " | ".join(str(x) for x in row) + " |")
    print()
    print(f"| | {two[0][1]} | {two[0][2]} |\n|---|---:|---:|")
    for row in two[1:]:
        print("| " + " | ".join(str(x) for x in row) + " |")
    print()
    print("review categories (mine):", r["review_mine"], "cost:", r["cost"])


if __name__ == "__main__":
    main()
