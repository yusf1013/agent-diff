"""Template every test behind the denominator tables, and check two things on each one. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.dates_02.kit.build

1. **Identity:** rendered on its anchor day, the template gives back the test exactly (apart from the old `clock`).
2. **Residue:** rendered with every token blanked out, nothing date-like is left: no ISO date, Slack timestamp,
   month name with a day or year, weekday, or year. What is left is listed, with why it stays as written.

One context per scenario (its anchor and its phrase bindings) is built from the scenario's cover and shared by the
scenario's probes and policy units, so that a phrase renders the same way in all of them; a boundary test is its own
scenario. Writes the templates to suite/ (cases/, units/, boundary/ by domain), numbers/build.json (per test:
anchor, tokens by kind, identity, residue) and numbers/bindings.json (per scenario: each phrase's day and why).
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.dates_02.kit import anchors, templates
from grounding.runs.dates_02.kit.population import CASE_FOLDERS
from grounding.runs.report_01.kit.common import RUNS, load

HERE = Path(__file__).resolve().parents[1]
SUITE = HERE / "suite"
RESIDUE = re.compile(
    rf"(?P<iso>\d{{4}}-\d{{2}}-\d{{2}})|(?P<ts>\b\d{{10}}\.\d{{6}}\b)"
    rf"|(?P<md>\b(?:{templates.MON_RE})\.?\s+\d{{1,2}}(?!\d))|(?P<my>\b(?:{templates.MON_RE})\.?\s+\d{{4}})"
    rf"|(?P<month>\b(?:{'|'.join(templates.MONTHS)})\b)|(?P<weekday>\b(?:{templates.WD_RE})s?\b)"
    r"|(?P<year>(?<![\w$#.])(?:19[5-9]\d|20[0-4]\d)(?![\w]))")
WHY_LEFT = {"weekday": "a recurring weekday (plural) or a weekday setting", "month": "a month name without a preposition"}


def cover_of(scenario: str, rows: list[dict]) -> dict:
    for r in rows:
        if r["test"] == scenario:
            return load(RUNS / r["path"])
    hits = [p for f in CASE_FOLDERS for p in f.glob(f"*/{scenario}.json")]
    if len(hits) != 1:
        raise SystemExit(f"{scenario}: cover not found ({hits})")
    return load(hits[0])


def strip(case: dict) -> dict:
    return {k: v for k, v in case.items() if k not in ("clock", "dates")}


def residue(template: dict) -> list[dict]:
    blank = templates.render(template, templates.date.fromisoformat(template["dates"]["anchor"]["day"]), mark="§")
    out = []
    for path, v in templates.walk(strip(blank)):
        if not isinstance(v, str) or path.endswith("case_sha256"):
            continue
        key = path.split(".")[-1].replace("[]", "")
        for m in RESIDUE.finditer(v):
            kind = m.lastgroup
            if templates.ID_KEYS.match(key) and kind in ("year", "month", "weekday", "md", "my"):
                continue
            out.append({"path": path, "kind": kind, "text": m.group(0), "context": v[max(0, m.start() - 50):m.end() + 50]})
    return out


def main():
    rows = load(HERE / "numbers/population.json")
    by_scenario = defaultdict(list)
    for r in rows:
        by_scenario[r["scenario"]].append(r)
    report, binding_report = [], {}
    totals = Counter()
    for scenario, members in sorted(by_scenario.items()):
        cover = cover_of(scenario, members) if not scenario.startswith("BDA-") else load(RUNS / members[0]["path"])
        domain = cover["domain"]
        anchor = anchors.anchor_for(scenario, domain, cover)
        ctx = templates.context_for(cover, anchor.day, anchor.zone)
        # the cover first, so that its phrases fix the bindings its probes and units reuse
        order = sorted(members, key=lambda r: (r["test"] != scenario, r["test"]))
        cover_t, _ = templates.make(cover, ctx)
        mode = templates.mode_for(cover_t, ctx)
        totals[f"scenarios (a boundary test is its own): mode {mode}"] += 1
        for r in order:
            case = load(RUNS / r["path"])
            t, found = templates.make(case, ctx)
            t["dates"] = {"anchor": anchor.as_dict(), "mode": mode}
            back = templates.render(t, anchor.day)
            identical = strip(back) == strip(case)
            if not identical:
                diffs = [p for (p, a), (q, b) in zip(templates.walk(strip(back)), templates.walk(strip(case))) if a != b][:5]
            left = residue(t)
            folder = {"boundary": "boundary"}.get(r["kind"], "units" if r["kind"] in ("absence", "underspecified", "by-product unit") else "cases")
            out = SUITE / folder / domain / f"{r['test']}.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n")
            kinds = Counter(f["kind"] for f in found if f["token"])
            report.append({"test": r["test"], "scenario": scenario, "kind": r["kind"], "group": r["group"], "domain": domain,
                           "anchor": anchor.as_dict(), "tokens": dict(kinds), "tokens_total": sum(kinds.values()),
                           "left_as_written": [{"kind": f["kind"], "text": f["text"], "path": f["path"]} for f in found if not f["token"]],
                           "identity": identical, "identity_diffs": [] if identical else diffs, "residue": left,
                           "template": str(out.relative_to(RUNS))})
            totals["tests"] += 1
            totals["identical"] += identical
            totals["with residue"] += bool(left)
            totals["tokens"] += sum(kinds.values())
            for k, n in kinds.items():
                totals[f"tokens: {k}"] += n
        binding_report[scenario] = {"anchor": anchor.as_dict(), "mode": mode, "bindings": {" ".join(map(str, k)): {"day": v[0], "how": v[1]} for k, v in ctx.bindings.items()},
                                    "notes": ctx.notes}
    (HERE / "numbers/build.json").write_text(json.dumps({"totals": dict(totals), "tests": report}, indent=1, ensure_ascii=False) + "\n")
    (HERE / "numbers/bindings.json").write_text(json.dumps(binding_report, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(dict(totals), indent=1))
    bad = [x for x in report if not x["identity"]]
    print("not identical:", len(bad), [(x["test"], x["identity_diffs"][:3]) for x in bad[:8]])
    res = Counter((x["kind"], x2["kind"], x2["text"]) for x in report for x2 in x["residue"])
    print("residue (kind of test, kind, text):", res.most_common(40))


if __name__ == "__main__":
    main()
