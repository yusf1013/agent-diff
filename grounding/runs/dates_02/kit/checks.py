"""Does a rendered test stay the same test on any day it runs? Three mechanical checks over the templates of build.py,
on every run day from 2026-10-03 for two years (731 days; it crosses 2027-28 and the leap day 2028-02-29). No model
calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.dates_02.kit.checks

1. **Same tests.** For every scenario, the cover rendered on a run day is derived again with the frozen derivation
   (`autogen_01/kit/derive.suite_with_dropped`): its reference check must stay clean (the target the only record
   selected, every near miss killed by its witness), the same probes must be kept and dropped, and each derived probe
   must equal the original probe rendered on that day (rendering commutes with the derivation). On 61 run days: every
   day of the first fortnight, then every day that crosses a month end, a DST change, the year end or the leap day.
2. **Calendar groupings kept.** A phrase that names a month or a year without a day ("created in March", "set up in
   March 2024", "the 2018 cohort") selects by calendar month or year, which a shift of whole days does not keep: a date
   near a month's end can cross into the next. For every such phrase, the records dated in the named month (or year)
   must be the same records on every run day, and none may join them. Also: a date written without a year ("June 8")
   must stay within half a year of the run day, so that its nearest reading is still the right one; a weekday in a
   request ("on Thursday") must name a day one to six days ahead of the run day, so that its next occurrence is the
   target's day.
3. **No record from the future.** Every timestamp of something done (created, updated, posted, completed, ...) must lie
   before the run's moment, for runs at 00:05 and at 23:55 local time.

Writes numbers/checks.json.
"""
from __future__ import annotations

import copy
import json
import re
from collections import Counter, defaultdict
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.autogen_01.kit import derive
from grounding.runs.dates_02.kit import templates
from grounding.runs.report_01.kit.common import RUNS, load

HERE = Path(__file__).resolve().parents[1]
FIRST_RUN_DAY = date(2026, 10, 3)
HORIZON = 731
MONTH_ONLY = re.compile(r"\{(Month|MONTH|month|Mon|Sept)\}")
DAY_FIELD = re.compile(r"\{d\}")
YEAR_FIELD = re.compile(r"\{yyyy\}")


def run_days_sample() -> list[date]:
    days = [FIRST_RUN_DAY + timedelta(days=i) for i in range(14)]
    for i in range(14, HORIZON):
        d = FIRST_RUN_DAY + timedelta(days=i)
        nxt = d + timedelta(days=1)
        la = ZoneInfo("America/Los_Angeles")
        dst = datetime.combine(d, time(12), la).utcoffset() != datetime.combine(nxt, time(12), la).utcoffset()
        if nxt.month != d.month or d.month != (d - timedelta(days=1)).month or dst or (d.month, d.day) in ((12, 31), (1, 1), (2, 28), (2, 29), (3, 1)):
            days.append(d)
    return days


def shift_for(template: dict, run_day: date) -> int:
    return (run_day - date.fromisoformat(template["dates"]["anchor"]["day"])).days


def plain(case: dict) -> dict:
    return {k: v for k, v in case.items() if k not in ("case_sha256", "dates", "clock")}


# ---------------------------------------------------------------- 1. same tests


def check_derivation(cover_t: dict, probe_ts: dict[str, dict], days: list[date]) -> dict:
    orig = templates.render(cover_t, date.fromisoformat(cover_t["dates"]["anchor"]["day"]))
    k0, d0 = derive.suite_with_dropped(copy.deepcopy(plain(orig)))
    ids0 = (sorted(t["case_id"] for t, _ in k0), sorted(t["case_id"] for t, _ in d0))
    out = {"days": len(days), "failures": []}
    for day in days:
        cover = plain(templates.render(cover_t, day))
        _, errors = derive._finish(copy.deepcopy(cover))
        kept, dropped = derive.suite_with_dropped(copy.deepcopy(cover))
        ids = (sorted(t["case_id"] for t, _ in kept), sorted(t["case_id"] for t, _ in dropped))
        problems = []
        if errors:
            problems.append(f"reference check: {errors[:2]}")
        if ids != ids0:
            problems.append("different probes kept or dropped")
        for t, _ in kept:
            if t["case_id"] in probe_ts and t["case_id"] != cover_t["case_id"]:
                want = plain(templates.render(probe_ts[t["case_id"]], day))
                if plain(t) != want:
                    diff = [p for (p, a), (q, b) in zip(templates.walk(plain(t)), templates.walk(want)) if a != b][:3]
                    problems.append(f"{t['case_id']} differs from its rendered template at {diff}")
        if problems:
            out["failures"].append({"run_day": day.isoformat(), "problems": problems})
    return out


# ---------------------------------------------------------------- 2. calendar groupings


def data_days(case: dict, ctx_frame: str, anchor_day: date, domain: str) -> list[tuple[str, date]]:
    """(path, local day) of every timestamp or date in the test's data, in the frame templates.py shifts it in."""
    ctx = templates.Context(anchor_day, "", domain, ctx_frame,
                            sorted({v for p, v in templates.walk(case["seed"]) if isinstance(v, str)
                                    and p.split(".")[-1] in ("timeZone", "time_zone") and "/" in v}))
    out = []
    for p, v in walk_indexed(case["seed"]):
        if isinstance(v, str) and (templates.ISO_FULL.match(v) or (domain == "slack" and templates.SLACK_TS.match(v))):
            out.append((p, templates.local_day(v, ctx)))
    return out


def walk_indexed(x, path=""):
    """Like templates.walk, with list indices in the path, so that each value has its own path."""
    if isinstance(x, dict):
        for k, v in x.items():
            yield from walk_indexed(v, f"{path}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from walk_indexed(v, f"{path}[{i}]")
    else:
        yield path, x


def tokens_in(template: dict):
    for p, v in templates.walk(template):
        if isinstance(v, str):
            for m in templates.TOKEN.finditer(v):
                yield p, m.group(1), v


def date_filters(case: dict) -> list[tuple[str, str, list]]:
    """(table, field, [(op, value)]) of every date filter in the test's reference queries."""
    out = []

    def rec(node):
        conds = defaultdict(list)
        for f in node.get("filters") or []:
            v = f.get("value")
            if isinstance(v, str) and templates.ISO_FULL.match(v):
                conds[f["field"]].append((f.get("op"), v))
        for field, c in conds.items():
            out.append((node.get("table"), field, c))
        for e in node.get("edges") or []:
            rec(e.get("node") or {})
    for r in case["references"]:
        rec(r.get("query") or {})
    return out


def check_groupings(template: dict, original: dict, days_all: list[date]) -> list[dict]:
    """For every phrase in the request that names a month without a day and is a condition (a reference query filters
    a date field on a range holding that month), the records whose filtered field falls in the named month must be the
    same on every run day, under the scenario's shift."""
    anchor = template["dates"]["anchor"]
    anchor_day = date.fromisoformat(anchor["day"])
    mode = template["dates"].get("mode", "day")
    frame = anchor["zone"] if original["domain"] == "calendar" else "UTC"
    ctx = templates.Context(anchor_day, "", original["domain"], frame,
                            sorted({v for p, v in templates.walk(original["seed"]) if isinstance(v, str)
                                    and p.split(".")[-1] in ("timeZone", "time_zone") and "/" in v}))
    filters = date_filters(original)
    problems = []
    for m in templates.TOKEN.finditer(template.get("prompt", "")):
        kind, *parts = m.group(1).split("|")
        if kind != "P":
            continue
        k, f = int(parts[0]), "|".join(parts[1:])
        if not MONTH_ONLY.search(f) or DAY_FIELD.search(f):
            continue
        bound = anchor_day + timedelta(days=k)
        hit = None
        for table, field, conds in filters:
            days = [templates.local_day(v, ctx) for _, v in conds]
            if any((d.year, d.month) == (bound.year, bound.month) for d in days):
                hit = (table, field)
        if hit is None:
            problems.append({"token": m.group(1), "problem": "names a month, but no date filter of the reference query covers it"})
            continue
        table, field = hit
        values = [(i, templates.local_day(row[field], ctx)) for i, row in enumerate(original["seed"].get(table, []))
                  if isinstance(row.get(field), str) and templates.ISO_FULL.match(row[field])]
        members0 = {i for i, d in values if (d.year, d.month) == (bound.year, bound.month)}
        bad = []
        for run_day in days_all:
            sh = templates.Shift(anchor_day, run_day, mode)
            b2 = sh.day(k)
            members = {i for i, d in values if (lambda x: (x.year, x.month))(sh.day((d - anchor_day).days)) == (b2.year, b2.month)}
            if members != members0:
                bad.append(run_day.isoformat())
        problems.append({"token": m.group(1), "text_at_anchor": templates.fmt_date(bound, f), "condition": f"{table}.{field}",
                         "records_in_it": len(members0), "mode": mode, "run_days_broken": len(bad), "first_broken": bad[:5]})
    return [p for p in problems if p.get("run_days_broken", 1)]


def weekday_in_request(template: dict, original: dict) -> list[dict]:
    """A weekday in the request should name a day 1-6 days ahead of the anchor (the target's day), so that on any run
    day its next occurrence is the target's."""
    anchor_day = date.fromisoformat(template["dates"]["anchor"]["day"])
    frame = template["dates"]["anchor"]["zone"] if original["domain"] == "calendar" else "UTC"
    expected = {str(x) for r in original["references"] for x in r.get("expected", [])}
    target_days = set()
    ctx = templates.Context(anchor_day, "", original["domain"], frame,
                            sorted({v for p, v in templates.walk(original["seed"]) if isinstance(v, str)
                                    and p.split(".")[-1] in ("timeZone", "time_zone") and "/" in v}))
    for rows in original["seed"].values():
        for row in rows if isinstance(rows, list) else []:
            if any(isinstance(v, (str, int)) and str(v) in expected for v in row.values()):
                for p, v in templates.walk(row):
                    if isinstance(v, str) and templates.ISO_FULL.match(v) and p.split(".")[-1] in ("dateTime", "date", "start_datetime", "start_date"):
                        target_days.add(templates.local_day(v, ctx))
    out = []
    for m in templates.TOKEN.finditer(template["prompt"]):
        kind, *parts = m.group(1).split("|")
        if kind != "W":
            continue
        j = int(parts[0])
        hits = sorted((d - anchor_day).days for d in target_days if (d - anchor_day).days % 7 == j % 7)
        out.append({"weekday_offset": j, "target_day_offsets": hits,
                    "ok": bool(hits) and all(1 <= h <= 6 for h in hits) if expected else None})
    return out


# ---------------------------------------------------------------- 3. no record from the future


def future_events(template: dict, original: dict) -> dict:
    """The latest timestamp of something done, as an offset from the anchor day's local midnight; a record is from the
    future on a run when it is later than the run's moment."""
    anchor = template["dates"]["anchor"]
    zone = ZoneInfo(anchor["zone"])
    anchor_day = date.fromisoformat(anchor["day"])
    latest, where = None, None
    for p, v in templates.walk(original["seed"]):
        key = p.split(".")[-1].replace("[]", "")
        if not isinstance(v, str) or not templates.EVENT_FIELD.match(key):
            continue
        if templates.SLACK_TS.match(v):
            inst = datetime.fromtimestamp(float(v), timezone.utc)
        elif templates.ISO_FULL.match(v) and "T" in v or (templates.ISO_FULL.match(v) and " " in v):
            s = v.replace(" ", "T").replace("Z", "+00:00")
            inst = datetime.fromisoformat(s)
            if inst.tzinfo is None:
                inst = inst.replace(tzinfo=timezone.utc)
        else:
            continue
        if latest is None or inst > latest:
            latest, where = inst, p
    if latest is None:
        return {"latest_event": None}
    midnight = datetime.combine(anchor_day, time(0), zone)
    hours = (latest - midnight).total_seconds() / 3600
    # rendered on run day D, the event lands `hours` after D's midnight (whole days kept); a run at 00:05 sees it
    # in the future when hours > 0.08, a run at 23:55 when hours > 23.9
    return {"latest_event": latest.isoformat(), "field": where, "hours_after_anchor_midnight": round(hours, 2),
            "future_for_a_run_at_00:05": hours > 5 / 60, "future_for_a_run_at_23:55": hours > 23 + 55 / 60}


def main():
    build = load(HERE / "numbers/build.json")["tests"]
    days_sample = run_days_sample()
    days_all = [FIRST_RUN_DAY + timedelta(days=i) for i in range(HORIZON)]
    by_scenario = defaultdict(list)
    for t in build:
        by_scenario[t["scenario"]].append(t)
    pop = {r["test"]: r for r in load(HERE / "numbers/population.json")}
    result = {"run_days_sampled": [d.isoformat() for d in days_sample], "scenarios": {}, "tests": {}}
    totals = Counter()
    for scenario, members in sorted(by_scenario.items()):
        tmpl = {m["test"]: load(RUNS / m["template"]) for m in members}
        entry = {}
        if scenario.startswith("G4-") or scenario.startswith("AP"):
            cover_t = tmpl.get(scenario)
            if cover_t is None:   # a by-product's scenario whose cover is not in the tables: template it alongside
                from grounding.runs.dates_02.kit.build import cover_of
                from grounding.runs.dates_02.kit import anchors
                cover = cover_of(scenario, [])
                a = anchors.anchor_for(scenario, cover["domain"], cover)
                ctx = templates.context_for(cover, a.day, a.zone)
                cover_t, _ = templates.make(cover, ctx)
                cover_t["dates"] = {"anchor": a.as_dict()}
            probes = {k: v for k, v in tmpl.items() if not k.startswith(("AT-", "U-", "UC-"))}
            entry["derivation"] = check_derivation(cover_t, probes, days_sample)
            totals["scenarios checked by derivation"] += 1
            totals["scenarios whose derivation holds on every sampled day"] += not entry["derivation"]["failures"]
        for m in members:
            original = load(RUNS / pop[m["test"]]["path"])
            g = check_groupings(tmpl[m["test"]], original, days_all)
            w = weekday_in_request(tmpl[m["test"]], original)
            f = future_events(tmpl[m["test"]], original)
            result["tests"][m["test"]] = {"scenario": scenario, "kind": m["kind"], "groupings": g, "weekdays": w, "future": f}
            totals["tests"] += 1
            totals["tests with a month condition broken on some run day"] += bool(g)
            totals["tests with a request weekday not 1-6 days ahead"] += any(x["ok"] is False for x in w)
            totals["tests with an event after the anchor day's 00:05"] += bool(f.get("future_for_a_run_at_00:05"))
            totals["tests with an event after the anchor day's 23:55"] += bool(f.get("future_for_a_run_at_23:55"))
        result["scenarios"][scenario] = entry
    result["totals"] = dict(totals)
    (HERE / "numbers/checks.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps(dict(totals), indent=1))
    for s, e in result["scenarios"].items():
        if e.get("derivation", {}).get("failures"):
            print("DERIVATION", s, e["derivation"]["failures"][:2])
    seen = set()
    for t, e in result["tests"].items():
        for g in e["groupings"]:
            k = (e["scenario"], g.get("token"))
            if k not in seen:
                seen.add(k); print("MONTH CONDITION", e["scenario"], t, g)
        for w in e["weekdays"]:
            if w["ok"] is False and (e["scenario"], "w") not in seen:
                seen.add((e["scenario"], "w")); print("WEEKDAY", e["scenario"], t, w)
        if e["future"].get("future_for_a_run_at_00:05") and (e["scenario"], "f") not in seen:
            seen.add((e["scenario"], "f")); print("FUTURE", e["scenario"], t, e["future"])


if __name__ == "__main__":
    main()
