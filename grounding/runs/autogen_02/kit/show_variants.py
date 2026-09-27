"""Print the automated variants of a variants2 output folder for review: status, the writer's answers per round, the
code and reader findings, the original request, and the cost.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.show_variants DIR [--manual]

`--manual` also prints my Phase 1 request (drop-F) or clone for the same fact or scenario, for the comparison of the
automated variants with the hand-made ones. (Only I read this; it never reaches an agent.)
"""
import argparse
import json
from pathlib import Path

STUDY = Path(__file__).resolve().parents[1]


def cost(folder: Path) -> tuple[float, float, float]:
    lst = billed = secs = 0.0
    for p in folder.rglob("*.result.json"):
        r = json.loads(p.read_text())
        lst += r.get("total_cost_usd") or 0
        billed += r.get("cost_usd_billed") or 0
    return lst, billed, secs


def review(folder: Path, scenarios: list[str] | None):
    """For my review before a run: per accepted variant, the scenario's request, the variant's request, and every
    candidate record with the scenario's note on it (bundle.candidates)."""
    from grounding.runs.autogen_01.kit import bundle
    from grounding.runs.autogen_02.kit.variants2 import source_cases
    originals = {c["case_id"]: c["prompt"] for src in ("population", "phase4") for c in source_cases(src)}
    for record_path in sorted(folder.glob("*/record.json")):
        r = json.loads(record_path.read_text())
        if r["status"] != "accepted" or (scenarios and r["scenario"] not in scenarios):
            continue
        case = json.loads((record_path.parent / "variant.json").read_text())
        cand, _ = bundle.candidates(case)
        cand = "\n".join(line[:260] for line in cand.splitlines())
        print(f"\n{'#' * 80}\n=== {r['id']} (matches {r.get('matches')}, near misses left {r.get('other_near_misses')})"
              f"\nORIGINAL: {originals.get(r['scenario'])}\nVARIANT:  {case['prompt']}\n{cand}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=Path)
    parser.add_argument("--manual", action="store_true")
    parser.add_argument("--status", nargs="+")
    parser.add_argument("--review", action="store_true",
                        help="accepted variants only: the original and the variant request, then every candidate")
    parser.add_argument("--scenarios", nargs="+", help="with --review: only these scenarios")
    args = parser.parse_args()
    if args.review:
        review(args.dir, args.scenarios)
        return
    manual_dropf, manual_clone = {}, {}
    if args.manual:
        for v in json.loads((STUDY / "phase1_dropf.json").read_text())["variants"]:
            manual_dropf[(v["scenario"], v["fact"])] = v.get("prompt") or f"NOT DERIVABLE: {v.get('not_derivable')}"
        for v in json.loads((STUDY / "phase1_clones.json").read_text())["clones"]:
            manual_clone[v["scenario"]] = v
    from grounding.runs.autogen_02.kit.variants2 import source_cases
    originals = {}
    for record_path in sorted(args.dir.glob("*/record.json")):
        r = json.loads(record_path.read_text())
        if args.status and r["status"] not in args.status:
            continue
        if not originals:
            originals = {c["case_id"]: c["prompt"] for src in ("exemplars", "population", "phase4")
                         for c in source_cases(src)}
        lst, billed, _ = cost(record_path.parent)
        print(f"\n=== {r['id']} [{r['status']}] facts={r.get('dropped_facts', '')} matches={r.get('matches', '')} "
              f"others={r.get('other_near_misses', '')} cost list ${lst:.3f} billed ${billed:.4f}")
        print(f"ORIGINAL: {originals.get(r['scenario'])}")
        for entry in r.get("rounds", []):
            w = entry.get("writer", {})
            if "request" in w:
                print(f"  round {entry['round']} writer: possible={w.get('possible')} REQUEST: {w.get('request')}")
                print(f"    removed: {w.get('removed_words')} | {w.get('reason')}")
            else:
                print(f"  round {entry['round']} writer: possible={w.get('possible')} key={w.get('new_key')} "
                      f"changes={json.dumps(w.get('changes'), ensure_ascii=False)} skip={w.get('skip_children')} | "
                      f"{w.get('reason')}")
            for f in entry.get("findings", []):
                print(f"    FINDING: {f}")
        if r["status"] == "not_derivable":
            print(f"  code: {r.get('problems')}")
        if args.manual:
            if r["id"].startswith("UC-"):
                print(f"  MANUAL: {json.dumps(manual_clone.get(r['scenario']), ensure_ascii=False)}")
            else:
                print(f"  MANUAL: {manual_dropf.get((r['scenario'], r['fact']))}")


if __name__ == "__main__":
    main()
