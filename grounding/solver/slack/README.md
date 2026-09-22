# Slack solver runner

This is our Bedrock/Docker runner around the benchmark's ReAct convention. The solver prompt is extracted from the prompt constant and formatter in AgentDiff's `experiments/kdd 2026/agent-diff bench.ipynb`, then populated with the existing Slack API docs. Notebook outputs are not executed. The local runner and sandbox bridge are ours; their prompt source is upstream.

`run.py` runs original numbered tasks, saving new baseline results under [runs/slack_baseline](../../runs/slack_baseline/). `sandbox_bridge.py` routes the sandbox's requests to its isolated service. Build the adjacent Dockerfile as `agent-diff-slack-executor`. See `python -m grounding.solver.slack.run --help` for baseline options. Supply the repository SDK on `PYTHONPATH` or install it, and use a Python environment with `bedrock_llm` and the runner's dependencies.

Generated cases use [the AgentDiff adapter](../../integrations/agentdiff/runtime.py), which calls the same episode implementation and records the exact system prompt, model/configuration, trajectory, termination, and usage. State snapshots and native diffs go to the case's `environment/`; prepared evaluator evidence goes to `evaluation/inputs/`.

`compare_manual.py` runs a fixed custom suite on Sonnet 5 and Haiku 4.5, with isolated environments, explicit caching, preserved logical SDK requests, and per-model usage accounting. Run `python -m grounding.solver.slack.compare_manual --help` for options. Existing outcomes are skipped on resume; infrastructure retries require the explicit retry flag and retain earlier attempts. It does not grade the runs. The [57-case comparison](../../runs/manual_comparison_01/report.md) contains the subsequent manual review.

The baseline model defaults, prompt, 40-turn limit, timeout, and recovery behavior are preserved. Optional thinking/output limits and price overrides are recorded per invocation; Haiku's explicit thinking setting does not change Sonnet's baseline defaults.
