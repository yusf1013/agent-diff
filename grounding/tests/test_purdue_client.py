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


class LimitTests(unittest.TestCase):
    def _posted_max_tokens(self, call_value, client_cap):
        import httpx
        seen = {}

        async def fake_post(url, headers=None, json=None):
            seen.update(json)
            req = httpx.Request("POST", str(url))
            return httpx.Response(200, json={
                "id": "r", "model": "m",
                "choices": [{"message": {"content": "<done>x</done>"},
                             "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 1, "completion_tokens": 1}},
                request=req)

        async def run():
            client = pc.PurdueClient(model_id="m", api_key="test",
                                     max_output_tokens=client_cap)
            client._client.post = fake_post
            try:
                await client.create([{"role": "user", "content": "hi"}],
                                    max_tokens=call_value)
            finally:
                await client.close()
        asyncio.run(run())
        return seen["max_tokens"]

    def test_client_cap_takes_precedence(self):
        self.assertEqual(self._posted_max_tokens(16384, 8192), 8192)
        self.assertEqual(self._posted_max_tokens(4096, 8192), 4096)
        self.assertEqual(self._posted_max_tokens(16384, None), 16384)

    def test_retryable_transient_400s(self):
        import httpx
        client = pc.PurdueClient.__new__(pc.PurdueClient)
        for body in ("Rate limit exceeded", "Open WebUI: Server Connection Error",
                     "model overloaded, try again"):
            req = httpx.Request("POST", "https://x")
            resp = httpx.Response(400, text=body, request=req)
            self.assertTrue(client._is_retryable(
                httpx.HTTPStatusError("e", request=req, response=resp)), body)
        req = httpx.Request("POST", "https://x")
        resp = httpx.Response(400, text="invalid max_tokens", request=req)
        self.assertFalse(client._is_retryable(
            httpx.HTTPStatusError("e", request=req, response=resp)))


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
