# transfer_feasibility_01: which tests can be rerun on the real services?

Desk study for the lead ("RoadMap specialist"), started 2026-09-30 in the judge_qwen session (request of about
03:00 EDT). No model calls and no host: the services' public API documentation, fetched and cited with dates, and
the suite's recorded seeds.

## Status

- **2026-09-30 04:10 EDT. Done; the case study is proposed below.**
  - 1,006 tests classified: the 565 regular tests and the 441 policy units.
  - Results: 37 realizable as is; 403 as is with test accounts; 476 with a stated change; 90 not realizable with
    ordinary accounts.
  - The lead's request said 563 regular tests; the final manifest (report_01, `final_execution_keys`, and
    openclaw_eval_01's `final_regular_with_6b.json`) has 565, which is what is used.
- **Not done:** no account was created and no call made to a real service, so every "pilot" item below is still
  open.

## The question

How can we rerun a sample of the suite's tests against the real services (Slack, Linear, Box, Google Calendar),
to see whether the failures the mock exposes also happen there? Concretely:
- which of the suite's tests could be set up on the real services with ordinary accounts, or a small team of test
  accounts, through the public APIs;
- which only with a stated change (a date shifted, a second account, a paid plan), and which not at all, and why;
- and what a case study of about 40 tests would need: which tests, which accounts, what seeding scripts, how the
  agent reaches the real endpoints, and what it costs in time and money.

The mock was chosen because seeding is easy there: a message from someone two days ago is one row. The study asks
which of the suite's seed constructs the real services let a tester create.

## Method

1. **What each test depends on** ([inventory.py](inventory.py) → [inventory.json](inventory.json)).
   - For every test and unit, from the case file the runs used:
     - the (table, field) constructs its reference queries and near misses read, and the fields it writes;
     - the people other than the actor who must act in the seed (author, own, modify, upload, react, resolve,
       answer), and those who only need to exist;
     - whether the request names a date or a weekday;
     - whether the test runs on a fixed clock.
   - 224 distinct constructs, with frequencies in [constructs_seen.json](constructs_seen.json).
2. **What each construct needs** ([rules.json](rules.json), sources in [sources.json](sources.json)). One rule per
   construct, from the services' API documentation read on 2026-09-30:
   - Slack's method pages and help center;
   - Linear's published GraphQL schema (quoted in [linear_schema_excerpt.txt](linear_schema_excerpt.txt));
   - Box's API reference and support pages;
   - Google's Calendar API reference and help pages;
   - the plan and price pages.
3. **Each test's class** ([classify.py](classify.py) → [tests.csv](tests.csv), counts in
   [classification.json](classification.json)).
   - A test takes the worst class among its constructs, plus checks that need the seed itself:
     - Linear's team count;
     - Box's collections, ownership and uploaders, and records created after their last modification;
     - Calendar's event types, ACL scopes and rooms.
   - A test is a failure-transfer candidate if it failed on OpenClaw ([sample.py](sample.py)).

Classes:
- `as_is`: the actor's account alone creates the seed exactly.
- `team`: exact, but other people in the seed must be real accounts.
- `change`: possible with a stated change.
- `no`: not with ordinary accounts.

In the lead's terms, `as_is` and `team` are "realizable as is (with test accounts)".

## Results

| | Regular tests | Policy units | All |
|---|---:|---:|---:|
| As is (the actor's account alone) | 19 | 18 | **37** |
| As is with test accounts | 226 | 177 | **403** |
| With a stated change | 273 | 203 | **476** |
| Not realizable with ordinary accounts | 47 | 43 | **90** |
| **All** | **565** | **441** | **1,006** |

By service (regular tests; policy units in [classification.json](classification.json)):

| Service | As is | With test accounts | With a change | Not realizable |
|---|---:|---:|---:|---:|
| Box (139) | 9 | 17 | 71 | 42 |
| Calendar (103) | 7 | 80 | 11 | 5 |
| Linear (213) | 3 | 66 | 144 | 0 |
| Slack (110) | 0 | 63 | 47 | 0 |

**People.** 106 tests need no one but the actor. The rest need 1 to 9 other people (median 4), each a real
account; those who act in the seed also need their own API token.
- Slack: a member with a user token each (every message author and reactor).
- Linear: a member with a personal API key each (creators, commenters, resolvers).
- Box: an App User each, used through the As-User header.
- Google: an account each for calendar owners, organizers and attendees who answer.

**Why tests are not realizable** (90), in four groups, all documented:

| Construct | Regular | Units | Why |
|---|---:|---:|---|
| Box Hubs | 25 | 22 | Hubs exist only for "Enterprise and Enterprise Plus customers" |
| A Box near miss created after its last modification | 9 | 8 | Box sets `created_at`; the mock's 6 impossible records cannot exist |
| Box ownership that differs within a folder, when the test turns on ownership | 8 | 6 | "The Owner of the parent destination folder becomes the Owner of the newly moved folder": applied to uploads too, an inference to confirm in the pilot |
| A focus-time event on a secondary Calendar calendar | 5 | 7 | Focus time exists "only on primary calendars", for work or school accounts |

**The changes, and how many tests need each** (some need several):

| Change | Tests | What it means |
|---|---:|---|
| Accounts | 900 | Every other person in the seed is a real account |
| Date shift | 204 | A server-set time becomes the seeding time, and the request's date words are rewritten to it: Box's `created_at`/`modified_at` (only `content_*` can be set at upload), Slack's message and channel times, Linear's `updatedAt` and resolved times, and the four clocked scenarios |
| Rename | 179 | The service assigns ids, handles, emails, logins, issue identifiers and cycle numbers. Requests that name them are rewritten, or the records are created in order. Box's one collection is Favorites |
| Several days of seeding | 143 | A near miss differs by a server-set time on a named day ("created on June 3"); its records must be created on different days |
| Consistency | 118 | Box: the uploader is the file's creator ("in most cases"), and a folder's owner owns what is in it (inferred from the move rule). The mock breaks both in these seeds, and, if the inferences hold, the real service does not allow it. The test survives, but the creator and owner fields then agree with the uploader and the folder owner, which may make it easier |
| Paid plan | 123 | Linear Basic for more than 2 teams (88) or admin roles; Linear Business for guests and private teams (27); Box Business for file versions (10); Slack Pro for guests (7). Box Hubs' Enterprise plan (47 tests) is counted as not realizable |
| Pilot | 183 | Linear inputs documented as internal (a document's team or initiative, team owners), sub-teams on the Free plan ("1 level"), a milestone's status (derived): 58 tests. And the two Box consistency rules above, which are inferred rather than quoted: 125 more |
| UI step | 31 | Slack time zones, deactivated members, bot users and roles; Linear suspended users, admins and app users |
| Google Workspace | 21 | Focus time and rooms need a work account and a Workspace domain |

Only 156 of the 476 "with a change" tests need nothing heavier than a rename or a plain date shift.

**Constructs that need a change, with the tests they affect.** Everything else the suite reads is created exactly
by a documented API call (full list in [rules.json](rules.json)).

| Service | Construct | Tests | Class | Change |
|---|---|---:|---|---|
| Box | hubs, hub items | 37 | no | Enterprise plan |
| Box | collections (named) | 32 | change | the one collection is Favorites |
| Box | folder and file `created_at`, `modified_at` | 18-31 each | change | date shift |
| Box | task and comment `created_at` | 20-22 | change | date shift |
| Box | user `login` | 16 | change | rename (App Users get generated logins) |
| Box | file `version_number` | 10 | change | a paid plan (the free developer plan keeps 1 version) |
| Calendar | event type (focus time) | 11 | change or no | a work account, primary calendar only |
| Calendar | room attendees | 10 | change | a Workspace domain's resources |
| Linear | issue identifier | 44 | change | rename, or create in order |
| Linear | comment resolved time | 29 | change | date shift |
| Linear | cycle number | 25 | change | create cycles in number order, or rename |
| Linear | document's team | 24 | change | pilot (`[Internal]` input) |
| Linear | guest users | 18 | change | Business plan |
| Linear | sub-teams, team owners, milestone status | 9-15 | change | pilot |
| Linear | issue `updatedAt` | 11 | change | date shift |
| Slack | username (handle) | 32 | change | rename, or choose account emails so the handles match |
| Slack | message and channel times | 14 each | change | date shift (posting time) |
| Slack | bots, deactivated members, time zones, roles | 7-8 each | change | a UI step (guests need Pro) |

Two things are easy that one might expect to be hard:
- **Linear backdates for imports:** `IssueCreateInput.createdAt` ("Must be a time in the past") and `completedAt`,
  and `CommentCreateInput.createdAt`.
- **Google Calendar events can be created on any past date,** so the Calendar tests' 2018 dates and the agent's
  fake clock carry over.

What is hard is the Box timestamps, Box's ownership rules, and anything plan-gated.

## The case study proposed

### The sample

40 tests ([sample.csv](sample.csv), [sample.json](sample.json)), 10 per service: 6 regular tests and 4 policy
units.
- **Balance:** half failed on OpenClaw and half did not.
  - Failure transfer: a failure on the mock that recurs on the real service.
  - False transfer: a new failure on the real service.
- **Eligible:**
  - realizable as is or with test accounts, or with only a rename or a plain date shift;
  - at most 4 people besides the actor;
  - free plans only;
  - no clocked scenario;
  - not AR-LIN-24, where the PI's two rulings on its "Cycle 4" near miss disagree.
- **The Box gap:** no eligible Box absence unit passed all its trials on OpenClaw. The one with the fewest failures
  (1 of 3) takes that slot.
- **Changes in the sample:** 3 renames and 2 date shifts; everything else is created exactly.

| Service | Regular (failed / passed on OpenClaw) | Absence | Underspecified | People besides the actor (max) |
|---|---|---|---|---:|
| Box | 3 / 3 | 1 failed, 1 with 1 of 3 failing | 1 / 1 | 4 |
| Calendar | 3 / 3 | 1 / 1 | 1 / 1 | 4 |
| Linear | 3 / 3 | 1 / 1 | 1 / 1 | 4 |
| Slack | 3 / 3 | 1 / 1 | 1 / 1 | 4 |

### Accounts

All on free tiers for this sample.
- **Slack:**
  - a free workspace, owned by the PI;
  - four member accounts, with email addresses chosen so their handles match the seeds' where a request names a
    handle;
  - a fifth member named Agent Bot as the actor, with a user token (so search works, as it did on the mock), and
    one Slack app for the tokens;
  - user-token scopes (chat:write, reactions:write, users.profile:write), each member authorizing once.
  - The Free plan's 10-app limit is not reached.
- **Linear:**
  - a free workspace (2 teams, 250 issues; the sample's tests use at most 2 teams);
  - four members, each with a personal API key;
  - the actor, "Jordan Lee", as a fifth member.
- **Box:**
  - a free developer account, whose admin is the actor;
  - one app with JWT or Client Credentials authentication, configured for As-User;
  - up to four App Users, named as the seeds name people (the plan's App User limit is to be confirmed in the pilot).
  - App Users' logins are generated, so no sampled request names a login.
- **Google Calendar:**
  - five personal Google accounts: the actor and four others;
  - a Google Cloud OAuth client in testing mode, with each account's refresh token. In testing mode a refresh token
    for the Calendar scope expires in 7 days, so tokens are renewed per session.
  - The sample avoids focus time, rooms and group ACLs.

### Seeding scripts

One script per service, sharing a shape. Each reads a case file (seed, references, request) and:
1. **Creates** the records in dependency order through the real API, as the right person:
   - Slack: channels, then members, then messages by each author's token, then reactions;
   - Linear: teams and states, issues with `createdAt`/`completedAt`, comments with `createdAt`, then resolves;
   - Box: folders, then uploads through As-User, tasks and comments;
   - Calendar: calendars and ACLs from the owner's account, events inserted or imported with the organizer and
     iCalUID, attendee responses from the attendees' accounts.
2. **Records an id map** from the seed's ids to the real ones.
3. **Rewrites** the case's references (targets and near misses) and the request's renamed words and shifted dates,
   so judge v2 and the scoring run unchanged on real ids.
4. **Snapshots** every seeded record, and the workspace's lists, before and after the agent's turn. The real
   services have no diff endpoint, so the state diff comes from the snapshots; listing the whole small workspace
   also catches writes outside the seed.
5. **Tears down** everything it created (channels archived and renamed, issues, teams, files and folders,
   calendars and events deleted), so the next test starts clean.

Because requests name fixed things ("#incidents", "the Web team"), tests of one service run one at a time; the
four services can run in parallel.

### The agent's route to the real endpoints

Today's [bin/curl](../../integrations/openclaw/bin/curl) rewrites the real base URLs to the replica's environment
and adds the AgentDiff key. For real services, a second shim leaves the URLs alone and adds each host's
credential. The skills already tell the agent to use "placeholder tokens like `<TOKEN>` where credentials would go", and that
authentication is "handled automatically via proxy". The shim replaces the placeholder's header for each host:

| Host | Header the shim sends | Token |
|---|---|---|
| `slack.com`, `api.slack.com` | `Authorization: Bearer xoxp-…` | a user token of the actor's account, "Agent Bot" (see the first risk) |
| `api.linear.app` | `Authorization: lin_api_…` ("Authorization: <API_KEY>" for personal keys; OAuth uses Bearer) | the actor's personal API key |
| `api.box.com`, `upload.box.com` | `Authorization: Bearer …` | an access token for the actor (JWT/CCG, refreshed hourly) |
| `www.googleapis.com/calendar/v3` | `Authorization: Bearer ya29…` | the actor's OAuth access token (refreshed hourly) |

- Tokens stay in a local file the agent never reads.
- The Calendar fake clock (2018-06-17) stays as it is.
- The skills' documentation is the same text the mock runs used. On a real service the agent may also use
  endpoints the replica lacked, which is part of what transfer means.

### Cost and time

| Item | Estimate |
|---|---|
| Accounts and plans | $0: free tiers only (Slack Free, Linear Free, Box free developer plan, personal Google accounts) |
| One-time setup (the PI) | A few hours: five Google accounts (phone checks likely), four Slack and four Linear invitations, the Slack app and the Google OAuth client |
| Seeding scripts (a coding agent) | About 2 days for the four services, with a pilot of every construct the sample uses and the "pilot" items it touches |
| Runs | 40 tests × 3 trials = 120 executions. Each takes 1-3 min to seed, at most 10 min for the agent, and 1-2 min to snapshot and tear down; one at a time per service, so about 6 hours of wall time with the services in parallel |
| Solver | the self-hosted Qwen through OpenClaw: no per-token cost, about 4% of a full round's executions |
| Judge | 120 verdicts: judge v2 on Muse about $2.40 at list price, or on the self-hosted Qwen at no per-token cost |
| Rate limits | not expected to bind (a test seeds tens of records), but not checked against each service's documented limits |

**If a plan is added,** the eligible pool grows:
- Linear Basic ($10 a user a month) opens the 88 tests with more than 2 teams.
- A Google Workspace Business Standard trial (14 days, then $14 a user a month) opens focus time on primary
  calendars and rooms.
- Box Hubs would need an Enterprise plan, which is not an ordinary account.

### Risks to check in the pilot

- **The Slack actor.** The mock's actor is a bot, and it can search. On real Slack, `search.messages` takes only a
  user token ("User token: search:read"). In the final OpenClaw runs, 233 of 555 Slack executions (42%) called it.
  - With a bot token the agent loses search, a harness difference that would confound transfer.
  - Proposal: the actor is a regular member named "Agent Bot", using a user token. Its `is_bot` flag then differs
    from the seed's, which no sampled request depends on.
- **Box's As-User on the free developer plan.** The plan says "not every endpoint is available", and the As-User
  guide names no plan. Every Box test with other people depends on it, so it is the first thing to try; the fallback
  is managed users on a Box Business trial.
- **Box's two inferred rules** (the uploader is the creator; a folder's owner owns what is in it). One collaborator
  upload settles both.
- **Linear's 250-issue cap on the Free plan.** 30 executions at 10 to 20 issues each could cross it if deleted issues
  still count; the pricing page does not say.
- Whether Linear accepts cycles wholly in the past, documents in a team (`teamId` is internal), and team owners.
- Slack's workspace import could keep old message timestamps (the help pages do not say). It would replace date
  shifts, but a Free workspace hides messages older than 90 days.
- Pre-existing data in real accounts will be visible to the agent: Slack's #general, Linear's default team, Google's
  holiday and birthday calendars. Hide or delete what can be, and record what cannot.
- Box consistency: in the sampled Box tests the uploader and ownership already agree with the folder, or are fixed
  by the "consistency" change. After the change the tests may be easier; compare those pairs separately.

## Files

| File | What |
|---|---|
| [inventory.py](inventory.py), [inventory.json](inventory.json), [constructs_seen.json](constructs_seen.json) | What each test depends on |
| [sources.json](sources.json), [linear_schema_excerpt.txt](linear_schema_excerpt.txt) | The documentation relied on, with dates and quotes |
| [rules.json](rules.json) | One rule per construct |
| [classify.py](classify.py), [tests.csv](tests.csv), [classification.json](classification.json) | The per-test table (class, changes, people, reasons, OpenClaw outcome) and its counts |
| [sample.py](sample.py), [sample.csv](sample.csv), [sample.json](sample.json) | The proposed sample |

## Limits

- **A desk study.** Rules are made at the level of a construct from documentation, not from calls to the services,
  so every "pilot" item is open, and a documented field can still behave differently.
- **People are counted from the seeds' author, owner and responder fields.** A person who is only mentioned in a
  request text is not counted.
- **The "consistency" change keeps a test's logic but may make it easier.** Whether that matters is a question for
  the PI.
- **Prices and plan limits change.** They are as read on 2026-09-30.
