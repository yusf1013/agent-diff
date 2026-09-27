"""The blind sample for judge v2's evaluation (plan, Phase 2 "Blind set"): trials of a Phase 3 or 4 run drawn at random
before the run, which I label before reading any verdict on them.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.blind_sample CASES_DIR RUN_NAME N SEED

Writes eval/blind_<RUN_NAME>.json: the drawn keys (run/trial/case), the seed and the time. The draw uses only the
cases folder, so it cannot depend on any outcome.
"""
import json
import random
import sys
from datetime import datetime
from pathlib import Path

STUDY = Path(__file__).resolve().parents[1]


def main():
    cases_dir, run_name, n, seed = Path(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    cases = sorted(p.stem for p in cases_dir.glob("*/*.json"))
    slots = [f"{run_name}/{t}/{c}" for c in cases for t in ("t1", "t2", "t3")]
    drawn = sorted(random.Random(seed).sample(slots, min(n, len(slots))))
    out = STUDY / "eval" / f"blind_{run_name}.json"
    if out.exists():
        raise SystemExit(f"{out} exists: the sample is drawn once")
    out.write_text(json.dumps({"_about": "Blind sample for judge v2: drawn before the run from the cases folder "
                                         "alone; labelled by me before reading any verdict on these trials.",
                               "cases_dir": str(cases_dir), "seed": seed, "drawn_at": datetime.now().isoformat(),
                               "of": len(slots), "keys": drawn}, indent=1) + "\n")
    print(f"{len(drawn)} of {len(slots)} trials -> {out}")


if __name__ == "__main__":
    main()
