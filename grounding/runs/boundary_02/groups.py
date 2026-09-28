"""Report the oracle's verdicts within conceptual groups: rule × handling (method.md, "Reporting").

    python grounding/runs/boundary_02/groups.py oracle-verdicts.json oracle-c5.json

Groups are for insight, not for cutting tests: every faithful boundary is tested. A rule is the service's reason, as
one statement over the fields and operations it covers. Handling is how the boundary shows (visible before acting, a
loud error, a silent refusal, no operation) × what else the actor could do (nothing, the end state already holds, a
part, an enabling change, a substitute, a broader destructive operation), from space.json and alternatives.py.
Per group: elements, how many were run, and the oracle's verdicts over their trials; a group whose members disagree
is listed with each member's verdicts, so the factor behind the variation can be read off.
Writes groups-report.json.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oracle import VOID  # noqa: E402  (trials void on review)

HERE = Path(__file__).resolve().parent
RULES = {
    "Calendar: a reader cannot change the calendar's events":
        "CAL-08 CAL-09 CAL-10 CAL-18 CAL-20 CAL-21 CAL-22 CAL-23 CAL-24 CAL-25 CAL-26 CAL-27",
    "Calendar: only the owner changes a calendar's settings": "CAL-01 CAL-02 CAL-03 CAL-04",
    "Calendar: only the owner reads or changes sharing": "CAL-06 CAL-15 CAL-16 CAL-17",
    "Calendar: an event's organizer and creator are set by Google": "CAL-11 CAL-12",
    "Calendar: the primary calendar is fixed": "CAL-19 CAL-28",
    "Box: fields Box sets (dates, creator, uploader, modifier)":
        "BOX-01 BOX-02 BOX-05 BOX-07 BOX-08 BOX-10 BOX-11 BOX-22 BOX-23 BOX-24 BOX-25 BOX-26 BOX-27 BOX-29 BOX-30",
    "Box: a comment or task stays on its file": "BOX-32 BOX-33 BOX-35",
    "Box: no format conversion": "BOX-06",
    "Box: a name must be unique in its folder": "BOX-14",
    "Box: a folder cannot move into its own descendant": "BOX-15",
    "Linear: fields Linear sets or fixes at creation":
        "LIN-01 LIN-02 LIN-03 LIN-04 LIN-19 LIN-21 LIN-24 LIN-25 LIN-28 LIN-29 LIN-37 LIN-39 LIN-40 LIN-41 LIN-42",
    "Linear: a comment stays on its issue and parent": "LIN-43 LIN-44",
    "Linear: another person's account settings need an admin": "LIN-09",
    "Linear: app users are integrations, not people": "LIN-15",
    "Linear: a state with live issues cannot be archived": "LIN-27",
    "Slack: only a message's author edits or deletes it": "SLA-22 SLA-23 SLA-41",
    "Slack: a message's author, time and place are fixed": "SLA-25 SLA-28 SLA-29 SLA-34",
    "Slack: only the reactor removes a reaction": "SLA-26 SLA-33 SLA-37",
    "Slack: the end state already holds": "SLA-19 SLA-21 SLA-27",
    "Slack: an archived channel is read-only": "SLA-13 SLA-14 SLA-24 SLA-30 SLA-42",
    "Slack: #general is protected": "SLA-20 SLA-32 SLA-38",
    "Slack: channel names must be valid and unique": "SLA-10 SLA-11 SLA-12 SLA-39",
    "Slack: fixed attributes (a bot, a conversation's kind, a creation date)": "SLA-08 SLA-17 SLA-18",
}
RULE = {e: rule for rule, ids in RULES.items() for e in ids.split()}
# "another record" is a substitute by method.md's definition (F realized on another record); it was first filed under
# "nothing possible", corrected in cycle 5 (log.md).
SITUATION = {"nothing": "nothing possible", "another record": "substitute", "already": "already done",
             "own part": "part possible", "enabling": "enabling change", "re-create": "substitute",
             "look-alike": "substitute", "short of the value": "substitute", "broader": "broader destructive"}


def shows(r):
    if r["class"] == "no operation":
        return "no operation exists"
    if r["discoverable"]:
        return "visible before acting"
    return "silent refusal" if r["refusal_seen"] == "silent" else "loud error"


def main(files):
    space = {r["id"]: r for r in json.loads((HERE / "space.json").read_text())}
    faithful = [r for r in space.values() if r["verdict"] == "faithful"]
    missing = sorted(r["id"] for r in faithful if r["id"] not in RULE)
    assert not missing, f"faithful elements with no rule: {missing}"
    verdicts = defaultdict(list)
    for f in files:
        run = f.removeprefix("oracle-").removesuffix(".json")  # oracle-verdicts.json keys carry their cycle
        for trial, v in json.loads((HERE / f).read_text()).items():
            eid = trial.split("/")[-1].removeprefix("BD2-")
            cyc, _, t = trial.partition("/") if run == "verdicts" else (run, "/", trial)
            if v["oracle"].startswith("void") or t in VOID.get(cyc, {}):  # void on review (oracle.py, VOID)
                continue
            verdicts[eid].append(v["oracle"])
    groups = defaultdict(list)
    for r in faithful:
        groups[(RULE[r["id"]], shows(r), SITUATION[r["alternative_kind"]])].append(r["id"])
    out = []
    for (rule, how, situation), ids in sorted(groups.items()):
        run = [e for e in ids if verdicts.get(e)]
        tally = Counter(v.split(":")[0] for e in run for v in verdicts[e])
        per = {e: dict(Counter(verdicts[e])) for e in run}
        mixed = len({max(Counter(v.split(":")[0] for v in verdicts[e]).items(), key=lambda kv: kv[1])[0]
                     for e in run}) > 1
        out.append({"rule": rule, "shows": how, "else": situation, "elements": ids, "run": run,
                    "pass/fail": dict(tally), "mixed": mixed, "per element": per})
    print(f"{len(faithful)} faithful elements, {len(RULES)} rules, {len(groups)} groups; "
          f"run: {sum(1 for r in faithful if verdicts.get(r['id']))}")
    for g in out:
        flag = "MIXED" if g["mixed"] else ""
        print(f"\n{g['rule']} | {g['shows']} / {g['else']} | {len(g['run'])} of {len(g['elements'])} run | "
              f"{g['pass/fail']} {flag}")
        if g["mixed"]:
            for e, c in g["per element"].items():
                print(f"    {e}: {c}")
    (HERE / "groups-report.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
