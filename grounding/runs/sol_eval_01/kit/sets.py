"""The Sol round's sets: each one's kind, suite index and cases folder, for the kit's scripts. Importing this module
also imports regen_01's rulings wrapper (regen_01/rules.py), so the rulings recognize the regenerated half's near
misses under their opaque ids; it adds only that half's id folder and duplicate units, so the first half's numbers
are unchanged (kit/score.py and kit/policy.py `regress` check it).

- The Muse-written half (the lead's runs, 2026-09-30 00:00): regular_p4 and regular_6b (cases copied here by
  kit/prepare.py), policy_absence and policy_underspecified.
- The regenerated half (this session's runs, kit/run_regen.py): regen_full_01, regen_absence_01 and
  regen_underspecified_01, on regen_01's cases folders unchanged.
"""
from __future__ import annotations

from pathlib import Path

from grounding.runs.regen_01 import rules as _regen_rules  # noqa: F401  (before anything reads the rulings)

STUDY = Path(__file__).resolve().parents[1]
REGEN = STUDY.parent / "regen_01"

SETS = {
    "regular_p4": {"kind": "regular", "half": "muse", "suite": STUDY / "cases" / "regular_p4" / "suite.json"},
    "regular_6b": {"kind": "regular", "half": "muse", "suite": STUDY / "cases" / "regular_6b" / "suite.json"},
    "policy_absence": {"kind": "absence", "half": "muse", "cases": STUDY / "cases" / "policy_absence"},
    "policy_underspecified": {"kind": "underspecified", "half": "muse",
                              "cases": STUDY / "cases" / "policy_underspecified"},
    "regen_full_01": {"kind": "regular", "half": "regen", "suite": REGEN / "runs" / "full_01_cases" / "suite.json",
                      "cases": REGEN / "runs" / "full_01_cases", "qwen_run": REGEN / "runs" / "full_01"},
    "regen_absence_01": {"kind": "absence", "half": "regen", "cases": REGEN / "runs" / "absence_01_cases",
                         "qwen_run": REGEN / "runs" / "absence_01"},
    "regen_underspecified_01": {"kind": "underspecified", "half": "regen",
                                "cases": REGEN / "runs" / "underspecified_01_cases",
                                "qwen_run": REGEN / "runs" / "underspecified_01"},
}


def kind(name: str) -> str:
    return SETS[name]["kind"]


def of_half(half: str) -> list[str]:
    return [name for name, s in SETS.items() if s["half"] == half]
