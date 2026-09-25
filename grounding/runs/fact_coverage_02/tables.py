"""Tables for report.md, computed from the scored runs and manual labels. No service calls.

    python -m grounding.runs.fact_coverage_02.tables > tables.md

A distinct bug is a distinct fact exposed in at least one trial of a test (`policy:` entries are policy results,
not fact bugs). Reruns of fixed scenarios supersede their v1 tests (SUPERSEDED). Facts exposed only through a
trial labelled contestable are marked with *.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.fact_coverage_02.score import collect

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
SUPERSEDED = {  # v1 test ids -> the run that reran the fixed scenario
    **{c: "method_new_lin25" for c in ("LIN-25", "P-LIN-25-I11", "P-LIN-25-I12")},
    **{c: "method_new_slk21" for c in ("SLK-21", "P-SLK-21-I11", "P-SLK-21-I12", "P-SLK-21-I13", "P-SLK-21-I14",
                                       "SLK-21-A", "SLK-21-A-I14")},
}
PILOT_BUGS = ["A:Event.creator_email", "R:Folder.created_by_id", "R:TaskAssignment.assigned_by_id",
              "R:File.modified_by_id", "R:HubItem.folder", "R:File.collections", "R:issue_label_issue_association",
              "R:Document.initiativeId", "R:IssueRelation.issueId", "D:local_time",
              "A:CalendarListEntry.summary_override", "A:User.displayName", "D:all_day", "A:TeamMembership.owner",
              "B:TeamMembership", "A:File.version_number"]


def load(runs, only=None):
    manual = json.loads((HERE / "manual_labels.json").read_text())
    tests = collect([RUNS / r for r in runs if (RUNS / r).exists()], manual, only)
    keep = []
    for t in tests:
        if t["run"] == "method_new" and t["case_id"] in SUPERSEDED:
            continue
        keep.append(t)
    return keep


def facts(tests, strict=False):
    key = "exposed_strict" if strict else "exposed"
    return {x for t in tests for x in t[key] if not x.startswith("policy:")}


def mark(fs, strict):
    return ", ".join(f"`{f}`" + ("" if f in strict else "*") for f in sorted(fs)) or "none"


def row(label, tests):
    exposing = [t for t in tests if t["failures"]]
    fs, strict = facts(tests), facts(tests, strict=True)
    trials = sum(len(t["trials"]) for t in tests)
    established = sum(t["established"] for t in tests)
    return (f"| {label} | {len(tests)} | {len(exposing)} | {len(fs)} ({len(strict)}) | {established}/{trials} | "
            f"{mark(fs, strict)} |")


HEAD = ("| Arm | Tests | Tests exposing | Distinct facts (uncontested) | Trials established | Facts |\n"
        "|---|---:|---:|---:|---:|---|")


def new_facts():
    tests = load(["method_new", "method_new_lin25", "method_new_slk21"])
    out = ["## New facts: cover-style control vs method probes", "", HEAD]
    by_domain = defaultdict(list)
    for t in tests:
        by_domain[t["domain"]].append(t)
    for domain in ("box", "calendar", "linear", "slack"):
        ts = by_domain[domain]
        out.append(row(f"{domain} control", [t for t in ts if t["form"] == "cover control"]))
        out.append(row(f"{domain} probes", [t for t in ts if t["form"] in ("probe", "packed plain")]))
    controls = [t for t in tests if t["form"] == "cover control"]
    probes = [t for t in tests if t["form"] in ("probe", "packed plain")]
    out.append(row("**all controls**", controls))
    out.append(row("**all probes**", probes))
    out.append(row("**controls + probes**", controls + probes))
    only_c, only_p = facts(controls) - facts(probes), facts(probes) - facts(controls)
    out += ["", f"Found only by a control: {mark(only_c, facts(controls, True))}. "
                f"Found only by probes: {mark(only_p, facts(probes, True))}.", ""]
    return out, tests


def families(tests, title):
    out = [f"## Yield by family: {title}", "",
           "| Family | Probes | Exposing | Share | Distinct facts |", "|---|---:|---:|---:|---:|"]
    fam = defaultdict(list)
    for t in tests:
        if t["form"] == "probe":
            fam[t["family"]].append(t)
    for f in sorted(fam):
        ts = fam[f]
        n = sum(1 for t in ts if t["failures"])
        out.append(f"| {f} | {len(ts)} | {n} | {n / len(ts):.0%} | {len(facts(ts))} |")
    return out + [""]


def pilot_facts():
    out = ["## Pilot facts: budget points", "", HEAD]
    b1 = load(["b1"])
    b1_t1 = load(["b1"], only=["t1"])
    method = load(["method_pilot", "method_pilot_panel"])
    method_t1 = load(["method_pilot", "method_pilot_panel"], only=["t1"])
    layer = [t for t in b1 if t["form"] == "target-present layer"]
    layer_t1 = [t for t in b1_t1 if t["form"] == "target-present layer"]

    def pick(ts, forms=None, sub=None):
        return [t for t in ts if (forms is None or t["form"] in forms)
                and (sub is None or (t["family"] not in (None, "F0")) == sub)]
    out.append(row("B1 cover cases, trial 1", b1_t1))
    out.append(row("B1 cover cases, 3 trials", b1))
    for label, ts in [("substitute probes (F1–F8)", pick(method, ["probe"], True)),
                      ("+ packed plain tests", pick(method, ["probe"], True) + pick(method, ["packed plain"])),
                      ("all probes (F0 one by one)", pick(method, ["probe"])),
                      ("all probes + packed + layer", pick(method, ["probe", "packed plain"]) + layer)]:
        out.append(row(label + ", 3 trials", ts))
    out.append(row("all probes + packed + layer, trial 1",
                   pick(method_t1, ["probe", "packed plain"]) + layer_t1))
    out.append(row("B1 + substitute probes, 3 trials", b1 + pick(method, ["probe"], True)))
    found = facts(pick(method, ["probe", "packed plain"]) + b1)
    out += ["", f"Pilot bugs (16) found again: {', '.join(f'`{b}`' for b in PILOT_BUGS if b in found) or 'none'}.",
            f"Pilot bugs not found: {', '.join(f'`{b}`' for b in PILOT_BUGS if b not in found) or 'none'}.",
            f"Facts not among the pilot's 16: {mark(found - set(PILOT_BUGS), found)}.", ""]
    return out, method + b1


def panel(tests):
    out = ["## Policy panel", "", "| Test | Domain | Note | Failing trials |", "|---|---|---|---:|"]
    for t in tests:
        if t["form"] == "policy panel":
            out.append(f"| {t['case_id']} | {t['domain']} | {t.get('note') or ''} | {t['failures']}/{t['established']} |")
    return out + [""]


def usage(runs):
    out = ["## Usage", "", "| Run | Tests | Requests | Input tokens | Output tokens |", "|---|---:|---:|---:|---:|"]
    for r in runs:
        ts = load([r])
        if not ts:
            continue
        out.append(f"| {r} | {len(ts)} | {sum(t['requests'] for t in ts):,} | "
                   f"{sum(t['tokens']['input'] for t in ts):,} | {sum(t['tokens']['output'] for t in ts):,} |")
    return out + [""]


def main():
    lines, new = new_facts()
    lines += families(new, "new facts")
    pilot_lines, pilot = pilot_facts()
    lines += pilot_lines + families([t for t in pilot if t["run"] == "method_pilot"], "pilot facts")
    lines += panel(new + pilot)
    lines += usage(["b1", "method_new", "method_new_lin25", "method_new_slk21", "method_pilot", "method_pilot_panel"])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
