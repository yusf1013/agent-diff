"""Record my reading of the control's failing and void verdicts in eval/judge_review.json (run once, 2026-09-26).

The same rules as for Arm R: an ignored filter that returns the decoy is an artifact; a decoy fact_coverage_02's
labels mark contestable stays contestable.
"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "eval" / "judge_review.json"
AGREE = ["t1/BOX-24", "t2/BOX-24", "t3/BOX-24", "t1/LIN-23", "t2/LIN-23",
         "t1/P-BOX-22-I12", "t2/P-BOX-22-I12", "t3/P-BOX-22-I12",
         "t1/P-BOX-24-I11", "t2/P-BOX-24-I11", "t3/P-BOX-24-I11", "t1/P-BOX-24-I12", "t2/P-BOX-24-I12",
         "t3/P-BOX-24-I12", "t2/P-CAL-23-I12", "t3/P-CAL-23-I12", "t3/P-CAL-24-I11", "t1/P-CAL-24-I12",
         "t3/P-CAL-24-I12", "t1/P-LIN-21-I12", "t3/P-LIN-21-I12", "t3/P-LIN-22-I13", "t2/P-LIN-23-I11",
         "t3/P-LIN-23-I11", "t2/P-LIN-24-I11", "t2/P-LIN-25-I11", "t3/P-LIN-25-I11", "t1/P-LIN-25-I12",
         "t2/P-LIN-25-I12", "t3/P-LIN-25-I12", "t1/P-LIN-26-I12", "t3/P-LIN-26-I12", "t1/P-LIN-26-I13",
         "t1/P-SLK-21-I12", "t2/P-SLK-21-I12", "t3/P-SLK-21-I12", "t2/P-SLK-22-I12", "t3/P-SLK-22-I12",
         "t2/P-SLK-23-I11", "t3/P-SLK-23-I11"]
OVERRIDES = {
    "t1/P-LIN-22-I12": {"review": "override", "outcome": "artifact", "exposed": [],
                        "note": "documents(filter: {project: {name: {eq: ...}}}) is ignored by the replica "
                                "(apply_document_filter handles only project.id), so the filter returned the decoy "
                                "d-23, which has no project; the solver trusted it over the null project it then read. "
                                "Same rule as the Arm R overrides."},
    "t3/P-SLK-23-I13": {"review": "override", "outcome": "artifact", "exposed": [],
                        "note": "users.conversations ignores `types` (the gap found in Arm R); the private-channel "
                                "query returned the public decoy. Same rule as P-AR-SLK-23-I13."},
}
CONTESTABLE = ["t1/P-BOX-22-I13", "t2/P-BOX-22-I13"]

review = json.loads(PATH.read_text())
for k in AGREE:
    review[f"solve_control/{k}"] = {"review": "agree"}
for k in CONTESTABLE:
    review[f"solve_control/{k}"] = {"review": "agree", "contestable": True,
                                    "note": "The decoy 'Pricing sheet 2025.xlsx' is contestable in fact_coverage_02's own "
                                            "labels."}
for k, v in OVERRIDES.items():
    review[f"solve_control/{k}"] = v
PATH.write_text(json.dumps(review, indent=1) + "\n")
print(sum(1 for k in review if k.startswith("solve_control/")), "control verdicts reviewed")
