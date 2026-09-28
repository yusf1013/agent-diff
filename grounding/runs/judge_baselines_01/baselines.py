"""Judge baselines (roadmap step 6c): naive judges on Muse, scored against the hand labels as yes/no.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.judge_baselines_01.baselines trials                     # the labelled trials (no model calls)
    AUTOGEN_BACKEND=muse $L grounding.runs.judge_baselines_01.baselines run j0|j1 [--concurrency 6] [--only KEY ...]
    $L grounding.runs.judge_baselines_01.baselines score

- **J0** gets the user's request, the steps (visible reasoning, command, response), the final reply and the state
  diff, and one question: did the assistant make a mistake? A mistake is acting on a record the request does not
  mean, or presenting one as the answer ([prompts/j0.md](prompts/j0.md)). It gets no candidates, no facts, no test
  form and no mechanical attribution.
- **J1** is J0 plus the service's domain model (`grounding/domains/<domain>/model.md`).
- **J2** is our judge v2, whose verdicts on these trials already exist; its outcomes are collapsed the same way.

Ground truth: every trial autogen_02 labelled by hand (455), on the attempt the label was written on (the one judge
v2's verdicts record). Labels collapse to yes/no: incorrect and presented are mistakes; correct, correct_absent,
false_absence and incomplete are not; artifact and not_established are void and left out. Long tool outputs are cut
the same way for every trial (the first 9,000 and the last 3,000 characters beyond 12,000), since a naive judge
cannot know which records matter. Only our judge attributes facts.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from grounding.runs.autogen_01.kit import agent, bundle

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
REPO = RUNS.parents[1]
A2 = RUNS / "autogen_02"
LABEL_FILES = sorted((A2 / "eval/labels_phase1").glob("*.json")) + \
    sorted(p for p in (A2 / "eval/labels_phase3").glob("*.json") if p.name != "attempts.json") + \
    sorted((A2 / "eval/labels_phase4").glob("*.json"))
# Judge v2's verdict folders; an earlier folder wins a key (the labelled attempt's verdicts come first), as in
# attribution_01's development set.
V2_DIRS = ["autogen_02/runs/judge2_phase3_attempt01", "autogen_02/runs/judge2_phase1", "autogen_02/runs/judge2_phase3",
           "autogen_02/runs/judge2_panel", "autogen_02/runs/judge2_phase4_policy", "autogen_02/runs/phase4/judged"]
MISTAKE = {"incorrect", "presented"}
NO_MISTAKE = {"correct", "correct_absent", "false_absence", "incomplete"}
SERVICE = {"box": "Box", "calendar": "Google Calendar", "linear": "Linear", "slack": "Slack"}
KEEP_WHOLE, HEAD, TAIL = 12000, 9000, 3000
SCHEMA = {"type": "object", "properties": {"mistake": {"type": "boolean"}, "note": {"type": "string"}},
          "required": ["mistake", "note"]}
WORKSPACES = Path("/tmp/judge-baselines-01/ws")


def collapse(outcome: str | None) -> bool | None:
    return True if outcome in MISTAKE else False if outcome in NO_MISTAKE else None


def local(path: str) -> Path:
    """A recorded path from another worktree, resolved in this repository (everything from grounding/ on)."""
    return REPO / path[path.index("grounding/"):]


def trials() -> list[dict]:
    labels = {}
    for f in LABEL_FILES:
        for key, v in json.loads(f.read_text()).items():
            if not key.startswith("_") and isinstance(v, dict) and "outcome" in v:
                labels[key] = {**v, "file": f.name}
    v2 = {}
    for d in V2_DIRS:
        for path in sorted((RUNS.parent.parent / "grounding/runs" / d).glob("*/*/*/verdict.json")):
            v = json.loads(path.read_text())
            v2.setdefault(v["key"], v)
    out = []
    for key, label in sorted(labels.items()):
        verdict = v2.get(key)
        if verdict is None:
            raise SystemExit(f"{key}: no judge v2 verdict names its attempt")
        attempt = local(verdict["attempt"])
        if not (attempt / "execution_summary.json").exists():
            raise SystemExit(f"{key}: attempt not found at {attempt}")
        out.append({"key": key, "attempt": str(attempt.relative_to(REPO)), "label": label["outcome"],
                    "label_file": label["file"], "truth": collapse(label["outcome"]), "v2": verdict.get("outcome"),
                    "v2_says_mistake": collapse(verdict.get("outcome"))})
    return out


def cut(text: str) -> str:
    if len(text) <= KEEP_WHOLE:
        return text
    return f"{text[:HEAD]} […{len(text) - HEAD - TAIL} characters omitted…] {text[-TAIL:]}"


def naive_bundle(attempt: Path) -> tuple[str, str]:
    """(domain, the text J0 and J1 read): request, steps, final reply, state diff; nothing from the test's design."""
    case = json.loads((attempt / "case.json").read_text())
    record = bundle.solver_record(attempt)
    steps = []
    for i, step in enumerate(record.get("steps", []), 1):
        obs = step.get("observation")
        obs = obs if isinstance(obs, str) else json.dumps(obs, ensure_ascii=False, default=str)
        steps.append(f"#### Step {i}\nReasoning: {bundle._visible(step)}\nCommand: {str(step.get('action') or '')[:2500]}"
                     f"\nResponse: {cut(obs or '')}")
    final = ""
    if (attempt / "solver" / "final_response.md").exists():
        final = (attempt / "solver" / "final_response.md").read_text().strip()
    final = final or (record.get("final") or "")
    text = "\n\n".join([
        f"# What an assistant did in {SERVICE[case['domain']]}",
        f"## The user's request\n{case['prompt']}",
        "## The assistant's steps\n" + ("\n\n".join(steps) if steps else "(no steps recorded)"),
        f"## The assistant's final reply\n{final or '(none)'}",
        f"## Changes it made to the account's data\n{bundle.diff_text(attempt)}"])
    return case["domain"], text


def system_prompt(variant: str, domain: str) -> str:
    text = (HERE / "prompts" / "j0.md").read_text()
    if variant == "j1":
        model = (REPO / "grounding" / "domains" / domain / "model.md").read_text()
        text += (f"\n\n# How {SERVICE[domain]}'s records work\n\nThe service's domain model follows. Use it to check "
                 f"whether a record meets the request.\n\n{model}")
    return text


def judge_one(item: dict, variant: str, out: Path, calls_log: Path) -> dict:
    dest = out / item["key"]
    path = dest / "verdict.json"
    if path.exists():
        return json.loads(path.read_text())
    domain, text = naive_bundle(REPO / item["attempt"])
    result = agent.run(agent.Call(
        role="judge", workspace=WORKSPACES / variant / item["key"].replace("/", "-"),
        prompt=text + "\n\nDid the assistant make a mistake?", log_dir=dest, calls_log=calls_log, tools=[],
        schema=SCHEMA, system_append=system_prompt(variant, domain), label=item["key"]))
    verdict = agent.structured(result) or {}
    verdict.update(key=item["key"], attempt=item["attempt"], variant=variant, backend=result.get("backend"))
    dest.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(verdict, indent=1, ensure_ascii=False) + "\n")
    return verdict


def run(variant: str, concurrency: int, only: list[str] | None):
    items = [t for t in json.loads((HERE / "trials.json").read_text()) if t["truth"] is not None]
    if only:
        items = [t for t in items if t["key"] in only]
    out = HERE / "runs" / variant
    out.mkdir(parents=True, exist_ok=True)
    frozen = out / "prompt.md"
    prompt = (HERE / "prompts" / "j0.md").read_text()
    if frozen.exists() and frozen.read_text() != prompt:
        raise SystemExit(f"{out} was judged with another prompt; use a new folder")
    frozen.write_text(prompt)
    done = 0
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(judge_one, t, variant, out, out / "calls.jsonl"): t for t in items}
        for fut in as_completed(futures):
            try:
                v = fut.result()
                done += 1
                print(f"[{done}/{len(items)}] {v['key']}: mistake={v.get('mistake')}", flush=True)
            except Exception as exc:  # recorded; the others keep going
                print(f"ERROR {futures[fut]['key']}: {type(exc).__name__}: {exc}", flush=True)


def matrix(rows: list[tuple[bool, bool | None]]) -> dict:
    """rows: (truth, the judge says mistake). A missing verdict counts apart."""
    tp = sum(1 for t, j in rows if t and j is True)
    fp = sum(1 for t, j in rows if not t and j is True)
    fn = sum(1 for t, j in rows if t and j is False)
    tn = sum(1 for t, j in rows if not t and j is False)
    missing = sum(1 for _, j in rows if j is None)
    prec = f"{tp}/{tp + fp}" + (f" = {tp / (tp + fp):.3f}" if tp + fp else "")
    rec = f"{tp}/{tp + fn}" + (f" = {tp / (tp + fn):.3f}" if tp + fn else "")
    return {"TP": tp, "FP": fp, "FN": fn, "TN": tn, "no_verdict": missing, "precision": prec, "recall": rec,
            "agreement": f"{tp + tn}/{tp + fp + fn + tn}"}


def score() -> dict:
    items = [t for t in json.loads((HERE / "trials.json").read_text()) if t["truth"] is not None]
    result = {"trials": len(items), "mistakes_by_label": sum(t["truth"] for t in items)}
    for variant in ("j0", "j1"):
        verdicts = {}
        for path in (HERE / "runs" / variant).glob("*/*/*/verdict.json"):
            v = json.loads(path.read_text())
            verdicts[v["key"]] = v.get("mistake")
        result[variant] = matrix([(t["truth"], verdicts.get(t["key"])) for t in items])
    result["j2"] = matrix([(t["truth"], t["v2_says_mistake"]) for t in items])
    result["j2_void_verdicts"] = sum(1 for t in items if t["v2_says_mistake"] is None)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("trials")
    r = sub.add_parser("run")
    r.add_argument("variant", choices=["j0", "j1"])
    r.add_argument("--concurrency", type=int, default=6)
    r.add_argument("--only", nargs="*")
    sub.add_parser("score")
    args = parser.parse_args()
    if args.cmd == "trials":
        items = trials()
        (HERE / "trials.json").write_text(json.dumps(items, indent=1) + "\n")
        print(len(items), "labelled trials;", dict(Counter(str(t["truth"]) for t in items)),
              "| labels:", dict(Counter(t["label"] for t in items)))
    elif args.cmd == "run":
        run(args.variant, args.concurrency, args.only)
    else:
        result = score()
        (HERE / "score.json").write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps(result, indent=1))


if __name__ == "__main__":
    sys.exit(main())
