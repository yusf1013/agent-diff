"""Is a subfolder of a named folder in the request's scope? A reader-only probe (not a test).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.probe_subfolder
    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.reader \
        --cases SMA-AR-BOX-23-HS SMA-AP2-BOX-02-HS

For requests about the files in a named Box folder, build.py places no copy in a subfolder: whether "the PDFs in the
Product Specs folder" includes a subfolder's PDFs was assumed contestable (method.md check 8), never asked. This
builds, for two such covers, the hard case with a copy one folder down inside the named folder ("Current", as
trap_box makes it) and nothing else, as SMA-<cover>-HS, for the cold reader alone. After the reader, the files move
to probes/ so that no check, run or summary counts them as tests. The reader's verdicts are in reader.json.
"""
from __future__ import annotations

import json

from grounding.runs.several_match_auto_01 import build as B
from grounding.runs.several_match_auto_01.population import covers

COVERS = ("AR-BOX-23", "AP2-BOX-02")


def main():
    answers = json.loads((B.HERE / "writer.json").read_text())
    by_id = {c["case_id"]: c for c in covers()}
    for cid in COVERS:
        b = B.Builder(by_id[cid], answers[cid], drop={"O"})
        b.copy_target(0, "V")
        traps = b.trap_box()
        problems = b.checks()
        case = B.finish(b, "H", answers[cid], by_id[cid], "S")
        # The reference query pins the parent folder by name, so it does not select the subfolder copy: the fdc
        # check reports that, as expected. The probe is written anyway; only the reader reads it.
        (B.OUT / "box" / f"{case['case_id']}.json").write_text(json.dumps(case, indent=1, default=str) + "\n")
        print(case["case_id"], traps, b.place, problems or "ok")


if __name__ == "__main__":
    main()
