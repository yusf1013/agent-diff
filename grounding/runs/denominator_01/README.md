# denominator_01: how the prescribed tests are filled

The reference is [protocols/denominator.md](../../protocols/denominator.md): 732 prescribed cases (213 regular
probes, 213 absence, 213 underspecified, 93 capability boundaries) without several-match. This study's kit measures
how the generation attempts on record fill them, item by item, under alternative one-attempt rules. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.denominator_01.kit.filling

| Path | What |
|---|---|
| [kit/filling.py](kit/filling.py) | Per item (a servable fact in each of three forms), which designated attempt fills it with a test valid under the rulings as they stand; four one-attempt rules; one test per item by an outcome-blind tie-break (the fact's own brief, then the earliest attempt); spares; the unfilled items. Writes `numbers/filling.json`. |
| [kit/suite_forms.py](kit/suite_forms.py) | The forms on record per (scenario, fact): packed probes, single-decoy probes, the AP/AP2 doubles, writer-added facts (the production view that the denominator replaces). |
| [kit/grouping_rule.py](kit/grouping_rule.py) | The Phase 4 grouping rule applied to all 213 servable facts (84 briefs), and the policy units deduplicated by brief. |
| `numbers/filling.json` | Per rule: scenarios, failed briefs, items filled per form and per service, production counts, spares, the designated test of every item, the unfilled items. |

**Inputs:** the catalog (`fact_coverage_01/catalog`), the unservable list (`autogen_02/inputs/briefs_phase4.excluded.json`),
the briefs of every generation run, the three suite indexes (`openclaw_eval_01/suite`, `completion_01/suite/cases`,
`regen_01/runs/full_01_cases`), the policy plans (`autogen_02/runs/phase3/plan_*.json`,
`openclaw_eval_01/runs/policy/plan_extension.json`, `regen_01/suite/units.json`) and the rulings
(`openclaw_eval_01/rulings.py` with `regen_01/rules.py`). The boundary numbers (93 faithful, 89 valid round-1
requests, one restored by a retry) are read from `boundary_02/space.json` and `boundary_auto_01/summary.json`.

**The rules** (`designated(rule)` in the kit): `final` = the frozen pipeline's attempt (Muse) for every brief;
`first` = the earliest attempt (Sonnet v1 for the hand-grouped briefs); `+retry` = plus one retry after an attempt
with no accepted scenario. A retry is the completion_01 regeneration of a Phase 4 brief or the regeneration study's
second draw. The PI's choice between the rules was open on 2026-10-01.

**Result (2026-10-01):** rule `final+retry` fills 195 + 187 + 161 + 90 = 633 of 732; `first+retry` 643; every
attempt on record together 667. The log is in [protocols/overnight_2026-09-30.md](../../protocols/overnight_2026-09-30.md).
