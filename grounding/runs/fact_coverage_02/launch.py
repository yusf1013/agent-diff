"""Run a module with the environment these runs used (the Purdue key is read from grounding/.env, never stored).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.fact_coverage_02.run --out ... [args]

Sets GENAI_API_KEY from PURDUE_GENAI_STUDIO_API_KEY in grounding/.env (or $GROUNDING_ENV), the shared Purdue
rate limiter (19 requests per minute, one file for every process), DATABASE_URL (unless already set) and
PYTHONPATH (the repository, the SDK and the Purdue client in $BEDROCK_LLM_SRC), then runs the module from the
repository root.
"""
import os
import runpy
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
PATHS = [str(REPO / "sdk/agent-diff-python"), str(REPO),
         os.environ.get("BEDROCK_LLM_SRC", str(Path.home() / "PyProj/bedrock-llm/src"))]

env_file = Path(os.environ.get("GROUNDING_ENV", REPO / "grounding/.env"))
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.startswith("PURDUE_GENAI_STUDIO_API_KEY="):
            os.environ["GENAI_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
os.environ.setdefault("PURDUE_RATE_LIMIT_FILE", "/tmp/purdue_genai_rate_limit.json")
os.environ.setdefault("PURDUE_RATE_LIMIT_PER_MINUTE", "19")
os.environ.setdefault("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
os.environ["PYTHONPATH"] = ":".join(PATHS)
for path in reversed(PATHS):
    sys.path.insert(0, path)
os.chdir(REPO)

module = sys.argv[1]
sys.argv = [module] + sys.argv[2:]
runpy.run_module(module, run_name="__main__", alter_sys=True)
