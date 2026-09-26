"""Record my reading of the Arm R verdicts judged after the session-limit rerun (2026-09-26, 12:30). Run once.

AR-SLK-22 and AR-SLK-24 (the two scenarios whose solver runs came last) have no failing trial. The two new void
verdicts are Linear trials where Qwen concluded that Linear has no documents, as in the clean sample (report §2).
"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "eval" / "judge_review.json"
NOTE = ("Agree: the solver answered 'none' after wrongly concluding that Linear has no documents, without reading "
        "any; the manual labels treated the same behaviour as not established.")
review = json.loads(PATH.read_text())
for key in ("solve_arm_r/t2/FP-AR-LIN-22-I11-I12", "solve_arm_r/t2/P-AR-LIN-22-I14"):
    review[key] = {"review": "agree", "note": NOTE}
PATH.write_text(json.dumps(review, indent=1) + "\n")
print(sum(1 for k in review if k.startswith("solve_arm_r/")), "Arm R verdicts reviewed")
