"""Offline checks for the Purdue adapter: evidence preservation, limits, retries."""
import asyncio
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

os.environ.setdefault("PURDUE_RATE_LIMIT_DISABLE", "1")

from grounding.solver.slack import purdue_client as pc
from grounding.solver.slack import purdue_rate_limit as rl


def _message():
    raw = {"id": "r1", "model": "qwen3.6:27b",
           "choices": [{"message": {"content": "<done>x</done>",
                                     "reasoning_content": "private reasoning"},
                        "finish_reason": "stop"}],
           "usage": {"prompt_tokens": 5, "completion_tokens": 7}}
    blocks = [pc._Block(type="thinking", text="private reasoning"),
              pc._Block(type="text", text="<done>x</done>")]
    return pc._Message(id="r1", model="qwen3.6:27b", content=blocks,
                       stop_reason="stop", raw=raw)


class SerializationTests(unittest.TestCase):
    def test_thinking_text_and_raw_preserved_in_evidence(self):
        dumped = _message().model_dump()
        thinking = [b for b in dumped["content"] if b["type"] == "thinking"]
        self.assertEqual(len(thinking), 1)
        self.assertEqual(thinking[0]["text"], "private reasoning")
        self.assertEqual(dumped["raw"]["id"], "r1")
        self.assertIn("reasoning_content",
                      dumped["raw"]["choices"][0]["message"])

    def test_conversation_excludes_thinking(self):
        dumped = [b for b in _message().model_dump()["content"]]
        text = pc._content_to_text(dumped)
        self.assertIn("<done>x</done>", text)
        self.assertNotIn("private reasoning", text)

    def test_openai_messages_exclude_thinking(self):
        client = pc.PurdueClient.__new__(pc.PurdueClient)
        dumped = _message().model_dump()["content"]
        out = pc.PurdueClient._openai_messages(
            client, [{"role": "assistant", "content": dumped}], "sys")
        joined = json.dumps(out)
        self.assertIn("<done>x</done>", joined)
        self.assertNotIn("private reasoning", joined)
        self.assertEqual(out[0]["role"], "system")


class LimiterTests(unittest.TestCase):
    def test_shared_window_across_calls(self):
        with tempfile.TemporaryDirectory() as d:
            path = str(Path(d) / "rl.json")
            with mock.patch.dict(os.environ, {"PURDUE_RATE_LIMIT_FILE": path,
                                              "PURDUE_RATE_LIMIT_PER_MINUTE": "2",
                                              "PURDUE_RATE_LIMIT_DISABLE": "0"}):
                async def two():
                    await rl.acquire_purdue_slot()
                    await rl.acquire_purdue_slot()
                    return rl.read_state_for_tests(Path(path))
                stamps = asyncio.run(two())
                self.assertEqual(len(stamps), 2)

    def test_bypass_flag(self):
        with mock.patch.dict(os.environ, {"PURDUE_RATE_LIMIT_DISABLE": "1"}):
            asyncio.run(rl.acquire_purdue_slot())


if __name__ == "__main__":
    unittest.main()
