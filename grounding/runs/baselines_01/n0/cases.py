"""Turn a baseline's tests.json into runnable cases for openclaw_eval_01's runner.

Each test's seed operations are expanded with the kit's seed builders (`autogen_01/kit/seedops.py`), the same code
our writer's seeds go through. `"@name"` references in the assertions are resolved to ids. The case keeps the test's
request, expected outcome and assertions under `baseline`, which the runner never passes to the agent under test
(`openclaw/runtime.py`, `solver_case`).
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, seedops

CODE = {"box": "BOX", "calendar": "CAL", "linear": "LIN", "slack": "SLK"}
REQUIRED = ("id", "request", "seed", "expected", "assertions")


def count_tests(path: Path) -> int | None:
    try:
        return len(json.loads(path.read_text()).get("tests", []))
    except Exception:
        return None


def from_tests(domain: str, data: dict, generator: str = "N0") -> tuple[list[dict], list[str]]:
    tests = data.get("tests") if isinstance(data, dict) else None
    if not isinstance(tests, list) or not tests:
        return [], ["`tests.json` needs a non-empty list under `tests`."]
    built, errors, seen = [], [], set()
    for i, test in enumerate(tests, start=1):
        tid = test.get("id") if isinstance(test, dict) else None
        name = tid or f"test {i}"
        if not isinstance(test, dict):
            errors.append(f"{name}: not an object.")
            continue
        missing = [k for k in REQUIRED if k not in test]
        if missing:
            errors.append(f"{name}: missing {', '.join(missing)}.")
            continue
        if tid in seen:
            errors.append(f"{name}: the id is used twice.")
            continue
        seen.add(tid)
        if not isinstance(test["assertions"], list):
            errors.append(f"{name}: `assertions` must be a list.")
            continue
        try:
            seed, refs, actor = seedops.expand(domain, test["seed"])
        except Exception as exc:  # the seed operations' own message, as a user would see it
            errors.append(f"{name}: the seed could not be created: {exc}")
            continue
        try:
            assertions = seedops.resolve(test["assertions"], refs)
        except Exception as exc:
            errors.append(f"{name}: an assertion refers to an unknown `@name`: {exc}")
            continue
        case = {"case_id": f"{generator}-{CODE[domain]}-{tid}", "domain": domain, "form": "baseline",
                "acting_user_id": actor, "seed": seed, "prompt": str(test["request"]).strip(), "references": [],
                "probes": [],
                "baseline": {"generator": generator, "test_id": tid, "request": test["request"],
                             "expected": test["expected"], "assertions": assertions,
                             "seed_ops": test["seed"], "refs": refs}}
        case["case_sha256"] = derive.digest({k: v for k, v in case.items() if k != "case_sha256"})
        built.append(case)
    return built, errors
