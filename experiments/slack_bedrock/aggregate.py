"""Combine scored batches, verifying full Slack coverage and provenance."""
import argparse
import json
from pathlib import Path

from run import ROOT, RATES, cost, save


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--overhead", action="append", default=[], type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replace-infrastructure-errors", action="store_true")
    args = parser.parse_args()
    rows = [json.loads(line) for line in (ROOT / "datasets/agent-diff-bench/all_numbered.jsonl").read_text().splitlines()]
    expected = {r["test_id"]: r for r in rows if r["service"] == "slack"}
    results = {}
    replaced = []
    configs, prompts = [], []
    for folder in args.runs:
        configs.append(json.loads((folder / "config.json").read_text()))
        prompts.append((folder / "system_prompt.txt").read_bytes())
        for path in folder.glob("slack_*.json"):
            result = json.loads(path.read_text())
            key = result["test_id"]
            if key in results:
                previous = results[key]
                known_error = "messages: text content blocks must be non-empty"
                if not (args.replace_infrastructure_errors
                        and previous.get("termination") == "error"
                        and known_error in previous.get("error", "")):
                    raise ValueError(f"Duplicate scored task without eligible infrastructure error: {key}")
                replaced.append(previous)
            if "evaluation" not in result:
                raise ValueError(f"Missing evaluation: {key}")
            result["artifact"] = str(path.resolve())
            results[key] = result
    if set(results) != set(expected):
        raise ValueError(f"Coverage mismatch: missing={set(expected) - set(results)}, extra={set(results) - set(expected)}")
    for key in ["model", "docs_mode", "trials", "turn_limit", "timeout_seconds",
                "max_output_tokens_per_call", "temperature", "effort", "prompt_caching",
                "rates_usd_per_million", "git_commit", "dataset_sha256"]:
        if any(config[key] != configs[0][key] for config in configs):
            raise ValueError(f"Protocol mismatch: {key}")
    if any(prompt != prompts[0] for prompt in prompts):
        raise ValueError("System prompts differ")
    ordered = [results[key] for key in expected]
    tokens = {key: sum(r["usage"].get(key, 0) for r in ordered) for key in RATES}
    overhead_tokens = {key: 0 for key in RATES}
    for result in replaced:
        for key in RATES:
            overhead_tokens[key] += result["usage"].get(key, 0)
    for folder in args.overhead:
        summary = json.loads((folder / "summary.json").read_text())
        for key in RATES:
            overhead_tokens[key] += summary["tokens"][key]
    passed = sum(r["evaluation"]["passed"] for r in ordered)
    satisfied = sum(r["evaluation"]["score"]["passed"] for r in ordered)
    total = sum(len(json.loads(row["answer"])["assertions"]) for row in expected.values())
    assert total == sum(r["evaluation"]["score"]["total"] for r in ordered)
    report = {
        "model": configs[0]["model"], "docs_mode": "relevant", "concurrency": 10,
        "scored_runs": [str(p.resolve()) for p in args.runs],
        "overhead_runs": [str(p.resolve()) for p in args.overhead],
        "replaced_infrastructure_attempts": [{"test_id": r["test_id"], "artifact": r["artifact"],
                                              "cost_usd": r["cost_usd"], "error": r["error"]}
                                             for r in replaced],
        "tasks": len(ordered), "passed_tasks": passed, "pass_rate_percent": 100 * passed / len(ordered),
        "passed_assertions": satisfied, "total_assertions": total,
        "assertion_weighted_score_percent": 100 * satisfied / total,
        "tokens": tokens, "cost_usd": cost(tokens),
        "overhead_cost_usd": cost(overhead_tokens),
        "total_cost_including_overhead_usd": cost(tokens) + cost(overhead_tokens),
        "rates_usd_per_million": RATES,
        "model_calls": sum(r["usage"]["successful_requests"] for r in ordered),
        "mean_input_tokens_per_task": sum(tokens[k] for k in tokens if k != "output_tokens") / len(ordered),
        "mean_output_tokens_per_task": tokens["output_tokens"] / len(ordered),
        "results": [{"test_id": r["test_id"], "test_name": r["test_name"],
                     "passed": r["evaluation"]["passed"], "score": r["evaluation"]["score"],
                     "failures": r["evaluation"]["failures"], "termination": r["termination"],
                     "turns": len(r["steps"]), "cost_usd": r["cost_usd"],
                     "artifact": r["artifact"]} for r in ordered],
    }
    args.output.mkdir(parents=True, exist_ok=True)
    save(args.output / "summary.json", report)
    markdown = f"""# Full Slack benchmark: Sonnet 5, relevant docs

- Task pass rate: **{passed}/{len(ordered)} ({report['pass_rate_percent']:.2f}%)**.
- Assertion-weighted score: **{satisfied}/{total} ({report['assertion_weighted_score_percent']:.2f}%)**.
- Scored inference cost: **${cost(tokens):.6f}**.
- Infrastructure-error overhead: **${cost(overhead_tokens):.6f}**.
- Total including that overhead: **${report['total_cost_including_overhead_usd']:.6f}**.

One scored trial per task, ten concurrent workers, fresh database environments,
the authors' relevant-docs system prompt and XML ReAct interface, 40 turns / eight
minutes per episode, provider-default effort and temperature, and five-minute
explicit caching. Previously completed tasks were reused, not rerun. All scored
batch configurations and system prompts were checked for consistency.
Episodes stopped by a known Bedrock history-serialization error were rerun from
fresh environments; their earlier attempts contribute to overhead only. Completed
task failures were not retried to improve scores.

Scores are from the repository evaluator against unchanged dataset assertions.
Costs use reported token usage at the requested higher list rates, not a retrieved
AWS invoice; infrastructure charges are excluded. The first ten scored tasks
reused provider cache prefixes from the earlier interrupted batch, whose cost is
included separately above.

## Token accounting

| Category | Tokens | USD per million | Cost |
|---|---:|---:|---:|
"""
    for key, count in tokens.items():
        markdown += f"| {key} | {count:,} | ${RATES[key]:.2f} | ${count * RATES[key] / 1e6:.6f} |\n"
    markdown += "\n## Task results\n\n| Test | Pass | Assertions | Turns | Cost |\n|---|---|---:|---:|---:|\n"
    for result in report["results"]:
        score = result["score"]
        markdown += f"| {result['test_id']} | {'PASS' if result['passed'] else 'FAIL'} | {score['passed']}/{score['total']} | {result['turns']} | ${result['cost_usd']:.6f} |\n"
    markdown += "\n## Failed assertions\n"
    for result in report["results"]:
        if not result["passed"]:
            markdown += f"\n### {result['test_id']}: {result['test_name']}\n\n"
            markdown += "\n".join("- " + str(failure) for failure in result["failures"]) + "\n"
    (args.output / "REPORT.md").write_text(markdown)
    print(json.dumps({k: v for k, v in report.items() if k != "results"}, indent=2))


if __name__ == "__main__":
    main()
