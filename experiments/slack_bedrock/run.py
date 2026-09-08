"""Run numbered Slack tasks with the authors' documented ReAct setup on Bedrock.

Use a Python environment with bedrock-llm, agent-diff, and httpx installed.
The backend must already be seeded. Build the adjacent Dockerfile as
agent-diff-slack-executor before running. No credentials enter agent containers.
"""
from __future__ import annotations

import argparse
import ast
import asyncio
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

from agent_diff import AgentDiff
from bedrock_llm import BedrockClaudeClient

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RATES = {"input_tokens": 3.0, "output_tokens": 15.0,
         "cache_creation_input_tokens": 3.75, "cache_read_input_tokens": 0.30}


def official_prompt():
    """Extract only the formatter and prompt constant, never notebook outputs."""
    notebook = ROOT / "experiments/kdd 2026/agent-diff bench.ipynb"
    namespace = {}
    template = None
    for cell in json.loads(notebook.read_text())["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name == "format_docs_markdown":
                exec(compile(ast.Module(body=[node], type_ignores=[]), str(notebook), "exec"), namespace)
            if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "REACT_SYSTEM_PROMPT_WITH_API_DOCS"
                for target in node.targets
            ):
                template = ast.literal_eval(node.value)
    if template is None or "format_docs_markdown" not in namespace:
        raise RuntimeError("Official notebook prompt/formatter missing")
    docs = json.loads((ROOT / "examples/slack/testsuites/slack_docs/slack_api_full_docs.json").read_text())
    return template.format(
        service_name="Slack", base_url="https://slack.com/api",
        service_description="Slack workspace messaging and collaboration API",
        extra_context="",
        api_docs=namespace["format_docs_markdown"](docs),
    )


def save(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2, default=str) + "\n")
    temporary.replace(path)


def cost(tokens):
    return sum(tokens.get(key, 0) * rate / 1_000_000 for key, rate in RATES.items())


def assistant_content(message):
    """Keep model content while removing response-only fields and empty text."""
    return [
        block.model_dump(mode="json", exclude={"parsed_output"}, exclude_none=True)
        for block in message.content
        if not (block.type == "text" and not block.text)
    ]


async def episode(row, args, prompt, out):
    client = AgentDiff(base_url=args.base_url)
    env = run = process = None
    record = {"test_id": row["test_id"], "test_name": row["test_name"],
              "row_number": row["#"], "question": row["question"], "steps": []}
    path = out / (row["test_id"] + ".json")
    llm = BedrockClaudeClient(model_id=args.model, prompt_caching=True, timeout=480)
    container = None
    try:
        info = json.loads(row["info"])
        env = await asyncio.to_thread(client.init_env,
            templateService="slack", templateName=info["seed_template"],
            impersonateUserId=info["impersonate_user_id"])
        record["environment_id"] = env.environmentId
        container = "ad-slack10-" + env.environmentId
        process = await asyncio.create_subprocess_exec(
            "docker", "run", "--rm", "-i", "--name", container, "--network", "host",
            "-e", "EVAL_ENV_ID=" + env.environmentId,
            "-e", "EVAL_BASE_URL=" + args.base_url,
            "-v", str(ROOT / "sdk/agent-diff-python/agent_diff/code_executor.py") + ":/opt/agent/code_executor.py:ro",
            "-v", str(HERE / "sandbox_bridge.py") + ":/opt/agent/bridge.py:ro",
            "agent-diff-slack-executor", "python", "-u", "/opt/agent/bridge.py",
            stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            limit=16 * 1024 * 1024,
        )
        run = await asyncio.to_thread(client.start_run, envId=env.environmentId)
        record["run_id"] = run.runId
        messages = [{"role": "user", "content": "Task: " + row["question"]}]
        started = time.monotonic()
        record["started_at"] = datetime.now(timezone.utc).isoformat()
        try:
            async with asyncio.timeout(480):
                for turn in range(1, 41):
                    response = await llm.create(messages, system=prompt, max_tokens=128000,
                                                usage_label=row["test_id"])
                    text = response.text
                    step = {"turn": turn, "response": response.message.model_dump(mode="json"),
                            "usage": response.usage.to_dict()}
                    record["steps"].append(step)
                    record["usage"] = llm.usage.snapshot().to_dict()
                    save(path, record)
                    content = assistant_content(response.message)
                    if content:
                        messages.append({"role": "assistant", "content": content})
                    action = re.search(r"<action>(.*?)</action>", text, re.DOTALL)
                    done = re.search(r"<done>(.*?)</done>", text, re.DOTALL)
                    if action:
                        command = action.group(1).strip()
                        step["action"] = command
                        process.stdin.write((json.dumps({"command": command, "timeout": 30}) + "\n").encode())
                        await process.stdin.drain()
                        line = await process.stdout.readline()
                        if not line:
                            raise RuntimeError("Execution container exited: " + (await process.stderr.read()).decode())
                        observation = json.loads(line)
                        step["observation"] = observation
                        stdout, stderr = observation.get("stdout", ""), observation.get("stderr", "")
                        if observation.get("exit_code", 0) != 0:
                            obs = f"{stdout}\n[stderr]: {stderr}\n[exit_code]: {observation['exit_code']}".strip()
                        else:
                            obs = stdout.strip() if stdout else "(empty output)"
                        messages.append({"role": "user", "content": f"<observation>\n{obs}\n</observation>"})
                    elif done:
                        record["termination"] = "done"
                        record["final"] = done.group(1).strip()
                        break
                    else:
                        messages.append({"role": "user", "content": "Please respond with either an <action> to execute or <done> if the task is complete."})
                    save(path, record)
                else:
                    record["termination"] = "turn_limit"
        except TimeoutError:
            record["termination"] = "timeout"
        except Exception as exc:
            record["termination"] = "error"
            record["error"] = f"{type(exc).__name__}: {exc}"
        record["elapsed_seconds"] = time.monotonic() - started
        # Stop execution before taking the final snapshot, including on timeout.
        await asyncio.to_thread(subprocess.run, ["docker", "rm", "-f", container], capture_output=True)
        container = None
        await process.wait()
        await asyncio.to_thread(client.evaluate_run, runId=run.runId, expectedOutput=json.loads(row["answer"]))
        result = await asyncio.to_thread(client.get_results_for_run, runId=run.runId)
        record["evaluation"] = result.model_dump(mode="json")
    except Exception as exc:
        record["error"] = f"{type(exc).__name__}: {exc}"
        record.setdefault("termination", "setup_error")
    finally:
        record["usage"] = llm.usage.snapshot().to_dict()
        record["cost_usd"] = cost(record["usage"])
        await llm.close()
        if container:
            await asyncio.to_thread(subprocess.run, ["docker", "rm", "-f", container], capture_output=True)
        if env:
            try:
                await asyncio.to_thread(client.delete_env, envId=env.environmentId)
            except Exception as exc:
                record["cleanup_error"] = str(exc)
        save(path, record)
    evaluation = record.get("evaluation", {})
    print(json.dumps({"test_id": row["test_id"], "termination": record.get("termination"),
                      "score": evaluation.get("score"), "passed": evaluation.get("passed"),
                      "cost_usd": record["cost_usd"], "error": record.get("error")}), flush=True)
    return record


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:18000")
    parser.add_argument("--model", default="us.anthropic.claude-sonnet-5")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--offset", type=int, default=0,
                        help="Skip this many Slack tasks before selecting tasks")
    parser.add_argument("--concurrency", type=int, default=10)
    parser.add_argument("--test-ids", nargs="+", help="Select explicit Slack IDs instead of offset/limit")
    args = parser.parse_args()
    if args.limit < 1 or args.offset < 0 or args.concurrency < 1:
        parser.error("limit/concurrency must be positive and offset nonnegative")
    rows = [json.loads(line) for line in (ROOT / "datasets/agent-diff-bench/all_numbered.jsonl").read_text().splitlines()]
    rows = [row for row in rows if row["service"] == "slack"]
    if args.test_ids:
        selected = set(args.test_ids)
        if selected - {row["test_id"] for row in rows}:
            parser.error("Unknown Slack test ID")
        rows = [row for row in rows if row["test_id"] in selected]
    else:
        rows = rows[args.offset:args.offset + args.limit]
    if not rows:
        parser.error("No Slack tasks selected")
    out = HERE / "results" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out.mkdir(parents=True)
    prompt = official_prompt()
    (out / "system_prompt.txt").write_text(prompt)
    config = {"model": args.model, "docs_mode": "relevant", "concurrency": min(args.concurrency, len(rows)),
              "offset": args.offset,
              "trials": 1, "turn_limit": 40, "timeout_seconds": 480,
              "max_output_tokens_per_call": 128000, "temperature": "provider_default",
              "effort": "provider_default", "prompt_caching": "explicit_5m",
              "rates_usd_per_million": RATES, "test_ids": [row["test_id"] for row in rows],
              "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
              "dataset_sha256": hashlib.sha256((ROOT / "datasets/agent-diff-bench/all_numbered.jsonl").read_bytes()).hexdigest()}
    save(out / "config.json", config)
    print(f"RESULTS_DIR={out}", flush=True)
    slots = asyncio.Semaphore(args.concurrency)

    async def worker(row):
        async with slots:
            return await episode(row, args, prompt, out)

    print(f"Running {len(rows)} tasks with {args.concurrency} concurrent workers", flush=True)
    results = await asyncio.gather(*(worker(row) for row in rows))
    tokens = {key: sum(result["usage"].get(key, 0) for result in results) for key in RATES}
    total = sum(len(json.loads(row["answer"])["assertions"]) for row in rows)
    passed_assertions = sum(result.get("evaluation", {}).get("score", {}).get("passed", 0) for result in results)
    summary = {"tasks": len(rows), "passed_tasks": sum(bool(result.get("evaluation", {}).get("passed")) for result in results),
               "passed_assertions": passed_assertions, "total_assertions": total,
               "assertion_weighted_score_percent": passed_assertions / total * 100,
               "tokens": tokens, "cost_usd": cost(tokens), "rates_usd_per_million": RATES,
               "results": [{key: result.get(key) for key in ["test_id", "test_name", "termination", "elapsed_seconds", "cost_usd", "error"]}
                           | {"passed": result.get("evaluation", {}).get("passed"), "score": result.get("evaluation", {}).get("score")}
                           for result in results]}
    save(out / "summary.json", summary)
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    asyncio.run(main())
