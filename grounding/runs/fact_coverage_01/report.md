# Grounding coverage: a fact-based criterion, near-minimal covers, and what 327 Qwen episodes show

| | |
|---|---|
| Date | 2026-09-24 |
| Where | Worktree `/home/yusf/PyProj/agent-diff-coverage-claude`, branch `exp/coverage-claude` (uncommitted). Everything is in `grounding/runs/fact_coverage_01/`, and all links below are relative to that folder. |
| Solver | Purdue GenAI `qwen3.8:27b` with the benchmark's standard prompt and a 40-turn / 480-second episode. The previously recorded `qwen3.6:27b` is no longer served by Purdue. |
| Evidence | 327 scored episodes (179 distinct cases) on new Box, Calendar and Linear cases, plus 17 completed reruns of 11 earlier Slack cases. Every failure cited here was read in its trajectory, final answer and state diff. |
| Status | Pilot complete. The criterion and catalogs are a proposal backed by one model and 1–3 trials per condition. They are not a validated final benchmark. All cases and judgments are manual research work. |

This report is meant to be read on its own. Companion files are only needed for detail:
- [criterion.md](criterion.md): the definition on one page;
- [findings.md](findings.md): the run-by-run log, in the order the experiments happened;
- [README.md](README.md): directory map and commands.

---

## Contents

1. [Summary](#1-summary)
2. [The question and the constraints](#2-the-question-and-the-constraints)
3. [Starting point: what was already known](#3-starting-point-what-was-already-known)
4. [The criterion: fact-discrimination coverage](#4-the-criterion-fact-discrimination-coverage)
5. [The catalogs: how many requirements](#5-the-catalogs-how-many-requirements)
6. [How the tests were built, run and judged](#6-how-the-tests-were-built-run-and-judged)
7. [Results](#7-results)
8. [Cover size and redundancy](#8-cover-size-and-redundancy)
9. [What makes a coverage dimension meaningful](#9-what-makes-a-coverage-dimension-meaningful)
10. [Limitations](#10-limitations)
11. [Next steps](#11-next-steps)
12. [How the work unfolded](#12-how-the-work-unfolded)
- [Appendix A: the four catalogs](#appendix-a-the-four-catalogs)
- [Appendix B: the pilot cover cases](#appendix-b-the-pilot-cover-cases)
- [Appendix C: per-fact results](#appendix-c-per-fact-results)
- [Appendix D: files, sources and reproduction](#appendix-d-files-sources-and-reproduction)
- [Appendix E: glossary](#appendix-e-glossary)

---

## 1. Summary

**The question.** What coverage criterion makes grounding tests meaningful, and how do we build a small cover for it
across Slack, Box, Calendar and Linear?

**The answer, in four parts.**

1. **Count facts of the domain model, linearly.**
   - A requirement is one fact that an ordinary request can use to identify something and that the agent can observe.
   - Facts come in five kinds: an attribute, a relationship role, a hierarchy level, a "these conditions must hold on one
     record" constraint (binding), or a derived view such as "one occurrence of a recurring event".
   - This gives **Slack 34, Box 60, Calendar 40, Linear 121** requirements, 255 in total.
   - Route-based spaces over the same models reach 5.9×10¹⁰ read-screened routes (Linear).
2. **A test covers a fact only if it contains a near-miss built from the fact's designated alternative.**
   - The designated alternative is what an agent could plausibly substitute: created instead of owned, the reversed
     direction of a relation, the other level of a hierarchy, conditions split across two related records, UTC instead
     of local time.
   - Each claim is checked mechanically by running the intended selection and the substituted one on the test data.
3. **Resolution mode is not a coverage dimension.**
   - When a request presupposes something that does not exist, Qwen acts on a partial match and reports it as the match,
     whichever condition is missing (46 of 48 runs). It even takes an .xlsx file for "the PDF".
   - That is one generic habit. It gets a small fixed policy panel per domain (about 3 tests), not a copy per fact.
   - Fact credit is given only when the target is present or the request permits "there is none".
4. **A near-minimal cover packs 3–5 facts into one natural request.**
   - The pilot's covers are irredundant: the exact minimum equals the number of cases, or one fewer.
   - At the observed density, full covers would need about 14 Box, 14 Calendar and 35 Linear tests.
   - Add roughly 10 Slack tests (extrapolated) and 3 policy tests per domain: about 85 tests in total, i.e. high tens.

**What the runs showed about the agent.**

- **Bug count.** The 327 episodes are 179 distinct cases built from 37 scenarios. Counting one bug per failed
  requirement, they exposed **16 distinct bugs** plus **1 policy bug** (§7.8). 6 of the 16 were reproduced; 10 were
  seen once.
- With the no-match habit neutralized, near-misses built from designated alternatives were acted on in **10 of 26**
  runs, plain near-misses for the same nine facts in **1 of 27**. The alternative is what makes a fact meaningful.
- The genuine fact-level weaknesses are few and recurrent. They fall into three families:
  - **person roles conflated**: "created" read as organizer (9/9) or owner (5/9), "assigned" read as "created" (2/3);
  - **containment taken as membership**:
    - a file inside a collected folder counted as "in Favorites" (2/2);
    - a hub counted as including a folder because it holds that folder's parent (3/12);
  - **representation misread**:
    - a Linear "blocked by" relation handled as "blocks" (13/13, including 3/3 with the correct relation present);
    - a UTC time read as the local day;
    - a renamed calendar confused with one whose real name matches.
- Most facts held. Of the 59 facts for which Qwen demonstrably looked at the near-miss, **43 never failed**.
- Spelling the relation out in the request cured two weak facts (folder creator, hub inclusion). It did not cure event
  creator or relation direction: there Qwen read the evidence correctly and acted against it.

---

## 2. The question and the constraints

The research question, as you posed it: *what would be a good coverage criterion, and how would we design the minimal or
near-minimal cover of its requirements?* The constraints you set:

- **Meaningful dimensions.** The criterion may be simple (linear coverage is acceptable), but failures should relate to
  facts of the domain model. Facts need not be entities or routes.
- **Scale.** High tens to a few hundred requirements per domain, or a requirement space whose cover needs that many
  tests.
- **No redundancy.** Never more tests than requirements; one test may cover several requirements.
- **No meaningless multipliers.** In the earlier 57-case Slack pilot, most failures came from setting the resolution mode
  to *underspecified*. Failures there looked like repeated reproductions of one behaviour.
- **Way of working.** Work autonomously. Run many tests on Qwen (free, 60 requests/minute) and learn from the results,
  not from plumbing. Limitations of the mock are not agent bugs, and cataloguing them is not the goal.

---

## 3. Starting point: what was already known

### 3.1 The adopted domain models

The four replicas have manually extracted conceptual models (entities, relationship roles, attributes, states, derived
views, API observability):
[Slack](../../domains/slack/model.md), [Box](../../domains/box/model.md), [Calendar](../../domains/calendar/model.md),
[Linear](../../domains/linear/model.md). They are compared in [route_comparison.md](../../domains/route_comparison.md):

| Domain | Entities | Relationship roles | Structural routes | Read-screened routes |
|---|---:|---:|---:|---:|
| Slack | 13 | 20 | 2,870 | 212 (174 after an ordinary-request review) |
| Box | 10 | 29 | 12,398 | 6,500 |
| Calendar | 7 | 10 | 168 | 30 |
| Linear | 49 | 159 | 989,643,546,920 | 58,820,072,198 |

Counting every route as a requirement works for Slack and is impossible for Linear: the explosion you anticipated.

### 3.2 The evaluation plan's coverage space

[evaluation_plan.md](../../protocols/evaluation_plan.md) defined the space as *referent entity × focal identifying
attribute/path × resolution mode* (absent, single, multiple, underspecified). For Slack this became 174 complete routes,
26 identifying attributes, 28 entity–mode requirements and 25 capability limitations
([catalog.md](../../domains/slack/coverage/catalog.md),
[route redundancy analysis](../../domains/slack/coverage/route_redundancy_analysis.md)).

### 3.3 The 57-case manual Slack suite and the three-model pilot

**The suite.** [manual_exemplars_01](../manual_exemplars_01/README.md) has 10 scenario families (W01–W10) and 57
cases: 10 single, 10 multiple, 11 absent and 26 underspecified. It was run once each on Sonnet 5, Haiku 4.5 and
Qwen 3.6 27B ([Claude comparison](../manual_comparison_01/report.md), [Qwen comparison](../purdue_comparison_01/report.md)).

**Codex's secondary analysis**
([manual_findings.md](../../campaigns/coverage_codex_01/manual_findings.md)) found:

- **98 demonstrated grounding errors in 171 episodes.** 75 of them (76.5%) were on underspecified cases, which fail
  almost always.
- **15 genuine selection errors with real records** among the 23 other errors:
  - relationship substitution (8), e.g. W08, where a message *located* in the named channel was taken for one *written
    by a member* of it;
  - conditions joined across different records (1): one person's reaction plus another person's emoji;
  - a selection condition discarded (6).

  The remaining 8 errors were invented evidence.
- **Minimum covers can differ wildly in what they expose.** Under a simple linear comparator (26 requirements), the
  exact minimum cover has 7 cases. Different 7-case minimum covers contained between 3 and 18 incorrect episodes, out
  of 21 (7 cases × 3 models). So the criterion alone did not determine how much a cover exposes.

**Implication.** Even before any new run, resolution mode dominated the counts while the diagnostic signal sat in
relational confusions. We needed a criterion that ties requirements to model facts without multiplying them by modes.

---

## 4. The criterion: fact-discrimination coverage

### 4.1 Requirement = one model fact

| Kind | Fact | Example (pilot) |
|---|---|---|
| **A** attribute | an identifying value: identity, text, time, quantity or state | `File.extension`, `Event.start`, `Issue.priority`, `Event.creator_email` |
| **R** relationship | a role connecting the referent to its evidence | `File.owned_by_id`, `IssueRelation.issueId`, `TeamMembership` |
| **H** hierarchy | a self-relationship level | `Folder.parent_id` (direct vs nested), `Issue.parentId`, `Event.recurring_event_id` |
| **B** binding | conditions that must hold on the *same* related record | an attendee *and* their response on one attendee record |
| **D** derived | a computed view with an ordinary use | one occurrence of a series, the local calendar day, the current cycle |

Each requirement is counted once, however many routes, modes or other facts it could combine with.

### 4.2 Designated alternatives

Every fact comes with the confusions an agent could plausibly make, derived from the model:

| Kind | Designated alternative | Pilot example |
|---|---|---|
| R | a sibling role between the same entities, or a short alternative connection | owner ↔ creator ↔ last modifier; organizer ↔ attendee; the reversed direction of a relation; message location ↔ author's membership |
| A | a sibling attribute of the same entity and kind; for states, another value | name ↔ description; handle ↔ real name; start ↔ end; summary override ↔ summary |
| H | the other level | nested ↔ direct; reply ↔ replied-to; exception ↔ series master; parent team ↔ sub-team |
| B | the conditions split across two records | a file with Priya's hiring comment and Omar's travel comment |
| D | the neighbouring representation | the series master for one occurrence; the UTC day for the local day; the next cycle for the current one |

Sibling attributes are derived mechanically (same entity, same kind). Roles and representations were chosen by hand
from the model. About two thirds of each catalog has a designated alternative (§5.1).

### 4.3 The credit rule

A test covers fact *f* when one of its references uses *f* and both conditions hold:

1. **The seed contains a near-miss through f's alternative.**
   - The near-miss satisfies every other condition.
   - It is selected when *f* is replaced by its alternative (or dropped), and not selected by the intended selection.
   - Both selections are executed on the seed by [fdc.py](fdc.py). A claim that does not change the result earns
     nothing, and each near-miss can credit only one fact.
2. **The test is in a fact-sensitive form.**
   - Either the target is present, so the near-miss competes with it,
   - or no target exists and the request permits reporting that.
   - A request that presupposes a match which does not exist earns no fact credit. There, the agent's choice is driven
     by a generic habit (§7.2).

**Worked example (BOX-01).** Request: *"Add the tag q3-close to the PDF that Maya Chen owns directly in the Finance
Reports folder (not in its subfolders) and that Leo Park modified last."*
([case](pilot/cases/box/BOX-01.json), [design](pilot/cases_box.py))

| File | Folder | Owner | Creator | Last modifier | Role in the test |
|---|---|---|---|---|---|
| Q3 revenue summary.pdf | Finance Reports | Maya Chen | Dana | Leo | **target** |
| Q3 expense summary.pdf | Finance Reports | Dana | Maya Chen | Leo | near-miss for *owner* (alternative: creator) |
| Q3 revenue summary.xlsx | Finance Reports | Maya Chen | Maya Chen | Leo | near-miss for *file type* |
| Q3 forecast.pdf | Finance Reports/Drafts | Maya Chen | Maya Chen | Leo | near-miss for *direct containment* (alternative: nested) |
| Q3 payroll summary.pdf | Finance Reports | Maya Chen | Leo | Maya Chen | near-miss for *last modifier* (alternative: creator) |
| Q3 vendor summary.pdf | Finance Archive | Maya Chen | Maya Chen | Leo | near-miss for *folder name* |
| Q3 travel summary.pdf | Finance Reports | Maya Lopez | Maya Lopez | Leo | near-miss for *person name* |

(The seed also contains one unrelated Dana file.) The checker executes the reference query and six mutants, and all six
claims pass, so this one natural request credits six facts. [build.py](pilot/build.py) re-runs every claim of every
case, and a sanity test confirmed that deliberately wrong claims are rejected.

### 4.4 Policy panel

Resolution behaviour is measured once per domain, not per fact. The panel has about 3 tests per domain:

- a presupposed no-match with a one-condition near-miss;
- far misses: one missing several relational conditions, one missing a type condition;
- an unresolved choice (underspecified) and a collection request.

### 4.5 Relation to established criteria

The credit rule borrows two established ideas and applies them to the facts of a conceptual model instead of to code or
SQL text:
- the independence idea of MC/DC: each condition must be shown to change the outcome on its own;
- the kill condition of SQL mutation testing: a test database kills a mutant query when their results differ.

---

## 5. The catalogs: how many requirements

### 5.1 Counts

Built by [catalog/build.py](catalog/build.py) from the curated inventories in [catalog/facts.py](catalog/facts.py).
Generated tables are in [catalog/counts.md](catalog/counts.md) and per-domain JSON in [catalog/](catalog/).

| Domain | A | R | H | B | D | **Total** | With a designated alternative |
|---|---:|---:|---:|---:|---:|---:|---:|
| Slack | 20 | 4 | 1 | 4 | 5 | **34** | 22 (65%) |
| Box | 31 | 19 | 2 | 5 | 3 | **60** | 45 (75%) |
| Calendar | 28 | 4 | 1 | 3 | 4 | **40** | 25 (62%) |
| Linear | 63 | 38 | 5 | 12 | 3 | **121** | 80 (66%) |
| **All** | 142 | 65 | 9 | 24 | 15 | **255** | 172 (67%) |

Attribute subkinds (identity / text / time / quantity / state): Slack 5/5/2/0/8, Box 6/7/8/3/7, Calendar 8/4/2/0/14,
Linear 19/8/11/3/22. The facts without an alternative are mostly state and type flags. Those held in every fact-sensitive
test that looked at them (§7.6).

### 5.2 How the catalogs were derived

- **Full accounting.** Every stored column of an included entity and every model relationship gets a disposition, and
  the builder fails if anything is unaccounted for. That is 40 Slack, 170 Box, 106 Calendar and 472 Linear columns, and
  22 / 29 / 10 / 159 relationships.
- **Exclusion categories.**
  - storage handles and foreign keys (the latter are represented as R facts);
  - constants and bookkeeping (etags, hashes, sort orders, caches);
  - presentation (colors, icons, URLs) and configuration flags;
  - uninterpreted JSON and unexposed fields;
  - API-filtered states (e.g., Box returns only non-trashed items);
  - aliases of an included fact;
  - fields judged not to be ordinary identifying conditions.
- **Excluded entities, with reasons per entity in [facts.py](catalog/facts.py).**
  - **Slack (9 tables):**
    - the workspace (single-workspace scope);
    - named roles, role assignments, files, file attachments, stored mentions and edit records (no API access);
    - workspace and user settings (unexposed).
  - **Box (1):** file version history (not readable).
  - **Calendar (2):** users (no directory; people appear as email values) and stored reminder records (unused by the
    API).
  - **Linear (29):**
    - Organization (single scope), ExternalUser (integration identities) and ProjectLabel (its project link is not
      readable);
    - DocumentContent (content is kept as a Document attribute), Post, IssueImport and OrganizationDomain;
    - Reaction (no emoji or user stored) and 21 other minimal records without identifying content (Favorite, Draft,
      Template, Webhook, histories, …).
- **One exclusion came from testing: Box `Collection.name`.** The replica supports only the single Favorites collection
  ([operations.py](../../../backend/src/services/box/database/operations.py#L1935)), and a second collection made
  `GET /collections` fail in a pilot preflight. So the attribute cannot discriminate anything.

### 5.3 Comparison with route-based spaces

| Domain | FDC requirements | Read-screened routes | Read-screened routes of ≤ 3 edges | Entity × route × mode | All fact pairs |
|---|---:|---:|---:|---:|---:|
| Slack | 34 | 212 (174 reviewed) | — | 696 | 561 |
| Box | 60 | 6,500 | 1,146 | 26,000 | 1,770 |
| Calendar | 40 | 30 | 28 | 120 | 780 |
| Linear | 121 | 58,820,072,198 | 23,372 | 2.35×10¹¹ | 7,260 |

Full fact lists are in [Appendix A](#appendix-a-the-four-catalogs).

---

## 6. How the tests were built, run and judged

### 6.1 Anatomy of a case

Each case is a JSON file ([example](pilot/cases/linear/LIN-04.json)).

**What the solver sees:** the request, the acting user and a fresh seed.

**What it does not see:**
- **references**, one per thing to resolve, each with its reference query, expected referents and credit claims;
- grounding **cards** and **task specifications** in the existing locked schema, so the custom evaluator can consume
  them later;
- read **probes** that check each near-miss is observable through the API.

Cases are written in Python ([cases_box.py](pilot/cases_box.py), [cases_calendar.py](pilot/cases_calendar.py),
[cases_linear.py](pilot/cases_linear.py)) with shared helpers ([common.py](pilot/common.py)). They are emitted by
[build.py](pilot/build.py), which also runs every credit check. 263 cases are built; 179 of them were run.

### 6.2 The pilot cover cases

There are 32 packed cover cases: 9 Box, 9 Calendar and 14 Linear, each crediting 1–7 facts. Their requests are listed
in [Appendix B](#appendix-b-the-pilot-cover-cases). No new Slack cases were built; Slack relies on the earlier suite
plus reruns.

### 6.3 Experimental variants

The cover cases answer *what is covered*; the variants answer *what exposes failures*. Each variant is a small
transformation of a cover case ([variants.py](pilot/variants.py)).

| Variant | Construction | Question it answers | Built | Run |
|---|---|---|---:|---:|
| Target flip (`-A`, `-P`) | remove the target rows, or add one | does the resolution form change the outcome? | 31 | 25 |
| Isolated (`-I<r><k>`) | keep one near-miss; remove the target and all other near-misses | is each fact exposed on its own? | 97 | 22 |
| Plain (`-PLAIN`) | the near-miss fails the condition *without* the tempting alternative | does the alternative matter? | 4 | 4 |
| Far (`-FAR`) | leave only candidates missing several conditions | how far does the no-match habit reach? | 3 | 3 |
| Told (`-TOLD`) | append "If there isn't one, just tell me." to a no-target request | what remains once the presupposition is removed? | 31 | 31 |
| Contrast (`CON-`) | isolated + told, in ALT and PLAIN versions differing only in the near-miss row | alternative vs plain, cleanly | 18 | 18 |
| ALT sweep (`ALT-`) | isolated + told, for every claim that has an alternative | which alternatives does Qwen confuse? | 33 | 33 |
| Wording (`WRD-`) | the four weakest facts, with the relation spelled out | reading the phrase vs reading the data | 4 | 4 |
| Arrangement | new cases: hierarchy direction/level, and the W08 shape in other domains (plus 4 flips) | do Slack's and Linear's weak spots generalize? | 10 | 8 |

### 6.4 Execution

**Harness.**
- Box, Calendar and Linear cases install their own seed through a new adapter,
  [custom_runtime.py](../../integrations/agentdiff/custom_runtime.py). It reuses the backend seed scripts, records the
  read probes and installed state, and runs the unchanged episode loop of
  [smoke_runtime.py](../../integrations/agentdiff/smoke_runtime.py).
- Slack reruns use the unchanged Purdue runner, with only the model name overridden ([slack_bridge.py](pilot/slack_bridge.py)).
- The pilot runner is [run.py](pilot/run.py).

**Settings.**
- Same as the recorded comparison ([solver README](../../solver/README.md)): standard prompt, provider defaults, 16,384
  output tokens per call, 40 turns, 480 seconds, shared 60-requests/minute limiter.
- The Calendar prompt fixes "now" at Sunday 2018-06-17 00:01 Los Angeles
  ([notebook](../../../experiments/kdd%202026/agent-diff%20bench.ipynb)), so Calendar cases use June 2018 dates.

**Volume.**
- **Custom-seed attempts: 622.** All are kept, none of the unfinished ones is scored:
  - completed: 333 (303 finished, 29 hit the time limit, 1 hit the turn limit);
  - infrastructure errors: 133, mostly Purdue rate limits;
  - interrupted while lanes were reprioritized: 156 (131 before the solver started, 25 during the run).
- **Scored episodes: 327**, the latest completed attempt per (run, case): 303 finished, 23 timed out, 1 hit the turn
  limit. Six timed-out attempts were retried; the retry is scored, and the timed-out attempt is kept on disk.
- **Slack reruns:** 19 attempts, of which 17 completed.
- **Usage, as reported by the Purdue API:** 2,798 model requests, 14.08 M input tokens and 0.77 M output tokens (custom
  runs 2,655 requests, 13.29 M / 0.74 M; Slack reruns 143, 0.79 M / 0.04 M).
  - No cache usage was reported.
  - Usage is missing for the 25 attempts interrupted mid-run.
  - Cost is 0: Purdue does not charge per token.
- **Fixture checks:** 87 no-model checks (`prepare_*` runs, 54 passed) installed seeds and ran the read probes without
  calling the model.

### 6.5 Judging

1. **Automatic attribution** ([analyze.py](pilot/analyze.py), [results.py](pilot/results.py)).
   - The state diff shows which records the agent changed.
   - Changing a near-miss is attributed to that near-miss's fact. Changing any other non-target goes into an "other"
     bucket.
   - A no-target run counts as correct only if it finished and the answer reports absence.
2. **Manual reading.** Every failure cited in this report was read in its trajectory and answer
   ([show.py](pilot/show.py) prints one).
   - Corrections are in [manual_labels.json](pilot/manual_labels.json), with a note for each. Examples: an answer
     naming people only to exclude them; an action that was noticed and reverted.
   - Final rows are in [results.json](pilot/results.json).
3. **Mock artifacts excluded, not counted.**
   - A Linear `issues(filter: {parent})` argument that the mock ignores (LIN-10 is marked invalid);
   - a Box `DELETE /tasks` that returns 500 (BOX-03 was changed to a due-date update);
   - a Linear project status the mock does not return (LIN-08 was not run).

   Mock limitations are not agent failures.

---

## 7. Results

### 7.1 The form of the test decides what is measured

| Form | Acted on a wrong record | What it measures |
|---|---:|---|
| Target present | **4/60** (all Linear) | misreading with the answer available |
| No target, request presupposes a match | **46/48** (96%) | one generic no-match habit |
| No target, "If there isn't one, just tell me" | **33/180** (18%) | fact-specific confusions, concentrated on alternatives |

Breakdown by design and domain, produced by [report_data.py](pilot/report_data.py):

| Design | Box | Calendar | Linear | Total |
|---|---:|---:|---:|---:|
| Target present | 0/21 | 0/15 | 4/24 | 4/60 |
| Packed, presupposing, no target | 11/11 | 5/5 | 6/6 | 22/22 |
| Isolated, presupposing | 12/13 | — | 8/9 | 20/22 |
| Plain, presupposing | 4/4 | — | — | 4/4 |
| Packed, told | 2/20 | 2/16 | 3/25 | 7/61 |
| Contrast ALT, told | 4/17 | 3/6 | 3/3 | 10/26 |
| Contrast PLAIN, told | 1/18 | 0/6 | 0/3 | 1/27 |
| ALT sweep, told | 7/22 | 4/20 | 4/24 | 15/66 |
| *Far miss, presupposing* | *3/4* | — | — | *3/4* |
| *Wording probe, told* | *0/6* | *3/3* | *3/3* | *6/12* |

Each cell is wrong actions over runs with a clear outcome. Runs without a clear outcome (timed out without acting,
incomplete, unclear or invalid) are not in the denominators: 23 in total, listed per condition by `report_data.py`. The last two rows are probes discussed in
§7.2 and §7.5 and are not part of the three form totals.

### 7.2 The no-match habit is generic

With a presupposing request and one near-miss, Qwen acted on it (20/22) for nearly any unmet condition, including type
and identity:

- **The .xlsx for "the PDF":** *Successfully added the tag "q3-close" to the file "Q3 revenue summary.xlsx" (ID: 1003),
  which is owned by Maya Chen, directly in the Finance Reports folder, and last modified by Leo Park*
  ([BOX-01-A-I12](pilot/runs/qwen_box_iso_t1/BOX-01-A-I12/attempt-04/solver/final_response.md)).
- **Another Maya, stated openly and tagged anyway:** *… "Q3 travel summary.pdf" (ID: 1007), which is the PDF directly in
  the Finance Reports folder (ID: 100) owned by Maya Lopez and last modified by Leo Park*
  ([BOX-01-A-I16](pilot/runs/qwen_box_iso_t1/BOX-01-A-I16/attempt-04/solver/final_response.md)). The request named
  Maya Chen.
- **A completion task for "the review task"**
  ([BOX-03-A-I11](pilot/runs/qwen_box_iso_t1/BOX-03-A-I11/attempt-03/solver/final_response.md)).
- **A Linear issue of the wrong priority, label or team.** One answer called a non-high-priority issue *"a
  high-priority bug assigned to Priya Nair"*
  ([LIN-01-A-I12](pilot/runs/qwen_linear_ctrl_t1/LIN-01-A-I12/attempt-02/solver/final_response.md)).

The two refusals:
- a PDF that exists only in another folder
  ([BOX-01-A-I15](pilot/runs/qwen_box_iso_t1/BOX-01-A-I15/attempt-04/solver/final_response.md));
- a comment by another author
  ([LIN-02-I12](pilot/runs/qwen_linear_ctrl_t1/LIN-02-I12/attempt-02/solver/final_response.md)).

Plain near-misses were also taken (4/4, [runs](pilot/runs/qwen_box_plain_t1/)), so in this form the alternative does not
matter.

**Far misses** (presupposing request; only candidates that miss several conditions):

| Case | What is left in the seed | Outcome |
|---|---|---|
| [BOX-01-A-FAR](pilot/runs/qwen_controls_t4/BOX-01-A-FAR/attempt-01/solver/final_response.md) | a Dana-owned .docx | refused in the one completed run: *"I did not apply the "q3-close" tag to avoid incorrectly modifying an unintended file"*; two runs timed out while still searching |
| [BOX-04-FAR](pilot/runs/qwen_controls_t4/BOX-04-FAR/attempt-01/solver/final_response.md) | Dana's hub holding an unrelated folder | used that hub in both completed runs. In one it also added the "Launch assets" folder to the hub, which made the request's condition true after the fact: *"The hub now contains three folders: Q4 campaign, Launch assets, and Brand guidelines."* |
| [BOX-06-FAR](pilot/runs/qwen_controls_t4/BOX-06-FAR/attempt-01/solver/final_response.md) | a folder created by Dana, tagged internal, described as Borealis, owned by Sam | tagged it in the one completed run: *"This folder is owned by Sam Rivera …"* (the request said Sam *created* it); one run timed out |

So the habit tolerated several unmet conditions at once, relational ones and secondary attributes such as tag and
description (3 of 3 completed runs). It was blocked by the unmet type condition in that condition's only completed run.

**Absence permitted.** One added sentence makes the same seeds mostly pass. For example:
*"There is no such file. Among the three PDFs directly in the Finance Reports folder: Q3 expense summary.pdf – owned by
Dana Whitfield (modified by Leo Park) …"*
([BOX-01-A-TOLD](pilot/runs/qwen_controls_t1/BOX-01-A-TOLD/attempt-01/solver/final_response.md), 3 of 4 trials).
Similarly, *"There is no hub that matches both criteria"*
([BOX-04-TOLD](pilot/runs/qwen_controls_t1/BOX-04-TOLD/attempt-01/solver/final_response.md), 4 of 4 trials).

This is the same redundancy the underspecified Slack cases showed. Per-fact tests in the presupposing form re-measure
one behaviour, so the criterion measures that behaviour once in the policy panel and gives fact credit only in
fact-sensitive forms.

### 7.3 Designated alternatives, not plain misses, expose fact-level failures

Contrast pairs have one near-miss, no target, and permitted absence. The ALT and PLAIN versions differ only in the
near-miss row ([cases_contrast.py](pilot/cases_contrast.py); runs [t1](pilot/runs/qwen_contrast_t1/),
[t2](pilot/runs/qwen_contrast_t2/), [t3](pilot/runs/qwen_contrast_t3/)).

| Fact | ALT near-miss | ALT acted | PLAIN near-miss | PLAIN acted |
|---|---|---:|---|---:|
| relation direction | ENG-7 *blocks* the migration issue | **3/3** | the migration issue blocks another issue | 0/3 |
| event creator | Maya *organizes* the offsite; Sam created it | **3/3** | Sam organized and created it | 0/3 |
| folder creator | Sam *owns* the folder; Dana created it | **2/2** | Dana owns and created it | 1/3 |
| hub inclusion | Leo's hub includes the folder that *contains* Launch assets | **2/3** | Leo's hub holds only an unrelated folder | 0/3 |
| file owner | Maya *created* the file; Dana owns it | 0/3 | Dana created and owns it | 0/3 |
| file last modifier | Leo *created* it; Maya modified it last | 0/3 | Dana created it | 0/3 |
| task creator | Dana *assigned* it; Sam created it | 0/3 | Sam created and assigned it | 0/3 |
| folder description | the name says Atlas, the description says Borealis | 0/3 | the name no longer mentions Atlas | 0/3 |
| attendee role | Priya *organizes* the review; Omar declined | 0/3 | Dana organizes it; Priya is not involved | 0/3 |
| **Total** | | **10/26** | | **1/27** |

The single PLAIN failure silently leaves out the unmet condition
([CON-folder-creator-plain t2](pilot/runs/qwen_contrast_t2/CON-folder-creator-plain/attempt-01/solver/final_response.md)):
the generic habit leaking through the permission. The ALT failures instead restate the alternative as a match. For
example: *"It matches all the criteria: Owned by: Sam Rivera …"*
([CON-folder-creator-alt t1](pilot/runs/qwen_contrast_t1/CON-folder-creator-alt/attempt-01/solver/final_response.md)).

### 7.4 The fact-level weaknesses form three families

These counts come from all fact-sensitive runs, counting a run only when the near-miss was the sole candidate or was
explicitly fetched ([held.py](pilot/held.py); the per-fact table is in [Appendix C](#appendix-c-per-fact-results)). In
each failure, the answer restates the alternative as if it satisfied the request.

**Person roles conflated.**

| Fact (designated alternative) | Failed / runs | Qwen's words (link) |
|---|---:|---|
| event creator (organizer) | 9/9 | *"organized by Maya Chen (created by Sam Rivera). Successfully made Omar Haddad an optional attendee"*, for "the offsite that Maya Chen created" ([WRD-event-creator](pilot/runs/qwen_wording_t1/WRD-event-creator/attempt-01/solver/final_response.md)) |
| folder creator (owner) | 5/9 | *"This folder directly under Projects is owned by Sam Rivera"*, for "Sam Rivera created" ([BOX-06-TOLD](pilot/runs/qwen_told_t1/BOX-06-TOLD/attempt-01/solver/final_response.md)) |
| task assigner (creator) | 2/3 | *"an open review task due 2026-09-20 … created by Dana Whitfield and assigned to two people"*, for "which Dana Whitfield assigned"; Sam made the assignments ([ALT-BOX-08-A-I15](pilot/runs/qwen_altsweep_t2/ALT-BOX-08-A-I15/attempt-01/solver/final_response.md)) |
| file last modifier (creator) | 1/11 | *"owned by Maya Chen and was created/modified by Leo Park"*; Leo only created it ([BOX-01-A-TOLD t2](pilot/runs/qwen_controls_t2/BOX-01-A-TOLD/attempt-01/solver/final_response.md)) |

**Containment taken as membership.**

| Fact (designated alternative) | Failed / runs | Qwen's words (link) |
|---|---:|---|
| collection, via a collected folder | 2/2 | *"Found one locked spreadsheet in your Favorites collection: "Pack summary.xlsx" (inside the "Budget pack" folder)"*; only the folder is in Favorites ([ALT-BOX-05-A-I11](pilot/runs/qwen_altsweep_t2/ALT-BOX-05-A-I11/attempt-01/solver/final_response.md)) |
| hub inclusion, via the containing folder | 3/12 | *"The hub already contained the Marketing folder (which includes the Launch assets folder)"* ([CON-hub-inclusion-alt](pilot/runs/qwen_contrast_t1/CON-hub-inclusion-alt/attempt-01/solver/final_response.md)) |
| label, via the parent issue | 1/2 | moved "Cache images for offline mode", a sub-issue whose parent epic carries the Bug label ([ALT-LIN-01-A-I13](pilot/runs/qwen_altsweep_t2/ALT-LIN-01-A-I13/attempt-01/solver/final_response.md)) |
| initiative, via its project | 1/2 | renamed Maya's doc for the Referral program project inside the Growth initiative: *"Found the document "Referral launch plan" (created by Maya Chen) associated with the Growth team"* ([ALT-LIN-07-A-I12](pilot/runs/qwen_altsweep_t2/ALT-LIN-07-A-I12/attempt-01/solver/final_response.md)) |

*Correction ([bugs.md](bugs.md#corrections-to-reportmd)): the label and initiative failures are not containment
confusions. In both runs Qwen never looked at the parent's label or the document's initiative; it dropped the
condition.*

**Representation misread.**

| Fact (designated alternative) | Failed / runs | Qwen's words (link) |
|---|---:|---|
| Linear relation direction | 13/13 | *"The relation "r-1" (ENG-7 → blocks → ENG-9 …) has been deleted"*, for "ENG-7 is blocked by the database migration issue" ([LIN-04-P t3](pilot/runs/qwen_direction_t3/LIN-04-P/attempt-01/solver/final_response.md)) |
| team owners, read from a members view without the owner flag | 1/2 | listed Ava Brooks, Ethan Cole, Mia Wong and Noah Kim as the Design team's owners; Mia and Ethan are plain members ([LIN-06](pilot/runs/qwen_linear_01/LIN-06/attempt-03/solver/final_response.md)) |
| local day vs UTC | 1/2 | an event at 03:00Z on June 21 reported as *"Thursday, June 21, 8:00 AM PDT"* (it is Wednesday 8 PM) ([ALT-CAL-01-A-I16](pilot/runs/qwen_altsweep_t2/ALT-CAL-01-A-I16/attempt-01/solver/final_response.md)) |
| summary override vs summary | 1/2 | asked to hide "the calendar I renamed to Family" (none exists), hid the calendar whose own name is Family and which I display as "Cousins" ([ALT-CAL-04-A-I11](pilot/runs/qwen_altsweep_t2/ALT-CAL-04-A-I11/attempt-01/solver/final_response.md)) |
| handle vs real name | 1/1 | *"Successfully assigned ENG-5 … to Maya Chen"* for "@maya"; no user has that handle, and Maya Chen's is mchen ([LIN-11-A-TOLD](pilot/runs/qwen_told_t1/LIN-11-A-TOLD/attempt-01/solver/final_response.md)). The second trial asked which Maya was meant. |
| all-day exclusive end date | 1/3 | *"the all-day offsite event "Team offsite prep" (June 28–29)"*; it is an all-day event on June 28 only ([CAL-06-A-TOLD t2](pilot/runs/qwen_told_t2/CAL-06-A-TOLD/attempt-01/solver/final_response.md)) |

**Relation direction is the most robust failure.**
- **Seed.** The target-present seed (LIN-04-P) holds the correct relation (the migration issue ENG-9 blocks ENG-7) and
  four near-misses, including the reversed one (ENG-7 blocks ENG-9).
- **Result.** Qwen deleted the reversed relation in 3 of 3 trials
  ([t1](pilot/runs/qwen_direction_t1/LIN-04-P/attempt-01/solver/final_response.md),
  [t2](pilot/runs/qwen_direction_t2/LIN-04-P/attempt-01/solver/final_response.md),
  [t3](pilot/runs/qwen_direction_t3/LIN-04-P/attempt-01/solver/final_response.md)).
- **Control.** LIN-02-P, with the same Linear setup and comment facts, was correct 4/4.
- **Cause.** The API lists an issue's outgoing relations under `relations` and incoming ones under `inverseRelations`
  ([Linear schema](../../../backend/src/services/linear/api/schema/Linear-API.graphql#L8289),
  [#L8419](../../../backend/src/services/linear/api/schema/Linear-API.graphql#L8419)). Qwen reads only `relations` and
  treats the relation as undirected.

### 7.5 Phrase reading vs representation

Wording probe: the four weakest facts on the same seeds, with the relation spelled out
([cases_wording.py](pilot/cases_wording.py); runs [t1](pilot/runs/qwen_wording_t1/), [t2](pilot/runs/qwen_wording_t2/),
[t3](pilot/runs/qwen_wording_t3/)). All four are absence-permitted and contain only the ALT near-miss.

| Fact | Unhinted | Spelled out | Acted | Kind |
|---|---|---|---:|---|
| folder creator | "Sam Rivera created a … folder" | "Sam Rivera created (not necessarily owns) a … folder" | 0/3 | phrase reading |
| hub inclusion | "that already includes the Launch assets folder" | "that already lists the Launch assets folder itself as one of its items" | 0/3 | phrase reading |
| event creator | "the all-day offsite Maya Chen created" | "… that Maya Chen created (she may not be its organizer)" | 3/3 | reads the evidence, overrides it |
| relation direction | "ENG-7 is blocked by the database migration issue" | "… (that is, the migration issue blocks ENG-7)" | 3/3 | direction ignored |

**The direction probe, step by step**
([trajectory](pilot/runs/qwen_wording_t1/WRD-relation-direction/attempt-01/solver/WRD-relation-direction.json)):
1. Queried ENG-7's `relations`: r-1, ENG-7 blocks ENG-9.
2. Queried the migration issue's own `relations`: empty, so it blocks nothing.
3. Deleted r-1 anyway: *"The blocking relation between ENG-7 (Upgrade auth library) and ENG-9 (Run database migration
   for the v2 schema) was found and successfully removed."*

**What this means for test design.** Phrase-reading weaknesses depend on how a test words the fact; representation
weaknesses belong to the fact itself. A cover should word facts as users naturally do. A failure that survives explicit
wording is the stronger finding.

### 7.6 What held

- **43 of 59 strictly tested facts never failed** ([Appendix C](#appendix-c-per-fact-results)). They include:
  - person roles: file owner (0/12), file creator (0/6), task creator (0/5), comment author, attendee vs organizer
    (0/5), assignee vs creator, document creator vs editor;
  - views and representations: series vs occurrence, calendar owner vs a calendar named after the person, next vs
    current cycle;
  - bindings: comments, tasks and hub items.
- **Hierarchy levels that the API names explicitly held in all 15 runs:**
  - target present 9/9 (three cases × three trials);
  - target removed, absence permitted 6/6.

  Examples:
  - *"WEB-12 ("Idempotent payment requests") has no parent issue"*
    ([LIN-17-A-TOLD](pilot/runs/qwen_level_t1/LIN-17-A-TOLD/attempt-01/solver/final_response.md));
  - *"His comment … is a top-level comment, not a reply to another comment"*
    ([BOX-11-A-TOLD](pilot/runs/qwen_level_t1/BOX-11-A-TOLD/attempt-01/solver/final_response.md));
  - only the moved Design sync occurrence was edited
    ([CAL-11](pilot/runs/qwen_level_t2/CAL-11/attempt-01/solver/final_response.md)).

  In most of these runs the strict count's test did not register a fetch of the other level's record by its id. So,
  apart from the recurring-event case, these runs do not enter the strict count.
- **The W08 shape did not transfer.** A near-miss matches on the surface through a more salient relation, and the target
  needs one extra lookup. All five such cases passed in all 15 runs of the three W08 trials; one of those runs timed out
  after making the correct change. One earlier LIN-15 run (round 4) ended without an established outcome.
  - Box: *the PDF the Finance Reports folder's owner created* (vs a PDF located in that folder; BOX-09), and *the
    comment the Vendor Contracts folder's owner left* (vs the file owner's comment; BOX-10);
  - Calendar: *the calendar Kenji Sato owns* (vs one named Kenji Sato; CAL-10);
  - Linear: *the open issue assigned to a member of the Design team* (vs a Design-team issue; LIN-15), and *the bug in
    the project Maya Chen leads* (vs a bug assigned to Maya; LIN-16).

  See [BOX-09](pilot/runs/qwen_w08_t1/BOX-09/attempt-01/solver/final_response.md),
  [CAL-10](pilot/runs/qwen_w08_t1/CAL-10/attempt-01/solver/final_response.md) and
  [LIN-16](pilot/runs/qwen_w08_t1/LIN-16/attempt-02/solver/final_response.md).
- **Caveat.** A target-present pass is weak evidence when the agent never inspected the near-miss.
  - Box folder listings return only names and ids
    ([listing](../../../backend/src/services/box/database/operations.py#L738)), so an owner, creator or modifier
    near-miss is examined only if the agent fetches that item. (An earlier version said listings show the creator and
    last modifier; see [bugs.md](bugs.md#corrections-to-reportmd).)
  - An audit of Box runs ([audit_present.py](pilot/audit_present.py)) found several passes of this kind.
  - That is why §7.4 and Appendix C use the strict count.

### 7.7 Slack on qwen3.8

Earlier Slack cases were rerun unchanged except for the model ([trial 1](pilot/runs/qwen38_slack_bridge/runs/qwen36/),
[trial 2](pilot/runs/qwen38_slack_bridge_t2/runs/qwen36/)). The unchanged runner names its output subdirectory
`qwen36`, but the model used was `qwen3.8:27b`, as each attempt's `solver/config.json` records.

| Case (mode) | Request (abridged) | qwen3.8 | Earlier runs (qwen3.6 / Sonnet 5 / Haiku 4.5) |
|---|---|---|---|
| W08-base (single) | remove my 🔥 from the message *written by a member* of the launch-readiness channel | **2/2 wrong**: removed it from Elena's message *located* in that channel ([answer](pilot/runs/qwen38_slack_bridge_t2/runs/qwen36/W08-base/attempt-01/solver/final_response.md)) | wrong / wrong / wrong ([review](../purdue_comparison_01/case_reviews/W08-base.md)) |
| W08-multiple (multiple) | the same, plural | 1/1 wrong | right / right / wrong |
| W08-absent (absent) | the same, no match | 2/2 wrong | wrong / wrong / wrong |
| W02-absent (absent) | DM the person who reacted 🔥 to the budget-freeze announcement in #finance | 2/2 wrong (DM'd Imani, whose 🔥 is on the budget-freeze announcement in #operations) | wrong / right / wrong |
| W09-base (absent) | what workspace is shown on the profile of the bot in #incident-response | 2/2 wrong (answered through a bot that is not in the channel) | wrong / wrong / wrong |
| W03-absent, W04-base (absent) | no match exists | timed out in all 4 runs | wrong on qwen3.6 |
| W02-base, W03-single, W04-single, W09-single | target present | all correct (1 run each) | correct on qwen3.6 |

**W08 wording.** W08's request ("the message written by a member of the channel about launch readiness") can also be
read as a statement about location. Its analogues with unambiguous wording passed (§7.6), so part of W08 is wording
rather than a model fact.

### 7.8 Distinct test cases and distinct bugs

*Each of the 16 bugs is examined, with its evidence, in [bugs.md](bugs.md). That review corrects three statements in
this section ([details](bugs.md#corrections-to-reportmd)):*
- *the 179 case IDs are 168 distinct inputs;*
- *the 25 failing cases are 21 distinct inputs;*
- *3 bugs, not 4, recurred across different inputs, because hub inclusion's failures all come from one input.*

**Distinct test cases.** The 327 scored episodes are **179 distinct test cases**, derived from **37 scenarios**. A
scenario is a seed plus a request: the 31 runnable cover cases and the 6 arrangement cases.
- 76 cases ran once, 64 twice, 33 three times and 6 four times, so 148 episodes are repeat trials.
- Most of the 179 are diagnostic controls: target flips, isolated near-misses, told variants, contrasts, the ALT sweep
  and wording probes. The fact-sensitive cover itself is 30 cases (§8.1).

**What counts as a distinct bug.** Two failures are the same bug if and only if they are attributed to the same
requirement.
- **Attribution comes from construction.** Each near-miss differs from the target in exactly one fact, and the checker
  verifies that mechanically. Selecting the near-miss therefore pins the failure to that fact.
- **The same requirement failing in different cases or trials is one bug.** One episode that selects two different
  near-misses exposes two bugs (LIN-06).
- **Failures on presupposed no-target requests are one bug against the resolution policy**, not one per fact (§7.2).
  The behaviour occurs whichever fact is missing and disappears when absence is permitted.
- **Mock artifacts (LIN-10) are not agent bugs.**

**Result: 16 requirement-level bugs, plus 1 policy bug.**
- **Requirement-level bugs.** 44 failing fact-sensitive episodes, in 25 distinct cases, map to 16 distinct
  requirements: Box 6, Calendar 4, Linear 6.
- **The policy bug.** 49 failing presupposing episodes (the 46 of §7.1 plus 3 far misses) are one policy bug.
  - They touched 35 requirements, 26 of which never failed once absence was permitted.
  - Counting them per requirement would add 26 spurious bugs, the same inflation the underspecified Slack cases
    produced.

| Requirement | Domain | Failing episodes | Cases | Family | Example |
|---|---|---:|---:|---|---|
| R IssueRelation.issueId (relation direction) | Linear | 13 | 5 | representation | [LIN-04-P t3](pilot/runs/qwen_direction_t3/LIN-04-P/attempt-01/solver/final_response.md) |
| A Event.creator_email (creator read as organizer) | Calendar | 9 | 4 | person role | [WRD-event-creator](pilot/runs/qwen_wording_t1/WRD-event-creator/attempt-01/solver/final_response.md) |
| R Folder.created_by_id (creator read as owner) | Box | 6¹ | 4 | person role | [BOX-06-TOLD](pilot/runs/qwen_told_t1/BOX-06-TOLD/attempt-01/solver/final_response.md) |
| R HubItem.folder (inclusion via a containing folder) | Box | 3 | 2 | containment | [CON-hub-inclusion-alt](pilot/runs/qwen_contrast_t1/CON-hub-inclusion-alt/attempt-01/solver/final_response.md) |
| R File.collections (membership via a collected folder) | Box | 2 | 1 | containment | [ALT-BOX-05-A-I11](pilot/runs/qwen_altsweep_t2/ALT-BOX-05-A-I11/attempt-01/solver/final_response.md) |
| R TaskAssignment.assigned_by_id (assigner read as creator) | Box | 2 | 1 | person role | [ALT-BOX-08-A-I15](pilot/runs/qwen_altsweep_t2/ALT-BOX-08-A-I15/attempt-01/solver/final_response.md) |
| R File.modified_by_id (modifier read as creator) | Box | 1 | 1 | person role | [BOX-01-A-TOLD t2](pilot/runs/qwen_controls_t2/BOX-01-A-TOLD/attempt-01/solver/final_response.md) |
| R issue labels (label via the parent issue) | Linear | 1 | 1 | containment | [ALT-LIN-01-A-I13](pilot/runs/qwen_altsweep_t2/ALT-LIN-01-A-I13/attempt-01/solver/final_response.md) |
| R Document.initiativeId (document of a project in the initiative) | Linear | 1 | 1 | containment | [ALT-LIN-07-A-I12](pilot/runs/qwen_altsweep_t2/ALT-LIN-07-A-I12/attempt-01/solver/final_response.md) |
| D local_time (UTC read as the local day) | Calendar | 1 | 1 | representation | [ALT-CAL-01-A-I16](pilot/runs/qwen_altsweep_t2/ALT-CAL-01-A-I16/attempt-01/solver/final_response.md) |
| A CalendarListEntry.summary_override (renamed vs real name) | Calendar | 1 | 1 | representation | [ALT-CAL-04-A-I11](pilot/runs/qwen_altsweep_t2/ALT-CAL-04-A-I11/attempt-01/solver/final_response.md) |
| D all_day (exclusive end date) | Calendar | 1 | 1 | representation | [CAL-06-A-TOLD t2](pilot/runs/qwen_told_t2/CAL-06-A-TOLD/attempt-01/solver/final_response.md) |
| A User.displayName (handle vs real name) | Linear | 1 | 1 | representation | [LIN-11-A-TOLD](pilot/runs/qwen_told_t1/LIN-11-A-TOLD/attempt-01/solver/final_response.md) |
| A TeamMembership.owner (owner flag missing from the members view) | Linear | 1 | 1 | representation | [LIN-06](pilot/runs/qwen_linear_01/LIN-06/attempt-03/solver/final_response.md) |
| B TeamMembership (owner of another team, plain member here) | Linear | 1² | 1 | representation | [LIN-06](pilot/runs/qwen_linear_01/LIN-06/attempt-03/solver/final_response.md) |
| A File.version_number (version 2 for "3 or later") | Box | 1³ | 1 | — | [BOX-07-A-TOLD](pilot/runs/qwen_told_t1/BOX-07-A-TOLD/attempt-01/solver/final_response.md) |

¹ One of the six is the PLAIN contrast failure (§7.3), where the generic habit leaked through the permission.
² The same episode as the row above.
³ Qwen acted, noticed the error and reverted it; the final state is correct.

**How much weight each count bears.**
- **Reproduction.** 6 bugs were reproduced in two or more episodes. 4 of them recurred in two or more distinct cases:
  relation direction, event creator, folder creator and hub inclusion. The other 10 were seen once and are provisional.
- **Transient errors.** Excluding the transient version-number error gives 15.
- **Granularity.** The count depends on how fine-grained the requirements are. Grouped by cause, the 15 non-transient
  bugs collapse into the three families of §7.4; with the policy bug, that makes 4 failure modes.
- **Slack.** The Slack reruns (§7.7) are not in the 327. They re-exposed the known W08 substitution and the same policy
  bug.

[report_data.py](pilot/report_data.py) prints these numbers and every failing episode's path, in its section "Distinct
cases and bugs".

---

## 8. Cover size and redundancy

### 8.1 The pilot covers are irredundant

Only fact-sensitive forms count here:
- each presupposing cover case is replaced by its told twin, which has the same seed and claims;
- LIN-08 has no twin and is dropped.

The exact minimum was computed by exhaustive search ([cover_sensitive.json](pilot/cover_sensitive.json)):

| Domain | Cover cases | Facts credited | Exact minimum | New facts per needed case |
|---|---:|---:|---:|---:|
| Box | 9 | 38/60 | 9 | 4.2 |
| Calendar | 9 | 26/40 | 9 | 2.9 |
| Linear | 13 | 42/121 | 12 (LIN-14 repeats covered facts) | 3.5 |

### 8.2 Projected full covers

At the realized density, a full cover needs about:
- **14 Box, 14 Calendar and 35 Linear tests**;
- about **10 Slack tests** (extrapolated; no Slack FDC cases were built);
- about 3 policy tests per domain.

That is roughly 85 tests in total, inside the "high tens" target. The requirement counts, 34–121 per domain, are inside
the target range too. The pilot already has 30 irredundant fact-sensitive cover cases, so completing the covers means
about 43 new fact tests plus 12 policy tests.

### 8.3 The earlier Slack suite under this criterion

This mapping works at the occurrence level: which facts a case *mentions* through its fixed selector
([slack_suite_map.py](pilot/slack_suite_map.py)). The suite's near-misses were not re-checked under FDC, and bindings
were not mapped.

- The 57 cases mention **11 of Slack's 34 facts**:
  - attributes: channel name, channel topic, message text, reaction type, bot flag, real name;
  - relationship roles: message author, message location, channel membership, reaction;
  - derived: member count.
- The 20 target-present cases alone mention all 11, and an exact minimum of **4** of them covers them (e.g., W03-multiple,
  W05-base, W06-base, W09-multiple; 96 such covers exist).
- The 37 absent and underspecified cases add **no** fact, and 16 of the 20 target-present cases are also redundant.

### 8.4 Construction recipe

1. Pick a natural request whose identifying path uses several facts. Give each fact one near-miss through its designated
   alternative, satisfying every other condition.
2. Co-locate near-misses with the target, so rejecting them requires inspecting the distinguishing field. Alternatively,
   use a no-target seed with "if there isn't one, tell me".
3. Word relational conditions the way users naturally do, but unambiguously. Don't list the target first.
4. Verify every claim mechanically, and preflight the seed through the real API to check that each distinguishing field
   is observable.
5. Add the per-domain policy panel once.

---

## 9. What makes a coverage dimension meaningful

- **The fact, with its alternative.** Failures did not track route length, number of conditions or entity type. They
  tracked whether a fact has a plausible sibling that the observation does not clearly rule out:
  - person roles of one object (creator / owner / organizer / assigner) look alike in payloads;
  - containment through a parent looks like membership;
  - direction is implicit in which list a relation appears under;
  - a members view drops the owner flag.

  Where the API names the distinction explicitly (`parent`, `children`, comment `item`, `recurringEventId`), Qwen did
  not confuse it.
- **Not the resolution mode.** Absent and underspecified requests each trigger one habit. They belong in a small policy
  panel, which is exactly why the 57-case suite looked redundant.
- **Not the wording, unless you mean to test reading.** Two weak facts disappeared when the relation was spelled out.
  Tests should use natural wording, and a failure that survives explicit wording is the stronger finding.

For G2 and G3 in the [evaluation plan](../../protocols/evaluation_plan.md), this suggests varying a fact's designated
alternative, rather than the resolution mode, when building controlled variants.

---

## 10. Limitations

- **One model** (`qwen3.8:27b`), 1–3 trials per cell, so rates are indicative.
  - The four most frequent weak facts (relation direction, event creator, folder creator, hub inclusion) failed in two
    or more independent designs.
  - The other weak facts come from one design and 1–2 trials.
- **Model change.** The earlier Slack evidence used `qwen3.6:27b`. The reruns show the main Slack results repeat on
  3.8, except W08-multiple.
- **Hand-chosen alternatives.** Designated alternatives for roles and representations were chosen by hand from the model
  (sibling attributes are mechanical). Missed alternatives would make the catalog look more robust than it is.
- **The strict count is conservative.** It tests only 59 facts. It misses runs that reached a near-miss through a
  listing, through a parent/child field, or under a different identifier (e.g., a Linear issue fetched as `WEB-13`
  rather than by its internal id). The lenient count (97 facts, 81 held) is an upper bound.
- **Coverage so far.** Strictly tested facts are Box 30/60, Calendar 12/40, Linear 17/121 and Slack 0/34 (new FDC cases).
- **Scoring of retries.** Six timed-out attempts were retried and the retry was scored. Timeouts are otherwise excluded
  from denominators.
- **Mock behaviour** shaped some cases (single collection, trashed items hidden, task deletion error, project status).
  These were excluded or designed around, not counted.
- **Manual work.** Cases, alternatives and failure readings are manual. Automatic attribution is provisional, and every
  failure cited was read.

---

## 11. Next steps

1. **Complete the covers in fact-sensitive forms.** That is about 43 new fact tests, including Slack, plus the policy
   panels (§8.2). Run 2–3 trials each.
2. **Add a second solver** (e.g., Sonnet or Haiku) to separate model-specific from fact-specific weaknesses.
3. **Extend the three failure families to untested facts:** other person-role pairs, other containment paths, other
   representation pairs.
4. **Build the per-domain policy panels** (3 tests each) and fold the absent/underspecified behaviour into them.
5. **Feed the cases to the custom evaluator.** The cards and task specs are already in the case files; the evidence
   bundles are in each attempt directory.

---

## 12. How the work unfolded

1. **Context and catalogs.**
   - Read the models, protocols, prior suite and Codex's findings.
   - Defined the criterion and built the catalogs with full accounting.
   - Wrote the credit checker and the first Box cases.
2. **Plumbing, then your redirect.** Box, Calendar and Linear needed a custom-seed installer. I spent too long on it and
   on mock capabilities before your correction; after the redirect, the work shifted to running and iterating.
3. **Round 1: packed cases in all three domains.** Target present was almost always right; no target was almost always
   wrong.
4. **Round 2: flips, isolation, plain, far, told.** The no-target failures turned out to be one generic habit. Permitting
   absence left a residue on specific facts.
5. **Round 3: contrast, ALT sweep, wording, W08 arrangement, hierarchy level.** The residue concentrated on designated
   alternatives and formed three families.
6. **Corrections after review.**
   - Coverage and redundancy numbers were recomputed under the fact-sensitive rule.
   - Robustness was counted strictly.
   - The far-miss wording was corrected.
   - This report's numbers were regenerated from the run records.

**Infrastructure notes.**
- `qwen3.6:27b` disappeared from Purdue, so the runs use `qwen3.8:27b`.
- Concurrency above about 10 episodes triggered Purdue rate limits. Those attempts were retried and kept as
  infrastructure outcomes.

---

## Appendix A: the four catalogs

Kinds: A attribute, R relationship, H hierarchy, B binding, D derived. Machine-readable versions with evidence and
alternatives: [slack.json](catalog/slack.json), [box.json](catalog/box.json), [calendar.json](catalog/calendar.json),
[linear.json](catalog/linear.json).

**Slack (34)**, model: [model.md](../../domains/slack/model.md)
- A (20):
  - User: username, email, real_name, display_name, timezone, title, is_active, is_bot;
  - Conversation: channel_name, topic_text, purpose_text, is_private, is_dm, created_at, is_archived;
  - WorkspaceMembership: role;
  - Message: message_text, blocks, created_at;
  - Reaction: reaction_type.
- R (4): message author, message location, channel membership, reaction.
- H (1): thread (root vs reply).
- B (4): conversation→messages, user→messages, message→reactions, user→reactions.
- D (5): reply count, member count, reaction count, latest message, DM identified by its participants.

**Box (60)**, model: [model.md](../../domains/box/model.md)
- A (31):
  - User: name, login;
  - Folder: name, description, size, tags, shared_link, created_at, modified_at;
  - File: name, description, size, version_number, extension, lock, tags, shared_link, uploader_display_name,
    created_at, modified_at;
  - Comment: message, created_at;
  - Task: message, action, is_completed, due_at, created_at;
  - TaskAssignment: resolution_state;
  - Hub: title, description, created_at.
- R (19):
  - file owner / creator / modifier; folder owner / creator / modifier; file's folder;
  - comment's file; comment author;
  - task's file; task creator; assignee; assigner;
  - hub creator; hub updater; hub includes file; hub includes folder;
  - file in collection; folder in collection.
- H (2): folder containment (direct vs nested); comment reply.
- B (5): folder→files, file→comments, file→tasks, task→assignments, hub→items.
- D (3): folder item count, file comment count, task assignment count.

**Calendar (40)**, model: [model.md](../../domains/calendar/model.md)
- A (28):
  - Calendar: summary, description, location, time_zone, data_owner;
  - CalendarListEntry: access_role, summary_override, hidden, selected;
  - Event: status, summary, description, location, creator_email, organizer_email, start, end, transparency,
    visibility, hangout_link, event_type;
  - EventAttendee: email, resource, optional, response_status;
  - AclRule: role, scope_type, scope_value.
- R (4): calendar on my list, event's calendar, attendance, access grant.
- H (1): recurring series vs modified occurrence.
- B (3): event→attendees, calendar→events, calendar→grants.
- D (4): virtual occurrence, local time, primary calendar, all-day vs timed.

**Linear (121)**, model: [model.md](../../domains/linear/model.md)
- A (63):
  - Issue: title, description, priority, estimate, dueDate, createdAt, updatedAt, completedAt, identifier;
  - User: name, displayName, email, active, admin, guest, app, timezone, statusLabel;
  - Team: name, key, description, private; TeamMembership: owner;
  - WorkflowState: name, type; IssueLabel: name, isGroup;
  - Project: name, description, priority, health, startDate, targetDate;
  - ProjectMilestone: name, targetDate, status; ProjectStatus: name, type;
  - Cycle: number, name, startsAt, endsAt;
  - Comment: body, createdAt, resolvedAt; Attachment: title, url, sourceType;
  - IssueRelation: type; Document: title, content;
  - Initiative: name, description, status, health, targetDate; ProjectRelation: type;
  - Notification: title, type, readAt; OrganizationInvite: email, role, acceptedAt.
- R (38):
  - issue: assignee, creator, subscribers, labels, team, state, project, milestone, cycle;
  - attachment: issue, creator; comment: issue, author, resolver;
  - cycle team; relation source and target; label team;
  - project: lead, creator, status; milestone project; team membership; state team;
  - document: project, initiative, team, creator, editor;
  - initiative: owner, creator; initiative–project; project relation source and target; initiative relation;
  - invite: sender, invitee; notification actor.
- H (5): parent/sub-issue, comment thread, label group, parent/sub-team, parent/sub-initiative.
- B (12): team→issues, project→issues, cycle→issues, assignee→issues, issue→comments, issue→labels,
  issue→relations, issue→sub-issues, team→memberships, project→milestones, issue→attachments, project→documents.
- D (3): current cycle, overdue, issue count.

Excluded entities and their reasons are in §5.2.

---

## Appendix B: the pilot cover cases

Form: *present* means the target is present; *absent* means no target (scored through its told twin, §8.1). The last
column lists the credited requirements ([coverage.json](pilot/coverage.json)). Case files are in
[pilot/cases/](pilot/cases/).

| Case | Form | Request | Facts credited |
|---|---|---|---|
| [BOX-01](pilot/cases/box/BOX-01.json) | present | Add the tag q3-close to the PDF that Maya Chen owns directly in the Finance Reports folder (not in its subfolders) and that Leo Park modified last. | 6: File.extension, Folder.name, User.name, H Folder.parent_id, File.modified_by_id, File.owned_by_id |
| [BOX-02](pilot/cases/box/BOX-02.json) | absent | Find the spreadsheet in the Finance Reports folder that Priya Nair commented on about travel costs, and add " - travel reviewed" to the end of its name. | 6: Comment.message, File.extension, B file→comments, Comment.created_by_id, Comment.file_id, File.parent_id |
| [BOX-03](pilot/cases/box/BOX-03.json) | present | Set the due date to October 9, 2026 on the review task Dana Whitfield created on the Acme vendor contract that's assigned to Omar Haddad and that Omar hasn't completed yet. | 6: Task.action, resolution state, B task→assignments, Task.created_by_id, Task.item_id, assignee |
| [BOX-04](pilot/cases/box/BOX-04.json) | absent | Add the Brand guidelines folder that Maya Chen owns to the hub Leo Park created that already includes the Launch assets folder. | 4: B hub→items, Folder.owned_by_id, Hub.created_by_id, HubItem.folder |
| [BOX-05](pilot/cases/box/BOX-05.json) | present | Remove the shared links from the locked spreadsheets in my Favorites collection. | 4: File.extension, File.lock, File.shared_link, File.collections |
| [BOX-06](pilot/cases/box/BOX-06.json) | absent | Sam Rivera created a client-tagged folder directly under Projects for the Atlas rollout (its description says so) that holds a PDF Maya Chen owns. Add the tag atlas-q3 to that folder. | 5: Folder.description, Folder.tags, B folder→files, H Folder.parent_id, Folder.created_by_id |
| [BOX-07](pilot/cases/box/BOX-07.json) | present | Add FINAL to the end of the name of the legal-tagged contract whose latest version Leo Park uploaded - it's on version 3 or later and was last modified in September 2026. | 4: File.modified_at, File.tags, File.uploader_display_name, File.version_number |
| [BOX-08](pilot/cases/box/BOX-08.json) | present | Add the tag escalate to the file that has an open review task, due before October 1, 2026, which Dana Whitfield assigned to two or more people. | 5: Task.due_at, Task.is_completed, B file→tasks, D assignment count, assigner |
| [BOX-09](pilot/cases/box/BOX-09.json) | present | Add the tag owner-draft to the PDF that the owner of the Finance Reports folder created. | 4: File.extension, File.created_by_id, File.owned_by_id, Folder.owned_by_id |
| [CAL-01](pilot/cases/calendar/CAL-01.json) | present | Move the design review that Priya Nair declined on Thursday to Room 5B. | 6: Event.start, Event.summary, response status, attendance, D local time, B event→attendees |
| [CAL-02](pilot/cases/calendar/CAL-02.json) | present | Cancel just this Tuesday's session of the weekly Platform sync that Omar Haddad organizes - leave the rest of the series alone. | 4: organizer, Event.start, Event.summary, D occurrence |
| [CAL-03](pilot/cases/calendar/CAL-03.json) | absent | Remove dana.whitfield@northwind.example's write access to the Marketing calendar. | 4: ACL role, scope type, scope value, grant's calendar |
| [CAL-04](pilot/cases/calendar/CAL-04.json) | present | In my calendar list, hide the calendar I renamed to "Family", and remove every hidden calendar that I can only read. | 3: access role, hidden, summary override |
| [CAL-05](pilot/cases/calendar/CAL-05.json) | absent | Delete my private focus-time block in the Library this Friday - the one that shows me as free. | 4: event type, location, transparency, visibility |
| [CAL-06](pilot/cases/calendar/CAL-06.json) | present | Make Omar Haddad an optional attendee on the all-day offsite Maya Chen created for June 29. | 3: creator, Event.start, D all-day |
| [CAL-07](pilot/cases/calendar/CAL-07.json) | present | Change the description of Kenji Sato's Tokyo-time calendar that has the all-hands on June 21 to "APAC team events". | 3: data owner, time zone, B calendar→events |
| [CAL-08](pilot/cases/calendar/CAL-08.json) | absent | Delete the dentist appointment on Wednesday from my primary calendar. | 2: Event.start, D primary |
| [CAL-09](pilot/cases/calendar/CAL-09.json) | present | Move the meeting Priya Nair organized on Thursday to 3pm the same day (keep its length). | 3: organizer, Event.start, event's calendar |
| [LIN-01](pilot/cases/linear/LIN-01.json) | present | Move the Mobile team's high-priority bug that's assigned to Priya Nair to In Review. | 7: priority, label name, team name, state name, assignee, state's team, labels |
| [LIN-02](pilot/cases/linear/LIN-02.json) | absent | Delete the comment Leo Park left on ENG-42 asking to postpone the release. | 4: comment body, issue identifier, comment's issue, comment author |
| [LIN-03](pilot/cases/linear/LIN-03.json) | present | Set the target date of the Beta milestone in the Checkout Redesign project that Maya Chen leads to October 30, 2026. | 4: project name, milestone name, project lead, milestone's project |
| [LIN-04](pilot/cases/linear/LIN-04.json) | absent | ENG-7 is blocked by the database migration issue. Remove that blocking relation. | 4: issue title, relation type, relation source, relation target |
| [LIN-05](pilot/cases/linear/LIN-05.json) | present | Today is September 23, 2026. Move every open issue in the Platform team's current cycle that's estimated at 5 points or more and is past its due date into the team's next cycle. | 6: due date, estimate, D current cycle, D overdue, cycle's team, issue's cycle |
| [LIN-06](pilot/cases/linear/LIN-06.json) | present | Which active admins are owners of the Design team itself (not its sub-teams)? Just list their names. | 5: membership owner flag, active, admin, B team→memberships, H sub-team |
| [LIN-07](pilot/cases/linear/LIN-07.json) | present | Rename the doc Maya Chen created for the Growth initiative to "Growth Q4 plan". | 3: initiative name, document creator, document's initiative |
| [LIN-08](pilot/cases/linear/LIN-08.json) | absent | Set the priority to Urgent on the in-progress project that Priya Nair leads and that's due before November 1, 2026. | 4 on paper (target date, status name, lead, status); not run, because the mock returns no project status |
| [LIN-09](pilot/cases/linear/LIN-09.json) | present | Assign to Leo Park the Checkout project issue that has a GitHub pull request Leo attached. | 4: source type, B issue→attachments, attachment creator, issue's project |
| [LIN-10](pilot/cases/linear/LIN-10.json) | present | Mark the sub-issue of "Checkout revamp" that's assigned to Sam Rivera as Done. | 3: issue title, H parent, assignee |
| [LIN-11](pilot/cases/linear/LIN-11.json) | present | Assign ENG-5 to @maya. | 1: handle |
| [LIN-12](pilot/cases/linear/LIN-12.json) | present | Resolve the comment thread Priya Nair started on WEB-12 about the flaky tests. | 3: comment body, H thread root, comment's issue |
| [LIN-14](pilot/cases/linear/LIN-14.json) | present | Set the priority to Urgent on the Infra team's issue about certificate expiry. | 2: team name, H parent team |
| [LIN-15](pilot/cases/linear/LIN-15.json) | present | Set the priority to High on the open issue that's assigned to a member of the Design team. | 4: state type, H sub-team, assignee, membership |

---

## Appendix C: per-fact results

**How to read the columns.**
- *Strict* counts fact-sensitive runs where the near-miss was the sole candidate, or was explicitly fetched, or was
  acted on.
- *Lenient* also counts runs where the near-miss appeared only in a listing.
- *Presupposing* counts runs of presupposing no-target forms in which the fact's near-miss was present.

The strict and lenient counts come from [held.py](pilot/held.py); the complete lenient table is
[fact_table.md](pilot/fact_table.md).

**Failed at least once under the strict count (16 facts)**

| Fact | Strict: failed / tested | Lenient | Presupposing: acted / present |
|---|---:|---:|---:|
| R IssueRelation.issueId (direction) | 13/13 | 13/13 | 1/1 |
| A Event.creator_email | 9/9 | 9/11 | 1/1 |
| R File.collections | 2/2 | 2/2 | 0/1 |
| A User.displayName (handle) | 1/1 | 1/3 | 0/1 |
| R TaskAssignment.assigned_by_id | 2/3 | 2/5 | 1/1 |
| R Folder.created_by_id | 5/9 | 5/12 | 0/2 |
| D local_time | 1/2 | 1/4 | 0/1 |
| A CalendarListEntry.summary_override | 1/2 | 1/4 | 1/1 |
| R issue labels | 1/2 | 1/7 | 1/1 |
| R Document.initiativeId | 1/2 | 1/4 | 1/1 |
| A TeamMembership.owner | 1/2 | 1/3 | — |
| B TeamMembership | 1/2 | 1/3 | — |
| D all_day | 1/3 | 1/5 | 0/1 |
| A File.version_number (acted, then reverted) | 1/3 | 1/3 | 1/1 |
| R HubItem.folder | 3/12 | 3/13 | 3/3 |
| R File.modified_by_id | 1/11 | 1/11 | 3/3 |

**Held in every strict test (43 facts).** Each fact is shown as strict tested count; presupposing acted/present, when
the near-miss ever appeared in a presupposing run.

| Domain | Facts |
|---|---|
| Box (24) | File.owned_by_id 12 (2/3); File.created_by_id 6; Folder.description 5 (2/3); Task.created_by_id 5 (2/2); Comment.created_by_id 4 (1/3); File.lock 4 (1/1); File.shared_link 4 (0/1); B hub→items 4 (0/2); File.tags 3 (0/1); File.uploader_display_name 3 (0/1); Hub.created_by_id 3 (0/2); TaskAssignment.assigned_to_id 3 (0/1); Comment.message 2 (0/2); Comment.file_id 2 (0/2); B file→comments 2 (3/3); B folder→files 2 (1/2); Folder.tags 2 (0/2); Task.due_at 2 (0/1); File.modified_at 1 (0/1); Folder.owned_by_id 1; Task.is_completed 1 (0/1); B file→tasks 1 (0/1); D assignment count 1 (0/1); User.name 5 (1/2) |
| Calendar (8) | attendance 5 (1/1); H series vs exception 3; D occurrence 3; Calendar.data_owner 2; Event.organizer_email 2; D primary 2 (0/1); AclRule.scope_type 2 (0/1); Event.start 1 (1/3) |
| Linear (11) | Attachment.creatorId 3; Attachment.sourceType 2; B issue→attachments 2; Comment.issueId 2 (1/2); Comment.userId 2 (0/2); Cycle.teamId 2; Document.creatorId 2 (0/1); Issue.assigneeId 2 (1/2); Issue.projectId 2; Project.leadId 2; D current cycle 2 |

**The two columns side by side are the main result in one view.** Many facts fail only when the request presupposes a
match: that is the generic habit. A few fail even when absence is permitted or the target is present: those are the
meaningful facts.

---

## Appendix D: files, sources and reproduction

| What | Where |
|---|---|
| Criterion (one page) | [criterion.md](criterion.md) |
| Run-by-run log | [findings.md](findings.md) |
| Review of the 16 bugs, with corrections to this report | [bugs.md](bugs.md) |
| Catalog curation and builder | [catalog/facts.py](catalog/facts.py), [catalog/build.py](catalog/build.py), [catalog/counts.md](catalog/counts.md) |
| Credit checker | [fdc.py](fdc.py) |
| Cases | [pilot/](pilot/): designs in `cases_*.py`, [variants.py](pilot/variants.py); built JSON in [cases/](pilot/cases/) |
| Mechanical checks and coverage | [checks.json](pilot/checks.json), [coverage.json](pilot/coverage.json), [cover_sensitive.json](pilot/cover_sensitive.json) |
| Runs (all attempts kept) | [pilot/runs/](pilot/runs/): `qwen_*` solver runs, `qwen38_slack_bridge*` Slack reruns, `prepare_*` fixture checks (console `.log` files stay local; git ignores them) |
| Analysis | [analyze.py](pilot/analyze.py), [results.py](pilot/results.py), [results.json](pilot/results.json), [manual_labels.json](pilot/manual_labels.json), [fact_table.py](pilot/fact_table.py), [held.py](pilot/held.py), [contrast_table.py](pilot/contrast_table.py), [audit_present.py](pilot/audit_present.py), [report_data.py](pilot/report_data.py), [slack_suite_map.py](pilot/slack_suite_map.py), [show.py](pilot/show.py) |
| Harness | [custom_runtime.py](../../integrations/agentdiff/custom_runtime.py), [run.py](pilot/run.py), [slack_bridge.py](pilot/slack_bridge.py) |

**Contents of an attempt directory.**
- `case.json`: the exact case that was run;
- `solver/final_response.md`: the answer;
- `solver/<CASE>.json`: the full trajectory;
- `solver/requests/`: every request sent;
- `environment/initial_state.json`, `environment/final_state.json` and `environment/diff_run.json`;
- `execution_summary.json`: status, termination and usage.

**Commands**, run from the worktree root. Solver runs need the environment described in
[solver/README.md](../../solver/README.md).

```bash
python3 -m grounding.runs.fact_coverage_01.catalog.build                 # catalogs + accounting check
python3 -m grounding.runs.fact_coverage_01.pilot.build                   # cases + every credit claim checked
python -m grounding.runs.fact_coverage_01.pilot.run --out <new dir> --cases BOX-01 --prepare-only   # no model calls
python -m grounding.runs.fact_coverage_01.pilot.run --out <new dir> --cases BOX-01 --concurrency 4  # Qwen run
python3 -m grounding.runs.fact_coverage_01.pilot.results <run dirs> --json out.json
python3 -m grounding.runs.fact_coverage_01.pilot.report_data             # §7.1 and §7.8 numbers, evidence links
python3 -m grounding.runs.fact_coverage_01.pilot.held                    # strict / lenient fact counts
python3 -m grounding.runs.fact_coverage_01.pilot.slack_suite_map         # §8.3
python3 -m grounding.runs.fact_coverage_01.pilot.show <attempt dir>      # read one trajectory
```

**Sources consulted.**
- Domain models and route counts: [domains/](../../domains/), [route_comparison.md](../../domains/route_comparison.md).
- Protocols: [evaluation_plan.md](../../protocols/evaluation_plan.md), [card_extraction.md](../../protocols/card_extraction.md).
- The manual suite and its comparisons: [manual_exemplars_01](../manual_exemplars_01/README.md),
  [manual_comparison_01](../manual_comparison_01/report.md), [purdue_comparison_01](../purdue_comparison_01/report.md).
- Codex's secondary analysis:
  [manual_findings.md](../../campaigns/coverage_codex_01/manual_findings.md).
- Replica source, for observability:
  - Box: [folder listings](../../../backend/src/services/box/database/operations.py#L738) (names and ids only, no
    people fields), [search excludes trashed items](../../../backend/src/services/box/database/operations.py#L1819),
    [favorites-only collections](../../../backend/src/services/box/database/operations.py#L1935);
  - Linear: [`inverseRelations`](../../../backend/src/services/linear/api/schema/Linear-API.graphql#L8289) and
    [`relations`](../../../backend/src/services/linear/api/schema/Linear-API.graphql#L8419).

---

## Appendix E: glossary

| Term | Meaning here |
|---|---|
| Fact | One element of the domain model usable to identify something: an attribute, relationship role, hierarchy level, binding or derived view |
| Designated alternative | The plausible substitute for a fact: a sibling role or attribute, the other level, the reversed direction, a split across records, a neighbouring representation |
| Near-miss | A record that satisfies every condition of a request except one fact, usually by satisfying its alternative |
| Credit | A fact counts as covered only when a near-miss for it changes the result of the reference query (checked mechanically) |
| Packed test | One natural request with several facts, one near-miss each |
| Presupposing request | A request that assumes the thing exists ("the PDF that …"); with no match it triggers the generic habit |
| Told / absence permitted | The same request plus "If there isn't one, just tell me." |
| Fact-sensitive form | Target present, or no target with absence permitted |
| Policy panel | A few fixed tests per domain for resolution behaviour (no match, far miss, ambiguity, collections) |
| Strict count | A run tests a fact only if its near-miss was the sole candidate, was explicitly fetched, or was acted on |
