"""Phase 2 calibration summary: the automated variants against my hand-made ones (plan, Phase 2 bars).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.calibration dropf DIR
    python ... calibration clone DIR

drop-F: per fact, the automated status and request, mine, whether they are identical, and the content words the
automated request adds (the check added after cal1, applied here after the fact to runs made without it).
clone: per scenario, the automated status as run, and as re-scored under amendment 3's rule (only the match set is a
finding for a clone, whose request is the scenario's own), from the reader verdicts saved with each round; and mine.
Writes DIR/calibration.json. My validity review of each accepted variant is recorded separately
(eval/phase2_review.json).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import reader2
from grounding.runs.autogen_02.kit.variants2 import added_words, source_cases

STUDY = Path(__file__).resolve().parents[1]


def dropf(folder: Path) -> dict:
    manual = {(v["scenario"], v["fact"]): v for v in json.loads((STUDY / "phase1_dropf.json").read_text())["variants"]}
    originals = {c["case_id"]: c["prompt"] for c in source_cases("exemplars")}
    rows = []
    for path in sorted(folder.glob("*/record.json")):
        r = json.loads(path.read_text())
        m = manual.get((r["scenario"], r["fact"]), {})
        auto = r.get("request") if r["status"] == "accepted" else None
        row = {"id": r["id"], "fact": r["fact"], "status": r["status"], "rounds": len(r.get("rounds", [])),
               "auto": auto, "manual": m.get("prompt"), "manual_not_derivable": m.get("not_derivable"),
               "identical": bool(auto and m.get("prompt") and auto.strip() == m["prompt"].strip()),
               "added_words": added_words(originals[r["scenario"]], auto) if auto else [],
               "problems": r.get("problems", [])}
        rows.append(row)
    derivable = [x for x in rows if x["status"] != "not_derivable"]
    summary = {"facts": len(rows), "derivable_by_code": len(derivable),
               "same_derivability_as_mine": sum((x["status"] != "not_derivable") == bool(x["manual"]) for x in rows),
               "accepted": sum(x["status"] == "accepted" for x in rows),
               "accepted_clean": sum(x["status"] == "accepted" and not x["added_words"] for x in rows),
               "writer_declined": sum(x["status"] == "writer_declined" for x in rows),
               "rejected": sum(x["status"] == "rejected" for x in rows),
               "identical_to_mine": sum(x["identical"] for x in rows)}
    return {"summary": summary, "rows": rows}


def clone(folder: Path) -> dict:
    manual = {v["scenario"]: v for v in json.loads((STUDY / "phase1_clones.json").read_text())["clones"]}
    rows = []
    for path in sorted(folder.glob("*/record.json")):
        r = json.loads(path.read_text())
        rescored, at_round, notes = r["status"], None, []
        for entry in r.get("rounds", []):
            w = entry.get("writer", {})
            if not w.get("possible"):
                rescored = "writer_declined"
                break
            code = [f for f in entry.get("findings", []) if not f.startswith("The reader")]
            verdict = entry.get("reader")
            if verdict is None:
                continue  # code findings before any reader: the round failed on code
            variant = json.loads((path.parent / "variant.json").read_text()) if (path.parent / "variant.json").exists() \
                else None
            intended = [str(x) for x in (variant["references"][0]["expected"] if variant else [])] or None
            match = [f for f in entry.get("findings", []) if f.startswith(("The reader says", "The reader did not"))
                     and "single record" not in f]
            if not code and not match:
                rescored, at_round = "accepted", entry["round"]
                notes = reader2.wording_notes(verdict)
                break
        m = manual.get(r["scenario"], {})
        rows.append({"id": r["id"], "status_as_run": r["status"], "status_rescored": rescored,
                     "accepted_at_round": at_round, "wording_notes": notes, "changes": r.get("changes"),
                     "new_key": r.get("new_key"), "manual": m.get("changes"), "manual_not_derivable":
                     m.get("not_derivable"), "problems": r.get("problems", [])})
    summary = {"scenarios": len(rows),
               "accepted_as_run": sum(x["status_as_run"] == "accepted" for x in rows),
               "accepted_rescored": sum(x["status_rescored"] == "accepted" for x in rows),
               "declined": sum(x["status_rescored"] == "writer_declined" for x in rows),
               "same_possible_call_as_mine": sum((x["status_rescored"] == "accepted") == (not x["manual_not_derivable"])
                                                 for x in rows)}
    return {"summary": summary, "rows": rows}


def main():
    kind, folder = sys.argv[1], Path(sys.argv[2]).resolve()
    result = dropf(folder) if kind == "dropf" else clone(folder)
    (folder / "calibration.json").write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(result["summary"], indent=1))
    for row in result["rows"]:
        print(json.dumps(row, ensure_ascii=False)[:700])


if __name__ == "__main__":
    main()
