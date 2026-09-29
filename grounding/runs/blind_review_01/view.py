"""Evidence-only review. No score, verdict, triage, reference-label or review-report imports."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
GROUNDING = HERE.parents[1]


def read(p):
    return json.loads(p.read_text())


def compact(x):
    return json.dumps(x, ensure_ascii=False, separators=(",", ":"))


def clean(x):
    """Display compression only: null fields omitted, all non-null values retained."""
    if isinstance(x, dict):
        return {k:clean(v) for k,v in x.items() if v is not None}
    if isinstance(x, list):
        return [clean(v) for v in x]
    if isinstance(x, str) and x.lstrip().startswith(('{','[')):
        try:
            return clean(json.loads(x))
        except (ValueError, TypeError):
            return x
    return x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--brief", action="store_true")
    ap.add_argument("--steps", help="Comma-separated one-based step positions; full observations")
    ap.add_argument("--seed", action="store_true")
    ap.add_argument("--packet", action="store_true", help="All API observations, compact JSON; shortened thinking; omit skill documentation responses")
    ap.add_argument("--overview", action="store_true", help="Commands, final, diff and construction references only; inspect selected steps separately")
    ap.add_argument("--no-thinking", action="store_true")
    args = ap.parse_args()
    manifest = read(HERE / "manifest.json")
    rows = {r["blind_id"]: r for r in manifest["sample"]}
    selected = {int(n) for n in args.steps.split(",")} if args.steps else None
    for bid in args.ids:
        m = rows[bid]
        at = GROUNDING / m["attempt"]
        for name, expected in m["source_hashes"].items():
            if expected:
                assert hashlib.sha256((GROUNDING / name).read_bytes()).hexdigest() == expected, name
        case = read(at / "case.json")
        solver = read(GROUNDING / m["solver_record"])
        summary = read(at / "execution_summary.json")
        print(f"\n===== {bid}: {m['domain']} / {m['form']} =====")
        print("REQUEST:", case["prompt"])
        print("ACTOR:", case.get("acting_user_id"))
        for i, ref in enumerate(case["references"]):
            fields = ("name","use","expected","claims","resolution","written") if args.packet or args.overview else ("name","use","description","expected","claims","resolution","written","query")
            ref_display = {k:ref.get(k) for k in fields}
            if args.overview:
                ref_display['claims'] = [{k:c.get(k) for k in ('requirement','witness','explanation')} for c in ref.get('claims', [])]
            print(f"REFERENCE /references/{i}:", compact(ref_display))
        if args.seed:
            print("FULL SEED:", compact(case.get("seed")))
            print("CARDS:", compact(case.get("cards")))
            print("TASK SPEC:", compact(case.get("task_spec")))
        print("TERMINATION:", solver.get("termination"), "STATUS:",summary.get("status"))
        for i, step in enumerate(solver.get("steps", [])):
            if selected and i+1 not in selected:
                continue
            thinking = step.get("thinking") or step.get("text") or ""
            if not thinking:
                thinking = " ".join(c.get("text", "") for c in (step.get("response") or {}).get("content", []) if c.get("type") == "text")
            action = step.get("action") or compact(step.get("arguments"))
            if args.overview:
                queries = []
                for literal in re.findall(r"'([^']*)'", str(action)):
                    try:
                        payload = json.loads(literal)
                    except ValueError:
                        continue
                    if isinstance(payload, dict) and isinstance(payload.get('query'), str):
                        queries.append(payload)
                if queries:
                    action = ' | '.join(compact(q) for q in queries)
                    if all('__type' in q['query'] or '__schema' in q['query'] for q in queries):
                        action = '[GraphQL schema introspection; full command retained in source]'
                else:
                    action = re.sub(r''' -H (?:'[^']*'|"[^"]*")''', '', str(action))
            print(f"STEP {i+1} (/steps/{i}):", action)
            if thinking and not args.overview and not args.no_thinking:
                if args.packet and len(str(thinking)) > 700 and not selected:
                    print("REASONING:", str(thinking)[:350] + " [middle omitted; use --steps for full text] " + str(thinking)[-350:])
                else:
                    print("REASONING:", str(thinking)[:600] + (" [abridged]" if len(str(thinking)) > 600 else "") if args.brief and not selected else thinking)
            if (not args.brief or selected) and not args.overview:
                command = str(step.get("action") or step.get("arguments"))
                documentation = bool(re.match(r"^(cat|sed|head|read) ", command)) and ("SKILL.md" in command or "/references/" in command)
                if args.packet and documentation and not selected:
                    print("OBSERVATION: [skill documentation omitted; inspect --steps if material]")
                else:
                    print("OBSERVATION (null fields omitted):" if args.packet else "OBSERVATION:", compact(clean(step.get("observation")) if args.packet else step.get("observation")))
        final = at / "solver/final_response.md"
        print("FINAL:", final.read_text() if final.exists() else solver.get("final"))
        dp = at / "environment/diff_run.json"
        if dp.exists():
            diff = read(dp).get("diff", {})
            for cat, vals in diff.items():
                for i, item in enumerate(vals) if isinstance(vals, list) else []:
                    if (args.packet or args.overview) and cat == "inserts" and item.get("__table__") == "calendar_sync_tokens":
                        continue
                    if cat == "updates":
                        before, after = item.get("before", {}), item.get("after", {})
                        changed = {k: [before.get(k), after.get(k)] for k in sorted(set(before)|set(after)) if before.get(k) != after.get(k)}
                        print(f"DIFF /diff/{cat}/{i}:", compact({"table": item.get("__table__"), "after_id": {k:v for k,v in after.items() if k=='id' or k.endswith('_id')}, "changed": changed}))
                    else:
                        print(f"DIFF /diff/{cat}/{i}:", compact(item))
            if not any(diff.values()):
                print("DIFF: no changes")
            elif args.packet or args.overview:
                count = sum(v.get("__table__") == "calendar_sync_tokens" for v in diff.get("inserts", []))
                if count:
                    print("AUTOMATIC READ SIDE EFFECTS:", count, "calendar_sync_tokens inserts (full raw diff retained)")
        else:
            print("DIFF: missing")


if __name__ == "__main__":
    main()
