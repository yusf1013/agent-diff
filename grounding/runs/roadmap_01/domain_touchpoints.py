"""The mechanical half of the domain-knowledge audit: in every code file the automated pipeline uses, the lines that
name a domain, one of its tables, or a domain-specific field. Reads files only.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.roadmap_01.domain_touchpoints

Writes domain_touchpoints.json: per file, its size and the domain-specific lines (line number, text, domains named).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
G = HERE.parents[1]
FILES = {
    # generation, checks and derivation (autogen_01's kit, reused by autogen_02)
    "generation": ["runs/autogen_01/kit/orchestrate.py", "runs/autogen_01/kit/scenario.py",
                   "runs/autogen_01/kit/seedops.py", "runs/autogen_01/kit/preflight.py",
                   "runs/autogen_01/kit/derive.py", "runs/autogen_01/kit/check_cases.py",
                   "runs/autogen_01/kit/check_derived.py", "runs/autogen_01/kit/check_effects.py",
                   "runs/autogen_01/kit/check_nested.py", "runs/autogen_01/kit/check_attachments.py",
                   "runs/autogen_01/kit/reader.py", "runs/autogen_02/kit/generate.py"],
    "inputs": ["runs/autogen_01/inputs/make_facts.py", "runs/autogen_01/inputs/make_briefs.py",
               "runs/autogen_01/inputs/make_api.py", "runs/autogen_02/inputs/make_briefs4.py"],
    "fact checks (fdc)": ["runs/fact_coverage_01/pilot/common.py", "runs/fact_coverage_01/fdc.py"],
    "policy variants": ["runs/autogen_02/kit/policy.py", "runs/autogen_02/kit/variants2.py",
                        "runs/autogen_02/kit/reader2.py", "runs/autogen_02/kit/population.py",
                        "runs/autogen_02/kit/sampler.py", "runs/autogen_02/kit/check_derivable.py"],
    "judging": ["runs/autogen_01/kit/judge.py", "runs/autogen_01/kit/bundle.py", "runs/autogen_02/kit/judge2.py"],
    "runner": ["integrations/agentdiff/smoke_runtime.py", "integrations/agentdiff/custom_runtime.py",
               "integrations/agentdiff/runtime.py", "runs/fact_coverage_01/pilot/run.py",
               "runs/fact_coverage_02/run.py"],
}
DOMAIN_WORDS = {
    "box": r"\bbox\b|box_[a-z_]+|\bBox\b",
    "calendar": r"\bcalendar\b|calendar_[a-z_]+|\bCalendar\b|google-calendar",
    "linear": r"\blinear\b|\bLinear\b|\bissues?\b|workflow_states|project_milestones|issue_label",
    "slack": r"\bslack\b|\bSlack\b|\bmessages\b|message_reactions|\bchannels?\b|\bts\b|thread_ts",
}


def main():
    out = {}
    for group, files in FILES.items():
        for rel in files:
            p = G / rel
            if not p.exists():
                out[rel] = {"group": group, "missing": True}
                continue
            lines = p.read_text().splitlines()
            hits = []
            for i, line in enumerate(lines, 1):
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                named = [d for d, rx in DOMAIN_WORDS.items() if re.search(rx, line)]
                if named:
                    hits.append({"line": i, "domains": named, "text": s[:160]})
            out[rel] = {"group": group, "lines": len(lines), "domain_lines": len(hits),
                        "by_domain": {d: sum(d in h["domains"] for h in hits) for d in DOMAIN_WORDS}, "hits": hits}
    (HERE / "domain_touchpoints.json").write_text(json.dumps(out, indent=1) + "\n")
    for rel, r in out.items():
        if r.get("missing"):
            print(f"MISSING {rel}")
            continue
        print(f"{r['group']:18} {rel:55} {r['lines']:5d} lines, {r['domain_lines']:4d} domain-specific  {r['by_domain']}")


if __name__ == "__main__":
    main()
