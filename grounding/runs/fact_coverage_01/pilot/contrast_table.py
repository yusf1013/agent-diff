"""Alternative-vs-plain contrast table across trials (absence permitted, one near-miss, no target)."""
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

runs = [r for r in sys.argv[1:] if Path(r).exists()]
out = Path("/tmp") / "contrast_rows.json"
subprocess.run([sys.executable, "-m", "grounding.runs.fact_coverage_01.pilot.results", *runs, "--json", str(out)],
               check=True, capture_output=True)
rows = json.loads(out.read_text())
tab = defaultdict(lambda: {"alt": [], "plain": []})
for r in rows:
    if r.get("status") != "completed" or not r["reference"].endswith(".r1"):
        continue
    fact, kind = r["case_id"][4:].rsplit("-", 1)
    tab[fact][kind].append(r["outcome"])
VALID = ("incorrect", "correct_absent", "correct", "recovered", "absent_unclear")
tot = {"alt": [0, 0], "plain": [0, 0]}
print(f"| Fact | ALT acted / runs | PLAIN acted / runs |\n|---|---|---|")
for fact, d in sorted(tab.items()):
    cells = []
    for kind in ("alt", "plain"):
        acted = sum(x == "incorrect" for x in d[kind])
        valid = sum(x in VALID for x in d[kind])
        tot[kind][0] += acted
        tot[kind][1] += valid
        cells.append(f"{acted}/{valid}")
    print(f"| {fact} | {cells[0]} | {cells[1]} |")
print(f"| **total** | **{tot['alt'][0]}/{tot['alt'][1]}** | **{tot['plain'][0]}/{tot['plain'][1]}** |")
