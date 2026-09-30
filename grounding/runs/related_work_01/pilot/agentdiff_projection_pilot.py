"""Pilot of the Agent-Diff projection on 8 obligations of 6 Slack tests: facts, near misses, and the oracle's view.

For each sampled obligation (a card of grounding/domains/slack/analysis), three questions, all without a model call:
1. Occurrence: which catalog facts (grounding/runs/fact_coverage_01/catalog/slack.json) its identifying conditions use.
2. Test side: does the test's seed (the shared slack_bench_v2 seed) hold a near miss for each fact, a record that
   meets every other condition and fails only this one? Split into the fact's designated alternative (credit rule 1)
   and a plain difference (F0). Witnesses are computed from the seed, not asserted.
3. Oracle side: the test's own assertions (examples/slack/testsuites/slack_bench.json via the dataset's answer field)
   are compiled and run by the backend's own engine on a correct diff, then on the same diff with the witness put in
   the target's place. If the second still passes, the suite cannot see a failure on that fact.

Run from the repository root: python -m grounding.runs.related_work_01.pilot.agentdiff_projection_pilot
Writes agentdiff_projection_pilot.json next to this file.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "backend"))

from src.platform.evaluationEngine.assertion import AssertionEngine  # noqa: E402
from src.platform.evaluationEngine.compiler import DSLCompiler  # noqa: E402

HERE = Path(__file__).parent
SEED = json.loads((REPO / "examples/slack/seeds/slack_bench_v2.json").read_text())
TESTS = {json.loads(l)["test_id"]: json.loads(l)
         for l in (REPO / "datasets/agent-diff-bench/all_numbered.jsonl").read_text().splitlines()}
SUITE_IGNORE = json.loads((REPO / "examples/slack/testsuites/slack_bench.json").read_text()).get("ignore_fields", {})
RECORDED = REPO / "grounding/reference_labels/slack/inputs"

USERS = {u["user_id"]: u for u in SEED["users"]}
ROLE = {m["user_id"]: m["role"] for m in SEED["user_teams"]}
MEMBERS = {}
for m in SEED["channel_members"]:
    MEMBERS.setdefault(m["channel_id"], set()).add(m["user_id"])
CH = {c["channel_name"]: c["channel_id"] for c in SEED["channels"]}
MSG = {m["message_id"]: m for m in SEED["messages"]}


def run_assertions(test_id, diff):
    spec = json.loads(TESTS[test_id]["answer"])
    spec = {**spec, "ignore_fields": spec.get("ignore_fields") or SUITE_IGNORE}
    compiled = DSLCompiler().compile(spec)
    return AssertionEngine(compiled).evaluate(diff)["passed"]


def recorded(test_id):
    return json.loads((RECORDED / test_id / "recorded_diff.json").read_text())


def replace_text(diff, old, new):
    out = copy.deepcopy(diff)
    for row in out["inserts"]:
        if isinstance(row.get("message_text"), str):
            row["message_text"] = row["message_text"].replace(old, new)
    return out


def replace_field(diff, table, field, old, new):
    out = copy.deepcopy(diff)
    for kind in ("inserts", "updates"):
        for row in out.get(kind, []):
            if row.get("__table__") == table and row.get(field) == old:
                row[field] = new
    return out


def authors_of(pred):
    return {m["user_id"] for m in SEED["messages"] if pred(m["message_text"])}


def pilot():
    rows = []

    # 1. slack_89 O1: the admins of the workspace, reported by name in #random.
    admins = {u for u, r in ROLE.items() if r == "admin"}
    same_first = {u for u in ROLE if ROLE[u] != "admin" and any(
        USERS[u]["real_name"].split()[0] == USERS[a]["real_name"].split()[0] for a in admins)}
    gold = recorded("slack_89")  # Sonnet's reply names both admins (labelled correct)
    wrong = replace_text(replace_text(gold, "Morgan Freeman", "Morgan Stanley"), "Robert Walsh", "Robert Chen")
    rows.append({
        "test": "slack_89", "obligation": 1, "request": "the admins of the Test Workspace",
        "facts": {"A:WorkspaceMembership.role": {
            "designated": sorted(same_first), "designated_note": "state: another value (member), same first name as an admin",
            "plain": len([u for u in ROLE if ROLE[u] != "admin"])}},
        "oracle": {"gold_passes": run_assertions("slack_89", gold),
                   "near_miss_passes": run_assertions("slack_89", wrong),
                   "near_miss": "reply names Morgan Stanley and Robert Chen (members) instead of the admins"}})

    # 2. slack_104 O2: the current members of #engineering, count and names posted to #general.
    eng = CH["engineering"]
    posters_not_members = sorted({m["user_id"] for m in SEED["messages"] if m["channel_id"] == eng} - MEMBERS[eng])
    gold = recorded("slack_104")
    witness = posters_not_members[0] if posters_not_members else None
    wrong = replace_text(gold, "Morgan Stanley (@Morgan)", f"{USERS[witness]['real_name']} (@{USERS[witness]['username']})") \
        if witness else gold
    wrong_count = replace_text(gold, "*Member Count:* 5", "*Member Count:* 15")
    rows.append({
        "test": "slack_104", "obligation": 2, "request": "who's currently in #engineering (count and names)",
        "facts": {"R:channel_members": {"designated": posters_not_members,
                                        "designated_note": "posted in #engineering but not a member"},
                  "D:member_count": {"designated": ["15 (a count containing 5)"],
                                     "designated_note": "view: members vs posters; the assertion is a substring"}},
        "oracle": {"gold_passes": run_assertions("slack_104", gold),
                   "near_miss_passes": run_assertions("slack_104", wrong),
                   "near_miss": f"a poster who is not a member ({witness}) listed in place of a member",
                   "wrong_count_passes": run_assertions("slack_104", wrong_count)}})

    # 3. slack_87 O1: everyone who posted about login or password, invited to a new channel.
    about = lambda t: "login" in t.lower() or "password" in t.lower()
    authors = authors_of(about)
    channels_with = {m["channel_id"] for m in SEED["messages"] if about(m["message_text"])}
    members_not_authors = sorted(set().union(*(MEMBERS.get(c, set()) for c in channels_with)) - authors)
    reactors = {r["user_id"] for r in SEED["message_reactions"] if about(MSG[r["message_id"]]["message_text"])} - authors
    gold = recorded("slack_87")
    new_channel = next(r["channel_id"] for r in gold["inserts"] if r["__table__"] == "channels")
    swap_out = "U05MORGAN23"
    # No designated witness exists (every member of those channels is an author; no reactor), so the oracle is tried
    # with a plain one: a user who never posted about login or password.
    plain_witness = "U04OMER23"
    wrong = replace_field(gold, "channel_members", "user_id", swap_out, plain_witness)
    extra = copy.deepcopy(gold)
    extra["inserts"].append({"__table__": "channel_members", "channel_id": new_channel,
                             "user_id": plain_witness, "joined_at": "2026-09-08T12:07:05"})
    rows.append({
        "test": "slack_87", "obligation": 1, "request": "everyone who has posted about login or password",
        "facts": {"R:messages.user_id": {"designated": members_not_authors + sorted(reactors),
                                         "designated_note": "member of a channel with such a post, or a reactor, "
                                                            "who is not an author: none in the seed"},
                  "A:Message.message_text": {"plain": "every user who never posted about it"}},
        "oracle": {"gold_passes": run_assertions("slack_87", gold),
                   "near_miss_passes": run_assertions("slack_87", wrong),
                   "near_miss": f"{plain_witness} (plain) invited instead of {swap_out}",
                   "extra_invite_passes": run_assertions("slack_87", extra)}})

    # 4. slack_105 O3: the root of the circuit-tracer thread (reply in the thread, react to the root).
    root = "1706110000.000100"
    replies = sorted(m["message_id"] for m in SEED["messages"] if m.get("parent_id") == root)
    gold = {"deletes": [], "updates": [], "inserts": [
        {"__table__": "messages", "message_id": "1788883900.000001", "channel_id": eng, "user_id": "U01AGENBOT9",
         "parent_id": root, "message_text": "Sophie estimates Wednesday next week.", "ts": None, "type": "message",
         "blocks": None, "created_at": "2026-09-08T12:10:00"},
        {"__table__": "message_reactions", "message_id": root, "user_id": "U01AGENBOT9", "reaction_type": "eyes"}]}
    wrong = replace_field(replace_field(gold, "messages", "parent_id", root, replies[0]),
                          "message_reactions", "message_id", root, replies[0])
    rows.append({
        "test": "slack_105", "obligation": 3, "request": "the thread where Robert asked about the rewrite timeline",
        "facts": {"H:messages.parent_id": {"designated": replies, "designated_note": "a reply taken for the root"},
                  "R:messages.channel_id": {"plain": "circuit-tracer messages elsewhere"}},
        "oracle": {"gold_passes": run_assertions("slack_105", gold),
                   "near_miss_passes": run_assertions("slack_105", wrong),
                   "near_miss": f"reply and reaction attached to the reply {replies[0]}"}})

    # 5. slack_67 O2: the pizza-combo message in #random (thumbs down).
    rnd = CH["random"]
    pizza = "1706051755.000000"
    other_random = sorted(m["message_id"] for m in SEED["messages"] if m["channel_id"] == rnd and m["message_id"] != pizza)
    elsewhere = sorted(m["message_id"] for m in SEED["messages"]
                       if "pizza" in m["message_text"].lower() and m["channel_id"] != rnd)
    gold = {"deletes": [], "updates": [], "inserts": [
        {"__table__": "message_reactions", "message_id": mid, "user_id": "U01AGENBOT9", "reaction_type": rt}
        for mid, rt in [("1699572000.000789", "thumbsup"), ("1706052027.000000", "thumbsup"),
                        ("1706052160.000000", "thumbsup"), ("1706052665.000000", "thumbsup"), (pizza, "thumbsdown")]]}
    wrong = replace_field(gold, "message_reactions", "message_id", pizza, "1706053102.000000")
    lunch_dropped = copy.deepcopy(gold)
    lunch_dropped["inserts"] = [r for r in gold["inserts"] if r["message_id"] not in ("1706052027.000000", "1706052160.000000")]
    rows.append({
        "test": "slack_67", "obligation": 2, "request": "the message about piza combo (in #random)",
        "facts": {"A:Message.message_text": {"plain": len(other_random)},
                  "R:messages.channel_id": {"designated": elsewhere, "designated_note": "a pizza message in another channel"}},
        "oracle": {"gold_passes": run_assertions("slack_67", gold),
                   "near_miss_passes": run_assertions("slack_67", wrong),
                   "near_miss": "thumbs down on another #random message"}})
    rows.append({
        "test": "slack_67", "obligation": 1, "request": "all messages in #random that are questions about lunch",
        "facts": {"A:Message.message_text": {"plain": "the other #random messages"},
                  "R:messages.channel_id": {"plain": "lunch talk elsewhere, if any"}},
        "oracle": {"gold_passes": run_assertions("slack_67", gold),
                   "near_miss_passes": run_assertions("slack_67", lunch_dropped),
                   "near_miss": "two of the four lunch questions left out (a several-match miss)"}})

    # 6. slack_74 O2 and slack_89 O2: a destination channel named exactly (#general, #random).
    gold = recorded("slack_74")
    wrong = replace_field(gold, "messages", "channel_id", CH["general"], CH["random"])
    rows.append({
        "test": "slack_74", "obligation": 2, "request": "#general",
        "facts": {"A:Conversation.channel_name": {"plain": len(CH) - 1}},
        "oracle": {"gold_passes": run_assertions("slack_74", gold),
                   "near_miss_passes": run_assertions("slack_74", wrong),
                   "near_miss": "the questions posted to #random instead"}})
    gold = recorded("slack_89")
    wrong = replace_field(gold, "messages", "channel_id", CH["random"], CH["general"])
    rows.append({
        "test": "slack_89", "obligation": 2, "request": "#random",
        "facts": {"A:Conversation.channel_name": {"plain": len(CH) - 1}},
        "oracle": {"gold_passes": run_assertions("slack_89", gold),
                   "near_miss_passes": run_assertions("slack_89", wrong),
                   "near_miss": "the reply posted to #general instead"}})
    return rows


def main():
    rows = pilot()
    summary = {
        "obligations": len(rows),
        "gold_diff_passes": sum(r["oracle"]["gold_passes"] for r in rows),
        "with_a_designated_near_miss_in_seed": sum(
            any(f.get("designated") for f in r["facts"].values()) for r in rows),
        "oracle_blind_to_the_near_miss": sum(r["oracle"]["near_miss_passes"] for r in rows),
    }
    (HERE / "agentdiff_projection_pilot.json").write_text(json.dumps({"summary": summary, "rows": rows}, indent=1) + "\n")
    print(json.dumps(summary, indent=1))
    for r in rows:
        print(r["test"], "O%d" % r["obligation"], "| designated:",
              {k: v.get("designated") for k, v in r["facts"].items() if v.get("designated")},
              "| gold passes:", r["oracle"]["gold_passes"], "| near miss passes:", r["oracle"]["near_miss_passes"],
              {k: v for k, v in r["oracle"].items() if k.endswith("_passes") and k not in ("gold_passes", "near_miss_passes")})


if __name__ == "__main__":
    main()
