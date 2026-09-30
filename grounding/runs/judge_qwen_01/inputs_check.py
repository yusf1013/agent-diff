"""Check, before any Qwen call, that the replay sends Qwen exactly what Muse received (no model calls).

For every final execution with a Muse verdict:
- the saved prompt is judge.system.md, the separator, and the user text (common.muse_prompt);
- judge.system.md equals today's judge_v2.md plus the domain's replica notes (the prompt is unchanged);
- the user text ends with the kit's closing line;
- the user text rebuilt from the attempt folder by the kit (judge2.triage and bundle.build, with the form Muse was
  given) equals the saved one, up to the order of keys inside the diff's UPDATE lines. bundle.diff_text builds that
  dict from a set of field names, so its order follows Python's per-process string hashing.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.inputs_check

Writes inputs_check.json.
"""
from __future__ import annotations

import json
import re
from collections import Counter

from grounding.runs.autogen_01.kit import bundle
from grounding.runs.autogen_02.kit import judge2
from grounding.runs.judge_qwen_01.common import ASK, HERE, attempt_path, judged_keys, muse_prompt, muse_verdict

UPDATE = re.compile(r"^(- UPDATE \S+ `[^`]*`: )(\{.*\})$")


def normal(text: str) -> str:
    out = []
    for line in text.splitlines():
        m = UPDATE.match(line)
        if m:
            try:
                line = m.group(1) + json.dumps(json.loads(m.group(2)), sort_keys=True, ensure_ascii=False)
            except ValueError:
                pass  # a truncated dict (diff_text cuts at 800 characters) stays as is
        out.append(line)
    return "\n".join(out)


def main():
    counts, problems = Counter(), []
    prompt = judge2.PROMPT.read_text()
    for key in judged_keys():
        v = muse_verdict(key)
        system, user = muse_prompt(key)
        attempt = attempt_path(key)
        run, trial, _ = key.split("/")
        case, summary, tri = judge2.triage(run, trial, attempt)
        expected_system = prompt + "\n\n# Replica notes for this domain\n\n" + \
            (judge2.INPUTS / case["domain"] / "replica.md").read_text()
        rebuilt = bundle.build(case, attempt, v["form"], tri, summary) + ASK
        checks = {"system_is_current_prompt": system == expected_system, "ends_with_ask": user.endswith(ASK),
                  "user_exact": rebuilt == user, "user_same_up_to_key_order": normal(rebuilt) == normal(user)}
        for name, ok in checks.items():
            counts[name] += ok
        if not (checks["system_is_current_prompt"] and checks["ends_with_ask"] and checks["user_same_up_to_key_order"]):
            problems.append({"key": key, **checks})
    out = {"executions": len(judged_keys()), "passed": dict(counts), "problems": problems}
    (HERE / "inputs_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "problems"}, indent=1), f"{len(problems)} problems")


if __name__ == "__main__":
    main()
