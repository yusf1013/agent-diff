"""Tests whose seeds give records ids that name their role in the test ("ev_target", "doc-decoy1", ...). The services'
APIs return these ids, so the agent under test can read them: a hint only a test would give. Found on 2026-09-27
while building the judge baselines (a Qwen trial reasoned "d-target ... this is the clear target"). Reads the frozen
suite and every policy unit; no model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.role_ids

Writes role_ids.json beside this file.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNITS = HERE.parent / "autogen_02" / "runs" / "phase3" / "units"
ROLE = re.compile(r"target|decoy", re.I)
FORMS = (("AT-", "absence twin"), ("UC-", "clone"), ("U-", "drop-F"), ("FP-", "fact probe"), ("P-", "probe"))


def role_ids(case: dict) -> list[str]:
    out = set()
    for rows in case["seed"].values():
        for row in rows if isinstance(rows, list) else []:
            for k, v in (row.items() if isinstance(row, dict) else []):
                if isinstance(v, str) and (k == "id" or k.endswith("_id") or k in ("key", "identifier")) \
                        and ROLE.search(v):
                    out.add(v)
    return sorted(out)


def form(case_id: str) -> str:
    return next((f for p, f in FORMS if case_id.startswith(p)), "cover")


WORDS = re.compile(r"[a-z]{3,}", re.I)
PREFIXES = {"ev", "cal", "cle", "doc", "att", "usr", "team", "user", "issue", "proj", "com", "msg", "chan", "lbl",
            "northwind", "example", "com"}


def worded(identifier: str) -> list[str]:
    """The words in an id beyond a short type prefix and the seed's domain ("ev_start_swap" -> start, swap)."""
    return [w for w in WORDS.findall(identifier.split("@")[0]) if w.lower() not in PREFIXES]


def near_miss_ids(folder: Path) -> dict:
    """Across a suite's covers: how many near misses have an id made of words (which can describe the trap), per
    domain, with examples."""
    out = {}
    for path in sorted(folder.glob("*/*.json")):
        case = json.loads(path.read_text())
        if form(case["case_id"]) != "cover":
            continue
        d = out.setdefault(case["domain"], {"near_misses": 0, "worded": 0, "examples": []})
        for ref in case["references"]:
            for claim in ref["claims"]:
                d["near_misses"] += 1
                words = worded(str(claim["witness"]))
                if words:
                    d["worded"] += 1
                    if len(d["examples"]) < 8:
                        d["examples"].append(str(claim["witness"]))
    return out


def main():
    rows = []
    for source, folder in (("suite", HERE / "suite" / "cases"), ("policy units", UNITS)):
        for path in sorted(folder.glob("*/*.json")):
            case = json.loads(path.read_text())
            ids = role_ids(case)
            if ids:
                rows.append({"source": source, "case_id": case["case_id"], "form": form(case["case_id"]), "ids": ids})
    summary = {f"{s} / {f}": n for (s, f), n in sorted(Counter((r["source"], r["form"]) for r in rows).items())}
    worded_ids = near_miss_ids(HERE / "suite" / "cases")
    (HERE / "role_ids.json").write_text(json.dumps({"_about": __doc__.split("\n\n")[0], "summary": summary,
                                                    "near_miss_ids_made_of_words": worded_ids, "tests": rows},
                                                   indent=1) + "\n")
    print(json.dumps(summary, indent=1))
    print(json.dumps({d: {k: v for k, v in x.items()} for d, x in worded_ids.items()}, indent=1))


if __name__ == "__main__":
    main()
