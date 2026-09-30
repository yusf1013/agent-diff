"""Write rulings.json (this study's rulings, in roadmap_01/known_defects.json's format) from my review, eval/review.json.
No model calls.

    python3 grounding/runs/qwen_writer_01/rulings_from_review.py

- a near miss I ruled flawed -> a `near_misses` entry (ruling "flawed"): its probe is left out; the cover and the fact
  probe that hold it stay, and a trial whose only acted-on records are flawed near misses does not count;
- a scenario I ruled invalid -> a `curated` entry that leaves out every test derived from it ("weak but valid" and
  "valid" scenarios are kept).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = "qwen_writer_01/eval/review.json (my review under the PI's criteria of 2026-09-28; for the PI to overrule)"


def main():
    review = json.loads((HERE / "eval" / "review.json").read_text())
    doc = json.loads((HERE / "rulings.json").read_text())
    doc["near_misses"] = [{"scenario": sid, "witness": w, "ruling": "flawed", "why": n["note"], "source": SOURCE}
                          for sid, r in sorted(review.items()) if not sid.startswith("_")
                          for w, n in r["near_misses"].items() if n["verdict"] == "flawed"]
    doc["curated"] = [{"id": sid, "kind": "scenario: invalid", "note": r.get("note", ""), "source": SOURCE,
                       "for_new_agents": "leave out", "frozen_suite": "leave out"}
                      for sid, r in sorted(review.items()) if not sid.startswith("_") and r["verdict"] == "invalid"]
    (HERE / "rulings.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(doc['near_misses'])} flawed near misses, {len(doc['curated'])} scenarios left out")


if __name__ == "__main__":
    main()
