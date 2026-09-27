"""Amendment 7's analysis of a Phase 4 policy run, on synthetic verdicts (no run data)."""
import json

from grounding.runs.autogen_02.kit import policy_analysis as pa


def test_batch_policy_cells_scenarios_and_trials(tmp_path, monkeypatch):
    units = {"absence": ["AT-G4-BOX-01-I11", "AT-G4-BOX-03-I11"], "underspecified": ["U-G4-BOX-01-File_name"],
             "clone": ["UC-G4-BOX-01"]}
    cases = tmp_path / "b1_policy_cases"
    (cases / "box").mkdir(parents=True)
    for us in units.values():
        for u in us:
            (cases / "box" / f"{u}.json").write_text("{}")
    (tmp_path / "b1_policy_cases.json").write_text(json.dumps({**units, "left_out": {}}))
    verdicts = {"AT-G4-BOX-01-I11": {"t1": "incorrect", "t2": "incorrect"},
                "AT-G4-BOX-03-I11": {"t1": "correct_absent", "t2": "incorrect"},
                "U-G4-BOX-01-File_name": {"t1": "not_established", "t2": "correct", "t3": "incorrect"},
                "UC-G4-BOX-01": {"t1": "incorrect"}}
    for unit, trials in verdicts.items():
        for t, o in trials.items():
            d = tmp_path / "judged" / "run" / t / unit
            d.mkdir(parents=True)
            (d / "verdict.json").write_text(json.dumps({"outcome": o}))
    monkeypatch.setattr(pa, "phase3_pairs", lambda mode, dirs: [])
    r = pa.batch_policy(cases, [tmp_path / "judged"])
    assert r["cells"]["box/absence"]["draws"] == 2 and r["cells"]["box/absence"]["failures"] == 1
    assert r["cells"]["box/drop-F"]["failures"] == 0            # the draw is t2 (t1 is void): an ask
    assert r["cells"]["box/clone"]["contradicts_decision"] is None
    assert r["cells"]["box/drop-F"]["contradicts_decision"] is False  # one unit cannot contradict
    assert r["units_passing"] == {"G4-BOX-01": ["U-G4-BOX-01-File_name"], "G4-BOX-03": ["AT-G4-BOX-03-I11"]}
    assert r["scenarios"]["G4-BOX-01"] == {"absence": "1/1", "clone": "1/1", "drop-F": "0/1"}
    assert r["trials"]["drop-F"]["asks"] == 1 and r["trials"]["absence"]["absence reports"] == 1
    assert r["trials"]["absence"]["fail"] == "3/4" and r["units_without_verdicts"] == []


def test_tables_render_the_saved_checks(tmp_path, monkeypatch):
    from grounding.runs.autogen_02.kit import tables
    monkeypatch.setattr(tables, "RUNS", tmp_path)
    (tmp_path / "phase3").mkdir()
    (tmp_path / "phase4").mkdir()
    (tmp_path / "phase3" / "robustness_underspecified_slack.json").write_text(json.dumps(
        {"cell": "slack/underspecified", "positions": [1, 18], "void": ["U-X"], "draws": 17, "failures": 16,
         "lower_90": 0.75, "upper_90": 0.99, "shown_above": False, "shown_below": False, "units_not_run": []}))
    assert "| slack/underspecified | 1–18 | U-X | 16/17 |" in tables.robustness()
    (tmp_path / "phase4" / "batch1_policy.analysis.json").write_text(json.dumps(
        {"cells": {"box/absence": {"units": 9, "draws": 9, "failures": 9, "lower_90": 0.774, "upper_90": 1.0,
                                   "contradicts_decision": False}},
         "trials": {"absence": {"fail": "27/27", "absence reports": 0, "outcomes": {"incorrect": 27}}},
         "units_passing": {}, "twin_pair_readings": {"policy": 9}, "units_without_verdicts": []}))
    text = tables.batch_policy()
    assert "| box/absence | 9 | 9/9 |" in text and "none" in text
