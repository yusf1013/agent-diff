# dates_01: tests that never go stale — what happened with dates, and the proper fix

*The PI's investigation request of 2026-10-01 (afternoon): a test's dates are written as absolute literals, so running
it on another day can outdate it; the current remedy shifts the agent's clock, which broke on GPT-6.1 Sol and will
not transfer to the real services. What were the writers told, has the problem crept into the reported numbers, and
what is the complete fix? No model calls; everything below is read from the records or computed by
[kit/inventory.py](kit/inventory.py) → [numbers/inventory.json](numbers/inventory.json).*

## Status

- **2026-10-01, evening: investigated; the fix is designed and prototyped mechanically; the PI's decision is pending.**
- Nothing was run and nothing in the suites was changed.

## 1. What happened

The Linear scenario *"Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High"* was written on
2026-09-27. Its target is due October 15, 2026; its near miss for the due-date fact is a sibling-field lure — an issue
that carries October 15 in a different field, its creation date — so one record is *created* on 2026-10-15, two and a
half weeks after the writing day. Run before October 15, the world holds a record created in the future. The
2026-09-28 discussion kept such scenarios "on a clock": the test carries the instant the agent's clock starts at
(here 2026-10-16), and the harness shifts the agent's process clock to it. Four first-round scenarios run this way
(this one; "the overdue issue"; the message posted "on Tuesday"; the issue "completed on October 2"); every scenario
of the Sept 28 and Sept 30 batches got the clock of the moment it was written; Calendar has always run on a fixed
day, Sunday June 17, 2018, because its replica has that day built in.

On the self-hosted Qwen the shift costs nothing. On Sol, OpenClaw runs through the ChatGPT plan login, whose token
expires on 2026-10-10 (the store's `expires` field, in milliseconds), and OpenClaw's login code compares that expiry
with the same process clock the harness shifts: under a clock of October 16 the login looks expired, the model
cannot be resolved, and the run dies before the first model call. The scenario's 10 regular tests and 6 policy tests
— 15 items of the denominator — never ran on Sol and are counted as not run in `grounding/denominator_tables.md`.

## 2. What the writers were told about dates

- **Box, Linear, Slack: nothing about the current date.** The writer's method notes ask for "consistent dates" and
  realistic seeds, and forbid internal ids in the request ("name things as a user would: names, titles, people,
  dates"). No document names a current date, and the writer's transcript for the Linear scenario never mentions
  "today". The writer chose October 15 as a plausible upcoming due date relative to its own sense of time (it wrote
  on September 27) and then needed the same literal in a sibling field for the lure; it did not think October 15 was
  the current date — it had no current date at all.
- **Calendar: a fixed day.** The Calendar replica notes tell the writer: *"The agent is told that it is Sunday, June
  17, 2018, 00:01, America/Los_Angeles. Relative dates in requests ('this Thursday', 'tomorrow') resolve from there.
  Seeds place events in June 2018."* The replica itself has `REPLICA_NOW_RFC3339 = "2018-06-17T00:00:00-07:00"` and
  uses it as the default lower bound of `events.list` (events ending before that day are hidden unless asked for).
- **Every writer annotates its conditions.** The scenario format records each condition's phrase and the facts it
  rests on (`conditions: [{text, facts}]`), e.g. `("due on October 15", [A:Issue.dueDate])`. All 19 explicit date
  phrases in the adopted scenarios' requests sit inside a condition's text; the one date outside every condition is
  content to be written ("Retro moved to Friday, September 25"). This annotation is what makes a mechanical rewrite
  of the request possible without any new work for the writer.

## 3. Where "now" enters a test

| Where | Today | Consequence |
|---|---|---|
| **The agent's view of the date** | OpenClaw's system prompt gives only the time zone ("Current Date & Time / Time zone: America/Los_Angeles"); the agent learns the date from the timestamp OpenClaw prefixes to the user's message, "[Sun 2018-06-17 00:01 PDT]", taken from the process clock, which the harness shifts with a Node module (`fake_clock.cjs`). Claude Code's backend shifts the whole process tree with an LD_PRELOAD library. | The Node module does not reach bash, `curl` or file times: `date`, `ls -l` and HTTP `Date` headers show the real clock. |
| **The replicas** | Calendar: a built-in fixed now (above). Box, Slack, Calendar stamp writes with the real time. Linear computes a cycle's active/past/future flags from the real time when a cycle is *created* through the API; seeded cycles keep the flags the writer wrote. | With a shifted agent clock, new records are stamped in the agent's "past"; harmless for grounding. Calendar's fixed now must move with any date shift. |
| **The judge** | Never told the clock; grades from the labelled target and near-miss records. | Unaffected by either approach. |
| **The login** | The ChatGPT plan token's expiry is compared with the shifted clock. | Any test clock past 2026-10-10 cannot run on the plan. An API key has no expiry (and costs money). |

## 4. The 86 adopted scenarios, inventoried

| | Count |
|---|---:|
| Scenarios | 86 |
| Scenarios whose seed holds dates (ISO dates and datetimes, Slack message timestamps, epoch seconds) | 86 — Linear 2,374 values, Box 1,182, Calendar 1,096, Slack 901 |
| Scenarios whose reference query filters on a date | 31 |
| Requests with an explicit date phrase ("June 8", "July 15, 2026", "September 15th") | 17 requests, 19 phrases: 18 map to a seed date, 1 is content |
| Requests with a month-year phrase ("set up in March 2024") | 1 |
| Requests naming a weekday ("on Thursday") | 13 (11 Calendar) |
| Requests with a word that depends on the day ("overdue"; "the Mobile team's current cycle") | 2 |
| Records created, posted or modified after the clock the test ran with (incl. first-round scenarios on the real clock) | 0 |
| Policy units (derived requests) with a date phrase | 77; every phrase maps to the cover's seed, except the same content date |

**A whole-week shift of every date is mechanically safe for the entire suite.** The prototype shifts every
date-like value of a scenario together — seed, reference query, near-miss witnesses (Slack message ids are
timestamps), probes, expected outputs and the clock — by a whole number of weeks (weekday names stay true), in the
stated time zone for zone-aware values (wall time survives a DST boundary), then runs the derivation's own reference
check and derives the tests again. For all 86 scenarios, at three shifts (to the current week, +4 weeks, +52 weeks)
and for the clocked Linear scenario also −4 and −8 weeks: the target is still the only record selected, every near
miss is still killed by its witness, and exactly the same tests are kept and dropped.

## 5. Has it crept into the numbers in `denominator_tables.md`?

- **Yes, in one place by construction:** the 15 Sol items of the clocked Linear scenario are "filled, not run".
- **No record was ever shown created in the future:** no scenario, including the 25 first-round ones that ran on
  the real clock on Sept 28–29, has a creation-like field after the clock it ran with.
- **The real clock leaked into shifted runs, rarely:** the agent read the real clock through bash `date`, `ls -l`
  or an HTTP header in 13 of Qwen's 657 Calendar trials, 10 of its 153 clocked trials, and 2 of Sol's 462 Calendar
  trials (outcomes mixed; none voided).
- **A 2018 world fights the model's prior.** In 40 of Qwen's 657 Calendar trials the recorded reasoning treats the
  year as 2025 or 2026 despite the 2018 timestamp ("Today is Sunday, 2026-06-14. 'Friday' means the coming Friday";
  "the current date is 2026-06-17 (Wednesday), so the nearest Thursday is…"). 22 of the 40 were judged failures.
  Of the 108 trials that expose a Calendar fact for Qwen, 7 carry this confusion; **no fact's exposure rests only on
  such trials**, so the fact counts in the tables stand, while 7 of 108 Calendar exposures (6%) come from trials in
  which the agent was unsure what year it was. Sol's reasoning is not recorded, so the same check cannot be made for
  Sol (its visible text shows no such confusion).
- **The judge** was never told the clock and grades from the labelled records; its verdicts are unaffected.

## 6. The options

| Option | What it fixes | What it does not fix | Cost |
|---|---|---|---|
| **A. Keep shifting the agent's clock** (today) | Nothing new | Login expiry on the plan; the real clock leaks through bash, files and HTTP; a world dated 2018 fights the model's prior (40 confused Qwen trials); no transfer to real services; Calendar's replica now is a constant | — |
| **B. Shift the test's dates to the run day** (the renderer below) | Everything in A's list: no agent clock shim, so no login problem and no leaks; the world is in the present; the same renderer serves the transfer (the transfer study's "server-set time" rule) | Nothing known; the prototype passes 86 of 86 | Mechanical: the renderer (the prototype is most of it), the request rewrite from the writer's conditions, one Calendar replica setting; no model calls, no writer work |
| **C. A login that never expires** (an API key; the plan's token is OpenAI's) | Only the Sol symptom | Leaks, the model's prior, the transfer | Money per run |
| **D. Constrain the writers** (every date in the past, no relative words, explicit dates only) | The need for a clock on Box, Linear, Slack | Calendar (its replica has a fixed now and its requests are about upcoming events); loses natural requests ("overdue", "current cycle", "this Thursday"); a writer-side rule the PI did not want | Cheap, with a loss of realism |
| **E. Complete the clock shim** (LD_PRELOAD for OpenClaw as for Claude Code) | The leaks | The login, the prior, the transfer | Small |

## 7. The proper fix: render each test's dates to the run day

**Principle.** A scenario keeps its absolute dates and declares its anchor — the instant it was written for (its
`clock`; Calendar's June 17, 2018). When an environment is created, every date in the test is moved by the whole
number of weeks that brings the anchor into the current week, so the world is dated in the present, weekdays are
preserved, and no agent clock is touched.

**What moves together** (the prototype, `kit/inventory.py`, `shift_case`): the seed (ISO dates and datetimes,
Slack message timestamps, epoch seconds), the reference query's date filters, the near-miss witnesses where they are
timestamps, probes, cards and expected outputs, and the clock. Zone-aware values move in their stated zone, so "10
a.m. in Los Angeles" stays 10 a.m. across a DST boundary; naive and UTC values move in UTC.

**The request and the derived requests.** Each date phrase that belongs to a condition (the writer's `conditions`
annotation; 19 of 19 today) is re-rendered in the same style at the shifted date ("October 15" → "September 17");
a month-year phrase is bound to the seed date it describes and re-rendered likewise; weekday names need no change;
a date that is content to be written (1 today) is left as it is. Any phrase the renderer cannot bind stops the
build loudly — a check, not a guess. The policy units' reworded requests go through the same step.

**Verification, every build:** the reference check (the target is the only record selected; every near miss is
killed by its witness) and an identical derivation — the two checks that pass 86 of 86 today — plus "no stale
literal": every month-name phrase in a rendered request maps to a shifted seed date or is a declared content date.

**The replicas.** Calendar's built-in now becomes the environment's creation time (one constant made a
per-environment setting; a configuration change, not a replica fix). Slack's and Box's real-time stamps are then
consistent with the world. Linear's seeded cycle flags are static; a build check confirms they agree with the
anchor. The harness's leak scan stays on as a regression check and should find nothing.

**What does not change.** The writer's work (dates stay absolute; the conditions annotation already exists), the
judge, the evaluator, the existing results: a shifted test is the same test by construction (the checks prove it),
so nothing already run needs re-running. For the transfer to the real services the same renderer applies with the
transfer study's rule that a server-set time becomes the seeding time.

## 8. Immediate actions, pending the PI's word

1. **The 15 Sol items:** shift the clocked Linear scenario by −4 weeks (its clock becomes 2026-09-18, before the
   login's expiry and before today; "October 15" → "September 17" in its request and 6 unit requests; the checks
   pass), build its 16 cases and run them on Sol: 48 trials on the plan, judged for about $1.60 at list price on
   Muse (or on the self-hosted Qwen if the PI adopts it as judge).
2. **The renderer** as a build step of the suite (`materialize` → render → check), applied to every scenario at
   environment creation, with the Calendar replica setting.
3. **Writer docs:** the Calendar note changes from "the agent is told it is June 17, 2018" to "the scenario's anchor
   is June 17, 2018; tests are rendered to the run week". No other writer change.
