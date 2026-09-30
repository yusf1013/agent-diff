"""B1, step 1: the covers the agent solves, and the write operations every correct trial used (FeasiGen's rule).

    python -m grounding.runs.related_work_01.b1.traces

FeasiGen (arXiv 2605.28532, abstract): "extracts tool-calling traces from successful executions across multiple agent
systems, identifies critical tools consistently shared across diverse execution strategies, and masks these tools".
Here: the covers of the frozen suite (6a, 6b) that OpenClaw with the self-hosted Qwen solved in all three trials, none
over the 8-minute budget (Box from full_02, the other services from full_03, and 6b from full_04, as the final score
reads them); in each trial, the state-changing calls read from the agent's curl commands; the critical operations are
those every trial used. No model calls. Writes solved.json.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
RUNS = REPO / "grounding/runs/openclaw_eval_01/runs"
# The runs the final score reads, per service (openclaw_eval_01 README: Box's ids did not change, so Box keeps full_02).
SOURCES = [("full_02", {"box"}), ("full_03", {"calendar", "linear", "slack"}), ("full_04", {"box", "calendar", "linear",
                                                                                              "slack"})]
SLACK_READS = {"users.list", "users.info", "users.lookupByEmail", "users.conversations", "users.profile.get",
               "conversations.list", "conversations.history", "conversations.info", "conversations.members",
               "conversations.replies", "search.messages", "search.all", "reactions.get", "reactions.list",
               "auth.test", "team.info", "pins.list", "bots.info", "emoji.list", "usergroups.list", "files.list"}
ID = re.compile(r"(?<=/)(?:[^/?\s]*\d[^/?\s]*|\$\{?\w+\}?[^/?\s]*)(?=/|$)")


def operations(command: str) -> list[str]:
    """The state-changing API operations in one exec command (curl calls only; the skill documents curl)."""
    out = []
    for m in re.finditer(r"\bcurl\b(.*?)(?=\bcurl\b|$)", command, re.S):
        seg = m.group(1)
        url = re.search(r"https://[^\s\"'\\]+", seg)
        if not url:
            continue
        u = url.group(0).split("?")[0]
        method = re.search(r"(?:-X|--request)\s*['\"]?([A-Z]+)", seg)
        has_body = re.search(r"(?:^|\s)(?:-d|--data(?:-raw|-binary|-urlencode)?|-F|--form)\b", seg)
        verb = method.group(1) if method else ("POST" if has_body else "GET")
        if "slack.com/api/" in u:
            name = u.rsplit("/api/", 1)[1]
            if name not in SLACK_READS:
                out.append(f"slack {name}")
        elif "api.linear.app/graphql" in u:
            # the body is often written to a file first (a heredoc, or Python) and sent with -d @file: read the
            # whole command
            body = command[command.find("mutation"):] if "mutation" in command else ""
            names = re.findall(r"\b([a-z]\w*(?:Create|Update|Delete|Archive|Unarchive|Add|Remove|Move|Set|Link|Unlink|"
                               r"Subscribe|Unsubscribe|Resolve|Unresolve|Merge))\s*\(", body)
            out += [f"linear {n}" for n in dict.fromkeys(names)]
        elif verb != "GET" and ("api.box.com" in u or "upload.box.com" in u):
            path = re.sub(r"^https://(?:api|upload)\.box\.com(?:/api)?/2\.0", "", u)
            out.append(f"box {verb} {ID.sub('{id}', path)}")
        elif verb != "GET" and "googleapis.com/calendar/v3" in u:
            path = u.split("/calendar/v3", 1)[1]
            out.append(f"calendar {verb} {ID.sub('{id}', re.sub(r'%40|@', '@', path))}")
    return out


def trial_ops(run: str, trial: str, case_id: str) -> list[str] | None:
    attempts = sorted((RUNS / run / trial / case_id).glob("attempt-*"))
    if not attempts:
        return None
    record = attempts[-1] / "solver" / f"{case_id}.json"
    steps = json.loads(record.read_text())
    ops = []
    for s in (steps.get("steps") or []) + (steps.get("followup_steps") or []):
        if s.get("tool") == "exec":
            ops += operations(s["arguments"].get("command", ""))
    return ops


def main():
    solved = []
    for run, services in SOURCES:
        score = json.loads((RUNS / f"{run}.score.json").read_text())
        adjudicated = json.loads((RUNS / f"{run}.adjudicated.json").read_text())
        over = {o["trial"] for o in adjudicated.get("trials_over_budget", [])}
        for t in score["tests"]:
            if t["domain"] not in services or t["form"] != "cover":
                continue
            outcomes = {k: v.get("outcome") for k, v in t["trials"].items()}
            if len(outcomes) != 3 or any(o != "correct" for o in outcomes.values()):
                continue
            if any(f"{k}/{t['case_id']}" in over for k in outcomes):
                continue
            per_trial = {k: trial_ops(run, k, t["case_id"]) for k in outcomes}
            shared = set.intersection(*(set(v or []) for v in per_trial.values()))
            solved.append({"case_id": t["case_id"], "run": run, "domain": t["domain"],
                           "critical": sorted(shared), "per_trial": {k: sorted(set(v or [])) for k, v in per_trial.items()}})
    (HERE / "solved.json").write_text(json.dumps(solved, indent=1) + "\n")
    by = {}
    for s in solved:
        by.setdefault(s["domain"], []).append(s)
    for d, rows in sorted(by.items()):
        print(f"== {d}: {len(rows)} solved covers; with a shared write operation: {sum(bool(r['critical']) for r in rows)}")
        for r in rows:
            print(f"   {r['case_id']:<14} {r['run']}  critical={r['critical']}")


if __name__ == "__main__":
    main()
