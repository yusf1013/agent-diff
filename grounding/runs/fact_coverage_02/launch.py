"""Run a module with the environment these runs used (keys are read from files, never stored or printed).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.fact_coverage_02.run --out ... [args]
    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py ...

The solver backend (`SOLVER_BACKEND`):
- `purdue` (the default): Purdue GenAI Studio. GENAI_API_KEY comes from PURDUE_GENAI_STUDIO_API_KEY in grounding/.env
  (or $GROUNDING_ENV), with Purdue's shared rate limiter (19 requests a minute, one file for every process).
- `selfhost`: the self-hosted Qwen3.8-27B (~/qwen-selfhost, served as `qwen3.8-27b`). GENAI_API_KEY comes from
  ~/qwen-selfhost/secrets/api_key (or $SELFHOST_KEY_FILE); grounding/.env is not read, so the Purdue key cannot
  replace it. Every session on this machine shares one limiter for it (its own file; 110 requests a minute, below the
  server's measured best of about 130, or $SELFHOST_RATE_LIMIT_PER_MINUTE). Keep at most about 48 trials in flight per
  session. Time spent waiting on that limiter stays off each trial's time budget (the agent clock); time queued inside
  the server would not, which is why the limiter is shared rather than disabled.

Also sets DATABASE_URL (unless already set) and PYTHONPATH (the repository, the SDK and the Purdue client in
$BEDROCK_LLM_SRC), then runs the module from the repository root.
"""
import os
import runpy
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
PATHS = [str(REPO / "sdk/agent-diff-python"), str(REPO),
         os.environ.get("BEDROCK_LLM_SRC", str(Path.home() / "PyProj/bedrock-llm/src"))]

backend = os.environ.setdefault("SOLVER_BACKEND", "purdue")
if backend == "selfhost":
    if os.environ.get("PURDUE_RATE_LIMIT_DISABLE") == "1":
        raise SystemExit("SOLVER_BACKEND=selfhost shares one rate limiter with the other sessions on this machine; "
                         "unset PURDUE_RATE_LIMIT_DISABLE")
    key_file = Path(os.environ.get("SELFHOST_KEY_FILE", Path.home() / "qwen-selfhost/secrets/api_key"))
    os.environ["GENAI_API_KEY"] = key_file.read_text().strip()
    os.environ["PURDUE_BASE_URL"] = os.environ.get("SELFHOST_BASE_URL",
                                                   "http://127.0.0.1:18000/v1/chat/completions")
    os.environ["PURDUE_RATE_LIMIT_FILE"] = os.environ.get("SELFHOST_RATE_LIMIT_FILE",
                                                          "/tmp/qwen_selfhost_rate_limit.json")
    os.environ["PURDUE_RATE_LIMIT_PER_MINUTE"] = os.environ.get("SELFHOST_RATE_LIMIT_PER_MINUTE", "110")
    os.environ.setdefault("SOLVER_MODEL", "qwen3.8-27b")
elif backend == "purdue":
    env_file = Path(os.environ.get("GROUNDING_ENV", REPO / "grounding/.env"))
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("PURDUE_GENAI_STUDIO_API_KEY="):
                os.environ["GENAI_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
    os.environ.setdefault("PURDUE_RATE_LIMIT_FILE", "/tmp/purdue_genai_rate_limit.json")
    os.environ.setdefault("PURDUE_RATE_LIMIT_PER_MINUTE", "19")
else:
    raise SystemExit(f"SOLVER_BACKEND must be purdue or selfhost, not {backend!r}")
os.environ.setdefault("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
os.environ["PYTHONPATH"] = ":".join(PATHS)
for path in reversed(PATHS):
    sys.path.insert(0, path)
os.chdir(REPO)

module = sys.argv[1]
sys.argv = [module] + sys.argv[2:]
runpy.run_module(module, run_name="__main__", alter_sys=True)
