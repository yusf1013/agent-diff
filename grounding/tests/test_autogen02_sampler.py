"""The Phase 3 sampler's statistics and decisions, on synthetic outcomes (no run data)."""
import json

from grounding.runs.autogen_02.kit import sampler


def _plan(tmp_path, cells, looks=(11, 18, 25)):
    doc = {"mode": "absence", "seed": 0, "looks": list(looks),
           "cells": {c: [{"unit": u, "domain": c.split("/")[0], "scenario": "S", "mode": "absence", "facts": ["F"],
                          "family": "F0", "position": i + 1, **({"source": "phase4"} if u.startswith("P4") else {})}
                         for i, u in enumerate(units)] for c, units in cells.items()}}
    (tmp_path / "plan_absence.json").write_text(json.dumps(doc))


def _verdicts(tmp_path, outcomes):
    for unit, trials in outcomes.items():
        for t, o in trials.items():
            d = tmp_path / "judged" / "run" / t / unit
            d.mkdir(parents=True)
            (d / "verdict.json").write_text(json.dumps({"outcome": o}))


def _decide(tmp_path, monkeypatch):
    monkeypatch.setattr(sampler, "review_exclusion", lambda u: None)
    return sampler.decide(tmp_path, "absence", [tmp_path / "judged"])


def test_bounds():
    assert round(sampler.lower_bound(11, 11), 3) == 0.811  # 11 of 11 shows a rate above 0.8 at 90%
    assert sampler.lower_bound(10, 10) < 0.8                # 10 of 10 cannot
    assert sampler.lower_bound(17, 18) > 0.8 and sampler.lower_bound(23, 25) > 0.8
    assert sampler.upper_bound(0, 11) < 0.8


def test_look1_decides_when_all_fail(tmp_path, monkeypatch):
    units = [f"U{i}" for i in range(20)]
    _plan(tmp_path, {"box/absence": units})
    _verdicts(tmp_path, {u: {"t1": "incorrect", "t2": "incorrect", "t3": "incorrect"} for u in units[:11]})
    d = _decide(tmp_path, monkeypatch)["box/absence"]
    assert d["look_reached"] == 11 and d["decision"] == "policy-level" and d["failures"] == 11


def test_one_pass_continues_and_extra_units_are_ignored(tmp_path, monkeypatch):
    units = [f"U{i}" for i in range(20)]
    _plan(tmp_path, {"box/absence": units})
    outcomes = {u: {"t1": "incorrect"} for u in units[:14]}
    outcomes["U3"] = {"t1": "correct_absent"}
    _verdicts(tmp_path, outcomes)
    d = _decide(tmp_path, monkeypatch)["box/absence"]
    # 14 units ran, but a decision uses exactly the units up to the last completed look (11)
    assert d["look_reached"] == 11 and d["draws"] == 11 and d["failures"] == 10
    assert d["decision"] == "continue to the next look"


def test_void_t1_uses_first_usable_later_trial(tmp_path, monkeypatch):
    units = [f"U{i}" for i in range(11)]
    _plan(tmp_path, {"box/absence": units})
    outcomes = {u: {"t1": "incorrect"} for u in units}
    outcomes["U0"] = {"t1": "not_established", "t2": "correct_absent", "t3": "incorrect"}
    outcomes["U1"] = {"t1": "artifact", "t2": "artifact", "t3": "artifact"}
    _verdicts(tmp_path, outcomes)
    d = _decide(tmp_path, monkeypatch)["box/absence"]
    assert d["draws"] == 10 and d["failures"] == 9  # U0 draws t2 (a pass); U1 has no usable trial


def test_small_cell_exhausted_and_extension_reported_apart(tmp_path, monkeypatch):
    phase3 = [f"U{i}" for i in range(10)]
    _plan(tmp_path, {"calendar/absence": phase3})
    _verdicts(tmp_path, {u: {"t1": "incorrect"} for u in phase3})
    d = _decide(tmp_path, monkeypatch)["calendar/absence"]
    assert d["decision"] == "undecided (units exhausted)" and d["look_reached"] == 10
    # amendment 5: Phase 4 units appended after the fixed order complete look 1
    _plan(tmp_path, {"calendar/absence": phase3 + ["P4a", "P4b"]})
    _verdicts(tmp_path, {"P4a": {"t1": "incorrect"}})
    d = _decide(tmp_path, monkeypatch)["calendar/absence"]
    assert d["look_reached"] == 11 and d["decision"] == "policy-level"
    assert d["phase3_only"]["draws"] == 10 and d["phase4_only"]["draws"] == 1
