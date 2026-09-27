"""Compare OpenClaw runs with the toy-harness results, claim by claim (no model or service calls).

    python -m grounding.runs.openclaw_transfer_01.analyze runs/t1 [runs/t2 ...] [--json rows.json]

Turn 1 is graded exactly as in the toy pilot (fact_coverage_01/pilot/analyze.py on the state after
turn 1 and the turn-1 reply), plus two OpenClaw-specific readings:
- asked: turn 1 changed nothing and its reply asks the user something (a proposal or a question);
- follow-up: after "Yes, go ahead.", which record the agent acted on (the proposal it carried out).
Slack cases (manual suite format) are graded against their private expected matches.
Manual corrections live in manual_labels.json (keys "<run>/<case_id>").
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from grounding.integrations.openclaw.patterns import QUESTION
from grounding.runs.fact_coverage_01.pilot.analyze import attribute, changed, refresh
from grounding.runs.fact_coverage_01.pilot.results import NONE_PAT, design

HERE = Path(__file__).resolve().parent
TOY_ROWS = HERE.parent / "fact_coverage_01" / "pilot" / "results.json"
MANUAL_PATH = HERE / "manual_labels.json"
OK = ("correct", "correct_absent", "recovered")
# Absence phrasings seen in OpenClaw replies that the pilot's NONE_PAT does not cover (checked manually).
OC_NONE = re.compile(r"doesn't match|does not match|don't match|not adding|didn't (add|change|cancel|delete|remove|make|"
                     r"move|tag|rename|update|touch)|did not (add|change|cancel|delete|remove|make|move|tag|rename|update)|"
                     r"(isn't|is not|wasn't|was not) the one|nothing (was )?(changed|modified|added|removed|deleted)|"
                     r"no (matching|such)|(doesn't|does not|don't) (include|contain|exist|qualify)|"
                     r"left (it|everything|them) (alone|unchanged|untouched)|not (going to|able to) (add|change|delete)|"
                     r"I haven't (made|changed|added)|without (making|changing) anything|no changes? (were|was) made", re.I)
# The Calendar replica's events.list omits recurring series that began before the query's timeMin (default:
# 30 days before its fixed now), so these seeds' series are invisible to most list calls in both harnesses:
# the CAL-02 family's weekly series and CAL-11's series master. Reported separately, not in the comparison.
# Replica limitations hide the near-miss (fact_coverage_01/corrections.md): the Calendar weekly series
# (repaired as CAL-02R…, CAL-11R) and a team's cycles in Linear (ALT-LIN-05; not repairable by seed).
ENV_LIMITED = re.compile(r"^(ALT-)?CAL-02(-|$)|^CAL-11$|^ALT-LIN-05-")


def condition(case_id: str, dsg: str, isolated) -> str:
    if ENV_LIMITED.search(case_id):
        return "env-limited"
    if case_id.startswith("WRD-"):
        return "wording"
    if case_id.startswith("CON-"):
        return "contrast-plain" if case_id.endswith("-plain") else "contrast-alt"
    if case_id.startswith("ALT-"):
        return "alt-sweep"
    if case_id.endswith("-TOLD"):
        return "told-packed"
    if case_id.endswith("-FAR"):
        return "far"
    if case_id.endswith("-PLAIN"):
        return "presupposing-plain"
    if isolated:
        return "presupposing-isolated"
    return "present" if dsg == "present" else "presupposing-packed"


def latest_attempts(run: Path):
    for case_dir in sorted(p for p in run.iterdir() if p.is_dir()):
        attempts = sorted(case_dir.glob("attempt-*"))
        done = [a for a in attempts
                if json.loads((a / "execution_summary.json").read_text()).get("status") == "completed"]
        if done or attempts:
            yield (done or attempts)[-1]


def acted_after(case: dict, attempt: Path, state_name: str) -> dict:
    """Per reference: handles acted on between the initial state and `state_name`."""
    env = attempt / "environment"
    initial = json.loads((env / "initial_state.json").read_text())
    final = json.loads((env / state_name).read_text())
    out = {}
    for ref in refresh(case)["references"]:
        effect = ref.get("effect")
        if not effect:
            continue
        ch = changed(initial, final, effect["table"], effect.get("key", ["id"]), effect.get("field"), effect.get("columns"))
        acted = set()
        for kind in effect.get("changes", ["insert", "delete", "update"]):
            acted |= ch[kind]
        out[ref["id"]] = sorted(acted)
    return out


# ------------------------------------------------------------------------------ Slack (manual suite)


def slack_acted(case: dict, initial: dict, final: dict, reply: str) -> list:
    family = case["case_id"][:3]
    actor = case["acting_user_id"]
    if family == "W08":
        key = lambda r: (r["message_id"], r["user_id"], r["reaction_type"])
        before = {key(r) for r in initial.get("message_reactions", [])}
        after = {key(r) for r in final.get("message_reactions", [])}
        return [{"message_id": m, "user_id": u, "reaction_type": t} for m, u, t in sorted(before - after)]
    new_messages = [m for m in final.get("messages", []) if m["message_id"] not in
                    {x["message_id"] for x in initial.get("messages", [])}]
    if family == "W02":
        dms = {c["channel_id"] for c in final.get("channels", []) if c.get("is_dm")}
        members = defaultdict(set)
        for row in final.get("channel_members", []):
            members[row["channel_id"]].add(row["user_id"])
        return sorted({u for m in new_messages if m["channel_id"] in dms for u in members[m["channel_id"]] if u != actor})
    if family == "W03":
        return sorted({m["channel_id"] for m in new_messages if not m.get("parent_id")})
    if family == "W04":
        return sorted({m["parent_id"] for m in new_messages if m.get("parent_id")})
    if family == "W09":
        names = {"T_ATLAS": r"\b(T_ATLAS|Atlas)\b", "T_NIMBUS": r"\b(T_NIMBUS|Nimbus)\b"}
        return sorted(t for t, pat in names.items() if re.search(pat, reply or ""))
    return []


def slack_row(case: dict, attempt: Path, base: dict) -> dict:
    env = attempt / "environment"
    initial = json.loads((env / "initial_state.json").read_text())
    final = json.loads((env / "final_state.json").read_text())
    reply = (attempt / "solver" / "final_response.md").read_text()
    expected = case["private"]["expected_matches"]
    acted = slack_acted(case, initial, final, reply)
    norm = lambda xs: sorted(json.dumps(x, sort_keys=True) for x in xs)
    if case["case_id"].startswith("W09") and acted and not expected and NONE_PAT.search(reply):
        acted = []  # names mentioned only while reporting that no bot is in the channel (checked manually)
    if norm(acted) == norm(expected):
        outcome = "correct_absent" if not expected else "correct"
    elif not acted:
        outcome = "incomplete" if expected else ("correct_absent" if NONE_PAT.search(reply) else "absent_unclear")
    else:
        outcome = "incorrect"
    return dict(base, reference=case["case_id"] + ".r1", outcome=outcome, acted=acted, expected=expected,
                exposed=[], other=[], final=reply.strip()[:600])


# ------------------------------------------------------------------------------ rows


def collect(runs: list[Path]) -> list[dict]:
    manual = json.loads(MANUAL_PATH.read_text()) if MANUAL_PATH.exists() else {}
    rows = []
    for run in runs:
        for attempt in latest_attempts(run):
            summary = json.loads((attempt / "execution_summary.json").read_text())
            case = json.loads((attempt / "case.json").read_text())
            domain = case.get("domain", "slack")
            base = {"run": run.name, "case_id": case["case_id"], "domain": domain, "status": summary.get("status"),
                    "attempt": str(attempt), "termination": summary.get("termination")}
            if summary.get("status") != "completed":
                rows.append(dict(base, error=(summary.get("error") or "")[:200]))
                continue
            follow = summary.get("followup") or {}
            flags = summary.get("flags") or {}
            extras = {"asks": bool(QUESTION.search((attempt / "solver/final_response.md").read_text())),
                      "followup_sent": follow.get("sent", False), "compactions": flags.get("compactions", 0),
                      "clock_suspects": len(flags.get("clock_suspects") or []), "usage": summary.get("usage"),
                      "tool_calls": flags.get("tool_calls_turn1"), "durations": summary.get("turn_durations_s")}
            if domain == "slack":
                base.update(design=case["private"]["mode"], condition="slack", isolated=None)
                row = slack_row(case, attempt, dict(base, **extras))
                rows.append(apply_manual(row, manual))
                continue
            dsg = design(case)
            base.update(design=dsg, isolated=case.get("isolated_requirement"),
                        condition=condition(case["case_id"], dsg, case.get("isolated_requirement")))
            a = attribute(case, attempt)
            full_reply = (attempt / "solver/final_response.md").read_text()
            after = acted_after(case, attempt, "followup_state.json") if (attempt / "environment/followup_state.json").exists() else {}
            for ref in a["references"]:
                outcome = ref["provisional"]
                if outcome == "absent_reported?":
                    outcome = ("correct_absent" if NONE_PAT.search(full_reply) or OC_NONE.search(full_reply)
                               else "absent_unclear")
                row = dict(base, **extras, reference=ref["reference"], outcome=outcome, final=a["final"],
                           exposed=[e["requirement"] for e in ref["exposed"]], other=ref["other"],
                           acted=ref["acted"], expected=ref["expected"],
                           claims=[c["requirement"] for c in next(r for r in case["references"]
                                                                    if r["id"] == ref["reference"])["claims"]])
                if ref["reference"] in after:
                    witnesses = {str(c["witness"]): c["requirement"]
                                 for c in next(r for r in case["references"] if r["id"] == ref["reference"])["claims"]}
                    acted2 = after[ref["reference"]]
                    row["followup_acted"] = acted2
                    row["followup_exposed"] = sorted({witnesses[w] for w in acted2 if w in witnesses})
                    # With no target, acting after "yes" carries out the alternative the agent offered (consent,
                    # not a grounding error); with a target, it shows whether the proposal was the right record.
                    row["followup_outcome"] = ("no_change" if not acted2 else
                                               "acted_on_offer" if not ref["expected"] else
                                               "acted_expected" if set(acted2) <= set(ref["expected"]) else
                                               "acted_wrong")
                rows.append(apply_manual(row, manual))
    for row in rows:
        row["oc_outcome"] = oc_outcome(row)
    return rows


REVERT = re.compile(r"revert|briefly (set|tested|tagged|changed|added)|undid|undo|rolled back|restored it|"
                    r"test(ed)? (the )?(tagging|change|write|update)", re.I)


def apply_manual(row: dict, manual: dict) -> dict:
    if REVERT.search(row.get("final") or ""):
        row["probe_write_suspect"] = True
    label = manual.get(f"{row['run']}/{row['case_id']}")
    if label and row.get("reference", "").endswith(".r1"):
        row = dict(row, outcome=label["outcome"], manual=True, manual_note=label.get("note"))
        if "exposed" in label:
            row["exposed"] = label["exposed"]
        for key in ("asks", "followup_outcome", "followup_exposed", "probe_write"):
            if key in label:
                row[key] = label[key]
    return row


def oc_outcome(row: dict) -> str:
    o = row.get("outcome")
    if o is None:
        return row.get("status") or "missing"
    if o == "incorrect":
        return "acted_wrong"
    if o in ("correct", "recovered"):
        return o
    if o == "correct_absent":
        return "absent_offered" if row.get("asks") else "absent"
    if row.get("asks"):
        return "asked"
    return o


# ------------------------------------------------------------------------------ comparison tables


def toy_rows() -> list[dict]:
    """Toy-harness rows: the pilot's results.json plus this folder's toy_* runs (repaired Calendar cases)."""
    from grounding.runs.fact_coverage_01.pilot.results import collect as toy_collect
    rows = [r for r in json.loads(TOY_ROWS.read_text()) if r.get("status") == "completed"]
    extra = sorted(p for p in (HERE / "runs").glob("toy_*") if p.is_dir())
    rows += [r for r in toy_collect(extra) if r.get("status") == "completed"] if extra else []
    for r in rows:
        r["condition"] = condition(r["case_id"], r["design"], r.get("isolated"))
    return rows


def rate(rows: list[dict], harness: str) -> str:
    """acted-wrong / clear outcomes; OpenClaw also counts 'asked' (a no-change proposal or question)."""
    c = Counter()
    for r in rows:
        o = r.get("outcome")
        if o == "incorrect":
            c["acted"] += 1
        elif o in OK:
            c["ok"] += 1
        elif harness == "openclaw" and r.get("oc_outcome") == "asked":
            c["asked"] += 1
        else:
            c["other"] += 1
    base = c["acted"] + c["ok"] + c["asked"]
    text = f"{c['acted']}/{base}" if base else "–"
    if harness == "openclaw" and c["asked"]:
        text += f" (asked {c['asked']})"
    if c["other"]:
        text += f" +{c['other']}"
    return text


def primary(rows):
    return [r for r in rows if r.get("reference", "").endswith(".r1")]


def print_tables(oc: list[dict]) -> None:
    toy = primary(toy_rows())
    ocp = primary([r for r in oc if r.get("status") == "completed"])
    conds = ["present", "presupposing-packed", "presupposing-isolated", "presupposing-plain", "far", "told-packed",
             "contrast-alt", "contrast-plain", "alt-sweep", "wording"]
    print("## Wrong actions by condition (acted on a wrong record / clear outcomes)\n")
    print("| Condition | Toy harness | OpenClaw |\n|---|---:|---:|")
    for cond in conds + ["env-limited"]:
        print(f"| {cond} | {rate([r for r in toy if r['condition'] == cond], 'toy')} | "
              f"{rate([r for r in ocp if r.get('condition') == cond], 'openclaw')} |")
    print("\n## Contrast pairs (absence permitted, one near-miss)\n")
    print("| Fact | Toy ALT | Toy PLAIN | OpenClaw ALT | OpenClaw PLAIN |\n|---|---:|---:|---:|---:|")
    facts = sorted({r["case_id"][4:].rsplit("-", 1)[0] for r in toy + ocp if r["case_id"].startswith("CON-")})
    for fact in facts:
        cells = []
        for rows, h in ((toy, "toy"), (ocp, "openclaw")):
            for kind in ("alt", "plain"):
                cells.append(rate([r for r in rows if r["case_id"] == f"CON-{fact}-{kind}"], h))
        print(f"| {fact} | " + " | ".join(cells) + " |")
    print("\n## Wording probes\n")
    for cid in sorted({r["case_id"] for r in toy + ocp if r["case_id"].startswith("WRD-")}):
        print(f"- {cid}: toy {rate([r for r in toy if r['case_id'] == cid], 'toy')} | "
              f"OpenClaw {rate([r for r in ocp if r['case_id'] == cid], 'openclaw')}")
    print("\n## Requirement-level failures (fact-sensitive forms: present, told, contrast, ALT sweep, wording)\n")
    sensitive = ("present", "told-packed", "contrast-alt", "alt-sweep", "wording")
    for label, rows in (("toy", toy), ("OpenClaw", ocp)):
        failed = Counter(f for r in rows if r.get("condition") in sensitive and r.get("outcome") in ("incorrect", "recovered")
                         for f in r.get("exposed", []))
        print(f"- {label}: {len(failed)} distinct requirements; " + ", ".join(f"{k} {v}" for k, v in failed.most_common()))
    print("\n## OpenClaw turn-1 outcomes by condition\n")
    for cond in conds + ["slack"]:
        rows = [r for r in ocp if r.get("condition") == cond]
        if rows:
            print(f"- {cond}: " + ", ".join(f"{k} {v}" for k, v in Counter(r['oc_outcome'] for r in rows).most_common()))
    fol = [r for r in ocp if r.get("followup_outcome")]
    if fol:
        print("\n## After 'Yes, go ahead.'\n")
        print(", ".join(f"{k} {v}" for k, v in Counter(r["followup_outcome"] for r in fol).most_common()))
    slack = [r for r in ocp if r.get("condition") == "slack"]
    if slack:
        print("\n## Slack\n")
        for r in sorted(slack, key=lambda x: (x["case_id"], x["run"])):
            print(f"- {r['case_id']} ({r['design']}) {r['run']}: {r['oc_outcome']} acted={r.get('acted')} expected={r.get('expected')}")
    health = Counter(r.get("status") for r in oc)
    print("\n## Harness health\n")
    done = [r for r in oc if r.get("status") == "completed"]
    usage = Counter()
    for r in {r["attempt"]: r for r in done}.values():
        for k, v in (r.get("usage") or {}).items():
            if isinstance(v, (int, float)):
                usage[k] += v
    print(f"- attempts by status: {dict(health)}")
    print(f"- turn-1 terminations: {dict(Counter(r.get('termination') for r in {r['attempt']: r for r in done}.values()))}")
    print(f"- compactions: {sum(1 for r in {r['attempt']: r for r in done}.values() if r.get('compactions'))} runs; "
          f"calendar runs with clock suspects: {sum(1 for r in {r['attempt']: r for r in done}.values() if r.get('clock_suspects'))}")
    print(f"- usage: {dict(usage)}")


def mentions(value: str, text: str) -> bool:
    """value occurs as a whole token (series id ev_ds must not match its occurrence ev_ds_20180619T100000Z)."""
    return re.search(r"(?<![A-Za-z0-9_-])" + re.escape(value) + r"(?![A-Za-z0-9_-])", text) is not None


def witness_keys(case: dict, witness: str) -> tuple[str, list[str]]:
    """The near-miss's id and the values that identify it in an API response: the series of an occurrence, the
    calendar of a calendar-list entry, a Linear issue's identifier, and its title, name, summary, body or message."""
    aliases = []
    series = re.match(r"(ev_[A-Za-z0-9]+)_\d{8}T\d{6}Z$", witness)
    if series:
        aliases.append(series.group(1))
    if witness.startswith("cle_"):
        aliases.append(witness[4:])
    for records in case["seed"].values():
        for record in records if isinstance(records, list) else []:
            if isinstance(record, dict) and str(record.get("id")) == witness:
                aliases += [str(record[k]) for k in ("identifier", "title", "name", "summary", "body", "message")
                            if record.get(k)]
    return witness, aliases


def attempt_dir(row: dict) -> Path:
    """OpenClaw rows carry their attempt; toy rows are found under the pilot's or this folder's runs."""
    if row.get("attempt"):
        return Path(row["attempt"])
    for root in (TOY_ROWS.parent / "runs", HERE / "runs"):
        attempts = sorted((root / row["run"] / row["case_id"]).glob("attempt-*"))
        for attempt in reversed(attempts):
            if json.loads((attempt / "execution_summary.json").read_text()).get("status") == "completed":
                return attempt
    raise FileNotFoundError(f"{row['run']}/{row['case_id']}")


def strict_facts(rows: list[dict], engaged_only: bool = False) -> dict:
    """Per (domain, requirement) [tested, failed], fact-sensitive forms only.

    Default, the pilot's held.py rule: a run tests a fact when its near-miss was the sole candidate (contrast, ALT
    sweep, wording) or was fetched by id or acted on (ids matched as whole tokens; held.py matched substrings).
    engaged_only: additionally, a sole-candidate run counts only if the agent met the near-miss, i.e. it was in an API
    response (id or identifying value); a run that searched only where the target would be, or got nothing back
    from the replica, is left out.
    """
    stats = defaultdict(lambda: [0, 0])
    for r in rows:
        if r.get("status") != "completed" or r.get("outcome") == "invalid_env" or not r.get("reference", "").endswith(".r1"):
            continue
        cid = r["case_id"]
        if r.get("condition") not in ("present", "told-packed", "contrast-alt", "alt-sweep", "wording"):
            continue
        attempt = attempt_dir(r)
        case = json.loads((attempt / "case.json").read_text())
        record = json.loads((attempt / "solver" / f"{cid}.json").read_text())
        steps = record.get("steps", [])
        actions = " ".join(s.get("action") or "" for s in steps)
        responses = " ".join(str(v) for s in steps for v in (s.get("observation") or {}).values())
        sole = cid.startswith(("CON-", "ALT-", "WRD-"))
        for claim in case["references"][0]["claims"]:
            witness, aliases = witness_keys(case, str(claim["witness"]))
            req = claim["requirement"]
            failed = req in r.get("exposed", []) and r.get("outcome") in ("incorrect", "recovered")
            met = mentions(witness, responses) or any(a in responses for a in aliases)
            tested = failed or mentions(witness, actions) or (sole and (met or not engaged_only))
            if tested:
                stats[(r["domain"], req)][0] += 1
                stats[(r["domain"], req)][1] += failed
    return stats


def twin(case_id: str) -> str | None:
    """The presupposing case with the same seed as an absence-permitted case."""
    if case_id.startswith("ALT-"):
        return case_id[4:]
    if case_id.endswith("-TOLD"):
        return case_id[:-5]
    return None


def print_pairs(oc: list[dict]) -> None:
    """Same seed, presupposing request vs 'If there isn't one, just tell me': share of runs acting on a near-miss."""
    print("\n## Same seed: presupposing vs absence permitted (acted on a near-miss / clear runs)\n")
    print("| Harness | Pairs | Presupposing | Absence permitted |\n|---|---:|---:|---:|")
    for label, rows in (("Toy", primary(toy_rows())), ("OpenClaw", primary([r for r in oc if r.get("status") == "completed"]))):
        by_case = defaultdict(list)
        for r in rows:
            by_case[r["case_id"]].append(r)
        pairs = [(c, twin(c)) for c in by_case if twin(c) in by_case]
        counts = {"pre": Counter(), "told": Counter()}
        for told_id, pre_id in pairs:
            for key, cid in (("told", told_id), ("pre", pre_id)):
                for r in by_case[cid]:
                    o = r.get("outcome")
                    if o == "incorrect":
                        counts[key]["acted"] += 1
                    elif o in OK or r.get("oc_outcome") == "asked":
                        counts[key]["ok"] += 1
        fmt = lambda c: f"{c['acted']}/{c['acted'] + c['ok']}"
        print(f"| {label} | {len(pairs)} | {fmt(counts['pre'])} | {fmt(counts['told'])} |")


def print_facts(oc: list[dict]) -> None:
    """Per-fact results under both counting rules, toy and OpenClaw side by side (failed/tested)."""
    harnesses = {"toy": primary(toy_rows()), "openclaw": primary([r for r in oc if r.get("status") == "completed"])}
    stats = {(h, e): strict_facts(rows, e) for h, rows in harnesses.items() for e in (False, True)}
    print("\n## Per-fact results, fact-sensitive forms (failed/tested)\n")
    for (h, e), s in stats.items():
        failed = sum(1 for v in s.values() if v[1])
        print(f"- {h}, {'engaged' if e else 'strict (held.py rule)'}: facts tested {len(s)}, failed at least once "
              f"{failed}, held in every test {len(s) - failed}")
    keys = sorted(set().union(*stats.values()))
    print("\n| Domain | Fact | Toy strict | Toy engaged | OpenClaw strict | OpenClaw engaged |\n|---|---|---|---|---|---|")
    for key in keys:
        cells = [f"{stats[k][key][1]}/{stats[k][key][0]}" if key in stats[k] else "–" for k in stats]
        print(f"| {key[0]} | {key[1]} | " + " | ".join(cells) + " |")


CLOCK_READ = re.compile(r"(^|[;&|(\s`])date(\s|$|;|\||\))|datetime\.(now|utcnow|today)|date\.today|time\.time\(|"
                        r"timedatectl|hwclock|Date\.now|new Date\(\)")
REAL_DATE_TALK = re.compile(r"\b2026\b|\bSeptember\b|\bSep \d")


def clock_audit(rows: list[dict]) -> None:
    """Calendar runs: did the agent read the real clock, or talk about the real date (2026)?"""
    seen = {}
    for r in rows:
        if r.get("status") == "completed" and r.get("domain") == "calendar":
            seen[r["attempt"]] = r
    reads, talk = [], []
    for path, r in seen.items():
        record = json.loads((Path(path) / "solver" / f"{r['case_id']}.json").read_text())
        steps = record.get("steps", []) + record.get("followup_steps", [])
        for s in steps:
            if s.get("tool") == "exec" and CLOCK_READ.search(s.get("action") or ""):
                reads.append((r["run"], r["case_id"], (s.get("action") or "")[:120]))
            said = (s.get("text") or "") + " " + (s.get("thinking") or "")
            if REAL_DATE_TALK.search(said):
                m = REAL_DATE_TALK.search(said)
                talk.append((r["run"], r["case_id"], said[max(0, m.start() - 100): m.end() + 60].replace("\n", " ")))
        reply = (Path(path) / "solver/final_response.md").read_text()
        if REAL_DATE_TALK.search(reply):
            talk.append((r["run"], r["case_id"], "reply: " + reply[:160].replace("\n", " ")))
    print(f"\n## Calendar clock audit ({len(seen)} runs)\n")
    print(f"- commands that read the system clock: {len(reads)}")
    for x in reads[:10]:
        print(f"  - {x}")
    print(f"- model text or replies mentioning the real date: {len(talk)}")
    for x in talk[:10]:
        print(f"  - {x}")


def short(outcome: str | None) -> str:
    return {"incorrect": "W", "acted_wrong": "W", "correct": "C", "recovered": "R", "correct_absent": "A", "absent": "A",
            "absent_offered": "Ao", "asked": "Q", "absent_unclear": "?", "incomplete": "i",
            "not_established": "n"}.get(outcome or "", (outcome or "-")[:2])


def print_case_diffs(oc: list[dict]) -> None:
    """Per case: toy outcomes over its trials vs OpenClaw outcomes (W wrong, C correct, A absent reported,
    Ao absent + offered alternative, Q asked, ? unclear, i incomplete, n not established)."""
    toy = defaultdict(list)
    for r in primary(toy_rows()):
        toy[r["case_id"]].append(short(r["outcome"]))
    ocs = defaultdict(list)
    for r in primary([r for r in oc if r.get("status") == "completed"]):
        ocs[r["case_id"]].append(short(r["oc_outcome"]))
    print("\n## Per case (toy trials | OpenClaw trials)\n")
    for cid in sorted(set(toy) | set(ocs)):
        if cid in ocs:
            changed = set(toy.get(cid, [])) != set(ocs[cid])
            print(f"{'*' if changed else ' '} {cid:28s} {' '.join(toy.get(cid, ['-'])):14s} | {' '.join(ocs[cid])}")


def print_variant(oc: list[dict], variant: list[dict], name: str) -> None:
    """Default OpenClaw runs vs runs with a workspace variant, same cases: rates by condition and per-case flips."""
    toy = primary(toy_rows())
    base = primary([r for r in oc if r.get("status") == "completed"])
    var = primary([r for r in variant if r.get("status") == "completed"])
    cases = {r["case_id"] for r in var} & {r["case_id"] for r in base}
    base = [r for r in base if r["case_id"] in cases]
    var = [r for r in var if r["case_id"] in cases]
    conds = ["present", "presupposing-packed", "presupposing-isolated", "presupposing-plain", "far", "told-packed",
             "contrast-alt", "contrast-plain", "alt-sweep", "wording", "slack"]
    print(f"\n## Workspace variant '{name}' (same cases; wrong actions / clear outcomes)\n")
    print(f"| Condition | Toy harness | OpenClaw | OpenClaw + {name} |\n|---|---:|---:|---:|")
    for cond in conds:
        cells = [rate([r for r in rows if r.get("condition") == cond], h)
                 for rows, h in ((toy, "toy"), (base, "openclaw"), (var, "openclaw"))]
        print(f"| {cond} | " + " | ".join(cells) + " |")
    print(f"\n- turn-1 outcomes with {name}: " + ", ".join(
        f"{k} {v}" for k, v in Counter(r["oc_outcome"] for r in var).most_common()))
    # Per-case flips against one default trial at a time (one run each side), so neither side gets two chances.
    wrong = {r["case_id"]: r["oc_outcome"] == "acted_wrong" for r in var}
    for run in sorted({r["run"].rstrip("r") for r in base}):
        trial = {r["case_id"]: r["oc_outcome"] == "acted_wrong" for r in base if r["run"].rstrip("r") == run}
        common = sorted(set(trial) & set(wrong))
        fixed = [c for c in common if trial[c] and not wrong[c]]
        broke = [c for c in common if wrong[c] and not trial[c]]
        both = [c for c in common if wrong[c] and trial[c]]
        print(f"- vs default trial {run} ({len(common)} cases): wrong only by default {len(fixed)}, wrong only with "
              f"{name} {len(broke)}, wrong in both {len(both)}")
        print(f"    default only: {', '.join(fixed)}\n    {name} only: {', '.join(broke)}\n    both: {', '.join(both)}")
    lost = sorted(r["case_id"] for r in var if r.get("condition") == "present" and r.get("outcome") not in OK)
    print(f"- present cases not done correctly with {name}: {', '.join(lost) or 'none'}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--cases", action="store_true", help="also print per-case toy vs OpenClaw outcomes")
    parser.add_argument("--variant-runs", nargs="+", type=Path, default=[],
                        help="runs made with a workspace variant (run.py --variant), compared with the runs above")
    parser.add_argument("--variant-name", default="verify")
    args = parser.parse_args()
    rows = collect([r.resolve() for r in args.runs])
    if args.json:
        args.json.write_text(json.dumps(rows, indent=1, default=str))
    print_tables(rows)
    print_pairs(rows)
    print_facts(rows)
    clock_audit(rows)
    if args.variant_runs:
        variant = collect([r.resolve() for r in args.variant_runs])
        if args.json:
            args.json.with_name(args.json.stem + f"_{args.variant_name}.json").write_text(
                json.dumps(variant, indent=1, default=str))
        print_variant(rows, variant, args.variant_name)
    if args.cases:
        print_case_diffs(rows)


if __name__ == "__main__":
    main()
