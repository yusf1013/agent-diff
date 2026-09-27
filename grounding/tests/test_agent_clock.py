"""The agent clock: Purdue waiting stays off an episode's time budget, under a wall ceiling (no network)."""
import asyncio
import os
from unittest import mock

import httpx

os.environ.setdefault("PURDUE_RATE_LIMIT_DISABLE", "1")

from grounding.solver.slack import purdue_client as pc  # noqa: E402
from grounding.solver.slack.agent_clock import AgentClock  # noqa: E402


def _episode(budget, ceiling, body):
    """Run `body(clock)` inside asyncio.timeout(budget) with the clock attached; returns (termination, clock)."""
    async def run():
        clock = AgentClock(budget, ceiling)
        try:
            async with asyncio.timeout(budget) as t:
                clock.attach(t)
                await body(clock)
            return "done", clock
        except TimeoutError:
            return clock.termination(), clock
    return asyncio.run(run())


def test_waiting_does_not_use_the_budget():
    async def body(clock):
        clock.pause(0.3)                 # the limiter's queue, longer than the whole budget
        await asyncio.sleep(0.3)
        await asyncio.sleep(0.05)        # the agent's own work
    term, clock = _episode(0.2, 5.0, body)
    assert term == "done"
    assert abs(clock.waited - 0.3) < 1e-9


def test_the_agents_own_time_still_runs_out():
    async def body(clock):
        await asyncio.sleep(0.4)
    term, _ = _episode(0.1, 5.0, body)
    assert term == "timeout"


def test_the_ceiling_cuts_endless_waiting():
    async def body(clock):
        for _ in range(10):
            clock.pause(0.2)
            await asyncio.sleep(0.2)
    term, _ = _episode(0.1, 0.5, body)
    assert term == "ceiling"


def test_hold_and_settle():
    async def body(clock):
        before = clock._timeout.when()
        held = clock.hold(10.0)
        clock.settle(held, 0.0, succeeded=True)     # a successful call: its time counts, the deadline returns
        assert abs(clock._timeout.when() - before) < 1e-6
        held = clock.hold(10.0)
        clock.settle(held, 2.0, succeeded=False)    # a failed attempt of 2 s: the deadline ends 2 s later
        assert abs(clock._timeout.when() - (before + 2.0)) < 1e-6
        assert clock.waited == 2.0
    term, _ = _episode(5.0, 30.0, body)
    assert term == "done"


def _ok(request):
    return httpx.Response(200, json={"id": "r", "model": "m",
                                     "choices": [{"message": {"content": "<done>x</done>"}, "finish_reason": "stop"}],
                                     "usage": {"prompt_tokens": 1, "completion_tokens": 1}}, request=request)


def test_purdue_client_tells_the_clock_of_limiter_waits_backoffs_and_failures():
    """One limiter wait, one rate-limited attempt and its backoff: all of it off the budget, which is shorter than
    the waiting."""
    calls = {"n": 0}

    async def fake_post(url, headers=None, json=None):
        calls["n"] += 1
        req = httpx.Request("POST", str(url))
        await asyncio.sleep(0.05)
        if calls["n"] == 1:
            return httpx.Response(400, text="Rate limit exceeded", request=req)
        return _ok(req)

    async def fake_slot(on_wait=None):
        if on_wait:
            on_wait(0.1)
        await asyncio.sleep(0.1)

    async def run():
        client = pc.PurdueClient(model_id="m", api_key="test", timeout=30.0)
        client._client.post = fake_post
        client._rate_wait_seconds = lambda attempt: 0.1
        clock = AgentClock(0.2, 5.0)
        client.agent_clock = clock
        try:
            async with asyncio.timeout(0.2) as t:
                clock.attach(t)
                with mock.patch.object(pc, "acquire_purdue_slot", fake_slot):
                    await client.create([{"role": "user", "content": "hi"}], max_tokens=10)
            return "done", clock
        except TimeoutError:
            return clock.termination(), clock
        finally:
            await client.close()

    term, clock = asyncio.run(run())
    assert term == "done"           # 0.45 s of wall time against a 0.2 s budget
    assert calls["n"] == 2
    # two limiter waits (0.1 each), the failed attempt (~0.05) and the backoff (0.1)
    assert 0.33 < clock.waited < 0.5
