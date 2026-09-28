"""OpenClaw on the self-hosted Qwen (roadmap step 6a): the per-attempt provider, the judge's record format, test
selection with the known defects, and the proxy's self-host guard. Offline: no model, database or OpenClaw calls."""
import json
from datetime import date

import pytest

from grounding.integrations.openclaw import purdue_proxy
from grounding.integrations.openclaw import runtime as oc
from grounding.runs.openclaw_eval_01 import run


def fake_config(workspace):
    return {
        "agents": {"defaults": {"model": {"primary": "openai/x"}, "workspace": "/nowhere", "maxConcurrent": 4},
                   "list": [{"id": oc.AGENT_ID, "workspace": str(workspace), "agentDir": "/nowhere",
                             "model": {"primary": "purdue/qwen3.8:27b", "fallbacks": []}}]},
        "models": {"providers": {"purdue": {
            "baseUrl": "http://127.0.0.1:18777/v1", "api": "openai-completions", "timeoutSeconds": 300,
            "apiKey": {"source": "env", "provider": "default", "id": "SECRET_NAME"},
            "models": [{"id": "qwen3.8:27b", "name": "Qwen", "reasoning": True, "contextWindow": 65536,
                        "maxTokens": 8192, "compat": {"supportsUsageInStreaming": True}}]}}},
        "tools": {}, "skills": {}, "plugins": {"entries": {}}, "commands": {}}


@pytest.fixture
def workspace(tmp_path):
    ws = tmp_path / "ws"
    (ws / "skills").mkdir(parents=True)
    (ws / "AGENTS.md").write_text("- When in doubt, ask.\n")
    return ws


def test_selfhost_provider_is_written_per_attempt(tmp_path, workspace, monkeypatch):
    monkeypatch.setattr(oc, "real_config", lambda: fake_config(workspace))
    config = oc.build_state_dir(tmp_path / "state", "tok123456", "linear", backend="selfhost")
    assert list(config["models"]["providers"]) == ["selfhost"]
    provider = config["models"]["providers"]["selfhost"]
    assert provider["baseUrl"] == f"http://127.0.0.1:{purdue_proxy.SELFHOST_PORT}/run/tok123456/v1"
    assert provider["apiKey"] == "local-proxy"
    assert provider["timeoutSeconds"] == oc.TIMEOUT_SECONDS  # one request may take the whole turn
    [model] = provider["models"]
    assert (model["id"], model["contextWindow"], model["maxTokens"]) == ("qwen3.8-27b", 131072, 8192)
    assert model["compat"] == {"supportsUsageInStreaming": True} and model["reasoning"] is True
    assert config["agents"]["list"][0]["model"] == {"primary": "selfhost/qwen3.8-27b", "fallbacks": []}
    written = json.loads((tmp_path / "state" / "openclaw.json").read_text())
    assert "SECRET_NAME" not in json.dumps(written)


def test_purdue_backend_is_unchanged(tmp_path, workspace, monkeypatch):
    monkeypatch.setattr(oc, "real_config", lambda: fake_config(workspace))
    config = oc.build_state_dir(tmp_path / "state", "tok123456", "box")
    provider = config["models"]["providers"]["purdue"]
    assert provider["baseUrl"] == f"http://127.0.0.1:{purdue_proxy.DEFAULT_PORT}/run/tok123456/v1"
    assert provider["models"][0]["contextWindow"] == 65536 and provider["timeoutSeconds"] == 300
    assert config["agents"]["list"][0]["model"]["primary"] == "purdue/qwen3.8:27b"


def test_judge_steps_take_the_toy_format():
    steps = [
        {"turn": 1, "tool": "read", "arguments": {"path": "skills/linear/SKILL.md"}, "action": "read {}",
         "text": "", "thinking": "I should read the skill.", "observation": {"stdout": "docs", "is_error": False}},
        {"turn": 1, "tool": "exec", "arguments": {"command": "curl x"}, "action": "curl x", "text": "Checking.",
         "thinking": "", "observation": {"stdout": "boom", "is_error": True}},
        {"turn": 1, "tool": None, "compaction": True},
        {"turn": 1, "tool": None, "text": "Done.", "thinking": "All good."},
    ]
    before = json.dumps(steps)
    out = oc.judge_steps(steps)
    assert json.dumps(steps) == before  # inputs unchanged
    assert [s["turn"] for s in out] == [1, 2, 3, 4] and [s["user_turn"] for s in out] == [1, 1, 1, 1]
    assert out[0]["response"]["content"] == [{"type": "text", "text": "<thinking>\nI should read the skill.\n</thinking>\n"}]
    assert out[0]["observation"] == {"status": "success", "stdout": "docs"}
    assert out[1]["observation"] == {"status": "error", "stdout": "boom"}
    assert out[1]["response"]["content"][0]["text"] == "Checking."
    assert out[2]["observation"]["stdout"] == "(OpenClaw compacted the conversation)"
    assert "observation" not in out[3] and out[3]["response"]["content"][0]["text"].endswith("Done.")


def test_the_bundle_reads_judge_steps():
    from grounding.runs.autogen_01.kit import bundle
    [step] = oc.judge_steps([{"turn": 1, "tool": "exec", "action": "curl y", "text": "", "thinking": "Look up y.",
                              "observation": {"stdout": "{}", "is_error": False}}])
    assert bundle._visible(step) == "Look up y."
    assert "#### Step 1" in bundle.trajectory({"steps": [step]}, [])


def test_scenario_of():
    assert run.scenario_of("P-G4-LIN-02-I11") == "G4-LIN-02"
    assert run.scenario_of("FP-AR-SLK-22-I11-I12") == "AR-SLK-22"
    assert run.scenario_of("AT-AP2-SLK-03-I13") == "AP2-SLK-03"
    assert run.scenario_of("UC-G4-BOX-04") == "G4-BOX-04"
    assert run.scenario_of("U-G4-CAL-05-CalendarListEntry_hidden") == "G4-CAL-05"
    assert run.scenario_of("G4-CAL-06") == "G4-CAL-06"


def write_case(root, domain, case_id):
    path = root / domain / f"{case_id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"case_id": case_id, "domain": domain, "case_sha256": "x"}))


def test_selection_applies_the_known_defects(tmp_path, monkeypatch):
    monkeypatch.setattr(run, "defect_actions", lambda: {
        "G4-LIN-02": "keep until 2026-09-30", "G4-CAL-06": "keep (rebuilt with the fixed seed)",
        "AT-G4-CAL-01-I15": "leave out", "P-G4-LIN-01-I13": "dropped by the derivation",
        "U-G4-CAL-05-CalendarListEntry_summary_override": "read before it runs"})
    for domain, case_id in [("linear", "G4-LIN-01"), ("linear", "P-G4-LIN-02-I11"), ("calendar", "P-G4-CAL-06-I11"),
                            ("calendar", "AT-G4-CAL-01-I15"), ("calendar", "AT-G4-CAL-01-I14"),
                            ("linear", "P-G4-LIN-01-I13"),
                            ("calendar", "U-G4-CAL-05-CalendarListEntry_summary_override")]:
        write_case(tmp_path, domain, case_id)
    items, left_out = run.select(tmp_path, None, set(), date(2026, 9, 28))
    ran = [c["case_id"] for c, _ in items]
    assert ran[0] == "P-G4-LIN-02-I11"  # date-limited tests go first
    assert set(ran) == {"P-G4-LIN-02-I11", "G4-LIN-01", "P-G4-CAL-06-I11", "AT-G4-CAL-01-I14"}
    assert set(left_out) == {"AT-G4-CAL-01-I15", "P-G4-LIN-01-I13", "U-G4-CAL-05-CalendarListEntry_summary_override"}
    items, left_out = run.select(tmp_path, None, {"U-G4-CAL-05-CalendarListEntry_summary_override"}, date(2026, 10, 1))
    ran = {c["case_id"] for c, _ in items}
    assert "P-G4-LIN-02-I11" not in ran and "past the date" in left_out["P-G4-LIN-02-I11"]
    assert "U-G4-CAL-05-CalendarListEntry_summary_override" in ran


def test_known_defects_have_a_frozen_suite_action():
    doc = json.loads(run.KNOWN_DEFECTS.read_text())
    entries = doc["curated"] + doc["from_the_witness_check"]
    assert all(e["frozen_suite"] for e in entries)
    actions = run.defect_actions()
    assert actions["G4-CAL-06"].startswith("keep") and actions["G4-BOX-05"] == "keep"
    assert run.date_limit(actions["G4-LIN-02"]) == date(2026, 9, 30)


def test_selfhost_proxy_needs_the_launcher():
    ok = {"SOLVER_BACKEND": "selfhost", "PURDUE_BASE_URL": "http://127.0.0.1:18000/v1/chat/completions"}
    assert purdue_proxy.selfhost_upstream(ok) == "http://127.0.0.1:18000/v1"
    with pytest.raises(SystemExit):
        purdue_proxy.selfhost_upstream({**ok, "SOLVER_BACKEND": "purdue"})
    with pytest.raises(SystemExit):
        purdue_proxy.selfhost_upstream({**ok, "PURDUE_RATE_LIMIT_DISABLE": "1"})
    with pytest.raises(SystemExit):
        purdue_proxy.selfhost_upstream({**ok, "PURDUE_BASE_URL": "https://genai.rcac.purdue.edu/api"})
