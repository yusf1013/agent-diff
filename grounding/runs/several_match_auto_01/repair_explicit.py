"""Explicit rebuilds after review.
- Two round-2 repairs, with the drops the reader's verdicts implied (round 2 is not idempotent: its first run
  overwrote the placements it reads). BOX-23-H: the reader doubted the copy in the other folder (O); G4-CAL-01-H: the
  copies on the other calendars (C, H).
- Box cases whose first build gave a file and a folder the same id (seedkit then kept separate counters): rebuilt
  as R versions with one id space, the writer's texts kept."""
import json
from pathlib import Path

from grounding.runs.several_match_auto_01 import build as B
from grounding.runs.several_match_auto_01.population import covers

HERE = B.HERE
answers = json.loads((HERE / "writer.json").read_text())
report = json.loads((HERE / "build.json").read_text())
placements = json.loads((HERE / "placements.json").read_text())
by_id = {c["case_id"]: c for c in covers()}
for cover_id, drop in (("BOX-23", {"O"}), ("G4-CAL-01", {"C", "H"})):
    r = B.build_one(by_id[cover_id], answers[cover_id], tiers=("H",), suffix="R", drop=drop, no_variants=True)
    c = r["cases"].get("H") or {}
    report[f"{cover_id}:HR"] = {**r, "repair_of": f"SMA-{cover_id}-H", "dropped": sorted(drop), "round": 2}
    if c.get("built"):
        placements[c["id"]] = c["placements"]
    else:
        (B.OUT / r["domain"] / f"SMA-{cover_id}-HR.json").unlink(missing_ok=True)
        placements.pop(f"SMA-{cover_id}-HR", None)
    print(cover_id, "built" if c.get("built") else f"not built: {c.get('why')}", c.get("traps"))
for cover_id, tier in (("AP-BOX-02", "H"), ("G4-BOX-04", "E")):
    r = B.build_one(by_id[cover_id], answers[cover_id], tiers=(tier,), suffix="R")
    c = r["cases"].get(tier) or {}
    report[f"{cover_id}:{tier}R"] = {**r, "repair_of": f"SMA-{cover_id}-{tier}", "why": "a file and a folder shared an id"}
    if c.get("built"):
        placements[c["id"]] = c["placements"]
    print(cover_id, tier, "built" if c.get("built") else f"not built: {c.get('why') or c.get('problems')}")
(HERE / "build.json").write_text(json.dumps(report, indent=1, default=str) + "\n")
(HERE / "placements.json").write_text(json.dumps(placements, indent=1) + "\n")
