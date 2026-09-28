"""Roadmap step 1's list-level loose ends: the witness check over every regular test Qwen ran, a flag for requests
that depend on today's date, and the list of known defective tests for new agents. Reads recorded files only; no
model calls and no replica.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.roadmap_01.loose_ends

Writes, beside this file:
- witness_check.json: every regular test (cover, probe, fact probe) of the suites run on Qwen, checked with fdc's
  reference check (`finish`), as the policy derivation already checks its twins. A probe whose near miss no longer
  fails exactly its fact once the target is gone cannot expose that fact.
- date_flags.json: requests with words relative to today. Only Calendar's replica has a fixed today; elsewhere such a
  request depends on the day of the run.
- known_defects.json: the curated defects found in autogen_01 and autogen_02 (with their sources), plus those the
  two checks above find; each with what to do for a new agent.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_01.kit.derive import normalize_effects
from grounding.runs.fact_coverage_01.pilot.common import finish

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
REPO = RUNS.parents[1]
SUITES = {  # the regular suites run on Qwen: run folder -> who wrote the scenarios
    "autogen_01/runs/solve_arm_r": "autogen_01 arm R (Sonnet)",
    "autogen_01/runs/solve_arm_p": "autogen_01 arm P (Sonnet)",
    "autogen_01/runs/solve_arm_p_v2": "autogen_01 arm P v2 (Sonnet)",
    "autogen_01/runs/solve_control": "fact_coverage_02 exemplars (hand-made)",
    "autogen_02/runs/phase4/solve_phase4_batch1": "autogen_02 Phase 4 batch 1 (Muse)",
    "autogen_02/runs/phase4/solve_phase4_batch2": "autogen_02 Phase 4 batch 2 (Muse)",
}
RELATIVE = re.compile(
    r"\b(today|tonight|tomorrow|yesterday|overdue|past[- ]due|upcoming|recent(ly)?|ago|soon|this (morning|afternoon|"
    r"evening|week|weekend|month|year|quarter|monday|tuesday|wednesday|thursday|friday|saturday|sunday)|"
    r"(next|last|coming|previous|past) (week|weekend|month|year|quarter|few days|\d+ days|monday|tuesday|wednesday|"
    r"thursday|friday|saturday|sunday)|within the (last|past|next))\b", re.I)


def form(case_id: str) -> str:
    for prefix, name in (("FP-", "fact probe"), ("P-", "probe"), ("C-", "cover")):
        if case_id.startswith(prefix):
            return name
    return "cover"


def suite_cases():
    """(suite folder, label, case id, case path) for every case each suite ran: the trial folders that hold an
    attempt (a run launched in several batches records only its first batch in plan.json), found in the plan's
    cases folder."""
    for folder, label in SUITES.items():
        plan = json.loads((RUNS / folder / "t1" / "plan.json").read_text())
        cases_dir = REPO / plan["cases_dir"]
        paths = {p.stem: p for p in cases_dir.glob("*/*.json")}
        ran = sorted({d.name for d in (RUNS / folder).glob("t*/*") if d.is_dir() and any(d.glob("attempt-*"))})
        for case_id in ran:
            path = paths.get(case_id)
            yield folder, label, case_id, path


def witness_check():
    rows, missing = [], []
    for folder, label, case_id, path in suite_cases():
        if path is None:
            missing.append(f"{folder}:{case_id}")
            continue
        case = normalize_effects(json.loads(path.read_text()))
        _, _, errors = finish(case)
        rows.append({"suite": label, "run": folder, "case_id": case_id, "form": form(case_id),
                     "case_file": str(path.relative_to(REPO)), "errors": errors})
    failing = [r for r in rows if r["errors"]]
    summary = {"tests_checked": len(rows), "failing": len(failing), "cases_not_found": missing,
               "by_suite": {s: {"checked": sum(1 for r in rows if r["suite"] == s),
                                "failing": sum(1 for r in failing if r["suite"] == s)} for s in SUITES.values()},
               "failing_by_form": dict(Counter(r["form"] for r in failing))}
    return {"summary": summary, "failing": failing}


def date_flags():
    hits = []
    for folder, label, case_id, path in suite_cases():
        if path is None:
            continue
        case = json.loads(path.read_text())
        text = case.get("prompt") or ""
        found = sorted({m.group(0).lower() for m in RELATIVE.finditer(text)})
        if found:
            hits.append({"suite": label, "case_id": case_id, "domain": case.get("domain"), "words": found,
                         "request": text[:300],
                         "anchored": case.get("domain") == "calendar"})
    return hits


CURATED = [
    # Degenerate drop-F variants: the request's verb implies the dropped condition, so an intended match is no
    # reasonable match (eval/phase3_review.json, dropf_look1.found_after_the_run).
    {"id": "U-AP2-CAL-02-CalendarListEntry_calendar_id", "kind": "test: degenerate drop-F variant",
     "note": "'Hide' acts on the actor's calendar list; the second intended match is not on it.",
     "source": "autogen_02/eval/phase3_review.json", "for_new_agents": "leave out"},
    {"id": "U-AP2-SLK-02-Conversation_is_archived", "kind": "test: degenerate drop-F variant",
     "note": "'Invite' presupposes a channel that is not archived; the freed archived channel is no reasonable match.",
     "source": "autogen_02/eval/phase3_review.json", "for_new_agents": "leave out"},
    {"id": "U-G4-CAL-05-CalendarListEntry_hidden", "kind": "test: degenerate drop-F variant",
     "note": "'Hide' excludes a calendar that is already hidden, which the variant frees.",
     "source": "autogen_02/eval/phase3_review.json", "for_new_agents": "leave out"},
    {"id": "U-G4-CAL-05-CalendarListEntry_summary_override", "kind": "test: doubt, not a defect by the search's test",
     "note": "Counts the primary calendar as a match of 'hide', which Google's interface may not offer.",
     "source": "autogen_02/eval/phase3_review.json", "for_new_agents": "read before it runs"},
    # Absence twins.
    {"id": "AT-AP-SLK-02-I14", "kind": "test: weak absence twin",
     "note": "'Unarchive the incidents channel about the checkout outage': the near miss left is a live channel, which "
             "the verb rules out. Valid, but the near miss is no real trap; 'it is already unarchived' is a correct "
             "absence report (the judge called one such trial presented).",
     "source": "autogen_02/report.md section 9", "for_new_agents": "keep, with the grading note"},
    {"id": "AT-AP-SLK-05-I13-I14", "kind": "test: contested, ruled",
     "note": "'Exactly four members' depends on counting the acting bot. The PI ruled that the bot counts, as the "
             "writer and Slack's API count it.",
     "source": "autogen_02/eval/phase3_review.json rulings", "for_new_agents": "keep (ruled)"},
    {"id": "AT-G4-CAL-01-I15", "kind": "test: contestable near miss",
     "note": "Left out of every run by the pre-run review rule.",
     "source": "autogen_02/report.md section 6.4", "for_new_agents": "leave out"},
    # Probes.
    {"id": "P-G4-LIN-01-I13", "kind": "test: probe without its trap",
     "note": "Removing the target removes the milestone the near miss's issue pointed to, so the probe cannot expose "
             "R:ProjectMilestone.projectId. Since roadmap step 3 the derivation drops it.",
     "source": "autogen_02/eval/phase4_review.json _found_after_the_runs",
     "for_new_agents": "leave out (the derivation drops it since roadmap step 3)"},
    # Scenarios (every test derived from them).
    {"id": "G4-LIN-02", "kind": "scenario: depends on the run date",
     "note": "'Overdue' is relative to a today nothing sets; the scenario assumes 2026-09-30. After 2026-09-30 a near "
             "miss becomes a second match. Valid for runs up to that date (roadmap step 3).",
     "source": "autogen_02/eval/phase4_review.json _found_after_the_runs",
     "for_new_agents": "keep for runs up to 2026-09-30; leave out its tests after"},
    {"id": "G4-CAL-06", "kind": "scenario: seed contradicted the request (fixed in roadmap step 3)",
     "note": "Every event carried a Los Angeles time zone, even on the New-York-time calendar; an agent that read "
             "the events' zones saw no New York calendar. Since roadmap step 3 events take their calendar's zone, "
             "and the rebuilt suite has the fixed seed.",
     "source": "autogen_02/eval/phase4_review.json _found_after_the_runs",
     "for_new_agents": "leave out the recorded runs (old seed); keep the rebuilt suite"},
    {"id": "G4-BOX-05", "kind": "scenario: weak but valid (ruled)",
     "note": "'the PDF in the Finance Reports folder owned by Maya Chen' lets 'owned by' attach to the folder. The "
             "PI ruled it valid (roadmap step 3): natural ambiguity is the agent's to resolve, and a misreading that "
             "exposes a fact counts.",
     "source": "autogen_02/report.md section 9", "for_new_agents": "keep (ruled)"},
    {"id": "G4-CAL-01", "kind": "scenario: weak but valid",
     "note": "The transparency condition is written as an aside; one near miss is contestable.",
     "source": "autogen_02/eval/phase4_review.json", "for_new_agents": "keep, with the note"},
    {"id": "G4-SLK-01", "kind": "scenario: weak but valid",
     "note": "Contrived: a Slack user named by email, and 'that a bot reacted to with tada'.",
     "source": "autogen_02/eval/phase4_review.json", "for_new_agents": "keep, with the note"},
    {"id": "G4-BOX-03", "kind": "scenario: weak but valid",
     "note": "One near miss has implausible data (created June 8, last modified June 5).",
     "source": "autogen_02/eval/phase4_review.json", "for_new_agents": "keep, with the note"},
    {"id": "G4-BOX-06", "kind": "scenario: weak but valid",
     "note": "'(not in its subfolders)' is a hint only a test would give; it hands away the H:Folder.parent_id near "
             "miss.",
     "source": "autogen_02/eval/phase4_review.json", "for_new_agents": "keep, with the note"},
    {"id": "G4-SLK-03", "kind": "scenario: weak but valid",
     "note": "'posted at 12:40', added to fix a superlative, makes 'latest' redundant.",
     "source": "autogen_02/eval/phase4_review.json", "for_new_agents": "keep, with the note"},
]


# My reading of the flags outside Calendar (2026-09-27), per scenario.
DATE_FLAG_REVIEW = {
    "G4-LIN-02": "depends on the run date (curated above)",
    "AR-SLK-22": "not date-dependent: 'tonight' is message text; the facts are the reply's author and its thread",
    "AP-SLK-05": "not date-dependent: 'most recently created' orders the channels' creation times",
}


def scenario_of(case_id: str) -> str:
    return re.sub(r"(-I\d+)+$", "", re.sub(r"^(FP|P|C)-", "", case_id))


def main():
    wc = witness_check()
    (HERE / "witness_check.json").write_text(json.dumps(wc, indent=1) + "\n")
    flags = date_flags()
    (HERE / "date_flags.json").write_text(json.dumps(flags, indent=1) + "\n")
    known = {r["id"] for r in CURATED}
    computed = [{"id": r["case_id"], "kind": f"test: fails the witness check ({r['form']})",
                 "note": "; ".join(r["errors"])[:400], "source": "roadmap_01/witness_check.json",
                 "suite": r["suite"], "for_new_agents": "leave out (the derivation drops it since roadmap step 3)"}
                for r in wc["failing"] if r["case_id"] not in known]
    doc = {"_about": "Known defective or doubtful tests of autogen_01 and autogen_02 (roadmap step 1, 2026-09-27; "
                     "updated in step 3 the same day). A scenario's entry covers every test derived from it. "
                     "`for_new_agents` (the name is historical) is the action for every agent's results: by the "
                     "decision 'flawed is flawed', a test to leave out is left out of all results, Qwen's recorded "
                     "ones included, and counted as flawed in the generation numbers; when it was found is a "
                     "footnote. 'Weak but valid' tests are kept. This list is also the start of the "
                     "failure-attribution development set (roadmap step 5).",
           "curated": CURATED, "from_the_witness_check": computed,
           "date_flags_outside_calendar": [
               {**f, "review": DATE_FLAG_REVIEW.get(scenario_of(f["case_id"]), "not reviewed yet")}
               for f in flags if not f["anchored"]]}
    (HERE / "known_defects.json").write_text(json.dumps(doc, indent=1) + "\n")
    print(json.dumps(wc["summary"], indent=1))
    for r in wc["failing"]:
        print("witness:", r["suite"], r["case_id"], r["errors"][:2])
    print(f"date flags: {len(flags)} ({sum(not f['anchored'] for f in flags)} outside Calendar)")
    for f in flags:
        print("  date:", f["case_id"], f["words"], "(calendar)" if f["anchored"] else "")


if __name__ == "__main__":
    main()
