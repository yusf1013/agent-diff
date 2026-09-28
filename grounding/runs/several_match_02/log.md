# several_match_02 log

One entry per cycle: what changed, what ran, what was learned.

## Cycle 0: the pilot's routes (2026-09-28, no runs)

**What ran:** [routes.py](routes.py) over several_match_01's 24 plural trials (the self-hosted Qwen).

**What was learned:**
- **Generous quantities almost always.** The agent asked for `limit=1000`, `limit=999`, `limit=200`,
  `maxResults=250` or `count=100` in nearly every listing or search. The one pagination miss was an unfiltered
  GraphQL `issues` query at Linear's default of 50 (SM-LIN-01 t1).
- **Recursion when the request states the scope:**
  - "including the ones in its subfolders": 3/3 listed every subfolder;
  - "on the calendars I own": 6/6 listed the owned calendars (`minAccessRole=owner`) and queried each;
  - "and its sub-teams": the agent read the team tree and filtered on all three team ids, or listed every issue.
- **Server-side filters whenever they work** (Linear: team, assignee, state, labels).
- **"Stops after the first batch": 1 of 24** (SM-LIN-01 t1, the unfiltered page). In SM-BOX-01 (2 matches in the
  named folder, then 2 in subfolders) the agent went on into the subfolders 3/3. In SM-LIN-01 t3 it widened a narrow
  filter after finding 2.
- **The placements were all explicit.** Every hidden place was named by the request's wording (subfolders, owned
  calendars, sub-teams) or fell to a larger page. So the pilot tested whether the agent follows a stated scope, and
  it does.

**The replica's defaults that hide records** (checked in the code; they are faithful):
- Calendar `calendarList` leaves out hidden calendars unless `showHidden=true`;
- Slack `conversations.list` lists only public channels unless `types` includes `private_channel`;
- Linear `issues` leaves out archived issues unless `includeArchived: true`;
- Box `search` requires a query term (as real Box does).

These, and scopes that span containers, are the candidate hiding places for cycle 1.

**Measurement note:** routes.py matched records by name as well as by id. Calendar events that share a title were
therefore counted together. From cycle 1 it matches by id only.

## Cycle 1: the first strategy matrix (2026-09-28, mechanical, no agent runs)

**What was built:**
- [strategies.py](strategies.py) runs each strategy as real API calls against the replica.
- [probes.py](probes.py) has 9 probe seeds, each isolating one candidate hiding place.
- Results are in `matrix.json`.

**What ran:** every strategy of each service on every probe (5–6 strategies per service, one environment per probe).

| Probe (place) | Strategies that miss a match | Strategies that find all |
|---|---|---|
| BX-TREE (subfolders, 1–2 levels) | list named folder (default and limit 1000); search by the folder's name | search `pdf` below the folder (limit 200); list the tree |
| BX-PAGE (150-item folder) | list named folder (default page); search by the folder's name | list named (limit 1000); search `pdf` below the folder |
| CL-OWNED (owned secondary calendars) | primary only (with or without text search) | calendar list → each calendar (any variant) |
| **CL-HIDDEN (an owned calendar hidden in the list)** | primary only; calendar list (default); calendar list (owner only) | calendar list with `showHidden=true` → each |
| LN-PAGE (70 issues) | all issues (default page of 50) | all issues (first 250); named team; server filter |
| LN-SUBTEAM (2 sub-teams) | named team's issues; server filter on the named team | all issues (the workspace is small); team tree |
| SK-PRIVATE (a private channel in a name-prefix scope) | named channel's history; channel list (default types) | search (text); channel list with private types |
| SK-HISTORY (140 messages) | named channel history (default 100) | history (limit 999); search |
| SK-SEARCH (34 other messages match the words) | search (default count 20); history (default) | search (count 100); history (limit 999) |

**What was learned:**
- **Quantity placements never hide from the generous variant.** Beyond-the-first-page fails in all four services,
  as the pilot's routes predicted. Page size is not a hiding place for an agent that asks for big pages.
- **One placement defeats every shortcut tried: a hidden calendar the actor owns.** Only `showHidden=true` finds
  it. Hiding here comes from a visibility default, not from quantity or structure.
- **A container scope hides a match only when no single query spans the containers:**
  - a Box tree falls to one search below the folder whenever the condition is searchable (here the `pdf`
    extension);
  - Linear sub-teams fall to "list every issue" in a small workspace;
  - a private Slack channel falls to search, because search spans private channels and the condition is text.
- **The next hypothesis:** a hiding place works when a structural scope (a tree, a team hierarchy, channel
  privacy) combines with a condition that no search or filter can express. That combination forces enumeration of
  the containers.

**Next (cycle 2, mechanical):**
- a Box tree with a condition search cannot express (the last modifier, which listings show);
- Linear sub-teams in a workspace too large to list at once (over 250 issues; also check whether the replica caps
  `first`);
- a Slack request about channels (search does not search topics), with private channels in scope;
- Slack archived channels, to see what search and `exclude_archived` do.

## Cycle 2: conditions no search can express, and selection (2026-09-28, mechanical)

**What changed:**
- Box: a person-name search strategy.
- Linear:
  - `first: 1000`;
  - strategies that model selection as well as retrieval ("retrieve every issue, then keep the named team" against
    "…keep the team tree");
- Slack:
  - channel-level strategies (a request about channels, where search does not help);
  - `exclude_archived`.
- New probes: BX-TREE-MOD, LN-SUBTEAM-BIG, SK-CHANNELS, SK-ARCHIVED.

| Probe (place) | Lazy strategies that miss | Strategies that find all |
|---|---|---|
| **BX-TREE-MOD** (tree; condition: the last modifier; mixed file types) | list named (both); search by the folder's name, the extension, the person's name | list the tree only |
| LN-SUBTEAM(-BIG) (sub-teams; 5 or 285 issues) | named team's issues; server filter on the named team; all issues → keep the named team | all issues → keep the team tree; the team tree's issues |
| **SK-CHANNELS** (a request about channels; 2 of the 4 are private) | search (it does not cover topics); channel list (default types) | channel list with private types only |
| SK-ARCHIVED (an archived channel in the scope) | named channel history; channel list with `exclude_archived` | search (it covers archived channels); channel list (default) |

**What was learned:**
- **The hypothesis holds on these probes.** A structural scope hides a match when the condition cannot be put into a
  search or a filter:
  - the last modifier in Box (real Box search has no modifier filter, and search needs a query term);
  - channel topics in Slack (search covers messages, not topics).
- **Laziness can be in the selection, not the retrieval.** In Linear an agent can fetch every issue and still drop
  the sub-teams' issues by keeping only the named team. The strategies must model both steps. With selection
  modeled, sub-teams hide in a small workspace too.
- **Workspace size does not help in the replica.** The replica does not cap `first` (1000 works; real Linear's
  documented maximum is 250), so "list everything" always fits in one page here.
- **Archived channels are a weak hiding place.** Only an agent that passes `exclude_archived=true` misses them;
  search and the default listing include them.
- **For Slack message requests, no hiding place survives search** in these probes. Search spans every channel the
  bot is in (private and archived included) and matches the text.

**The candidate lazy-proof placements, one per service, for agent tests (cycle 3):**
- see below.

## Cycle 3: four lazy-proof tests on the self-host (2026-09-28)

**What ran:** SM2-BOX-01, SM2-CAL-01, SM2-LIN-01 and SM2-SLK-01, built and checked by the kit (build.py, checks/).
On their own seeds the strategy runner confirms that every lazy strategy misses a match and the thorough one finds
all. 5 trials each on the self-hosted Qwen: runs/c3, graded in grades-c3.json, routes read with routes.py.

| Placement class | Targets acted on |
|---|---|
| V (visible) | 40/40 |
| C1, C2 (one or two levels into a folder tree or team tree the request states) | 35/35 |
| **H (behind a visibility default: a hidden owned calendar, private channels)** | **2/15** |

| Test | Trials | What happened |
|---|---|---|
| SM2-BOX-01 (tree, last modifier) | 5 exact | listed every subfolder with `limit=1000` |
| SM2-LIN-01 (sub-teams, depth 2) | 5 exact | read the team tree, then filtered on every team id |
| SM2-CAL-01 (hidden owned calendar) | 0 exact: 2 incomplete, 3 both | never asked for hidden calendars (`showHidden`), in 5 of 5; also deleted the Vendor sync on Maya's writable calendar in 3 of 5 |
| SM2-SLK-01 (private channels) | 1 exact, 4 incomplete | see the mock gap below |

**What was learned:**
- **The structural hiding places do not catch this agent.** When the request states the scope ("anywhere in the
  Finance folder", "or any team under it"), Qwen walks the whole tree, every time. They still defeat every lazy
  strategy, so they remain valid tests for lazier agents.
- **Visibility defaults catch it.** A calendar the actor owns but has hidden, and private channels, are left out by
  the API's defaults unless the agent asks. Qwen asked in 1 of 10 trials.
- **A mock gap inside the Slack result.** The Slack replica reads a POST's arguments from the body only. A POST
  whose arguments are in the URL's query string gets the defaults (`_get_params_async`).
  - Real Slack accepts arguments in the query string.
  - Two of the four Slack misses (t2, t4) asked for `types=public_channel,private_channel` that way and got only
    public channels. Those misses are the mock's.
  - The genuine misses are t1 and t3, which never asked for private channels: 2 of the 3 trials that were not
    affected by the gap.
  - Across all 1,044 recorded Slack trials, 27 (2.6%) sent a POST with arguments only in the query string. This is a
    benchmark-wide mock gap to report, not to fix here.
- **"On my calendars" is contestable.** Three trials counted Maya's team calendar, which the actor can edit but does
  not own, as "my calendar". The pilot's "the calendars I own" had no such error. Cycle 4 uses "the calendars I own".

**Next (cycle 4):**
- (planned) SM2-CAL-01 with "the calendars I own";
- SM2-SLK-01 again, with more trials, graded per trial for whether the agent asked for private channels and whether
  the mock honoured it;
- more visibility defaults, mechanically first: group DMs and DMs in a message-level Slack request (search may
  cover them), and archived Linear issues.

- **Box:** a folder tree (depth 1 and 2), with a condition listings show but search cannot express (the last
  modifier).
- **Calendar:** an owned calendar that is hidden in the calendar list.
- **Linear:** sub-teams (depth 1 and 2), with the scope stated. The stated scope hands the hiding place to the
  agent, which is recorded.
- **Slack:** a request about channels, with private channels in scope.

## Cycle 4: the Calendar wording, more Slack trials, and DMs (2026-09-28)

**What changed:**
- SM2-CAL-02 is SM2-CAL-01 with "on the calendars I own" instead of "on my calendars".
- SM2-SLK-01 ran again.
- A mechanical probe, SK-DMS, tests a message-level request with no channel scope: matches in public channels, a
  group DM and a DM.
- The grader now matches records by id only. Cycle 3's "first seen" for the hidden event was a shared title, not
  the event; every H miss is in fact "never retrieved".

**What ran:** 5 trials each of SM2-CAL-02 and SM2-SLK-01 (runs/c4, grades-c4.json).

| Test | Trials | What happened |
|---|---|---|
| SM2-CAL-02 (hidden owned calendar, "the calendars I own") | 5 incomplete | every trial listed calendars with `minAccessRole=owner` and no `showHidden`; the hidden calendar was never retrieved; no near miss acted on |
| SM2-SLK-01, again | 3 exact, 2 incomplete | all five asked for private channels. The two misses asked only in a POST query string, which the mock ignores |

**The two tests over both cycles:**
- **Hidden owned calendar:** missed in 10 of 10 trials.
  - Qwen enumerates the calendars it owns, but never asks for hidden ones.
  - With "the calendars I own", the near miss on Maya's writable calendar is never acted on (0/5, against 3/5 with
    "my calendars").
- **Private channels:** 4 exact and 2 genuine misses (never asked) in the 6 trials the mock gap did not affect. The
  other 4 trials asked correctly and were defeated by the mock.

**SK-DMS (mechanical):** the replica's search covers group DMs and DMs, so a text condition finds them all. Only
channel-list routes that do not ask for `mpim,im` miss them. A DM is a hiding place only for requests that search
cannot express.

**What was learned:**
- **Where to put the extra matches so that this agent cannot pass: behind a visibility default the request's scope
  includes but does not name.**
  - A hidden calendar the user owns: 10/10 missed.
  - Private channels, for a request about channels: 2 of 6 valid trials missed.
- **Stated structural scopes are followed:**
  - folder trees and sub-team trees: 0 misses in 10 trials;
  - owned calendars that are visible: 0 misses in 10.
- **The hidden-calendar result does not depend on the contestable wording.** It holds with "the calendars I own".

## Cycle 5: controls, and pagination beyond the largest page (2026-09-28)

**Why:** cycles 3–4 found that visibility defaults hide matches from Qwen, and that stated structural scopes do not.
Two questions follow.
- **Is the miss caused by the default, or by an inability?**
  - SM2-CAL-03 names hidden calendars in the scope ("including any I have hidden").
  - SM2-SLK-02 says "public or private".

  If Qwen then finds everything, the defaults are the hiding place.
- **Does Qwen follow pagination when even its largest page leaves matches behind?** The generous variant always
  won in cycles 1–4, because no seed was larger than one big page.
  - SM2-BOX-02 has a 1,150-file folder. The condition (the last modifier) is one search cannot express, so a listing
    is the only route, and `limit=1000` leaves two matches for page 2.
  - SM2-SLK-03 has an 1,100-message channel. The condition (Leo's :rocket: reaction) is one search cannot express,
    and `limit=999` leaves the two oldest matches.

**Mechanical check:** on both pagination seeds, only paging through every page finds all four matches. Every
single-page route misses two, including the tree and channel-list routes that were thorough on the smaller seeds.

**What ran:** 5 trials of each test (`runs/c5`, `grades-c5.json`).

| Test | Trials | What happened |
|---|---|---|
| SM2-CAL-03 (hidden owned calendar, "including any I have hidden") | 5 exact | every trial asked for `showHidden=true` |
| SM2-SLK-02 (private channels, "public or private") | 4 exact, 1 incomplete | every trial asked for private channels. The one miss asked in a POST query string, which the mock ignores |
| SM2-BOX-02 (1,150 files; the last modifier) | **void** | 1 exact; 4 ran out of time with no change |
| SM2-SLK-03 (1,100 messages; Leo's :rocket:) | **void** | all 5 ran out of time. One still reacted to all four matches, after checking reactions message by message over both pages; two reacted to the newest message, which is not a match; two changed nothing |

**Both pagination tests are void.** Their conditions are not visible on the route the test depends on.
- The Box replica's folder listing returns only the mini fields (id, name, etag), whatever `fields` asks for.
  `_filter_fields` only keeps keys the item already has. Real Box returns `modified_by` when asked.
- The Slack replica's `conversations.history` returns no `reactions`. Real Slack includes them on each message.

So the condition took one call per record, 1,150 or 1,100 of them, and the time budget ran out. The paging itself
was not the obstacle:
- 3 of the 4 Box trials asked for `offset=1000`;
- the one exact trial paged, then fetched each file.

The plan's validity rules already listed the Box trap, but the strategy runner counts retrieval: it records a match
as found when its id comes back, not when its condition does. **A test must also be checked for whether the
condition's field comes back on the thorough route.** This is now checked by hand before a test is built.

**What was learned:**
- **The visibility defaults are the hiding place, not an inability.** With the hidden calendars, or the private
  channels, named in the request, Qwen finds them: 5/5, and 4/5 plus 1 mock miss. Without naming them: 0/10 and 4/6.
- **Two more replica gaps** (Box listing `fields`, Slack history `reactions`) join the Slack POST query-string gap
  on the list to report.

## Cycle 6: pagination with a condition the listing shows; the numbers, redone (2026-09-28)

**What changed:**
- **SM2-BOX-03** (SM2-BOX-02's folder): "Add the tag legal-hold to every PDF in the Contracts folder."
- **SM2-SLK-04** (SM2-SLK-03's channel): "Add an :eyes: reaction to every message Leo Park posted in #deploys."

  Both put 2 matches beyond the largest page (1000 and 999), and the name or the author is in every listed record.
- **The runner's labels.** A route thorough in one respect only is now lazy:
  - the folder tree with one page per folder;
  - every page of one folder;
  - private channels with one page of history.

  The thorough route covers every respect: the tree with every page, or public and private channels with every page
  of history.
- **Combined seeds** (mechanical): one seed per service holding every placement that service allows, under a
  condition search cannot express.
  - BX-COMBINED: the named folder, two levels down, and beyond the first 1000 items of a subfolder, for "not a Word
    document".
  - SK-COMBINED: the newest page, beyond the largest page, a private channel and an archived channel, for the
    author.
  - LN-COMBINED: sub-teams, and a 75-issue named team that overflows the default page.

**What ran:** 5 trials each of SM2-BOX-03 and SM2-SLK-04 (`runs/c6`, `grades-c6.json`).

| Test | Trials | Route |
|---|---|---|
| SM2-BOX-03 | 5 exact | all 5 paged past the first 1000 items (`offset=1000`, or a loop) |
| SM2-SLK-04 | 5 exact | 2 paged the history with the cursor; 3 used search (`from:` twice; the phrase "Leo deployed", which the seed's texts carry, once) |

Recall beyond the largest page: 20/20.

**The numbers, redone** ([numbers.py](numbers.py), `numbers.json`): the smallest set of valid probes that defeats
every lazy strategy.

| Service | Lazy strategies | Tests needed | Which |
|---|---:|---:|---|
| Box | 8 | 1 | BX-COMBINED |
| Calendar | 4 | 1 | CL-HIDDEN |
| Linear | 6 | 1 | LN-COMBINED. Two list-everything strategies (`first: 250`, `first: 1000`) are defeated by no placement: the replica caps no page size, so a large enough page always holds everything |
| Slack | 12 | 3 | one per kind of request: SK-CHANNELS (about channels), SK-COMBINED (messages in a set of channels), SK-DMS (messages anywhere) |

Without combining (one placement per test), Box needs 2 and Slack 4.

**What was learned:**
- **Pagination does not hide matches from Qwen.** When the listing shows the condition, it pages past the largest
  page or filters on the server, every time. With container depth (cycles 3–4), pagination and depth are both
  followed. Only the visibility defaults catch this agent.
- **One test per service and kind of request can defeat every lazy strategy we know of.** This works if the test
  combines the placements in one seed, under a condition no search expresses and that the listings show.
- **Two constraints on combining:**
  - The thorough route must fit the time budget: a folder of 1,100 items takes 2 calls; a condition checked per
    record takes 1,100.
  - A write request cannot use a placement where the write is impossible. A Slack reaction in an archived channel
    fails, so for a write request, leaving archived channels out is right, not lazy.

**Next (cycle 7):** run the combined tests on the agent: SM2-BOX-04 (BX-COMBINED as a request) and SM2-SLK-05
(SK-COMBINED without its archived channel, plus a second public channel).

## Cycle 7: the combined tests on the agent (2026-09-28)

**What ran:** 5 trials each (`runs/c7`, `grades-c7.json`).
- SM2-BOX-04: "Add the tag q3-review to every file anywhere in the Finance folder that isn't a Word document."
- SM2-SLK-05: "Add an :eyes: reaction to every message Leo Park posted in the channels whose names start with
  incident-."

Both defeat every lazy strategy on their seeds.

| Test | Trials | Misses |
|---|---|---|
| SM2-BOX-04 | 4 exact, 1 incomplete | t2 walked the whole tree and paged the 1,101-item subfolder with `offset=1000&limit=100`, then stopped. The match was item 1,101 (`total_count` said 1101) |
| SM2-SLK-05 | 1 exact, 4 incomplete | **private channel:** missed in 4 of 5. Three never asked for private channels (`types=public_channel`); one asked in a POST query string, which the mock ignores. **beyond the largest page:** missed in 2 of 5, which read one page of the 1,100-message channel |

Recall by placement: visible 15/15; container 10/10; beyond a page 7/10; private channel 1/5.

**What was learned:**
- **The combined tests caught the agent more often than the single-placement tests did.** Counts side by side:
  - Beyond-a-page matches: 20/20 found when they were the test's only placement (cycle 6); 7/10 here.
  - Private channels: 4 of 6 valid trials found them in cycles 3–4, 1 of 5 here (1 of 4 without the mock's miss).

  The comparison is small (5 trials a test), and the requests differ in wording and kind: a channel-level request
  against a message request over several channels. So it suggests, and does not show, that combining makes a test
  stronger as well as saving tests. Five more trials of each run next (`runs/c7b`).
- **A candidate placement:** the last item of a listing whose length is just past a round page. One trial paged with a
  smaller second page and stopped short of `total_count`. That is one trial, not a finding.

## Cycle 7b: five more trials of each combined test (2026-09-28)

**Why:** cycle 7's comparison rested on 5 trials a test.

**What ran:** 5 more trials each (`runs/c7b`, `grades-c7b.json`).

| Test | Cycle 7 | Cycle 7b | Pooled |
|---|---|---|---|
| SM2-BOX-04 | 4 exact | 2 exact | 6/10 exact; the match beyond the subfolder's first 1000 items found 6/10 |
| SM2-SLK-05 | 1 exact | 4 exact | 5/10 exact; private channel 5/10 (5/9 without the mock's miss); beyond the largest page 8/10 |

**The four Box misses** were all paging mistakes on the 1,101-item subfolder, with `total_count` ignored each time:
- twice, a 100-item second page from offset 1000, which stopped at item 1,100;
- twice, a loop on `next_marker` without `usemarker=true`. In offset mode no marker comes back, real Box
  included, so the loop ended after one page.

**The private-channel miss** never asked for private channels.

**What was learned (revising cycle 7):**
- **Beyond the largest page: 20/20 alone, 14/20 inside a combined test.** The difference holds with 10 trials a
  test. Every combined-test miss was the agent paging wrongly, not failing to page at all.
  - In the combined tests the page to overflow was a subfolder's or a second channel's, not the named one's.
  - So two readings fit: combining weakens the agent, or paging a nested container is where it slips. A test that
    puts the long listing in a subfolder, with no other placement, would tell them apart.
- **Private channels: about the same alone (8/12, SM2-SLK-01) and combined (5/9).** Cycle 7's 1 of 4 was small-sample
  noise. The visibility default catches the agent in both settings.
- **The candidate placement recurs:** 2 of the 4 Box misses stopped at a round offset, one item short of the end.
- **Also:** the Box replica has no marker pagination for folder items (it has it only for hubs). No trial here was
  hurt by it: the two marker loops never asked for markers. But an agent that did ask would meet the gap.
- **The hiding places that catch Qwen, over all cycles:**
  - behind a visibility default (hidden calendars, private channels): caught in most trials;
  - beyond the largest page, only in combination (3 of 10) or at the list's end (1 of 5);
  - one or two containers down: never (0 of 25).

## Cycle 8: the method on four cover cases of the fact method (2026-09-28)

**The question.** Method v1 ([method.md](method.md)) was written from purpose-built seeds. Does it build valid
tests from the fact method's own cover scenarios? How far do its traps reach there? And does a plural probe add
anything over the plural covers (method.md, "Open question")?

**What was built** ([covers.py](covers.py); checks in [covers_check.py](covers_check.py), `covers_check.json`).
Four cover scenarios of fact_coverage_02 whose request is meaningfully plural:

| Scenario | Plural request | Hard-tier traps |
|---|---|---|
| CAL-23 | "Delete Friday's architecture reviews that Kenji Sato (kenji.sato@northwind.example) attends as an optional guest." | a target on another owned calendar ("Architecture board", visible); one on a hidden owned calendar |
| BOX-23 | "Add the tag renewal to every contract PDF whose description mentions the Initech renewal, that is larger than 2 MB and has at least three comments." | a target one folder down (Contracts/2026); one in another folder (Legal) |
| LIN-21 | "Assign to Priya Nair every Web team issue about the login redirect that Omar Haddad created on September 10." | a target past the first 50 issues (44 older Web issues) |
| SLK-21 | "Add a :thumbsup: reaction to every message Priya Sharma posted in #deploys on September 23 about the rollback." | a target past the first 100 messages of #deploys (150 posts that day) |

- Per scenario: the easy tier E (3 targets in plain view), the hard tier H (2 in plain view plus the traps), and
  the fact method's probes of the scenario with plural wording (P1…, 12 probes; the seed and the one decoy
  unchanged, "the" → "every", "If there isn't one" → "If there aren't any").
- The covers' conditions and decoys are unchanged. All 22 cases passed the fact checks and the preflight.

**Cycle 8b: two construction errors, found by check 2 and by one trial.**
1. **Check 2 failed for the one-page search in two hard cases.**
   - BOX-23-H: the condition is text that search expresses, and all its hits fit on Box's default search page (30).
   - SLK-21-H: its 25 rollback drills overflowed Slack's default search page (20), but not the largest (100).

   H2 adds a crowd of hits that fail the condition. For Box: 32 "Initech renewal redline" PDFs over 2 MB with
   fewer than three comments, so that real Box's size and extension filters keep them too. For Slack: every
   #deploys post mentions the rollback.
2. **SLK-21-H's paged target was on another day in the actor's time zone.** It sat at 03:00 UTC on September 23:
   20:00 on September 22 in Los Angeles, the actor's zone per `users.list`. It was found when one trial timed out
   while converting the timestamps to Los Angeles time. The cover had kept its target and its date decoy where both
   readings agree; the trap did not.
   - The placement is void in H and H2 (`grade_covers.py`, VOID): its target is neither required nor an error.
   - H3 moves it to 07:10 UTC (00:10 on September 23 in Los Angeles), with H2's crowd. H3 passes every check.
   - The other scenarios hold in both readings: Linear's dates sit between 08:00 and 18:00 UTC, and Calendar's
     events carry the calendar's own zone, the reading the fact method uses.

The runner's retry pass reloads the case directory, so H2 ran inside `runs/c8` (its `plan.json` predates them;
each attempt keeps its `case.json`). H3 ran in `runs/c8b`.

**Trap reach on the real covers** (the strategy runner on each hard seed):

| Scenario | Lazy shortcuts | Defeated | Not covered |
|---|---:|---:|---|
| CAL-23 | 4 | 4 (H) | — |
| BOX-23 | 5 | 3 (H), 4 (H2) | search at the largest page (200): needs a crowd of more than 200 hits |
| SLK-21 | 8 | 2 (H), 3 (H2, H3) | 5 read #deploys 999 messages a page: need more than 999 messages |
| LIN-21 | 6 | 1 (H) | 2 read 250 or 1,000 issues a page: need more than 250 issues. 3 are not lazy for this request: the Web team is the whole scope (no sub-teams; Web Platform is the decoy's team), and the server filter can express every condition |

On real covers the practical traps are:
- another container, where the scope has several (calendars, folders);
- a visibility default;
- the default page;
- a crowd past the default search page.

Every largest-page shortcut is out of practical reach except Slack's search (100). The practicality rule reports
them as not covered, as intended, instead of building 1,000-item seeds.

**Qwen on the self-host** (3 trials a case; `runs/c8`, `runs/c8b`; [grade_covers.py](grade_covers.py) →
`grades-c8.json`, `grades-c8b.json`):

| Case | Complete | Missed | What was missed |
|---|---:|---:|---|
| CAL-23 E / H | 3 / 0 | 0 / 3 | H: the target on the visible "Architecture board" calendar and the one on the hidden calendar, in every trial |
| BOX-23 E / H / H2 | 3 / 3 / 3 | 0 | — |
| LIN-21 E / H | 3 / 2 | 0 / 1 | H t2: the 51st issue |
| SLK-21 E / H / H2 | 3 / 2 / 3 | 0 | H t3 timed out (a failure) before acting; the paged target is void in H and H2 |
| SLK-21 H3 | 3 | 0 | — (every trial read #deploys at 999 or 1,000 a page; t2's first search and history calls put their arguments in a POST query string, the replica's known gap, and it resent them in the body) |

Targets found by placement (timeouts and void targets excluded): plain view 76/76; one folder down 6/6; another
folder 6/6; another owned calendar 0/3; hidden calendar 0/3; past the first page 5/6 (Linear 2/3, Slack H3 3/3).

- **Calendar: every hard trial read only the primary calendar.** It made one `events.list` call and never listed
  the calendars. It missed the visible "Architecture board" calendar as well as the hidden one, so the miss is scope,
  not visibility; the plain container match disambiguates, as the scoring rule intends. In cycles 3–7 containers
  never caught the agent (65/65), but those requests named the scope ("the calendars I own", "anywhere in the Finance
  folder"). This request names none, and the agent took the default container.
- **Linear: one trial listed issues without `first` or `pageInfo`** and got the default 50.
- **Box: every trial searched** at 100 or 200 results a page and read the condition from the results. H2's crowd
  (about 40 hits) fit on one such page. That is the largest-page shortcut, not covered in practice.
- **Slack: every trial read #deploys at 999 messages a page,** or searched with `from:` and a channel. Nothing past a
  page was missed.
- **Discrimination on the covers:** one decoy taken in 33 cover trials. LIN-21-E t3 filtered `createdAt >= 2024-09-10`
  (the wrong year, no upper bound), never read the dates, and assigned the September 11 issue as created on
  September 10.
- **Timeouts: 2 of 75 trials, and 1 of the control's 12.** All three were on SLK-21's request, in 5 to 8 long turns:
  - H t3 was converting the timestamps to Los Angeles time;
  - P2 t1 was widening the date window;
  - the control's P-SLK-21-I12 t1 met the POST query-string gap, resent its search, then produced two turns with no
    action.

  The self-host was shared with other jobs: median 31 s a turn, p90 61 s (84 trials of this cycle). So the 480 s
  budget held 8 to 16 turns.

**The probe question: does a plural probe expose a fact that the plural covers do not?**
- **Plural probes:** 0 of 41 answered trials took the decoy or presented it as the match (1 timeout). Every answer
  said there were none and named why the near miss fails.
- **The same four probes with singular wording,** run as a control on the same self-host the same hour (`runs/c8c`,
  `grades-c8c.json`); their first run was on Purdue on 2026-09-25:

  | Probe (fact) | Singular, Purdue | Singular, self-host | Plural, self-host | Plural covers (E, H) |
  |---|---:|---:|---:|---:|
  | P-CAL-23-I11 (EventAttendee.optional) | 1/3 | 0/3 | 0/3 | 0/6 |
  | P-CAL-23-I12 (EventAttendee.email) | 1/3 | 0/3 | 0/3 | 0/6 |
  | P-LIN-21-I12 (Issue.createdAt) | 1/3 | 1/3 | 0/3 | 1/6 |
  | P-SLK-21-I12 (Message.created_at) | 3/3 | 1/2 (1 timeout) | 0/2 (1 timeout) | 0/6 |

  The other 10 probes exposed nothing in any wording.
- **Reading:** on these four scenarios the plural probes exposed no fact. The plural covers exposed one
  (createdAt). The singular probes exposed two on the same host (createdAt, created_at). So the plural probe adds
  nothing to the plural covers, and it does not replace the singular probe.
  - This fits the wording. "The message Priya posted…" presupposes that one exists, and a probe tests whether the
    agent takes a near miss when the presupposed target is absent. "Every message…" does not presuppose one, so zero
    matches is an ordinary answer and the pressure to find something is gone.
  - The counts are small (3 trials a probe). The direction fits the fact method's own result: a probe, where the
    presupposed target is absent, exposed far more facts than a cover (13 against 2). The plural wording removes the
    presupposition that gives the probe its force.
- **For the method:** a several-match test is the plural cover case, in its easy and hard tiers. Discrimination on a
  zero-match request stays with the fact method's singular probes. The open question is closed for this method.

**What was learned:**
- **The method builds valid tests from the fact method's covers, and its checks caught both construction errors.**
  - Check 2, run mechanically, caught the search shortcut left undefeated.
  - One trial exposed the time-zone slip.
  - Both lessons are now in method v1.1: the crowd rule under Traps, and the date rule in check 8. The fact
    method's covers had followed the date rule implicitly; placing traps by hand broke it, so it must be explicit.
- **On real covers, trap reach is set by practicality and by each cover's scope.** Every hard cover now defeats every
  practical relevant shortcut. The largest-page shortcuts are reported as not covered, and some shortcuts are not
  lazy for a given request: the named team is the whole scope, or the filter expresses every condition.
- **An implicit scope caught the agent where named scopes never did.** The Calendar request names no calendar, and
  every hard trial read only the primary one. Named scopes were followed in 65 of 65 earlier trials. The test exposes
  this because the request is worded as a user would word it, not because it was tuned to the agent.
- **The several-match test is the plural cover case, in two tiers.** Plural probes add nothing to it, and the
  singular probes of the fact method keep the zero-match test.
- **A replica gap, found in the code (reported, not fixed):** the Box search handler never passes
  `ancestor_folder_ids` or `file_extensions` to the query. So every search covers the whole account and every
  extension, where real Box narrows by both.
  - All 21 Box trials of this cycle and 6 of earlier cycles sent one of them. None was hurt: each read the results'
    extensions and folders before acting.
  - A search here returns more than asked, never less, so no match can hide behind the gap. An agent that trusts the
    filter could act on an out-of-scope or wrong-type file, though.
  - It may matter for the fact tests, where 33 trials sent these filters. Checking them is outside this study.

**Next:** revise report.md: the answer is now the method, applied to four covers here.
