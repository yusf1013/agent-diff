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
    t1 = load(["method_new", "method_new_lin25", "method_new_slk21"], only=["t1"])
    out.append(row("all controls, trial 1", [t for t in t1 if t["form"] == "cover control"]))
    out.append(row("all probes, trial 1", [t for t in t1 if t["form"] in ("probe", "packed plain")]))
    only_c, only_p = facts(controls) - facts(probes), facts(probes) - facts(controls)
    out += ["", f"Found only by a control: {mark(only_c, facts(controls, True))}. "
                f"Found only by probes: {mark(only_p, facts(probes, True))}.", ""]
    return out, tests


def families(tests, title):
    out = [f"## Yield by family: {title}", "",
           "| Family | Probes | Exposing | Share | Distinct facts | Found by no other family |", "|---|---:|---:|---:|---:|---|"]
    fam = defaultdict(list)
    for t in tests:
        if t["form"] == "probe":
            fam[t["family"]].append(t)
    for f in sorted(fam):
        ts = fam[f]
        n = sum(1 for t in ts if t["failures"])
        others = facts([t for g, us in fam.items() if g != f for t in us])
        unique = sorted(facts(ts) - others)
        out.append(f"| {f} | {len(ts)} | {n} | {n / len(ts):.0%} | {len(facts(ts))} | "
                   f"{len(unique)}: {', '.join(f'`{u}`' for u in unique)} |")
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


def bug_list(tests, manual):
    """One row per distinct fact: the tests exposing it (failing trials / established trials) and a reviewed note."""
    by_fact = defaultdict(list)
    for t in tests:
        for f in t["exposed"]:
            if not f.startswith("policy:"):
                by_fact[f].append(t)
    out = ["## Distinct facts exposed", "",
           "| Fact | Domain | Pilot bug | Tests (failing/established trials) | One reviewed trial |", "|---|---|---|---|---|"]
    for f in sorted(by_fact, key=lambda x: (by_fact[x][0]["domain"], x)):
        ts = by_fact[f]
        cells = ", ".join(f"{t['case_id']} ({'' if t['run'] == 'b1' else t['family'] or t['form'] or ''}"
                          f"{', B1' if t['run'] == 'b1' else ''}) {t['failures']}/{t['established']}" for t in ts)
        note = ""
        for t in ts:
            for trial, r in sorted(t["trials"].items()):
                label = manual.get(f"{t['run']}/{trial}/{t['case_id']}")
                if label and f in label.get("exposed", []) and label.get("note"):
                    note = f"{t['run']}/{trial}/{t['case_id']}: {label['note']}"
                    break
            if note:
                break
        pilot = str(PILOT_BUGS.index(f) + 1) if f in PILOT_BUGS else ""
        out.append(f"| `{f}` | {ts[0]['domain']} | {pilot} | {cells} | {note.replace('|', '/')} |")
    return out + [""]


def usage(runs):
    """Every attempt of every trial, including retries and superseded first versions (provider-reported)."""
    out = ["## Usage (all attempts)", "",
           "| Run | Case ids | Attempts | Requests | Input tokens | Output tokens | Cache tokens |",
           "|---|---:|---:|---:|---:|---:|---:|"]
    total = defaultdict(int)
    for r in runs:
        cases, row = set(), defaultdict(int)
        for path in sorted((RUNS / r).glob("t*/*/attempt-*/execution_summary.json")):
            s = json.loads(path.read_text())
            u = s.get("usage") or {}
            cases.add(s["case_id"])
            row["attempts"] += 1
            row["requests"] += u.get("total_requests", 0)
            row["input"] += u.get("input_tokens", 0)
            row["output"] += u.get("output_tokens", 0)
            row["cache"] += u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)
        if not row["attempts"]:
            continue
        for k, v in row.items():
            total[k] += v
        out.append(f"| {r} | {len(cases)} | {row['attempts']} | {row['requests']:,} | {row['input']:,} | "
                   f"{row['output']:,} | {row['cache']:,} |")
    out.append(f"| **total** | | {total['attempts']} | {total['requests']:,} | {total['input']:,} | "
               f"{total['output']:,} | {total['cache']:,} |")
    return out + ["", "Exploration runs (`smoke_slack`) and no-model preflights (`prepare_*`) are not counted."]


def denominators(runs):
    """Trials per run (latest attempt of each trial; superseded v1 tests excluded) and why any lack a result."""
    out = ["## Trials without a result", "",
           "| Run | Trials | Established | Timeout | Infrastructure | Replica or seed artifact | Other |",
           "|---|---:|---:|---:|---:|---:|---:|"]
    for r in runs:
        ts = load([r])
        if not ts:
            continue
        counts = defaultdict(int)
        for t in ts:
            for trial, res in t["trials"].items():
                counts["trials"] += 1
                if res["outcome"] not in ("not_established", "artifact"):
                    counts["established"] += 1
                    continue
                if res["outcome"] == "artifact":
                    counts["artifact"] += 1
                    continue
                attempt = sorted((RUNS / r / trial / t["case_id"]).glob("attempt-*"))[-1]
                s = json.loads((attempt / "execution_summary.json").read_text())
                kind = ("infra" if s.get("status") == "infrastructure_error" else
                        "timeout" if s.get("termination") == "timeout" else "other")
                counts[kind] += 1
        out.append(f"| {r} | {counts['trials']} | {counts['established']} | {counts['timeout']} | {counts['infra']} | "
                   f"{counts['artifact']} | {counts['other']} |")
    return out + [""]


def fact_probes():
    """Each fact probe (all decoys of one fact together) against the single-decoy probes of the same decoys."""
    from grounding.runs.fact_coverage_02.analyze import trial_rows
    suite = json.loads((HERE / "suite_factprobe.json").read_text())
    if not (RUNS / "factprobe").exists():
        return []
    fp = {t["case_id"]: t for t in load(["factprobe"])}
    singles = {t["case_id"]: t for t in load(["method_new", "method_new_lin25", "method_new_slk21", "method_pilot"])}
    acted = defaultdict(lambda: defaultdict(int))  # fact probe -> decoy -> failing trials acting on it
    for row in trial_rows(RUNS / "factprobe"):
        res = fp.get(row["case_id"], {}).get("trials", {}).get(row["trial"])
        if res and res["outcome"] in ("incorrect", "presented"):
            for ref in row.get("references", []):
                for e in ref["exposed"]:
                    acted[row["case_id"]][e["witness"]] += 1
    out = ["## Fact probes: all of a fact's decoys together vs one decoy per probe", "",
           "| Fact probe | Fact | Together: failing trials (decoys acted on) | Alone: failing trials per decoy |",
           "|---|---|---|---|"]
    together, alone, n_alone = set(), set(), 0
    for s in suite:
        t = fp.get(s["case_id"])
        if not t:
            continue
        if t["failures"]:
            together.add(s["fact"])
        cells = []
        for sid, fam in zip(s["singles"], s["families"]):
            st = singles.get(sid)
            cells.append(f"{fam} {st['failures']}/{st['established']}" if st else f"{fam} not run")
            n_alone += 1
            if st and st["failures"] and s["fact"] in st["exposed"]:
                alone.add(s["fact"])
        hits = ", ".join(f"{w} ×{n}" for w, n in sorted(acted[s["case_id"]].items()))
        out.append(f"| {s['case_id']} | `{s['fact']}` | {t['failures']}/{t['established']}"
                   f"{f' ({hits})' if hits else ''} | {'; '.join(cells)} |")
    out += ["", f"Facts exposed with all decoys together: {len(together)} of {len(suite)} facts ({len(suite)} tests). "
                f"Exposed by some single-decoy probe: {len(alone)} ({n_alone} tests). "
                f"Only together: {sorted(together - alone) or 'none'}. Only alone: {sorted(alone - together) or 'none'}.", ""]
    return out


def compact(label, tests, bold=False):
    exposing = sum(1 for t in tests if t["failures"])
    fs, strict = facts(tests), facts(tests, strict=True)
    trials = sum(len(t["trials"]) for t in tests)
    est = sum(t["established"] for t in tests)
    cell = f"{len(fs)}" if fs == strict else f"{len(fs)} ({len(strict)})"
    b = "**" if bold else ""
    return f"| {b}{label}{b} | {len(tests)} | {exposing} | {b}{cell}{b} | {est}/{trials} |"


def report_tables():
    """The exact rows of report.md §5.1, §6 and §7 (paste, do not retype)."""
    head = "| Arm | Tests | Tests exposing | Distinct facts | Trials established |\n|---|---:|---:|---:|---:|"
    b1, b1_t1 = load(["b1"]), load(["b1"], only=["t1"])
    m, m_t1 = load(["method_pilot"]), load(["method_pilot"], only=["t1"])
    layer = [t for t in b1 if t["form"] == "target-present layer"]
    layer_t1 = [t for t in b1_t1 if t["form"] == "target-present layer"]
    sub = [t for t in m if t["form"] == "probe" and t["family"] not in (None, "F0")]
    probes = [t for t in m if t["form"] == "probe"]
    packed = [t for t in m if t["form"] == "packed plain"]
    nearest = [t for t in m if t["case_id"].startswith("PB-")]
    out = ["### §5.1", "", head,
           compact("B1 cover cases, trial 1", b1_t1), compact("B1 cover cases, 3 trials", b1),
           "| B2, the pilot's fact-sensitive cases (mostly 1 trial) | 125 | | 16 | |",
           compact("Method: substitute probes (F1–F8)", sub),
           compact("… plus packed plain tests", sub + packed),
           compact("… F0 decoys one by one instead", probes),
           compact("… plus packed and layer tests", probes + packed + layer),
           compact("Method (all but the panel), trial 1",
                   [t for t in m_t1 if t["form"] in ("probe", "packed plain")] + layer_t1),
           compact("B1 plus substitute probes", b1 + sub),
           compact("Everything on the pilot's facts (B1 and method)", b1 + probes + packed, bold=True),
           "", f"Nearest-value (PB-*) probes: {len(nearest)} tests, facts {sorted(facts(nearest))}.", ""]
    new = load(["method_new", "method_new_lin25", "method_new_slk21"])
    out += ["### §6", "", head]
    for domain in ("box", "calendar", "linear", "slack"):
        ds = [t for t in new if t["domain"] == domain]
        out.append(compact(f"{domain.capitalize()} control", [t for t in ds if t["form"] == "cover control"]))
        out.append(compact(f"{domain.capitalize()} probes", [t for t in ds if t["form"] in ("probe", "packed plain")]))
    out.append(compact("All controls", [t for t in new if t["form"] == "cover control"], bold=True))
    out.append(compact("All probes", [t for t in new if t["form"] in ("probe", "packed plain")], bold=True))
    out.append(compact("Both", [t for t in new if t["form"] in ("cover control", "probe", "packed plain")], bold=True))
    return out + [""]


def main():
    lines, new = new_facts()
    lines += families(new, "new facts")
    pilot_lines, pilot = pilot_facts()
    lines += pilot_lines + families([t for t in pilot if t["run"] == "method_pilot"], "pilot facts")
    lines += families([t for t in new + pilot if t["run"] != "b1"], "both suites")
    lines += panel(new + pilot)
    from grounding.runs.fact_coverage_02.followups import (fact_probes_equal_runs, hidden_targets, packed_vs_alone,
                                                           request_size, run_budget)
    lines += packed_vs_alone(load) + run_budget(load)
    lines += fact_probes() + fact_probes_equal_runs(load)
    lines += hidden_targets(load) + request_size(load)
    manual = json.loads((HERE / "manual_labels.json").read_text())
    followup = load(["factprobe", "factprobe_extra"]) + [t for t in load(["hidden_pilot"]) if t["form"] == "hidden target"]
    lines += bug_list([t for t in new + pilot if t["form"] != "policy panel"] + followup, manual)
    runs = ["b1", "method_new", "method_new_lin25", "method_new_slk21", "method_pilot", "method_pilot_panel", "factprobe",
            "factprobe_extra", "wording_check", "hidden_pilot"]
    lines += denominators(runs)
    lines += usage(runs)
    lines += ["## Report rows", ""] + report_tables()
    print("\n".join(lines))


if __name__ == "__main__":
    main()
