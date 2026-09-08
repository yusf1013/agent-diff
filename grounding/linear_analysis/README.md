# Linear grounding-obligation measurements

All 57 Linear entries (`linear_0`–`linear_56`, numbered 108–164) are annotated under [protocol v1](../GROUNDING_OBLIGATIONS_ONBOARDING.md). Read [the tables](report.md), [cards](cards.md), [metrics](metrics.json), and [partial-coverage review](coverage_audit.md). These measure the benchmark, not solving agents.

## Evidence and counting

Allowed sources are the full test entry, `linear_expanded`, the local API extract, and the declarative `Linear-API.graphql` API schema. The latter supplies response/entity definitions and the relation-deletion mutation omitted by the extract. No resolver, model, evaluator, runtime, or external ER model was inspected. [sources.json](sources.json) records source hashes; [source_map.md](source_map.md) maps attributes to the interface.

Each test starts from the same seed independently. `linear_12` cannot inherit Bugs from `linear_11`; Bugs is absent. Explicitly created labels, states, teams, comments, and issues are new outputs, including new sub-issues and relation endpoints. Qualifying assignees/authors do not automatically create person obligations. Literal names in comments are not lookup requests. Existing named workflow states and labels are referents; priority values and relation-type enums are prompt constants, not entities.

Repeated entity use is counted once. Different requested sets can overlap: the Szymon packet evidence includes the failed packets, while the failed-packet action subset has its own narrower requested boundary. The Engineering benchmark/destination in `linear_54` is counted once despite its several uses. Source and destination coverage follow the same rules as Slack: a final reference can fully cover identity without certifying the rest of the operation.

## Findings requiring explicit boundaries

- `linear_29`: the two Product descriptions concern the same trace-analysis work. PROD-2 was created January 15, after PROD-1 on January 1. Product has no Duplicate state; its creation is a new output, and the missing initial status is recorded as absent.
- `linear_32`: John has two priority-Urgent issues, ENG-3 and PROD-2. Only ENG-3's reassignment is required by the assertions; the set is partially covered. The instruction to leave non-urgent work unchanged constrains the selection boundary, not a new independently acted-on subject.
- `linear_33`: the asserted Product In Review ID is absent from the seed, which supplies only Product Todo. The requested state is absent; an answer-only ID does not establish its semantic identity.
- `linear_35`: Artem, Engineer Five, Derek, and Mila tie at zero assigned issues among Engineering members. The choose-one referent set lists all four. Requiring Artem selects a valid eligible outcome; accepting every alternative is not required for identity coverage.
- `linear_41`: Yuto has 3/4 sprouted packets and three sprouted varieties. Szymon has 1/3 sprouted; his two failed packets are the action subset. Both applicable conditional branches are retained. New Seed Guardian is not an initial label.
- `linear_43`: Marcus alone is ambiguous between two users. The mutation assertion selects Marcus Aurelius, the adopted permissive boundary. The team-specific Mobile status handle also constrains the team contribution; this is a derived reference, not a requirement to inspect a trajectory.
- `linear_48`: Master Edit Lock directly blocks four issues; the phase-two color issue is indirect. The assertion's `directly blocks 4` fragment does not bind the subject to Master Edit Lock. Its partial label concerns final factual attribution, not missing source IDs.
- `linear_54`: all 19 teams are included. The maximum membership count is 7; 18 teams are understaffed, and the total gap is 112. The assertion demands 28 and only three staffing-issue destinations. Preserve the seed/assertion discrepancy rather than excluding twelve zero-member teams to make 28 fit.
- `linear_55`: the seeded count is three flagged comments on two distinct issues. The count fragment is checked, the requested comment-ID list is not, and both warning destinations are checked individually.

There are no pending assertion-specification questions. Some predicates concern changed rows for objects the prompt first creates; the analysis records their stated referent constraints without certifying evaluator behavior or execution feasibility.

## Maintenance and checks

`analysis.json` is the editable annotation source; `config.json` supplies the domain adapter. The shared renderer generates the same core artifacts as Slack and collects every partial explanation into `coverage_audit.md`.

```bash
python grounding/linear_analysis/build.py
python grounding/linear_analysis/build.py --check
```

Structural checks cover test completeness, exact card keys, seed identities, documented attribute names, assertion indices, aggregate reconciliation, and artifact freshness. Additional seed inspection checked priority/assignee populations, scoped workflow states, timestamps, team membership counts, tied assignment minima, and directed dependency counts. These checks are not an independently protected proof checker or semantic certification.
