"""Audit self-hosted Qwen/OpenClaw usage for report_01, without model calls.

Run from the repository root: python -m grounding.runs.report_01.kit.qwen_usage
Reads each original proxy metadata record once (archives or unpacked records),
including unsuccessful requests, and reconciles against execution summaries.
The baseline root can point at its worktree before that branch is merged.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import tarfile

RUNS = Path(__file__).resolve().parents[2]
BASELINES = (
    "n0/runs/gen_01/solve_01", "n1/runs/gen_01/solve_01",
    "twin2/n0m/runs/gen_01/solve_01", "twin2/n1m/runs/gen_01/solve_01",
    "cycle2/solve_01", "plain48/solve_01",
)
APART = ("full_01", "smoke_01", "smoke_02", "smoke_03")
FIELDS = (
    "requests", "upstream_attempts", "input_tokens", "output_tokens",
    "reasoning_tokens", "cached_input_tokens", "cache_creation_input_tokens",
    "requests_without_usage", "requests_without_cache_read_details",
    "requests_without_cache_creation_details", "non_200",
)


def load(path):
    return json.loads(path.read_text())


def metadata(attempt):
    archive = attempt / "solver/requests.tar.xz"
    loose = attempt / "solver/requests"
    if archive.exists():
        assert not list(loose.glob("*.meta.json")), f"Two metadata sources: {attempt}"
        with tarfile.open(archive, "r|xz") as stream:
            for member in stream:
                if member.isfile() and member.name.endswith(".meta.json"):
                    yield json.load(stream.extractfile(member))
    else:
        for path in sorted(loose.glob("*.meta.json")):
            yield load(path)


def audit_attempt(attempt):
    summary = load(attempt / "execution_summary.json")
    assert summary.get("harness") == "openclaw", attempt
    assert summary.get("backend") == "selfhost", attempt
    config = attempt / "solver/config.json"
    if config.exists():
        assert load(config)["model"]["primary"] == "selfhost/qwen3.8-27b", attempt
    totals = Counter({key: 0 for key in FIELDS})
    for meta in metadata(attempt):
        totals["requests"] += 1
        totals["upstream_attempts"] += len(meta.get("attempts", []))
        totals["non_200"] += meta.get("final_status") != 200
        usage = meta.get("usage")
        if not usage:
            totals["requests_without_usage"] += 1
            continue
        totals["input_tokens"] += usage.get("prompt_tokens", 0) or 0
        totals["output_tokens"] += usage.get("completion_tokens", 0) or 0
        totals["reasoning_tokens"] += (usage.get("completion_tokens_details") or {}).get("reasoning_tokens", 0) or 0
        details = usage.get("prompt_tokens_details") or {}
        for source, target, missing in (
            ("cached_tokens", "cached_input_tokens", "requests_without_cache_read_details"),
            ("created_cache_tokens", "cache_creation_input_tokens", "requests_without_cache_creation_details"),
        ):
            if details.get(source) is None:
                totals[missing] += 1
            else:
                totals[target] += details[source]
    saved = summary.get("usage") or {}
    differences = {key: {"summary": saved.get(key, 0), "metadata": totals[key]}
                   for key in ("requests", "input_tokens", "output_tokens", "requests_without_usage")
                   if saved.get(key, 0) != totals[key]}
    totals["attempts_without_summary_usage"] = int(not bool(saved))
    totals["attempts_without_request_metadata"] = int(totals["requests"] == 0)
    totals["trial_attempts"] = 1
    return totals, differences


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baselines-root", type=Path, default=RUNS / "baselines_01")
    args = parser.parse_args()
    oc = RUNS / "openclaw_eval_01/runs"
    sources = [("regular", f"openclaw_eval_01/runs/{name}", oc / name)
               for name in ("full_02", "full_03", "full_04")]
    sources += [("policy", f"openclaw_eval_01/runs/policy/{p.name}", p)
                for p in sorted((oc / "policy").glob("solve_*"))]
    sources += [("baseline_ablation", f"baselines_01/{name}", args.baselines_root / name)
                for name in BASELINES]
    sources += [("stopped_and_smoke", f"openclaw_eval_01/runs/{name}", oc / name) for name in APART]
    per_run, groups, differences = {}, {}, {}
    for group, name, folder in sources:
        assert folder.is_dir(), folder
        attempts = sorted(folder.glob("t*/*/attempt-*"))
        assert attempts, folder
        totals = Counter()
        with ThreadPoolExecutor(max_workers=8) as pool:
            for attempt, (counts, delta) in zip(attempts, pool.map(audit_attempt, attempts)):
                totals.update(counts)
                if delta:
                    differences[f"{name}/{attempt.relative_to(folder)}"] = delta
        totals["trials"] = len({a.parent for a in attempts})
        totals["total_tokens"] = totals["input_tokens"] + totals["output_tokens"]
        per_run[name] = {"group": group, **totals}
        groups.setdefault(group, Counter()).update(totals)
        print(name, totals["input_tokens"], totals["output_tokens"], flush=True)
    main_total = groups["regular"] + groups["policy"]
    reported = main_total + groups["baseline_ablation"]
    out = {
        "scope": "Self-hosted Qwen3.8-27B through OpenClaw only; report_01 main and RQ8 result runs, with stopped/smoke runs separate.",
        "source": "Provider usage in solver/requests.tar.xz or solver/requests/*.meta.json; all recorded attempts, each counted once.",
        "interpretation": [
            "Input counts repeated prompt/context tokens on each model request; cached input is a subset, not an addition.",
            "Output includes reasoning; reasoning tokens are a subset, not an addition.",
            "Missing usage is unknown, not zero consumption; totals are recorded lower bounds, not GPU-compute estimates.",
            "Cache-read and cache-creation details are provider-reported; missing detail fields are counted explicitly.",
            "Generation/judging models and every toy-harness run (including self-hosted step 5) are excluded.",
            "Reused trials in judge comparisons and ablations are not counted a second time; fresh reruns are counted.",
        ],
        "runs": per_run, "groups": groups,
        "opening_table_scope": main_total,
        "all_reported_result_runs": reported,
        "including_stopped_and_smoke": reported + groups["stopped_and_smoke"],
        "summary_metadata_differences": differences,
    }
    path = RUNS / "report_01/numbers/qwen_usage.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({key: out[key] for key in ("opening_table_scope", "all_reported_result_runs", "including_stopped_and_smoke")}, indent=2))
    print(f"Summary differences: {len(differences)}; saved {path}")


if __name__ == "__main__":
    main()
