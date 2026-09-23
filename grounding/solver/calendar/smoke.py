"""Calendar Qwen smoke runner: isolated seed install, preflight, Purdue episode, diff."""
from __future__ import annotations

import asyncio

import requests

from grounding.integrations.agentdiff import smoke_runtime

SERVICE = "calendar"
SEED_NAME = "calendar_default"


def preflight(client, env_id: str) -> dict:
    """Read-only Calendar visibility checks (never mutates; never raises)."""
    checks: list[dict] = []
    errors: list[str] = []
    base = f"{client.base_url}/api/env/{env_id}/services/calendar"
    try:
        response = requests.get(f"{base}/users/me/calendarList", headers=client._headers(), timeout=60)
        try:
            body = response.json()
        except ValueError:
            body = {"non_json_response": response.text[:500]}
        items = body.get("items", []) if isinstance(body, dict) else []
        checks.append({"probe": "GET /users/me/calendarList", "status_code": response.status_code,
                       "count": len(items)})
        if response.status_code != 200:
            errors.append(f"GET /users/me/calendarList returned HTTP {response.status_code}")
    except Exception as exc:
        errors.append(f"GET /users/me/calendarList raised {type(exc).__name__}: {exc}")
    try:
        response = requests.get(f"{base}/calendars/primary", headers=client._headers(), timeout=60)
        try:
            body = response.json()
        except ValueError:
            body = {"non_json_response": response.text[:500]}
        checks.append({"probe": "GET /calendars/primary", "status_code": response.status_code,
                       "id": body.get("id") if isinstance(body, dict) else None})
        if response.status_code != 200:
            errors.append(f"GET /calendars/primary returned HTTP {response.status_code}")
    except Exception as exc:
        errors.append(f"GET /calendars/primary raised {type(exc).__name__}: {exc}")
    return {"checks": checks, "errors": errors}


def main() -> None:
    parser = smoke_runtime.common_parser(__doc__)
    args = parser.parse_args()
    asyncio.run(smoke_runtime.run_smoke(SERVICE, SEED_NAME, preflight, args))


if __name__ == "__main__":
    main()
