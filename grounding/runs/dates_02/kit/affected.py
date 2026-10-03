"""Which tests in the denominator tables the dates affected, how, and what each agent's runs show. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.dates_02.kit.affected

Per test (numbers/population.json; templates and anchors from build.py):

- **Dated 2018**: every Calendar test (scenarios and boundary tests). The agent ran under a clock set to Sunday
  2018-06-17; its own sense of the year is 2025-2026. Trial evidence, from the runner's own flags
  (`clock_suspects`): the model's text or final reply names a year 2023-2029 (`real_year_in_model_text`,
  `real_year_in_reply`; recorded for Qwen, whose reasoning is kept; Sol's is not), a tool output showed one
  (`real_year_in_tool_output`: `date`, an HTTP header, a file time), or the agent ran a command that reads the clock
  (`time_command`).
- **Run under a day other than the one it was designed for, where the day matters**: the designed day (the anchor)
  against the clock each trial ran under; the day matters when a condition of the request is read against today
  ("overdue", "the current cycle", a weekday).
- **Not run**: an agent with no trial of a test the other agent ran.
- **Stale as written**: the first day from 2026-10-03 on which the test, run as written on the real clock (no clock
  shift, no rendering), no longer has its designed answer, and why.

For every affected test, each agent's trials and outcome (a trial's folder is <run>/<trial>/<test>/attempt-01 under
the run's study unless `attempt` says otherwise; `run` names the run folder): a regular item failed when its test exposed its fact in a
trial (the adjudicated lists denominator_01 reads); a policy item when a trial failed (judge v2's incorrect or
presented, or over the budget). For Calendar, whether a failure rests only on trials that show the year confusion.
Writes numbers/affected.json.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.autogen_02.kit import sampler
from grounding.runs.dates_02.kit import templates
from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.report_01.kit.common import RUNS, load

HERE = Path(__file__).resolve().parents[1]
TODAY = date(2026, 10, 3)
VERDICT_ROOTS = [RUNS / "openclaw_eval_01/runs", RUNS / "regen_01/runs", RUNS / "sol_eval_01/eval"]
YEAR_FLAGS = ("real_year_in_model_text", "real_year_in_reply")
POLICY_KINDS = ("absence", "underspecified", "by-product unit")


def verdict_index() -> dict[str, dict]:
    out = {}
    for root in VERDICT_ROOTS:
        for p in root.rglob("verdict.json"):
            if not any(part.startswith("judged_") for part in p.parts):
                continue
            v = json.loads(p.read_text())
            a = v.get("attempt") or ""
            i = a.find("grounding/runs/")
            if i >= 0:
                out[a[i + len("grounding/runs/"):]] = v
    return out


def trial_outcome(t: dict, verdicts: dict, policy: bool) -> dict:
    v = verdicts.get(t["path"])
    over = rulings.over_budget(RUNS / t["path"]) if t["status"] == "completed" else False
    outcome = v.get("outcome") if v else ("not judged" if t["status"] == "completed" else t["status"])
    if policy and over:
        outcome = "incorrect"
    return {"agent": t["agent"], "run": t["run"], "trial": t["trial"], "clock": (t["clock"] or "real")[:10],
            "ran_on": (t["started"] or "")[:10], "flags": sorted(set(t["clock_suspects"])), "outcome": outcome,
            "exposed": (v or {}).get("exposed") or [], "over_budget": over, "path": t["path"]}


# ------------------------------------------------------------------------------------------- stale as written


def _issues(seed):
    states = {s["id"]: s.get("type") for s in seed.get("workflow_states", [])}
    return [(i["id"], i.get("dueDate"), states.get(i.get("stateId"))) for i in seed.get("issues", [])]


def _filters(node):
    for f in node.get("filters") or []:
        yield f
    for e in node.get("edges") or []:
        yield from _filters(e.get("node") or {})


def _select(seed: dict, query: dict, day: date) -> list:
    """The query's selection with its conditions relative to today read against `day`: "overdue" as due before that
    day, "the current cycle" as the team's cycle whose dates hold that day (noon UTC)."""
    import copy
    from grounding.runs.fact_coverage_01 import fdc
    q = copy.deepcopy(query)
    noon = datetime.combine(day, datetime.min.time(), timezone.utc) + timedelta(hours=12)
    for f in _filters(q):
        if f.get("fact") == "D:overdue" and f.get("field") == "dueDate":
            f["value"] = day.isoformat()
        if f.get("fact") == "D:current_cycle" and f.get("field") == "number":
            old = [c for c in seed.get("cycles", []) if c.get("number") == f["value"] and c.get("isActive")]
            if old:
                team = old[0]["teamId"]
                now = [c for c in seed.get("cycles", []) if c.get("teamId") == team
                       and datetime.fromisoformat(c["startsAt"].replace("Z", "+00:00")) <= noon
                       < datetime.fromisoformat(c["endsAt"].replace("Z", "+00:00"))]
                f["value"] = now[0]["number"] if now else -1
    return sorted(json.dumps(x, sort_keys=True) for x in fdc.evaluate(seed, q))


def _stale_now(scenario: str, case: dict, anchor_day: date) -> dict | None:
    """The first day from TODAY on which the test, run as written on the real clock, loses its designed answer."""
    claims = set(case.get("coverage_claims", []))
    seed = case["seed"]
    if case["domain"] == "calendar":
        return {"from": TODAY.isoformat(), "why": "its world is dated June 2018; an agent on the real clock reads "
                "'Thursday' and every other date in 2026"}
    if claims & {"D:overdue", "D:current_cycle"} or any(f.get("fact") in ("D:overdue", "D:current_cycle")
                                                         for f in _filters(case["references"][0]["query"])):
        query = case["references"][0]["query"]
        designed = _select(seed, query, anchor_day)
        for i in range(1, 400):
            d = anchor_day + timedelta(days=i)
            got = _select(seed, query, d)
            if got != designed:
                return {"from": d.isoformat(), "why": "read against that day, its request selects "
                        f"{len(got)} record(s) where the designed day selects {len(designed)}"
                        + (" (a near miss due on or before then becomes overdue)" if "D:overdue" in str(query)
                           else " (by its dates another cycle is current, while the data still flags the old one)")}
    for f in _filters(case["references"][0]["query"]):
        if f.get("fact") == "A:ProjectMilestone.status" and f.get("value") == "next":
            due = [g["value"] for g in _filters(case["references"][0]["query"])
                   if g.get("field") == "targetDate" and g.get("op") == "eq" and isinstance(g.get("value"), str)]
            if due:
                d = date.fromisoformat(due[0][:10]) + timedelta(days=1)
                return {"from": d.isoformat(), "why": "its target milestone still has the status 'next' after its "
                        "target date has passed (Linear itself shows such a milestone as overdue)"}
    events = []
    for p, v in templates.walk(seed):
        key = p.split(".")[-1]
        if isinstance(v, str) and templates.EVENT_FIELD.match(key) and templates.ISO_FULL.match(v) and len(v) > 10:
            events.append(datetime.fromisoformat(v.replace("Z", "+00:00").replace(" ", "T")).date())
    future = [d for d in events if d >= TODAY]
    if future:
        return {"from": None, "until": max(future).isoformat(), "why": f"a record in its data is created on "
                f"{max(future).isoformat()}, in the future of any earlier run"}
    for m in templates.TOKEN.finditer(case.get("prompt", "") if "⟦" in case.get("prompt", "") else ""):
        pass
    return None


def yearless_until(template: dict) -> dict | None:
    """A date the request writes without a year ("last modified on June 8", "created in March") reads as the nearest
    such date only until that day or month comes round again: then it names a newer one."""
    anchor_day = date.fromisoformat(template["dates"]["anchor"]["day"])
    first = None
    for m in templates.TOKEN.finditer(template.get("prompt", "")):
        kind, *parts = m.group(1).split("|")
        if kind != "P":
            continue
        k, f = int(parts[0]), "|".join(parts[1:])
        if "{yyyy}" in f or not any(x in f for x in ("{Month}", "{Mon}", "{Sept}", "{month}", "{MONTH}")):
            continue
        bound = anchor_day + timedelta(days=k)
        again = templates.add_months(bound, 12) if "{d}" in f else templates.add_months(bound.replace(day=1), 12)
        text = templates.fmt_date(bound, f)
        if first is None or again < first[0]:
            first = (again, text)
    if first is None:
        return None
    return {"from": first[0].isoformat(), "why": f"its request writes \"{first[1]}\" without a year, which from that day "
            "names a newer date"}


def stale_as_written(scenario: str, case: dict, anchor_day: date, template: dict) -> dict | None:
    """The first way the test, run as written on the real clock, loses its designed answer (now, or later)."""
    found = [x for x in (_stale_now(scenario, case, anchor_day), yearless_until(template)) if x]
    if not found:
        return None
    key = lambda x: x.get("from") or "0000"   # noqa: E731  ("until" entries are stale now)
    return min(found, key=key)


def main():
    from grounding.runs.dates_02.kit.population import trials as recorded_trials
    pop = load(HERE / "numbers/population.json")
    by_test = recorded_trials()
    build = {t["test"]: t for t in load(HERE / "numbers/build.json")["tests"]}
    retained = load(RUNS / "denominator_01/numbers/retained.json")
    verdicts = verdict_index()
    rows = []
    totals = Counter()
    for r in pop:
        case = load(RUNS / r["path"])
        b = build[r["test"]]
        anchor_day = date.fromisoformat(b["anchor"]["day"])
        policy = r["kind"] in POLICY_KINDS
        trials = [trial_outcome(t, verdicts, policy) for t in by_test.get(r["test"], [])]
        effects = []
        if r["domain"] == "calendar":
            effects.append("dated 2018")
        clocks = sorted({t["clock"] for t in trials})
        if b["anchor"].get("clock"):
            ran = datetime.fromisoformat(b["anchor"]["clock"].replace("Z", "+00:00")).astimezone(
                templates.ZoneInfo(b["anchor"]["zone"])).date()
            if ran != anchor_day:
                effects.append(f"run under a clock {abs((ran - anchor_day).days)} days "
                               f"{'before' if ran < anchor_day else 'after'} its designed day")
        agents_run = {t["agent"] for t in trials if t["outcome"] not in ("preflight", "solver_running", "infrastructure_error")}
        for agent in ("qwen", "sol"):
            if r["kind"] != "boundary" and agent not in agents_run:
                effects.append(f"not run by {agent}")
        template = load(RUNS / b["template"])
        stale = stale_as_written(r["scenario"], case, anchor_day, template) \
            if r["kind"] != "boundary" or r["domain"] == "calendar" else None
        mode = template["dates"].get("mode", "day")
        held = yearless_until(template) if mode == "fixed" else None     # still stale with the renderer (Slack held)
        if stale:
            effects.append("stale as written by 2026-10-03" if (stale.get("from") or "0") <= TODAY.isoformat()
                           else "stale as written later")
        # item outcome per agent (the tables' reading) and the trials behind a failure
        per_agent = {}
        for agent in ("qwen", "sol"):
            mine = [t for t in trials if t["agent"] == agent]
            if r["kind"] == "boundary":
                per_agent[agent] = {"trials": len(mine)}
                continue
            if policy:
                rec = retained[agent]["units"].get(r["test"], {})
                failed = rec.get("failed")
                failing = [t for t in mine if t["outcome"] in sampler.FAIL]
            else:
                rec = retained[agent]["tests"].get(r["test"], {})
                exposed = rec.get("exposed")
                failed = None if exposed is None else bool(exposed)
                failing = [t for t in mine if set(t["exposed"]) & set(exposed or [])] if exposed else []
            year_touched = [t for t in mine if set(t["flags"]) & set(YEAR_FLAGS)]
            per_agent[agent] = {
                "trials": len(mine), "failed": failed, "failing_trials": len(failing),
                "trials_with_the_year_confused": len(year_touched),
                "trials_reading_the_real_clock": sum("time_command" in t["flags"] for t in mine),
                "trials_shown_a_real_year": sum("real_year_in_tool_output" in t["flags"] for t in mine),
                "failure_rests_only_on_year_confused_trials": bool(failing) and all(set(t["flags"]) & set(YEAR_FLAGS) for t in failing),
                "clocks": sorted({t["clock"] for t in mine}), "ran_on": sorted({t["ran_on"] for t in mine})}
        rows.append({"test": r["test"], "scenario": r["scenario"], "group": r["group"], "kind": r["kind"],
                     "domain": r["domain"], "facts": r["facts"], "anchor": b["anchor"], "effects": effects,
                     "stale_as_written": stale, "mode": mode, "stale_even_rendered": held,
                     "agents": per_agent, "trials": trials})
        totals["tests"] += 1
        for e in effects:
            totals[e.split(" by ")[0] if e.startswith("not run") else e] += 1
    with open(HERE / "numbers/affected.json", "w") as out:     # one line per test: the trials make it long
        out.write('{"totals": ' + json.dumps(dict(totals)) + ',\n')
        anchors = {row["scenario"]: row["anchor"] for row in rows}
        out.write(' "anchors": ' + json.dumps(anchors) + ',\n')

        def lean(d):
            return {k: v for k, v in d.items() if v not in ([], False, None, 0)}

        def keep(row):     # the trials of the tests the dates touched on record or touch today; counts for the rest
            touched = [e for e in row["effects"] if e != "stale as written later"]
            row = {k: v for k, v in row.items() if k != "anchor"} | {"agents": {a: lean(x) for a, x in row["agents"].items()}}
            return {k: v for k, v in row.items() if k != "trials"} | (
                {"trials": [{k: v for k, v in t.items() if k != "path" and v not in ([], False, None)}
                            | ({"attempt": t["path"].rsplit("/", 1)[1]} if not t["path"].endswith("attempt-01") else {})
                            for t in row["trials"]]}
                if touched else {"trials": len(row["trials"])})
        out.write(' "tests": [\n' + ",\n".join(json.dumps(keep(row)) for row in rows))
        out.write("\n]}\n")
    print(json.dumps(dict(totals), indent=1))


if __name__ == "__main__":
    main()
