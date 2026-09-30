"""Judge v2 against my blind labels, per set and pooled, for the Sol round. No model calls.

Uses autogen_02/kit/judge2.py's `compare` unchanged per set (collapsed agreement, the confusion, the judge as a
detector of failures on trials both call usable, the same exposed facts when both fail), with each label compared
with the verdict on the attempt it was written on. Adds what `compare` leaves out:
- exact outcome agreement (the eight outcomes, not collapsed);
- mechanism agreement where both call the trial a failure (Sol's reasoning is not recorded, so the judge's
  mechanism rests on the final answer and the responses, as my label does);
- the effective label: an adjudication or a correction replaces the initial label (both kept in their own files);
- pooled totals, and every disagreement with both notes: `pooled` over the Muse-written half's four sets (as
  report_01 reads it), `pooled_regen` over the regenerated half's three, `pooled_all` over all seven.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.judge_accuracy   # eval/judge_accuracy.json
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_01.kit.judge import COLLAPSE
from grounding.runs.autogen_02.kit import judge2
from grounding.runs.sol_eval_01.kit import sets

STUDY = Path(__file__).resolve().parents[1]
EVAL = STUDY / "eval"
SETS = tuple(sets.SETS)


def effective_labels(name: str) -> tuple[dict, dict]:
    folder = EVAL / f"labels_{name}"
    initial = {k: v for k, v in json.loads((folder / f"{name}_blind.json").read_text()).items() if not k.startswith("_")}
    labels, changed = dict(initial), {}
    for kind in ("adjudications", "corrections"):
        path = folder / f"{name}_{kind}.json"
        if path.exists():
            for k, v in json.loads(path.read_text()).items():
                if not k.startswith("_"):
                    labels[k] = v
                    changed[k] = kind
    return labels, changed


def locked(name: str) -> bool:
    """A set is compared only once all its blind labels are written and locked (eval/labels_<set>/<set>_blind.sha256
    holds the labels file's hash), so no verdict is read before the labels are final."""
    import hashlib
    folder = EVAL / f"labels_{name}"
    lock = folder / f"{name}_blind.sha256"
    if not lock.exists():
        return False
    digest = lock.read_text().split()[0]
    return hashlib.sha256((folder / f"{name}_blind.json").read_bytes()).hexdigest() == digest


def verdict_for(name: str, key: str, attempt: str) -> dict | None:
    folder = EVAL / f"judged_{name}" / key
    for path in [folder / "verdict.json"] + sorted(folder.glob("verdict-*.json")):
        if path.exists():
            v = json.loads(path.read_text())
            if Path(v.get("attempt", "")).name == attempt:
                return v
    return None


def pool(sets_out: dict, names: list[str]) -> dict:
    pooled, mech = Counter(), Counter()
    for name in names:
        if name not in sets_out:
            continue
        s = sets_out[name]
        pooled["labelled"] += s["with_verdict"]
        pooled["exact"] += int(s["exact_agreement"].split("/")[0])
        pooled["collapsed"] += int(s["collapsed_agreement"].split("/")[0])
        det = s["failure_detection"]
        for k in ("usable_by_both", "judge_fail", "label_fail", "both_fail", "void_by_label_only", "void_by_judge_only"):
            pooled[k] += det[k]
        pooled["same_facts"] += int(det["same_exposed_facts_when_both_fail"].split("/")[0])
        for pair, n in s["mechanism_label_to_judge_when_both_fail"].items():
            mech[tuple(pair.split(" -> "))] += n
    return {**pooled, "sets": [n for n in names if n in sets_out],
            "precision": f"{pooled['both_fail']}/{pooled['judge_fail']}",
            "recall": f"{pooled['both_fail']}/{pooled['label_fail']}",
            "mechanism_agreement_when_both_fail": f"{sum(n for (a, b), n in mech.items() if a == b)}"
                                                  f"/{sum(mech.values())}"}


def main():
    out = {"_about": __doc__.split("\n\n")[0], "sets": {}}
    for name in SETS:
        if not (EVAL / f"labels_{name}" / f"{name}_blind.json").exists() or not (EVAL / f"judged_{name}").exists():
            continue
        if not locked(name):
            print(f"{name}: its blind labels are not complete and locked yet; not compared")
            continue
        labels, changed = effective_labels(name)
        attempts = {k: v["attempt"] for k, v in labels.items()}
        tmp = EVAL / f"labels_{name}" / ".effective.json"
        tmp.write_text(json.dumps(labels))
        base = judge2.compare(EVAL / f"judged_{name}", [tmp], attempts=attempts)
        tmp.unlink()
        rows, exact, mech, missing = [], 0, Counter(), []
        for key, lab in sorted(labels.items()):
            v = verdict_for(name, key, lab["attempt"])
            if v is None:
                missing.append(key)
                continue
            same = lab["outcome"] == v.get("outcome")
            exact += same
            both_fail = COLLAPSE.get(lab["outcome"]) == "fail" and COLLAPSE.get(v.get("outcome")) == "fail"
            if both_fail:
                mech[(lab.get("mechanism"), v.get("mechanism"))] += 1
            if not same or (both_fail and lab.get("mechanism") != v.get("mechanism")):
                rows.append({"key": key, "label": lab["outcome"], "judge": v.get("outcome"),
                             "label_exposed": lab.get("exposed"), "judge_exposed": v.get("exposed"),
                             "label_mechanism": lab.get("mechanism"), "judge_mechanism": v.get("mechanism"),
                             "label_changed_by": changed.get(key), "label_note": lab.get("note"),
                             "judge_note": v.get("note")})
        det = base["failure_detection"]
        out["sets"][name] = {"labelled": len(labels), "with_verdict": len(labels) - len(missing),
                             "missing_verdict": missing, "exact_agreement": f"{exact}/{len(labels) - len(missing)}",
                             "collapsed_agreement": base["collapsed_agreement"], "failure_detection": det,
                             "confusion_label_to_judge": base["confusion_ref_to_judge"],
                             "mechanism_label_to_judge_when_both_fail": {f"{a} -> {b}": n for (a, b), n in mech.items()},
                             "labels_changed": changed, "differences": rows}
    out["pooled"] = pool(out["sets"], sets.of_half("muse"))
    out["pooled_regen"] = pool(out["sets"], sets.of_half("regen"))
    out["pooled_all"] = pool(out["sets"], list(SETS))
    (EVAL / "judge_accuracy.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    for name, s in out["sets"].items():
        print(name, {k: s[k] for k in ("labelled", "exact_agreement", "collapsed_agreement")}, s["failure_detection"],
              s["mechanism_label_to_judge_when_both_fail"], f"{len(s['differences'])} differences")
    for k in ("pooled", "pooled_regen", "pooled_all"):
        print(k, {x: y for x, y in out[k].items() if x != "sets"})


if __name__ == "__main__":
    main()
