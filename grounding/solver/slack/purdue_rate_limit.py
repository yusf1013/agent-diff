"""Shared cross-process request-rate limiter for the Purdue GenAI endpoint.

Per-process concurrency limits and reactive backoff do not enforce a shared
provider limit when several investigators, runners, or retries call the API
at once. This module implements a reservation-based sliding-window limiter
backed by a lock file, so every process on this machine draws from the same
per-minute budget before each HTTP attempt (initial calls and retries alike).

State lives in a small JSON file under the system temp directory (override
with PURDUE_RATE_LIMIT_FILE). The window is 60 seconds; the default budget
is 60 reservations per window (override with PURDUE_RATE_LIMIT_PER_MINUTE).
Set PURDUE_RATE_LIMIT_DISABLE=1 to bypass (offline tests only).
"""
from __future__ import annotations

import asyncio
import fcntl
import json
import os
import tempfile
import time
from pathlib import Path

WINDOW_SECONDS = 60.0


def _state_path() -> Path:
    override = os.getenv("PURDUE_RATE_LIMIT_FILE")
    if override:
        return Path(override)
    return Path(tempfile.gettempdir()) / "purdue_genai_rate_limit.json"


def _budget() -> int:
    try:
        value = int(os.getenv("PURDUE_RATE_LIMIT_PER_MINUTE", "60"))
    except ValueError:
        value = 60
    return max(1, value)


def _read_timestamps(path: Path) -> list[float]:
    try:
        data = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []
    if not isinstance(data, list):
        return []
    return [float(t) for t in data if isinstance(t, (int, float))]


def _reserve(now: float, budget: int, path: Path) -> float:
    """Reserve a slot under an exclusive lock. Returns seconds to wait (0 ok)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a+") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            handle.seek(0)
            try:
                data = json.load(handle)
            except (json.JSONDecodeError, OSError):
                data = []
            stamps = [float(t) for t in data if isinstance(t, (int, float))]
            cutoff = now - WINDOW_SECONDS
            stamps = [t for t in stamps if t > cutoff]
            if len(stamps) < budget:
                stamps.append(now)
                handle.seek(0)
                handle.truncate()
                json.dump(stamps, handle)
                return 0.0
            wait = (stamps[0] + WINDOW_SECONDS) - now
            handle.seek(0)
            handle.truncate()
            json.dump(stamps, handle)
            return max(wait, 0.01)
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


async def acquire_purdue_slot(on_wait=None) -> None:
    """Wait until this process holds a shared rate-limit slot. Blocking.

    `on_wait(seconds)`, when given, is told of each wait before it starts (an episode's agent clock keeps it off the
    agent's time budget)."""
    if os.getenv("PURDUE_RATE_LIMIT_DISABLE") == "1":
        return
    path = _state_path()
    budget = _budget()
    while True:
        wait = await asyncio.to_thread(_reserve, time.time(), budget, path)
        if wait <= 0:
            return
        if on_wait is not None:
            on_wait(wait)
        await asyncio.sleep(wait)


def read_state_for_tests(path: Path | None = None) -> list[float]:
    """Return current (unpruned) reservation timestamps. Test helper."""
    return _read_timestamps(path or _state_path())
