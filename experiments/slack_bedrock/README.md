# Slack benchmark on Bedrock

`run.py` selects Slack rows of `all_numbered.jsonl` and runs them with a bounded
pool of workers, each preparing a fresh environment. It extracts the docs formatter
and relevant-docs system prompt from the authors' experiment notebook. Each agent
uses XML ReAct and the repository's BashExecutorProxy inside a dedicated container.
AWS credentials remain with the host-side Bedrock client.

The run uses Sonnet 5, provider-default temperature and effort, five-minute prompt
caching, at most 40 turns, and an eight-minute timeout per episode. The evaluator
receives the original JSONL assertions; these are never sent to the agent.

Build the execution image from the repository root:

```bash
docker build -t agent-diff-slack-executor experiments/slack_bedrock
```

Start a local backend with a migrated PostgreSQL database and run
`backend/utils/seed_slack_template.py` against that database. The backend must be
reachable from the execution containers, which use host networking. Then, from
the sibling bedrock-llm repository:

```bash
uv run --with-editable ../agent-diff/sdk/agent-diff-python \
  python ../agent-diff/experiments/slack_bedrock/run.py \
  --base-url http://127.0.0.1:18000
```

Every invocation makes paid model calls. `--offset` skips completed Slack tasks,
`--limit` controls the number of selected tasks, and `--concurrency` bounds the
number of active episodes (default 10). To complete the remaining 49 after the
first ten, add `--offset 10 --limit 49 --concurrency 10`. Results are saved after every turn.
Cost is computed from separate input/output/cache token categories at the
requested conservative rates: $3/$15 ordinary input/output, $3.75 cache writes,
and $0.30 cache reads per million tokens. It excludes infrastructure costs.

See [results/REPORT.md](results/REPORT.md) for the completed first-ten evaluation
and the separately accounted interrupted batch.

The completed 59-task evaluation is in
[results/full_slack/REPORT.md](results/full_slack/REPORT.md). It combines the
first ten with the remaining 49, replacing only attempts stopped by a known
history-serialization error and including their costs as overhead. `aggregate.py`
checks full task coverage, protocol consistency, and duplicate IDs before writing
the combined score and cost report.
