"""The mechanical steps of method.md: from a writer-approved cover, build the easy and hard plural cover cases.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.build [ID ...]

For every cover the writer judged plural-worthy (writer.json) and whose wording passed the code checks:
- **Easy tier (SMA-<id>-E):** the target plus two copies in plain view (same container, the writer's variant texts).
- **Hard tier (SMA-<id>-H),** for the four record kinds the route table covers: the target and one plain copy, plus
  one trap per laziness behaviour that applies to the request. Whether the request pins its container comes from
  the reference query (a condition on the container field). Traps:
  - Calendar events, container not pinned: a copy on another owned calendar (C), a copy on an owned calendar
    hidden in the list (H).
  - Box files, folder not pinned: a copy one folder down (C1) and one in another folder (O); a crowd of the cover's
    own near misses that fail a condition search cannot express, ahead of the traps in search order.
  - Linear issues: a copy past the first 50 issues of the team (P), with older filler issues ahead of it.
  - Slack messages, channel pinned: a copy past the first 100 messages of the channel (P), with newer filler
    messages ahead of it. The fillers mention the search words when they fail another condition (the author), so a
    one-page search misses the copy too.
  - Slack messages, channel not pinned: a copy in another public channel (C) and in a private channel (H).
- **Checks:** fdc.check_reference (the query selects exactly the targets; every near-miss claim still holds); no
  container over 200 records; every target's date the same in UTC and the actor's zone (Los Angeles).
Writes cases/<domain>/SMA-*.json, placements.json, build.json (per cover: what was built, and why not).
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from grounding.runs.autogen_01.kit import derive
from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.several_match_auto_01 import seedkit
from grounding.runs.several_match_auto_01.population import covers
from grounding.runs.several_match_auto_01.writer import KIND

HERE = Path(__file__).resolve().parent
OUT = HERE / "cases"
LA = ZoneInfo("America/Los_Angeles")
CONTAINER = {"calendar_events": "calendar_id", "box_files": "parent_id", "issues": "teamId", "messages": "channel_id"}
PRACTICAL = 200


def pinned(query) -> bool:
    field = CONTAINER.get(query["table"])
    return any(f.get("field") == field for f in query.get("filters") or []) or \
        any((e.get("join") or {}).get("parent") == field for e in query.get("edges") or [])


def utc(text):
    return datetime.fromisoformat(str(text).replace("Z", "+00:00")).replace(tzinfo=timezone.utc) \
        if "+" not in str(text)[10:] else datetime.fromisoformat(str(text))


def iso_z(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Builder:
    """One case under construction: its seed, targets and placements."""

    def __init__(self, cover, answer, drop=(), no_variants=False):
        self.drop = set(drop)
        self.case = copy.deepcopy(cover)
        self.domain = cover["domain"]
        self.seed = self.case["seed"]
        self.ref = self.case["references"][0]
        self.table = self.ref["query"]["table"]
        self.key = str(self.ref["expected"][0])
        self.field = KIND.get(self.table, ("", "name"))[1]
        self.variants = [] if no_variants else [v for v in answer.get("variants") or [] if v]
        self.words = (answer.get("search_words") or "").strip()
        self.targets = [self.key]
        self.place = {self.key: "V"}
        self.seq = 700
        self.notes = []

    # ---------------------------------------------------------------- copies
    def text(self, i):
        original = (seedkit.find_row(self.case, self.table, self.key) or {}).get(self.field)
        v = self.variants[i % len(self.variants)] if self.variants else original
        if self.table == "box_files" and original and not self.variants:  # names stay unique in a folder
            stem, dot, ext = original.rpartition(".")
            return f"{stem} ({i + 2}).{ext}" if dot else f"{original} ({i + 2})"
        if self.table == "box_files" and original and "." in original:
            ext = original.rsplit(".", 1)[1]
            if not str(v).lower().endswith("." + ext.lower()):
                v = f"{v}.{ext}"
        return v

    def copy_target(self, i, code, **over):
        """A copy of the target: the variant text, a fresh key, and the kind's identity fields."""
        row = seedkit.find_row(self.case, self.table, self.key)
        over = {self.field: self.text(i), **over}
        nk = None
        if self.table == "messages":
            when = over.pop("_at", None) or utc(row["created_at"]) + timedelta(minutes=i + 1)
            self.seq += 1
            nk = f"{int(when.timestamp())}.{self.seq:06d}"
            over.update(ts=nk, created_at=iso_z(when))
        elif self.table == "issues":
            team = next(t for t in self.seed["teams"] if t["id"] == over.get("teamId", row["teamId"]))
            n = 1 + max([int(x.get("number") or 0) for x in self.seed["issues"] if x.get("teamId") == team["id"]]
                        or [0])
            nk = f"{self.key}-sm{i}-{code.lower()}"
            over.update(identifier=f"{team['key']}-{n}", number=float(n), sortOrder=float(n),
                        branchName=f"{team['key'].lower()}-{n}", url=f"https://linear.app/northwind/issue/"
                        f"{team['key']}-{n}")
        elif self.table == "calendar_events":
            nk = f"{self.key}_sm{i}{code.lower()}"
            over.update(ical_uid=f"{nk}@northwind.example", etag=f'"etag_{nk}"')
        nk = str(seedkit.clone(self.seed, self.domain, self.table, self.key, over, new_key=nk))
        selected = {str(x) for x in fdc.evaluate(self.seed, self.ref["query"])}
        if nk not in selected and self.field in over:  # the variant broke a condition: keep the original text
            original = (seedkit.find_row(self.case, self.table, self.key) or {}).get(self.field)
            seedkit.find_row(self.case, self.table, nk)[self.field] = original
            self.notes.append(f"variant {i} failed the query; the copy keeps the original text")
        self.targets.append(nk)
        self.place[nk] = code
        return nk

    # ---------------------------------------------------------------- traps
    def trap_calendar(self):
        prim_entry = next(e for e in self.seed["calendar_list_entries"] if e.get("primary"))
        prim = next(c for c in self.seed["calendars"] if c["id"] == prim_entry["calendar_id"])
        made = []
        for i, (code, cid, name, hidden) in enumerate((("C", "team-events@northwind.example", "Team events", False),
                                                        ("H", "planning@northwind.example", "Planning", True)), 1):
            if code in self.drop:
                continue
            self.seed["calendars"].append({**copy.deepcopy(prim), "id": cid, "summary": name,
                                           "description": f"{name} calendar", "etag": f'"etag_{cid}"'})
            self.seed["calendar_list_entries"].append({**copy.deepcopy(prim_entry), "id": f"cle_{cid}",
                                                       "calendar_id": cid, "primary": False, "hidden": hidden,
                                                       "etag": f'"etag_cle_{cid}"'})
            self.copy_target(i, code, calendar_id=cid)
            made.append("an owned calendar hidden in the list" if hidden else "another owned calendar")
        return made

    def box_crowd(self):
        """32 copies of a near miss that shares the search words and fails a condition search cannot express."""
        if not self.words:
            return None
        claims = self.ref.get("claims") or []
        for c in claims:
            if c["requirement"].split(":")[-1] in ("File.name", "File.description"):
                continue
            w = seedkit.find_row(self.case, "box_files", str(c["witness"]))
            if not w or self.words.lower() not in f"{w.get('name')} {w.get('description')}".lower():
                continue
            stem, _, ext = str(w["name"]).rpartition(".")
            for n in range(32):
                seedkit.clone(self.seed, self.domain, "box_files", str(w["id"]),
                              {"name": f"{stem or w['name']} {n + 1:02d}" + (f".{ext}" if stem else "")})
            return c["requirement"]
        return None

    def trap_box(self):
        f = seedkit.find_row(self.case, "box_files", self.key)
        crowd = self.box_crowd()
        folder = seedkit.find_row(self.case, "box_folders", f["parent_id"]) or self.seed["box_folders"][0]
        made = []
        for i, (code, name, parent) in enumerate((("C1", "Current", f["parent_id"]), ("O", "Shared", "0")), 1):
            if code in self.drop:
                continue
            fid = str(1 + max(int(x["id"]) for x in self.seed["box_folders"] + self.seed["box_files"]
                              if str(x["id"]).isdigit()))
            self.seed["box_folders"].append({**copy.deepcopy(folder), "id": fid, "name": name, "parent_id": parent})
            self.copy_target(i, code, parent_id=fid)
            made.append("one folder down" if code == "C1" else "another folder")
        if crowd:
            made.append(f"a search crowd failing {crowd}")
        return made

    def trap_linear(self):
        if "P" in self.drop:
            return []
        row = seedkit.find_row(self.case, "issues", self.key)
        team = row["teamId"]
        day = str(row["createdAt"])[:10]
        paged_at = f"{day}T23:30:00"
        latest_plain = max(str(seedkit.find_row(self.case, "issues", t)["createdAt"]) for t in self.targets)
        team_rows = [x for x in self.seed["issues"] if x.get("teamId") == team]
        before = sum(1 for x in team_rows if str(x.get("createdAt")) <= latest_plain)
        fillers = 50 - before
        if fillers < 0 or paged_at <= latest_plain:
            self.notes.append("page trap impossible: the team already fills the first page, or no later time that day")
            return []
        creators = [u["id"] for u in self.seed["users"] if u["id"] != row.get("creatorId")] or [row.get("creatorId")]
        start = datetime.fromisoformat(day) - timedelta(days=70)
        tname = next(t["name"] for t in self.seed["teams"] if t["id"] == team)
        for n in range(fillers):
            seedkit.clone(self.seed, self.domain, "issues", self.key, {
                "title": f"{tname} task {n + 1}", "description": None, "creatorId": creators[n % len(creators)],
                "assigneeId": None, "labelIds": [], "createdAt": (start + timedelta(hours=20 * n)).isoformat(),
                "updatedAt": (start + timedelta(hours=20 * n)).isoformat(), "identifier": f"FILL-{n}",
                "number": float(9000 + n), "branchName": f"fill-{n}", "cycleId": None, "projectId": None,
                "parentId": None, "dueDate": None, "estimate": None}, new_key=f"fill-{self.key}-{n}", follow=False)
        self.copy_target(3, "P", createdAt=paged_at, updatedAt=paged_at)
        return [f"past the first 50 issues ({fillers} older issues)"]

    def trap_slack_pinned(self):
        if "P" in self.drop:
            return []
        row = seedkit.find_row(self.case, "messages", self.key)
        t = utc(row["created_at"])
        day = t.date()
        p = datetime(day.year, day.month, day.day, 7, 10, tzinfo=timezone.utc)
        if t.astimezone(LA).date() != day or t - p < timedelta(minutes=10):
            self.notes.append("page trap impossible: no room before the target on the same day in UTC and LA")
            return []
        author_pinned = any((e.get("join") or {}).get("parent") == "user_id" for e in self.ref["query"].get("edges") or [])
        filler_text = (f"{self.words.capitalize()} check 1 passed." if (author_pinned and self.words)
                       else "Build 4100 deployed.")
        candidates = [m["user_id"] for m in self.seed.get("channel_members") or []
                      if m["channel_id"] == row["channel_id"] and m["user_id"] != row["user_id"]] or \
            [u["user_id"] for u in self.seed["users"] if u["user_id"] != row["user_id"]]
        # Only authors whose filler the request would not select (a filler must fail a condition).
        others = [u for u in dict.fromkeys(candidates) if not fdc.node_matches(
            self.seed, self.ref["query"], {**row, "user_id": u, "message_text": filler_text})]
        if not others:
            self.notes.append("page trap impossible: every author's filler would meet the request")
            return []
        n_fill = 110
        step = (t - p) / (n_fill + 2)
        self.copy_target(3, "P", _at=p)
        for n in range(n_fill):
            when = p + step * (n + 1)
            self.seq += 1
            ts = f"{int(when.timestamp())}.{self.seq:06d}"
            text = f"{self.words.capitalize()} check {n + 1} passed." if (author_pinned and self.words) \
                else f"Build {4100 + n} deployed."
            self.seed["messages"].append({"message_id": ts, "ts": ts, "channel_id": row["channel_id"],
                                          "user_id": others[n % len(others)], "message_text": text,
                                          "type": "message", "created_at": iso_z(when)})
        return ["past the first 100 messages of the channel"] + \
            (["a search crowd (the fillers mention the search words)"] if author_pinned and self.words else [])

    def trap_slack_open(self):
        row = seedkit.find_row(self.case, "messages", self.key)
        chan = next(c for c in self.seed["channels"] if c["channel_id"] == row["channel_id"])
        members = [m for m in self.seed.get("channel_members") or [] if m["channel_id"] == chan["channel_id"]]
        made = []
        for i, (code, cid, name, private) in enumerate((("C", "C_SMA_OPEN", "team-updates", False),
                                                        ("H", "C_SMA_PRIV", "leads", True)), 1):
            if code in self.drop:
                continue
            self.seed["channels"].append({**copy.deepcopy(chan), "channel_id": cid, "channel_name": name,
                                          "is_private": private, "topic_text": "", "purpose_text": ""})
            for m in members:
                self.seed["channel_members"].append({**copy.deepcopy(m), "channel_id": cid})
            self.copy_target(i, code, channel_id=cid)
            made.append("another channel" if code == "C" else "a private channel")
        return made

    # ---------------------------------------------------------------- checks
    def checks(self):
        problems = []
        self.ref["expected"] = list(self.targets)
        _, errors = fdc.check_reference(self.seed, self.ref)
        if errors:
            problems.append(f"fdc: {errors[:3]}")
        col = CONTAINER.get(self.table)
        if col:
            sizes = Counter(str(r.get(col)) for r in self.seed[self.table])
            big = {k: v for k, v in sizes.items() if v > PRACTICAL}
            if big:
                problems.append(f"impractical: containers over {PRACTICAL}: {big}")
        for t in self.targets:
            r = seedkit.find_row(self.case, self.table, t)
            stamp = r.get("created_at") if self.table == "messages" else r.get("createdAt") if self.table == "issues" \
                else None
            if stamp and utc(stamp).date() != utc(stamp).astimezone(LA).date():
                problems.append(f"date differs in UTC and Los Angeles for {t}")
        return problems


def finish(b: Builder, tier, answer, cover, suffix=""):
    case = b.case
    tid = f"SMA-{cover['case_id']}-{tier}{suffix}"
    case.update(case_id=tid, prompt=answer["plural_request"], mode="multiple", plural=True, form="present")
    b.ref.update(expected=list(b.targets), description=f"every record the plural request selects ({len(b.targets)})")
    case["cards"] = [{**(case.get("cards") or [{}])[0], "Test ID": tid, "Referent set": list(b.targets)}]
    case["task_spec"] = [{"line": 1, "text": answer["plural_request"], "obligations": [1]}]
    case.pop("_arm", None)
    case["source_cover"] = cover["case_id"]
    case["case_sha256"] = derive.digest(case)
    return case


def build_one(cover, answer, tiers=("E", "H"), suffix="", drop=(), no_variants=False):
    out = {"cover": cover["case_id"], "domain": cover["domain"], "table": cover["references"][0]["query"]["table"],
           "pinned": pinned(cover["references"][0]["query"]), "cases": {}}
    for tier in tiers:
        b = Builder(cover, answer, drop=drop, no_variants=no_variants)
        traps = []
        try:
            if tier == "E":
                b.copy_target(0, "V")
                b.copy_target(1, "V")
            else:
                b.copy_target(0, "V")
                kind = b.table
                if kind == "calendar_events" and not out["pinned"]:
                    traps = b.trap_calendar()
                elif kind == "box_files" and not out["pinned"]:
                    traps = b.trap_box()
                elif kind == "box_files":
                    traps = [t for t in [b.box_crowd()] if t]
                    traps = [f"a search crowd failing {traps[0]}"] if traps else []
                    if traps:  # the crowd precedes nothing here; a copy after it in search order
                        b.copy_target(1, "V")
                elif kind == "issues":
                    traps = b.trap_linear()
                elif kind == "messages" and out["pinned"]:
                    traps = b.trap_slack_pinned()
                elif kind == "messages":
                    traps = b.trap_slack_open()
                if not traps:
                    out["cases"][tier] = {"built": False, "why": "no applicable trap for this request", "notes": b.notes}
                    continue
        except Exception as exc:  # a construction the generic code cannot make: recorded, not raised
            out["cases"][tier] = {"built": False, "why": f"construction failed: {type(exc).__name__}: {exc}"[:300]}
            continue
        problems = b.checks()
        case = finish(b, tier, answer, cover, suffix)
        out["cases"][tier] = {"built": not problems, "id": case["case_id"], "targets": len(b.targets),
                              "traps": traps, "problems": problems, "notes": b.notes, "placements": b.place}
        if not problems:
            dest = OUT / cover["domain"] / f"{case['case_id']}.json"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(json.dumps(case, indent=1, default=str) + "\n")
    return out


def main(ids):
    answers = json.loads((HERE / "writer.json").read_text())
    report_path = HERE / "build.json"
    report = json.loads(report_path.read_text()) if report_path.exists() and ids else {}
    placements = json.loads((HERE / "placements.json").read_text()) if (HERE / "placements.json").exists() and ids \
        else {}
    for cover in covers():
        cid = cover["case_id"]
        if ids and cid not in ids:
            continue
        a = answers.get(cid)
        if not a or a.get("missing"):
            report[cid] = {"cover": cid, "skipped": "no writer answer"}
            continue
        if not a.get("plural_worthy"):
            report[cid] = {"cover": cid, "skipped": f"not plural-worthy: {a.get('reason')}"}
            continue
        if a.get("problems"):
            report[cid] = {"cover": cid, "skipped": f"wording: {a['problems']}"}
            continue
        r = build_one(cover, a)
        report[cid] = r
        for tier, c in r["cases"].items():
            if c.get("built"):
                placements[c["id"]] = c["placements"]
        status = {t: ("ok" if c.get("built") else (c.get("why") or c.get("problems"))) for t, c in r["cases"].items()}
        print(f"{cid:14} pinned={r['pinned']!s:5} {json.dumps(status)[:230]}")
    report_path.write_text(json.dumps(report, indent=1, default=str) + "\n")
    (HERE / "placements.json").write_text(json.dumps(placements, indent=1) + "\n")
    built = Counter(t for r in report.values() for t, c in (r.get("cases") or {}).items() if c.get("built"))
    print("built:", dict(built), "| skipped:", sum(1 for r in report.values() if r.get("skipped")))


def repair(drop_traps: bool):
    """Rebuild the cases the cold reader did not agree on, in two rounds (the first build and its trials stay on record).
    - Round 1 (`--repair`): each disagreed first build is rebuilt with every copy keeping the original text, all traps
      kept, as SMA-<cover>-ER / -HR. Most doubts were about a variant title, not a place.
    - Round 2 (`--repair2`): each repaired case the reader still did not agree on is rebuilt again without the traps
      whose targets the reader left out or doubted: those placements are contestable for this request."""
    answers = json.loads((HERE / "writer.json").read_text())
    verdicts = json.loads((HERE / "reader.json").read_text())
    report = json.loads((HERE / "build.json").read_text())
    placements = json.loads((HERE / "placements.json").read_text())
    by_id = {c["case_id"]: c for c in covers()}
    for cid, v in sorted(verdicts.items()):
        if v["agreed"] or cid.endswith("R") != drop_traps:
            continue
        cover_id, tier = cid.removeprefix("SMA-").rsplit("-", 1)
        tier = tier[0]
        doubtful = set(v["missing"]) | set(v["unsure"]) | set(v["extra"])
        drop = ({placements.get(cid, {}).get(t) for t in doubtful} - {None, "V"}) if drop_traps else set()
        r = build_one(by_id[cover_id], answers[cover_id], tiers=(tier,), suffix="R", drop=drop, no_variants=True)
        c = r["cases"].get(tier) or {}
        report[f"{cover_id}:{tier}R"] = {**r, "repair_of": cid, "dropped": sorted(drop), "round": 2 if drop_traps else 1}
        if c.get("built"):
            placements[c["id"]] = c["placements"]
        elif drop_traps:  # nothing valid is left of this hard case: remove the stale repaired file
            stale = OUT / r["domain"] / f"SMA-{cover_id}-{tier}R.json"
            stale.unlink(missing_ok=True)
        print(f"{cid:24} -> {c.get('id') or '-'} built={c.get('built')} dropped={sorted(drop)} "
              f"{c.get('why') or c.get('problems') or ''}")
    (HERE / "build.json").write_text(json.dumps(report, indent=1, default=str) + "\n")
    (HERE / "placements.json").write_text(json.dumps(placements, indent=1) + "\n")


if __name__ == "__main__":
    if "--repair" in sys.argv or "--repair2" in sys.argv:
        repair("--repair2" in sys.argv)
    else:
        main(set(sys.argv[1:]))
