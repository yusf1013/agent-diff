# completion_01: the remaining briefs (roadmap 6b)

Roadmap step 6b ([roadmap](../../protocols/roadmap.md)): generate the scenarios the servable space still lacks, so
that OpenClaw's evaluation ([openclaw_eval_01](../openclaw_eval_01/README.md)) covers it whole.

| Path | What |
|---|---|
| [inputs/briefs_6b.json](inputs/briefs_6b.json) | 26 briefs, 74 facts: the servable facts no evaluated scenario covers (autogen_02's count: 54 + 8 + 12) |
| [generate.py](generate.py) | Phase 4's generator, unchanged, on these briefs |
| `runs/gen_01/` | The generation run |

## The briefs

- **19 Phase 4 briefs never generated** (orders 33 to 51; the run was cut to 32 for time): Box 6, Calendar 1,
  Linear 12. 54 facts.
- **3 Phase 4 briefs with no accepted scenario,** generated again: G4-CAL-08 (the generation failed), G4-BOX-02 and
  G4-LIN-03 (rejected). 8 facts. Phase 4's records of the first attempts stay in autogen_02.
- **4 new briefs** (G4-BOX-15, G4-CAL-10, G4-LIN-21, G4-SLK-09) for the 12 facts of autogen_01's development briefs
  (DV-BOX-01, DV-CAL-01, DV-LIN-01, DV-SLK-01). Their scenarios were accepted in the second development round
  (`autogen_01/runs/gen_dev_02`), so the replicas serve these facts; they were used to develop the method and so
  never counted as coverage. Phase 4 drew only facts no autogen_01 brief had used, which left these 12 out.

## How the suite is built

As 6a's after the discussion of 2026-09-28: the generator is unchanged and the writer is asked about neither ids nor
dates. When the suite is built, every test gets opaque ids (`autogen_01/kit/opaque_ids.py`, with the same checks as
`openclaw_eval_01/opaque_suite.py`) and a test-side clock: the day its scenario was written, or a later day if its
data has an event after it (Calendar keeps its 2018 day). Every accepted scenario gets my validity review before any
run, and every Muse-written policy variant a manual read.
