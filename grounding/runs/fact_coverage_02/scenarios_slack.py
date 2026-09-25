"""New Slack scenarios (the pilot tested no Slack facts; manual design). Each has its target; probes are derived.

Every claim carries its substitute family (method.md). Message ts values are the created_at instants, so dates the
agent reads from the API agree with the seed; all instants fall on the same calendar day from UTC-11 to UTC+11.
PANEL builds the Slack policy panel (P1-P3).
"""
from __future__ import annotations

import copy
from datetime import datetime, timezone

from grounding.runs.fact_coverage_01.pilot.common import DROP, REPLACE, SUB, claim, e, f, n, q, ref
from grounding.runs.fact_coverage_01.pilot.variants import absent_of, isolate
from grounding.runs.fact_coverage_02.scenarios_box import fam
from grounding.runs.fact_coverage_02.suite_pilot import rename

ACTOR = "U01AGENBOT9"
PEOPLE = {"priya": "Priya Sharma", "diego": "Diego Alvarez", "leo": "Leo Park", "omar": "Omar Haddad",
          "aisha": "Aisha Khan", "maya": "Maya Chen"}


REACTION = {"table": "message_reactions", "changes": ["insert"], "key": ["message_id", "user_id", "reaction_type"],
            "field": "message_id"}  # an added reaction is located by the message it is on


def uid(key):
    return ACTOR if key == "actor" else "U_" + key.upper()


class Seed:
    def __init__(self, people=None):
        self.t = {k: [] for k in ["teams", "users", "user_teams", "channels", "channel_members", "messages",
                                  "message_reactions", "user_mentions"]}
        self.t["teams"].append({"team_id": "T1", "team_name": "Northwind", "created_at": "2025-01-01T00:00:00Z"})
        self.user("actor", "Agent Bot", username="agentbot", display="AgentBot", bot=True)
        for key, name in {**PEOPLE, **(people or {})}.items():
            self.user(key, name)
        self.seq = 0

    def user(self, key, name, username=None, display=None, bot=False):
        username = username or name.lower().replace(" ", ".")
        self.t["users"].append({"user_id": uid(key), "username": username, "email": f"{username}@northwind.example",
                                "real_name": name, "display_name": display or name.split()[0],
                                "created_at": "2025-01-01T00:05:00Z", "is_bot": bot, "is_active": True})
        self.t["user_teams"].append({"user_id": uid(key), "team_id": "T1", "role": "admin" if bot else "member"})

    def channel(self, cid, name, members, *, private=False, topic="", purpose="", gc=False):
        self.t["channels"].append({"channel_id": cid, "channel_name": name, "team_id": "T1", "topic_text": topic,
                                   "purpose_text": purpose, "is_private": private, "is_dm": False, "is_gc": gc,
                                   "created_at": "2026-01-05T09:00:00Z", "is_archived": False})
        for key in ["actor", *members]:
            self.t["channel_members"].append({"channel_id": cid, "user_id": uid(key), "joined_at": "2026-01-05T09:05:00Z"})
        return cid

    def message(self, channel, author, text, at, parent=None, mentions=()):
        self.seq += 1
        epoch = int(datetime.fromisoformat(at.replace("Z", "+00:00")).timestamp())
        mid = f"{epoch}.{self.seq:06d}"
        row = {"message_id": mid, "channel_id": channel, "user_id": uid(author), "message_text": text, "type": "message",
               "ts": mid, "created_at": at}
        if parent:
            row["parent_id"] = parent
        self.t["messages"].append(row)
        for i, key in enumerate(mentions):
            self.t["user_mentions"].append({"mention_id": f"mn-{mid}-{i}", "message_id": mid, "user_id": uid(key),
                                            "mentioned_at": at})
        return mid

    def seed(self):
        return {k: copy.deepcopy(v) for k, v in self.t.items() if v}


def user_is(key, name, fact=None, op="eq"):
    return n("users", [f(key, "real_name", op, name, fact)])


def case(cid, s, prompt, refs, mode="single"):
    return {"case_id": cid, "domain": "slack", "form": "present", "mode": mode, "acting_user_id": ACTOR,
            "seed": s.seed(), "prompt": prompt, "references": refs, "probes": []}


# ---------------------------------------------------------------------------
def slk_21():
    """Message author, day and channel."""
    s = Seed()
    s.channel("C_DEPLOYS", "deploys", ["priya", "diego", "leo"])
    s.channel("C_DEPSTG", "deploys-staging", ["priya", "diego"])
    s.channel("C_GENERAL", "general", list(PEOPLE))
    s.message("C_DEPLOYS", "leo", "Deploying web 4.12 to production.", "2026-09-23T09:00:00Z")
    t = s.message("C_DEPLOYS", "priya", "Rollback of payments-api finished; error rates are back to normal.",
                  "2026-09-23T12:00:00Z")                                                               # target
    mention = s.message("C_DEPLOYS", "diego", "<@U_PRIYA> the search-api rollback is done on my side.",
                        "2026-09-23T12:20:00Z", mentions=["priya"])                                   # mentions Priya
    prev = s.message("C_DEPLOYS", "priya", "Rollback plan for the cache migration is ready for review.",
                     "2026-09-22T12:00:00Z")                                                            # day before
    stg = s.message("C_DEPSTG", "priya", "Rollback on staging went through cleanly.", "2026-09-23T12:10:00Z")
    gen = s.message("C_GENERAL", "priya", "FYI: the billing rollback is complete.", "2026-09-23T12:30:00Z")
    query = q("messages", [f("f_text", "message_text", "contains_ci", "rollback", "A:Message.message_text"),
                           f("f_day", "created_at", "contains_ci", "2026-09-23", "A:Message.created_at")], [
        e("e_user", "user_id", "user_id", user_is("f_user", "Priya Sharma"), "R:Message.user_id"),
        e("e_chan", "channel_id", "channel_id", n("channels", [f("f_chan", "channel_name", "eq", "deploys")]),
          "R:Message.channel_id")], key=("message_id",))
    mentioned = e("e_user", "message_id", "message_id", n("user_mentions", [], [
        e("e_mu", "user_id", "user_id", user_is("x", "Priya Sharma"))]))
    near_channel = e("e_chan", "channel_id", "channel_id", n("channels", [f("x", "channel_name", "contains_ci", "deploys")]))
    claims = [
        fam(claim("R:Message.user_id", mention, SUB("e_user", mentioned), "Diego posted it; it mentions Priya.",
                  alternative="user_mentions.user_id"), "F1"),
        fam(claim("A:Message.created_at", prev, DROP("f_day"), "Posted on September 22.", alternative="adjacent day"), "F7"),
        fam(claim("R:Message.channel_id", stg, SUB("e_chan", near_channel), "Posted in #deploys-staging.",
                  alternative="similarly named channel"), "F8"),
        fam(claim("R:Message.channel_id", gen, DROP("f_chan"), "Posted in #general."), "F0"),
    ]
    # v1 asked for :white_check_mark:, which the replica's reaction list rejects; v2 uses a listed reaction.
    return case("SLK-21", s, "Add a :thumbsup: reaction to the message Priya Sharma posted in #deploys on "
                             "September 23 about the rollback.",
                [ref("SLK-21.r1", "Resolve the message", "Priya Sharma's #deploys message of 2026-09-23 about the "
                     "rollback; only the payments-api rollback message.", "target", query, [t], claims,
                     paths=[{"entities": ["messages", "users"], "relationships": ["messages.user_id"]},
                            {"entities": ["messages", "channels"], "relationships": ["messages.channel_id"]}],
                     identifying=["messages.user_id", "messages.channel_id", "messages.created_at",
                                  "messages.message_text"],
                     written=["message_reactions"], effect=REACTION)])


# ---------------------------------------------------------------------------
def slk_22():
    """A reply's thread (thread root vs reply; a reply whose own text, not its thread, matches) and its author."""
    s = Seed()
    s.channel("C_INC", "incidents", ["leo", "diego", "omar"])
    root = s.message("C_INC", "leo", "Checkout outage: 502s on /pay since 14:05 UTC.", "2026-09-21T14:06:00Z")
    t = s.message("C_INC", "diego", "Rolled back the gateway config; watching the error rate.", "2026-09-21T14:20:00Z",
                  parent=root)                                                                                  # target
    other = s.message("C_INC", "omar", "Payments dashboards look normal again.", "2026-09-21T14:25:00Z", parent=root)
    top = s.message("C_INC", "diego", "The postmortem for the checkout outage is on Friday.", "2026-09-22T10:00:00Z")
    root2 = s.message("C_INC", "leo", "Search latency spike on the product pages.", "2026-09-22T16:00:00Z")
    side = s.message("C_INC", "diego", "Might be the same config push as the checkout outage.", "2026-09-22T16:10:00Z",
                     parent=root2)
    user_edge = e("e_user", "user_id", "user_id", user_is("f_user", "Diego Alvarez"), "R:Message.user_id")
    chan_edge = e("e_chan", "channel_id", "channel_id", n("channels", [f("f_chan", "channel_name", "eq", "incidents")]))
    query = q("messages", [], [user_edge, e("e_thread", "parent_id", "message_id", n("messages", [
        f("f_topic", "message_text", "contains_ci", "checkout outage")]), "H:Message.parent_id"), chan_edge],
        key=("message_id",))
    own_text = q("messages", [f("x", "message_text", "contains_ci", "checkout outage")],
                 [copy.deepcopy(user_edge), copy.deepcopy(chan_edge)], key=("message_id",))
    own_text_reply = q("messages", [f("x", "message_text", "contains_ci", "checkout outage"), f("y", "parent_id", "not_null")],
                       [copy.deepcopy(user_edge), copy.deepcopy(chan_edge)], key=("message_id",))
    claims = [
        fam(claim("H:Message.parent_id", top, REPLACE(own_text, "thread topic replaced by the message's own text"),
                  "Diego's top-level post about the outage, not a reply in its thread.",
                  alternative="thread root instead of a reply"), "F4"),
        fam(claim("H:Message.parent_id", side, REPLACE(own_text_reply, "thread topic replaced by the reply's own text"),
                  "Diego's reply mentions the outage, but its thread is about search latency.",
                  alternative="reply whose own text, not its thread, matches"), "F2"),
        fam(claim("R:Message.user_id", other, DROP("f_user"), "Omar's reply in the outage thread."), "F0"),
    ]
    return case("SLK-22", s, "Add an :eyes: reaction to Diego Alvarez's reply in the #incidents thread about the "
                             "checkout outage.",
                [ref("SLK-22.r1", "Resolve the reply", "Diego Alvarez's reply in the checkout-outage thread of "
                     "#incidents; only the gateway rollback reply.", "target", query, [t], claims,
                     paths=[{"entities": ["messages", "messages"], "relationships": ["messages.parent_id"]},
                            {"entities": ["messages", "users"], "relationships": ["messages.user_id"]}],
                     identifying=["messages.parent_id", "messages.message_text", "messages.user_id"],
                     written=["message_reactions"], effect=REACTION)])


# ---------------------------------------------------------------------------
def slk_23(twin=False):
    """A channel's purpose (its topic and name are the substitutes) and privacy."""
    s = Seed()
    s.channel("C_LEGALOPS", "legal-ops", ["maya", "omar"], private=True, topic="Contract reviews",
              purpose="Coordinating vendor contracts and renewals")                                     # target
    s.channel("C_PROC", "procurement", ["maya", "leo"], private=True, topic="Vendor contracts this quarter",
              purpose="Purchase approvals and budgets")
    s.channel("C_VENDOR", "vendor-contracts", ["omar", "aisha"], private=True, purpose="Archive of signed agreements")
    s.channel("C_CONTRACTS", "contracts-team", ["maya", "aisha"], purpose="Coordinating vendor contracts with legal")
    if twin:
        s.channel("C_VENDORMGMT", "vendor-mgmt", ["leo", "aisha"], private=True,
                  purpose="Coordinating vendor contracts for EMEA")
    query = q("channels", [f("f_purpose", "purpose_text", "contains_ci", "coordinating vendor contracts",
                             "A:Channel.purpose_text"),
                           f("f_priv", "is_private", "eq", True, "A:Channel.is_private")], key=("channel_id",))
    by_topic = q("channels", [f("x", "topic_text", "contains_ci", "vendor contracts"), f("y", "is_private", "eq", True)],
                 key=("channel_id",))
    by_name = q("channels", [f("x", "channel_name", "contains_ci", "vendor-contracts"), f("y", "is_private", "eq", True)],
                key=("channel_id",))
    claims = [
        fam(claim("A:Channel.purpose_text", "C_PROC", REPLACE(by_topic, "purpose replaced by topic"),
                  "Its topic, not its purpose, is about vendor contracts.", alternative="Channel.topic_text"), "F1"),
        fam(claim("A:Channel.purpose_text", "C_VENDOR", REPLACE(by_name, "purpose replaced by name"),
                  "Named vendor-contracts; its purpose is an archive of signed agreements.",
                  alternative="Channel.channel_name"), "F1"),
        fam(claim("A:Channel.is_private", "C_CONTRACTS", DROP("f_priv"), "A public channel with that purpose."), "F0"),
    ]
    expected = ["C_LEGALOPS", "C_VENDORMGMT"] if twin else ["C_LEGALOPS"]
    return case("SLK-23", s, "Set the topic of the private channel whose purpose is coordinating vendor contracts to "
                             "\"Renewals due Oct 31\".",
                [ref("SLK-23.r1", "Resolve the channel", "The private channel whose purpose is coordinating vendor "
                     "contracts; only legal-ops.", "target", query, expected, claims,
                     resolution="underspecified" if twin else None,
                     paths=[{"entities": ["channels"], "relationships": []}],
                     identifying=["channels.purpose_text", "channels.is_private"], written=["channels.topic_text"],
                     effect={"table": "channels", "changes": ["update"], "key": ["channel_id"], "columns": ["topic_text"]})],
                mode="underspecified" if twin else "single")


# ---------------------------------------------------------------------------
def slk_24():
    """Channel membership (posting in the channel and a similarly named member are the substitutes)."""
    s = Seed(people={"leoparker": "Leo Parker"})
    s.channel("C_FINLEADS", "finance-leads", ["priya", "leo", "maya"], private=True, purpose="Finance leadership")  # target
    s.channel("C_OPSLEADS", "ops-leads", ["priya", "maya"], private=True, purpose="Operations leadership")
    s.message("C_OPSLEADS", "leo", "Sharing the Q3 ops budget before I hand this over.", "2026-09-10T12:00:00Z")
    s.channel("C_BUDGET", "budget-review", ["priya", "leoparker"], private=True, purpose="Budget review")
    s.channel("C_HRPARTNERS", "hr-partners", ["priya", "omar"], private=True, purpose="HR business partners")
    s.message("C_FINLEADS", "maya", "Q3 close checklist is pinned.", "2026-09-15T12:00:00Z")

    def member(key, name, fact="R:channel_members"):
        return e(f"e_{key}", "channel_id", "channel_id", n("channel_members", [], [
            e(f"e_{key}_u", "user_id", "user_id", user_is(f"f_{key}", name))]), fact)
    query = q("channels", [f("f_priv", "is_private", "eq", True)], [member("priya", "Priya Sharma"),
                                                                     member("leo", "Leo Park")], key=("channel_id",))
    posted = e("e_leo", "channel_id", "channel_id", n("messages", [], [
        e("e_leo_m", "user_id", "user_id", user_is("x", "Leo Park"))]))
    namesake = e("e_leo", "channel_id", "channel_id", n("channel_members", [], [
        e("e_leo_n", "user_id", "user_id", user_is("x", "leo park", op="contains_ci"))]))
    claims = [
        fam(claim("R:channel_members", "C_OPSLEADS", SUB("e_leo", posted), "Leo posted there but is not a member.",
                  alternative="Message.channel_id of Leo's message"), "F1"),
        fam(claim("R:channel_members", "C_BUDGET", SUB("e_leo", namesake), "The member is Leo Parker, not Leo Park.",
                  alternative="similarly named user"), "F8"),
        fam(claim("R:channel_members", "C_HRPARTNERS", DROP("f_leo"), "Priya and Omar are members; Leo is not."), "F0"),
    ]
    return case("SLK-24", s, "Post \"Reminder: expense reports are due Friday\" in the private channel that both Priya "
                             "Sharma and Leo Park are members of.",
                [ref("SLK-24.r1", "Resolve the channel", "The private channel with both Priya Sharma and Leo Park as "
                     "members; only finance-leads.", "target", query, ["C_FINLEADS"], claims,
                     paths=[{"entities": ["channels", "channel_members", "users"],
                             "relationships": ["channel_members.channel_id", "channel_members.user_id"]}],
                     identifying=["channel_members.user_id", "users.real_name", "channels.is_private"],
                     written=["messages"], effect={"table": "messages", "changes": ["insert"], "key": ["message_id"],
                                                   "field": "channel_id"})])


SCENARIOS = [slk_21, slk_22, slk_23, slk_24]


def panel():
    """Slack policy panel: P1 target removed (presupposing), P2 one plain decoy (presupposing), P3 twin target."""
    p1 = absent_of(slk_21())
    p2 = rename(isolate(slk_21(), 0, 3), "SLK-21-A-I14")
    p3 = rename(slk_23(twin=True), "SLK-23-TWIN")
    p3["variant_of"] = "SLK-23"
    return [(p1, "P1: target removed, presupposing wording"), (p2, "P2: one plain decoy, presupposing wording"),
            (p3, "P3: two records fully match a singular request")]
