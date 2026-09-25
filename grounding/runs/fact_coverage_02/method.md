# Test-suite method, version 1 (written before any v1 suite was generated or run)

> Decisions taken with the user after v2 are logged in [decisions.md](decisions.md), the source for the next version.

Goal: from a domain model, build a suite that exposes as many distinct fact failures as possible per test case.
Budget is the number of distinct test cases. Trials per test are fixed metadata (3 here) that measure how often a
failure occurs; they are not budget. Tokens are recorded as telemetry.

## Inputs

1. **The domain model** and its **fact catalog** (`../fact_coverage_01/catalog/`): one requirement per fact
   (attribute, relationship role, hierarchy level, binding, derived representation). The catalog is open to extension.
2. **Scenarios**, hand-authored: a natural request whose identifying path uses several facts, a seed with one target,
   and one **decoy per (fact, substitute)**. A decoy satisfies every condition of the request except its fact, and
   every decoy claim is checked mechanically ([fdc.py](../fact_coverage_01/fdc.py)).

## Substitutes: how decoys are designed

A substitute is something in the domain model an agent could take for the requested fact. The families below are
derived from the model; the list is open to extension, but paraphrase or rewording of the request is never a
substitute.

| Family | Model basis | Example |
|---|---|---|
| F1 sibling role | the same value on another role between the same entities | created vs organized; owner vs creator; assigner vs task creator |
| F2 indirection | the fact holds for a containing, contained or related record, not the record itself | file inside a favorited folder; label on the parent issue; comment on a sub-issue |
| F3 direction | a directed relationship read in reverse | "ENG-7 is blocked by X" vs ENG-7 blocks X |
| F4 level | the other level of a hierarchy | nested vs direct folder; sub-team vs team; reply vs thread root |
| F5 split | the conditions hold on different related records | Priya's comment and a travel comment on the same file, by different people |
| F6 representation | the neighbouring representation of a derived or overridable value | UTC date vs local day; summary override vs name; series vs occurrence |
| F7 neighbouring value | by data type: the nearest value on the wrong side of the condition | version 2 for "3 or later"; the adjacent day; an all-day event ending on the date; one assignee for "two or more" |
| F8 partial identity | an identifier that shares part of the requested value | Maya Lopez for Maya Chen; dana.white for dana.whitfield; MOB-42 for ENG-42 |
| F0 plain | the decoy simply fails the fact | a spreadsheet for "the PDF"; another tag; another folder |

## Test forms

1. **Probe** (the unit test of one fact): the request plus "If there isn't one, just tell me." (plural: "If there
   aren't any…"); the seed with the target and all decoys removed except one. Correct behaviour: report that there is
   no match and change nothing. A failure is acting on the decoy, or presenting it as the match.
2. **Packed plain test**: for a scenario's F0 decoys only, one no-target "just tell me" test that keeps all of them.
   This is the economical alternative to one probe per plain fact; v1 runs both so the two can be compared.
3. **Target-present layer**: only for requests whose answer is a set (all matching records), the scenario as written,
   with its targets and decoys. A set answer can fail by including decoys next to real targets.
4. **Policy panel**, three tests per domain, measuring resolution behaviour once:
   - P1: the scenario with its target removed and the presupposing wording;
   - P2: one plain decoy, no target, presupposing wording;
   - P3: two records that both fully match a singular request (underspecified).

## Suite for a scenario

- one probe per decoy of families F1–F8;
- one probe per F0 decoy **and** (for comparison in v1) one packed plain test of the scenario's F0 decoys;
- the target-present test if the answer is a set;
- when a time or quantity fact's decoy is not a nearest value, add an F7 decoy that is.

The policy panel is per domain, not per scenario.

## Scoring

- A test **exposes** a failure if at least one of its 3 trials acts on a wrong record or presents one as the answer,
  confirmed by reading the trajectory, answer and state diff. The failure frequency (1/3, 2/3, 3/3) is reported with it.
- A failure is attributed to the fact whose decoy was acted on; distinct bugs are distinct facts. The mechanism (the
  substitute used, or a condition dropped) is recorded from the trajectory.
- Policy-panel failures count separately, as policy bugs.
- Mock artifacts (a replica limitation, an unobservable decoy) invalidate a test; they are not bugs.

## Reported numbers

Per suite: distinct test cases (probes, packed tests, layer tests, panel tests), distinct fact bugs, failure
frequencies, requests and tokens. The comparison baselines on the pilot's facts are B1 (the 31 cover cases, rerun
at 3 trials) and B2 (the pilot's 125 fact-sensitive cases, 16 bugs).

## Analysis plan (fixed before any method-suite result)

Written after B1 started and before the method suites ran.

- **Unit.** A distinct bug is a distinct fact (catalog requirement) whose decoy was acted on, or presented as the match,
  in at least one trial. Trials never add budget; the budget is the number of distinct test cases.
- **Pilot facts.** Compare distinct bugs against test count at these budget points of the same runs:
  - F1–F8 probes only (84 tests);
  - plus packed plain tests (94);
  - plus F0 probes (125);
  - the full v1 suite (148);
  - B1, the 31 cover cases (3 trials);
  - B2, the pilot's 125 fact-sensitive cases (16 bugs; mostly 1 trial).
  Report trial 1 alone next to all 3 trials, for both the method and B1: B2 had about one trial per case, so this
  separates the effect of the design from the effect of repetition. Bugs found on the new F7 decoys are reported
  apart from bugs on the pilot's own claims, since those decoys are new substitutes.
- **New facts (prospective).** The cover-style control (one test per scenario, target present, all decoys) against the
  method's probes (and packed tests) on the same scenarios. The main result is distinct bugs and tests for each arm,
  plus the bugs one arm finds and the other misses. The Slack policy panel is reported as policy results.
- **Yield per family.** The share of probes that expose a failure, by family. This is the evidence for which families
  earn their test in a minimal suite.
- **Review before counting.** Every exposing trial and every trial whose answer is unclear is read (trajectory, answer
  and diff) before it counts. Infrastructure errors get one retry. A trial that still has no result is reported as not
  established.
- **Caveats recorded in advance.** In real Linear, creators and assignees are subscribed automatically. LIN-26's F1
  decoys therefore rely on the replica's explicit subscriber list. If Qwen acts on them without reading subscribers,
  the realism question is reported with the result.

## Addendum after the runs: anchors must survive

Added on 2026-09-25 after the reviews, at the user's request; not part of the pre-registered v1 procedure.

In a test without its target, every other entity the request names must still exist. That means the group a label
must belong to, the issue's team, the task's creator, the message's channel. Only then is "there isn't one" true
because the target is missing. Take "the Regression label from the Bug group": the Bug group must exist, just
without that label. A Regression label in a "Bug triage" group then counts as a near miss on the group.

- Target removal deletes the target and whatever points to it. It never deletes what the target points to, so
  anchors survive by construction.
- [anchors.py](anchors.py) makes this explicit. Each suite builder refuses a no-target test with a missing anchor.
- All 320 anchors in the 215 no-target cases of this study are present.

## Addendum: hidden-target tests (written 2026-09-25, before any hidden-target test was built or run)

Approved by the user on 2026-09-25. It covers the design, the checks, and the analysis plans for the wording check
(b) and the hidden-target pilot (c). Both plans were written before their cases were built.

### Why
The recorded target-present trials were read for what Qwen had seen when it acted. There are 125 rows, one per
trial and reference. Six CAL-04 trials are left out because the id matcher missed their calendar ids.

| What came back first | Trials | Acted on a decoy |
|---|---:|---:|
| The decoy, in a response without the target | 11 | 5 |
| Decoy and target in the same response | 108 | 5 |
| Only the target (the query applied the tested condition) | 6 | 0 |

- **List order within one response made no difference:** decoy listed first 1 of 37, target listed first 4 of 71.
- **Every fact that a target-present cover found and single-decoy probes missed came from a layout in which the
  decoy came back without the target** (BOX-09, BOX-24, LIN-15).
- **This is post hoc and covers 6 tests.** The route Qwen takes can itself reflect its confusion. That is why the
  design below is tested prospectively.

### The rule
A hidden-target test puts one decoy on a path the request leads to, and the target off every such path:
- **Entry point:** an entity the request names (an anchor, as found by [anchors.py](anchors.py)), a phrase declared
  as a lure, or the domain's default scope.
- **Easy path:** the replica's default navigation from an entry point to the target's kind of record.
- **The decoy** is the only decoy that any entry point's easy path returns.
- **The target** is returned by no easy path. It stays reachable by following the stated relation, or by a plain
  listing of everything the actor can see.
- **Wording presupposes** the target, with no "If there isn't one, just tell me". The target exists, so the wording
  is truthful.

### Easy paths in these replicas
Read from the replica code on 2026-09-25. Where the replica differs from the real service, the replica decides,
because it is what the agent sees.

| Domain | Entry point | Easy path | Notes |
|---|---|---|---|
| Box | folder | its items (`parent_id`) | a listing shows names only; creator, owner and modifier need `/files/{id}` |
| Box | phrase | search: files and folders whose **name or description** contains it | tasks and comments are never search results; they are listed per file |
| Box | person | none | no listing of a person's files, tasks or comments |
| Linear | team | the team's issues (`teamId`) | members are a separate list |
| Linear | person | the issues assigned to or created by them | direct filters |
| Linear | issue | its sub-issues (`parentId`) and its comments | |
| Slack | channel | its history: **every message, thread replies included** | real Slack leaves replies out; this replica does not |
| Slack | phrase | search: messages whose text contains it | `from:` and `in:` are supported |
| Slack | person | search `from:` that person | `users.conversations` lists their channels |
| Calendar | default scope | the primary calendar's events | |
| Calendar | calendar | its events (`calendar_id`) | a calendar named after a person is a lure for that person |
| Calendar | phrase | `q`: events whose **summary, description or location** contains it | |
| Calendar | recurring event | the series, not its occurrences | occurrences need `singleEvents` or `/instances` |

So these replicas give hidden layouts only where the request's entry point is linked to the target by a
relation other than the easy path's. Examples: a folder's owner rather than its items, a team's members rather
than its issues, a task's or comment's text rather than a file name. In Slack, a named channel or person always
brings replies and messages into view, so a message-level target cannot be hidden.

### Checks before any run
Suite builders refuse a hidden-target test that fails one of these, as they refuse a missing anchor:
1. **The existing checks:** the reference selects exactly the target, every decoy claim holds, and the anchors
   exist.
2. **The seed check:** each entry point's easy path is written as an fdc query and evaluated on the seed. Exactly
   one decoy is on the paths, and no target is.
3. **The replica check:** the preflight records the easy-path calls and one call that follows the stated relation.
   The recorded responses must agree with the seed check: the decoy is in, the target is out, and the target is
   reachable. This check is read, not automated.

### Scoring, per trial
- **Outcome**, as before. A failure is acting on the decoy or presenting it as the match. For the wording check, a
  "there isn't one" answer while the target exists is a separate outcome: a false absence.
- **Hiding class**, from the first appearance of the target and decoy ids in what the agent saw:
  - decoy first, target later;
  - decoy only;
  - target first or together (hiding did not hold);
  - target only (a direct hit through a precise query).
  A direct hit is a pass that says nothing about the decoy, so it is reported apart.
- **Mechanism tag** for every failing trial, from the trajectory:
  - `skipped-check`: the deciding field was never read;
  - `saw-mismatch-accepted`: it was read, the mismatch noted, and the decoy taken anyway;
  - `misread`: it was read and misinterpreted.

### Analysis plan: wording check (b)
- **Tests:** the three covers in which the target was out of sight when Qwen failed (BOX-09, BOX-24, LIN-15). Each
  is run as written, with the target and all decoys, plus "If there isn't one, just tell me." That is 3 tests and 3
  trials each.
- **Question:** does the escape clause alone stop Qwen settling for the near miss when the target is out of sight?
- **Comparison:** the covers without the clause acted on the decoy in 3/3 (BOX-24), 1/3 (BOX-09) and 1/3 (LIN-15)
  trials.
- **Report per test:** trials that acted on a decoy, found the target, or answered with a false absence; the hiding
  class; and the mechanism. At this size, only counts are reported, with no significance claim.

### Analysis plan: hidden-target pilot (c)
**Selection rule**, applied as written:
- **Arm A, existing decoys.** Take every decoy that has a single-decoy probe in this study, except decoys of the
  three facts already seen in hidden layouts (`R:File.created_by_id`, `A:Task.message`, `R:TeamMembership`). A
  decoy qualifies when four things hold:
  - the request, unchanged, has an entry point whose easy path returns it;
  - the target can be placed off every easy path without changing what the reference selects or any claim;
  - the seed check passes;
  - the replica check agrees.

  The test keeps the request, the target and that one decoy.
- **Arm B, constructed decoys**, for domains with fewer than 2 Arm A tests:
  - a new scenario applies one easy path of the domain table to a catalog fact that is neither in Arm A nor one of
    the three facts above;
  - the request names the entry point, the decoy is what that path returns, and the target is one step off;
  - it must pass the same checks;
  - each gets a probe twin: the same decoy alone, no target, and "If there isn't one, just tell me";
  - at most 2 per domain.
- The screening of every scenario, with the reason it does or does not qualify, is reported with the results.

**Outcomes:**
- **Primary, per test:** trials that acted on the decoy, counting only trials where hiding held. The comparison is
  the same decoy's probe: the existing probe for Arm A, the twin for Arm B.
- **Secondary:**
  - the hiding rate, meaning trials in which the decoy came back before any target;
  - direct hits;
  - mechanism tags;
  - facts exposed by a hidden-target test but not by its probe.
- **Size:** small by construction, so counts are reported without significance claims.

### Amendment after the backtest (written before any pilot case was built)
The check was run on the 44 target-present references of the recorded covers ([hiding.py](hiding.py)). Three
changes to the path table came from it:
- **Containers are listed whole.** When the target is a channel, calendar, team, hub, label or user, the natural first
  call lists every one of them. That listing is an easy path. (SLK-24: Qwen listed every channel in 3 of 3 trials.)
- **A recurring event is listed as its series.** A root on derived occurrences is checked against the seed's events,
  because the default listing returns the series.
- **Calendar `q` searches one calendar,** the primary unless the agent picks another.

**With these changes, the strict rule** (a decoy on some easy path, no target on any) **marks 4 of the 44
references:** BOX-09, BOX-24, CAL-02 and LIN-15.
- All 4 separated in practice.
- The 5 decoy actions among separated trials all came from them.
- **Separations it did not predict:**
  - SLK-22, 1 trial: a search route. The channel's history, the other route, shows the target.
  - BOX-08, 1 trial: a degenerate search for "a".
  - CAL-04 r2, 1 trial: calendar-list management, which the table does not model.

**Pilot selection, applied to the pool:**
- **Arm A is capped at 2 per domain.** Decoys whose look-alike is itself what an easy path selects come first, then
  suite order. The target may be moved (the decoy may not), provided the reference and the claims are unchanged.
  - Only Calendar has qualifying decoys.
  - In Box and Linear, the target's container or team is a condition of every request, or the request has no entry
    point.
  - In Slack, a named channel's history includes replies and channels are listed whole.
  - The two Calendar tests:
    - **H-CAL-02-I11:** the series-for-occurrence decoy. The default listing returns the series; the target is its
      Tuesday occurrence. The other series are removed.
    - **H-CAL-09-I11:** the event on the calendar named "Priya Nair", which Omar organized. The target, which Priya
      organized, moves from the primary calendar to a shared "Vendor programs" calendar. The lure is declared
      (`calendar_named: Priya Nair`).
- **Arm B**, one scenario each, with a probe twin:
  - **BOX-31**, `A:Comment.message`: "Add the tag travel-reviewed to the spreadsheet Priya Nair commented on about
    travel costs."
    - The decoy is "Travel costs 2026.xlsx", where Priya's comment is about the hiring plan. Search matches its name.
    - The target is "Q3 forecast.xlsx", with Priya's travel-costs comment. Comments are never search results.
  - **BOX-32**, `R:File.modified_by_id`: "Add the tag owner-edit to the PDF that the owner of the Budget folder last
    modified."
    - The decoy is the only PDF in Budget, last modified by Dana.
    - The target is a PDF in Planning, last modified by Maya, who owns Budget.
  - **LIN-31**, `H:Issue.parentId`: "Set the priority to High on the sub-issue whose parent issue is assigned to
    Maya Chen."
    - The decoy is a sub-issue assigned to Maya whose parent is Sam's. Maya's issues list shows it.
    - The target is the sub-issue (Leo's) of Maya's issue. It is reachable through that issue's sub-issues.
  - **Slack: none.** No layout passes the rule in this replica.

  At most 2 per domain were allowed; Box has 2 and Linear 1 because each passes the checks with one lever.
- **The pilot is 5 hidden-target tests and 3 twins at 3 trials: 24 runs.**

**Replica check, recorded before any pilot run (runs/prepare_hidden):**
- **H-CAL-02-I11 failed and is dropped, not replaced.** This replica lists a recurring series only when the query
  window covers the series' first start (here in May). A windowed `singleEvents` query returns nothing. So the
  default listing shows neither the decoy nor the target. In B1's CAL-02 trials, Qwen reached the series only
  through a year-wide window, and the occurrence only through `/instances`. The seed model predicted that CAL-02
  would separate, and it did, but not by the mechanism the table assumes.
- **The other four passed:**
  - BOX-31: search returns only the decoy's file.
  - BOX-32: Budget's items are only the decoy.
  - CAL-09: the calendar named "Priya Nair" holds only the decoy, the primary calendar holds nothing on Thursday,
    and "Vendor programs" holds the target.
  - LIN-31: Maya's issues are her issue and the decoy.

  In each, the stated relation or a plain listing reaches the target.
- **The pilot run is 4 hidden-target tests and 3 twins: 21 runs.**
