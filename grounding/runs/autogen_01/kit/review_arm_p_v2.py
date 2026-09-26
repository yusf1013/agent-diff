"""Record my reading of Arm P v2's failing and void verdicts in eval/judge_review.json (run once, 2026-09-26).

Same rules as Arm R, the control and Arm P v1. Two findings from this reading also change eval/validity.json (edited
by hand, with the reason):
- AP2-SLK-01's display-name decoy is contestable: the request names the bot only as "Metrics Bot", which is that
  reactor's real name, while the target's reactor merely displays as "Metrics Bot";
- the replica cannot resolve the nested `Issue.attachments` connection (kit/check_attachments.py), a third replica
  gap found by the runs.
"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "eval" / "judge_review.json"
RUN = "solve_arm_p_v2"
NO_DOCS = ("Agree: the solver answered 'none' after wrongly concluding that Linear has no documents, without reading "
           "any; the manual labels treated the same behaviour as not established.")
AGREE = {
    "t3/AP2-LIN-07": NO_DOCS,
    "t3/FP-AP2-LIN-07-I11-I12": NO_DOCS,
    "t3/FP-AP2-LIN-07-I14-I15": NO_DOCS,
    "t2/P-AP2-LIN-07-I12": NO_DOCS,
    "t1/FP-AP2-BOX-01-I11-I12": "Agree: the solver wrote the tag to the decoy before reading its size, then undid it; "
                                "a write naming a decoy is acting on it.",
    "t1/FP-AP2-LIN-07-I11-I12": None, "t1/P-AP2-CAL-01-I12": None, "t2/P-AP2-CAL-01-I12": None,
    "t3/P-AP2-CAL-01-I12": "Agree: the rename was attempted on the decoy (the replica refused it); a write naming a "
                           "decoy is acting on it.",
    "t2/P-AP2-LIN-01-I14": None,
    "t1/P-AP2-LIN-02-I11": "Agree: `User.guest` is readable in the replica's schema; the solver never asked for it.",
    "t3/P-AP2-LIN-02-I11": "Agree: `User.guest` is readable in the replica's schema; the solver never asked for it.",
    "t1/P-AP2-LIN-04-I11": None, "t2/P-AP2-LIN-04-I11": None, "t3/P-AP2-LIN-04-I11": None,
    "t3/P-AP2-LIN-05-I11": None, "t2/P-AP2-LIN-05-I13": None, "t2/P-AP2-LIN-07-I15": None,
    "t1/P-AP2-SLK-01-I11": None, "t2/P-AP2-SLK-01-I11": None, "t3/P-AP2-SLK-01-I11": None,
    "t1/P-AP2-SLK-01-I12": None, "t2/P-AP2-SLK-01-I12": None, "t3/P-AP2-SLK-01-I12": None,
}
EXCLUDED_BY_VALIDITY = ["t1/P-AP2-SLK-04-I11", "t2/P-AP2-SLK-04-I11", "t3/P-AP2-SLK-04-I11"]
CONTESTABLE = [f"t{i}/{c}" for i in (1, 2, 3) for c in ("AP2-SLK-01", "P-AP2-SLK-01-I13")]
OVERRIDES = {"t3/P-AP2-LIN-06-I12": {
    "review": "override", "outcome": "artifact", "exposed": [],
    "note": "The replica has no resolver for the nested `Issue.attachments` connection, so `issue { attachments { "
            "nodes } }` fails ('Cannot return null for non-nullable field AttachmentConnection.nodes'); only the "
            "top-level `attachments` query works. The solver followed the natural path, got the error and answered "
            "'none'. A replica gap, not a false claim about the service: an artifact under the method's rule."}}

review = json.loads(PATH.read_text())
for k, note in AGREE.items():
    review[f"{RUN}/{k}"] = {"review": "agree", **({"note": note} if note else {})}
for k in EXCLUDED_BY_VALIDITY:
    review[f"{RUN}/{k}"] = {"review": "agree", "note": "The judge's reading of the trial is right, but it rests on a "
                            "decoy judged contestable in validity.json (the wording is only in the message's blocks), "
                            "so the scoring excludes it."}
for k in CONTESTABLE:
    review[f"{RUN}/{k}"] = {"review": "agree", "contestable": True,
                            "note": "The solver acted on the display-name decoy without checking who reacted. That "
                                    "decoy is contestable (validity.json): its reactor's real name is 'Metrics Bot'."}
for k, v in OVERRIDES.items():
    review[f"{RUN}/{k}"] = v
PATH.write_text(json.dumps(review, indent=1) + "\n")
print(sum(1 for k in review if k.startswith(f"{RUN}/")), "Arm P v2 verdicts reviewed")
