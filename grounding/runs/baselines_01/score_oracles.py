"""Score a baseline pipeline's oracles against my hand labels, on that pipeline's own trials, flawed tests included.

    python3 grounding/runs/baselines_01/score_oracles.py GEN_DIR     # e.g. n0/runs/gen_01; writes oracles.score.json

Oracles:
- **assertions:** the test's own AgentDiff assertions (assertions.json, from assertions.py);
- **assertions_faithful:** the same, evaluated as our format document described them (assertions.faithful.json, from
  `assertions.py --faithful`);
- **assertions_corrected:** assertions_faithful with the tests in harness_flaws.json (broken by our replica or our
  format document, not by the baseline) counted apart;
- **plain_expected:** a plain LLM judge given the test author's expected outcome (judges.py);
- **j0:** judge_baselines_01's J0 (judges.py).

Truth, from labels.json: incorrect and presented are mistakes; correct, correct_absent, asked and incomplete are not;
artifact and not_established are void. A trial of a test my review found invalid is counted apart, as a false result
if an oracle reports a failure on it. A correct trial with a wrong written value (a priority on the wrong scale) is a
real failure outside the grounding scope, also counted apart.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

MISTAKE = {"incorrect", "presented"}
VOID = {"artifact", "not_established"}


def verdicts(folder: Path) -> dict:
    out = {}
    for p in folder.rglob("verdict.json"):
        v = json.loads(p.read_text())
        out[v["key"]] = v.get("mistake")
    return out


def main():
    gen = Path(sys.argv[1]).resolve()
    labels = {k: v for k, v in json.loads((gen / "labels.json").read_text()).items() if not k.startswith("_")}
    review = {r["test"]: r for r in json.loads((gen / "review.json").read_text())}
    if (gen / "runtime_flaws.json").exists():  # flaws found while labelling count as well ("flawed is flawed")
        for test in (k for k in json.loads((gen / "runtime_flaws.json").read_text()) if not k.startswith("_")):
            review.setdefault(test, {})["valid"] = False
    oracles = {}
    for name, file in (("assertions", "assertions.json"), ("assertions_faithful", "assertions.faithful.json")):
        if (gen / file).exists():
            oracles[name] = {f"solve_01/{k}": (not v["passed"]) if v.get("passed") is not None else None
                             for k, v in json.loads((gen / file).read_text()).items()}
    harness = {}
    if (gen / "harness_flaws.json").exists():
        harness = {k: v for k, v in json.loads((gen / "harness_flaws.json").read_text()).items() if not k.startswith("_")}
    if "assertions_faithful" in oracles:
        oracles["assertions_corrected"] = oracles["assertions_faithful"]
    for name in ("plain_expected", "j0"):
        if (gen / f"judged_{name}").exists():
            oracles[name] = verdicts(gen / f"judged_{name}")
    out = {}
    for name, says_by_key in oracles.items():
        cells = defaultdict(int)
        notes = defaultdict(list)
        for key, label in labels.items():
            case = key.split("/")[-1]
            says = says_by_key.get(key)
            if says is None:
                cells["no_verdict"] += 1
                continue
            if name == "assertions_corrected" and case in harness:
                cells["harness_flaw_reported_failure" if says else "harness_flaw_passed"] += 1
                continue
            if not review.get(case, {}).get("valid", True):
                cells["invalid_test_reported_failure" if says else "invalid_test_passed"] += 1
                if says:
                    notes["invalid_test_reported_failure"].append(key)
                continue
            if label["outcome"] in VOID:
                cells["void_reported_failure" if says else "void_passed"] += 1
                continue
            truth = label["outcome"] in MISTAKE
            if not truth and label.get("value_error"):
                cells["value_error_reported" if says else "value_error_missed"] += 1
                continue
            cell = {(True, True): "TP", (True, False): "FN", (False, True): "FP", (False, False): "TN"}[(truth, bool(says))]
            cells[cell] += 1
            if cell in ("FP", "FN"):
                notes[cell].append(key)
        tp, fp, fn = cells["TP"], cells["FP"], cells["FN"]
        cells["precision"] = round(tp / (tp + fp), 3) if tp + fp else None
        cells["recall"] = round(tp / (tp + fn), 3) if tp + fn else None
        out[name] = {"cells": dict(cells), "keys": {k: sorted(v) for k, v in notes.items()}}
    (gen / "oracles.score.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v["cells"] for k, v in out.items()}, indent=1))


if __name__ == "__main__":
    main()
