"""A plausibility scan of the seeds of both writers' accepted scenarios, so that 'weak but valid' (implausible data)
is judged by one standard on both sides. No model calls.

    python3 grounding/runs/qwen_writer_01/eval/data_scan.py

Flags: a record created after its last modification; a Box file version dated before its file existed or a
version 1 dated after the file's creation; a hub item added before its hub existed; two active cycles of one Linear
team, or overlapping cycles of one team, or a cycle both active and next; a Slack conversation whose flags
conflict (a group conversation reported public, a DM with more than two members). Writes eval/data_scan.json.
"""
import json
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent
sys.path.insert(0, str(STUDY.parents[2]))
from grounding.runs.qwen_writer_01 import cases  # noqa: E402

MUSE = STUDY.parent / "autogen_02" / "runs" / "phase4_gen"


def t(v):
    if not v:
        return None
    try:
        d = datetime.fromisoformat(str(v).replace("Z", "+00:00"))
        return d.replace(tzinfo=None) if d.tzinfo is None else d.astimezone().replace(tzinfo=None)
    except ValueError:
        return None


def scan(case: dict) -> list[str]:
    s, out = case["seed"], []
    for table, rows in s.items():
        for r in rows if isinstance(rows, list) else []:
            if not isinstance(r, dict):
                continue
            c = t(r.get("created_at") or r.get("createdAt"))
            m = t(r.get("modified_at") or r.get("updated_at") or r.get("updatedAt"))
            if c and m and c > m:
                out.append(f"{table} {r.get('id')}: created {c:%Y-%m-%d %H:%M} after its last change {m:%Y-%m-%d %H:%M}")
    files = {str(f["id"]): f for f in s.get("box_files", [])}
    for v in s.get("box_file_versions", []):
        f = files.get(str(v.get("file_id")))
        if f and t(v.get("created_at")) and t(f.get("created_at")):
            if t(v["created_at"]) < t(f["created_at"]):
                out.append(f"box_file_versions {v.get('id')}: dated before its file existed")
            elif str(v.get("version_number")) == "1" and t(v["created_at"]) > t(f["created_at"]):
                out.append(f"box_file_versions {v.get('id')}: version 1 dated {t(v['created_at']):%Y-%m-%d}, after its file was created {t(f['created_at']):%Y-%m-%d}")
    hubs = {str(h["id"]): h for h in s.get("box_hubs", [])}
    for i in s.get("box_hub_items", []):
        h = hubs.get(str(i.get("hub_id")))
        if h and t(i.get("added_at")) and t(h.get("created_at")) and t(i["added_at"]) < t(h["created_at"]):
            out.append(f"box_hub_items {i.get('id')}: added {t(i['added_at']):%Y-%m-%d}, before its hub was created {t(h['created_at']):%Y-%m-%d}")
    by_team = {}
    for cy in s.get("cycles", []):
        by_team.setdefault(cy.get("teamId"), []).append(cy)
        if cy.get("isActive") and cy.get("isNext"):
            out.append(f"cycles {cy['id']}: both active and next")
    for team, cys in by_team.items():
        active = [c["id"] for c in cys if c.get("isActive")]
        if len(active) > 1:
            out.append(f"cycles of {team}: {len(active)} active ({', '.join(active)})")
        spans = sorted((t(c.get("startsAt")), t(c.get("endsAt")), c["id"]) for c in cys if c.get("startsAt") and c.get("endsAt"))
        for (s1, e1, a), (s2, e2, b) in zip(spans, spans[1:]):
            if s2 < e1:
                out.append(f"cycles {a} and {b} of {team} overlap")
    members = {}
    for m in s.get("channel_members", []):
        members.setdefault(m.get("channel_id"), set()).add(m.get("user_id"))
    for ch in s.get("channels", []):
        if ch.get("is_gc") and not ch.get("is_private"):
            out.append(f"channels {ch['channel_id']}: a group conversation reported public (named '{ch.get('channel_name')}')")
        if ch.get("is_dm") and len(members.get(ch["channel_id"], ())) > 2:
            out.append(f"channels {ch['channel_id']}: a DM with {len(members[ch['channel_id']])} members")
    return out


def main():
    plan = json.loads((STUDY / "plan.json").read_text())
    drawn = [sid for d in sorted(plan["drawn"]) for sid in plan["drawn"][d]]
    qwen = cases.accepted()
    result = {}
    for sid in drawn:
        result[sid] = {"muse": scan(json.loads((MUSE / sid / "case.json").read_text())),
                       "qwen": scan(json.loads((qwen[sid] / "case.json").read_text())) if sid in qwen else None}
    (HERE / "data_scan.json").write_text(json.dumps(result, indent=1) + "\n")
    for sid, r in result.items():
        print(sid)
        for who in ("muse", "qwen"):
            print(f"  {who}: {r[who] if r[who] is not None else 'not accepted yet'}")


if __name__ == "__main__":
    main()
