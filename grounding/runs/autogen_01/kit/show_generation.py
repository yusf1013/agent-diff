"""Print a generation run's history per scenario: findings per version and the reader's verdicts (for reading).

    python3 -m grounding.runs.autogen_01.kit.show_generation RUN_DIR [SCENARIO ...]
"""
import json
import sys
from pathlib import Path

run = Path(sys.argv[1])
only = set(sys.argv[2:])
for sdir in sorted(p for p in run.iterdir() if p.is_dir() and p.name not in ("cases", "kit_snapshot")):
    if only and sdir.name not in only:
        continue
    print(f"=== {sdir.name}")
    outcome = sdir / "outcome.json"
    if outcome.exists():
        o = json.loads(outcome.read_text())
        print(f"  status {o['status']} versions {o['versions']} ({o['seconds']}s)")
        for h in o["history"]:
            print(f"  v{h['version']} {h['stage']}: {len(h['problems'])} problems")
            for p in h["problems"]:
                print("     -", p[:500])
    for v in sorted(sdir.glob("reader-v*/verdict.json")):
        t2 = json.loads(v.read_text()).get("turn2", {})
        print(f"  {v.parent.name}: faithful={t2.get('faithful')} natural={t2.get('natural')} "
              f"| {t2.get('naturalness_note', '')[:160]}")
        for a in t2.get("ambiguity_effects", []):
            print(f"     amb changes={a.get('changes_matches')} plausible={a.get('plausible')} "
                  f"\"{a.get('phrase', '')[:70]}\" | {a.get('explain', '')[:220]}")
    latest = sorted(sdir.glob("scenario-v*.json"))
    if latest:
        s = json.loads(latest[-1].read_text())
        print(f"  request: {s.get('request')}")
        for d in s.get("reference", {}).get("decoys", []):
            print(f"     {d.get('witness')} {d.get('fact')} {d.get('family')}: {d.get('explanation', '')[:160]}")
