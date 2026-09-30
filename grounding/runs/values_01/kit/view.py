"""Evidence for reading an execution by hand: the request, the construction's references (hypotheses), the steps,
the final reply, the diff, and this study's flags. No grounding outcome, judge verdict or note is read or shown.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.view KEY [KEY ...] [--steps 3,5] [--full]

Adapted from blind_review_01/view.py.
"""
from __future__ import annotations

import argparse
import json
import re

from grounding.runs.values_01.kit.common import case, diff, executions, read, reply, transcript


def compact(x) -> str:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":"), default=str)


def short(s, n: int) -> str:
    s = str(s or "")
    return s if len(s) <= n else s[:n // 2] + f" [... {len(s) - n} chars ...] " + s[-n // 2:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keys", nargs="+")
    ap.add_argument("--steps", help="one-based step numbers shown in full")
    ap.add_argument("--full", action="store_true", help="every step in full")
    ap.add_argument("--obs", type=int, default=500, help="characters of each observation")
    ap.add_argument("--writes", action="store_true", help="only the steps that issue a write, in full")
    args = ap.parse_args()
    rows = {e["key"]: e for e in executions()}
    flags = {name: read(name) for name in ("values", "writes", "reply")}
    chosen = {int(n) for n in args.steps.split(",")} if args.steps else set()
    from grounding.runs.values_01.kit.writes import writes_of
    for key in args.keys:
        ex = rows[key]
        c = case(ex)
        print(f"\n===== {key}  ({ex['domain']} / {ex['form']}; timeout: {ex['timeout']}) =====")
        print("REQUEST:", c["prompt"])
        print("ACTOR:", c.get("acting_user_id"))
        for i, ref in enumerate(c["references"]):
            print(f"REFERENCE {i}:", compact({"use": ref.get("use"), "table": ref["query"]["table"],
                                              "expected": ref.get("expected"), "written": ref.get("written"),
                                              "claims": [{k: cl.get(k) for k in ("requirement", "witness", "explanation")}
                                                         for cl in ref.get("claims", [])]}))
        write_steps = {w["step"] + 1 for w in writes_of(ex)} if args.writes else set()
        for i, s in enumerate(transcript(ex).get("steps", [])):
            n = i + 1
            if args.writes and n not in write_steps and n not in chosen:
                continue
            full = args.full or n in chosen or n in write_steps
            action = s.get("action") or compact(s.get("arguments"))
            action = re.sub(r''' -H (?:'[^']*'|"[^"]*")''', "", str(action))
            print(f"STEP {n}:", action if full else short(action, 900))
            think = s.get("thinking") or ""
            if think:
                print("  THINKING:", think if full else short(think, 400))
            obs = s.get("observation")
            if obs is not None:
                print("  OBS:", compact(obs) if full else short(compact(obs), args.obs))
        print("FINAL REPLY:", reply(ex))
        d = diff(ex)
        for kind in ("inserts", "updates", "deletes"):
            for i, item in enumerate(d.get(kind, [])):
                if item.get("__table__") == "calendar_sync_tokens":
                    continue
                if kind == "updates":
                    b, a = item.get("before") or {}, item.get("after") or {}
                    changed = {k: [b.get(k), a.get(k)] for k in sorted(set(a) | set(b)) if b.get(k) != a.get(k)}
                    ids = {k: v for k, v in a.items() if k == "id" or k.endswith("_id")}
                    print(f"DIFF {kind}/{i}:", compact({"table": item.get("__table__"), "ids": ids, "changed": changed}))
                else:
                    print(f"DIFF {kind}/{i}:", compact(item))
        v, w, r = (flags[n].get(key, {}) for n in ("values", "writes", "reply"))
        print("FLAGS values:", compact({k: v.get(k) for k in ("values", "other_fields", "other_records", "other_tables",
                                                             "no_net_change", "replica_effects") if v.get(k)}))
        print("FLAGS writes:", compact({k: w.get(k) for k in ("rejected", "not_in_diff", "inverse_ops", "unresolved")
                                        if w.get(k)}))
        print("FLAGS reply:", compact({k: r.get(k) for k in ("stance", "flags", "no_reply") if r.get(k)}))


if __name__ == "__main__":
    main()
