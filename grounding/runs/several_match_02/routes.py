"""The retrieval route of each recorded plural trial: every API call, with what it returned of the targets.

    python grounding/runs/several_match_02/routes.py [RUN_DIR ...]     # default: several_match_01's runs/main

For each trial it prints one line per call: the step, the call's endpoint and paging or scope parameters, how many
targets and near misses first appeared in its response, and a running count of targets seen. This is the raw
material for classifying routes by hand (log.md): did the agent page, recurse into containers, filter on the server,
use generous page sizes, and query again after a first batch of matches? No service or model calls.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARAMS = re.compile(r"(limit|first|count|maxResults|offset|cursor|after|page|pageToken|ancestor_folder_ids|"
                    r"file_extensions|types|timeMin|timeMax|q|query|channel|filter)=?", re.I)


def endpoint(action: str) -> str:
    a = action.replace("\\n", " ")
    url = re.search(r"https?://[^\s\"']+", a)
    ep = re.sub(r"https?://(api\.box\.com/2\.0|www\.googleapis\.com/calendar/v3|slack\.com/api|api\.linear\.app)",
                "", url.group(0)) if url else "?"
    if "graphql" in ep:
        q = re.search(r"query\"?\s*:\s*\"\s*(?:query|mutation)?\s*\{?\s*([^\"]{0,160})", a.replace('\\"', "'"))
        ep = "gql " + (q.group(1) if q else "?")
    data = " ".join(re.findall(r"(?:-d|--data-urlencode)\s+['\"]([^'\"]{0,120})", a))
    return (ep + (" " + data if data else ""))[:230]


def labels(case: dict, ids: list[str]) -> dict[str, list[str]]:
    """Match records by id only (cycle 0: names shared across records, such as event titles, miscounted)."""
    return {i: [f'"{i}"', f"'{i}'", f"={i}"] for i in ids}


def main(runs: list[Path]):
    for run in runs:
        for att in sorted(run.glob("t*/*/attempt-*")):
            case = json.loads((att / "case.json").read_text())
            ref = case["references"][0]
            targets = [str(t) for t in ref["expected"]]
            decoys = [str(c["witness"]) for c in ref["claims"]]
            names = labels(case, targets + decoys)
            traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
            steps = json.loads(traj.read_text()).get("steps") or []
            seen_t, seen_d = set(), set()
            print(f"\n== {att.parent.parent.name}/{case['case_id']} ({len(targets)} targets)")
            for n, s in enumerate(steps, 1):
                a = s.get("action") or ""
                o = (s.get("observation") or {}).get("stdout", "")
                new_t = {t for t in targets if t not in seen_t and any(x in o for x in names[t])}
                new_d = {d for d in decoys if d not in seen_d and any(x in o for x in names[d])}
                seen_t |= new_t
                seen_d |= new_d
                write = bool(re.search(r"-X\s*(PUT|PATCH|DELETE)|mutation|reactions\.add|chat\.", a))
                print(f"  {n:2d} {'W' if write else 'R'} +{len(new_t)}t +{len(new_d)}d [{len(seen_t)}/{len(targets)}] "
                      f"{endpoint(a)}")


if __name__ == "__main__":
    args = [Path(a) for a in sys.argv[1:]] or [HERE.parent / "several_match_01/runs/main"]
    main(args)
