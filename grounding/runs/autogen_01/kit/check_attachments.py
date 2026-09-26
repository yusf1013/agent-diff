"""Which AP-LIN-06 / AP2-LIN-06 trials ever saw the attachment records, given the replica's broken Issue.attachments.

    python3 -m grounding.runs.autogen_01.kit.check_attachments

The replica has no resolver for the nested `Issue.attachments` connection, so `issue { attachments { nodes } }` fails
with "Cannot return null for non-nullable field AttachmentConnection.nodes"; only the top-level `attachments` query
works. A trial that never saw any attachment id in an observation cannot have established its answer.
"""
import json
from pathlib import Path

RUNS = Path(__file__).resolve().parents[1] / "runs"


def attachment_ids(gen, sid):
    """Each attachment's id and url (unique per record; titles are shared by design)."""
    case = json.loads((RUNS / gen / sid / "case.json").read_text())
    return {v for r in case["seed"].get("attachments", []) for v in (r["id"], r.get("url")) if v}


def main():
    for solve, gen, sid in (("solve_arm_p", "gen_arm_p", "AP-LIN-06"), ("solve_arm_p_v2", "gen_arm_p_v2", "AP2-LIN-06")):
        ids = attachment_ids(gen, sid)
        score = json.loads((RUNS / f"{solve}.score.json").read_text())
        outcome = {(k, t["case_id"]): r["outcome"] for t in score["tests"] for k, r in t["trials"].items()}
        seen_n = total = 0
        for trial_dir in sorted(RUNS.glob(f"{solve}/t*/*{sid[sid.index('-') + 1:]}*")):
            attempt = sorted(trial_dir.glob("attempt-*"))[-1]
            solver = next((attempt / "solver").glob(f"{trial_dir.name}.json"))
            steps = json.loads(solver.read_text())["steps"]
            text = " ".join(str(s.get("observation", "")) for s in steps)
            broken = "AttachmentConnection.nodes" in text
            seen = any(i in text for i in ids)
            total += 1
            seen_n += seen
            print(f"{solve}/{trial_dir.parent.name}/{trial_dir.name}: outcome={outcome.get((trial_dir.parent.name, trial_dir.name))}"
                  f" hit_error={broken} saw_attachments={seen}")
        print(f"== {sid}: {seen_n}/{total} trials saw an attachment record\n")


if __name__ == "__main__":
    main()
