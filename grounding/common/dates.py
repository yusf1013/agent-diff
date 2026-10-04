"""Dates as templates: every date in a test held as an offset from its anchor day, rendered from the real day.

Shifting the agent's clock to fit a test's hard-coded dates is discontinued (the PI, 2026-10-03; grounding/AGENTS.md,
"Dates: never change the agent's clock"). A test's dates move instead: grounding/runs/dates_02 templated every test
behind the denominator tables with `make` and verified the templates; the runners call `for_run` when they create a
test's environment.

`make(case, ctx)` replaces every date in a test (its data, request, reference queries, near-miss explanations, cards
and task specification) with a token; `render(template, run_day)` fills the tokens in for a run on `run_day`. Every
value moves by the same number of days, Δ = run_day - anchor day, so the order of records, the days between them and
their times of day are kept, and the world stands to the run day as it stood to the anchor day. Rendering on the anchor
day gives the test back exactly (checks.py verifies this on every test).

Tokens (between ⟦ and ⟧; k is a day offset from the anchor day):
- `D|k`                         an ISO date, YYYY-MM-DD.
- `T|k|HH:MM:SS.ffffff|frame|out|sep,secs,frac`   a timestamp: wall time `HH:MM:SS.ffffff` on day k in `frame`
  (an IANA zone, `UTC`, `naive`, or `fixed±HH:MM`), written out as `naive`, `Z` (UTC) or `off`/`offnc` (the frame's
  offset at that instant, with or without the colon).
- `S|k|HH:MM:SS|suffix`        a Slack message timestamp (epoch seconds of that UTC wall time, then `.suffix`).
- `P|k|format`                 a date written in words, e.g. `P|-15|{Month} {d}{th}` -> "September 15th".
- `W|j|format`                 a weekday name, j days after the run day's weekday (`{Weekday}`, `{Wkd}`).
- `U|k|HH:MM:SS|zone|format`   the UTC clock time of a local wall time on day k (Calendar explanations).

Words in a format: {Month}/{MONTH}/{month} the month's name in that case, {Mon} its three-letter abbreviation,
{Sept} the four-letter "Sept" style, {d} the day, {th} its ordinal suffix, {yyyy} the year, {Weekday}/{weekday}/
{WEEKDAY}, {Wkd}, {HH}, {MM}.

Left as written (reported by `residue`): recurring weekdays ("on Fridays"), weekday settings
(`projectUpdateRemindersDay`), words relative to now ("tomorrow", "overdue", "next week": they are already relative),
quarters and seasons, times of day (wall time is kept), and anything a check flags.
"""
from __future__ import annotations

import calendar
import copy
import json
import re
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo

OPEN, CLOSE = "⟦", "⟧"
TOKEN = re.compile("⟦([^⟦⟧]*)⟧")
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
MON_ABBR = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Sept": 9,
            "Oct": 10, "Nov": 11, "Dec": 12}
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]   # date.weekday() order
WD_ABBR = {"Mon": 0, "Tue": 1, "Tues": 1, "Wed": 2, "Thu": 3, "Thur": 3, "Thurs": 3, "Fri": 4, "Sat": 5, "Sun": 6}

MON_RE = "|".join(MONTHS + sorted(MON_ABBR, key=len, reverse=True))
WD_RE = "|".join(WEEKDAYS)
ISO_FULL = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:([T ])(\d{2}):(\d{2})(?::(\d{2}))?(\.\d+)?(Z|[+-]\d{2}:?\d{2})?)?$")
SLACK_TS = re.compile(r"^(\d{10})\.(\d{6})$")
PHRASE = re.compile(
    r"(?P<iso>(?<![\w.-])\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2})?(?:\.\d+)?(?:Z|[+-]\d{2}:?\d{2})?)?(?![\w-]))"
    r"|(?P<ts>(?<![\w.])\d{10}\.\d{6}(?![\w.]))"
    r"|(?P<utc>\b(?P<uh>\d{1,2}):(?P<um>\d{2})(?= UTC\b))"
    rf"|(?P<wdmd>\b(?P<wdmd_w>{WD_RE}),?\s+(?P<wdmd_m>{MON_RE})(?P<wdmd_dot>\.?)\s+(?P<wdmd_d>\d{{1,2}})(?P<wdmd_th>st|nd|rd|th)?(?!\d)(?:(?P<wdmd_ys>,?\s+)(?P<wdmd_y>\d{{4}})(?!\d))?)"
    rf"|(?P<md>\b(?P<md_m>{MON_RE})(?P<md_dot>\.?)\s+(?P<md_d>\d{{1,2}})(?P<md_th>st|nd|rd|th)?(?![\d:])(?:(?P<md_ys>,?\s+)(?P<md_y>\d{{4}})(?!\d))?)"
    rf"|(?P<wdthe>\b(?P<wdthe_w>{WD_RE})\s+the\s+(?P<wdthe_d>\d{{1,2}})(?P<wdthe_th>st|nd|rd|th)\b)"
    rf"|(?P<my>\b(?P<my_m>{MON_RE})(?P<my_dot>\.?)\s+(?P<my_y>\d{{4}})(?!\d))"
    r"|(?P<onnth>\bon\s+the\s+(?P<onnth_d>\d{1,2})(?P<onnth_th>st|nd|rd|th)\b)"
    rf"|(?P<wd>\b(?P<wd_w>{WD_RE})(?![A-Za-z]))"
    rf"|(?P<mon2>\b(?P<mon2_m>{'|'.join(MONTHS)})(?![\w])(?!\s+\d))"
    rf"|(?P<mon>\b(?P<mon_pre>in|of|since|from|until|by|during|early|late|mid|before|after|through)(?P<mon_sp>[ -])(?P<mon_m>{'|'.join(MONTHS)})(?![\w])(?!\s+\d))"
    r"|(?P<yr>(?<![\w$#.])(?P<yr_y>19[5-9]\d|20[0-4]\d)(?![\w]))")

# Keys whose values are identifiers, hashes or settings: only whole-value timestamps (Slack message ids) are templated.
ID_KEYS = re.compile(r"^(id|.*_id|.*Id|ids|etag|ical_uid|case_sha256|url|.*Url|slugId|key|expected|witness|keep|"
                     r"target|record_id|Referent set|initiativeUpdateRemindersDay|projectUpdateRemindersDay|color|"
                     r"requirement|fact|coverage_claims|isolated_requirement|variant_of|case_id|_arm|named|element|"
                     r"Test ID)$")
EVENT_FIELD = re.compile(r"^(created|updated|modified|completed|canceled|cancelled|archived|resolved|trashed|deleted|"
                         r"edited|started|last_?seen|lastSeen|content_created|content_modified|added|assigned|joined|"
                         r"ts|message_id)(_at|At)?$", re.I)


def case_style(word: str) -> str:
    return "upper" if word.isupper() and len(word) > 1 else "title" if word[:1].isupper() else "lower"


def styled(word: str, style: str) -> str:
    return word.upper() if style == "upper" else word.lower() if style == "lower" else word


def month_number(name: str) -> int:
    name = name.rstrip(".")
    return MONTHS.index(name) + 1 if name in MONTHS else MON_ABBR[name]


def month_code(name: str) -> str:
    """The format placeholder that writes a month the way `name` is written."""
    if name in MONTHS:
        return {"upper": "{MONTH}", "lower": "{month}"}.get(case_style(name), "{Month}")
    return "{Sept}" if name == "Sept" else "{Mon}"


def weekday_code(name: str) -> str:
    return {"upper": "{WEEKDAY}", "lower": "{weekday}"}.get(case_style(name), "{Weekday}")


def ordinal(n: int) -> str:
    return "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def fmt_date(d: date, f: str) -> str:
    m = MONTHS[d.month - 1]
    w = WEEKDAYS[d.weekday()]
    return (f.replace("{Month}", m).replace("{MONTH}", m.upper()).replace("{month}", m.lower())
             .replace("{Sept}", "Sept" if d.month == 9 else m[:3]).replace("{Mon}", m[:3])
             .replace("{Weekday}", w).replace("{WEEKDAY}", w.upper()).replace("{weekday}", w.lower())
             .replace("{Wkd}", w[:3]).replace("{dth}", f"{d.day}{ordinal(d.day)}").replace("{d}", str(d.day))
             .replace("{th}", ordinal(d.day)).replace("{dd}", f"{d.day:02d}").replace("{mm}", f"{d.month:02d}")
             .replace("{yyyy}", str(d.year)))


# ------------------------------------------------------------------------------------------------ timestamps


def _wall(hh, mm, ss, frac) -> str:
    micro = (frac or ".0")[1:7].ljust(6, "0")
    return f"{hh}:{mm}:{ss or '00'}.{micro}"


def _time_text(t: time, secs: bool, frac: int) -> str:
    s = f"{t.hour:02d}:{t.minute:02d}"
    if secs:
        s += f":{t.second:02d}"
    if frac:
        s += "." + f"{t.microsecond:06d}"[:frac]
    return s


def _offset_text(off: timedelta, colon: bool) -> str:
    total = int(off.total_seconds())
    sign = "+" if total >= 0 else "-"
    h, m = divmod(abs(total) // 60, 60)
    return f"{sign}{h:02d}:{m:02d}" if colon else f"{sign}{h:02d}{m:02d}"


def _frame_tz(frame: str):
    if frame == "UTC":
        return timezone.utc
    if frame.startswith("fixed"):
        sign = 1 if frame[5] == "+" else -1
        return timezone(sign * timedelta(hours=int(frame[6:8]), minutes=int(frame[-2:])))
    return ZoneInfo(frame)


def render_timestamp(k: int, wall: str, frame: str, out: str, style: str, run_day: date) -> str:
    sep, secs, frac = style.split(",")
    d = run_day + timedelta(days=k)
    t = time.fromisoformat(wall)
    if frame == "naive" or out == "naive":
        return f"{d.isoformat()}{sep}{_time_text(t, secs == 's', int(frac))}"
    local = datetime.combine(d, t).replace(tzinfo=_frame_tz(frame))
    if out == "Z":
        u = local.astimezone(timezone.utc)
        return f"{u.date().isoformat()}{sep}{_time_text(u.time(), secs == 's', int(frac))}Z"
    return f"{d.isoformat()}{sep}{_time_text(t, secs == 's', int(frac))}{_offset_text(local.utcoffset(), out == 'off')}"


# ------------------------------------------------------------------------------------------------ the context


@dataclass
class Context:
    """One scenario's anchor and bindings, shared by every test of the scenario so that a phrase renders the same way
    in all of them."""
    anchor_day: date
    zone: str
    domain: str
    frame: str                      # the frame of zone-aware timestamps: Calendar's zone, else UTC
    zones: list[str] = field(default_factory=list)      # IANA zones named in the scenario's data
    seed_days: set = field(default_factory=set)        # local days of the cover's timestamps and dates
    target_days: set = field(default_factory=set)      # those of the cover's target records
    instants: list = field(default_factory=list)       # (UTC HH:MM, k, wall, zone) of zone-aware instants (Calendar)
    bindings: dict = field(default_factory=dict)       # phrase key -> (k, how)
    row_days: set = field(default_factory=set)         # while templating a data record: that record's days
    notes: list = field(default_factory=list)


def walk(x, path=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(x, list):
        for v in x:
            yield from walk(v, f"{path}[]")
    else:
        yield path, x


def parse_timestamp(s: str, ctx: Context):
    """(k, wall, frame, out, style, local datetime) of a whole-value ISO timestamp, or None for a date."""
    m = ISO_FULL.match(s)
    y, mo, d, sep, hh, mm, ss, frac, tz = m.groups()
    if sep is None:
        return None
    style = f"{sep},{'s' if ss else ''},{len(frac) - 1 if frac else 0}"
    wall = _wall(hh, mm, ss, frac)
    naive = datetime(int(y), int(mo), int(d), int(hh), int(mm), int(ss or 0), int((frac or ".0")[1:7].ljust(6, "0")))
    if tz is None:
        return ((naive.date() - ctx.anchor_day).days, wall, "naive", "naive", style, naive)
    if tz == "Z":
        inst = naive.replace(tzinfo=timezone.utc)
        if ctx.frame == "UTC":
            return ((naive.date() - ctx.anchor_day).days, wall, "UTC", "Z", style, inst)
        local = inst.astimezone(ZoneInfo(ctx.frame))
        lw = _wall(f"{local.hour:02d}", f"{local.minute:02d}", f"{local.second:02d}", f".{local.microsecond:06d}")
        return ((local.date() - ctx.anchor_day).days, lw, ctx.frame, "Z", style, local)
    sign = 1 if tz[0] == "+" else -1
    off = sign * timedelta(hours=int(tz[1:3]), minutes=int(tz[-2:]))
    inst = naive.replace(tzinfo=timezone(off))
    out = "off" if ":" in tz else "offnc"
    for z in ([ctx.frame] if ctx.frame != "UTC" else []) + ctx.zones:
        if inst.astimezone(ZoneInfo(z)).utcoffset() == off:
            return ((naive.date() - ctx.anchor_day).days, wall, z, out, style, inst)
    frame = "fixed" + _offset_text(off, True)
    return ((naive.date() - ctx.anchor_day).days, wall, frame, out, style, inst)


def struct_token(s: str, ctx: Context) -> str:
    if ISO_FULL.match(s):
        p = parse_timestamp(s, ctx)
        if p is None:
            d = date.fromisoformat(s)
            return f"{OPEN}D|{(d - ctx.anchor_day).days:+d}{CLOSE}"
        k, wall, frame, out, style, _ = p
        return f"{OPEN}T|{k:+d}|{wall}|{frame}|{out}|{style}{CLOSE}"
    a, b = SLACK_TS.match(s).groups()
    inst = datetime.fromtimestamp(int(a), timezone.utc)
    k = (inst.date() - ctx.anchor_day).days
    return f"{OPEN}S|{k:+d}|{inst.strftime('%H:%M:%S')}|{b}{CLOSE}"


def local_day(s: str, ctx: Context) -> date | None:
    if ISO_FULL.match(s):
        p = parse_timestamp(s, ctx)
        return date.fromisoformat(s) if p is None else ctx.anchor_day + timedelta(days=p[0])
    if SLACK_TS.match(s):
        return datetime.fromtimestamp(int(s.split(".")[0]), timezone.utc).date()
    return None


def context_for(cover: dict, anchor_day: date, zone: str) -> Context:
    domain = cover["domain"]
    frame = zone if domain == "calendar" else "UTC"
    zones = sorted({v for p, v in walk(cover["seed"]) if isinstance(v, str) and p.split(".")[-1] in ("timeZone", "time_zone")
                    and "/" in v})
    ctx = Context(anchor_day, zone, domain, frame, zones)
    expected = {str(x) for r in cover["references"] for x in r.get("expected", [])}
    for table, rows in cover["seed"].items():
        for row in rows if isinstance(rows, list) else []:
            is_target = any(isinstance(v, (str, int)) and str(v) in expected for v in row.values())
            for p, v in walk(row):
                if isinstance(v, str) and (ISO_FULL.match(v) or (domain == "slack" and SLACK_TS.match(v))):
                    d = local_day(v, ctx)
                    ctx.seed_days.add(d)
                    if is_target:
                        ctx.target_days.add(d)
                    if ISO_FULL.match(v) and frame != "UTC" and v[10:11] == "T" and (v.endswith("Z") or re.search(r"[+-]\d{2}:?\d{2}$", v)):
                        k, wall, fr, out, style, local = parse_timestamp(v, ctx)
                        if fr not in ("naive", "UTC") and not fr.startswith("fixed"):
                            u = local.astimezone(timezone.utc)
                            ctx.instants.append((u.strftime("%H:%M"), k, wall, fr))
    return ctx


# ------------------------------------------------------------------------------------------------ phrases


def _nearest(cands: list[date], ctx: Context) -> date:
    return min(cands, key=lambda c: (abs((c - ctx.anchor_day).days), c))


def resolve_month_day(month: int, day: int, year: int | None, ctx: Context) -> tuple[date, str]:
    if year:
        return date(year, month, day), "explicit year"
    in_target = [d for d in ctx.target_days if (d.month, d.day) == (month, day)]
    if in_target:
        return _nearest(in_target, ctx), "the target's date"
    in_seed = [d for d in ctx.seed_days if (d.month, d.day) == (month, day)]
    if in_seed:
        return _nearest(in_seed, ctx), "a date in the data"
    cands = []
    for y in (ctx.anchor_day.year - 1, ctx.anchor_day.year, ctx.anchor_day.year + 1):
        try:
            cands.append(date(y, month, day))
        except ValueError:
            pass
    return _nearest(cands, ctx), "the nearest such date to the anchor (not in the data)"


def resolve_in(days: set, pred) -> list[date]:
    return sorted(d for d in days if pred(d))


def bind(key: tuple, ctx: Context, resolver) -> int:
    if key not in ctx.bindings:
        d, how = resolver()
        ctx.bindings[key] = ((d - ctx.anchor_day).days, how)
    return ctx.bindings[key][0]


def phrase_token(m: re.Match, ctx: Context) -> str | None:
    """The replacement for one matched phrase (tokens and the literal text between them), or None to leave it."""
    g, s = m.groupdict(), m.string

    def between(a: str, b: str) -> str:
        return s[m.end(a):m.start(b)]
    if g["iso"]:
        return struct_token(g["iso"], ctx) if ISO_FULL.match(g["iso"]) else None
    if g["ts"]:
        return struct_token(g["ts"], ctx) if ctx.domain == "slack" else None
    if g["utc"]:
        hhmm = f"{int(g['uh']):02d}:{g['um']}"
        hits = sorted({(k, wall, z) for u, k, wall, z in ctx.instants if u == hhmm})
        if len(hits) == 1:
            k, wall, z = hits[0]
            return f"{OPEN}U|{k:+d}|{wall}|{z}|{'{HH}' if len(g['uh']) == 2 else '{H}'}:{{MM}}{CLOSE}"
        return None
    if g["wdmd"] or g["md"]:
        p = "wdmd" if g["wdmd"] else "md"
        mon, day = month_number(g[f"{p}_m"]), int(g[f"{p}_d"])
        year = int(g[f"{p}_y"]) if g[f"{p}_y"] else None
        try:
            k = bind(("md", mon, day, year), ctx, lambda: resolve_month_day(mon, day, year, ctx))
        except ValueError:
            return None
        body = (f"{month_code(g[f'{p}_m'])}{g[f'{p}_dot']}{between(f'{p}_dot', f'{p}_d')}{{d}}"
                f"{'{th}' if g[f'{p}_th'] else ''}{(g[f'{p}_ys'] + '{yyyy}') if year else ''}")
        if p == "md":
            return f"{OPEN}P|{k:+d}|{body}{CLOSE}"
        d = ctx.anchor_day + timedelta(days=k)
        sep = between("wdmd_w", "wdmd_m")
        if WEEKDAYS[d.weekday()] == g["wdmd_w"].capitalize():
            return f"{OPEN}P|{k:+d}|{weekday_code(g['wdmd_w'])}{sep}{body}{CLOSE}"
        ctx.notes.append(f"the weekday {g['wdmd_w']!r} does not match {d.isoformat()} in {m.group(0)!r}")
        j = (WEEKDAYS.index(g["wdmd_w"].capitalize()) - ctx.anchor_day.weekday()) % 7
        return f"{OPEN}W|{j}|{weekday_code(g['wdmd_w'])}{CLOSE}{sep}{OPEN}P|{k:+d}|{body}{CLOSE}"
    if g["wdthe"]:
        w, day = WEEKDAYS.index(g["wdthe_w"].capitalize()), int(g["wdthe_d"])
        key = ("wdthe", w, day)
        if key not in ctx.bindings:
            cands = []
            for dm in (-1, 0, 1):
                y, mo = ctx.anchor_day.year, ctx.anchor_day.month + dm
                y, mo = (y - 1, 12) if mo == 0 else (y + 1, 1) if mo == 13 else (y, mo)
                try:
                    c = date(y, mo, day)
                except ValueError:
                    continue
                if c.weekday() == w:
                    cands.append(c)
            if not cands:
                return None
            ctx.bindings[key] = ((_nearest(cands, ctx) - ctx.anchor_day).days, "the nearest such date to the anchor")
        k = ctx.bindings[key][0]
        return f"{OPEN}P|{k:+d}|{weekday_code(g['wdthe_w'])}{between('wdthe_w', 'wdthe_d')}{{d}}{{th}}{CLOSE}"
    if g["onnth"]:
        day = int(g["onnth_d"])

        def res():
            for pool, how in ((ctx.target_days, "the target's date with that day of the month"),
                              (ctx.seed_days, "a date in the data with that day of the month")):
                hits = [d for d in pool if d.day == day and abs((d - ctx.anchor_day).days) <= 31]
                if hits:
                    return _nearest(hits, ctx), how
            return None, ""
        key = ("onnth", day)
        if key not in ctx.bindings:
            d, how = res()
            if d is None:
                return None
            ctx.bindings[key] = ((d - ctx.anchor_day).days, how)
        k = ctx.bindings[key][0]
        return f"on the {OPEN}P|{k:+d}|{{d}}{{th}}{CLOSE}"
    if g["my"]:
        mon, year = month_number(g["my_m"]), int(g["my_y"])

        def res():
            inm = lambda d: d.year == year and d.month == mon  # noqa: E731
            t = resolve_in(ctx.target_days, inm)
            if t:
                return t[0], "the target's date in that month"
            sd = resolve_in(ctx.seed_days, inm)
            if sd:
                return _nearest(sd, ctx), "a date in the data in that month"
            return date(year, mon, 15), "the middle of that month (not in the data)"
        k = bind(("my", mon, year), ctx, res)
        return f"{OPEN}P|{k:+d}|{month_code(g['my_m'])}{g['my_dot']}{between('my_dot', 'my_y')}{{yyyy}}{CLOSE}"
    if g["wd"]:
        j = (WEEKDAYS.index(g["wd_w"].capitalize()) - ctx.anchor_day.weekday()) % 7
        return f"{OPEN}W|{j}|{weekday_code(g['wd_w'])}{CLOSE}"
    if g["mon"]:
        mon = month_number(g["mon_m"])

        own = [d for d in ctx.row_days if d.month == mon]
        if own:          # a month named in a record's own text: that record's date in that month
            k = (_nearest(own, ctx) - ctx.anchor_day).days
            return f"{g['mon_pre']}{g['mon_sp']}{OPEN}P|{k:+d}|{month_code(g['mon_m'])}{CLOSE}"

        def res():
            for pool, how in ((ctx.target_days, "the target's date in that month"),
                              (ctx.seed_days, "a date in the data in that month")):
                hits = [d for d in pool if d.month == mon]
                if hits:
                    return _nearest(hits, ctx), how
            months = [(y, mon) for y in (ctx.anchor_day.year - 1, ctx.anchor_day.year, ctx.anchor_day.year + 1)]
            past = [date(y, mo, 15) for y, mo in months if date(y, mo, 15) <= ctx.anchor_day]
            return (max(past) if past else date(ctx.anchor_day.year, mon, 15)), "the most recent such month (not in the data)"
        k = bind(("mon", mon), ctx, res)
        return f"{g['mon_pre']}{g['mon_sp']}{OPEN}P|{k:+d}|{month_code(g['mon_m'])}{CLOSE}"
    if g["mon2"]:
        mon = month_number(g["mon2_m"])
        hits = [d for d in ctx.target_days | ctx.seed_days if d.month == mon]
        if not hits:
            return None          # no date in that month: a name or a verb ("May I"), left as written
        own = [d for d in ctx.row_days if d.month == mon]
        if own:
            k = (_nearest(own, ctx) - ctx.anchor_day).days
            return f"{OPEN}P|{k:+d}|{month_code(g['mon2_m'])}{CLOSE}"

        def res():
            t = [d for d in ctx.target_days if d.month == mon]
            return (_nearest(t, ctx), "the target's date in that month") if t else (_nearest(hits, ctx), "a date in the data in that month")
        k = bind(("mon", mon), ctx, res)
        return f"{OPEN}P|{k:+d}|{month_code(g['mon2_m'])}{CLOSE}"
    if g["yr"]:
        n = int(g["yr_y"]) - ctx.anchor_day.year
        ctx.bindings.setdefault(("yr", int(g["yr_y"])), (n, "a year written as a number: the anchor's year moves to the "
                                                            "run's, the others keep their distance from it"))
        return f"{OPEN}Y|{n:+d}{CLOSE}"
    return None


def template_text(s: str, ctx: Context, found: list, path: str) -> str:
    out, last = [], 0
    for m in PHRASE.finditer(s):
        tok = phrase_token(m, ctx)
        kind = next(k for k in ("iso", "ts", "utc", "wdmd", "md", "wdthe", "my", "onnth", "wd", "mon", "mon2", "yr")
                    if m.group(k))
        found.append({"path": path, "kind": kind, "text": m.group(0), "token": tok})
        if tok is None:
            continue
        out.append(s[last:m.start()])
        out.append(tok)
        last = m.end()
    out.append(s[last:])
    return "".join(out)


def make(case: dict, ctx: Context) -> tuple[dict, list]:
    """(template, occurrences): every date-bearing value or phrase of `case` replaced by a token."""
    found = []
    seed = case.get("seed", {})
    if isinstance(seed, dict):        # a test: tables of rows
        rows = [row for rows in seed.values() if isinstance(rows, list) for row in rows if isinstance(row, dict)]
    else:                             # a writer's scenario: seed operations [kind, arguments]
        rows = [op[1] for op in seed if isinstance(op, list) and len(op) > 1 and isinstance(op[1], dict)]

    def days_around(ids: set) -> set:
        """The days of the records holding any of `ids`, and of the records those point to (one step)."""
        near = [row for row in rows if any(isinstance(v, (str, int)) and str(v) in ids for v in row.values())]
        linked = {str(v) for row in near for v in row.values() if isinstance(v, (str, int))}
        near += [row for row in rows if str(row.get("id", row.get("channel_id", row.get("user_id", "")))) in linked]
        return {local_day(v, ctx) for row in near for _, v in walk(row) if isinstance(v, str)
                and (ISO_FULL.match(v) or (ctx.domain == "slack" and SLACK_TS.match(v)))}

    def rec(x, key=None, path=""):
        if isinstance(x, dict):
            if re.fullmatch(r"\.references\[\]\.claims\[\]", path) and "witness" in x:
                saved = ctx.row_days         # a near miss's explanation: the near miss's own records first
                ctx.row_days = days_around({str(x["witness"])})
                try:
                    return {k: rec(v, k, f"{path}.{k}") for k, v in x.items()}
                finally:
                    ctx.row_days = saved
            if re.fullmatch(r"\.seed\.[^.\[]+\[\]", path):      # a data record: its own days, for its own text
                saved = ctx.row_days
                ctx.row_days = {local_day(v, ctx) for _, v in walk(x) if isinstance(v, str)
                                and (ISO_FULL.match(v) or (ctx.domain == "slack" and SLACK_TS.match(v)))}
                try:
                    return {k: rec(v, k, f"{path}.{k}") for k, v in x.items()}
                finally:
                    ctx.row_days = saved
            return {k: rec(v, k, f"{path}.{k}") for k, v in x.items() if k != "clock"}
        if isinstance(x, list):
            return [rec(v, key, f"{path}[]") for v in x]
        if isinstance(x, str):
            if key == "case_sha256":
                return x
            if ISO_FULL.match(x) or (ctx.domain == "slack" and SLACK_TS.match(x)):
                tok = struct_token(x, ctx)
                found.append({"path": path, "kind": "value", "text": x, "token": tok})
                return tok
            if key is not None and ID_KEYS.match(str(key)):
                return x
            return template_text(x, ctx, found, path)
        return x
    t = rec(case)
    return t, found


# ------------------------------------------------------------------------------------------------ rendering


def add_months(d: date, n: int) -> date:
    i = d.year * 12 + d.month - 1 + n
    y, m = divmod(i, 12)
    return date(y, m + 1, min(d.day, calendar.monthrange(y, m + 1)[1]))


def months_elapsed(anchor_day: date, run_day: date) -> int:
    """The largest whole number of months M with anchor_day + M months on or before run_day."""
    m = (run_day.year - anchor_day.year) * 12 + run_day.month - anchor_day.month
    while add_months(anchor_day, m) > run_day:
        m -= 1
    return m


@dataclass(frozen=True)
class Shift:
    """How a template is moved for a run: by whole days (`day`: the anchor day becomes the run day), by whole months
    (`month`: every date keeps its day of the month, so calendar months keep their records; the world's day is the
    anchor day moved by the whole months elapsed, at most a month before the run day), or not at all (`fixed`: Slack,
    whose message ids are their timestamps; see `mode_for`)."""
    anchor_day: date
    run_day: date
    mode: str = "day"

    @property
    def months(self) -> int:
        return months_elapsed(self.anchor_day, self.run_day)

    @property
    def world_day(self) -> date:
        if self.mode == "fixed":
            return self.anchor_day
        return self.run_day if self.mode == "day" else add_months(self.anchor_day, self.months)

    def day(self, k: int) -> date:
        d0 = self.anchor_day + timedelta(days=k)
        if self.mode == "fixed":
            return d0
        if self.mode == "day":
            return d0 + (self.run_day - self.anchor_day)
        return add_months(d0, self.months)


def render_token(body: str, sh: Shift) -> str:
    kind, *parts = body.split("|")
    if kind == "D":
        return sh.day(int(parts[0])).isoformat()
    if kind == "T":
        k, wall, frame, out, style = parts
        return render_timestamp(0, wall, frame, out, style, sh.day(int(k)))
    if kind == "S":
        k, hms, suffix = parts
        epoch = calendar.timegm(datetime.combine(sh.day(int(k)), time.fromisoformat(hms)).timetuple())
        return f"{epoch}.{suffix}"
    if kind == "P":
        k, f = parts[0], "|".join(parts[1:])
        return fmt_date(sh.day(int(k)), f)
    if kind == "W":
        j, f = parts
        return fmt_date(sh.world_day + timedelta(days=int(j)), f)
    if kind == "Y":
        return str(sh.world_day.year + int(parts[0]))
    if kind == "U":
        k, wall, zone, f = parts
        local = datetime.combine(sh.day(int(k)), time.fromisoformat(wall)).replace(tzinfo=ZoneInfo(zone))
        u = local.astimezone(timezone.utc)
        return f.replace("{HH}", f"{u.hour:02d}").replace("{H}", str(u.hour)).replace("{MM}", f"{u.minute:02d}")
    raise ValueError(f"unknown token {body!r}")


def render(template: dict, run_day: date, mark: str | None = None):
    """The test for a run on `run_day` (a local day in the anchor's zone). With `mark`, every token is written as
    `mark` instead (for the residue check)."""
    sh = Shift(date.fromisoformat(template["dates"]["anchor"]["day"]), run_day, template["dates"].get("mode", "day"))

    def sub(s: str) -> str:
        return TOKEN.sub(lambda m: mark if mark is not None else render_token(m.group(1), sh), s)

    def rec(x):
        if isinstance(x, dict):
            return {k: rec(v) for k, v in x.items()}
        if isinstance(x, list):
            return [rec(v) for v in x]
        if isinstance(x, str) and OPEN in x:
            return sub(x)
        return x
    out = rec({k: v for k, v in template.items() if k != "dates"})
    out["dates"] = {"anchor": template["dates"]["anchor"], "mode": sh.mode, "run_day": run_day.isoformat(),
                    "world_day": sh.world_day.isoformat(), "shift_days": (sh.world_day - sh.anchor_day).days}
    return out


def mode_for(cover_template: dict, ctx: "Context") -> str:
    """`month` when the request names a month without a day and that month holds the target's date (a condition by
    calendar month, which a shift of whole days does not keep); `fixed` for Slack; else `day`.

    Slack is held at its written days for now: a Slack message's id is its timestamp, so moving the dates moves the
    ids, and the PI's rulings, the blind labels and the verdicts are keyed by message id (two rulings in the
    denominator's scenarios). No Slack condition is read against today; its one date without a year ("posted on
    September 15th") stays unambiguous until 2027-09-15. Moving Slack needs the scoring to map message ids first."""
    if ctx.domain == "slack":
        return "fixed"
    for m in TOKEN.finditer(cover_template.get("prompt", "")):
        kind, *parts = m.group(1).split("|")
        if kind != "P":
            continue
        f = "|".join(parts[1:])
        if re.search(r"\{(Month|MONTH|month|Mon|Sept)\}", f) and "{d}" not in f:
            d = ctx.anchor_day + timedelta(days=int(parts[0]))
            if any((t.year, t.month) == (d.year, d.month) for t in ctx.target_days):
                return "month"
    return "day"


def run_day_of(now: datetime, zone: str) -> date:
    return now.astimezone(ZoneInfo(zone)).date()


def digest(value) -> str:
    import hashlib
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


CALENDAR_ZONE = "America/Los_Angeles"            # the calendars' zone, and the zone a Calendar agent is given
LOCAL_ZONE = "America/Indiana/Indianapolis"      # this machine's zone, which every other agent is given


def zone_for(domain: str) -> str:
    return CALENDAR_ZONE if domain == "calendar" else LOCAL_ZONE


def today_for(domain: str, now: datetime | None = None) -> dict:
    """The date and time a writer is given (in the zone its scenario's agent will see); recorded on the scenario as
    `written_for`, which is then its reference day."""
    zone = zone_for(domain)
    t = (now or datetime.now(timezone.utc)).astimezone(ZoneInfo(zone))
    return {"date": t.date().isoformat(), "time": t.strftime("%H:%M"), "zone": zone}


def today_text(when: dict) -> str:
    d = date.fromisoformat(when["date"])
    return (f"Today is {WEEKDAYS[d.weekday()]}, {MONTHS[d.month - 1]} {d.day}, {d.year}, and the time is "
            f"{when['time']} in {when['zone']}.")


DISCONTINUED = ("Shifting the agent's clock is discontinued (the PI, 2026-10-03: grounding/AGENTS.md, \"Dates: never "
                "change the agent's clock\"). Run the test's template (grounding/runs/dates_02/suite), which is rendered "
                "against the real day.")


def is_template(case: dict) -> bool:
    return "anchor" in (case.get("dates") or {}) and "run_day" not in case["dates"]


def at_anchor(template: dict) -> dict:
    """The test as written: the template rendered on its anchor day (equal to the original test, checks.py proves it);
    for what is keyed by the original ids and values, such as the PI's rulings."""
    return render(template, date.fromisoformat(template["dates"]["anchor"]["day"]))


def for_run(case: dict, now: datetime | None = None) -> tuple[dict, dict | None]:
    """The test as it runs now. A template is rendered against the real day in its anchor's zone (the zone the agent
    is given), with a fresh digest; the second value records the anchor, the mode, the run day and the shift. A test
    written with absolute dates runs as written, unless it was made to run on a shifted clock (a `clock`, or a Calendar
    test dated 2018): that is refused."""
    if is_template(case):
        zone = case["dates"]["anchor"]["zone"]
        rendered = render(case, run_day_of(now or datetime.now(timezone.utc), zone))
        rendered["case_sha256"] = digest({k: v for k, v in rendered.items() if k not in ("case_sha256", "dates")})
        return rendered, {"zone": zone, "template_sha256": case.get("case_sha256"), **rendered["dates"]}
    if case.get("clock") or case.get("domain") == "calendar":
        raise RuntimeError(f"{case.get('case_id')}: {DISCONTINUED}")
    return case, None


# The writer's worked examples with dates, and the day each was written for (Calendar's, like its tests). The writer
# sees them moved to the date it is given, so that no example shows another year (the PI, 2026-10-04).
EXAMPLE_ANCHORS = {"calendar-example.json": (date(2018, 6, 17), CALENDAR_ZONE)}


def example_context(example: dict, anchor_day: date, zone: str) -> Context:
    """A Context for a scenario in the writer's format (seed operations, a reference with its target ids)."""
    ctx = Context(anchor_day, zone, example["domain"], zone if example["domain"] == "calendar" else "UTC")
    targets = set(map(str, (example.get("reference") or {}).get("target", [])))
    for op in example.get("seed", []):
        args = op[1] if isinstance(op, list) and len(op) > 1 and isinstance(op[1], dict) else {}
        for _, v in walk(args):
            if isinstance(v, str) and ISO_FULL.match(v):
                d = local_day(v, ctx)
                ctx.seed_days.add(d)
                if str(args.get("id")) in targets:
                    ctx.target_days.add(d)
                p = parse_timestamp(v, ctx)
                if p and p[2] not in ("naive", "UTC") and not p[2].startswith("fixed"):
                    ctx.instants.append((p[5].astimezone(timezone.utc).strftime("%H:%M"), p[0], p[1], p[2]))
    return ctx


def move_example(raw: str, anchor_day: date, zone: str, run_day: date) -> str:
    """The example's text with every date moved to `run_day`, its layout kept: each string that changes is replaced
    where it stands."""
    example = json.loads(raw)
    t, _ = make(example, example_context(example, anchor_day, zone))
    t["dates"] = {"anchor": {"day": anchor_day.isoformat(), "zone": zone}, "mode": "day"}
    moved = render(t, run_day)
    moved.pop("dates")
    pairs = {}
    for (_, a), (_, b) in zip(walk(example), walk(moved)):
        if isinstance(a, str) and a != b:
            pairs[a] = b
    out = raw
    for a in sorted(pairs, key=len, reverse=True):
        for enc in {json.dumps(a, ensure_ascii=False), json.dumps(a)}:
            out = out.replace(enc, json.dumps(pairs[a], ensure_ascii=False))
    if json.loads(out) != moved:
        raise ValueError("moving the example changed more than its dates")
    return out


def move_examples(folder, today: dict) -> list[str]:
    """Move the worked examples in a writer's workspace to the date it is given; returns the files moved."""
    from pathlib import Path
    moved = []
    for name, (anchor_day, zone) in EXAMPLE_ANCHORS.items():
        path = Path(folder) / name
        if path.exists():
            run_day = date.fromisoformat(today["date"]) if today["zone"] == zone else \
                datetime.fromisoformat(f"{today['date']}T{today['time']}").replace(
                    tzinfo=ZoneInfo(today["zone"])).astimezone(ZoneInfo(zone)).date()
            path.write_text(move_example(path.read_text(), anchor_day, zone, run_day))
            moved.append(name)
    return moved

