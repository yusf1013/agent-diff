"""Box Qwen smoke runner: isolated seed install, preflight, Purdue episode, diff."""
from __future__ import annotations

import asyncio

import requests

from grounding.integrations.agentdiff import smoke_runtime

SERVICE = "box"
SEED_NAME = "box_default"


def preflight(client, env_id: str) -> dict:
    """Read-only Box visibility checks (never mutates; never raises)."""
    checks: list[dict] = []
    errors: list[str] = []
    base = f"{client.base_url}/api/env/{env_id}/services/box/2.0"
    try:
        response = requests.get(f"{base}/users/me", headers=client._headers(), timeout=60)
        try:
            body = response.json()
        except ValueError:
            body = {"non_json_response": response.text[:500]}
        checks.append({"probe": "GET /users/me", "status_code": response.status_code,
                       "body_keys": sorted(body) if isinstance(body, dict) else []})
        if response.status_code != 200 or not isinstance(body, dict) or "id" not in body:
            errors.append(f"GET /users/me returned HTTP {response.status_code}")
    except Exception as exc:
        errors.append(f"GET /users/me raised {type(exc).__name__}: {exc}")
    try:
        response = requests.get(f"{base}/folders/0", headers=client._headers(), timeout=60)
        try:
            body = response.json()
        except ValueError:
            body = {"non_json_response": response.text[:500]}
        checks.append({"probe": "GET /folders/0", "status_code": response.status_code,
                       "name": body.get("name") if isinstance(body, dict) else None})
        if response.status_code != 200:
            errors.append(f"GET /folders/0 returned HTTP {response.status_code}")
    except Exception as exc:
        errors.append(f"GET /folders/0 raised {type(exc).__name__}: {exc}")
    try:
        response = requests.get(f"{base}/folders/0/items", params={"limit": 5},
                                headers=client._headers(), timeout=60)
        try:
            body = response.json()
        except ValueError:
            body = {"non_json_response": response.text[:500]}
        checks.append({"probe": "GET /folders/0/items", "status_code": response.status_code,
                       "total_count": body.get("total_count") if isinstance(body, dict) else None})
        if response.status_code != 200:
            errors.append(f"GET /folders/0/items returned HTTP {response.status_code}")
    except Exception as exc:
        errors.append(f"GET /folders/0/items raised {type(exc).__name__}: {exc}")
    return {"checks": checks, "errors": errors}


def main() -> None:
    parser = smoke_runtime.common_parser(__doc__)
    args = parser.parse_args()
    asyncio.run(smoke_runtime.run_smoke(SERVICE, SEED_NAME, preflight, args))


if __name__ == "__main__":
    main()
