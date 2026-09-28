# several_match_02: where to place the extra matches so that a lazy agent cannot pass

*2026-09-28. A manual investigation in nine cycles of build, run, analyze and iterate ([log.md](log.md)); question
and first plan in [plan.md](plan.md). Its result is a method, [method.md](method.md) (version 1.1): the standard
that automated several-match tests must meet. Agent runs on the self-hosted Qwen; no Muse.*

## The question

The PI: "how do we pack or where do we pack the other matches so that a lazy agent cannot pass them."

A plural request ("every file…", "every message…") asks the agent to act on every record that meets its conditions.
A lazy agent takes a shortcut and passes whenever the shortcut happens to return every match. The design question
has three parts:
1. Which shortcuts exist, per service?
2. Where can a match go so that a given shortcut misses it? The match must stay in the request's scope and be
   reachable by a route that behaves as the real service does.
3. How many tests does it take to defeat every shortcut?

## The answer: the method

1. **The shortcuts are the requirement space.**
   - A route covers a plural request's scope along five dimensions: containers, pages, visibility, the search
     filter, and selection.
   - A laziness behaviour falls short on one of them.
   - A shortcut is a behaviour instantiated on a service's route table (read from the replica) for one kind of
     request: the exact API calls a lazy agent makes.
   - The investigation found 30 over the four services (table 1). [route_table.py](route_table.py) generates all 30
     from the route table with rules that name no service, plus 9 more that were never tried.
2. **Where to pack the matches: one trap per behaviour.** A trap is a place where a match sits so that every
   shortcut of that behaviour misses it and the thorough route finds it:
   - one or two containers down, or in another container in scope;
   - past a page;
   - behind a visibility default;
   - a condition no search expresses, or a crowd of search hits past a search page.

   The strategy runner checks each trap by running every shortcut as API calls on the test's own seed.
3. **How many tests: one per plural cover scenario, in two tiers.**
   - Matches are valid-side inputs: the request presupposes them. So one test may carry every trap, as valid
     classes share a test in equivalence partitioning.
   - The test is a **plural cover case**: a cover scenario of the fact method whose request is meaningfully plural,
     its conditions and decoys kept, two matches in plain view, and the fewest trap matches that make every
     practical shortcut miss one.
   - **Easy tier:** plain view only. **Hard tier:** plain view and the traps.
4. **Eight checks before any run** decide validity (method.md). The ones the cycles found:
   - the condition must come back on the thorough route (two tests were void without it);
   - the action must be possible at every target;
   - practicality: no container over about 200 records, and the thorough route a handful of calls;
   - nothing but the condition links the targets;
   - the wording names no hiding place, and every date holds in UTC and the actor's time zone.
5. **Coverage is reported per cover scenario:** the shortcuts, those defeated, those not covered and why, and those
   the agent was caught by.
   - Every largest-page shortcut is out of practical reach except Slack's search page of 100, so those are
     reported, not built.
   - A shortcut can also be irrelevant to a request: when the named team is the whole scope, keeping the named team
     is not lazy.
6. **Plural probes are not part of it.** The fact method's zero-match probe loses its force when worded plurally:
   0 of 41 plural probe trials exposed a fact, where the singular wording exposed two on the same host (cycle 8).

## The method applied to four cover cases (cycle 8)

Four cover scenarios of fact_coverage_02: CAL-23, BOX-23, LIN-21, SLK-21 ([covers.py](covers.py)).
- Per scenario: an easy and a hard plural cover case.
- A crowd tier (H2) where the one-page search needed one.
- The fact method's probes, with plural wording.
- Checks in `covers_check.json`; 75 trials plus a 12-trial control.

**What the checks and the runs caught in the construction (fixed, and folded into method v1.1):**
- The first hard cases left the one-page search undefeated in Box and Slack. H2 adds a crowd of hits that fail
  only the comment count or the author.
- SLK-21's paged target sat at 03:00 UTC on September 23, which is September 22 in the actor's zone. It is void in
  H and H2; H3 moves it.

**Trap reach:**

| Scenario | Lazy shortcuts | Defeated | Not covered |
|---|---:|---:|---|
| CAL-23 (events on my calendars) | 4 | 4 | — |
| BOX-23 (files anywhere) | 5 | 4 | search at the largest page (200): a crowd over 200 |
| SLK-21 (messages in one channel) | 8 | 3 | 4 read one page of 999 messages: over 999 messages. The three channel-list variants reduce to the named channel's page, since #deploys is public and live. 1 is not lazy for this request (every page of the named channel) |
| LIN-21 (issues in one team) | 6 | 1 | 2 read 250 or 1,000 issues a page: over 250 issues. 3 are not lazy for this request (the team has no sub-teams; the filter expresses every condition) |

**Qwen (3 trials a case):**

| Tier | Complete | Missed a target | Timeout |
|---|---:|---:|---:|
| Easy (4 cases) | 12 | 0 | 0 |
| Hard (H, H2, H3; 7 cases) | 16 | 4 | 1 |

- **Calendar hard: 0/3 complete.** Every trial read only the primary calendar, missing the visible "Architecture
  board" calendar and the hidden one.
  - Earlier requests that named the scope ("the calendars I own") were followed 65/65.
  - This one names no calendar, and the agent took the default container.
  - Both trap targets sit on calendars the actor owns, so even the narrow reading "the calendars I own" includes
    them. The misses are not contestable.
- **Linear hard: 2/3.** One trial read the default 50 issues and missed the 51st.
- **Box and Slack hard: complete.** Every trial searched or listed at the largest page, which is out of practical
  reach.
- **Discrimination:** one decoy taken in 33 cover trials (LIN-21-E: the September 11 issue).
- **Timeouts:** 3 of 87 trials, all on SLK-21's date request, on a host shared with other jobs (median 31 s a turn).

## How the method was found (cycles 0–7b)

| Cycle | What | Agent runs |
|---|---|---|
| 0 | the pilot's 24 routes: generous pages, stated scopes followed | — |
| 1–2 | the strategy matrix on 13 probe seeds; conditions no search expresses; selection modelled | — |
| 3–4 | four lazy-proof tests (tree, hidden calendar, sub-teams, private channels) | 30 |
| 5 | controls that name the hidden part; pagination beyond the largest page (void) | 20 |
| 6 | pagination with a condition the listing shows; the numbers redone; combined seeds | 10 |
| 7, 7b | the combined tests, 10 trials each | 20 |
| 8, 8b | the method on four cover cases; the plural-probe control | 87 |

Cycles 0–7 used purpose-built seeds: [scenarios.py](scenarios.py), built by [build.py](build.py) and pre-checked by
the kit, graded by id from the diff ([grade.py](grade.py)).

### Table 1: the shortcuts, and what defeats each

Mechanical: every strategy run as API calls against every probe seed (`matrix.json`, [strategies.py](strategies.py),
[probes.py](probes.py)). "Defeated by" names the placement that makes the strategy miss a match.

| Service | Lazy strategy | Defeated by |
|---|---|---|
| Box (files in a folder) | list the named folder: default page, `limit=1000`, or every page | a match in a subfolder |
| | list the tree, one page per folder | a match beyond a subfolder's first 1000 items |
| | search by words, by extension, or by a person's name (below the folder) | a condition no search expresses (not a Word document; the last modifier) |
| Calendar (events on my calendars) | the primary calendar only (with or without text search) | a match on another owned calendar |
| | calendar list (default, or owner only) → each calendar | a match on an owned calendar hidden in the list |
| Linear (issues in a team) | the named team's issues; a server filter on the named team; every issue → keep the named team | a match in a sub-team |
| | every issue (default page of 50) | a match beyond the default page |
| | every issue (`first: 250` or `1000`) | **none in the replica:** it caps no page size |
| Slack: messages in a set of channels | the named channel's history (default, 999, or every page) | a match in another channel in scope |
| | channel list (default types) → history | a match in a private channel |
| | channel list, `exclude_archived` → history | a match in an archived channel (read requests only) |
| | channel list (public and private) → one page of history | a match beyond the largest page |
| | search by words (default or 100 results) | a condition search cannot express, or more hits than one search page |
| Slack: requests about channels | search → the channels of the hits | any request about channels: search does not cover topics |
| | channel list (default types) | a private channel |
| Slack: messages anywhere | conversations of default types, or public and private → history | a match in a group DM or a DM |

The purpose-built seeds needed 6 tests to defeat every strategy that the replica lets be defeated (`numbers.json`),
using placements past the largest page (1,100 items). The method's practicality check drops those, so the count
that matters now is per cover scenario (above).

### Table 2: what caught the agent in cycles 3–7b

Qwen on the self-host, targets acted on out of targets, valid tests only. The misses caused by the Slack POST gap
(table 3) are excluded.

| Placement | Found | Tests |
|---|---:|---|
| Visible | 130/130 | all |
| One or two containers down (subfolders, sub-teams, another channel), the request naming its scope ("the Finance folder", "the calendars I own") | 65/65 | SM2-BOX-01, SM2-LIN-01, the Calendar tests, SM2-BOX-04, SM2-SLK-05 |
| Beyond the largest page of the named folder or channel (the only placement) | 20/20 | SM2-BOX-03, SM2-SLK-04 |
| Beyond the largest page of a subfolder, or of one of several channels in scope (combined tests) | 14/20 | SM2-BOX-04 6/10, SM2-SLK-05 8/10 |
| **Behind a visibility default, the request not naming it** | **13/31** | hidden calendar 0/10 (SM2-CAL-01, -02); private channels 8/12 alone (SM2-SLK-01), 5/9 combined (SM2-SLK-05) |
| Behind a visibility default, the request naming it (control) | 13/13 | SM2-CAL-03, SM2-SLK-02 |

- **Every combined-test miss was a paging mistake,** not a failure to page:
  - a 100-item second page from offset 1000 that stopped one item short of `total_count` (3 trials);
  - one page of history (2);
  - a loop on `next_marker` without asking for markers (2).
- **The private-channel rate does not change with combining** (8/12 alone, 5/9 combined).
- **Near misses acted on:** 3 of 70 valid trials, all in SM2-CAL-01, whose contestable "my calendars" let the agent
  take Maya's writable calendar as its own. None after the wording became "the calendars I own".

## Table 3: replica gaps met (reported, not fixed)

| Gap | Effect here | Beyond this study |
|---|---|---|
| Slack reads a POST's arguments from the body only (`_get_params_async`); real Slack also reads the query string | caused misses: 4 trials of SM2-SLK-01, 1 of SM2-SLK-02, 1 of SM2-SLK-05. Each asked for private channels in the query string and got public ones only. Met again in cycle 8 (resent in the body) | 27 of 1,044 recorded Slack trials (2.6%) send POST arguments only in the query string |
| Box folder listings return the mini fields whatever `fields` asks for (`_filter_fields` keeps only keys present); real Box expands `fields` | voided SM2-BOX-02 (the last modifier took 1,150 calls) | any test whose condition is a non-mini field of a listed item |
| Slack `conversations.history` omits `reactions`; real Slack includes them | voided SM2-SLK-03 (Leo's :rocket: took 1,100 calls) | any test about reactions over a long history |
| Linear accepts any `first`; real Linear caps pages (250) | two list-everything strategies cannot be defeated | pagination tests in Linear |
| Box folder listings have no marker pagination (`usemarker`); real Box has it | none here: the two marker loops never asked for markers | an agent that pages by marker gets one page |
| **Box search ignores `ancestor_folder_ids` and `file_extensions`** (the route never passes them to the query); real Box narrows by both | none here: all 21 Box trials of cycle 8 and 6 earlier sent one, and each read the results' extensions and folders. A search returns more than asked, never less | an agent that trusts the filter can act on an out-of-scope or wrong-type file; 33 fact-method trials sent these filters |

## Limits

- **One agent.** The method and the trap reach are mechanical and hold for any agent. The Qwen tables are Qwen's.
- **Four cover scenarios, 3 trials a case.** The plural-probe answer rests on small counts, with a direction that
  fits the wording's presupposition.
- **Checks by eye:** whether the condition comes back on the thorough route, and the time-zone rule.
- **Shortcut enumeration:** generated from the route table, but the runner still uses hand-coded functions, and the
  9 generated shortcuts never tried were not run on the agent.
- **A shared host:** the median turn took 31 s in cycle 8, so the 480 s budget held 8 to 16 turns.

## Files

- [method.md](method.md) (the result), [log.md](log.md) (cycles 0–8b), [plan.md](plan.md).
- Cycle 8: [covers.py](covers.py) → `cases_cover/`; [covers_check.py](covers_check.py) → `covers_check.json`;
  [grade_covers.py](grade_covers.py) → `grades-c8.json`, `grades-c8b.json`, `grades-c8c.json`;
  [route_table.py](route_table.py) → `route_table.json`.
- Cycles 0–7: [scenarios.py](scenarios.py) → `scenarios/`, built by [build.py](build.py) into `cases/` and `checks/`;
  [strategies.py](strategies.py) and [probes.py](probes.py) → `matrix.json`; [numbers.py](numbers.py) →
  `numbers.json`; [grade.py](grade.py) → `grades-c3.json` … `grades-c7b.json`; [routes.py](routes.py).
- Runs: `runs/c3` … `runs/c8c`, with `runs_c*.log`.
