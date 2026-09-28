"""The Slack seed conventions the generator builds on: the team, the bot actor, default people, channels and
message ids.

Copied verbatim from grounding/runs/fact_coverage_02/scenarios_slack.py (lines 17-71) on 2026-09-27, so that the
kit no longer imports a study's hand-made scenarios (roadmap step 3). Behaviour is unchanged; the study keeps its
own copy. The bot is a member of every channel it creates, so it can read them.
"""
from __future__ import annotations

import copy
from datetime import datetime


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

