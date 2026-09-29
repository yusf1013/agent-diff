"""The report's numbers, in the PI's terms (phase-2 requirements), from the saved outputs.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.summary

- The coverage space: the covers (91), the plural-worthy ones, and the laziness requirements: stopping early (every
  plural request) and the shortcuts of each request kind (the strategy tables).
- Tests generated automatically (built), and how many are valid: every seed check passed, the cold reader picked
  exactly the targets, the hard case's thorough route finds every target, and no known construction flaw.
- Coverage reached: per request kind, the shortcuts some valid hard test defeats.
- Failures exposed, on valid tests only: targets missed by placement (diligence), near misses acted on by fact
  (discrimination), and timeouts; distinct = (cover, placement) and (cover, fact).
- The judge's true and false positives (review.json, my review of every reported failure) and false negatives
  (review.json's sample of passes).
- Muse tokens and cost (runs/calls.jsonl) and the solver's tokens (execution summaries).
Writes summary.json and prints it.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Cases whose construction was flawed after the checks passed (log: the review found them).
FLAWED = {"SMA-AP-BOX-02-H": "a file and a folder shared an id", "SMA-BOX-23-H": "a file and a folder shared an id",
          "SMA-G4-BOX-04-E": "a file and a folder shared an id"}
# Why a shortcut that no valid hard test defeats is not covered, in the manual investigation's terms (several_match_02
# report, trap reach). Any other undefeated shortcut is reported as a construction gap.
PLACE = {"V": "V, plain view (stopping early)", "C": "C, another container in scope (scope)",
         "H": "H, behind a visibility default (visibility)", "C1": "C1, one folder down (scope)",
         "O": "O, another folder (scope)", "P": "P, past a page (pages)"}
IMPRACTICAL_1000 = "impractical: a container over 1,000 records (method check 6)"
IMPRACTICAL_999 = "impractical: a channel over 999 messages; the channel-list routes reduce to the named channel's page"
NOT_COVERED = {
    ("box", "list named (limit 1000)"): IMPRACTICAL_1000,
    ("box", "list tree, one page per folder (limit 1000)"): IMPRACTICAL_1000,
    ("box", "search extension under folder (limit 200)"): "impractical: a crowd over 200 hits",
    ("box", "search words under folder (limit 200)"): "impractical: a crowd over 200 hits",
    ("box", "list named, every page (limit 1000)"): "not lazy for these requests: a copy in a subfolder of the named "
                                                    "folder is contestable (check 8; the cold reader left it out in "
                                                    "2 of 2 probes, probe_subfolder.py), so none goes there, and every "
                                                    "page of the named folder is the thorough route",
    ("box-anywhere", "search words (limit 200)"): "impractical: a crowd over 200 hits",
    ("linear", "all issues (first 1000)"): "impractical: over 250 issues in scope",
    ("linear", "all issues (first 250)"): "impractical: over 250 issues in scope",
    ("linear", "named team's issues (first 250)"): "not lazy for these requests: the team (named, or pinned through its "
                                                    "state, cycle or project) is the whole scope",
    ("linear", "all issues (first 1000) -> keep the named team"): "not lazy for these requests: the team is the whole "
                                                                  "scope",
    ("linear", "server filter, all conditions (first 250)"): "not lazy for these requests: the filter expresses every "
                                                              "condition",
    ("slack", "named channel history (limit 999)"): IMPRACTICAL_999,
    ("slack", "channel list (default types) -> history"): IMPRACTICAL_999,
    ("slack", "channel list (exclude archived) -> history"): IMPRACTICAL_999,
    ("slack", "channel list (public+private) -> one page of history"): IMPRACTICAL_999,
    ("slack", "named channel history, every page (limit 999)"): "not lazy for these requests: the named channel is "
                                                                "the whole scope",
}


def load(name, default):
    p = HERE / name
    return json.loads(p.read_text()) if p.exists() else default


def main():
    writer, build, reader = load("writer.json", {}), load("build.json", {}), load("reader.json", {})
    checks, grades, review = load("checks.json", {}), load("grades.json", {"trials": []}), load("review.json", {})
    built = {}
    for key, r in build.items():
        for tier, c in (r.get("cases") or {}).items():
            if c.get("built"):
                built[c["id"]] = {"cover": r["cover"], "domain": r["domain"], "table": r["table"],
                                  "pinned": r["pinned"], "tier": tier[0]}
    valid, why_not = {}, {}
    for cid, b in built.items():
        reasons = []
        if not (reader.get(cid) or {}).get("agreed"):
            reasons.append("reader did not agree" if cid in reader else "not read")
        if b["tier"] == "H":
            ch = checks.get(cid) or {}
            if not ch.get("thorough_finds_all"):
                reasons.append("thorough route misses a target" if ch else "not checked")
        if cid in FLAWED:
            reasons.append(FLAWED[cid])
        (why_not if reasons else valid)[cid] = reasons or b
    # The covers, by the kind of record and whether the request names its container: which reached a valid easy and a
    # valid hard test. Kinds with no route table (method.md: four services, their main record kinds) get the easy
    # tier only.
    by_kind = defaultdict(lambda: {"plural-worthy covers": set(), "with a valid easy test": set(),
                                   "with a valid hard test": set()})
    for r in build.values():
        if "cases" not in r or not (writer.get(r["cover"]) or {}).get("plural_worthy"):
            continue
        k = by_kind[f"{r['table']}, {'container named' if r['pinned'] else 'no container named'}"]
        k["plural-worthy covers"].add(r["cover"])
        for tier, c in r["cases"].items():
            if c.get("id") in valid:
                k[f"with a valid {'easy' if tier[0] == 'E' else 'hard'} test"].add(r["cover"])
    kinds = defaultdict(lambda: {"shortcuts": set(), "defeated": set(), "tests": 0})
    for cid, b in valid.items():
        if b["tier"] != "H" or cid not in checks:
            continue
        k = kinds[checks[cid]["table"]]
        k["tests"] += 1
        k["shortcuts"] |= set(checks[cid]["defeated"]) | set(checks[cid]["not_defeated"])
        k["defeated"] |= set(checks[cid]["defeated"])
    trials = [t for t in grades["trials"] if t["trial"].split("/")[1] in valid]
    missed = Counter()
    distinct_miss, distinct_fact, timeouts = set(), set(), 0
    placements = load("placements.json", {})
    found_by_place = defaultdict(Counter)
    timeouts_done = 0
    for t in trials:
        if t["diligence"] == "timeout":
            timeouts += 1
            timeouts_done += not t["missing"]
            continue
        for tgt, place in (placements.get(t["trial"].split("/")[1]) or {}).items():
            found_by_place[place]["placed"] += 1
            found_by_place[place]["found"] += tgt not in t["missing"]
        for tgt, place in t["missing"].items():
            missed[(t["domain"], place)] += 1
            distinct_miss.add((t["cover"], place))
        for d, fact in t["decoys_acted"].items():
            distinct_fact.add((t["cover"], fact))
    reviewed = [v for v in review.values() if v.get("verdict") in ("TP", "FP")]
    sample = [v for v in review.values() if v.get("sample") == "pass"]
    muse = [json.loads(line) for line in (HERE / "runs" / "calls.jsonl").read_text().splitlines()] \
        if (HERE / "runs" / "calls.jsonl").exists() else []
    solver = Counter()
    for s in (HERE / "runs").glob("p3*/t*/SMA-*/attempt-*/execution_summary.json"):
        u = json.loads(s.read_text()).get("usage") or {}
        solver["input"] += u.get("input_tokens") or 0
        solver["output"] += u.get("output_tokens") or 0
        solver["attempts"] += 1
    out = {
        "covers": len(writer), "plural-worthy": sum(1 for a in writer.values() if a.get("plural_worthy")),
        "tests generated": {"all": len(built), "easy": sum(1 for b in built.values() if b["tier"] == "E"),
                            "hard": sum(1 for b in built.values() if b["tier"] == "H"),
                            "of them repaired versions": sum(1 for c in built if c.endswith("R")),
                            "of them iteration 2 (traps the first round lacked)": sum(1 for c in built
                                                                                      if c.endswith("HP"))},
        "valid": {"all": len(valid), "easy": sum(1 for b in valid.values() if b["tier"] == "E"),
                  "hard": sum(1 for b in valid.values() if b["tier"] == "H")},
        "not valid, by reason": dict(Counter(r for rs in why_not.values() for r in rs)),
        "covers by record kind": {k: {n: len(v) for n, v in d.items()} for k, d in
                                  sorted(by_kind.items(), key=lambda kv: -len(kv[1]["plural-worthy covers"]))},
        "coverage by request kind": {k: {"valid hard tests": v["tests"],
                                         "shortcuts defeated": f"{len(v['defeated'])} of {len(v['shortcuts'])}",
                                         "not defeated": {s: NOT_COVERED.get((k, s), "a construction gap")
                                                          for s in sorted(v["shortcuts"] - v["defeated"])}}
                                     for k, v in sorted(kinds.items())},
        "trials on valid tests": len(trials),
        "timeouts": timeouts,
        "timeouts with every target already changed (the answer cut off)": timeouts_done,
        "targets found by placement (valid tests, timeouts out)": {
            PLACE.get(p, p): f"{v['found']}/{v['placed']}" for p, v in sorted(found_by_place.items())},
        "targets missed (trials × targets), by service and placement": {f"{d} {p}": n for (d, p), n in
                                                                         sorted(missed.items())},
        "distinct (cover, placement) misses": len(distinct_miss),
        "distinct (cover, fact) near misses acted on": len(distinct_fact),
        "judge": {"reported failures reviewed": len(reviewed),
                  "true positives": sum(1 for v in reviewed if v["verdict"] == "TP"),
                  "false positives": sum(1 for v in reviewed if v["verdict"] == "FP"),
                  "passes sampled": len(sample),
                  "false negatives in the sample": sum(1 for v in sample if v.get("verdict") == "FN")},
        "muse": {"calls": len(muse), "input tokens": sum(r.get("input_tokens") or 0 for r in muse),
                 "cached input tokens": sum(r.get("cache_read_input_tokens") or 0 for r in muse),
                 "output tokens": sum(r.get("output_tokens") or 0 for r in muse),
                 "billed usd": round(sum(r.get("cost_usd_billed") or 0 for r in muse), 4),
                 "list usd": round(sum(r.get("cost_usd_list_price") or 0 for r in muse), 4)},
        "solver (self-hosted Qwen, no charge)": dict(solver),
    }
    (HERE / "summary.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
