"""Offline request-contract checks: no Bedrock, database, or Docker calls.

../bedrock-llm/.venv/bin/python -m unittest grounding.tests.test_solver_options
"""
import asyncio
from copy import deepcopy
import gzip
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, Mock, patch

from bedrock_llm import BedrockClaudeClient

from grounding.integrations.agentdiff import runtime


class NativeBlock:
    def __init__(self, **value):
        self.__dict__.update(value)

    def model_dump(self, **kwargs):
        return dict(self.__dict__)


class NativeMessage:
    def __init__(self, text):
        self.content = [NativeBlock(type="thinking", thinking="", signature="native-signature"),
                        NativeBlock(type="text", text=text)]
        self.usage = {"input_tokens": 3, "output_tokens": 7,
                      "cache_creation_input_tokens": 11, "cache_read_input_tokens": 13}

    def model_dump(self, **kwargs):
        return {"role": "assistant", "content": [b.model_dump() for b in self.content],
                "usage": self.usage}


class RecordedSDK:
    """Exercise the real helper request assembly against a local SDK double."""
    def __init__(self, outputs):
        self.outputs = iter(outputs)
        self.requests = []
        self.messages = self

    def stream(self, **request):
        self.requests.append(deepcopy(request))
        return self

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        pass

    async def get_final_message(self):
        value = next(self.outputs)
        if isinstance(value, Exception):
            raise value
        return NativeMessage(value)

    async def close(self):
        pass


class SolverOptionsTests(unittest.TestCase):
    def setUp(self):
        self.baseline = runtime.load_baseline()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.out = Path(self.temp.name)

    def episode(self, args, outputs):
        sdk = RecordedSDK(outputs)
        created = []

        def llm_factory(**kwargs):
            client = BedrockClaudeClient(sdk_client=sdk, backoff_base=0, **kwargs)
            created.append(client)
            return client

        client = SimpleNamespace(
            init_env=lambda **_: SimpleNamespace(environmentId="local-test"),
            start_run=lambda **_: SimpleNamespace(runId="local-run"),
            evaluate_run=lambda **_: None,
            get_results_for_run=lambda **_: SimpleNamespace(model_dump=lambda **_: {"diff": []}),
            delete_env=lambda **_: None,
        )
        process = SimpleNamespace(wait=AsyncMock())
        row = {"test_id": "case", "test_name": "case", "#": None, "question": "A task",
               "info": json.dumps({"seed_template": "local", "impersonate_user_id": "U1"}),
               "answer": "{}"}
        with patch.object(self.baseline, "BedrockClaudeClient", side_effect=llm_factory), \
             patch.object(self.baseline, "AgentDiff", return_value=client), \
             patch.object(self.baseline.asyncio, "create_subprocess_exec", AsyncMock(return_value=process)), \
             patch.object(self.baseline.subprocess, "run", Mock()), \
             patch("builtins.print"):
            result = asyncio.run(self.baseline.episode(row, args, "System instructions", self.out))
        return result, sdk, created[0]

    def test_default_episode_does_not_add_thinking_temperature_or_recording(self):
        args = SimpleNamespace(base_url="unused", model="us.anthropic.claude-sonnet-5")
        result, sdk, client = self.episode(args, ["<done>Done.</done>"])
        self.assertEqual(result["termination"], "done")
        self.assertEqual(sdk.requests[0]["max_tokens"], 128000)
        for key in ("thinking", "temperature", "output_config"):
            self.assertNotIn(key, sdk.requests[0])
        self.assertIsNone(client.thinking_budget)
        self.assertIsNone(client.effort)
        self.assertFalse((self.out / "requests").exists())

    def test_explicit_thinking_budget_does_not_inflate_total_and_record_matches_sdk(self):
        args = SimpleNamespace(base_url="unused", model="us.anthropic.claude-haiku-4-5-20251001-v1:0",
                               max_output_tokens=64000, thinking_budget=16000, record_requests=True)
        result, sdk, client = self.episode(args, ["Checking.", "<done>Done.</done>"])
        self.assertEqual(result["termination"], "done")
        self.assertIsNone(client.thinking_budget)
        for turn, request in enumerate(sdk.requests, 1):
            self.assertEqual(request["max_tokens"], 64000)
            self.assertEqual(request["thinking"], {"type": "enabled", "budget_tokens": 16000})
            self.assertEqual(request["temperature"], 1)
            self.assertNotIn("output_config", request)
            with gzip.open(self.out / "requests/case" / f"turn-{turn:03d}.json.gz", "rt") as handle:
                self.assertEqual(json.load(handle), request)
            self.assertEqual(request["system"][-1]["cache_control"], {"type": "ephemeral"})
            self.assertEqual(request["messages"][-1]["content"][-1]["cache_control"],
                             {"type": "ephemeral"})
        self.assertEqual(sdk.requests[1]["messages"][1]["content"][0]["signature"], "native-signature")
        self.assertNotIn("cache_control", result["steps"][0]["response"]["content"][0])
        self.assertEqual(result["usage"]["successful_requests"], 2)

    def test_failed_logical_call_keeps_request_and_failure(self):
        args = SimpleNamespace(base_url="unused", model="us.anthropic.claude-sonnet-5", record_requests=True)
        result, sdk, _ = self.episode(args, [RuntimeError("offline failure")] * 3)
        self.assertEqual(result["termination"], "error")
        with gzip.open(self.out / "requests/case/turn-001.json.gz", "rt") as handle:
            self.assertEqual(json.load(handle), sdk.requests[0])
        failure = json.loads((self.out / "requests/case/turn-001.error.json").read_text())
        self.assertEqual(failure["error"], "offline failure")
        self.assertEqual(failure["usage"]["failed_requests"], 1)
        self.assertEqual(failure["usage"]["retry_attempts"], 2)
        self.assertEqual(sdk.requests, [sdk.requests[0]] * 3)

    def test_run_prepared_passes_settings_and_keeps_rates_local(self):
        case = {"case_id": "prepared", "prompt": "A task", "acting_user_id": "U1"}
        initial = self.out / "initial.json"
        initial.write_text("{}")
        prepared = {"case_sha256": runtime.digest(case), "base_url": "unused",
                    "template_name": "local", "initial_state_path": str(initial),
                    "initial_state_sha256": runtime.digest({})}
        rates = {"input_tokens": 1, "output_tokens": 5, "cache_creation_input_tokens": 1.25,
                 "cache_read_input_tokens": .1}
        original = runtime.load_baseline()
        engine = SimpleNamespace(dispose=Mock())

        async def fake_episode(row, args, prompt, out):
            self.assertEqual(args.max_output_tokens, 64000)
            self.assertEqual(args.thinking_budget, 16000)
            self.assertTrue(args.record_requests)
            self.assertEqual(self.baseline.RATES, rates)
            self.assertEqual(self.baseline.cost({"input_tokens": 1_000_000}), 1)
            return {"termination": "done"}

        with patch.object(runtime, "load_baseline", return_value=self.baseline), \
             patch.object(runtime, "engine_for", return_value=engine), \
             patch.object(runtime, "cleanup") as cleanup, \
             patch.object(self.baseline, "official_prompt", return_value="System"), \
             patch.object(self.baseline, "episode", side_effect=fake_episode):
            asyncio.run(runtime.run_prepared(case, prepared, self.out / "run", model="haiku",
                                            max_output_tokens=64000, thinking_budget=16000,
                                            rates=rates, record_requests=True))
        config = json.loads((self.out / "run/config.json").read_text())
        self.assertEqual(config["max_output_tokens_per_call"], 64000)
        self.assertEqual(config["thinking"], {"type": "enabled", "budget_tokens": 16000})
        self.assertEqual(config["temperature"], 1)
        self.assertEqual(config["effort"], "provider_default")
        self.assertEqual(config["rates_usd_per_million"], rates)
        self.assertEqual(original.RATES["input_tokens"], 3)
        self.assertIsNot(self.baseline.RATES, rates)
        cleanup.assert_called_once()
        engine.dispose.assert_called_once()


if __name__ == "__main__":
    unittest.main()
