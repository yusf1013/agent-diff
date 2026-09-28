"""The launcher's solver backends: Purdue by default, or the self-hosted Qwen with its own key, endpoint and a limiter
shared across sessions. Offline: a probe module prints what the launcher set; no model calls."""
import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "grounding/runs/fact_coverage_02/launch.py"


def launch(tmp_path, **extra):
    """Run the probe through the launcher with a clean solver environment and a fake Purdue env file."""
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("PURDUE_", "SELFHOST_", "SOLVER_")) and k not in ("GENAI_API_KEY", "GROUNDING_ENV")}
    purdue_env = tmp_path / "purdue.env"
    purdue_env.write_text("PURDUE_GENAI_STUDIO_API_KEY=purdue-fake\n")
    env["GROUNDING_ENV"] = str(purdue_env)
    env.update(extra)
    p = subprocess.run([sys.executable, str(LAUNCH), "grounding.tests._launch_probe"], env=env, capture_output=True,
                       text=True)
    out = json.loads(p.stdout.strip().splitlines()[-1]) if p.returncode == 0 else None
    return p, out


def test_selfhost_uses_its_own_key_endpoint_model_and_shared_limiter(tmp_path):
    key = tmp_path / "api_key"
    key.write_text("selfhost-fake\n")
    p, out = launch(tmp_path, SOLVER_BACKEND="selfhost", SELFHOST_KEY_FILE=str(key), PROBE_EXPECT_KEY="selfhost-fake")
    assert p.returncode == 0, p.stderr
    assert out["key_matches"] is True  # the Purdue env file did not replace it
    assert out["PURDUE_BASE_URL"] == "http://127.0.0.1:18000/v1/chat/completions"
    assert out["SOLVER_MODEL"] == "qwen3.8-27b"
    assert out["PURDUE_RATE_LIMIT_FILE"] == "/tmp/qwen_selfhost_rate_limit.json"
    assert out["PURDUE_RATE_LIMIT_PER_MINUTE"] == "110"


def test_selfhost_limiter_settings_are_its_own(tmp_path):
    """A Purdue limiter exported in the shell does not leak into self-host runs."""
    key = tmp_path / "api_key"
    key.write_text("k\n")
    p, out = launch(tmp_path, SOLVER_BACKEND="selfhost", SELFHOST_KEY_FILE=str(key),
                    PURDUE_RATE_LIMIT_FILE="/tmp/purdue_genai_rate_limit.json", PURDUE_RATE_LIMIT_PER_MINUTE="19",
                    SELFHOST_RATE_LIMIT_PER_MINUTE="90")
    assert p.returncode == 0, p.stderr
    assert out["PURDUE_RATE_LIMIT_FILE"] == "/tmp/qwen_selfhost_rate_limit.json"
    assert out["PURDUE_RATE_LIMIT_PER_MINUTE"] == "90"


def test_purdue_stays_the_default(tmp_path):
    p, out = launch(tmp_path, PROBE_EXPECT_KEY="purdue-fake")
    assert p.returncode == 0, p.stderr
    assert out["SOLVER_BACKEND"] == "purdue"
    assert out["key_matches"] is True
    assert out["PURDUE_RATE_LIMIT_FILE"] == "/tmp/purdue_genai_rate_limit.json"
    assert out["PURDUE_RATE_LIMIT_PER_MINUTE"] == "19"
    assert out["PURDUE_BASE_URL"] is None and out["SOLVER_MODEL"] is None


def test_selfhost_refuses_a_disabled_limiter(tmp_path):
    key = tmp_path / "api_key"
    key.write_text("k\n")
    p, _ = launch(tmp_path, SOLVER_BACKEND="selfhost", SELFHOST_KEY_FILE=str(key), PURDUE_RATE_LIMIT_DISABLE="1")
    assert p.returncode != 0
    assert "PURDUE_RATE_LIMIT_DISABLE" in p.stderr


def test_unknown_backend_is_refused(tmp_path):
    p, _ = launch(tmp_path, SOLVER_BACKEND="openai")
    assert p.returncode != 0


def test_solve_waits_only_for_other_purdue_runs():
    from grounding.runs.autogen_02.kit import solve
    lines = ["123 python launch.py grounding.runs.fact_coverage_02.run --out /tmp/x", "456 bash"]
    assert solve.busy(lines, "purdue", backend=lambda pid: "purdue") is True
    assert solve.busy(lines, "purdue", backend=lambda pid: "selfhost") is False  # a self-host run does not block
    assert solve.busy(lines, "selfhost", backend=lambda pid: "purdue") is False  # a self-host run never waits
    assert solve.busy(["456 bash"], "purdue") is False
