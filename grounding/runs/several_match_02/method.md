# Several-match test method, version 1

*Written 2026-09-28, after the manual investigation ([log.md](log.md), cycles 0–7b) and before the method was
applied to any cover case. It is the standard that the automation must meet.*

Goal: from a domain model and its cover scenarios, build tests that expose an agent that does not act on every
record a plural request selects, because it stops early or takes a route that returns only part of the scope.
The tests sit next to the fact tests. They are form 3 of the fact method ([fact_coverage_02/method.md](../fact_coverage_02/method.md),
"target-present layer, for requests whose answer is a set"), and this method supplies where their targets go.

Budget is the number of distinct test cases. Trials (3) are metadata.

## Inputs

1. **The domain model and its fact catalog**, as in the fact method.
2. **The cover scenarios** of the fact method: a natural request, a seed, and decoys per fact and substitute.
3. **A route table per service.** For every operation that lists or searches a kind of record, it records:
   - the scope (which container);
   - recursion;
   - the default and largest page;
   - visibility defaults and the flags that change them;
   - which conditions its query or filter can express.

   It is read from the replica code, because the replica is what the agent sees. Differences from the real service
   are recorded as replica gaps. It extends the easy-path table of the fact method's hidden-target addendum.

## The requirement space: laziness behaviours and shortcuts

A plural request selects every record that meets its conditions within its scope. A route retrieves and selects
candidates, and it covers the scope along five dimensions. A laziness behaviour falls short on one of them:

| Dimension | What full coverage needs | Laziness behaviour |
|---|---|---|
| Scope | every container in the request's scope, at every depth | reads only the named or default container; does not recurse |
| Pages | every page of each listing | reads the first page, default or largest |
| Visibility | every visibility class in scope | keeps a listing's default (hidden calendars, private channels, archived channels, DMs) |
| Filter | a query that expresses the condition, or no query | narrows with terms that do not express the condition |
| Selection | keeps every retrieved record that meets the condition | keeps part of the scope (the named team only) |

- **A shortcut** is a behaviour instantiated on one service's route table, for one kind of request. It is the
  ordered API calls a lazy agent makes, and a page-size variant counts as its own shortcut.
- **The requirements are the shortcuts.** Each should be defeated by some test in the suite.
- The investigation enumerated 30 shortcuts over the four services (`matrix.json`):
  - Box 8, files in a folder tree;
  - Calendar 4, events on my calendars;
  - Linear 6, issues in a team tree;
  - Slack 12, over three kinds of request: about channels, messages in a set of channels, messages anywhere.

## Traps

A trap is a place in the seed where one match sits so that a behaviour's shortcuts miss it and the thorough route
finds it.

| Behaviour | Trap |
|---|---|
| Stays in the named container, does not recurse, keeps part of the scope | a match one or two containers down, or in another container in scope |
| Reads one page | a match past that page |
| Keeps a visibility default | a match behind the default |
| Narrows with the wrong terms | a condition no search expresses, or more hits than one search page returns |

- **Defeat.** Run the shortcut as API calls on the test's own seed. If the set it would act on misses any match, the
  test defeats it. One trap defeats every shortcut of its behaviour for that service and kind of request.
- **A trap can combine dimensions.** For example, past the first page of a subfolder is aimed at the tree walk that
  reads one page per folder.
- **The strategy matrix** (`matrix.json`, from [strategies.py](strategies.py) and [probes.py](probes.py)) records which
  placement defeats which shortcut.

## The test form: the plural cover case

Matches are valid-side inputs: the request presupposes matches, and they exist. So one test may carry several
placements, as valid classes share a test in equivalence partitioning.

A plural cover case is a cover scenario whose request is meaningfully plural, with:
- **its conditions and decoys, unchanged;**
- **two or more matches in plain view** on the natural route. They expose stopping early, and finding one there makes
  finding the others trivial, on purpose;
- **trap matches:** the fewest that make every relevant shortcut miss at least one match. No single retrieval that a
  shortcut makes returns them together with the plain-view matches.

**Two tiers:**
- **Easy:** plain-view matches only, for agents of low capability.
- **Hard:** plain view plus traps.

## Construction

**Creative** (by hand, or by the generator's writer):
1. Choose cover scenarios whose request is meaningfully plural. A user could plausibly have several matching records
   and want to act on all of them, such as several events at 8 a.m. to cancel.
2. Word the plural request as a user would.

**Mechanical:**
3. The request's kind (the record kind and the scope) selects the relevant shortcuts from the route table.
4. The behaviour-to-trap map and the strategy matrix give the smallest set of traps that covers them.
5. The kit's seed operations place the matches, and the decoys stay.
6. Check (below), then build and preflight as for any kit case.

## Checks before any run

A test that fails any check is refused:
1. **The fact method's checks:** the reference selects exactly the targets, every decoy claim holds, and the anchors
   exist.
2. **Every relevant shortcut, run on the seed, misses at least one target** (the strategy runner).
3. **The thorough route finds every target.**
4. **The condition comes back on the thorough route.** Each target's deciding field is in the response of the call
   that retrieves it. Two tests were void without this: the replica's Box listing omits `modified_by` whatever
   `fields` asks, and Slack history omits reactions.
5. **The action is possible at every target** (the preflight's write check). A reaction in an archived channel fails,
   so for a write request an archived channel is out of scope, and leaving it out is not lazy.
6. **Practical.**
   - The thorough route is a handful of calls: listings and their pages, with no per-record calls to read the
     condition.
   - No container holds more than about 200 records.
   - A trap that needs more is dropped, and its shortcuts are reported as not covered. In these replicas that drops
     the largest-page traps (1,000 items and more), leaving two shortcuts uncovered:
     - Box: walking the tree and reading one 1,000-item page per folder;
     - Slack: private and public channels, one 999-message page each.
7. **Nothing but the condition links the targets.** No text, name or field that a search could use may set the
   targets apart from the near misses. SM2-SLK-04's messages read "Leo deployed…", and one trial found them by a text
   search.
8. **The wording names no hiding place and is not contestable.**
   - No "including private channels" or "and its subfolders". Those wordings are kept only as controls.
   - "My calendars" was read as the calendars I can edit; "the calendars I own" was not.

## Scoring, per trial

- **Compare the set acted on with the target set.**
- **A missed target is attributed to its placement,** and through it to the behaviour. Where a trap combines
  dimensions, keep a plain match of each simpler kind (a plain subfolder match next to the paged one), so that a miss
  is unambiguous.
- **A decoy acted on is a fact failure,** attributed as in the fact method.
- **A test exposes a diligence failure** if at least one of its 3 trials misses a target.
- **Mock artifacts invalidate a trial:** a miss caused by a replica gap, such as the Slack POST query-string gap.

## Reported numbers

- **Per service and kind of request:**
  - the shortcuts;
  - those defeated by some test (coverage);
  - those not covered, with the reason (impractical, or undefeatable in the replica);
  - those exposed (the agent missed their trap in a trial).
- **Per behaviour:** targets missed out of targets placed.
- **Per tier:** tests that exposed a failure.

## Open question

**Plural probes.** The fact method's probe with plural wording has no target and one decoy, plus "if there aren't
any, just tell me". It tests discrimination on the zero-match request. Does it expose facts that the plural cover
cases do not? To answer it, compare them on the same scenarios. The prior is the single-target result: probes
exposed 13 facts, covers 2.

## What the automation provides

- **The route table** per service, as data.
- **Shortcuts generated from it.** Today they are hand-coded functions in `strategies.py`.
- **Trap seeding** from the behaviour-to-trap map. Today the seeds are written by hand.
- **The condition-visibility check.** Today it is done by eye.
- **The other checks**, as in the kit.
