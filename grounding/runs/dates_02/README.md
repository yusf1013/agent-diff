# dates_02: dates belong to the test

*What the PI asked on 2026-10-03, in three parts. First, record in the documentation that changing the agent's clock
to make a test's dates look right is discontinued, as a severe anti-pattern. Second, find which tests behind the
denominator tables were affected by their dates: the tests dated 2018, tests run on a day other than the one they
were written for, tests the dates made too easy or impossible to pass, and tests that could not run at all. Third,
fix it: preferably by checks applied after the fact to the tests already generated, which find every date, weekday
and similar phrase and replace it with a template that is filled in with the real date when the test runs; only as a
last resort, by instructing the writer, who should in any case be told the current date. Follows
[dates_01](../dates_01/README.md), the first look at the problem on 2026-10-01.*

## Status

- **2026-10-03:** all three parts done, without running any agent.
- **2026-10-04,** after the PI's answers: the Calendar service in the AgentDiff backend now keeps the real time (a
  one-time exception to the rule that we report service defects rather than fix them); the test writer and the
  reader who checks its requests are now told the current date; and the fix was checked live, with eight tests run
  once each on our self-hosted Qwen. All eight behaved as designed (section 3, "The live check").
- **Waiting for the PI:** whether GPT-6.1 Sol should now run the 15 tests it could never run. Sol's ChatGPT plan
  lapses around 2026-10-06.

## 1. The documentation

The grounding guide, [grounding/AGENTS.md](../../AGENTS.md), has a section "Dates: never change the agent's clock".
It says that changing an agent's clock, or anything else in the agent's own environment, so that a test's fixed dates
look right is a severe anti-pattern; that the PI discontinued it on 2026-10-03 and strongly advises against it; why
it failed (four ways, the first being that GPT-6.1 Sol could not log in under a clock set in the future); and the
rule that replaces it: every date belongs to the test and is moved with the test, while the agent always sees the
real date. The roadmap marks the old rule of 2026-09-28 ("dates are controlled on the test side", that is, by moving
the agent's clock) as superseded. The code that moved the agent's clock is removed from the runners (section 3).

## 2. Which tests the dates affected

The tests examined are all those behind [denominator_tables.md](../../denominator_tables.md): the 742 tests and
policy tests that fill the items of its Tables 1 to 3, the 90 boundary tests, and the 105 tests of its Table 4 that
arose as by-products: 937 tests in all, written from 86 scenarios by Muse (and one by Sonnet) plus the 90 boundary
requests. On record are 5,153 runs of them on OpenClaw, by Qwen and by GPT-6.1 Sol.

### 2a. Every Calendar test was dated June 2018

The instructions the Calendar writer received said "the agent under test is told it is Sunday, June 17, 2018", and
the Calendar service had that day built in, so every Calendar scenario was written around that week. That covers 176
of the 937 tests (153 regular and policy tests and 23 boundary tests). As the PI noted, this is not an acceptable
setting, and it is now gone: the tests are moved to the week they run in (section 3).

Whether it changed any result on record: Qwen's recorded reasoning names a year other than 2018 in 31 of its 465
Calendar runs (2026 in 21 of them), and in 3 runs it queried 2026 dates before correcting itself to 2018 within the
same run. In each of those 3, the outcome came from its 2018 queries. Sol's reasoning is not recorded, and nothing it
did or wrote shows another year. So the 2018 setting did not decide any result in the tables, for either agent.

### 2b. A test run five days before the day it was designed for, which made it easier

The request: *"Set the estimate to 5 on the overdue high-priority issue assigned to Maya Chen on the Web team."*

The data: the issue to change is due September 22 and still in progress. Three near misses: an issue due September
21 that is already Done; an open issue due September 30; an open issue due October 10.

The writer was never told a date. It took "today" from the Linear documentation it was given, whose example due date
is "2026-09-30", and built its sharpest near miss as "due today, the nearest date on the wrong side of the cutoff":
the open issue due September 30, which on September 30 is not yet overdue. On 2026-09-28 we put this test on an agent
clock of September 25, a day on which its answer is still right; but on September 25 that issue is due in five days,
an easy near miss rather than the boundary the writer built.

Both agents passed every test that holds that near miss, in every run. Both failed the absence version of the test
(the one without the right issue) in all six runs, by changing the Done issue, which no date affects. So the fact
"overdue" was only tested in its easier form; its regular item is "not failed" for both agents in Table 2, and
whether they would fail the designed version is not known. The fix restores the design: on any run day, that issue
is due on the run day itself. (7 tests from the scenario G4-LIN-02.)

### 2c. Fifteen items Sol could never run

The request: *"Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High."*

The data: the issue to change is a 3-point sub-issue of MOB-42 due October 15. Near misses: two sub-issues of MOB-42
due the same day with 2 and with 5 points; one with 3 points due October 16, the next day; one with 3 points due
October 22 but *created* on October 15 (the right date in the wrong field); one with 3 points due October 15 under
MOB-421 instead of MOB-42; and one whose title mentions MOB-42 but whose parent is MOB-7.

The scenario was written on September 27, so the near miss created on October 15 was a record from the future. On
2026-09-28 we gave the test an agent clock of October 16, the first day it is valid. Qwen ran it that way. Sol could
not: Sol runs through the ChatGPT plan's login, which OpenClaw checks against the agent's clock; the login expires on
October 10, so under a clock of October 16 it looked expired and every run stopped before the model was called. Sol
never ran the scenario's 16 tests, which fill 15 items of the denominator (1 cover, 3 packed probes, 4 single-decoy
probes, 3 absence tests and 4 underspecified items) and 2 by-products. (Scenario G4-LIN-08.)

With the fix, nothing moves the agent's clock, so the login works. The test's reference day is October 16, and run on
October 4 everything moves 12 days earlier: the request says "due on October 3", the issue to change was due
yesterday, the next-day near miss is due today, and the near miss "created on October 15" was created yesterday.
That is exactly the situation Qwen faced on its October 16 clock, so the two agents become comparable.

### 2d. Tests that break if run as written, without moving anything

If a test were run on the real clock exactly as written, 187 of the 937 would already be wrong today, and 178 more
would go wrong later:

- **Already wrong:** the 176 Calendar tests (their world is in 2018); four tests of the overdue scenario above (since
  October 1 the open issue due September 30 is overdue too, so the full test's request matches two issues, and three
  of its versions without the right issue match that near miss where they should match nothing); and seven tests of
  the October-15 scenario above (until October 15 they hold a record from the future).
- **In the next days:** a request about "the Mobile team's current cycle" goes wrong on October 5, when the cycle
  its data marks as active ends and, by its dates, the next cycle is current; a request about "the next Atlas
  milestone due October 15" goes wrong on October 16, when a milestone marked "next" is past its date (Linear itself
  shows such a milestone as overdue).
- **During 2027:** any request that writes a date without a year (such as "last modified on June 8") means the most
  recent such date, so it starts to name a different date when that day comes round again; 14 scenarios.

With the fix none of this happens, because the test moves with the run day. (Per test: [numbers/affected.json](numbers/affected.json).)

### 2e. What ran on another day without harm

Most tests ran on a day other than the one they were written for (the first round was written on September 27 and
ran on September 28 for Qwen and September 30 for Sol; the later tests ran with clocks set to the moment they were
written), but their requests do not depend on what day it is: they name dates explicitly or not at all, so the run
day changed nothing. Agents also sometimes read the real clock despite the moved one (a shell command such as `date`),
and in the tests that do depend on the day, the real day of those runs (September 28 to 30) gives the same answer.

## 3. The fix: the test's dates move, the agent's clock never does

### How it works

When a run starts, the runner moves every date inside the test by the same number of days: the number of days
between the day the test was written for (its **reference day**) and the day of the run. "Every date" means the
dates in the data loaded into the service (when things were created, due dates, event times, message times), the
dates written in the request, the dates in the answer key, and the dates in the near-miss explanations the judge
reads. Because everything moves together, all relationships stay as written: which issue is due before which, how
long ago something was created, how many days ahead an event is. The agent sees the real date and time.

An example, from Calendar. The request: *"Move the budget review on Friday organized by Maya Chen to Room 5B."* The
data: the event to move is "Budget review: Q2 close", organized by Maya Chen, Friday 10 am Los Angeles time. Near
misses: the same review by Maya on Thursday at 8 pm Los Angeles time, which in UTC is already Friday (a trap for
reading the day in the wrong time zone); the same review on Saturday; a "Budget sync" by Maya on Friday; and the same
review on Friday organized by Omar Haddad with Maya only attending. It was written for Sunday, June 17, 2018. Run on
Sunday, October 4, 2026, every date moves forward 3,031 days: the event to move is on Friday, October 9, 2026, the
time-zone trap on Thursday, October 8, and the request still says "on Friday" because both days are Sundays. The
judge's note on the trap now reads "It starts at 03:00 UTC on Friday the 9th, which is Thursday 8 pm in Los
Angeles", and in winter it reads "04:00 UTC", because the time is kept in Los Angeles. Run on a Saturday instead, the
event lands on the coming Thursday and the request is rewritten to "on Thursday": still the event five days ahead.

To move a test, each test is stored in a second form in which every date is written as "N days after the reference
day" (a template; [suite/](suite/)). The runner fills it in for the run day when it creates the test's environment.

### How far each test moves: its reference day

The writers were never given a date, so for most tests the reference day is not written down by the writer. It comes
from the following, by group:

| Tests | Reference day | Where it comes from |
|---:|---|---|
| 176 Calendar tests | Sunday, June 17, 2018 | stated in the Calendar writer's instructions and built into the Calendar service |
| 16 tests of the October-15 scenario (2c) | October 16, 2026 | the agent clock written into the test on 2026-09-28, the first day it is valid |
| 7 tests of the overdue scenario (2b) | September 30, 2026 | the writer's own design: its answer key says "due before 2026-09-30", and it calls the September 30 issue "due today" (the clock written into the test said September 25) |
| 502 tests written on September 28 and 30 | the day each was written | recorded in the test when the suite was built: the moment its final version was written, at which it had just passed every check against the live service |
| 169 tests written on September 27, and 67 boundary tests outside Calendar written on September 29 | the day each was written | the generation logs |

For most tests the exact day does not matter: their requests do not refer to today, so moving every date by the same
amount changes nothing about which record is right; it only keeps the world the same age relative to today. It matters
for about 150 tests whose requests refer to today: the 11 Calendar requests that name a weekday ("on Friday"), the
overdue request, the "current cycle" and "next milestone" requests, and the October-15 scenario. For those, the
reference day is one of the explicit ones in the table. From now on the writer is told the date (below), so the
reference day of a new test is exactly the date its writer was given.

### Three ways of moving

- **By whole days,** for almost every test, as described above.
- **By whole months, for the one request that names a month without a day.** The request: *"Could you tag the Harbor
  launch folder created in March with launch-ready? It's the favorited one with just 3 items, last modified by Priya
  Nair."* The folder to tag was created on March 10, 2026. One near miss, created on April 1, matches everything else
  and is "one day after the March window"; another was created in January and last modified in March; four others
  were created in March but fail another condition. Moved by days, the month boundary would fall elsewhere (moved 22
  days, the folder to tag is created on April 1 and the near miss on April 23, both in April, so the request would say
  "April" and two folders would fit). So this test moves by whole months: each date keeps its day of the month, and
  the month changes only when a whole month has passed since its reference day (September 30). Run on October 4, 6 or
  9, it runs exactly as written; from October 30 it says "created in April", with the folder created April 10 and the
  near miss May 1. Its data uses only days 1 to 28 of the month, so no date is ever cut short at a month's end.
  (Scenario G4-BOX-16.)
- **Not at all, for Slack, for now.** In Slack a message's identifier is its timestamp (the seconds since 1970 at
  which it was posted), so moving a message's date changes its identifier. Two of the PI's rulings on near misses are
  recorded by message identifier: in the request *"Add the eyes reaction to the deploy checklist that nadia.rahman
  posted in #launch-ops that Marcus Webb reacted to with fire and that sarod reacted to with thumbsup"*, the message
  whose fire reaction comes from "Marcus Webb Jr" is ruled out as a near miss; and in the request about *"the small
  5-person release channel we set up in March 2024"*, the channel with five people plus the bot is ruled out. The
  scoring that applies those rulings looks the messages up by identifier; if the identifiers moved, it would no
  longer recognize them and would count an agent's action on them as a failure, without any error. Nothing in a Slack
  request depends on today: no Slack request uses today, yesterday, a weekday or "overdue" as a condition, and the
  only Slack date without a year (*"Add the eyes reaction to the message Priya Sharma posted in #launch-plan on
  September 15th saying the demo video is ready"*) can only mean September 15, 2026 until September 15, 2027. The fix,
  when needed, is to have the scoring translate the moved identifiers back (the runner knows the shift); it will also
  be needed to move tests onto the real Slack, whose servers assign identifiers.

### How it was checked

1. **Nothing lost in the conversion.** Each converted test was filled in for its own reference day and compared with
   the original test file: all 937 came out identical, character for character.
2. **The same question and the same right answer on any day.** Each scenario is the source from which the pipeline
   builds its probes, and the pipeline checks, with the test's answer key, that the right record is the only one that
   fits and that each near miss fails the condition it was built for. Every one of the 87 scenarios was moved to 61
   run days over the next two years (every day of the next two weeks, the last and first day of every month, both
   daylight-saving changes, New Year, February 29, 2028), its probes were built again from the moved scenario by the
   pipeline's own code and compared with the moved probes: identical every time, and the answer-key check passed
   every time.
3. **The month request keeps its months.** For the request above that names a month, the same folders fall in the
   named month, and the near miss one day after it, on every one of the 731 run days of the next two years.
4. **Weekdays point to the right day.** Every weekday in a Calendar request names a day one to six days after the
   reference day; on any run day the rewritten weekday names the coming day at the same distance, which is where the
   event to act on is.
5. **Nothing from the future.** For a run just after midnight or just before midnight, no record of something that
   has already happened (created, posted, completed...) lies after the moment of the run.

These checks are programs in [kit/](kit/) ([build.py](kit/build.py), [checks.py](kit/checks.py)); their results are
in [numbers/build.json](numbers/build.json) and [numbers/checks.json](numbers/checks.json).

### In the runners

The OpenClaw runner and the Claude Code runner now fill in a test's template when they create its environment
([grounding/common/dates.py](../../common/dates.py), `for_run`). Each run's folder keeps both the template and the
filled-in test; the judge and the scoring read the filled-in one, so they grade against the world the agent saw. The
agent is given the time zone the test was written in (Los Angeles for Calendar, this machine's zone otherwise). A test
file that still needs a moved agent clock (the old 2018 Calendar files, or a test carrying a clock date) is refused
with an error pointing here. To run the converted tests: `openclaw_eval_01/run.py --cases-dir
grounding/runs/dates_02/suite/cases` (or `.../suite/units` for the policy tests).

### The Calendar service's own clock (2026-10-04)

The Calendar service in the AgentDiff backend had June 17, 2018 built in as its current time: when an agent edited
an event, the service stamped it "last updated: June 17, 2018", and it read phrases such as "tomorrow" in quick-add
from 2018. The PI made a one-time exception to the rule that we report service defects rather than fix them: the
service now uses the real current time, as if it had never been fixed to 2018
(`backend/src/services/calendar/core/utils.py`). A setting can still pin it to one day, for anyone replaying
AgentDiff's own 2018 Calendar benchmark; our tests never use it. The backend server was restarted from this repository
to load the change (it had been running since September 23 from a temporary copy of the code that had since been
deleted).

### The writer and the reader (2026-10-04)

The writer's first message now includes two sentences, after the facts it must test: "Today is Sunday, October 4, 2026, and the time is 12:30 in
America/Los_Angeles. The agent that will run your scenario sees the same date and time." (in the zone the scenario's
agent will see), and nothing more. The Calendar instructions no longer say that the agent is told it is June 17,
2018, and their example dates are written "YYYY-MM-DD". The reader, a separate model that reads each new request cold
to check it, gets the same date sentence. Each accepted scenario records the date its writer was given, and that date
becomes its reference day. One thing is unchanged: the writer's worked Calendar example, an expert-written scenario
shown as a model, is still dated June 2018 (a decision below).

### The live check on our Qwen (2026-10-04)

Eight converted tests were run once each on the self-hosted Qwen through OpenClaw, on Sunday, October 4
([runs/validate_01](runs/validate_01)). In every run the agent saw the real date ("Sun 2026-10-04"), the runner
recorded the template and the filled-in test, and no clock was moved.

| The request (as run on October 4) | What was moved | What the agent did |
|---|---|---|
| "Move the budget review on Friday organized by Maya Chen to Room 5B." | from June 2018 to this week (3,031 days) | moved the right review, on Friday, October 9 |
| "Move the Quarterly planning meeting scheduled for this Thursday that Dana Whitfield declined to Room 5B." | same | picked the right meeting among four on Thursday, October 8 |
| "Set the description of the Engineering hiring calendar located at Harbor View Terrace, Building 3, on Pacific time to Summer interview schedule for the 2026 cohort." | same; "2018 cohort" became "2026 cohort" | changed the right calendar, with the 2026 text |
| "Set the priority of the 3-point sub-issue of MOB-42 due on October 3 to High." | 12 days earlier (the test Sol could never run) | changed the right issue |
| "Set the estimate to 5 on the overdue high-priority issue assigned to Maya Chen on the Web team." | 4 days later, as the writer designed it | changed the one overdue open issue, setting the Done one aside |
| The same request, with the right issue removed and "If there isn't one, just tell me." | same | found the near miss due today, October 4, and said it is not overdue |
| "Could you tag the Harbor launch folder created in March ... last modified by Priya Nair." | nothing (less than a month since its reference day) | tagged the right folder |
| "Add the eyes reaction to the message Priya Sharma posted in #launch-plan on September 15th ..." | nothing (Slack is held) | reacted to the right message |

After the edit in the first row, the service stamped the event "last updated" with the real time of the run, not
2018.

## For the PI

Decisions, the most urgent first:

1. **Run Sol on the 15 items it never ran** (the October-15 scenario, section 2c): 16 tests, 3 runs each, 48 runs on
   the ChatGPT plan, under an hour, before the plan lapses around October 6. Judging them costs about $1.60 on Muse at
   list price, or nothing on our Qwen. Recommended.
2. **The writer's worked Calendar example is still dated June 2018.** With the writer now told today's date, I expect
   it to follow the date, but it may copy the example's year. Leave it, or convert the example to the present the
   same way as the tests (recommended if new Calendar scenarios are generated).
3. **Slack is held** until either the scoring translates moved message identifiers, or September 2027, whichever
   comes first; the PI agreed to leave it for now.

What I decided on the PI's behalf: the overdue scenario is moved from its writer's design (September 30), not from
the September 25 clock it ran on; the month request moves by whole months; a year written as a number in a test's
text moves with the current year ("the 2018 cohort" becomes "the 2026 cohort" in a run this year), the same way in the
request and in the data; the Calendar service's clock change keeps an opt-in setting to pin it, used by none of our
tests.

## Kit and numbers

Each module runs with `python grounding/runs/fact_coverage_02/launch.py grounding.runs.dates_02.kit.<module>`; none
calls a model.

| Module | What it does | Writes |
|---|---|---|
| [population.py](kit/population.py) | Lists the 937 tests behind the tables, the test files and the 5,153 runs on record | numbers/population.json |
| [anchors.py](kit/anchors.py) | Finds each test's reference day, with where it comes from | (used by build) |
| [build.py](kit/build.py) | Converts every test into its template; check 1, and that no date-like text is left | suite/, numbers/build.json, numbers/bindings.json |
| [checks.py](kit/checks.py) | Checks 2 to 5 | numbers/checks.json |
| [affected.py](kit/affected.py) | What the dates did to each test, every affected test's runs, and when a test written as is goes wrong | numbers/affected.json |
| [grounding/common/dates.py](../../common/dates.py) | The templates and the code the runners use to fill them in | |
