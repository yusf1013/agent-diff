# Linear outcome-coverage review

All coverage annotations are judged against final state/output, not retrieval traces. This table collects every partial label and its concrete missing constraint. Predicate examples are not full benchmark executions. See report.md for all assertions and semantic notes.

| Test / obligation | Partial-coverage reason |
|---|---|
| [linear_32 / 1](report.md#linear_32) | A1 requires ENG-3 reassignment, but also-urgent PROD-2 is unchecked. A2 protects ENG-1, not the completeness of urgent reassignment. |
| [linear_34 / 1](report.md#linear_34) | The description need only contain agent. It can omit the 500-error spike, timing, and analysis reported by the source comments. |
| [linear_41 / 1](report.md#linear_41) | The label name reflects the positive branch, but four generic label associations do not require the four Yuto packets. |
| [linear_41 / 3](report.md#linear_41) | The two failed-packet changes constrain the action subset, but GERMINATION_AUDIT: alone does not check the requested 1/3 rate and counts. |
| [linear_48 / 3](report.md#linear_48) | The number 4 is bound to directly blocks, but its subject need not be Master Edit Lock. A statement that an unrelated issue directly blocks 4 meets A5; A4 adds only an audit marker. |
| [linear_54 / 1](report.md#linear_54) | Some named counts are correct, but the all-team report is incomplete and A10 demands total 28 while the supplied seed yields 112. Separate comments can carry the fragments; no complete correct population report is enforced. |
| [linear_54 / 3](report.md#linear_54) | Only Product, Design, and QA staffing issues are required; fifteen other understaffed teams are omitted, and no per-issue numeric gap is checked. |
| [linear_55 / 1](report.md#linear_55) | Found 3 comments checks the count fragment, but the requested three comment IDs are completely unchecked. |
