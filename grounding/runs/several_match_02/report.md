# several_match_02: where to place the extra matches so that a lazy agent cannot pass

*2026-09-28. A manual investigation in eight cycles of build, run, analyze and iterate ([log.md](log.md)); question
and method in [plan.md](plan.md). Agent runs on the self-hosted Qwen; no Muse.*

## The question

The PI: "how do we pack or where do we pack the other matches so that a lazy agent cannot pass them."

A plural request ("every file…", "every message…") asks the agent to act on every record that meets its conditions.
A lazy agent takes a shortcut and passes whenever the shortcut happens to return every match. The design question
has three parts:
1. Which shortcuts exist, per service?
2. Where can a match go so that a given shortcut misses it? The match must stay in the request's scope and be
   reachable by a route that behaves as the real service does.
3. How many tests does it take to defeat every shortcut?

## The answer

1. **The shortcuts** are 30 lazy strategies over the four services: Box 8, Calendar 4, Linear 6, Slack 12. They are
   enumerated from the APIs' defaults and from the routes agents took (table 1). Each is an ordered list of real
   API calls, run against the replica.
2. **Where to put the matches.** Four kinds of place, each defeating a known set of shortcuts (table 2):
   - one or two containers down (subfolders, sub-teams, other channels in scope);
   - beyond the largest page, not merely the default one;
   - behind a visibility default (a hidden calendar, a private channel; for read requests, an archived channel or a
     DM);
   - with a condition no search or filter can express, so that the shortcut must enumerate.

   A place counts only under the validity rules below, which the cycles sharpened. The most consequential rule: the
   condition must come back on the thorough route, or a test that looks lazy-proof is void.
3. **How many tests:**
   - **Combined:** one test per service and kind of request defeats every shortcut defeatable in the replica, when
     that one seed holds every placement. That is 6 tests:
     - Box 1, Calendar 1 and Linear 1, each for the one kind of request enumerated;
     - Slack 3, one per kind: about channels; messages in a set of channels; messages anywhere.
   - **Without combining:** Box needs 2, and Slack 4.
   - **Not defeatable here:** Linear's two list-everything shortcuts, because the replica caps no page size.

For the agent (the feedback loop, not the design answer):
- Qwen was caught mainly behind visibility defaults.
- Pagination caught it only inside a combined test.
- Containers never caught it.

## Method

- **Terms** ([plan.md](plan.md)):
  - A **strategy** retrieves candidates, and for Linear also selects among them.
  - A **lazy** strategy covers only part of the request's scope. Its **generous variant** asks for the largest page
    (`limit=1000`, `first: 1000`, `count=100`). Visibility flags such as `showHidden` or private channel types are
    not generosity: they are the thorough behaviour under test.
  - The **thorough** strategy covers every respect of the scope at once (the whole tree, every page, every
    visibility). A test is valid only if it finds every match.
- **Cycles:**

  | Cycle | What | Agent runs |
  |---|---|---|
  | 0 | the pilot's 24 routes: generous pages, stated scopes followed | — |
  | 1–2 | the strategy matrix on 13 probe seeds; conditions no search expresses; selection modelled | — |
  | 3–4 | four lazy-proof tests (tree, hidden calendar, sub-teams, private channels) | 30 |
  | 5 | controls that name the hidden part; pagination beyond the largest page (void) | 20 |
  | 6 | pagination with a condition the listing shows; the numbers redone; combined seeds | 10 |
  | 7 | the combined tests | 20 |

  Every test was built and pre-checked by the kit (seed, reference, near misses, replica rules), run 5 times, and
  graded by id from the diff. Routes were read from the trajectories ([routes.py](routes.py)).

## Validity rules, as the cycles left them

- **Scope wording is a user's.** Contestable wordings are not used. Cycle 3 found that "my calendars" let 3 of 5
  trials count a team calendar the actor can edit; "the calendars I own" did not. Wordings that name the hidden part
  ("public or private", "including any I have hidden") hand it to the agent. They are used only as controls.
- **No replica gaps on the thorough route. The condition must come back on it, not just the ids.**
  - The runner counts retrieval, so this is checked by hand.
  - Missing it voided two tests in cycle 5: the Box replica's folder listing omits `modified_by` whatever `fields`
    asks, and the Slack replica's history omits `reactions`. Each condition then took one call per record.
- **The thorough route must fit the agent's time budget:** two pages of listing, not 1,100 per-record calls.
- **The request's action must be possible at every match.** A reaction in an archived channel fails, so for a write
  request, leaving archived channels out is right, not lazy.
- **The seed must make the thorough route a different query from the lazy one.** A small workspace lets "list
  everything" pass.
- **The condition must not leak into a searchable field.** SM2-SLK-04's matches read "Leo deployed…", so one trial
  found them by a text search; its verdicts stand.

## Table 1: the shortcuts, and what defeats each

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
| Slack: requests about channels | search → the channels of the hits; channel list (default types) | a private channel (topics are not searched) |
| Slack: messages anywhere | conversations of default types, or public and private → history | a match in a group DM or a DM |

## Table 2: the number of tests

`numbers.json` ([numbers.py](numbers.py)): the smallest set of valid seeds that defeats every lazy strategy.

| Service | Lazy strategies | Tests | Which | Run on the agent? |
|---|---:|---:|---|---|
| Box | 8 | 1 | BX-COMBINED (the named folder, two levels down, beyond a subfolder's first 1000 items; not a Word document) | yes: SM2-BOX-04 |
| Calendar | 4 | 1 | CL-HIDDEN (a hidden owned calendar) | yes: SM2-CAL-01 and SM2-CAL-02 hold the same placement |
| Linear | 6 | 1 | LN-COMBINED (sub-teams; a 75-issue named team). 2 strategies undefeatable (above) | partly: SM2-LIN-01 holds the sub-teams, not the default page |
| Slack | 12 | 3 | SK-CHANNELS (about channels); SK-COMBINED (messages in a set of channels); SK-DMS (messages anywhere) | SK-CHANNELS as SM2-SLK-01; SK-COMBINED as SM2-SLK-05, without its archived channel (a write request); SK-DMS not built |

- **Six tests** defeat every strategy that the replica lets be defeated. Box, Calendar and Linear had one kind of
  request enumerated each; more kinds would add tests.
- **Without combining** (one placement per test): Box 2, Calendar 1, Linear 2, Slack 4.

## Table 3: what caught the agent

Qwen on the self-host, targets acted on out of targets, valid tests only. The misses caused by the Slack POST gap
(table 4) are excluded.

| Placement | Found | Tests |
|---|---:|---|
| Visible | 115/115 | all |
| One or two containers down (subfolders, sub-teams, another channel) | 55/55 | SM2-BOX-01, SM2-LIN-01, the Calendar tests, SM2-BOX-04, SM2-SLK-05 |
| Beyond the largest page, as the only placement | 20/20 | SM2-BOX-03, SM2-SLK-04 |
| Beyond the largest page, inside a combined test | 7/10 | SM2-BOX-04 (1 miss: paged a 1,101-item subfolder with a 100-item second page and stopped at 1,100), SM2-SLK-05 (2 read one page) |
| **Behind a visibility default, the request not naming it** | **9/26** | hidden calendar 0/10 (SM2-CAL-01, -02); private channels 8/12 (SM2-SLK-01), 1/4 (SM2-SLK-05) |
| Behind a visibility default, the request naming it (control) | 13/13 | SM2-CAL-03, SM2-SLK-02 |

- **Near misses acted on:** 3 of 60 valid trials, all in SM2-CAL-01. Its contestable "my calendars" let the agent
  take Maya's writable calendar as its own. None after the wording became "the calendars I own".
- **The combined tests caught the agent more often than single placements:** SM2-SLK-05 was exact in 1 of 5. The
  comparison is small, and the kinds of request differ. [cycle 7b: to be added]
- **A candidate placement, seen once:** the last item of a listing just past a round page.

## Table 4: replica gaps met (reported, not fixed)

| Gap | Effect here | Beyond this study |
|---|---|---|
| Slack reads a POST's arguments from the body only (`_get_params_async`); real Slack also reads the query string | caused misses: 4 trials of SM2-SLK-01, 1 of SM2-SLK-02, 1 of SM2-SLK-05. Each asked for private channels in the query string and got public ones only | 27 of 1,044 recorded Slack trials (2.6%) send POST arguments only in the query string |
| Box folder listings return the mini fields whatever `fields` asks for (`_filter_fields` keeps only keys present); real Box expands `fields` | voided SM2-BOX-02 (the last modifier took 1,150 calls) | any test whose condition is a non-mini field of a listed item |
| Slack `conversations.history` omits `reactions`; real Slack includes them | voided SM2-SLK-03 (Leo's :rocket: took 1,100 calls) | any test about reactions over a long history |
| Linear accepts any `first`; real Linear caps pages (250) | two list-everything strategies cannot be defeated | pagination tests in Linear |

## Limits

- **One agent.** The design answers (tables 1 and 2) are mechanical and hold for any agent. Table 3 is Qwen's.
- **The shortcut list is enumerated, not exhaustive.** It comes from the APIs' defaults and the routes seen in about
  2,400 trajectories. A new kind of shortcut needs a new column in the matrix.
- **Not built:**
  - Calendar pagination (over 2,500 events in a window);
  - SK-DMS as an agent test;
  - LN-COMBINED as an agent test.
- **Small numbers:** 5 trials per test (10 for the combined tests).

## Files

- [plan.md](plan.md), [log.md](log.md) (cycles 0–7);
- [scenarios.py](scenarios.py) → `scenarios/`, built by [build.py](build.py) into `cases/` and `checks/`;
- [strategies.py](strategies.py) and [probes.py](probes.py) → `matrix.json`; [numbers.py](numbers.py) →
  `numbers.json`;
- [grade.py](grade.py) → `grades-c3.json` … `grades-c7.json`; [routes.py](routes.py) for routes;
- runs: `runs/c3` … `runs/c7b`, with `runs_c*.log`.
