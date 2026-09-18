"""Unit checks plus opt-in real DB/backend/sandbox integration with no model calls.

CAMPAIGN_TEST_DATABASE_URL=postgresql://postgres@127.0.0.1:15432/agentdiff_campaign \
  ../bedrock-llm/.venv/bin/python -m unittest grounding.tests.test_runtime
"""
import asyncio
from copy import deepcopy
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from grounding.integrations.agentdiff import runtime


class RuntimeUnitTests(unittest.TestCase):
    def test_parent_order_and_missing_parent(self):
        self.assertEqual([r["message_id"] for r in runtime.ordered_messages([
            {"message_id": "child", "parent_id": "root"}, {"message_id": "root"}
        ])], ["root", "child"])
        with self.assertRaisesRegex(ValueError, "missing parent"):
            runtime.ordered_messages([{"message_id": "child", "parent_id": "missing"}])

    def test_seed_real_fields_and_datetime(self):
        _, meta, _ = runtime.dependencies()
        with self.assertRaisesRegex(ValueError, "Unknown users fields"):
            runtime.normalize_row(meta.tables["users"], {"invented": "x"})
        value = runtime.normalize_row(meta.tables["users"], {"created_at": "2026-01-01T01:00:00+01:00"})
        self.assertEqual(value["created_at"].isoformat(), "2026-01-01T00:00:00")

    def test_no_mutating_visibility_method(self):
        client = SimpleNamespace(base_url="unused", _headers=lambda: {})
        # No HTTP is permitted in this unit test; only the allowlist itself is checked.
        self.assertNotIn("chat.postMessage", runtime.READ_METHODS)
        self.assertNotIn("conversations.open", runtime.READ_METHODS)
        self.assertIn("conversations.history", runtime.READ_METHODS)


@unittest.skipUnless(os.environ.get("CAMPAIGN_TEST_DATABASE_URL"), "Requires explicit local integration database")
class RuntimeIntegrationTests(unittest.TestCase):
    def test_relational_visibility_and_missing_projection_detection(self):
        from grounding.tests.test_validation import case_fixture
        # The backend history API sorts native message IDs as numeric timestamps.
        case = json.loads(json.dumps(case_fixture()).replace('M1', '1720000000.000001')
                          .replace('M2', '1720000000.000002').replace('M3', '1720000000.000003'))
        database_url = os.environ["CAMPAIGN_TEST_DATABASE_URL"]
        with tempfile.TemporaryDirectory(prefix="ad_visibility_test_") as folder:
            prepared = runtime.prepare(case, Path(folder) / "prepared", database_url)
            try:
                state = json.loads(Path(prepared["initial_state_path"]).read_text())
                report = json.loads(Path(prepared["visibility_path"]).read_text())
                good = runtime.certify_visibility(case, state, report)
                self.assertTrue(good["certified"], good)
                missing = deepcopy(report)
                missing["probes"] = [p for p in missing["probes"] if p["probe"]["method"] != "reactions.get"]
                result = runtime.certify_visibility(case, state, missing)
                self.assertFalse(result["certified"])
                self.assertTrue(any("reaction" in error for error in result["errors"]))
                changed = deepcopy(report)
                for item in changed["probes"]:
                    if item["probe"]["method"] == "conversations.info":
                        item["pages"][0]["body"]["channel"]["name"] = "different"
                result = runtime.certify_visibility(case, state, changed)
                self.assertTrue(any("field channel_name" in error for error in result["errors"]))
                user_case = deepcopy(case)
                user_case["private"]["near_misses"] = []
                user_case["private"]["selector"] = {"root_table": "users", "scope": [],
                    "focal": {"path": ["users"], "joins": [], "filters": [
                        {"node": 0, "field": "real_name", "op": "eq", "value": "Alex Rivera"}]},
                    "auxiliary": [{"path": ["users", "channel_members", "channels"],
                        "joins": ["channel_members.user_id", "channel_members.channel_id"],
                        "filters": [{"node": 2, "field": "channel_name", "op": "eq", "value": "security"}]}]}
                missing_name = deepcopy(report)
                for item in missing_name["probes"]:
                    for page in item["pages"]:
                        payloads = page["body"].get("channels", [])
                        if "channel" in page["body"] and isinstance(page["body"]["channel"], dict):
                            payloads = [*payloads, page["body"]["channel"]]
                        for payload in payloads:
                            if payload.get("id") == "CO":
                                payload.pop("name", None)
                result = runtime.certify_visibility(user_case, state, missing_name)
                self.assertTrue(result["certified"], result)
                # A claimed negative needs its auxiliary resemblance proven,
                # even when the API already disproves its focal condition.
                user_case["private"]["near_misses"] = ["U2"]
                result = runtime.certify_visibility(user_case, state, missing_name)
                self.assertFalse(result["certified"])
                self.assertTrue(any("field channel_name" in error for error in result["errors"]))
                anchored = deepcopy(case)
                anchored["private"]["near_misses"] = []
                anchored["private"]["selector"] = {"root_table": "messages", "scope": [],
                    "focal": {"path": ["messages", "channels"], "joins": ["messages.channel_id"],
                              "filters": [{"node": 1, "field": "channel_name", "op": "eq", "value": "security"}]},
                    "auxiliary": []}
                inaccessible = deepcopy(missing_name)
                inaccessible["probes"] = [item for item in inaccessible["probes"]
                    if not (item["probe"]["method"] == "conversations.history"
                            and item["probe"].get("params", {}).get("channel") == "CO")]
                result = runtime.certify_visibility(anchored, state, inaccessible)
                self.assertTrue(result["certified"], result)
                self.assertEqual(result["method"], "reverse_channel_anchor")
                self.assertTrue(result["prior_forward_check"]["errors"])
                # Root-neighbor history need not be universally available, but
                # a declared negative must still have its own observed evidence.
                anchored["private"]["near_misses"] = [state["messages"][0]["message_id"]]
                result = runtime.certify_visibility(anchored, state, inaccessible)
                self.assertFalse(result["certified"])
                anchored["private"]["near_misses"] = []
                no_catalog = deepcopy(inaccessible)
                no_catalog["probes"] = [p for p in no_catalog["probes"] if p["probe"]["method"] != "conversations.list"]
                self.assertFalse(runtime.certify_visibility(anchored, state, no_catalog)["certified"])
                hidden_channel = deepcopy(state)
                hidden_channel["channels"].append({"channel_id": "C_HIDDEN", "channel_name": "unlisted", "team_id": "T1"})
                self.assertFalse(runtime.certify_visibility(anchored, hidden_channel, inaccessible)["certified"])
                multiple_workspaces = deepcopy(state)
                multiple_workspaces["channels"][0]["team_id"] = "T_OTHER"
                self.assertFalse(runtime.certify_visibility(anchored, multiple_workspaces, inaccessible)["certified"])
                negative_case = deepcopy(anchored)
                negative_case["private"]["selector"]["auxiliary"] = [{"path": ["messages"], "joins": [],
                    "filters": [{"node": 0, "field": "message_text", "op": "contains_ci", "value": "rollout"}]}]
                negative_case["private"]["near_misses"] = [state["messages"][0]["message_id"]]
                self.assertTrue(runtime.certify_visibility(negative_case, state, missing_name)["certified"])
                corrupted_negative = deepcopy(missing_name)
                for item in corrupted_negative["probes"]:
                    for page in item["pages"]:
                        payloads = [*page["body"].get("messages", []), page["body"].get("message", {})]
                        for payload in payloads:
                            if payload.get("ts") == negative_case["private"]["near_misses"][0]:
                                payload["text"] = "Lunch is ready."
                self.assertFalse(runtime.certify_visibility(negative_case, state, corrupted_negative)["certified"])
                # Other profile memberships cannot be certified from a single displayed workspace.
                wm_case = deepcopy(case)
                wm_case["private"]["selector"] = {"root_table": "users", "scope": [], "auxiliary": [],
                    "focal": {"path": ["users", "user_teams"], "joins": ["user_teams.user_id"],
                              "filters": [{"node": 1, "field": "role", "op": "eq", "value": "owner"}]}}
                more_state = deepcopy(state)
                more_state["user_teams"].append({"user_id": "U1", "team_id": "T_OTHER", "role": "member"})
                result = runtime.certify_visibility(wm_case, more_state, report)
                self.assertTrue(any("ambiguous" in reason for reason in result["limitations"]))
            finally:
                runtime.cleanup(prepared, database_url)

    def test_real_seed_sandbox_diff_and_oracle_bundle_with_fake_llm(self):
        database_url = os.environ["CAMPAIGN_TEST_DATABASE_URL"]
        case = {
            "case_id": "runtime_contract", "prompt": "Post 'Runtime smoke' in #general.",
            "acting_user_id": "U_TEST",
            "seed": {"tables": {
                "teams": [{"team_id": "T_TEST", "team_name": "Runtime test"}],
                "users": [{"user_id": "U_TEST", "username": "riley", "email": "riley@example.test"}],
                "user_teams": [{"user_id": "U_TEST", "team_id": "T_TEST", "role": "owner"}],
                "channels": [{"channel_id": "C_TEST", "channel_name": "general", "team_id": "T_TEST"}],
                "channel_members": [{"user_id": "U_TEST", "channel_id": "C_TEST"}],
                "messages": [],
                "team_roles": [{"role_id": "R_TEST", "team_id": "T_TEST", "role_name": "Channel reviewer"}],
                "user_roles": [{"user_id": "U_TEST", "role_id": "R_TEST"}],
                "user_settings": [{"user_id": "U_TEST", "notification_level": "mentions"}],
            }},
            "cards": [], "task_spec": [],
        }

        class Block:
            type = "text"
            def __init__(self, text): self.text = text
            def model_dump(self, **kwargs): return {"type": self.type, "text": self.text}

        class Message:
            def __init__(self, text): self.content = [Block(text)]
            def model_dump(self, **kwargs): return {"role": "assistant", "content": [b.model_dump() for b in self.content]}

        class FakeLLM:
            def __init__(self, **kwargs):
                self.count = 0
                self.usage = SimpleNamespace(snapshot=lambda: SimpleNamespace(to_dict=lambda: {}))
            async def create(self, messages, **kwargs):
                self.count += 1
                text = ('<action>curl -s -X POST https://slack.com/api/chat.postMessage '
                        '-H \'Content-Type: application/json\' '
                        '-d \'{"channel":"C_TEST","text":"Runtime smoke"}\'</action>'
                        if self.count == 1 else '<done>Posted Runtime smoke in #general.</done>')
                return SimpleNamespace(text=text, message=Message(text), usage=SimpleNamespace(to_dict=lambda: {}))
            async def close(self): pass

        with tempfile.TemporaryDirectory(prefix="ad_campaign_test_") as folder:
            out = Path(folder)
            prepared = runtime.prepare(case, out / "prepared", database_url)
            initial = json.loads(Path(prepared["initial_state_path"]).read_text())
            self.assertEqual(initial["users"][0]["is_active"], True)
            self.assertEqual(initial["users"][0]["is_bot"], False)
            # Raw benchmark seed loading applies SQL defaults, not ORM defaults.
            self.assertIsNone(initial["users"][0]["created_at"])
            self.assertIsNone(initial["channels"][0]["created_at"])
            self.assertEqual(initial["user_settings"][0]["notification_level"], "mentions")
            self.assertEqual(len(initial["team_roles"]), 1)
            self.assertEqual(len(initial), 15)
            baseline = runtime.load_baseline()
            baseline.BedrockClaudeClient = FakeLLM
            with patch.object(runtime, "load_baseline", return_value=baseline):
                record = asyncio.run(runtime.run_prepared(case, prepared, out / "run", database_url))
            self.assertEqual(record["termination"], "done", record)
            self.assertNotIn("error", record)
            self.assertNotIn("passed", record["evaluation"])
            self.assertEqual(record["cost_usd"], 0)
            final = json.loads((out / "run/final_state.json").read_text())
            self.assertEqual([r["message_text"] for r in final["messages"]], ["Runtime smoke"])
            self.assertTrue(record["evaluation"]["diff"])
            self.assertTrue((out / "run/oracle_input/recorded_diff.json").exists())
            engine = runtime.engine_for(database_url)
            from sqlalchemy import text
            with engine.connect() as c:
                self.assertIsNone(c.execute(text("SELECT schema_name FROM information_schema.schemata WHERE schema_name=:name"),
                                            {"name": prepared["template_name"]}).first())
            engine.dispose()


if __name__ == "__main__":
    unittest.main()
