"""What I read to label one trial by hand: the request, the targets and decoys with their facts, the steps, the reply
and the diff. It shows no verdict and no mechanical attribution (the judge bundle's provisional outcome), so the label
cannot lean on either.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.claudecode_pilot_01.eval.label_view RUN_DIR CASE_ID [TRIAL]
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import bundle


def view(run_dir: Path, case_id: str, trial: str = "t1") -> str:
    attempt = sorted((run_dir / trial / case_id).glob("attempt-*"))[-1]
    case = json.loads((attempt / "case.json").read_text())
    summary = json.loads((attempt / "execution_summary.json").read_text())
    record = bundle.solver_record(attempt)
    cand, handles = bundle.candidates(case)
    final = (attempt / "solver" / "final_response.md").read_text().strip() \
        if (attempt / "solver" / "final_response.md").exists() else ""
    return "\n\n".join([
        f"# {case_id} ({case['domain']}), {attempt.name}: status {summary.get('status')}, termination "
        f"{record.get('termination') or summary.get('termination')}, "
        f"{(summary.get('turn_durations_s') or [None])[0]} s" + (f", error {summary.get('error')}"
                                                                if summary.get("error") else ""),
        f"## Request\n{case['prompt']}",
        f"## Candidates\n{cand}",
        f"## Steps\n{bundle.trajectory(record, handles)}",
        f"## Final answer\n{final or '(none)'}",
        f"## State diff\n{bundle.diff_text(attempt)}"])


if __name__ == "__main__":
    print(view(Path(sys.argv[1]), sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "t1"))
