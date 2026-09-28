"""List a run's trials (latest attempt of each) for judges.py.

    python3 grounding/runs/baselines_01/trials_of.py RUN_DIR > TRIALS.json

Keys are "<run name>/t<k>/<case id>"; attempts are repository-relative.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def main():
    run = Path(sys.argv[1]).resolve()
    items = []
    for trial_dir in sorted(run.glob("t*/*")):
        if not trial_dir.is_dir():
            continue
        attempts = sorted(trial_dir.glob("attempt-*"))
        if not attempts or not (attempts[-1] / "execution_summary.json").exists():
            continue
        items.append({"key": f"{run.name}/{trial_dir.parent.name}/{trial_dir.name}",
                      "attempt": str(attempts[-1].relative_to(REPO))})
    print(json.dumps(items, indent=1))


if __name__ == "__main__":
    main()
