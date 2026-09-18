# Box outcome-coverage review

All coverage annotations are judged against final state/output, not retrieval traces. This table collects every partial label and its concrete missing constraint. Predicate examples are not full benchmark executions. See report.md for all assertions and semantic notes.

| Test / obligation | Partial-coverage reason |
|---|---|
| [box_127 / 2](report.md#box_127) | A1 only requires a nonempty description on investments. A wrong nonempty count such as 999 meets the checked value condition. |
| [box_128 / 1](report.md#box_128) | Hubs_Found_999 meets the prefix predicate; the required seeded count 3 is not constrained. |
| [box_129 / 1](report.md#box_129) | A2 locates changed FOMC files but gives no explicit four-file requirement or linkage to the newly created FOMC_Reports folder. A proper subset is not ruled out by the stated predicates. |
| [box_133 / 2](report.md#box_133) | The renamed folder correctly checks both first-row values, but the requested description can omit title=Food while containing CPIM.SE901. This is missing final content, not missing source IDs. |
| [box_135 / 2](report.md#box_135) | The output filename binds reference and period, but the uploaded content and Data_value=2771 are not checked. |
| [box_150 / 1](report.md#box_150) | A2 constrains item_name containing fomc and at least four hub-item rows, but does not require the four distinct seeded file IDs or a common destination hub. Repeated associations across hubs are not ruled out by the predicates. |
| [box_151 / 1](report.md#box_151) | A1 constrains PDF extension and tag but neither the investments scope nor all five intended records; a different PDF or subset is not excluded. |
| [box_152 / 1](report.md#box_152) | A1 identifies changed fomc-named files but lacks an explicit four-file requirement and only checks FOMC in the description, not the requested filename-derived dates. |
