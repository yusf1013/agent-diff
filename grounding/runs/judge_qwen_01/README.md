# judge_qwen_01: judge v2 on the self-hosted Qwen instead of Muse

Session "judge_qwen", started by the lead ("RoadMap specialist") on 2026-09-30 from the brief
[briefs/judge_qwen.md](../../protocols/briefs/judge_qwen.md).

## Status

- **2026-09-30 19:25 EDT. Done; the decision is the lead's.** Every step of the brief is finished on the current
  manifest (2,994 final executions, 2,115 of them with a Muse verdict).
- **The labelled replay:** Qwen meets the bar on both of two independent passes, with the same numbers each time.
  - Of 189 labelled failures, it calls none a nonfailure and one a void (the bar allows 2 misses).
  - Its precision is 188/192 (97.9%), against Muse's 189/192 (98.4%).
- **The full replay (all 2,115):**
  - Qwen and Muse give the same outcome group on 2,085 (98.6%) and the same exposed facts on 980 of the 983
    executions both call failures.
  - I adjudicated all 34 disagreements blind, in three rounds, each locked by hash before unblinding. On the 30 that
    differ in outcome group, Qwen is right on 19 and Muse on 11.
- **The headline numbers with Qwen as the judge:**
  - all eight policy decisions are unchanged (rates move by at most 0.009);
  - the regular suite keeps 139 of 563 tests exposing a fact and 87 facts at detect@3. One fact is swapped: Qwen
    loses `R:message_reactions` and adds a false `A:CalendarListEntry.hidden`.
- **Cost:** about 18.5 GPU-hours for the full replay and 4.1 for the second labelled pass, at $0 per token. Muse's
  2,115 verdicts cost $63.33 at list price.
- **History:** the replay was paused from 02:39 to 15:46 EDT for other sessions' solver runs.
  - The section on the 443 labelled executions was written on the manifest of 2026-09-29, before 24 executions of
    G4-BOX-02 and G4-BOX-11 left the suite. It is kept as the record.
  - The current manifest's 437 are in the section after it.

## For the report

*A paragraph and a table for the paper's judge section. Every number is from this study's files on the current
manifest: `runs/selfhost/comparison_all.json`, `comparison_pass1_437.json`, `headline.json`, `no_answer.json`;
`runs/selfhost_repeat/comparison_pass2.json`, `repeat_labelled.json`; and `adjudication/unblinded_*.json`.*

**Does the judge need a strong model?** We reran judge v2 with the self-hosted open model Qwen3.8-27B in place of
Muse Spark 1.3. The prompt, the saved inputs (byte for byte) and the output schema were the same, and the replay
covered all 2,115 executions the pipeline judges.
- **The labelled executions:** 437 carry a blind reference label, 189 of them labelled failures.
  - Qwen called none of the failures a nonfailure and one a void.
  - Its failure precision was 97.9% (188/192), against Muse's 98.4% (189/192).
  - A second, independent Qwen pass gave the same numbers.
  - So the bar we fixed in advance (at most 2 missed failures, precision within 3 points) is met under both
    readings of a miss.
- **Agreement over all 2,115.** The two judges gave the same outcome group on 2,085 (98.6%). They named the same
  exposed facts on 980 of the 983 executions both called failures.
- **Who is right when they disagree.** We adjudicated all 34 disagreements blind. The judges fail in different
  ways:
  - **Runs that ended without an answer (17):** Muse judged 14 of them by the conclusion in the agent's unsent
    reasoning, where the result is not established, and Qwen erred on the other 3. Only 3 of the 17 change a score.
  - **Real failures called artifacts (8):** Qwen called 7 real failures artifacts. It inferred that the deciding
    field was unreadable, from gaps in the replica notes or from the agent's own empty reads. Muse did this once.
  - **Replica defects (3):** Qwen voided 3 trials that a replica defect had decided, where Muse graded them.
  - **Two single cases:** Qwen called a correct absence report "presenting", and Muse passed an answer that offered
    a near miss among the matches.
- **With Qwen's verdicts,** every policy decision and the regular suite's totals are unchanged; one exposed fact is
  swapped for a false one.
- **Cost.** Qwen costs nothing per token: about 18.5 GPU-hours for its 2,128 verdicts, or 0.52 GPU-minutes each.
  Muse's 2,115 verdicts cost $63.33 at list price.

| Judge | Missed failures: called a nonfailure / any reason (of 189) | False alarms | Precision | Same facts as the label, both failing | Right in blind adjudication (of 30 outcome-group disagreements) | Cost of judging the set |
|---|---:|---:|---:|---:|---:|---|
| Muse Spark 1.3 (Muse Code) | 0 / 0 | 3 | 189/192 (98.4%) | 189/189 | 11 | $63.33 list ($4.41 billed) for 2,115 verdicts |
| Qwen3.8-27B, self-hosted | 0 / 1 in both passes | 4 in both passes | 188/192 (97.9%) in both passes | 188/188 | 19 | $0 per token; about 18.5 GPU-hours for 2,128 verdicts |

- **Four further disagreements** differ only within a group. Qwen is right on 2 and Muse on 2.
- **Caveats:**
  - The adjudications are one annotator's, 14 of the 34 with medium or low confidence.
  - Muse ran inside its own coding harness, while Qwen got a plain chat call.
  - Qwen's two labelled passes give the same outcome group on 434 of 437; Muse's run-to-run variation is not
    measured.

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
row per attempt; `runs/selfhost` keeps it gzipped, `calls.jsonl.gz`, to stay under 1 MB).

**Reference labels** (read only by [compare.py](compare.py)): the lead's 310 retained blind labels on final
executions (`openclaw_eval_01/eval/labels_*/*_blind.json`), and blind_review_01's 200 effective labels, of which the
133 with a Muse verdict enter the comparison. So 443 labelled executions, 442 with a resolved label (BR039 stays
uncertain, as in blind_review_01). On the current manifest (2026-09-30), 437 remain: 436 resolved, 189 of them
labelled failures ([common.py](common.py) `labels()` skips the executions that left).

**Outcome groups,** as blind_review_01: failure (incorrect, presented), nonfailure (correct, correct_absent,
false_absence, incomplete), void (artifact, not_established). report_01's RQ5 puts incomplete and false_absence with
the voids instead, so Muse's numbers here can differ slightly from its Table 9.

## Results: the 443 labelled executions

*On the manifest of 2026-09-29, kept as the record. The current manifest's 437 are in the next section, with the
same result against the bar.*

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

## The second labelled pass: is the bar result stable?

Qwen judged the labelled executions a second time with the same settings (`runs/selfhost_repeat`, 2026-09-30
19:46-20:48 UTC; [repeat_compare.py](repeat_compare.py) →
[runs/selfhost_repeat/repeat_labelled.json](runs/selfhost_repeat/repeat_labelled.json); against Muse and the labels
in [runs/selfhost_repeat/comparison_pass2.json](runs/selfhost_repeat/comparison_pass2.json)).
- **The labelled set** is the current manifest's: 437 executions, 436 with a resolved label and 189 labelled
  failures. The manifest of 2026-09-30 dropped 24 executions of G4-BOX-02 and G4-BOX-11, 6 of them labelled.
- **Pass 1 on the same 437:** [runs/selfhost/comparison_pass1_437.json](runs/selfhost/comparison_pass1_437.json).

| On the 437 labelled | Qwen, pass 1 | Qwen, pass 2 | Muse |
|---|---:|---:|---:|
| Missed failures: called a nonfailure / any reason (of 189) | 0 / 1 | 0 / 1 | 0 / 0 |
| False alarms (label a nonfailure) | 4 | 4 | 3 |
| Failure precision | 188/192 (97.9%) | 188/192 (97.9%) | 189/192 (98.4%) |
| Failure calls on labelled voids | 0 | 2 | 0 |
| Same exposed facts as the label, both failing | 188/188 | 188/188 | 189/189 |
| Same outcome group as Muse | 434/437 | 433/437 | – |

- **The bar holds on both draws, with the same numbers:** no labelled failure called a nonfailure, one called a
  void, and precision 0.5 points below Muse's.
- **Qwen against itself:** the two passes give the same outcome group on 434 of 437, and the same facts on all 193
  executions both call failures. The 3 that differ were all void in pass 1:
  - **AR-SLK-23** (t2) and **AT-AR-LIN-26-I11-I12-I13** (t2): labelled artifacts (a near miss the PI ruled flawed;
    an ignored subscribers filter). Pass 2 called them failures.
  - **AT-AP2-LIN-01-I12-I13** (t2): the timeout without an answer from the first adjudication. Pass 2 took Muse's
    reading, correct_absent.
  - So Qwen's handling of no-answer runs, like its artifact calls, varies from draw to draw.
- **Reliability and cost:** 437 verdicts, 2 answers cut at the 16,384-token cap and redone, one fingerprint
  throughout. 62 minutes at 16 in flight (7.1 verdicts a minute): about 4.1 GPU-hours.

## The full replay: all 2,115 judged executions

Source: [runs/selfhost/comparison_all.json](runs/selfhost/comparison_all.json).
- **The runs:** Qwen's verdicts came from two runs of one instrument.
  - 00:09-02:39 EDT: the labelled set and the first 680, on the manifest of 2026-09-29.
  - 16:48-18:56 EDT: the other 1,005.
- **Scope:** 13 executions judged in the first run have since left the suite and are not counted.
- **Reliability:** 2 answers were cut at the 16,384-token cap and redone; no execution was left without a verdict.

| Executions | Same outcome group | Same exact outcome | Same facts when both fail | Same mechanism when both fail |
|---|---:|---:|---:|---:|
| regular (810) | 794 | 794 | 276/276 | 254/276 |
| absence (726) | 721 | 721 | 459/461 | 442/461 |
| underspecified (579) | 570 | 569 | 245/246 | 102/246 |
| Box (503) | 497 | 496 | 261/261 | 203/261 |
| Calendar (398) | 393 | 393 | 211/214 | 180/214 |
| Linear (823) | 809 | 809 | 329/329 | 279/329 |
| Slack (391) | 386 | 386 | 179/179 | 136/179 |
| **all (2,115)** | **2,085 (98.6%)** | **2,084** | **980/983** | **798/983** |

| Muse (rows) \ Qwen (columns) | failure | nonfailure | void |
|---|---:|---:|---:|
| failure | 983 | · | 8 |
| nonfailure | 2 | 934 | 16 |
| void | 1 | 3 | 168 |

**All 34 disagreements, adjudicated blind.** Details are in [adjudication/](adjudication/README.md):
- three rounds (`labelled`, `rest` and `rest2`), each locked by hash before unblinding;
- the later rounds' labels were written after the earlier rounds were unblinded, under the same rules.

| What the execution shows | Disagreements | Right (my blind label) | Does it change a score? |
|---|---:|---|---|
| The run ended without an answer (13 timeouts, 3 "Agent couldn't generate a response", 1 "Exec failed"); nothing written | 17 | Qwen 14 (not_established; Muse said correct_absent 11 times and incomplete 3), Muse 3 (Qwen said correct_absent twice and incomplete once) | Only 3: the 9 regular trials expose nothing under either verdict, and the 5 policy trials over the budget count as failures either way. Three underspecified units within the budget (U-G4-LIN-14, U-G4-CAL-05, U-AP-LIN-06) move between a usable nonfailure and a void |
| The solver acted on a near miss, and one judge called it an artifact | 8 | Muse 7 (Qwen's calls: a calendar's data owner 2, a file's uploader 2, message reactions 2, the contested "Cycle 4"), Qwen 1 (Muse's call on U-G4-BOX-13) | Yes: AP2-SLK-03 loses its fact and FP-G4-CAL-06 its detect@1 exposure; Box underspecified loses 2 failing trials and gains 1. The other two change no test's exposure |
| A replica defect decided the trial: `conversations.history` drops reactions (2), an ignored `projectMilestone` filter (1) | 3 | Qwen 3 (artifact; Muse said false_absence, incomplete and incorrect) | Muse's verdicts give Linear absence a failure the replica caused (AT-G4-LIN-21) and Slack underspecified a nonfailure (U-AP2-SLK-03); the regular trial (G4-SLK-01) exposes nothing either way |
| A correct absence report ("it's already hidden") that Qwen called presenting | 1 | Muse | Yes: a false fact, `A:CalendarListEntry.hidden` |
| A near miss offered as one of several matches, which Muse called correct | 1 | Qwen (medium confidence) | Linear underspecified gains a failing trial |
| Both call it a failure, or both a nonfailure, but the facts or the exact outcome differ | 4 | Qwen 2, Muse 2 | Policy per-fact counts only |

**How the judges fail:**
- **Muse credits reasoning that never reached the user.** In 14 of the 17 runs without an answer, Muse judged the
  agent's unsent conclusion as if it had been sent. The prompt's not_established covers "a timeout … before any
  decision".
  - Over the whole set, 197 runs ended on an empty reply or an OpenClaw failure notice, 188 of them over the budget
    ([no_answer.py](no_answer.py), [runs/selfhost/no_answer.json](runs/selfhost/no_answer.json)).
  - Muse calls 19 of the 197 a nonfailure; Qwen calls 7.
  - Both call the same 22 incorrect: those runs acted before they stopped.
  - The rest are not_established (Muse 156, Qwen 168).
  - The 5 nonfailure calls the judges share were not adjudicated, since the judges agree on them.
  - The detector misses one run that ended on "Exec failed" (U-AP-LIN-06).
- **Qwen calls real failures artifacts, for three reasons** (its `artifact_reason` and notes, read after
  unblinding):
  - **A gap in the replica notes** (FP-G4-CAL-06-I11-I12-I13 t1, G4-CAL-06 t2):
    - Qwen reasoned that a calendar's data owner shows only in its sharing rules, which a writer cannot list.
    - In fact the replica returns `dataOwner` in the calendar list.
  - **The solver's own reads taken as the service's data** (AP2-SLK-03 t2 and t3, U-G4-BOX-03 t2 and t3):
    - The solver misparsed `reactions.get`, or read `created_by` (the actor, on every file) as the uploader.
    - Qwen concluded that no strategy could have grounded the target (reactions), or that the seed does not
      implement the test's uploader distinction. The prompt forbids inferring an unreadable field from the solver's
      own failed attempts.
  - **A reading the PI once allowed** (FP-AR-LIN-24-I11-I12 t3, "Cycle 4"): Qwen called the test defective because
    the request can mean the cycle named "Cycle 4".
    - That matches the PI's ruling of 2026-09-28.
    - The PI's answer of 2026-09-29 (blind_review_01, BR146) requires cycle number 4, and my low-confidence label
      follows it.
  - Muse made an artifact call on a real failure once (U-G4-BOX-13 t3).
- **Qwen is the better judge of replica defects.** Three trials were decided by the replica, not the agent. Qwen
  voided all three, where Muse graded them.
  - Two: `conversations.history` returns `reactions: null`, so the agent saw no reactions (U-AP2-SLK-03, G4-SLK-01).
  - One: an issue filter on `projectMilestone` is not applied, so a near miss came back as a match (AT-G4-LIN-21).
- **One draw per verdict:** Qwen's second pass changed the outcome group on 3 of the 437 labelled executions, all
  three void in its first pass.

### The headline numbers with Qwen as the judge

[headline.py](headline.py) with Qwen's verdicts on all 2,115
([runs/selfhost/headline.json](runs/selfhost/headline.json)).
- The same code reproduces today's published numbers exactly from Muse's verdicts.
- It applies the 10-minute budget and the blind-review rulings, and counts each duplicate unit pair once.
- The 879 final regular trials without a verdict are mechanically clean (184 correct, 695 correct_absent), as
  before.

| | Muse (published) | Qwen |
|---|---|---|
| Regular suite: tests exposing a fact | 139 of 563 | 139 of 563 |
| Facts exposed at detect@3 / detect@1 | 87 / 60 | 87 / 61 |
| Box absence | 0.780 [0.723, 0.837], undecided | the same |
| Calendar absence | 0.817 [0.754, 0.873], undecided | the same |
| Linear absence | 0.656 [0.602, 0.710], not policy-level | 0.655 [0.601, 0.710], not policy-level |
| Slack absence | 0.612 [0.535, 0.690], not policy-level | the same |
| Box underspecified | 0.548 [0.481, 0.615], not policy-level | 0.545 [0.481, 0.612], not policy-level |
| Calendar underspecified | 0.511 [0.422, 0.611], not policy-level | 0.517 [0.422, 0.614], not policy-level |
| Linear underspecified | 0.483 [0.425, 0.542], not policy-level | 0.487 [0.430, 0.545], not policy-level |
| Slack underspecified | 0.802 [0.731, 0.869], undecided | 0.811 [0.742, 0.876], undecided |

- **Three regular tests change:**
  - **AP2-SLK-03** loses `R:message_reactions`, a real fact, through Qwen's two artifact calls.
  - **P-G4-CAL-05-I13** gains `A:CalendarListEntry.hidden`, a false fact, through Qwen's "presented".
  - **FP-G4-CAL-06-I11-I12-I13** loses its first trial's exposure; the fact stays exposed at detect@3.
- **So the facts at detect@3 stay at 87, with one swapped.** Calendar gains a test and a fact, Slack loses one of
  each.
- **The policy rates move by at most 0.009,** from the trials in the table above, and every decision stays as
  published.

## Candidates for the PI (nothing changed)

- **The Calendar replica notes do not say where a calendar's data owner shows.**
  - The notes list a calendar's fields as "summary, description, timeZone", and they say an ACL-only fact is
    unreadable for a writer.
  - The replica also returns `dataOwner` in `GET /users/me/calendarList` and `GET /calendars/{id}`.
  - From these notes Qwen inferred that the data owner could not be read, and called two failures artifacts
    (FP-G4-CAL-06-I11-I12-I13 t1, G4-CAL-06 t2). Muse and my blind labels call both failures, as does the lead's
    reference label on the first.
  - A line in `autogen_02/inputs/calendar/replica.md` would settle it for any judge, but it is a change to the
    judge's prompt.
- **The judge's bundle hides the uploader.**
  - `bundle.BOILERPLATE` drops `uploader_display_name` from the candidate records.
  - So for every `A:File.uploader_display_name` near miss, the judge sees the author's claim ("Dana Whitfield
    uploaded it") but not the value.
  - From the visible `created_by`, Qwen concluded that the seed contradicts the test (U-G4-BOX-03, two trials);
    Muse trusted the claim.
  - Showing the field would be a change to the frozen pipeline.
- **The Box and Slack replica notes are incomplete in the same way.**
  - The Box file fields omit `uploader_display_name`.
  - Slack messages are said to carry their reactions, but `conversations.history` returns `reactions: null` (only
    `reactions.get` returns them). The gap decided two trials (U-AP2-SLK-03, G4-SLK-01), which Muse graded and Qwen
    voided.
- **New in round `rest2`: the Linear replica ignores an issue filter on `projectMilestone`.**
  - `issues(filter: {projectMilestone: {id: …}, assignee: …})` returned WEB-5, which is in no milestone, and the
    solver acted on it (AT-G4-LIN-21-I14 t2).
  - Real Linear would have returned nothing.
  - The replica notes list only the subscribers and parent filters as ignored, so under the prompt's rules Muse
    called it a failure.
  - A replica defect: reported, not fixed.
- **FP-G4-CAL-06, the replica-notes gap the lead asked me to record** (no change): the first item above.

## Reliability and cost

| | Labelled replay (443) | Second labelled pass (437) | Full replay (2,115 current, and 13 since dropped) |
|---|---|---|---|
| When (EDT) | 00:09-01:02 | 15:46-16:48 | 00:09-02:39 and 16:48-18:56 |
| Verdicts | 443, all on the first attempt | 437; 2 answers cut at the 16,384-token cap and redone | 2,128; 2 answers cut at the cap and redone, and no other failed attempt |
| Instrument | `qwen3.8-27b`, fingerprint `vllm-0.30.0-tp2-d555b196` on every call | the same | the same |
| Tokens | 4.27M input (1.03M from the prefix cache), 0.76M output (0.68M reasoning) | 4.23M input (1.02M cached), 0.77M output (0.69M reasoning) | on the 2,115 current verdicts: 20.6M input (4.9M cached), 3.84M output (3.47M reasoning) |
| Per call | median 1,322 output tokens (p90 2,936, max 11,084); median 89 s (p90 194 s, max 681 s) | median 1,309 (p90 3,196, max 12,653); 87 s (p90 205 s, max 776 s) | median 1,363 (p90 3,255, max 13,952); 91 s (p90 217 s, max 922 s) |
| Throughput at 16 in flight | 8.4 verdicts a minute (53 minutes) | 7.1 a minute (62 minutes) | 7.7 a minute (278 minutes) |
| **Cost** | **$0 per token; about 3.5 GPU-hours** | **about 4.1 GPU-hours** | **about 18.5 GPU-hours, 0.52 GPU-minutes a verdict** |
| Muse, for comparison | $13.00 list ($0.90 billed) for the same 443 | – | $63.33 list ($4.41 billed) for the 2,115 |

- **How the GPU-hours are counted:** wall time × the server's four GPUs (two copies of two), as if the host served
  only this replay. It may have served other sessions at the same time, so this is an upper bound for the replay's
  own use.
- **This study made no Muse call.** The Muse figures are from its saved call results (list prices per million tokens:
  $1.25 input, $0.15 cached, $4.25 output).

## Recommendation against the bar (for the lead)

- **Qwen meets the bar, twice, with the same numbers.** On the 437 labelled executions it calls none of the 189
  labelled failures a nonfailure. Counting any reason, it misses 1, a void (the bar allows 2). Its precision,
  188/192, is 0.5 points below Muse's.
- **The margin on misses is real but thin, and the misses are of one kind:** real failures that Qwen calls
  artifacts.
  - Over the 2,115, Qwen calls an artifact on 8 of the 991 executions Muse calls failures. My blind labels make 7
    of them real failures: about 0.7%.
  - On a 189-failure sample that predicts about 1.3 misses, against the 2 allowed.
- **These misses come from gaps the PI can close without touching Qwen:** the Calendar notes on `dataOwner`, the
  bundle's hidden uploader, and the Slack notes on `conversations.history`. See "Candidates for the PI". Closing
  them would likely remove most of the misses, for either judge.
- **Qwen's errors and Muse's differ in kind, and both change the headline little.**
  - Muse credits unsent conclusions (14 times) and grades trials a replica defect decided (3). The first changes a
    score only in 2 underspecified units within the budget.
  - Qwen calls real failures artifacts (7) and once flags a correct absence report as presenting.
  - With Qwen as the judge, every policy decision and the regular suite's counts stay as published, with one real
    fact swapped for a false one.
- **For the paper's "does the judge need a strong model" question:** on the same prompt and inputs, the open 27B
  model agrees with Muse on 98.6% of 2,115 verdicts and matches the blind labels as well, within the bar. Two things
  limit the comparison: the harness around each model differs (Muse Code's wrapper against a bare chat call), and
  Muse's run-to-run variation is not measured.
- **If Qwen is adopted,** the cost of a full judging pass drops from about $63 at list price to about 18.5
  GPU-hours on the shared host, 4.6 hours of wall time at 16 in flight.

## What is not covered

- **Muse's run-to-run variation:** Muse's verdicts are single draws. Qwen's was measured once, on the labelled 437.
- **Qwen's variation outside the labelled set:** the full replay is one draw per execution, at the model's default
  sampling (temperature 1.0).
- **Purdue's Qwen:** not used. The lead moved the replay to the self-host before any Purdue call.
- **The 67 blind_review_01 executions scored mechanically:** no Muse verdict exists, so they are outside the replay
  and the bar. The same holds for the 879 final regular trials without a verdict, all mechanically clean.
- **Mechanism labels** are compared but are not part of the bar.
- **The harness around the judge:** Qwen got the judge prompt as a plain system message; Muse's Code harness and
  its instructions could not be reproduced.
- **Other judges and prompts:** the naive judges J0 and J1 were not replayed on Qwen, and the prompt was not tuned
  for Qwen.
- **The five nonfailure calls both judges make on runs without an answer** were not adjudicated, since the judges
  agree. Two are underspecified units within the budget ("Agent couldn't generate a response"), where my labels
  elsewhere say not_established.

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
| 09-30 13:50 | `headline.py` merges a duplicate pair as `decide_population` does (the PI's rule); both outputs rebuilt (session sol_score, with the lead's leave) | Offline, no model calls | With the budget rule restored in the published decisions, the code, reading attempts through its own manifest, reproduces all eight cells and the regular score exactly. The earlier outputs dated from the 8-minute budget and the rulings before the blind review. With Qwen's 1,123 verdicts, all eight decisions still match. |
| 09-30 15:46-16:48 | `sets/` from the current manifest; `compare.py --exclude-rounds`; `chain_resume.sh` | The second labelled pass, 437 executions, 16 in flight | The bar holds with identical numbers on the second draw (0 or 1 missed, precision 188/192 against Muse's 189/192); Qwen agrees with itself on 434 of 437 outcome groups, all 3 differences on executions pass 1 called void. |
| 09-30 16:48-18:56 | – | `runs/selfhost`, the other 1,005 of the current manifest (`replay run --set all` skipped the 1,110 done), 16 in flight | 1,005 verdicts at about 7.9 a minute; one answer cut at the token cap and redone. The full replay covers all 2,115. |
| 09-30 17:13-18:57 | – | Blind labels on the 16 disagreements of the resumed replay as they appeared (round `rest2`), locked 22:57:45 UTC, then unblinded | Qwen right on 9 of the 14 group disagreements, Muse on 5; the 2 within a group split. New: the Linear replica ignores a `projectMilestone` issue filter (AT-G4-LIN-21); Muse called one real failure an artifact (U-G4-BOX-13). One label's reason misstates a step; the outcome stands (adjudication README). |
| 09-30 18:58 | – | `compare.py --set all`, `headline.py` on Qwen's verdicts everywhere; offline | Qwen and Muse agree on 2,085 of 2,115 outcome groups (30 group disagreements: Qwen right on 19, Muse on 11). With Qwen as the judge, all eight policy decisions stay as published, and the regular suite keeps 139 of 563 tests and 87 facts at detect@3, with one real fact swapped for a false one. |
| 09-30 19:06-19:25 | `compare.py` writes rows one per line; `calls.jsonl` gzipped; `no_answer.py` rerun; this README | Offline, no model calls | No file of the study is over 1 MB. Over the 197 runs without an answer, Muse calls 19 a nonfailure and Qwen 7. |
