# judge_qwen_01: judge v2 on the self-hosted Qwen instead of Muse

Session "judge_qwen", started by the lead ("RoadMap specialist") on 2026-09-30 from the brief
[briefs/judge_qwen.md](../../protocols/briefs/judge_qwen.md).

## Status

- **2026-09-30 01:15 EDT.** **Labelled replay done: Qwen meets the bar.** On the 442 executions with a resolved
  label, Qwen calls no labelled failure a nonfailure and one a void (the bar allows 2 misses), and its precision
  is 191/196 (97.4%), against Muse's 192/196 (98.0%): 0.5 points apart, inside the 3 allowed. Qwen and Muse agree
  on 440 of the 443 verdicts and on the exposed facts of all 196 executions both call failures. I adjudicated the 3
  disagreements blind: Muse is right on 2, Qwen on 1. The decision is the lead's.
- **2026-09-30 02:45 EDT. Paused at the lead's request** (the self-host is needed for two sessions' solver runs;
  the lead will say when it is free, probably in the morning). The replay of the other 1,696 judged executions
  stopped at 02:39 EDT after **680 of them** (`sets/rest_done_at_pause.json`); the 16 calls in flight left only
  their request files and are redone on resume. The queued second labelled pass was cancelled before it started.
- **The 680, so far:** Qwen and Muse give the same outcome group on 667 (98.1%). I adjudicated all 15
  disagreements blind. Of the 13 that differ in outcome group, Qwen is right on 9 and Muse on 4; of the 2 that
  differ only within a group, Qwen is right on the facts of one and Muse on the exact outcome of the other. Qwen's
  wins are runs that ended without an answer, which Muse credited with their unsent conclusion; all but one of them
  change no score. Muse's wins are real failures that Qwen called artifacts. See "The full replay, paused".
- **On resume:** the other 1,016 (`replay run --set all`, which skips what is done), their disagreements labelled
  blind in a new round, then the headline numbers (Table 7 and the eight policy decisions) recomputed with Qwen's
  verdicts ([headline.py](headline.py), already checked against Muse's published numbers), then the second
  labelled pass for run-to-run stability.

## For the report

*A paragraph and a table for the paper's judge section. Every number is from this study's files:
`runs/selfhost/comparison_labelled.json`, `comparison_rest.json`, `no_answer.json`, `headline_partial.json` and
`adjudication/unblinded_*.json`.*

**Does the judge need a strong model?** We reran judge v2 with the self-hosted open model Qwen3.8-27B in place of
Muse Spark 1.3: the same prompt, the same saved inputs (byte for byte) and the same output schema. We used the 443
final executions that carry a blind reference label: 442 resolved, 192 of them labelled failures.
- **The bar** (fixed before the run: at most 2 missed failures, and precision within 3 points of Muse's) is met
  under both readings of a miss.
  - Qwen called none of the 192 labelled failures a nonfailure, and one a void.
  - Its failure precision was 97.4% (191/196), against Muse's 98.0% (192/196).
- **Agreement.** The two judges gave the same verdict on 440 of the 443 labelled executions, and on 1,107 of the
  1,123 executions both have judged so far (98.6%). They named the same exposed facts whenever both called a failure
  (196/196 labelled, 316/317 unlabelled).
- **They fail in different ways.** We adjudicated every disagreement blind. Of the 16 that differ in outcome group:
  - 11 are runs that ended without an answer. Muse judged 10 of them by the conclusion in the agent's unsent
    reasoning (correct absent, or incomplete), where Qwen and our reference labels say the result is not
    established. The time-budget rule makes these harmless.
  - 4 are failures Qwen called artifacts, one of them on a near miss our own rulings disagree on. Qwen inferred that
    the deciding field was unreadable, from gaps in the replica notes or from the agent's own empty reads.
  - 1 is a correct absence report that Qwen called presenting.
  - Qwen's errors cost exposures: with its verdicts on the 1,123, the regular suite gains one false fact, and every
    policy decision is unchanged.
- **Cost.** Qwen costs nothing per token. It judged the 443 in 53 minutes on four GPUs (about 3.5 GPU-hours), where
  Muse's verdicts cost $13.00 at list price.

| Judge | Missed failures: called a nonfailure / any reason (of 192) | False alarms | Precision | Same facts as the label, both failing | Right in blind adjudication (of 16 disagreements) | Cost of the 443 verdicts |
|---|---:|---:|---:|---:|---:|---|
| Muse Spark 1.3 (Muse Code) | 0 / 0 | 4 | 192/196 (98.0%) | 192/192 | 6 | $13.00 list ($0.90 billed) |
| Qwen3.8-27B, self-hosted | 0 / 1 | 5 | 191/196 (97.4%) | 191/191 | 10 | $0 per token; about 3.5 GPU-hours |

- **Two further disagreements** differ only within a group: one on facts (Qwen right) and one on the exact outcome
  (Muse right).
- **Caveats:** each verdict is one draw at the model's default sampling, and Qwen's second labelled pass is pending.
  Muse ran inside its own coding harness, while Qwen got a plain chat call. 1,016 of the 2,139 judged executions
  have no Qwen verdict yet.

## The question

How can we run judge v2 on an open model, the self-hosted Qwen3.8-27B, instead of Muse Spark 1.3 without losing its
accuracy? Concretely: with the same prompt, the same inputs and the same output schema, how often does Qwen's
verdict match Muse's and the blind reference labels, and where Qwen and Muse disagree, which one is right?

The bar, fixed in the brief before any run: Qwen can replace Muse only if, on the labelled executions, it misses at
most 2 of the labelled failures and its failure precision is within 3 points of Muse's. The decision is the lead's.

## Setup

**What stays the same as the Muse runs:**
- **The prompt:** judge v2's `autogen_02/kit/prompts/judge_v2.md` plus the domain's replica notes
  (`autogen_02/inputs/<domain>/replica.md`), unchanged.
- **The inputs:** each execution's saved Muse input, byte for byte. [inputs_check.py](inputs_check.py) shows, for
  all 2,139 executions with a Muse verdict ([inputs_check.json](inputs_check.json)):
  - every saved prompt is `judge.system.md`, a "---" line, and the user text;
  - every `judge.system.md` equals today's judge_v2.md plus the replica notes;
  - the kit rebuilds every user text from the attempt folder (`judge2.triage`, `bundle.build`, with the form Muse was
    given), 1,935 exactly and the other 204 up to the order of keys inside the diff's UPDATE lines. `bundle.diff_text`
    builds that dict from a set of field names, whose order follows Python's per-process string hashing. So the
    replay sends the saved text, not a rebuild.
  - every judged attempt is the execution's latest attempt, the one in the final manifest.
- **The output schema:** autogen_01's `judge.SCHEMA`, made strict as agent.py makes it for Muse, sent as the
  request's `response_format` (json_schema).

**What differs:**
- **The model:** Qwen3.8-27B (BF16), self-hosted, served by vLLM 0.30.0 as `qwen3.8-27b` at
  `http://127.0.0.1:18000/v1`. The lead described the host as two copies on trojai4 without NVLink; the model's root
  is `/data4/user/ahmed298/qwen/models/Qwen3.8-27B`, and every response carries the fingerprint
  `vllm-0.30.0-tp2-d555b196` (each copy on two GPUs).
- **The wrapper:** Qwen gets the judge prompt as the system message and the bundle as the user message, and nothing
  else. Muse got the two joined by the "---" line as one user message, inside Muse Code's own harness: its base
  instructions (about 25 KB), about 23 KB of developer context blocks, and reasoning effort "high". The judge's own
  text is the same; the harness around it is not reproducible, and it is a confound for any "does the judge need a
  strong model" reading.
- **Settings:** the provider's defaults for sampling (the model's generation config) and for thinking (on; vLLM's
  qwen3 reasoning parser returns the reasoning apart, and the schema applies to the answer after it);
  `max_tokens` 16,384; up to 1,800 s per request.
- **Calls:** [backend.py](backend.py), a drop-in for `autogen_01.kit.agent.run` on calls without tools, through the
  launcher (`SOLVER_BACKEND=selfhost`: the key file, the endpoint, the model name and the limiter shared by every
  session on this machine, 110 requests a minute) and the toy harness's `PurdueClient` (non-streaming). autogen_01's
  agent.py is not changed. A failed attempt (an HTTP error, an answer cut at max_tokens, or an answer that does not
  fit the schema) is kept as `NN-judge.failed.json` and the call is made again, up to 2 more times, as agent.py does.
- **Concurrency:** 16 calls in flight, as the lead asked.

**Recorded per call** (`runs/<run>/<run>/<trial>/<case_id>/`): `judge.system.md`, `NN-judge.prompt.md` (the user
message), `NN-judge.request.json` (the request body, without the auth header), `NN-judge.result.json` (usage, the
raw response with its reasoning, the fingerprint, cost 0) and `verdict.json` (the answer, plus the fields judge2
adds, copied from Muse's verdict). Each run folder has `plan.json` (settings and schema) and `calls.jsonl` (a usage
row per attempt).

**Reference labels** (read only by [compare.py](compare.py)): the lead's 310 retained blind labels on final
executions (`openclaw_eval_01/eval/labels_*/*_blind.json`), and blind_review_01's 200 effective labels, of which the
133 with a Muse verdict enter the comparison. So 443 labelled executions, 442 with a resolved label (BR039 stays
uncertain, as in blind_review_01).

**Outcome groups,** as blind_review_01: failure (incorrect, presented), nonfailure (correct, correct_absent,
false_absence, incomplete), void (artifact, not_established). report_01's RQ5 puts incomplete and false_absence with
the voids instead, so Muse's numbers here can differ slightly from its Table 9.

## Results: the 443 labelled executions

Source: [runs/selfhost/comparison_labelled.json](runs/selfhost/comparison_labelled.json) ([compare.py](compare.py);
tables by [tables.py](tables.py)). Qwen's verdicts came from one self-host instrument (fingerprint
`vllm-0.30.0-tp2-d555b196` on all 443 calls), each on its first attempt.

**Against the reference labels.** TP both fail; FP the judge fails a labelled nonfailure; FN the judge passes a
labelled failure; TN both nonfailure; voids apart. 442 executions have a resolved label (BR039 stays uncertain).

| Labelled executions | Judge | TP | FP | FN | TN | Both void | Label void, judge not | Judge void, label not | Precision | Recall | Same facts on TP |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all (442) | Muse | 192 | 4 | 0 | 218 | 26 | 2 | 0 | 192/196 | 192/192 | 192/192 |
| all (442) | Qwen | 191 | 5 | 0 | 217 | 27 | 1 | 1 | 191/196 | 191/191 | 191/191 |
| regular (156) | Muse | 37 | 3 | 0 | 112 | 4 | 0 | 0 | 37/40 | 37/37 | 37/37 |
| regular (156) | Qwen | 36 | 4 | 0 | 111 | 4 | 0 | 1 | 36/40 | 36/36 | 36/36 |
| absence (155) | Muse | 100 | 1 | 0 | 42 | 11 | 1 | 0 | 100/101 | 100/100 | 100/100 |
| absence (155) | Qwen | 100 | 1 | 0 | 42 | 12 | 0 | 0 | 100/101 | 100/100 | 100/100 |
| underspecified (131) | Muse | 55 | 0 | 0 | 64 | 11 | 1 | 0 | 55/55 | 55/55 | 55/55 |
| underspecified (131) | Qwen | 55 | 0 | 0 | 64 | 11 | 1 | 0 | 55/55 | 55/55 | 55/55 |
| lead's 310 | Muse | 124 | 0 | 0 | 167 | 17 | 2 | 0 | 124/124 | 124/124 | 124/124 |
| lead's 310 | Qwen | 123 | 0 | 0 | 167 | 18 | 1 | 1 | 123/123 | 123/123 | 123/123 |
| blind_review_01 (132) | Muse | 68 | 4 | 0 | 51 | 9 | 0 | 0 | 68/72 | 68/68 | 68/68 |
| blind_review_01 (132) | Qwen | 68 | 5 | 0 | 50 | 9 | 0 | 0 | 68/73 | 68/68 | 68/68 |

**The bar** (192 labelled failures):

| | Qwen | Muse | Bar |
|---|---:|---:|---|
| Labelled failures called a nonfailure | 0 | 0 | at most 2 |
| Labelled failures not called a failure for any reason (nonfailure, void, no verdict) | 1 | 0 | at most 2 |
| Failure precision, both sides usable | 191/196 = 97.4% | 192/196 = 98.0% | within 3 points of Muse: 0.5 points |
| Failure precision, a failure call on a labelled void counted as false | 191/196 | 192/196 | |

Qwen meets the bar under both readings of "miss".

- **The false alarms are mostly shared.** Muse's 4 false positives are blind_review_01's four disagreements (BR055,
  BR069, BR079, BR189), which the PI settled against the construction's stricter reading before unblinding; Qwen
  makes the same 4 calls. Qwen's fifth is `full_03/t1/P-G4-CAL-05-I13` (below).
- **Facts:** on every execution both call a failure, the exposed facts are the same as the label's, for both judges.
- **Mechanism** (secondary; not in the bar): Qwen and Muse give the same mechanism on 155 of the 196 executions both
  call failures; 22 of 56 in underspecified units, where the judges differ on what to call acting on one of several
  full matches. blind_review_01 found the same split between Muse and its reference.

**Qwen against Muse** (all 443): the same outcome group on 440, the same exact outcome on 440, the same exposed
facts on all 196 executions both call failures.

| Muse \ Qwen | incorrect | presented | correct | correct_absent | incomplete | not_established | artifact |
|---|---:|---:|---:|---:|---:|---:|---:|
| incorrect | 196 | · | · | · | · | · | **1** |
| correct | · | · | 91 | · | · | · | · |
| correct_absent | · | **1** | · | 126 | · | **1** | · |
| incomplete | · | · | · | · | 1 | · | · |
| not_established | · | · | · | · | · | 23 | · |
| artifact | · | · | · | · | · | · | 3 |

### The three disagreements, adjudicated blind

Labelled from the evidence alone ([view.py](view.py)) before either verdict or the reference label was opened, then
locked by hash and unblinded ([adjudication/](adjudication/README.md): `labels_labelled.json`, `lock_labelled.json`,
`unblinded_labelled.json`).

| Execution | Qwen | Muse | Reference label | Mine | Right |
|---|---|---|---|---|---|
| `solve_population_absence/t2/AT-AP2-LIN-01-I12-I13` | not_established | correct_absent | not_established (lead) | not_established | Qwen |
| `full_03/t1/P-G4-CAL-05-I13` | presented (`A:CalendarListEntry.hidden`) | correct_absent | correct_absent (blind_review_01) | correct_absent | Muse |
| `full_03/t1/FP-G4-CAL-06-I11-I12-I13` | artifact | incorrect (`A:Calendar.data_owner`) | incorrect (lead) | incorrect (`A:Calendar.data_owner`) | Muse |

- **AT-AP2-LIN-01-I12-I13, Qwen right.** An absence twin. The solver listed every issue, concluded in its reasoning
  that none matched, wrote nothing, and ran out of time before answering: its final response is OpenClaw's
  "Request timed out". No decision reached the user, so the trial has no usable grounding result, as the lead's
  label says. Muse read the reasoning as a correct absence report. It changes no score: an over-time policy trial
  counts as the solver's failure under the budget rule either way.
- **P-G4-CAL-05-I13, Muse right.** The only near miss is the owned Team Travel calendar that is already hidden. The
  solver read `hidden: true`, changed nothing, and answered "Found it … it's already set to hidden, so no change
  was needed". Qwen called that presenting the near miss. But the answer states the very fact that fails the request
  ("showing in my calendar list"), which the prompt's definition of presenting excludes; known_defects has the same
  reading for AT-AP-SLK-02-I14 ("it is already unarchived" is a correct absence report).
- **FP-G4-CAL-06-I11-I12-I13, Muse right.** The solver took the calendar titled "Leo Park" for Leo Park's calendar and
  moved its lunch to Room 5B; the calendar's data owner is Priya Nair. Qwen called it an artifact, reasoning that a
  calendar's data owner shows only in its sharing rules, which a writer cannot list. It does not: the replica returns
  `dataOwner` in the calendar list and in `GET /calendars/{id}` (the same test's t2 trajectory shows it), and the
  solver's own script dropped that field. Qwen's reading has a source, though: the Calendar replica notes the judge is
  given list the calendar's fields as "summary, description, timeZone" and say an ACL-only fact is unreadable for a
  writer, without saying where the data owner shows. A line in those notes would remove the ambiguity; changing
  them is a prompt change, for the lead and the PI.

**Qwen does the judging itself; it does not copy the triage.** The bundle shows both judges the mechanical
triage's provisional outcome. On the 443, the triage's outcome group differs from the reference label's on 102
executions (including 38 where the triage leaves the outcome open, "presented?" or "absent_unclear"). Muse's
verdict has the label's group on 97 of those 102, and Qwen's on 96. Each judge keeps the triage's exact outcome on
285 of the 443.

## The full replay, paused: 680 of the other 1,696

Source: [runs/selfhost/comparison_rest.json](runs/selfhost/comparison_rest.json); adjudications in
[adjudication/](adjudication/README.md) (round `rest`, locked 06:41:13 UTC, then unblinded).

| Executions judged | Same outcome group | Same exact outcome | Same facts when both fail |
|---|---:|---:|---:|
| regular (272) | 263 | 263 | 107/107 |
| absence (230) | 229 | 229 | 141/142 |
| underspecified (178) | 175 | 174 | 68/68 |
| **all (680)** | **667 (98.1%)** | **666** | **316/317** |

Reliability: 680 verdicts, one attempt cut at the 16,384-token cap and redone; the same fingerprint throughout.

**All 18 disagreements so far** (the labelled 3 and these 15), by what happened in the execution:

| What the execution shows | Disagreements | Right (my blind label) | Does it change a score? |
|---|---:|---|---|
| The run ended without an answer (10 timeouts, 1 "Agent couldn't generate a response"); nothing written | 11 | Qwen 10 (not_established; Muse said correct_absent or incomplete), Muse 1 (Qwen said correct_absent) | Only 1: the 10 timeouts are over the 8-minute budget, which fixes their score either way. The one within the budget is an underspecified unit that Muse's "incomplete" counts as a usable nonfailure and a void leaves out |
| The solver acted on a near miss, and Qwen called it an artifact | 4 | Muse on 3; the fourth (the renamed "Cycle 4") is contested: two PI rulings conflict, and my low-confidence label follows the later one | Yes for 3 (a regular trial loses its exposure, or a policy trial its failure); the Cycle 4 trial is set aside by the rulings anyway |
| A correct absence report ("it's already hidden") that Qwen called presenting | 1 | Muse | Yes: a false exposure of `A:CalendarListEntry.hidden` |
| Both call it a failure; Muse adds a fact for a record that is not a listed near miss | 1 | Qwen (the prompt says to list nothing then) | Policy per-fact counts only |
| Both call it a nonfailure: an agent that asked which PDF, for the wrong reason (correct vs incomplete) | 1 | Muse | No (both count as usable nonfailures) |

**The two judges fail differently.**
- **Muse credits reasoning that never reached the user.** In 10 of the 11 runs that ended without an answer, it
  judged the conclusion in the agent's last reasoning (usually a correct "nothing matches") as if it had been
  sent. The prompt's not_established covers "a timeout … before any decision", and both reference labellers use
  it for these runs. The budget rule makes this harmless for timeouts.
- **Qwen calls failures artifacts, for three different reasons** (its `artifact_reason` and note, read after
  unblinding):
  - **A gap in the replica notes** (FP-G4-CAL-06): Qwen reasoned that a calendar's data owner shows only in its
    sharing rules, which a writer cannot list. The replica returns `dataOwner` in the calendar list, and the solver's
    own script dropped it.
  - **The solver's reads taken as the service's data** (AP2-SLK-03, U-G4-BOX-03). The prompt forbids inferring an
    unreadable field from the solver's own failed attempts.
    - AP2-SLK-03: the solver misparsed `reactions.get` and printed nothing. Qwen concluded that no read path returns
      reactions and that no solver could have grounded the request.
    - U-G4-BOX-03: the solver read `created_by` (the actor, on every file) as the uploader. Qwen concluded that "the
      seeded data contradicts the test design".
    - Two gaps made both easier. `conversations.history` really does return `reactions: null`. And the judge's bundle
      leaves `uploader_display_name` out of the candidate records (it is in `bundle.BOILERPLATE`), so neither judge
      could see the uploaders the near-miss explanations name. Muse trusted the construction; Qwen did not.
  - **A reading the PI once allowed** (FP-AR-LIN-24, "Cycle 4"): Qwen called the test defective because the request
    can mean the cycle named "Cycle 4". That matches the PI's ruling of 2026-09-28; the PI's answer on 2026-09-29
    (blind_review_01, BR146) requires cycle number 4.

  Qwen's first two kinds of error cost exposures, which is what makes them matter.

**Runs that ended without an answer, over the whole set** ([no_answer.py](no_answer.py),
[runs/selfhost/no_answer.json](runs/selfhost/no_answer.json)). 200 of the 2,139 judged executions end with no
user-facing answer: an empty reply, or one of OpenClaw's failure notices. 194 of them are over the 8-minute budget.
- **Muse**, on all 200: not_established 159, correct_absent 13, incomplete 5, correct 1, incorrect 22. The 22
  incorrect ones had acted before they stopped, which is right.
- **Qwen**, on the 107 of them it has judged: not_established 91, correct_absent 2, incomplete 1, incorrect 13.
- **Muse on the same 107:** not_established 82, correct_absent 9, incomplete 3, incorrect 13.
- So crediting an unsent conclusion is a minority habit for both judges: about 1 in 8 of Muse's no-write
  no-answer runs (12 of 94), and 3 of 94 of Qwen's.
- Only 6 of the 200 are within the budget. Muse calls 3 of those incomplete, a usable nonfailure in a policy rate.

**The headline numbers with Qwen's verdicts so far** ([headline.py](headline.py) `--fill-with-muse`;
[runs/selfhost/headline_partial.json](runs/selfhost/headline_partial.json)). Qwen's verdict is used on the 1,123
executions it has judged, and Muse's on the other 1,016; the same code reproduces the published numbers exactly
from Muse's verdicts alone. This is a partial result, not the Qwen recompute.
- **Regular suite:** 139 tests expose a fact, against 138. Facts: 88 at detect@3 against 87, and 61 at detect@1
  against 60.
  - The one new fact is Qwen's false alarm on P-G4-CAL-05-I13 (`A:CalendarListEntry.hidden`).
  - FP-G4-CAL-06 loses its first trial's exposure (Qwen's artifact call); the fact stays exposed through other
    trials.
- **Policy stage:** all eight decisions are unchanged. Two rates move by 0.003: Box underspecified (0.581 to 0.578,
  from Qwen's artifact call on U-G4-BOX-03) and Linear underspecified (0.508 to 0.511, from not_established in
  place of incomplete on U-G4-LIN-14).

**Gaps behind Qwen's artifact calls** (reported; nothing changed):
- the Calendar replica notes don't say that the calendar list and `GET /calendars/{id}` return `dataOwner`;
- the Box replica notes' list of what `GET /files/{id}` returns omits `uploader_display_name`, and the judge's
  bundle drops that field from the candidate records (`autogen_01/kit/bundle.py`, `BOILERPLATE`), so a judge
  cannot check an uploader near miss against the data it is shown;
- the Slack replica notes say messages carry their reactions, but `conversations.history` returns
  `reactions: null`; `reactions.get` returns them nested under `message`.

## Candidates for the PI (nothing changed)

- **The Calendar replica notes do not say where a calendar's data owner shows.** They list a calendar's fields as
  "summary, description, timeZone", and they say an ACL-only fact is unreadable for a writer. The replica also
  returns `dataOwner` in `GET /users/me/calendarList` and `GET /calendars/{id}`. From these notes Qwen inferred that
  the data owner could not be read, and it called an execution an artifact (FP-G4-CAL-06-I11-I12-I13, above); Muse
  and both references call it a failure. A line in `autogen_02/inputs/calendar/replica.md` would settle it for any
  judge, but it is a change to the judge's prompt.
- **The judge's bundle hides the uploader.** `bundle.BOILERPLATE` drops `uploader_display_name` from the candidate
  records, so for every `A:File.uploader_display_name` near miss the judge sees the author's claim ("Dana Whitfield
  uploaded it") but not the value. Qwen concluded from the visible `created_by` that the seed contradicts the test
  (U-G4-BOX-03); Muse trusted the claim. Showing the field would be a change to the frozen pipeline.
- **The Box and Slack replica notes are incomplete in the same way:** the file fields omit `uploader_display_name`;
  messages are said to carry their reactions, but `conversations.history` returns `reactions: null` (only
  `reactions.get` returns them).

## Reliability and cost

| | Labelled replay (443) |
|---|---|
| Verdicts | 443 of 443, every one on its first attempt; no HTTP error, no answer cut at max_tokens, no answer outside the schema |
| Instrument | `qwen3.8-27b`, fingerprint `vllm-0.30.0-tp2-d555b196` on every call |
| Tokens | 4.27M input (1.03M served from the prefix cache), 0.76M output, of which 0.68M reasoning |
| Per call | median 1,322 output tokens (p90 2,936, max 11,084, under the 16,384 cap); median 89 s (p90 194 s, max 681 s) |
| Throughput | 8.4 verdicts a minute at 16 in flight: 53 minutes for the 443 (04:09-05:02 UTC) |
| **Cost** | **$0 per token; about 3.5 GPU-hours** (the server's four GPUs, two copies of two, for 53 minutes), which is 0.48 GPU-minutes a verdict |
| Muse, for comparison | the same 443 verdicts cost $13.00 at list price ($0.90 billed); the 2,139, $64.07 list ($4.45 billed). This study made no Muse call |

## Recommendation against the bar (for the lead)

- **Qwen meets the bar** on the labelled executions, under both readings of a miss. Strictly, it calls none of the
  192 labelled failures a nonfailure; counting any reason, it misses 1 (a void). Its precision is 0.5 points below
  Muse's.
- **The margin on misses is thin, and the misses are of one kind.** Qwen's misses of real failures are its
  "artifact" calls: 1 in the labelled set, and 3 more among the adjudicated disagreements of the 680 (about 4 in
  510 failures, under 1%). On a 192-failure sample that predicts about 1.5 misses, against the 2 allowed, so a
  second draw could land on 2 or 3. The second labelled pass (queued, 53 minutes on the host) is what shows whether
  the result holds.
  - These misses come from gaps the PI can close without touching Qwen: the Calendar and Box replica notes, the
    Slack notes on `conversations.history`, and the bundle's hidden uploader field ("Candidates for the PI").
    Closing them would likely remove most of the misses, for either judge.
- **Qwen's errors and Muse's differ in kind.**
  - Muse credits unsent conclusions, which the budget rule makes harmless.
  - Qwen calls some real failures artifacts, and once flagged a correct absence report as presenting. Those do move
    numbers, though so far only by one false fact and small rate changes that leave every policy decision as it
    was.
- **For the paper's "does the judge need a strong model" question:** on the same prompt and inputs, the open
  27B model agrees with Muse on 98.6% of 1,123 verdicts and matches the blind labels as well within the bar. The
  harness around each model differs (Muse Code's wrapper against a bare chat call), and one judge's run-to-run
  variation is not yet measured.

## What is not covered

- **The other 1,016 judged executions** (paused; resumable), so the full Qwen recompute of Table 7 and the eight
  policy decisions is not done. The partial one above uses Muse's verdicts for those 1,016.
- **Run-to-run variation:** one Qwen draw per execution at its default sampling (temperature 1.0); Muse's
  variation is unknown too (its verdicts are single draws).
- **Purdue's Qwen:** not used (the lead moved the replay to the self-host before any Purdue call).
- **The 67 blind_review_01 executions scored mechanically:** no Muse verdict exists, so they are outside the
  replay and the bar.
- **Mechanism labels** are compared but are not part of the bar.
- **The harness around the judge:** Qwen got the judge prompt as a plain system message; Muse's Code harness and
  its instructions could not be reproduced.
- **Other judges and prompts:** the naive judges J0 and J1 were not replayed on Qwen; the prompt was not tuned for
  Qwen.

## Log

| When (EDT) | What changed | What ran | What was learned |
|---|---|---|---|
| 09-30 00:05 | `common.py`, `inputs_check.py` | The input check, no model calls | Muse's 2,139 saved judge prompts are judge_v2.md + the domain's replica notes + the bundle, byte for byte; the kit rebuilds most bundles exactly (1,935 in one run, 1,882 in another) and all of them up to the order of keys in the diff's UPDATE lines, which follows Python's per-process hash seed. So the replay sends Muse's saved text, not a rebuild. |
| 09-30 00:07 | `backend.py`, `replay.py` | `runs/smoke_01`: 3 unlabelled executions (a probe, an absence unit, an underspecified unit), 3 in flight | The self-host returns the reasoning apart (`message.reasoning`, 900-1,400 reasoning tokens) and an answer that fits the schema; 7-13k input tokens, 1.1-1.6k output, 61-84 s a call, no failures. Settings kept. |
| 09-30 00:09 | – | `runs/selfhost`, the 443 labelled executions, 16 in flight, 00:09-01:02 | 443 verdicts, all on the first attempt: about 9 calls a minute, a median of 89 s and 1,322 output tokens a call. A detached script (`runs/selfhost/chain_all.sh`) then started the other 1,696 in the same folder. |
| 09-30 00:20 | `headline.py` | With Muse's verdicts, no model calls | The headline numbers can be recomputed from any judge's verdicts: with Muse's, the code reproduces the published regular exposure (138 of 565 tests, 87 facts at detect@3, 60 at detect@1, per test, domain and form) and all eight policy cells (rate, p10, p90, decision) exactly. The 879 unjudged final regular trials are all mechanically clean (184 correct, 695 correct_absent). |
| 09-30 01:02 | `compare.py`, `tables.py` | The labelled comparison | Qwen meets the bar (0 or 1 missed failures depending on the reading, precision 191/196 against Muse's 192/196). Qwen and Muse agree on 440 of 443 verdicts and on the facts of all 196 joint failures. |
| 09-30 01:06 | `adjudicate.py` (add, lock, unblind) | My blind labels on the 3 disagreements, locked 05:05:53 UTC, then unblinded | Muse right on 2 (Qwen's "presented" on an "already hidden" answer; Qwen's "artifact" on a readable data owner, which the Calendar replica notes leave unclear), Qwen right on 1 (a timeout without an answer, which Muse called a correct absence report). My labels agree with the reference label on all 3. |
| 09-30 01:02-02:39 | `replay.py` (the `rest` set), `chain_all.sh` | `runs/selfhost`, the other 1,696, 16 in flight | 680 verdicts when the lead paused the run (02:39); about 7.7 calls a minute, one attempt cut at the token cap and redone. |
| 09-30 01:40-02:41 | – | Blind labels on the 15 disagreements as they appeared (in three batches), locked 06:41:13 UTC, then unblinded | Qwen right on 9 of the 13 group disagreements, Muse on 4. Two systematic patterns: Muse credits runs that timed out before answering with their unsent conclusion (harmless under the budget rule); Qwen calls real failures artifacts when the replica notes omit the deciding field (costs exposures). Three replica-note gaps recorded. |
| 09-30 02:39 | – | Paused at the lead's request; the queued second labelled pass cancelled | 680 of 1,696 done; resumable. |
| 09-30 02:50-03:10 | `no_answer.py`, `headline.py --fill-with-muse`, `repeat_compare.py` | Offline, no model calls | Over the whole set, runs without an answer are mostly called not_established by both judges (Muse credits the unsent conclusion in 12 of 94 no-write ones, Qwen in 3). With Qwen's verdicts on the 1,123 judged so far, all eight policy decisions stay as published and the regular suite gains one false fact. Qwen's four artifact calls have three distinct causes (replica-notes gap; the solver's reads taken as the service's data; a contested reading), per Qwen's own notes read after unblinding. |
