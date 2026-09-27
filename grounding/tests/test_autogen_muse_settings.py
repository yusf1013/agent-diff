"""The Muse session settings that turn reminder subagents off for judge and reader calls (no Muse run)."""
import json

from grounding.runs.autogen_01.kit import agent


def test_judge_and_reader_run_without_reminders(tmp_path):
    for role in ("judge", "reader"):
        home = tmp_path / role
        assert agent._muse_settings(home, role) == "off"
        settings = json.loads((home / ".config" / "muse" / "settings.json").read_text())
        assert settings == {"schema_version": 1, "run": {"reminder_roster": {"agents": []}}}


def test_writer_keeps_muses_default(tmp_path):
    assert agent._muse_settings(tmp_path, "writer") == "default"
    assert not (tmp_path / ".config").exists()


def test_empty_role_list_restores_the_default(tmp_path, monkeypatch):
    monkeypatch.setattr(agent, "MUSE_NO_REMINDER_ROLES", set())
    assert agent._muse_settings(tmp_path, "judge") == "default"
    assert not (tmp_path / ".config").exists()
