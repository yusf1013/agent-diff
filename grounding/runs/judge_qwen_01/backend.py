"""An OpenAI-compatible backend for judge v2's calls: the self-hosted Qwen3.8-27B (or Purdue's) in place of Muse.

A drop-in for `autogen_01.kit.agent.run` on calls without tools: `run(call)` takes the same `agent.Call` and returns
a result with the fields judge v2 reads (`structured_output`, `result`, `backend`, `usage`, `total_cost_usd`).
autogen_01's agent.py is not changed.

- **Endpoint, key, model and limiter** come from the launcher (`SOLVER_BACKEND=selfhost`, or `purdue`), through the
  toy harness's `PurdueClient`: non-streaming, so cut streams do not matter; every HTTP attempt takes a slot from the
  limiter shared by all sessions on this machine; Purdue's rate-limit 400s are retried. The key is never read, logged
  or saved here.
- **Messages:** `call.system_append` is the system message and `call.prompt` the user message, as Claude Code gets
  them. Muse has no system-prompt flag, so agent.py sent Muse the two joined by a "---" line as one user message,
  inside Muse Code's own harness.
- **Output schema:** `call.schema`, made strict as agent.py makes it for Muse (`additionalProperties: false`), sent as
  `response_format` (json_schema). vLLM enforces it on the answer after the model's reasoning.
- **Settings:** the provider's defaults for sampling and thinking, as the solver runs use; `max_tokens` is
  `QWEN_JUDGE_MAX_TOKENS` (16,384); each HTTP request may take `QWEN_JUDGE_TIMEOUT` seconds (1,800).
- **A failed attempt** (an HTTP error after the client's own retries, an answer cut at max_tokens, or an answer that
  is not JSON under the schema) is kept as `NN-judge.failed.json`, and the call is made again from scratch, up to
  `call.retries` more times, as agent.py does.

Saved per attempt under `call.log_dir`: `judge.system.md` (the system message), `NN-judge.prompt.md` (the user
message), `NN-judge.request.json` (the request body, without the auth header) and `NN-judge.result.json` (the
result, with the raw response, reasoning included). A usage row goes to `call.calls_log`, with cost 0: the self-host
has no per-token charge.
"""
from __future__ import annotations

import asyncio
import json
import os
import time
from datetime import datetime, timezone

from grounding.runs.autogen_01.kit import agent
from grounding.solver.slack.purdue_client import PurdueClient

HOST = os.environ.get("SOLVER_BACKEND", "purdue")
MODEL = os.environ.get("QWEN_JUDGE_MODEL") or os.environ.get("SOLVER_MODEL") or (
    "qwen3.8:27b" if HOST == "purdue" else "qwen3.8-27b")
MAX_TOKENS = int(os.environ.get("QWEN_JUDGE_MAX_TOKENS", "16384"))
TIMEOUT = float(os.environ.get("QWEN_JUDGE_TIMEOUT", "1800"))
HTTP_ATTEMPTS = int(os.environ.get("QWEN_JUDGE_HTTP_ATTEMPTS", "4"))
BACKEND = f"qwen-{HOST}"


def settings() -> dict:
    return {"backend": BACKEND, "host": HOST, "endpoint": os.environ.get("PURDUE_BASE_URL") or "Purdue default",
            "model": MODEL, "max_tokens": MAX_TOKENS, "timeout_s": TIMEOUT, "http_attempts": HTTP_ATTEMPTS,
            "limiter_file": os.environ.get("PURDUE_RATE_LIMIT_FILE"),
            "limiter_per_minute": os.environ.get("PURDUE_RATE_LIMIT_PER_MINUTE"),
            "sampling": "provider defaults", "thinking": "provider default (on)"}


def check(answer, schema: dict) -> str | None:
    """Why an answer does not fit the schema (required keys, types, enums), or None when it fits."""
    if not isinstance(answer, dict):
        return "not a JSON object"
    for name in schema.get("required", []):
        if name not in answer:
            return f"missing {name}"
    for name, spec in schema.get("properties", {}).items():
        value = answer.get(name)
        if spec.get("type") == "string" and not isinstance(value, str):
            return f"{name} is not a string"
        if spec.get("type") == "array" and not (isinstance(value, list) and all(isinstance(x, str) for x in value)):
            return f"{name} is not a list of strings"
        if "enum" in spec and value not in spec["enum"]:
            return f"{name} is not one of {spec['enum']}"
    extra = set(answer) - set(schema.get("properties", {}))
    return f"unexpected keys {sorted(extra)}" if extra else None


async def _ask(system: str | None, user: str, response_format: dict | None) -> tuple[dict, str, dict, float]:
    client = PurdueClient(model_id=MODEL, timeout=TIMEOUT, max_attempts=HTTP_ATTEMPTS)
    options = {"response_format": response_format} if response_format else {}
    start = time.time()
    try:
        response = await client.create([{"role": "user", "content": user}], system=system, max_tokens=MAX_TOKENS,
                                       usage_label="judge", **options)
    finally:
        await client.close()
    return response.raw or {}, response.text, response.message.model_dump(), time.time() - start


def _row(call: agent.Call, index: int, attempt: int, seconds: float, raw: dict | None, failed: str | None) -> dict:
    raw = raw or {}
    usage = raw.get("usage") or {}
    choice = (raw.get("choices") or [{}])[0]
    message = choice.get("message") or {}
    reasoning = message.get("reasoning") or message.get("reasoning_content") or ""
    return {"utc": datetime.now(timezone.utc).isoformat(), "role": call.role, "label": call.label, "index": index,
            "attempt": attempt, "resumed": False, "session_id": None, "models": [raw.get("model", MODEL)],
            "num_turns": 1, "seconds": round(seconds, 1), "is_error": bool(failed), "subtype": choice.get("finish_reason"),
            "input_tokens": usage.get("prompt_tokens", 0), "output_tokens": usage.get("completion_tokens", 0),
            "cache_creation_input_tokens": 0,
            "cache_read_input_tokens": ((usage.get("prompt_tokens_details") or {}).get("cached_tokens") or 0),
            "cost_usd_list_price": 0.0, "cost_basis": "self-hosted, no per-token charge",
            "backend": BACKEND, "host": HOST, "system_fingerprint": raw.get("system_fingerprint"),
            "reasoning_chars": len(reasoning), **({"failed": failed} if failed else {})}


def run(call: agent.Call) -> dict:
    """One judge call (no tools). Returns the result dict, or raises after every attempt failed."""
    if call.tools or call.write or call.resume:
        raise ValueError("this backend serves single-turn calls without tools")
    call.log_dir.mkdir(parents=True, exist_ok=True)
    if call.system_append:
        (call.log_dir / f"{call.role}.system.md").write_text(call.system_append)
    response_format = None
    if call.schema:
        response_format = {"type": "json_schema",
                           "json_schema": {"name": "verdict", "schema": agent._strict_schema(call.schema)}}
    last_error = None
    for attempt in range(1, call.retries + 2):
        index = agent._next_index(call.log_dir)
        stem = f"{index:02}-{call.role}"
        (call.log_dir / f"{stem}.prompt.md").write_text(call.prompt)
        messages = ([{"role": "system", "content": call.system_append}] if call.system_append else []) + \
            [{"role": "user", "content": call.prompt}]
        body = {"model": MODEL, "messages": messages, "max_tokens": MAX_TOKENS, "stream": False,
                **({"response_format": response_format} if response_format else {})}
        (call.log_dir / f"{stem}.request.json").write_text(json.dumps(
            {"endpoint": os.environ.get("PURDUE_BASE_URL") or "Purdue default", "body": body}, indent=1,
            ensure_ascii=False))
        start = time.time()
        raw, text, message, failed, answer = None, "", None, None, None
        try:
            raw, text, message, _ = asyncio.run(_ask(call.system_append, call.prompt, response_format))
        except Exception as exc:  # the client's own retries are spent
            failed = f"http: {type(exc).__name__}: {str(exc)[:800]}"
        seconds = time.time() - start
        if not failed:
            finish = ((raw.get("choices") or [{}])[0]).get("finish_reason")
            if finish == "length":
                failed = f"cut at max_tokens ({MAX_TOKENS})"
            elif call.schema:
                try:
                    answer = json.loads(text)
                    problem = check(answer, call.schema)
                    if problem:
                        failed = f"answer does not fit the schema: {problem}"
                except ValueError:
                    failed = "answer is not JSON"
        usage = (raw or {}).get("usage") or {}
        result = {"session_id": None, "result": text, "structured_output": answer if not failed else None,
                  "is_error": bool(failed), "subtype": ((raw or {}).get("choices") or [{}])[0].get("finish_reason"),
                  "num_turns": 1, "backend": BACKEND, "host": HOST, "model": (raw or {}).get("model", MODEL),
                  "system_fingerprint": (raw or {}).get("system_fingerprint"), "settings": settings(),
                  "usage": {"input_tokens": usage.get("prompt_tokens", 0),
                            "output_tokens": usage.get("completion_tokens", 0),
                            "cache_read_input_tokens": ((usage.get("prompt_tokens_details") or {}).get(
                                "cached_tokens") or 0),
                            "cache_creation_input_tokens": 0},
                  "raw_usage": usage, "total_cost_usd": 0.0, "seconds": round(seconds, 1),
                  "message": message, "raw_response": raw}
        row = _row(call, index, attempt, seconds, raw, failed)
        if call.calls_log:
            with call.calls_log.open("a") as fh:
                fh.write(json.dumps(row) + "\n")
        if failed:
            last_error = {"error": failed, "result": result}
            (call.log_dir / f"{stem}.failed.json").write_text(json.dumps(last_error, indent=1, ensure_ascii=False))
            time.sleep(10 * attempt)
            continue
        (call.log_dir / f"{stem}.result.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
        return result
    raise RuntimeError(f"{call.role} {call.label}: every attempt failed; last: "
                       f"{(last_error or {}).get('error', '')[:500]}")
