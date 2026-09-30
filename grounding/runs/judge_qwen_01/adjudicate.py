"""The manual adjudication of Qwen-Muse disagreements: lock my labels, then unblind (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.adjudicate add NAME KEY --outcome O \
        [--acted IDS] [--exposed FACTS] [--mechanism M] [--artifact-reason R] [--steps S] --confidence C --reason R
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.adjudicate lock NAME
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.adjudicate unblind NAME --out runs/selfhost

Protocol (adjudication/README.md): the queue (`adjudication/queue_NAME.json`, keys only, shuffled) is read with
view.py, which shows evidence only. For each key I write, into `adjudication/labels_NAME.json`, the outcome, the ids
acted on, the exposed facts, the mechanism, the artifact reason, the reason and the decisive steps, before opening
either verdict or the reference label. `lock` records the labels' SHA-256 and the time. `unblind` refuses unless
the labels still match the lock, then sets each label beside Qwen's verdict, Muse's and the reference label, and
says who was right: on the outcome group (failure, nonfailure, void), then on the exact outcome, then, where the
group is failure, on the exposed facts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from grounding.runs.judge_qwen_01.common import HERE, cls, labels, load, muse_verdict

ADJ = HERE / "adjudication"


OUTCOMES = ("incorrect", "presented", "correct", "correct_absent", "false_absence", "incomplete", "not_established",
            "artifact")
MECHANISMS = ("skipped-check", "saw-mismatch-accepted", "misread", "none")


def add(name: str, key: str, outcome: str, acted: str, exposed: str, mechanism: str, artifact_reason: str,
        steps: str, confidence: str, reason: str):
    """Record one label (before the lock only; a key is written once)."""
    if (ADJ / f"lock_{name}.json").exists():
        raise SystemExit("locked: corrections after the lock go to corrections_NAME.json")
    if key not in load(ADJ / f"queue_{name}.json"):
        raise SystemExit(f"{key} is not in the queue")
    if outcome not in OUTCOMES or mechanism not in MECHANISMS:
        raise SystemExit("unknown outcome or mechanism")
    path = ADJ / f"labels_{name}.json"
    doc = load(path) if path.exists() else {"_about": "My blind labels on the Qwen-Muse disagreements (README.md). "
                                                      "Written from view.py's evidence before any verdict or "
                                                      "reference label was opened."}
    if key in doc:
        raise SystemExit(f"{key} already has a label")
    split = lambda text: [x.strip() for x in text.split(",") if x.strip()]
    doc[key] = {"outcome": outcome, "acted_on": split(acted), "exposed": sorted(split(exposed)),
                "mechanism": mechanism, "artifact_reason": artifact_reason, "decisive_steps": steps,
                "confidence": confidence, "reason": reason, "labelled_utc": datetime.now(timezone.utc).isoformat()}
    path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    queue = load(ADJ / f"queue_{name}.json")
    print(f"{key}: {outcome} {split(exposed)}; {sum(k in doc for k in queue)}/{len(queue)} labelled")


def lock(name: str):
    path = ADJ / f"labels_{name}.json"
    queue = load(ADJ / f"queue_{name}.json")
    mine = {k: v for k, v in load(path).items() if not k.startswith("_")}
    missing = [k for k in queue if k not in mine]
    if missing:
        raise SystemExit(f"{len(missing)} queued keys have no label yet, e.g. {missing[:3]}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    record = {"file": path.name, "sha256": digest, "labels": len(mine), "queue": len(queue),
              "locked_utc": datetime.now(timezone.utc).isoformat()}
    (ADJ / f"lock_{name}.json").write_text(json.dumps(record, indent=1) + "\n")
    print(json.dumps(record, indent=1))


def verdict_of(v: dict | None) -> dict | None:
    if not v:
        return None
    return {"outcome": v.get("outcome"), "exposed": sorted(v.get("exposed") or []), "mechanism": v.get("mechanism"),
            "note": v.get("note")}


def who(mine: dict, qwen: dict, muse: dict) -> dict:
    out = {}
    for level, get in (("group", lambda x: cls(x["outcome"])), ("outcome", lambda x: x["outcome"]),
                       ("facts", lambda x: sorted(x.get("exposed") or []))):
        if level == "facts" and cls(mine["outcome"]) != "fail":
            continue
        q, m, a = get(qwen), get(muse), get(mine)
        out[level] = "both" if q == m == a else "qwen" if q == a else "muse" if m == a else "neither"
    return out


def unblind(name: str, out: Path):
    record = load(ADJ / f"lock_{name}.json")
    path = ADJ / f"labels_{name}.json"
    if hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
        raise SystemExit("the labels changed after the lock")
    mine = {k: v for k, v in load(path).items() if not k.startswith("_")}
    ref = labels()
    rows, tally = [], Counter()
    for key in load(ADJ / f"queue_{name}.json"):
        qp = out / key / "verdict.json"
        q, m = verdict_of(load(qp)), verdict_of(muse_verdict(key))
        label = ref.get(key)
        a = mine[key]
        verdicts = who(a, q, m)
        tally.update(f"{level}:{w}" for level, w in verdicts.items())
        rows.append({"key": key, "mine": a, "qwen": q, "muse": m,
                     "reference_label": {k: label[k] for k in ("outcome", "exposed", "mechanism", "source")}
                     if label else None,
                     "right": verdicts,
                     "mine_vs_reference_group": None if not label or label["outcome"] is None else
                     cls(a["outcome"]) == cls(label["outcome"])})
    result = {"lock": record, "unblinded_utc": datetime.now(timezone.utc).isoformat(), "tally": dict(tally),
              "rows": rows}
    (ADJ / f"unblinded_{name}.json").write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    ad = sub.add_parser("add")
    ad.add_argument("name")
    ad.add_argument("key")
    ad.add_argument("--outcome", required=True)
    ad.add_argument("--acted", default="")
    ad.add_argument("--exposed", default="")
    ad.add_argument("--mechanism", default="none")
    ad.add_argument("--artifact-reason", default="")
    ad.add_argument("--steps", default="")
    ad.add_argument("--confidence", choices=["high", "medium", "low"], required=True)
    ad.add_argument("--reason", required=True)
    lk = sub.add_parser("lock")
    lk.add_argument("name")
    ub = sub.add_parser("unblind")
    ub.add_argument("name")
    ub.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if args.cmd == "add":
        add(args.name, args.key, args.outcome, args.acted, args.exposed, args.mechanism, args.artifact_reason,
            args.steps, args.confidence, args.reason)
    elif args.cmd == "lock":
        lock(args.name)
    else:
        unblind(args.name, args.out if args.out.is_absolute() else HERE / args.out)


if __name__ == "__main__":
    main()
