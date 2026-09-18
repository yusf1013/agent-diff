# Remaining-domain analysis preflight

Protocol: [v1](card_extraction.md). Baseline commit: `ae6d3a5`.
This is an evidence/readiness inventory, not a completed semantic annotation or coverage audit.

## Scope

The source is `datasets/agent-diff-bench/all_numbered.jsonl`. All 165 remaining entries parse, contain nonempty assertion specifications, and reference present seed files. Preserve the file's numbered order within each domain.

| Domain | Tests | Test IDs | Numbered entries | Seed | Assertions | Local API extract entries |
|---|---:|---|---|---|---:|---:|
| Box | 48 | box_116–box_163 | 60–107 | box_default | 92 | 26 |
| Linear | 57 | linear_0–linear_56 | 108–164 | linear_expanded | 165 | 19 |
| Calendar | 60 | calendar_164–calendar_223 | 165–224 | calendar_default | 274 | 37 |

Each domain uses one actor throughout: Box `27512847635`, Linear `2790a7ee-fde0-4537-9588-e233aa5a68d1`, Calendar `user_agent`. These are context supplied by the entries, not independent lookup obligations unless requested subjects require them.

## Located evidence

- Box seed: `examples/box/seeds/box_default.json`; API extract: `examples/box/testsuites/box_docs/box_api_full_docs.json`.
- Linear seed: `examples/linear/seeds/linear_expanded.json`; API extract: `examples/linear/testsuites/linear_docs/linear_api_full_docs.json`; additional declarative API definition: `backend/src/services/linear/api/schema/Linear-API.graphql`.
- Calendar seed: `examples/calendar/seeds/calendar_default.json`; API extract: `examples/calendar/testsuites/calendar_docs/calendar_api_full_docs.json`.

All three seed JSON files are byte-identical to their corresponding `backend/seeds/` copies. All assertion entity names occur in the corresponding seed, including initially empty entity collections. This check does not establish every predicate's meaning or coverage label.

The Box seed references 131 file contents through `box_file_versions.local_path`. They initially existed as Git LFS pointers. A scoped LFS pull materialized all 131 referenced files (59,684,552 bytes total). These contents are initial-state evidence. Seeded model-evaluation result files, if required by a Box task, are treated only as task documents, never as evidence of solving-agent performance.

Two materialized files disagree with their seed size/hash metadata:

| File ID | Filename | Seed size | Actual bytes |
|---|---|---:|---:|
| 8847291035 | phylosophy of sciance.md | 2048 | 883 |
| 9958302146 | reserch ethics guidlines.txt | 1536 | 969 |

Their actual SHA-1 hashes also differ from the seed's values. Preserve the seed's declared metadata and file contents as separate evidence; do not repair the benchmark or substitute filesystem byte counts for API-visible seed metadata. These files appear in the typo-renaming task `box_139`; the observed discrepancy does not prevent identifying them by name. Raise any later material conflict that cannot be settled under v1.

## API evidence gaps addressed at preflight

The Box extract omits comment/task update and deletion methods named by some entries. Official documentation is available for [updating comments](https://developer.box.com/reference/put-comments-id), [removing comments](https://developer.box.com/reference/delete-comments-id), [updating tasks](https://developer.box.com/reference/put-tasks-id), and [removing tasks](https://developer.box.com/reference/delete-tasks-id). Consulted 2026-09-08.

The Linear extract omits `issueRelationDelete`; the local declarative GraphQL schema includes it. Its schema also provides response/entity definitions. Reading that schema is API-definition evidence; resolvers and database models remain excluded.

Calendar has a broader local extract. The official [recurring-events guide](https://developers.google.com/workspace/calendar/api/guides/recurringevents), consulted 2026-09-08, is available for interpreting recurring series and instances. Additional official resource/method pages can be included as needed, with their locations and consultation dates recorded in each domain's source manifest. These sources establish documented interfaces, not implementation parity.

## Matters requiring careful annotation

- Calendar availability, timezone conversion, recurring instances, and seed-conditioned actions require explicit selection/computation explanations. Newly created series and their subsequently addressed instances are task outputs, not automatically new initial-state obligations.
- Do not use the analysis session's current date to interpret benchmark-relative dates. `calendar_164` says “this Saturday” without an explicit task clock in its metadata; assertion dates are supporting evidence, not a supplied solver clock. Preserve any resulting interpretation limits. By contrast, `calendar_172` explicitly defines its “tomorrow” date in the prompt.
- Box duplicate selection, content-derived values, and size comparisons require keeping metadata, content, and identifying versus computation roles distinct.
- Linear status/label subjects, scoped team membership counts, and issue dependencies require distinguishing independently described subjects from qualifying relationships and new outputs.
- Missing or uninterpretable assertion specifications must be raised to the user, not labeled `no`. No such unresolved case has been identified at preflight; detailed predicate review remains part of the full analysis.

## Planned deliverables and readiness

Create `grounding/box_analysis/`, `grounding/linear_analysis/`, and `grounding/calendar_analysis/`, each with the same core deliverables as `slack_analysis/`: maintained annotations, per-test tables, locked cards, machine-readable cards and metrics, source manifest/map, methodology notes, and reproducible structural/render checks. Include a review of partial-coverage explanations against the final-outcome standard. Reuse conventions, not Slack-specific test counts, entity keys, or calibration constants.

No credentials, running service, live database, implementation access, or additional user-provided files are currently needed to begin the full annotation. This is not a guarantee that detailed semantic review will raise no questions. The nearby conceptual ER documents are excluded as evidence.
