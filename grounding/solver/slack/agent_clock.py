"""An episode's time budget that leaves out waiting for Purdue.

Both Qwen episode loops (`grounding/solver/slack/run.py` for Slack, `grounding/integrations/agentdiff/smoke_runtime.py`
for Box, Calendar and Linear) run inside `asyncio.timeout(budget)`. The Purdue client moves that deadline later by
every second it spends waiting, so only the agent's own time counts toward the budget: its successful model calls
and its tool calls. Waiting means:
- the shared rate limiter's queue;
- the pauses after rate-limit and transient errors;
- attempts that fail (errors, and hangs up to the request timeout).

A successful call's time counts in full, although it may include queueing on Purdue's own servers: the responses
are not streamed, so that part cannot be told apart from generation.

A wall ceiling bounds the episode all the same. A cut by the budget is the agent's (termination `timeout`, graded); a
cut by the ceiling is the infrastructure's (termination `ceiling`, retried). A client without the `agent_clock` hook
(the Bedrock client) never moves the deadline, so its episodes keep the plain wall-clock budget.

Added on 2026-09-27 (roadmap_01): before it, the 8-minute budget included the limiter's queue, so under load it cut
long trials at 15–35 turns, before the 40-turn limit.
"""
from __future__ import annotations

import asyncio
import time

BUDGET_SECONDS = 480.0     # the agent's own time per episode (the budget every earlier run used, as wall time)
CEILING_SECONDS = 1800.0   # wall time per episode, waiting included
DESCRIPTION = ("agent clock (since 2026-09-27): with the Purdue client, waiting (the limiter queue, backoffs, failed "
               "attempts) is off the time budget, under a wall ceiling; other clients keep a wall-clock budget")


class AgentClock:
    def __init__(self, budget: float = BUDGET_SECONDS, ceiling: float = CEILING_SECONDS):
        if ceiling < budget:
            raise ValueError("the wall ceiling must not be below the budget")
        self.budget = float(budget)
        self.ceiling = float(ceiling)
        self.waited = 0.0
        self._timeout: asyncio.Timeout | None = None
        self._start = 0.0
        self._t0 = 0.0

    def attach(self, timeout: asyncio.Timeout) -> "AgentClock":
        """Bind the episode's `asyncio.timeout(budget)`; the clock starts now."""
        self._timeout = timeout
        self._start = asyncio.get_running_loop().time()
        self._t0 = time.monotonic()
        return self

    def _move(self, seconds: float) -> float:
        """Move the deadline by `seconds` (later or earlier), never past the ceiling; returns the amount moved."""
        if self._timeout is None or self._timeout.when() is None:
            return 0.0
        now = self._timeout.when()
        target = min(now + seconds, self._start + self.ceiling)
        self._timeout.reschedule(target)
        return target - now

    def pause(self, seconds: float) -> None:
        """Waiting about to happen (a limiter or backoff sleep): the deadline moves first, so the sleep cannot cut
        the episode."""
        self.waited += seconds
        self._move(seconds)

    def hold(self, request_timeout: float) -> float:
        """Before a model request: keep the deadline clear of the request's own timeout. Returns what was moved."""
        return self._move(request_timeout)

    def settle(self, held: float, used: float, succeeded: bool) -> None:
        """After the request: a successful call's time counts toward the budget; a failed attempt's does not."""
        keep = 0.0 if succeeded else used
        if not succeeded:
            self.waited += used
        self._move(keep - held)

    def termination(self) -> str:
        """For a TimeoutError: `ceiling` when the wall ceiling cut the episode, else `timeout` (the agent's budget)."""
        if self._timeout is not None and self._timeout.when() is not None \
                and self._timeout.when() >= self._start + self.ceiling - 1e-6:
            return "ceiling"
        return "timeout"

    def summary(self) -> dict:
        elapsed = time.monotonic() - self._t0 if self._t0 else 0.0
        return {"budget_seconds": self.budget, "ceiling_seconds": self.ceiling,
                "elapsed_seconds": round(elapsed, 3), "waited_seconds": round(self.waited, 3),
                "agent_seconds": round(max(0.0, elapsed - self.waited), 3),
                "rule": "Purdue waiting (limiter queue, backoffs, failed attempts) is off the budget"}
