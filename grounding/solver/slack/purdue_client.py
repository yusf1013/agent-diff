"""Async OpenAI-compatible client for Purdue GenAI Studio, mirroring BedrockClaudeClient.

Interface-compatible with the subset used by grounding/solver/slack/run.py:
episode(): BedrockClaudeClient(model_id, prompt_caching, timeout),
create(messages, system, max_tokens, usage_label, ...),
response.text / response.message.model_dump() / response.usage.to_dict(),
llm.usage.snapshot().to_dict(), llm._add_cache_breakpoints(request) (no-op),
await llm.close().

No prompt caching, no thinking budgets, no sampling overrides: provider defaults.
API key comes from GENAI_API_KEY env var only; never logged or saved.
"""
from __future__ import annotations

import asyncio
import logging
import os
from dataclasses import dataclass
from typing import Any
from collections.abc import Iterable, Mapping

import httpx

from bedrock_llm.usage import TokenUsage, UsageTracker

logger = logging.getLogger(__name__)

DEFAULT_BASE_URL = "https://genai.rcac.purdue.edu/api/chat/completions"


@dataclass(frozen=True, slots=True)
class PurdueResponse:
    text: str
    usage: TokenUsage
    message: Any
    raw: Any = None


class _RateLimitError(RuntimeError):
    pass


class _Block:
    def __init__(self, type: str, text: str = "", **extra: Any) -> None:
        self.type = type
        self.text = text
        for key, value in extra.items():
            setattr(self, key, value)

    def model_dump(self, mode: str = "json", **kwargs: Any) -> dict[str, Any]:
        # Evidence serialization: thinking blocks keep their text here. The
        # conversation path (_content_to_text) excludes non-text blocks by
        # type, so this does not change what is sent on later turns.
        data = {"type": self.type}
        if self.type in ("text", "thinking"):
            data["text"] = self.text
        for key in ("thinking", "signature", "reasoning"):
            if hasattr(self, key):
                data[key] = getattr(self, key)
        return data


class _Message:
    """Minimal stand-in for an SDK message with model_dump()."""

    def __init__(self, id: str | None, model: str, content: list[_Block],
                 stop_reason: str | None = None, raw: Any = None) -> None:
        self.id = id
        self.model = model
        self.content = content
        self.stop_reason = stop_reason
        self.raw = raw

    def model_dump(self, mode: str = "json", **kwargs: Any) -> dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "stop_reason": self.stop_reason,
            "content": [b.model_dump(mode=mode) for b in self.content],
            "raw": self.raw,
        }


def _content_to_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, Mapping):
                block_type = block.get("type")
                if block_type is not None and block_type != "text":
                    continue
                if block_type == "text":
                    parts.append(block.get("text", ""))
                elif "text" in block:
                    parts.append(str(block["text"]))
            elif getattr(block, "type", "text") != "text":
                continue
            elif hasattr(block, "text"):
                parts.append(getattr(block, "text") or "")
            else:
                parts.append(str(block))
        return "".join(parts)
    return str(content)


class PurdueClient:
    def __init__(
        self,
        model_id: str | None = None,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        prompt_caching: bool = False,
        usage_tracker: UsageTracker | None = None,
        timeout: float = 480.0,
        max_attempts: int = 6,
        backoff_base: float = 2.0,
        max_output_tokens: int | None = None,
        **_: Any,
    ) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        key = api_key or os.getenv("GENAI_API_KEY")
        if not key:
            raise ValueError("GENAI_API_KEY is required for Purdue GenAI Studio")
        self.model_id = model_id or os.getenv("PURDUE_MODEL_ID") or "qwen3.6:27b"
        self.base_url = base_url or os.getenv("PURDUE_BASE_URL") or DEFAULT_BASE_URL
        self.prompt_caching = False
        self.max_output_tokens = max_output_tokens
        self.usage = usage_tracker if usage_tracker is not None else UsageTracker()
        self.max_attempts = max_attempts
        self.backoff_base = backoff_base
        self._client = httpx.AsyncClient(timeout=timeout)
        self._api_key = key

    def _add_cache_breakpoints(self, request: dict[str, Any]) -> None:
        return None

    def _is_retryable(self, exc: BaseException) -> bool:
        if isinstance(exc, (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteTimeout,
                            httpx.PoolTimeout, httpx.RemoteProtocolError)):
            return True
        if isinstance(exc, _RateLimitError):
            return True
        if isinstance(exc, httpx.HTTPStatusError):
            if exc.response.status_code in (408, 409, 425, 429) or exc.response.status_code >= 500:
                return True
            if exc.response.status_code == 400:
                try:
                    body = exc.response.text or ""
                except Exception:
                    body = ""
                lowered = body.lower()
                if ("rate limit" in lowered or "rate_limit" in lowered
                        or "server connection error" in lowered
                        or "overloaded" in lowered or "try again" in lowered):
                    return True
        return False

    def _rate_wait_seconds(self, attempt: int) -> float:
        return min(60.0, 10.0 * (2 ** (attempt - 1)))

    def _openai_messages(self, messages: Iterable[Mapping[str, Any]], system: Any) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        if system is not None:
            out.append({"role": "system", "content": _content_to_text(system)})
        for msg in messages:
            role = msg.get("role", "user")
            out.append({"role": role, "content": _content_to_text(msg.get("content"))})
        return out

    async def create(
        self,
        messages: Iterable[Mapping[str, Any]],
        *,
        max_tokens: int = 16384,
        system: Any = None,
        usage_label: str | None = None,
        prompt_caching: bool | None = None,
        **request_options: Any,
    ) -> PurdueResponse:
        if max_tokens < 1:
            raise ValueError("max_tokens must be positive")
        forbidden = {"model", "messages", "max_tokens", "system"} & request_options.keys()
        if forbidden:
            raise TypeError(f"Pass {sorted(forbidden)} via named create() arguments")
        request_options.pop("thinking", None)
        request_options.pop("temperature", None)
        effective_max = max(max_tokens, self.max_output_tokens or max_tokens)
        body: dict[str, Any] = {
            "model": self.model_id,
            "messages": self._openai_messages(messages, system),
            "max_tokens": effective_max,
            "stream": False,
            **request_options,
        }
        headers = {"Authorization": "Bearer " + self._api_key, "Content-Type": "application/json"}
        last_exc: BaseException | None = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                logger.info("Calling %s on Purdue GenAI (attempt %s/%s, max_tokens=%s)",
                            self.model_id, attempt, self.max_attempts, effective_max)
                response = await self._client.post(self.base_url, headers=headers, json=body)
                try:
                    response.raise_for_status()
                except httpx.HTTPStatusError as http_exc:
                    try:
                        detail = (http_exc.response.text or "")[:300]
                    except Exception:
                        detail = ""
                    lowered = detail.lower()
                    if http_exc.response.status_code == 400 and (
                            "rate limit" in lowered or "server connection error" in lowered
                            or "overloaded" in lowered):
                        raise _RateLimitError(f"Transient Purdue 400: {detail}") from http_exc
                    raise httpx.HTTPStatusError(
                        f"{http_exc} | body: {detail}",
                        request=http_exc.request, response=http_exc.response) from http_exc
                data = response.json()
                if data is None:
                    raise _RateLimitError("Purdue returned JSON null (documented rate-limit signal)")
                choice = (data.get("choices") or [{}])[0]
                msg = choice.get("message") or {}
                text = (msg.get("content") or "").strip()
                if not isinstance(text, str):
                    text = str(text)
                finish = choice.get("finish_reason")
                raw_usage = data.get("usage") or {}
                prompt_t = int(raw_usage.get("prompt_tokens") or 0)
                completion_t = int(raw_usage.get("completion_tokens") or 0)
                usage = self.usage.record(
                    {"input_tokens": prompt_t, "output_tokens": completion_t,
                     "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0},
                    model=self.model_id, label=usage_label,
                )
                blocks: list[_Block] = []
                reasoning = msg.get("reasoning_content") or msg.get("reasoning")
                if reasoning:
                    blocks.append(_Block(type="thinking", text=str(reasoning)))
                blocks.append(_Block(type="text", text=text))
                message = _Message(id=data.get("id"), model=data.get("model", self.model_id),
                                   content=blocks, stop_reason=finish, raw=data)
                if finish == "length":
                    logger.warning("Purdue response hit max_tokens (%s) for label %s",
                                   effective_max, usage_label)
                return PurdueResponse(text=text, usage=usage, message=message, raw=data)
            except Exception as exc:
                last_exc = exc
                if attempt >= self.max_attempts or not self._is_retryable(exc):
                    try:
                        self.usage.record_failure()
                    except Exception:
                        pass
                    raise
                try:
                    self.usage.record_retry()
                except Exception:
                    pass
                if isinstance(exc, _RateLimitError) or (
                        isinstance(exc, httpx.HTTPStatusError) and "rate limit" in str(exc).lower()):
                    await asyncio.sleep(self._rate_wait_seconds(attempt))
                else:
                    await asyncio.sleep(self.backoff_base * (2 ** (attempt - 1)))
        assert last_exc is not None
        raise last_exc

    async def close(self) -> None:
        try:
            await self._client.aclose()
        except Exception:
            pass
