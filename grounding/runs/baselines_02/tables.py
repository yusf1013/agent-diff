"""The label-based measures of baselines_01, run unchanged on this study's arms.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.tables policy    # policy_facts.json
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.tables oracles   # per arm oracles.score.json
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.tables labels    # per arm labels.summary.json

- **policy:** baselines_01's `policy_facts.py` (facts exposed at the policy level, under its two readings), with its
  folder and arms pointed at this study; it writes `policy_facts.json` here.
- **oracles:** baselines_01's `score_oracles.py` (each arm's own assertions against my labels). It reads trial keys
  as `solve_01/<trial>/<case>`, so it runs on a scratch copy of the arm's labels, review and assertions with the run
  name rewritten to that; the result is copied back as `runs/gen_<arm>_01/oracles.score.json`.
- **labels:** baselines_01's `summarize_labels.py` on each arm's labels and review.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from grounding.runs.baselines_01 import policy_facts

HERE = Path(__file__).resolve().parent
B1 = HERE.parent / "baselines_01"
ARMS = {"SN0M": ("runs/gen_n0m_01", "solve_sn0m_01"), "SN1M": ("runs/gen_n1m_01", "solve_sn1m_01")}


def policy() -> None:
    policy_facts.HERE = HERE
    policy_facts.GENS = {arm: gen for arm, (gen, _) in ARMS.items()}
    policy_facts.main()


def oracles() -> None:
    for arm, (gen, run) in ARMS.items():
        src = HERE / gen
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp)
            labels = json.loads((src / "labels.json").read_text())
            (dst / "labels.json").write_text(json.dumps(
                {(k.replace(run + "/", "solve_01/", 1) if not k.startswith("_") else k): v for k, v in labels.items()}))
            for name in ("review.json", "assertions.twin.json", "harness_flaws.json", "runtime_flaws.json"):
                if (src / name).exists():
                    shutil.copy(src / name, dst / name)
            subprocess.run([sys.executable, str(B1 / "score_oracles.py"), str(dst)], check=True)
            shutil.copy(dst / "oracles.score.json", src / "oracles.score.json")


def labels() -> None:
    for arm, (gen, _) in ARMS.items():
        src = HERE / gen
        out = subprocess.run([sys.executable, str(B1 / "summarize_labels.py"), str(src / "labels.json"),
                              str(src / "review.json")], capture_output=True, text=True, check=True).stdout
        (src / "labels.summary.json").write_text(out)
        print(arm, out)


if __name__ == "__main__":
    {"policy": policy, "oracles": oracles, "labels": labels}[sys.argv[1]]()
