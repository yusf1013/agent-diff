"""Where dates live in the adopted scenarios, what depends on the day a test runs, and whether the test's own dates
can be shifted instead of the agent's clock (the PI's question of 2026-10-01). No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.dates_01.kit.inventory

For every Muse scenario in the adopted set (its cover in the run suites): the date-like values in its seed and query,
the date phrases and relative-time words in its request, its clock and the records dated after it; then a shift of
every date by whole weeks (seed, query, witnesses, probes, clock together), checked with the derivation's own
reference check (the target still selected, every near miss still killed by its witness) and compared with the
original derivation's kept and dropped tests. Writes numbers/inventory.json.
"""
from __future__ import annotations

import copy
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.autogen_01.kit import derive
from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.report_01.kit.common import RUNS, load

HERE = Path(__file__).resolve().parents[1]
FOLDERS = [RUNS / "openclaw_eval_01/suite_opaque/cases", RUNS / "completion_01/suite/cases", RUNS / "regen_01/suite/cases"]
CALENDAR_NOW = datetime(2018, 6, 17, 7, 1, tzinfo=timezone.utc)
FIRST_ROUND_RUN_DAY = datetime(2026, 9, 28, 12, 0, tzinfo=timezone.utc)   # full_03/full_04 ran on 09-28/29 on the real clock

ISO_DT = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2})(?::(\d{2})(?:\.(\d+))?)?(Z|[+-]\d{2}:?\d{2})?)?$")
SLACK_TS = re.compile(r"^(\d{10})\.(\d{6})$")
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec"
PROSE_DATE = re.compile(rf"\b({MONTHS})\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?(?:,?\s+(\d{{4}}))?\b|\b(\d{{1,2}})(?:st|nd|rd|th)?\s+({MONTHS})\b(?:,?\s+(\d{{4}}))?")
MONTH_YEAR = re.compile(rf"\b({MONTHS})\.?\s+(\d{{4}})\b")
YEAR = re.compile(r"\b(19\d\d|20\d\d)\b")
WEEKDAY = re.compile(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)s?\b", re.I)
RELATIVE = re.compile(r"\b(today|tonight|tomorrow|yesterday|this week|next week|last week|this month|last month|next month|this morning|this afternoon|"
                      r"overdue|upcoming|past due|due soon|currently|current|right now|recently|most recent(?:ly)?|latest|earliest|oldest|newest|"
                      r"\d+ (?:days?|weeks?|months?|hours?) ago|in \d+ (?:days?|weeks?)|next|last|this)\b", re.I)
CLOCK_WORDS = {"today", "tonight", "tomorrow", "yesterday", "this week", "next week", "last week", "this month", "last month", "next month",
               "this morning", "this afternoon", "overdue", "upcoming", "past due", "due soon", "currently", "current", "right now", "recently"}
MONTH_NUM = {m: i % 12 + 1 for i, m in enumerate("January February March April May June July August September October November December".split())}
MONTH_NUM.update({"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Sept": 9, "Oct": 10, "Nov": 11, "Dec": 12})


def parse_iso(s: str):
    m = ISO_DT.match(s)
    if not m:
        return None
    y, mo, d, hh, mm, ss, frac, tz = m.groups()
    if hh is None:
        return ("date", datetime(int(y), int(mo), int(d)), None)
    dt = datetime(int(y), int(mo), int(d), int(hh), int(mm), int(ss or 0), int((frac or "0")[:6].ljust(6, "0")))
    if tz == "Z":
        return ("dt", dt.replace(tzinfo=timezone.utc), "Z")
    if tz:
        sign = 1 if tz[0] == "+" else -1; hhh, mmm = int(tz[1:3]), int(tz[-2:])
        return ("dt", dt.replace(tzinfo=timezone(sign * timedelta(hours=hhh, minutes=mmm))), tz)
    return ("dt", dt, None)


def walk(x, path=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from walk(v, f"{path}[{i}]")
    else:
        yield path, x


def date_values(obj):
    """(path, kind, instant or None, raw) for every date-like leaf."""
    out = []
    for path, v in walk(obj):
        if isinstance(v, str):
            p = parse_iso(v)
            if p:
                kind, dt, tz = p
                out.append((path, "iso-" + kind + ("-" + (tz if tz == "Z" else "offset") if tz else "-naive" if kind == "dt" else ""), dt, v)); continue
            if SLACK_TS.match(v):
                out.append((path, "slack-ts", datetime.fromtimestamp(float(v), tz=timezone.utc), v))
        elif isinstance(v, bool):
            continue
        elif isinstance(v, int) and 1_400_000_000 <= v <= 2_000_000_000 and path.split(".")[-1].split("[")[0] in ("created", "updated", "ts", "latest", "oldest", "created_ts", "updated_ts", "timestamp"):
            out.append((path, "epoch-s", datetime.fromtimestamp(v, tz=timezone.utc), v))
    return out


def shift_value(v, weeks: int, zone_hint=None):
    """The same date-like value, `weeks` weeks later, in the same spelling; zone-aware offsets re-derived in the stated
    zone so that wall time survives a DST boundary."""
    if isinstance(v, str):
        p = parse_iso(v)
        if p:
            kind, dt, tz = p
            if kind == "date":
                return (dt + timedelta(weeks=weeks)).strftime("%Y-%m-%d")
            if tz is None:
                return (dt + timedelta(weeks=weeks)).strftime("%Y-%m-%dT%H:%M:%S") + (("." + v.split(".")[1]) if "." in v.split("T")[1] else "")
            if tz == "Z":
                return (dt + timedelta(weeks=weeks)).strftime("%Y-%m-%dT%H:%M:%S") + (("." + v.split(".")[1][:-1]) if "." in v.split("T")[1] else "") + "Z"
            if zone_hint:
                z = ZoneInfo(zone_hint)
                local = dt.astimezone(z)
                moved = (local.replace(tzinfo=None) + timedelta(weeks=weeks)).replace(tzinfo=z)   # wall time preserved
                s = moved.isoformat()
                return s if ":" in tz else s.replace("+", "+").replace(moved.strftime("%z")[:3] + ":" + moved.strftime("%z")[3:], moved.strftime("%z"))
            moved = dt + timedelta(weeks=weeks)
            return moved.strftime("%Y-%m-%dT%H:%M:%S") + tz
        if SLACK_TS.match(v):
            a, b = v.split(".")
            return f"{int(a) + weeks * 7 * 86400}.{b}"
        return v
    if isinstance(v, int) and not isinstance(v, bool) and 1_400_000_000 <= v <= 2_000_000_000:
        return v + weeks * 7 * 86400
    return v


def shift_case(case: dict, weeks: int) -> dict:
    zone = None
    for path, v in walk(case.get("seed", {})):
        if path.endswith(".timeZone") and isinstance(v, str) and "/" in v:
            zone = v; break
    def rec(x, key=None):
        if isinstance(x, dict):
            return {k: rec(v, k) for k, v in x.items()}
        if isinstance(x, list):
            return [rec(v, key) for v in x]
        if key in ("timeZone", "id", "case_id") and not (isinstance(x, str) and SLACK_TS.match(x)):
            return x
        return shift_value(x, weeks, zone)
    out = rec(case)
    if out.get("clock"):
        now = datetime.fromisoformat(case["clock"]["now"].replace("Z", "+00:00")) + timedelta(weeks=weeks)
        out["clock"] = {"now": now.strftime("%Y-%m-%dT%H:%M:%SZ")}
    return out


def main():
    rows = []
    totals = Counter()
    for folder in FOLDERS:
        for p in sorted(folder.glob("*/*.json")):
            case = load(p)
            if not re.fullmatch(r"G4-[A-Z]{3}-\d+", case["case_id"]) or rulings.test_exclusion(case):
                continue          # covers only (a cover's id is its scenario's id)
            d = case["domain"]; sid = case["case_id"]
            clock = datetime.fromisoformat(case["clock"]["now"].replace("Z", "+00:00")) if case.get("clock") else (CALENDAR_NOW if d == "calendar" else None)
            clock_source = "test clock" if case.get("clock") else ("Calendar's fixed day" if d == "calendar" else "none (ran on the real clock)")
            ref_now = clock or FIRST_ROUND_RUN_DAY
            seed_dates = date_values(case["seed"])
            query_dates = [x for x in date_values(case["references"][0]["query"])]
            kinds = Counter(k for _, k, _, _ in seed_dates)
            fields = Counter(path.split(".")[-1].split("[")[0] for path, _, _, _ in seed_dates)
            def inst(dt):
                return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
            future = [(path, raw) for path, k, dt, raw in seed_dates if dt and inst(dt) > ref_now]
            creation_future = [(path, raw) for path, raw in future if any(w in path.lower() for w in ("created", "ts", "posted", "updated", "modified"))]
            prompt = case.get("prompt") or ""
            prose = [m.group(0) for m in PROSE_DATE.finditer(prompt)]
            month_year = [m.group(0) for m in MONTH_YEAR.finditer(prompt) if not any(m.group(0) in x for x in prose)]
            years = [m.group(0) for m in YEAR.finditer(prompt)]
            weekdays = [m.group(0) for m in WEEKDAY.finditer(prompt)]
            rel = [m.group(0).lower() for m in RELATIVE.finditer(prompt)]
            clock_rel = [w for w in rel if w in CLOCK_WORDS or w.endswith("ago") or w.startswith("in ")]
            # do the prose month-day phrases map to seed dates?
            seed_md = {(dt.month, dt.day) for _, _, dt, _ in seed_dates if dt}
            mapped, unmapped = [], []
            for m in PROSE_DATE.finditer(prompt):
                mon = m.group(1) or m.group(5); day = m.group(2) or m.group(4)
                (mapped if (MONTH_NUM.get(mon), int(day)) in seed_md else unmapped).append(m.group(0))
            # near-midnight local timestamps (a DST crossing could move them to another local day)
            zone = next((v for path, v in walk(case["seed"]) if path.endswith(".timeZone") and isinstance(v, str) and "/" in v), None) or "America/Los_Angeles"
            near_midnight = 0
            for _, k, dt, _ in seed_dates:
                if dt and dt.tzinfo and k != "iso-date":
                    loc = dt.astimezone(ZoneInfo(zone)); mins = loc.hour * 60 + loc.minute
                    if mins < 60 or mins > 23 * 60:
                        near_midnight += 1
            # the shift: whole weeks that bring the clock to this week; also +4 and +52 weeks
            today = datetime.now(timezone.utc)
            weeks_to_now = max(1, int((today - ref_now).days // 7))
            results = {}
            orig_kept, orig_dropped = derive.suite_with_dropped(copy.deepcopy(case))
            orig_ids = (sorted(t["case_id"] for t, _ in orig_kept), sorted(t["case_id"] for t, _ in orig_dropped))
            for label, w in (("to this week", weeks_to_now), ("+4 weeks", 4), ("+52 weeks", 52)):
                shifted = shift_case(case, w)
                _, errors = derive._finish(copy.deepcopy(shifted))
                try:
                    kept, dropped = derive.suite_with_dropped(copy.deepcopy(shifted))
                    same = (sorted(t["case_id"] for t, _ in kept), sorted(t["case_id"] for t, _ in dropped)) == orig_ids
                except Exception as e:
                    same, errors = False, errors + [f"derivation: {type(e).__name__}: {e}"]
                results[label] = {"weeks": w, "cover_check_errors": errors, "same_tests_kept_and_dropped": same}
            row = {"scenario": sid, "domain": d, "clock": clock.isoformat() if clock else None, "clock_source": clock_source,
                   "seed_dates": len(seed_dates), "seed_date_kinds": dict(kinds), "seed_date_fields": dict(fields.most_common(8)),
                   "query_dates": [(path, raw) for path, _, _, raw in query_dates],
                   "future_dated_values": len(future), "future_dated_creation_fields": creation_future[:6],
                   "prompt_prose_dates": prose, "prompt_prose_dates_mapped_to_seed": mapped, "prompt_prose_dates_unmapped": unmapped,
                   "prompt_month_year": month_year, "prompt_years": years, "prompt_weekdays": weekdays, "prompt_relative_words": rel,
                   "prompt_clock_dependent_words": clock_rel, "near_midnight_timestamps": near_midnight, "shift": results}
            rows.append(row)
            totals["scenarios"] += 1
            totals["with seed dates"] += bool(seed_dates); totals["with query dates"] += bool(query_dates)
            totals["with future-dated creation fields"] += bool(creation_future); totals["with future-dated values"] += bool(future)
            totals["with prose dates in the request"] += bool(prose); totals["prose dates mapped"] += len(mapped); totals["prose dates unmapped"] += len(unmapped)
            totals["with month-year in the request"] += bool(month_year); totals["with weekday in the request"] += bool(weekdays)
            totals["with clock-dependent words"] += bool(clock_rel); totals["with near-midnight timestamps"] += bool(near_midnight)
            for label, r in results.items():
                totals[f"shift {label}: cover check clean"] += not r["cover_check_errors"]
                totals[f"shift {label}: same tests kept and dropped"] += r["same_tests_kept_and_dropped"]
    # the policy units' requests (the drop-F variants are reworded by the writer): prose dates mapped to their seed
    unit_rows = []
    for folder in (RUNS / "openclaw_eval_01/suite_opaque/units", RUNS / "completion_01/suite/units", RUNS / "regen_01/suite/units"):
        for p in sorted(folder.glob("*/*.json")):
            u = load(p)
            if not re.search(r"-G4-", u["case_id"]) or rulings.test_exclusion(u):
                continue
            prompt = u.get("prompt") or ""
            seed_md = {(dt.month, dt.day) for _, _, dt, _ in date_values(u["seed"]) if dt}
            mapped, unmapped = [], []
            for m in PROSE_DATE.finditer(prompt):
                mon = m.group(1) or m.group(5); day = m.group(2) or m.group(4)
                (mapped if (MONTH_NUM.get(mon), int(day)) in seed_md else unmapped).append(m.group(0))
            if mapped or unmapped or MONTH_YEAR.search(prompt):
                unit_rows.append({"unit": u["case_id"], "mapped": mapped, "unmapped": unmapped, "month_year": MONTH_YEAR.findall(prompt)})
    totals["units with prose dates"] = len(unit_rows); totals["unit prose dates unmapped"] = sum(len(r["unmapped"]) for r in unit_rows)
    (HERE / "numbers/inventory.json").write_text(json.dumps({"totals": dict(totals), "scenarios": rows, "units_with_prose_dates": unit_rows}, indent=1, default=str) + "\n")
    print(json.dumps(dict(totals), indent=1))
    by_domain = defaultdict(Counter)
    for r in rows:
        by_domain[r["domain"]]["scenarios"] += 1
        for k, v in r["seed_date_kinds"].items(): by_domain[r["domain"]][k] += v
        by_domain[r["domain"]]["future-dated creation fields (scenarios)"] += bool(r["future_dated_creation_fields"])
        by_domain[r["domain"]]["prose dates (scenarios)"] += bool(r["prompt_prose_dates"])
        by_domain[r["domain"]]["clock words (scenarios)"] += bool(r["prompt_clock_dependent_words"])
        by_domain[r["domain"]]["weekday (scenarios)"] += bool(r["prompt_weekdays"])
    for d, c in by_domain.items(): print(d, dict(c))
    print("\nclock-dependent words:", [(r["scenario"], r["prompt_clock_dependent_words"]) for r in rows if r["prompt_clock_dependent_words"]])
    print("\nfuture-dated creation fields:", [(r["scenario"], r["clock_source"], r["future_dated_creation_fields"][:2]) for r in rows if r["future_dated_creation_fields"]])
    print("\nunmapped prose dates:", [(r["scenario"], r["prompt_prose_dates_unmapped"], r["prompt_month_year"]) for r in rows if r["prompt_prose_dates_unmapped"] or r["prompt_month_year"]])
    print("\nshift failures:", [(r["scenario"], label, x["cover_check_errors"][:2], x["same_tests_kept_and_dropped"]) for r in rows for label, x in r["shift"].items() if x["cover_check_errors"] or not x["same_tests_kept_and_dropped"]][:12])


if __name__ == "__main__":
    main()
