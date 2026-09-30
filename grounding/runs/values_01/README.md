# values_01: failures beyond fact discrimination

Session "values", started 2026-09-29 by the lead session ("RoadMap specialist"). Brief:
[briefs/values.md](../../protocols/briefs/values.md). No solver runs; the data is on disk.

## Status

- **2026-09-30, done:** the report is [report.md](report.md): the check definitions, the counts, the hand reading
  (123 labels on 99 executions, 30 recall reads), precision per check, recall, examples and the value-layer proposal.
  Three development cycles (log below). No model calls ($0).
- **For the lead:** AR-BOX-24 as a known-defects candidate (a test-side clock); five replica findings; a correction to
  report_01's RQ7 restore row. Waiting for the next assignment.

## The question

**How can we report, beside the grounding verdict, what else goes wrong when an agent acts: the values it writes,
what its final reply claims, and what else it changes?** Which of these checks can be mechanical, with what
precision, and what should a "value layer" beside the fact-discrimination verdict look like?

The PI's worry (notes of 2026-09-29, section C): "are we missing a lot of valuable information that's right in
front of us?" These errors are not grounding failures, so they never count as fact exposure. The question is what
they are, how often they happen, and how a test system can check them without hand reading.

**What a good check must do:**
- flag an execution only when the error is real (precision, estimated by reading flagged executions by hand);
- miss few real errors (recall, estimated against the blind labels that recorded such errors, and against my reads);
- stay independent of the grounding verdict (it reads the request, the state diff, the transcript and the reply);
- state what it cannot see.

**Kept apart:** grounding (which record), values (what was written to it), side effects (what else changed), and
the reply (what the agent said it did or found). Test validity, solver failures and judge errors stay apart too.

## Materials

- The 3,018 final executions: `report_01/numbers/concise.json` → `final_execution_keys` (1,695 regular, 732
  absence, 591 underspecified), under `openclaw_eval_01/runs/`. Each has the request (`case.json`), the state diff,
  the transcript and the final reply.
- What exists: report_01 RQ7 and [beyond.py](../report_01/kit/beyond.py) (literal values for six fields, and a
  classification of additional writes).
- Checks on my classifiers: the blind labels of openclaw_eval_01 (notes) and blind_review_01 (`secondary_issues`).

## Plan (cycles; the log below records each)

1. **Value specifications.** The cases carry no structured requested value: it lives in the request's wording.
   For each of the 100 scenarios I write the requested value of each written field by hand, with its comparator.
   (A mechanical extractor over the request was dropped: the proposal is to declare the value at construction.)
2. **Written values**, on every execution that writes: dates and times (with time zones), free text (exact,
   normalized, paraphrased, wrong), booleans and states, enumerations, and records named as values.
3. **Side effects:** from the diff (other rows, other fields, inserts) and from the transcript (write commands whose
   effect the final diff does not show: restored, failed, or no-ops).
4. **The reply against the diff:** success claimed with no matching write; absence claimed with a match present or
   after a write; a value stated that differs from what was written.
5. **Hand reading:** about 60 flagged executions, stratified over the checks, read before any judge verdict;
   precision per check. Every "wrote, then restored" case read with its trajectory.
6. **The proposal:** which checks are mechanical, which need a judge, how they are reported apart from exposure,
   and what they cost.

## Kit

Run from the repository root with the backend's Python, in this order (each writes one file in `data/`):

```bash
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.values   # values written, side effects in the diff
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.writes   # write commands in the transcript
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.reply    # the reply against the diff
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.times    # R5: stated times (Calendar)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.counts   # the counts
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.precision     # precision from eval/labels.jsonl
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.labels_check  # recall against the blind labels
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.view KEY --writes  # evidence for reading
```

`kit.sample` drew the reading sample once (seed 20260930, [eval/sample.json](eval/sample.json)); do not rerun it.

| File | What |
|---|---|
| [kit/common.py](kit/common.py) | The 3,018 executions (report_01's manifest, asserted), their grounding outcome for cross-tabulation only |
| [kit/specs.py](kit/specs.py) | The requested value of every written field, per scenario, written by hand from the requests |
| [kit/values.py](kit/values.py) | Values written against the specifications; other fields, records and tables changed; no-net-change rows |
| [kit/writes.py](kit/writes.py) | Write commands in the transcript: rejected, undone, or absent from the diff |
| [kit/reply.py](kit/reply.py) | What the reply claims against the diff (R1 to R4, R2c) |
| [kit/times.py](kit/times.py) | R5: times the reply states for the Calendar event written |
| [kit/counts.py](kit/counts.py) | The counts, with denominators, by service, form and grounding outcome, clustered by scenario |
| [kit/sample.py](kit/sample.py), [kit/view.py](kit/view.py) | The seeded reading draw; the evidence-only viewer (no verdicts) |
| [kit/precision.py](kit/precision.py), [kit/labels_check.py](kit/labels_check.py) | Precision from the labels; recall against the earlier blind labels |
| [eval/labels.jsonl](eval/labels.jsonl) | Every hand label (stratum, label, note, evidence) |

## Log

### Cycle 1 (2026-09-30): build the checks, run them, tune on the patterns' own errors

- **Built:** the value specifications (100 scenarios; a scenario's variants keep its value phrase, checked over the
  395 distinct requests), then the three check families. The grounding outcome is read only for the counts: for
  regular executions from the run's score (judge v2 or mechanical triage), for policy ones from the saved verdict.
  No judge note is read.
- **Reproduced:** 1,264 executions write something (report_01: 547 + 466 + 251), and 105 of 149 Linear priority
  writes are wrong (RQ7).
- **Learned about values:** literal values are copied exactly. Of 1,399 writes to a specified field, 1,275 hold the
  requested value; every tag, estimate, title, name, description, location, time zone, archive state and record
  named as a value is right (4 paraphrased descriptions need a reader). The errors are interpretations:
  Linear's priority scale (105 writes, 12 scenarios), the year of an undated due date (9 writes of 2027 for
  "July 15", a request that depends on the run date), the colour "red" (5 of 16 target writes took another
  palette entry), and a reaction the replica lacks ("done" for "check").
- **Learned about the replica:** its Slack emoji list has `check` but not `white_check_mark`, so `check` is the right
  value in this mock; its event palette's red is 11, while the calendar palette's red is 3 (an agent used the
  latter). Linear's `documentUpdate` and `attachmentUpdate` answered with an error while applying the change in 76
  executions (known, openclaw_eval_01).
- **Tuned (development, before the precision sample):** each change fixed a pattern error seen in the flags, not a
  case. Claims of a change: check marks in criteria tables, "should I set …?", passives describing the data ("the
  reaction was added by Omar") and "Done checking" were read as claims; R1 fell from 212 to 10 flags while claim
  recall on writing executions stayed at 1,231 of 1,240. "No match": local statements ("doesn't match", "there's no
  way") were read as absence claims; now only conclusion forms count. "No change": "left it alone" about another
  record, and "no changes were made to sharing", were read as global; now only global forms count. R4: the written
  issue and proposals ("want me to set … ?") are left to R3. Transcript ids: Slack reactions are matched on the
  message, `conversations.open` is a lookup, Linear identifiers (WEB-3) map to ids, and only a mutation's own `id`
  names its record. Value checks compare only rows of the change the request asks for (an opened DM is not a topic
  write); position matters only where the request says "at the end".

### The lead's steer (2026-09-30)

"AR-BOX-24's 'July 15' is a test-side date dependency the date check missed (like AR-SLK-21), not only an agent
error. Record it as a candidate for the known-defects list with a test-side clock, and keep those 20 writes apart in
the value counts so the PI can read the numbers either way. Same for anything else whose right answer depends on the
run date." Done: a `run_date` flag in the specifications and its own row in every count. No other value depends on
the run date for these runs (AP-LIN-04's and AP2-LIN-04's "October 20" would after 2026-10-20).

### The hand reading (2026-09-30)

- The draw (seeded, committed before reading): 61 precision reads over 14 checks, every restore candidate (16), and
  30 unflagged writers for recall. Read in an evidence-only viewer; no verdict or note was read.
- **Restore cases, read with their trajectories and the PI's three questions** (authorized? lasting effects? called
  for?): 8 restorations, 2 comments created then deleted, 5 no-ops, 1 parser false positive. RQ7's restore row
  counts no-ops as restorations; its "changed meeting time" is the replica storing API-written times in UTC.
- What the reading found beyond the flags: an undisclosed write-and-revert (P-AR-LIN-21-I16: "I left everything
  unchanged"), which no diff check sees; probe writes provoked by Linear's error-but-applied answers; Calendar writes
  that email attendees; a replica gap (Slack's history omits reactions); `attachmentLinkURL` resolving by URL.

### Cycle 2 (2026-09-30): fixes from the reading, two additions

- **Fixed:** Linear mutations with other name endings (`attachmentLinkURL`, `documentMove`) were missed; the Box
  body fallback read `unzip -d` as a POST (now only the curl invocation, and later not with `-G`, a regression this
  cycle introduced and caught); modal verbs ("may have been set") read as claims; markdown bold hid priority pairs;
  proposals ("Want me to set ... ? (Or ...)") and the requested action ("to High") were read as statements.
- **Added:** R2c (a write that did not stand, not disclosed), a prior-value check for written issues ("was Low"), and
  a count of Calendar writes that ask the service to email attendees.
- **Effect:** R1 10 -> 8 (two false positives gone), R4 40 -> 52 (15 new, all true; 3 false positives gone), R2c 8
  (6 true), T 16 -> 15 (the parser false positive gone; 4 more mutations seen).

### Cycle 3 (2026-09-30): R4 recall, R5

- The earlier labels showed R4 missing priority statements on lines without the word "priority" ("(currently
  High)"), in tables, and on lines that also hold a question. Now: question sentences are dropped, not lines; tables
  with a Priority column are read; "currently <name>" counts. R4 52 -> 60 (9 new, all true; 1 false positive gone).
- R5, a bounded probe for the brief's "times": stated time ranges for the Calendar event written, against its stored
  times in its own and the user's zone. 158 of 159 comparable replies match; the one mismatch is an hour off. The
  parser needed two fixes ("AM/PM" and "11:00-12:00 AM" read literally).
- Stopped here: the remaining misses are statements that name no issue or state other facts, which need a reader.
