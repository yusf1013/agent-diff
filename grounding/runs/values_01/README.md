# values_01: failures beyond fact discrimination

Session "values", started 2026-09-29 by the lead session ("RoadMap specialist"). Brief:
[briefs/values.md](../../protocols/briefs/values.md). No solver runs; the data is on disk.

## Status

- **2026-09-30, cycle 1 done:** the checks are built and run on all 3,018 executions ([kit/](kit/), outputs in
  `data/`). Counts in `data/counts.json`. **Next:** the hand-read precision sample, the restore cases, the recall
  checks against the blind labels, then the report.
- Nothing is blocked. No model calls so far ($0).

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
   A mechanical extractor over the request is measured against these specifications.
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
python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.counts   # the counts
```

| File | What |
|---|---|
| [kit/common.py](kit/common.py) | The 3,018 executions (report_01's manifest, asserted), their grounding outcome for cross-tabulation only |
| [kit/specs.py](kit/specs.py) | The requested value of every written field, per scenario, written by hand from the requests |
| [kit/values.py](kit/values.py) | Values written against the specifications; other fields, records and tables changed; no-net-change rows |
| [kit/writes.py](kit/writes.py) | Write commands in the transcript: rejected, undone, or absent from the diff |
| [kit/reply.py](kit/reply.py) | What the reply claims against the diff (R1 to R4) |
| [kit/counts.py](kit/counts.py) | The counts, with denominators, by service, form and grounding outcome, clustered by scenario |

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
