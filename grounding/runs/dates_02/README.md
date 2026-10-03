# dates_02: dates belong to the test

*The PI's request of 2026-10-03, in three parts. (1) Record in the documentation that shifting the agent's clock is
discontinued as a severe anti-pattern. (2) Find which tests in the denominator tables the dates affected: the 2018
tests, tests run under a "now" other than the one they were written for, tests made too easy or impossible to pass,
tests that could not run. (3) Fix it: first by deterministic checks applied retrospectively to the generated tests,
turning every date, weekday and similar phrase into a template filled in with the real date when the test runs; only
as the last resort, minimal instructions to the writer, who should be given the current date. Follows
[dates_01](../dates_01/README.md). No model was called and no agent was run; everything below is computed from the
records by the [kit](kit/) into [numbers/](numbers/).*

## Status

- **2026-10-03, done:** all three parts. The documentation is updated; the investigation covers all 937 tests behind
  [denominator_tables.md](../../denominator_tables.md) and their 5,153 trials; every one of the 937 tests has a
  verified template ([suite/](suite/)), and the OpenClaw and Claude Code runners render templates when they create a
  test's environment and refuse a test made for a shifted clock.
- **Nothing was run.** Three runs are proposed below, one of them urgent (the OpenAI plan lapses around 2026-10-06).

## 1. The documentation

[grounding/AGENTS.md](../../AGENTS.md) has a section "Dates: never change the agent's clock": shifting the agent's
clock (or anything else in the agent's environment) to make a test's dates look right is a severe anti-pattern,
discontinued by the PI on 2026-10-03, with the four ways it failed and the rule that replaces it (dates belong to the
test). The roadmap's step 8 records the decision and marks the 2026-09-28 rule "dates are controlled on the test
side" as superseded. The OpenClaw adapter's README, the runner's `case_clock`, and the Claude Code backend's clock
shim are marked discontinued, and their code paths are now removed (part 3). Commit 566f0e1eaf.

## 2. Which tests the dates affected

**The question.** Which of the tests behind the denominator tables ran under a "now" other than the one they were
written for, what did that do to them (too easy, impossible, not run), and which of them would break if run today as
written?

**The population.** The 742 tests and policy units that fill Tables 1-3 (86 covers, 195 packed probes, 131
single-decoy probes counted apart from a packed one, 187 absence units, 143 underspecified units), the 90 boundary
tests, and the 105 by-product tests and units of Table 4: 937 tests from 86 Muse scenarios (plus one Sonnet scenario
behind one by-product unit) and 90 boundary requests. Their trials on OpenClaw: 5,153 (Qwen and Sol).

**Summary.**

| What happened | Tests (Tables 1-3 + Table 4) | Effect on the reported numbers |
|---|---:|---|
| Dated June 2018 (every Calendar test, boundary tests included) | 176 | None found: the 2018 setting decided no outcome on record (below) |
| Run under a day five days before the one it was designed for, where the day matters (the overdue issue) | 7 | Its sharpest near miss was tested in an easier form; both agents passed it |
| Not run by Sol because of its date (the issue due on October 15) | 16 (15 denominator items) | 15 items "filled, not run" for Sol in Table 2 |
| Broken today if run as written on the real clock | 187 | None so far; any new run as written would be invalid |
| Broken later if run as written (next weeks; 2027) | 178 more | None so far |

Everything else ran on a day other than the one it was written for, but none of it depends on the day: the first round
was written on 2026-09-27 and ran on the real clock on 09-28 (Qwen) and 09-30 (Sol); the later batches ran with
clocks set to the moment they were written. Their requests name explicit dates or none, so the run day changed
nothing. Per-test detail, with every trial of each test the dates touched: [numbers/affected.json](numbers/affected.json).

### 2a. The 2018 tests (known; listed, not elaborated)

Every Calendar test is dated June 2018, because the Calendar writer's notes say "the agent under test is told it is
Sunday, June 17, 2018" and its replica has that day built in: 16 covers, 33 packed probes, 40 single-decoy items (24
separate tests), 30 absence units, 26 underspecified items (24 units), 23 boundary tests, and 26 by-products, 176
tests in all. All of them are now templates rendered to the run day (part 3), so they run in the present.

What the records show: Qwen's recorded reasoning names a year other than 2018 in 31 of its 465 Calendar trials (2026
in 21, 2025 in 9, 2028 in 2, 2024 in 1), and in 3 of them it queried a 2026 date before correcting itself to 2018 in
the same trial. In every one of the 3, the
outcome came from its 2018 queries. Sol's reasoning is not recorded; its actions show no 2026 query and its replies no
other year. One Qwen failure falls only on a trial with the confusion (moving the Thursday lunch on "Leo Park's
calendar" in a probe whose calendar belongs to Leo Parker), and the trial shows it failed on the name ("parker, not
park"), not the date. So the 2018 setting decided no outcome in Table 2, for either agent.

### 2b. The overdue issue: designed for one day, run under another (too easy)

*"Set the estimate to 5 on the overdue high-priority issue assigned to Maya Chen on the Web team."* The target is
due September 22 and still in progress. The near misses: an issue due September 21 that is Done; an open issue due
September 30; an open issue due October 10.

- **What the writer designed:** the writer had no date. It took "today" from the Linear documentation it was given,
  whose example due date is "2026-09-30", and built its sharpest near miss as "due today, the nearest date on the
  wrong side of the cutoff" (due September 30). Its query defines overdue as "due before 2026-09-30".
- **What ran:** the 2026-09-28 discussion put the test on a clock of September 25, a day on which its answer is still
  right. On that day the September 30 issue is due in five days: a plain future due date, not the boundary.
- **What the agents did:** both passed every test that holds that near miss, in every trial: the probe that holds it
  alone (a Table 4 by-product), the packed probe for "overdue" and the cover. Both failed the absence test in all six
  trials, on the issue that is Done, which no date moves. The "overdue" fact's regular item is "not failed" for both
  agents in Table 2 on the easier version; whether they would fail the designed one is not known.
- **What depends on it:** one fact (`D:overdue`): its packed probe and its single-decoy probes for both agents. The
  template restores the design: rendered on any day, the issue is due on that day.
- Tests: the cover, the packed probe and three single-decoy probes, the absence and underspecified units
  (G4-LIN-02; the anchor and the evidence are in [kit/anchors.py](kit/anchors.py)).

### 2c. The issue due on October 15: not run by Sol (impossible)

*"Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High."* The near miss for the due date is
an issue *created* on October 15 (the right date in the wrong field). The scenario was written on September 27, so that
record was created in the future; it ran on a clock of October 16. Sol runs through the ChatGPT plan's login, whose
expiry (October 10) OpenClaw compares with the shifted clock: under October 16 the login looks expired and the run dies
before the first model call. Sol never ran its 16 tests: 15 items of the denominator (1 cover, 3 packed probes, 4
single-decoy probes, 3 absence units, 4 underspecified items) and 2 by-products. Qwen ran them all. These are "the
15 tests we are not able to run yet". Rendered today, the record is created yesterday and the issue was due
yesterday, as on the October 16 clock, and Sol can run them now. (G4-LIN-08.)

### 2d. Broken if run as written on the real clock

Run as written, without the shim and without rendering, 187 tests are broken today and 178 more break later
([numbers/affected.json](numbers/affected.json), `stale_as_written`):

- **Today:** the 176 Calendar tests (their world is in 2018); the overdue issue's cover, packed probe, absence unit
  and the probe with the September 30 issue (since October 1 two open issues are overdue, so the cover has two matches
  and the probes one); the October-15 issue's 7 tests that hold the record created on October 15 (until that day).
- **In the coming days:** "the Mobile team's current cycle" (G4-LIN-13) from October 5, when the cycle its data flags
  as active ends and by its dates the next one is current (the cover then selects the issue in the next cycle); "the
  next Atlas milestone due October 15" (G4-LIN-21) from October 16, when its milestone still says "next" after its
  date (Linear itself shows such a milestone as overdue); the probe with the October 10 issue from October 11.
- **In 2027:** every request that writes a date without a year names a newer date once that day comes round again:
  "created in March" (from 2027-03-01) to "October 15" (from 2027-10-15), 14 scenarios.

### 2e. Not affected by the dates

- The first round's other tests ran on the real clock one day (Qwen) and three days (Sol) after they were written,
  and the later batches on clocks set to the moment they were written. None of their requests depends on the day.
- The real clock leaked into shifted runs: agents ran a command that can read the clock in 174 of Qwen's and 36 of
  Sol's Calendar trials, and a tool's output showed them the real year, 2026, in 15 and 6 of them. In the tests outside Calendar that depend on the day (the
  overdue issue, the current cycle, the October-15 issue, the next milestone), the real day (September 28 to 30) gives
  the same answer as the clock did.

## 3. The fix: every date is a template, rendered when the test runs

**The retrospective checks work for every test; the last resort (writer instructions to write templates) is not
needed.** Every date in all 937 tests is found and replaced deterministically, and the templates are verified
mechanically ([kit/build.py](kit/build.py), [kit/checks.py](kit/checks.py); the library is
[grounding/common/dates.py](../../common/dates.py)).

**What is found and templated** (55,436 tokens; [numbers/build.json](numbers/build.json)):

| Kind | Count | Example |
|---|---:|---|
| Timestamps and dates in the data, queries, near-miss witnesses and answer keys | 53,661 | `2026-10-15`, `2018-06-21T10:00:00-07:00`, Slack's `1711108800.000001` |
| Dates in words | 771 | "last modified on June 8", "September 15th", "December 2, 2026" |
| Weekdays | 480 | "on Thursday", "Thursday's deploy" |
| Years | 233 | "the 2018 cohort", "Budget 2026.pdf" |
| ISO dates inside text | 88 | a channel topic "opened 2024-03-12" |
| Months without a day | 95 | "created in March", "the April release cohort" |
| Weekday with date, "Friday the 22nd", month and year | 87 | "Thursday, June 21", "March 2024" |
| Slack timestamps in explanations; UTC clock times | 21 | "ts 1789993800.000003", "03:00 UTC" |

Left as written, on purpose: a recurring weekday ("panels meet on Fridays", one Calendar description), weekday
settings (Linear's reminder day), words already relative to now ("tomorrow", "overdue", "next week"), times of day
(wall time is kept), quarters and seasons, and UTC times in Slack messages (Slack's frame is UTC). Nothing else is
left: rendered with every token blanked out, no test contains a date-like string ([numbers/build.json](numbers/build.json),
`residue`).

**How it works.** Each test has an anchor, the day it was written for: Calendar's June 17, 2018; the overdue issue's
September 30 (the writer's design, not the September 25 clock); otherwise the test's clock or the day it was written.
Every date becomes an offset in days from that anchor; a phrase keeps its form ("June 8" stays a month and a day,
"September 15th" keeps its suffix, a weekday stays a weekday); a phrase in a record's own text binds to that record's
dates, and a near miss's explanation to the near miss's records. When the environment is created, the anchor day
becomes the run day and everything moves with it, in the zone the agent is given (Los Angeles for Calendar, this
machine's for the others), with wall times kept across daylight saving. Two exceptions:

- **A request that names a month without a day** ("the Harbor launch folder created in March", whose near miss was
  created on April 1, "one day after the March window") moves by whole months, keeping each date's day of the month,
  so the month still holds exactly the same folders. One scenario (G4-BOX-16).
- **Slack is held at its written days for now.** A Slack message's id is its timestamp, so moving the dates moves the
  ids, and two of the PI's rulings in the denominator's scenarios, the blind labels and the verdicts are keyed by
  message id. No Slack condition is read against today; its one date without a year ("the message Priya posted on
  September 15th") stays unambiguous until 2027-09-15. Moving Slack needs the scoring to map message ids first (a
  decision below).

**How it is verified, on every test:**

1. **Identity:** rendered on its anchor day, every template gives back its test exactly: 937 of 937.
2. **Same tests on any day:** every scenario's cover, rendered on 61 run days over the next two years (every day of the
   first fortnight, every month end, both daylight-saving changes, the year end, the leap day 2028-02-29) and derived
   again by the frozen derivation, keeps a clean reference check, keeps and drops exactly the same probes, and each
   derived probe equals its own rendered template: 87 of 87 scenarios on all 61 days.
3. **Month conditions kept:** for the requests that select by calendar month, the same records fall in the named month
   on all 731 run days of the next two years.
4. **Weekdays:** every weekday in a Calendar request names a day one to six days ahead of the run day, so its next
   occurrence is the target's day ("on Thursday", written for Sunday, becomes "on Wednesday" on a Saturday run, with
   the event the coming Wednesday).
5. **Nothing from the future:** no record of something done (created, posted, completed...) lies after the run's
   moment, for runs at 00:05 or at 23:55 local time: 0 tests.

**In the runners** (no agent clock anywhere): the OpenClaw runtime and the Claude Code backend call `for_run` when they
create a test's environment. A template is rendered against the real day; the attempt folder keeps the template as
`case.template.json` and the rendered test as `case.json`, which the judge and the scoring read; the agent is given the
anchor's time zone; `config.json` records the anchor, the run day and the shift. A test made for a shifted clock (one
with a `clock`, or a Calendar test dated 2018) is refused with a pointer to this study. The run driver applies the PI's
rulings to a template's written form and skips the old date limits. Tests: `grounding/tests/test_dates.py` and the
updated `test_openclaw_eval.py` (18 pass).

**The writer.** No writer change is needed for the tests on record. For new scenarios, two small changes are proposed,
not applied (the frozen pipeline is the PI's to change): give the writer the current date, and take out the example
dates in its documentation that it uses as "today" (Linear's example due date "2026-09-30" became the overdue issue's
today; Slack's example message time is "2026-09-21"; Box's default times are in June 2026; Calendar's notes say "the
agent is told it is Sunday, June 17, 2018"). The templating then runs as a pipeline step after a scenario is accepted,
with the date the writer was given as its anchor. No instruction to write templates is needed.

**The replicas (reported, not changed).** Calendar's replica keeps a fixed "now" of June 17, 2018. For worlds rendered
to the present this changes nothing in the current tests: in `events.list` it only sets the default lower bound, and
its one-year upper window applies only when recurring events are expanded (checked in the replica's code,
`list_events`), and no Calendar scenario has a recurring event. But edits are stamped "updated" in 2018, quick-add
reads "tomorrow" from 2018, and a recurring event would be expanded around 2018 when no window is given.

**Running the templates.** `openclaw_eval_01/run.py --cases-dir grounding/runs/dates_02/suite/cases` (or `.../units`
for the policy units; the boundary tests need their code oracle wired first). The judge reads the rendered `case.json`
of each attempt as it stands (`fact_coverage_02.analyze.current` swaps in references only for an identical request
and data). `openclaw_eval_01/policy.py` still writes its unit folders from the old suites; a new policy run takes the
units from `dates_02/suite/units` instead (an old Calendar or clocked unit is refused, not run wrong).

## For the PI

Decisions, the most consequential first:

1. **Run the October-15 issue's 16 tests on Sol now** (the 15 items Sol never ran). They are runnable today rendered,
   and the OpenAI plan lapses around 2026-10-06. Size: 48 trials on the plan (no token charge), under an hour;
   judged on Muse for about $1.60 at list price (dates_01's estimate), or on the self-hosted Qwen at no cost; blind
   labels first. This fills
   Sol's 15 "filled, not run" items in Table 2. My recommendation: yes, today.
2. **Rerun the overdue issue's 7 tests as designed** (the issue due on the run day), on Qwen and on Sol: 21 trials
   each, plus the 2 by-product probes. It answers whether the agents' passes on "overdue" survive the boundary near
   miss the writer designed; one fact's items (its packed probe and single-decoy probes) can change in Table 2 for
   either agent. My recommendation: yes, with run 1.
3. **The Calendar rerun in the present** (asked for on 2026-10-01): the 153 Calendar tests of the tables rendered to
   the run week, 3 trials per agent (about 460 trials each). The records suggest the 2018 setting changed no outcome,
   so this measures its effect rather than repairs a number; Sol's share must run before the plan lapses. My
   recommendation: Qwen now (no cost), Sol only if the plan allows after runs 1 and 2.
4. **Slack:** keep it held at its written days (safe until 2027-09-15), or have the scoring map message ids so Slack
   moves with the run day like the rest. The mapping is also what the transfer to the real Slack needs, where the
   server sets every message id. My recommendation: hold now, map ids before the transfer.
5. **The writer:** give it the current date and remove the documentation's example dates (above). My recommendation:
   yes, before any new generation.

What I decided on the PI's behalf, with reasons:

- The overdue issue's anchor is the writer's design (September 30), not the September 25 clock it ran on: the test is
  rendered as designed, and the clock's version is the one reported in Table 2.
- A month named without a day moves by whole months, which keeps that scenario's near miss "one day after the March
  window" exactly; the shift by days would have made it a second match or a plain miss on most days.
- Years written as numbers move with the current year ("the 2018 cohort" becomes "the 2026 cohort" in a run this year),
  the same way in the request and in the data.
- Slack is held (above); nothing else is.

**Observations.** The writers were never given a date, but they did not write in a vacuum: the example dates in their
documentation became their "today". That is how the overdue issue's boundary near miss ended up five days off once a
clock was chosen for it. Calendar's 2018 world cost less than feared in the recorded runs: Qwen hesitated over the
year in 31 trials and corrected itself every time.

## Kit and numbers

All with `python grounding/runs/fact_coverage_02/launch.py grounding.runs.dates_02.kit.<module>`:

| Module | What | Writes |
|---|---|---|
| [population.py](kit/population.py) | The 937 tests behind the tables, their case files and their 5,153 trials | numbers/population.json |
| [anchors.py](kit/anchors.py) | Each test's anchor, with the evidence | (used by build) |
| [build.py](kit/build.py) | Templates every test; identity and residue | suite/, numbers/build.json, numbers/bindings.json |
| [checks.py](kit/checks.py) | Same tests on 61 run days; month conditions on 731; weekdays; nothing from the future | numbers/checks.json |
| [affected.py](kit/affected.py) | What the dates did to each test, each trial's clock, flags and outcome; stale as written | numbers/affected.json |
| [grounding/common/dates.py](../../common/dates.py) | The templates and the renderer the runners use (`for_run`) | |
