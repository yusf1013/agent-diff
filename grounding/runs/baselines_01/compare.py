"""Assemble the numbers of the report from the study's records (no model calls).

    python3 grounding/runs/baselines_01/compare.py      # writes compare.json and prints it

Per approach at the same budget (48 tests, 12 per domain): what the tests are (structure), what they expose on
OpenClaw with the self-hosted Qwen (3 trials), what their own oracle reports, and what they cost. Our side is the
expected value over random draws of 12 of our Phase 4 tests per domain (ours.json). Cycle 2's ablations are tallied
from its labels.
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
MISTAKE = {"incorrect", "presented"}
VOID = {"artifact", "not_established"}


def load(path: Path):
    return json.loads(path.read_text()) if path.exists() else None


def cost(path: Path) -> dict:
    rows = [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []
    return {"calls": len(rows), "list_usd": round(sum(r.get("cost_usd_list_price") or 0 for r in rows), 3),
            "billed_usd": round(sum(r.get("cost_usd_billed") or 0 for r in rows), 4)}


def structure(review: list) -> dict:
    fams = Counter(n["family"] for r in review for n in r["near_misses"])
    designated = sum(v for k, v in fams.items() if k != "F0")
    valid = [r for r in review if r["valid"]]
    return {"tests": len(review), "forms": dict(Counter(r["form"] for r in review)),
            "near_misses": sum(fams.values()), "near_misses_designated": designated,
            "families": dict(sorted(fams.items())),
            "facts_exercised": len({f for r in review for f in r["facts_exercised"] if not f.startswith("(")}),
            "facts_exercised_properly": len({f for r in valid for f in r["proper"]}),
            "invalid_before_runs": sum(1 for r in review if not r["valid"])}


def summary(gen: Path) -> dict:
    out = subprocess.run([sys.executable, str(HERE / "summarize_labels.py"), str(gen / "labels.json"),
                          str(gen / "review.json")], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def ablations() -> dict:
    labels = {k: v for k, v in load(HERE / "cycle2" / "labels.json").items() if not k.startswith("_")}
    by = defaultdict(list)
    for key, label in labels.items():
        by[key.split("/")[2]].append(label)

    def tally(cases):
        fails = sum(1 for c in cases for l in by[c] if l["outcome"] in MISTAKE)
        usable = sum(1 for c in cases for l in by[c] if l["outcome"] not in VOID)
        tests = sum(1 for c in cases if any(l["outcome"] in MISTAKE for l in by[c]))
        facts = sorted({f for c in cases for l in by[c] for f in l.get("exposed", [])})
        return {"failing_trials": fails, "usable_trials": usable, "tests_failing": tests, "tests": len(cases),
                "facts_exposed": facts}

    n0 = sorted(c for c in by if c.startswith("N0-"))
    alt = sorted(c for c in by if c.startswith("P-") and not c.endswith("-PL"))
    confounded = {"P-G4-BOX-01-I11", "P-G4-BOX-01-I12"}
    return {"form_n0_in_probe_form": tally(n0),
            "content_alt": tally(alt), "content_plain": tally([c + "-PL" for c in alt]),
            "content_alt_unconfounded": tally([c for c in alt if c not in confounded]),
            "content_plain_unconfounded": tally([c + "-PL" for c in alt if c not in confounded]),
            "confounded_pairs": sorted(confounded)}


def main():
    ours = load(HERE / "ours.json")
    phase4 = ours["phase4_muse"]
    per12 = lambda key: round(sum(d["per_12_tests"][key] for d in phase4.values()), 1)  # noqa: E731
    result = {"budget": "48 tests, 12 per domain", "approaches": {}}
    for name, gen in (("N0", HERE / "n0/runs/gen_01"), ("N1", HERE / "n1/runs/gen_01")):
        entry = {"structure": structure(load(gen / "review.json")),
                 "generation_cost": cost(gen / "calls.jsonl")}
        if (gen / "labels.json").exists():
            entry["exposure"] = summary(gen)
        if (gen / "oracles.score.json").exists():
            entry["own_oracles"] = {k: v["cells"] for k, v in load(gen / "oracles.score.json").items()}
        result["approaches"][name] = entry
    gen_cost = ours["phase4_generation_cost"]
    result["approaches"]["ours_phase4_per_48"] = {
        "structure": {"facts_exercised": per12("exercised"), "facts_with_a_near_miss": per12("near_miss_any_family"),
                      "facts_exercised_properly": per12("proper")},
        "exposure": {"tests_failing": per12("tests_exposing"), "facts_exposed_detect3": per12("exposed3"),
                     "facts_exposed_detect1": per12("exposed1"), "note": "no presupposing test in the regular suite"},
        "generation_cost": {"list_usd_per_test": gen_cost["list_per_test"], "billed_usd_per_test":
                            gen_cost["billed_per_test"], "list_usd_per_48": round(48 * gen_cost["list_per_test"], 2)}}
    result["ablations"] = ablations()
    (HERE / "compare.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
