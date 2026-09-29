# several_match_auto_01: automating the several-match method (phases 2 and 3)

*2026-09-28/29, overnight. The method is [../several_match_02/method.md](../several_match_02/method.md) (version
1.1), made by hand in the manual investigation. Here Muse (`muse-spark-1.3-contributor`) does the creative steps,
code does the rest, and the self-hosted Qwen is the instrument. Every number is from [summary.py](summary.py) →
`summary.json`, after all runs were graded.*

## The numbers the PI asked for

| | |
|---|---|
| **The coverage space** | The method's requirement space: the laziness behaviours (stopping early; falling short on scope, pages, visibility, filter or selection), each instantiated as **shortcuts**, the API calls a lazy agent makes on one service for one kind of request. The population's plural-worthy requests fall in **6 kinds of request with a route table, with 33 shortcuts**. **19 are lazy and practical to defeat**. 9 need more records than the replicas hold practically (a page of 250 to 1,000; a search crowd over 200). 5 are not lazy for these requests (for example, every page of the named channel is the thorough route). Stopping early applies to every plural request. |
| **Covers** | 91 single-target cover scenarios: the fact method's hand covers and autogen_01/02's generated ones. The writer judged **65 plural-worthy**; 26 name one record by nature (an exact title, a superlative, a rename to one name). 16 of the 65 are kinds with no route table (Box folders and tasks, calendars, Linear comments and projects, a Slack user) or a named calendar (a page trap there needs 250 events). They get the easy tier only. 4 more name the visibility ("every private channel"), so no trap is left to add. |
| **Tests generated automatically** | **131**: 101 first builds (64 easy, 37 hard); 17 repairs (after the reader's doubts, an id clash, or a seed that broke a unique key); 13 from iterations 2 and 3 (traps the first round lacked). |
| **Coverage reached** | **All 19 lazy, practical shortcuts are defeated** by at least one valid hard test (per kind: Box files in a named folder 4 of 8, Box files anywhere 5 of 5, Calendar 4 of 4, Linear 1 of 6, Slack messages in a named channel 3 of 8, Slack channels 2 of 2; the rest impractical or not lazy). Covers: 63 of 65 have a valid easy test, and 39 of the 49 with a route table have a valid hard test. |
| **Valid** | **103 of 131** (63 easy, 40 hard). Refused: the cold reader disagreed (16, mostly first builds later repaired); the page trap was impractical (5, iteration 2, below); the seed broke a unique key of the replica's schema (6); a file and a folder shared an id (3, repaired); the thorough route missed a target (1, a DM request: the route table has no DM routes). |
| **Distinct failures exposed** | 309 trials on the valid tests (3 per test); the review voids 8. **28 distinct (cover, placement) misses** and **13 distinct (cover, fact) near misses acted on**. By laziness behaviour: visibility in 9 covers (the hidden calendar in all 7 calendar covers, a private channel in 2); scope in 7 (another owned calendar); pages in 5 (Linear past the first 50 issues; 2 of them come with a misread condition). There was no clear case of stopping early, and no filter failure. The 7 plain-view misses all come with a misread condition, a near miss acted on instead, or a contestable variant title. |
| **The judge** | 93 failures reported on valid tests, each reviewed: **85 true, 8 false positives**. The 8 are 3 replica artifacts (a read the answer needs broke: Linear's projects and comments queries) and 5 acts on near misses that the cold reader itself doubted (so contestable). 10 true positives were read by hand (and the 3 artifacts); the rest follow from construction (fdc says the near miss fails a condition; the target meets every one) or the PI's timeout rule. **False negatives: 0 of 231 passes** by the method's criterion (the set acted on, and no change outside the target table). The judge does not check the value written. In 31 of 39 passed Linear trials that name a priority, Qwen wrote the wrong one, 25 of them 4 (Low) for Urgent. The fact method's scoring has the same design; this is for discussion. |
| **Tokens and cost** | Muse: 144 calls (4 writer, 140 reader); 4.48 M input tokens, 0.32 M of them cached (7%: the cold reader is a fresh session per case by design); 0.38 M output. **$0.52 billed** ($7.26 at list prices). Solver: the self-hosted Qwen, no charge; 29.3 M input and 1.6 M output tokens over 465 attempts. |

## The pipeline

| Step | Who | What |
|---|---|---|
| Population | code | 91 single-target covers: fact_coverage_02's hand-built covers, autogen_01's 49 generated scenarios, autogen_02's 28 ([population.py](population.py)) |
| Plural request | Muse writer (one call per service) | plural-worthy or not, with the reason; the plural wording; the words a user would search with; three texts for the extra matches ([writer.py](writer.py)) |
| Wording check | code | no hiding place the original did not name |
| Easy tier | code | the target plus two copies in plain view ([build.py](build.py), [seedkit.py](seedkit.py)) |
| Hard tier | code | one trap per laziness behaviour that applies. Whether the request names its container (a channel, calendar, folder or team) comes from the reference query |
| Checks | code | the reference query selects exactly the targets and every near-miss claim still holds (fdc); no container over 200 records; every target's date the same in UTC and Los Angeles; no row breaks a unique key of the replica's schema |
| Cold reader | Muse, a fresh session per case | reads the request and every record of the kind, with containers and visibility, and must pick exactly the targets ([reader.py](reader.py)) |
| Repair | code, then the reader again | a case the reader doubts is rebuilt with the original texts; if it still doubts, without the traps it doubted |
| Shortcut check | code, on the replica | every shortcut of the request's kind run on the hard seed; the thorough route must find every target ([checks.py](checks.py)) |
| Runs | self-hosted Qwen, 3 trials | [runs/p3](runs/p3) first builds; [runs/p3r](runs/p3r), [runs/p3u](runs/p3u) repairs; [runs/p3c](runs/p3c), [runs/p3t](runs/p3t) iterations 2 and 3 |
| Judge | code | the set acted on against the targets; misses by placement; near misses acted on by fact ([grade.py](grade.py)) |
| Review | code and me | every reported failure against its ground ([review_verdicts.py](review_verdicts.py)); every pass for changes outside the target table ([side_effects.py](side_effects.py)) and for the value written ([effects.py](effects.py)) |

## Phase 2: does the automation meet the manual standard?

**On the manual's own four covers** (cycle 8 of several_match_02), the writer's plural wordings are the manual's in
substance. SLK-21's is word for word; the others say "all the" where the manual says "every". The automated hard
cases defeat the same shortcuts, except one:

| Cover | Automated (valid hard case) | Manual (cycle 8) |
|---|---:|---:|
| CAL-23 | 4 of 4 | 4 of 4 |
| BOX-23 | 3 of 5 | 4 of 5 |
| LIN-21 | 1 of 6 | 1 of 6 |
| SLK-21 | 3 of 8 | 3 of 8 |
| **All** | **11 of 23** | **12 of 23** |

- BOX-23 lost its "another folder" copy. The builder names that folder "Shared", and the cold reader doubted a
  contract kept there; the manual had put it in "Legal". The repaired case drops it.
- The shortcut it defeated (listing the guessed folder's tree) is still defeated for the kind by AP-BOX-02-HR,
  whose "another folder" copy the reader accepted.

**Qwen on those four covers reproduces the manual's findings:**
- It never found the copy on the hidden calendar (0 of 3), as in the manual.
- It missed the Linear issue past the first page once in 3 (manual: once in 3).
- Box and Slack were clean in every trial that finished. SLK-21's hard case had one timeout; the manual's had one
  too.
- One difference: it found the copy on the second, visible owned calendar in 2 of 3 trials (manual: 0 of 3).

**Over the whole population the automation goes past the manual study.** The manual built four covers by hand in
four request kinds. The automation reaches 49 covers with a route table, in six request kinds:
- **All 19 lazy, practical shortcuts are defeated** (table above).
- Hard tests exist for 39 covers.

**The creative surface stayed small.** Muse writes the plural wording, the search words and three texts per cover
(4 writer calls), and reads each built case cold (140 reader calls, a fresh session each). Everything else is code:
the traps come from the reference query and the route table, and the checks and grading are mechanical.

## Phase 3: what the tests found

**Targets found, by where they were placed** (valid tests, timeouts and voided trials out):

| Placement | Behaviour it tests | Found |
|---|---|---:|
| V, plain view | stopping early | 708 of 731 |
| C1, one folder down | scope | 5 of 5 |
| O, another folder | scope | 2 of 2 |
| C, another owned calendar | scope | **7 of 21** |
| H, behind a visibility default | visibility | **2 of 26** (hidden calendar 0 of 21; private channel 2 of 5) |
| P, past a page | pages | 58 of 65 |
| S, text lacking the search words | filter | 10 of 10 |

**What Qwen does, at scale:**
- **Calendar requests that name no calendar: it reads the primary calendar.** This held in all 7 calendar covers
  with a hard case:
  - it never found a copy on a hidden calendar;
  - it found the copy on a second, visible owned calendar in 7 of 21 trials.

  The manual study saw this in its one calendar cover (0 of 3 each); here it is general.
- **Linear: it sometimes reads one page.** It missed the issue past the first 50 in 3 covers with no other error,
  and in 2 more that also misread the condition.
- **Slack channels: it keeps the default channel list** in 3 of 6 trials, missing the private copy (the list
  shows public channels only).
- **Box: it walks folders and pages.** Every copy one folder down, in another folder, past a page, or unnamed by
  the search words was found in the trials that finished. A search that narrows away a target never caught it.
- **Stopping early: no clear case.** All 23 plain-view misses come with another failure:
  - a misread condition (the uploader field; the Linear priority scale, below);
  - a near miss acted on instead;
  - one contestable variant title ("Architecture review sync").
- **Discrimination:** 13 distinct (cover, fact) near misses acted on. G4-BOX-01 is the most striking: in 7 trials
  Qwen read "the PDFs with a top-level comment by Dana saying 'approved for launch'" as an instruction to post that
  comment, and did.
- **The priority scale:** Qwen believes Linear's priority 4 is Urgent; the replica's schema says 1 is. This both
  fails requests that select by priority (G4-LIN-02: no "priority 3" high-priority issues found) and writes the
  wrong value in passes (above).

**Timeouts:** 23 of 309 trials, a failure by the PI's rule. The self-host was shared with other sessions' runs, and
turns took a median of 17 to 38 s depending on the hour ([pace.py](pace.py)). The timeouts cluster where the turns
were slow and where the requests were hardest (Linear GraphQL, Box folders of 100 files). In 2 of them every target
had already been changed; the answer was cut off.

## Construction lessons (the iterations)

1. **Iteration 2: the traps the first round lacked.**
   - The first coverage table showed two construction gaps:
     - Box files in a named folder got only a search crowd; 5 of 6 such covers had no hard case.
     - Slack requests about channels got no trap.
   - `build.py --iterate2` added a copy past the named folder's first 100 items, and a private copy of a channel
     the actor belongs to.
2. **Practicality is about reading the condition, not only reaching the target.**
   - The folder page trap fills the first page with copies of one of the cover's own near misses. When those
     fillers fail a condition the listing does not show (an owner, an upload date, a comment, a task, a shared
     link), the thorough route must read each of 100 files. The replica's folder listings ignore `fields`.
   - Result: 7 of 18 trials timed out.
   - The shortcut check had passed: it confirms that the targets are reachable, not what reading their condition
     costs.
   - The method's check 6 ("no per-record calls to read the condition") refuses these five tests. The summary now
     applies it mechanically.
   - AR-BOX-23-HP stays valid: its fillers fail on the extension, which the names show, and all 3 of its trials
     completed.
3. **Iteration 3: for those requests the condition is not text,** so a search narrows with words that do not
   express it. `build.py --iterate3` places a copy whose name and description lack the search words, with no
   fillers. The reader accepted 4 of 5, and the searches are defeated.
4. **The replica's database has constraints the fdc checks do not see.**
   - Five easy cases did not install. The causes:
     - a writer variant reused a channel name;
     - a Linear project's copied issues kept their identifiers;
     - channel copies carried their messages with the same message ids.
   - seedkit now gives copied rows fresh keys, and `checks()` refuses any seed that breaks a primary key or unique
     constraint of the schema ([unique_check.py](unique_check.py)).
   - The four the reader had accepted are rebuilt (`-EU`) and ran.
5. **The runner's retry pass reloads the cases directory.** It ran the repaired and iteration-2 cases a second
   time inside runs/p3. [grade.py](grade.py) grades each case from its own run; the duplicate trials are kept on
   disk and not counted.
6. **What the automation does not do yet:**
   - The trap containers have fixed names ("Current", "Shared", "Team events", "Planning", "leads"). "Shared" was
     contested; the writer could name them.
   - The writer's variant titles are sometimes contestable. Qwen left out "Architecture review sync" as "a sync
     meeting, not an architecture review", though the reader accepted it.
   - Copies of Slack thread replies land before their parent message (two hard cases lost).
   - DM requests have no route table (one hard case refused).
   - 16 covers are record kinds with no route table, so they get the easy tier only.

## Replica defects seen (reported, not fixed)

- **Box:** `PUT /files/{id}` without `shared_link` in the body removes the file's shared link. The folder route
  treats an absent `shared_link` as unset; the file route passes null. Found in the values written by G4-BOX-03's
  passed trials.
- **Box:** folder listings ignore `fields`, so only names and ids come back (known). This is what makes a page trap
  impractical for any condition but the name.
- **Linear:** null connections raise "Cannot return null for non-nullable field" on:
  - `Query.projects`, `Query.project`, `ProjectConnection.nodes`;
  - `CommentConnection.nodes` (a comment's children);
  - `team.cycles` (`CycleConnection.nodes`);
  - `Query.issuePriorityValues`.

  Three failures were voided for this, where the read a correct answer needs broke.
- **Box:** search ignores `ancestor_folder_ids` and `file_extensions` (known).

## Files

- [population.py](population.py) → `population.json`; [writer.py](writer.py) → `writer.json`;
  [build.py](build.py) → `cases/`, `build.json`, `placements.json`; [reader.py](reader.py) → `reader.json`;
  [checks.py](checks.py) → `checks.json`; [grade.py](grade.py) → `grades.json`;
  [review_verdicts.py](review_verdicts.py) → `review.json`; [side_effects.py](side_effects.py),
  [effects.py](effects.py) → `effects.json`; [pace.py](pace.py); [unique_check.py](unique_check.py);
  [summary.py](summary.py) → `summary.json`.
- [probe_subfolder.py](probe_subfolder.py): a reader-only probe (`probes/`), not a test.
- Muse calls: `runs/calls.jsonl` and `runs/writer/`, `runs/reader/` (prompts, transcripts, usage).
- Solver runs: `runs/p3`, `runs/p3r`, `runs/p3u`, `runs/p3c`, `runs/p3t`, `runs/smoke`.
