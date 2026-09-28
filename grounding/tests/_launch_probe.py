"""Test helper run through fact_coverage_02/launch.py: prints, as JSON, the solver settings the launcher set.

The key is never printed: only whether it is set, and whether it equals $PROBE_EXPECT_KEY. With --ping it also sends
one real request through PurdueClient (a live check by hand; the offline tests never pass it).
"""
import asyncio
import json
import os
import sys

SETTINGS = ("SOLVER_BACKEND", "SOLVER_MODEL", "PURDUE_BASE_URL", "PURDUE_RATE_LIMIT_FILE",
            "PURDUE_RATE_LIMIT_PER_MINUTE")


def main():
    out = {k: os.environ.get(k) for k in SETTINGS}
    expect = os.environ.get("PROBE_EXPECT_KEY")
    out["key_set"] = bool(os.environ.get("GENAI_API_KEY"))
    out["key_matches"] = None if expect is None else os.environ.get("GENAI_API_KEY") == expect
    if "--ping" in sys.argv:
        from grounding.solver.slack.purdue_client import PurdueClient

        async def ping():
            client = PurdueClient(model_id=os.environ.get("SOLVER_MODEL") or "qwen3.8:27b", timeout=120)
            try:
                r = await client.create([{"role": "user", "content": "Reply with the single word: ready"}],
                                        max_tokens=2000)
                return {"text": r.text[:80], "usage": r.usage.to_dict()}
            finally:
                await client.close()

        out["ping"] = asyncio.run(ping())
    print(json.dumps(out))


if __name__ == "__main__":
    main()
