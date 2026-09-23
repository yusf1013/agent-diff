"""Linear Qwen smoke runner: isolated seed install, preflight, Purdue episode, diff."""
from __future__ import annotations

import asyncio

import requests

from grounding.integrations.agentdiff import smoke_runtime

SERVICE = "linear"
SEED_NAME = "linear_expanded"


def preflight(client, env_id: str) -> dict:
    """Read-only Linear visibility checks (never mutates; never raises)."""
    checks: list[dict] = []
    errors: list[str] = []
    url = f"{client.base_url}/api/env/{env_id}/services/linear/graphql"
    headers = {**client._headers(), "Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, timeout=60,
                                 json={"query": "{ teams { nodes { id name key } } }"})
        try:
            body = response.json()
        except ValueError:
            body = {"non_json_response": response.text[:500]}
        nodes = ((body.get("data") or {}).get("teams") or {}).get("nodes", []) if isinstance(body, dict) else []
        checks.append({"probe": "POST teams query", "status_code": response.status_code,
                       "team_count": len(nodes),
                       "has_errors": bool(body.get("errors")) if isinstance(body, dict) else None})
        if response.status_code != 200 or not isinstance(body, dict) or body.get("errors") or not nodes:
            errors.append(f"POST teams query returned HTTP {response.status_code} "
                          f"errors={body.get('errors') if isinstance(body, dict) else body}")
    except Exception as exc:
        errors.append(f"POST teams query raised {type(exc).__name__}: {exc}")
    return {"checks": checks, "errors": errors}


def main() -> None:
    parser = smoke_runtime.common_parser(__doc__)
    args = parser.parse_args()
    asyncio.run(smoke_runtime.run_smoke(SERVICE, SEED_NAME, preflight, args))


if __name__ == "__main__":
    main()
