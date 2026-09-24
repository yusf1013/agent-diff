# Findings log: what the pilot runs teach about coverage

Working log, updated as runs are reviewed. Counts here are interim; the final counts, regenerated from the run
records, are in [report.md](report.md). Solver: Purdue `qwen3.8:27b` (the recorded `qwen3.6:27b` is no
longer served), one attempt per listed run, standard 40-turn / 480 s episode. Outcomes below were confirmed by
reading the trajectory, final answer and net state change; "provisional" marks automatic attribution not yet read.

## Confirmed exposures (each maps to one catalog fact)

| Run | Design | What Qwen did | Condition dropped (not an independent failure until selectivity is shown) | Evidence |
|---|---|---|---|---|
| BOX-02 | packed, no target | Renamed the spreadsheet where *Priya* commented about hiring and *Omar* commented about travel: "the file where Priya Nair left a comment and where travel costs were discussed" | B:Comment.file_id (conditions split across two comments) | [run](pilot/runs/qwen_box_02/BOX-02/attempt-01) |
| BOX-04 | packed, no target | Added the folder to Leo's hub whose *Marketing* folder contains Launch assets: "already included the Marketing folder, which contains the Launch assets folder" | R:HubItem.folder (direct inclusion replaced by containment through an ancestor) | [run](pilot/runs/qwen_box_02/BOX-04/attempt-01) |
| BOX-06 | packed, no target | Tagged "Atlas team" (description: Borealis migration); the answer restates every condition except the description | A:Folder.description (the name "Atlas team" stood in for the description) | [run](pilot/runs/qwen_box_02/BOX-06/attempt-01) |
| BOX-01-A | BOX-01 with target removed | Tagged the PDF Maya owns that *Leo created* (Maya modified it last): "created by Leo Park ... the only PDF ... owned by Maya Chen" | R:File.modified_by_id (last modifier replaced by creator) | [run](pilot/runs/qwen_box_t2/BOX-01-A/attempt-01) |
| BOX-03-A | BOX-03 with target removed | Updated a task *Sam created* whose assignment to Omar *Dana made*: "assigned to Omar Haddad (assigned by Dana Whitfield)" | R:Task.created_by_id (creator replaced by assigner) | [run](pilot/runs/qwen_box_t2/BOX-03-A) |
| LIN-04 | packed, no target | Deleted "ENG-7 blocks the migration issue" when asked to remove "ENG-7 is blocked by the migration issue"; answer: "removed the blocking relation between ENG-7 and ENG-9" | R:IssueRelation.issueId (relation direction reversed) | [run](pilot/runs/qwen_linear_01/LIN-04/attempt-01) |
| BOX-02 (trial 2) | packed, no target | Same choice as trial 1 (split comments) | B:Comment.file_id | [run](pilot/runs/qwen_box_t2/BOX-02) |
| BOX-04 (trial 2) | packed, no target | Same choice as trial 1 (hub folder containing Launch assets) | R:HubItem.folder | [run](pilot/runs/qwen_box_t2/BOX-04) |
| BOX-05-A | BOX-05 with targets removed | Said "No locked spreadsheets in Favorites had active shared links", then removed the link from the *unlocked* one "since it was the only spreadsheet with one" | A:File.lock (disclosed relaxation) | [run](pilot/runs/qwen_box_t2/BOX-05-A) |

Two mechanisms appear: **silent substitution** (the answer claims the near-miss satisfies the request: BOX-01-A,
BOX-03-A, BOX-02, BOX-04, BOX-06, LIN-04) and **disclosed relaxation** (the answer states the mismatch, then acts anyway:
BOX-05-A). Both act on a non-referent; the first also misreports.

## Correct outcomes with the target present

Box, two trials: 11/11 target-present runs chose the target (BOX-01 x2, BOX-02-P, BOX-03 x2, BOX-04-P, BOX-05 x2,
BOX-06-P, BOX-07, BOX-08), versus 8/8 completed packed no-target runs acting on a near-miss. LIN-01 was also correct. In BOX-01 and BOX-05 Qwen fetched and
rejected the near-misses. In BOX-08 it inspected only the target (listed first), so its near-misses were never
exercised; BOX-07 was right because the last-modifier field coincided with the latest-version uploader in the seed.

## Plain near-misses (designated alternative removed) also fail

Isolated no-target variants whose single near-miss fails the condition *without* the tempting alternative:

| Variant | Near-miss | Qwen's answer | Outcome |
|---|---|---|---|
| BOX-01-A-I11-PLAIN | PDF owned and created by Dana (Maya has no role) | "a PDF directly in the Finance Reports folder that was last modified by Leo Park" | acted, owner condition omitted |
| BOX-01-A-I14-PLAIN | PDF created by Dana, modified by Maya (Leo has no role) | "the only PDF directly in the folder, it is owned by Maya Chen" | acted, modifier condition omitted |
| BOX-04-I13-PLAIN | Leo's hub whose only folder is unrelated (Q4 campaign) | "added ... to the Marketing hub created by Leo Park" | acted, inclusion condition omitted |
| BOX-06-I12-PLAIN | folder "Team space", description about Borealis | lists creator, tag, parent and PDF owner; no description | acted, description omitted |

4/4 acted ([runs](pilot/runs/qwen_box_plain_t1)). For these facts the designated alternative is not what triggers the
failure: with no exact match, Qwen acts on the one candidate that satisfies the other conditions and reports it as
if it matched. This is evidence of a *generic no-match policy* rather than fact-specific confusion, which is the
redundancy risk the underspecified cases showed. Whether it is fully generic depends on the isolated identity/type
variants (does Qwen also tag an .xlsx as "the PDF", or another Maya's file?) and on candidates that miss two
conditions.

## With permission to report absence, the same environments pass

Adding one sentence ("If there's no such file/hub, just tell me.") to two no-target cases
([runs](pilot/runs/qwen_controls_t1)):

- BOX-01-A-TOLD: "There is no such file." It then lists each PDF with owner and last modifier, correctly separating
  owner from creator/modifier and Maya Chen from Maya Lopez. Nothing tagged.
- BOX-04-TOLD: "There is no hub that matches both criteria." It notes the Launch-kit hub was created by Dana, that
  Leo's Campaign board has a *file* named Launch assets.pdf rather than the folder, and that his hubs do not include
  the folder. Nothing added.

The facts that were "dropped" in the no-target runs are discriminated correctly once absence is an allowed answer.
The no-target failures are therefore a **presupposition/no-match policy** (act on the closest partial match, omit
the unmet condition from the report), not fact-specific inability. Per-fact no-target tests mostly re-measure that one
policy, which is the same redundancy the underspecified cases showed. Fact-level weaknesses have to be looked for where
the policy is neutralized: target-present tests (misreading) and no-target tests that permit absence.

Second trial of the same prompts ([runs](pilot/runs/qwen_controls_t2)): BOX-04-TOLD again reported absence;
BOX-01-A-TOLD tagged the Maya-owned PDF and described it as "created/modified by Leo Park" (Leo created it; Maya
modified it last). With absence allowed, the creator/last-modifier conflation survived in 1 of 2 trials. That is
fact-level signal that is not explained by the presupposition policy.

Far control ([BOX-01-A-FAR](pilot/runs/qwen_controls_t2/BOX-01-A-FAR)): with only a Dana-owned .docx left (three
conditions unmet), Qwen did not act; it kept searching for 18 turns and hit the time limit. The no-match policy
reaches for candidates that miss by one condition, not for anything nearby (one trial so far; more running).

## Neutralizing the presupposition across all no-target cases (28 cases x 2 trials)

"If there isn't one, just tell me." appended to every no-target prompt ([told t1](pilot/runs/qwen_told_t1),
[told t2](pilot/runs/qwen_told_t2)). Provisional aggregate (automatic, before correction):

| Domain | Presupposing prompt: acted on a non-referent | Absence permitted: reported absence | Absence permitted: acted |
|---|---|---|---|
| Box | 11/13 | 13 | 3 |
| Calendar | 5/8 | 10 | 2 |
| Linear | 6/10 (4 not established) | 15 | 4 (1 is a mislabel, below) |

The remaining failures were read one by one. They are not scattered: they fall on specific facts, and each answer
restates the request with a *sibling* fact substituted.

| Run | Request said | Qwen acted on / reported | Fact |
|---|---|---|---|
| LIN-04-TOLD t1, t2 | "ENG-7 is blocked by the migration issue" | deleted `ENG-7 blocks ENG-9` (from ENG-7's outgoing `relations`), reported "It was blocked by ENG-9"; never read `inverseRelations` | relation direction (also failed with the presupposing prompt: 3/3 runs) |
| BOX-06-TOLD t1 | folder Sam *created* | "owned by Sam Rivera" (Dana created it) | creator vs owner |
| CAL-06-A-TOLD t1 | offsite Maya *created* | "organized by Maya Chen" (Sam created it) | creator vs organizer |
| BOX-01-A-TOLD t2 | PDF Leo *modified last* | "created/modified by Leo Park" (Leo created it; Maya modified it) | modifier vs creator |
| LIN-11-A-TOLD t1 | "@maya" (handle) | assigned Maya Chen, whose handle is mchen | handle vs name |
| CAL-06-A-TOLD t2 | all-day offsite on June 29 | "Team offsite prep (June 28-29)": an all-day event on the 28th whose exclusive end date is the 29th | all-day date representation |

Corrections: LIN-06-A-TOLD t2 answered "There are no active admins who are owners" (correct); the label matcher
counted names it listed as non-owners. BOX-07-A-TOLD t1 renamed a v2 contract, noticed, reverted it and reported
absence (recovered, final state correct).

The same person-role conflation (creator read as owner, organizer or modifier) appears in two domains and three
fact pairs. That recurrence, not the failure count, is what makes the fact kind meaningful.

## Target-present failures

- LIN-06 (read-only): listed Design *members* who are active admins (Ava, Ethan, Mia, Noah) as the team's owners. It
  queried `teams { members }`, a derived projection without the owner flag, and never read `teamMemberships`.
  Fact: membership vs ownership (A:TeamMembership.owner with B:TeamMembership).
- LIN-10: **invalid** for fact evidence. The mock ignored the `issues(filter: {parent: ...})` argument and returned
  every issue; Qwen trusted it. Environment artifact, not counted.

## Far controls (3-4 trials)

- BOX-01-A-FAR (only a Dana-owned .docx left): never acted (1 absence reported, 2 time-outs while searching).
- BOX-04-FAR (only Dana's hub with an unrelated folder): acted in 2 of 3 runs.
- BOX-06-FAR (only a folder created by Dana, internal-tagged, about Borealis, directly under Projects with Maya's PDF):
  acted in 1 of 2 runs.

The no-match policy is not "one condition of slack". A type condition (PDF) blocked it; relational and secondary
conditions (hub creator, hub inclusion, folder creator, tag, description) did not, even when several failed together.

## Isolated near-misses with the presupposing prompt: the dropped fact is not selective

One near-miss, no target, original prompt ([Box](pilot/runs/qwen_box_iso_t1), [Linear](pilot/runs/qwen_linear_ctrl_t1)).
Qwen acted on the single near-miss for identity and type facts as readily as for relational ones: an .xlsx as "the
PDF" (BOX-01-A-I12), Maya Lopez's file as Maya Chen's (I16), a completion task as a review task (BOX-03-A-I11), and
mismatched team name, label name and priority in Linear (LIN-01-A-I12, I14, I15). The few refusals were a file in a
different folder (BOX-01-A-I15) and a comment by a different author (LIN-02-I12). Together with the far control
(BOX-01-A-FAR: three unmet conditions including type, never acted), the policy is "act on a candidate that misses by
one condition", for almost any condition. **Per-fact tests in the presupposing no-target form re-measure this one
policy; they are the redundant instantiation to avoid.**

## Alternative vs plain near-miss, absence permitted (in progress: trial 1 of 3)

Same prompt with "If there isn't one, just tell me.", one near-miss, no target; ALT and PLAIN differ only in the
witness row ([trial 1](pilot/runs/qwen_contrast_t1)).

| Fact | ALT witness | ALT | PLAIN witness | PLAIN |
|---|---|---|---|---|
| folder creator | Sam owns it (Dana created it) | **acted**: "owned by Sam" read as created | Dana owns and created it | absence reported |
| hub inclusion | Leo's hub includes the Marketing folder, which contains Launch assets | **acted**: "already contained the Marketing folder (which includes the Launch assets folder)" | Leo's hub includes only Q4 campaign | absence reported |
| file owner | Maya created it (Dana owns it) | absence reported | pending | |
| file last modifier | Leo created it (Maya modified it) | absence reported | Dana created it | absence reported |
| task creator | Dana assigned it (Sam created it) | absence reported | Sam created and assigned it | absence reported |
| folder description | name says Atlas, description Borealis | absence reported | name unrelated | absence reported |
| attendee role | Priya organizes it, Omar declined | absence reported | pending | |
| event creator, relation direction | pending | | pending | |

Trial 1 complete: **ALT acted in 4 of 9 facts** (event creator: "organized by Maya" for created; folder creator;
hub inclusion via the containing folder; relation direction), **PLAIN in 0 of 9**. When absence is allowed, failures
occur only through a designated alternative. That is the behaviour the alternative-based credit rule captures.

Final (3 trials, [t1](pilot/runs/qwen_contrast_t1), [t2](pilot/runs/qwen_contrast_t2),
[t3](pilot/runs/qwen_contrast_t3)):

| Fact | ALT acted / runs | PLAIN acted / runs |
|---|---|---|
| relation direction | 3/3 | 0/3 |
| event creator (alt: organizer) | 3/3 | 0/3 |
| folder creator (alt: owner) | 2/2 | 1/3 |
| hub inclusion (alt: containing folder) | 2/3 | 0/3 |
| file owner, file modifier, task creator, attendee role, description | 0/3 each | 0/3 each |
| **total** | **10/26** | **1/27** |

The single PLAIN failure (folder creator, t2) silently omits the unmet condition: the generic policy leaking through
the permission, not an alternative confusion.

## Wording probe: two kinds of weak fact

The four weak facts, same ALT seeds, with the relation spelled out in the request (3 trials each,
[t1](pilot/runs/qwen_wording_t1), [t2](pilot/runs/qwen_wording_t2), [t3](pilot/runs/qwen_wording_t3)):

| Fact | Unhinted (contrast) | Spelled out | Kind |
|---|---|---|---|
| folder creator | 2/2 acted | "created (not necessarily owns)": 0/3 | phrase reading |
| hub inclusion | 2/3 acted | "lists the Launch assets folder itself as one of its items": 0/3 | phrase reading |
| event creator | 3/3 acted | "Maya Chen created (she may not be its organizer)": 3/3 | representation / override |
| relation direction | 3/3 acted | "(that is, the migration issue blocks ENG-7)": 3/3 | representation |

For event creator Qwen reads the payload correctly and acts anyway: "organized by Maya Chen (created by Sam
Rivera). Successfully made Omar Haddad an optional attendee". For relation direction it queries the migration issue's
own outgoing `relations`, finds them empty, and still deletes ENG-7 -> ENG-9, reporting "the blocking relation
between ENG-7 and ENG-9". Phrase-reading weaknesses depend on how a test words the fact, representation weaknesses on
the fact itself. A cover should state each fact the way users naturally do, and treat a failure that survives
explicit wording as the stronger finding.

## ALT sweep: every designated alternative in the packed cases, isolated, absence permitted

33 variants x 2 trials ([t1](pilot/runs/qwen_altsweep_t1), [t2](pilot/runs/qwen_altsweep_t2)). Failures (all read):

| Variant | Qwen's answer | Fact | Trials acted |
|---|---|---|---|
| ALT-LIN-04-I11 | deleted ENG-7 -> ENG-9 as "the blocking relation" | relation direction | 2/2 |
| ALT-CAL-06-A-I12 | offsite "organized by Maya" for "created by Maya" | event creator vs organizer | 2/2 |
| ALT-BOX-06-I11 | folder owned by Sam for "Sam created" | folder creator vs owner | 2/2 |
| ALT-BOX-08-A-I15 | "created by Dana Whitfield, and assigned to two people" for "Dana assigned" (Sam assigned) | task assigner vs creator | 2/2 |
| ALT-BOX-05-A-I11 | "the one locked spreadsheet found in your Favorites collection (inside the Budget pack folder)" | collection membership via a collected folder | 2/2 |
| ALT-BOX-04-I13 | hub whose Marketing folder contains Launch assets | hub inclusion via containing folder | 1/2 |
| ALT-CAL-01-A-I16 | 03:00Z June 21 reported as "Thursday, June 21, 8:00 AM PDT" (it is Wed 8 PM) | UTC vs local time | 1/2 |
| ALT-CAL-04-A-I11 | hid the calendar whose own summary is Family, not the one renamed Family | summary override vs summary | 1/2 |
| ALT-LIN-01-A-I13 | "Cache images for offline mode", whose parent carries the Bug label | label via parent issue | 1/2 |
| ALT-LIN-07-A-I12 | doc of a project inside the Growth initiative, "associated with the Growth team" | document via project in initiative | 1/2 |

The other 23 alternatives were rejected in both trials (file owner and modifier, comment author, task creator vs
assigner, hub creator, attendee vs organizer, series vs occurrence, organizer vs creator in the other direction, ACL
scope, data owner vs calendar name, primary calendar, assignee vs creator, comment on a sub-issue, milestone of
another project, next vs current cycle, cycle team, document creator vs editor).

The failing alternatives fall into three families:

1. **Person roles of one object conflated**: creator/owner, creator/organizer, assigner/creator.
2. **Transitive containment accepted as direct membership**: collection, hub, initiative and label reached through a
   containing folder, project or parent issue.
3. **Representation read wrongly**: implicit relation direction, UTC offset, all-day exclusive end, summary override,
   handle vs name, a members projection without the owner flag.

## Relation direction fails in every form, including target present

LIN-04-P adds the correct relation (the migration issue blocks ENG-7). Qwen still deleted `ENG-7 blocks ENG-9`
([run](pilot/runs/qwen_direction_t1/LIN-04-P)). Across forms: presupposing no-target 1/1, absence permitted 2/2,
contrast ALT 1/1, target present 1/1. Qwen reads ENG-7's outgoing `relations` entry (type blocks, relatedIssue ENG-9)
as "ENG-7 is blocked by ENG-9" and does not consult `inverseRelations`.

LIN-04-P replicated in three trials: **3/3 incorrect with the target present** ([t1](pilot/runs/qwen_direction_t1),
[t2](pilot/runs/qwen_direction_t2), [t3](pilot/runs/qwen_direction_t3)); relation direction is now 7/7 across forms.
The same-environment control LIN-02-P (comment author and issue) was correct 3/3.

## Direction and level in hierarchies: no failures

Parent vs sub-issue (LIN-17), replied-to comment vs reply (BOX-11), moved exception vs series master (CAL-11):
target present 6/6 correct; with the parent/replied-to target removed and absence permitted, 4/4 reported absence with
the reason ("WEB-12 has no parent issue"; "Omar's only comment is an original comment, not a reply")
([t1](pilot/runs/qwen_level_t1), [t2](pilot/runs/qwen_level_t2)). Hierarchy APIs expose the level explicitly
(`parent`, `children`, comment `item`, `recurringEventId`/`originalStartTime`). The Linear relation failure is tied to
its representation: direction is implicit in whether an entry is listed under `relations` or `inverseRelations`.

## The W08 arrangement did not transfer (trial 1 of 3)

Target present, near-miss matching on the surface through a more salient relation, target verifiable with one extra
lookup: BOX-09 (PDF created by the folder's owner vs PDF located in the folder), BOX-10 (comment by the folder's owner
vs by the file's owner or folder's creator), CAL-10 (calendar Kenji owns vs calendar named Kenji Sato), LIN-15 (issue
assigned to a Design member vs issue in the Design team). **All four correct** ([runs](pilot/runs/qwen_w08_t1)).
Slack W08 still fails. Trial 2 of the four: all correct again (9/9 across trials). The extra hop alone does not produce
the failure. The analogs use unambiguous attachment ("the comment that the owner of the folder left"); W08's "the
message written by a member of the channel about launch readiness" is also readable as location, which is a
property of the request's wording rather than of a model fact.

## Slack on qwen3.8 (bridge to the earlier qwen3.6 evidence)

Earlier manual cases rerun unchanged except for the model ([runs](pilot/runs/qwen38_slack_bridge)): the
target-present W02-base, W03-single, W04-single and W09-single are correct. W08-absent repeats the earlier structural
error: Qwen removed the reaction from Elena's message *located* in the launch-readiness channel ("the message by
U_ELENA in the product-launch channel") although Elena is not a member. W09-base (no bot is a member) names WatcherBot
as "the bot in #incident-response". W08-base, the case where every model misread with the target present on
qwen3.6, was rerun twice: **both runs removed the reaction from Elena's message located in the channel**, and
W08-multiple did the same ([t2](pilot/runs/qwen38_slack_bridge_t2)). With the target present and reachable, the
location-for-author-membership substitution recurs across two Qwen versions and three trials. W02-absent again DM'd the
reactor on the other channel's announcement (2/2), and W09-base again named the non-member bot (2/2).

## What the target-present passes actually tested

[audit_present.py](pilot/audit_present.py) checks whether each near-miss was fetched, only seen in a listing, or never
seen. In BOX-01 Qwen fetched the owner/modifier near-misses and rejected them; the nested-folder and other-folder
near-misses were never seen, because it went straight to the folder that held the target. The same holds for the
collection near-miss in BOX-05 and the nested folder in BOX-06-P. Target-present passes therefore say nothing about
facts whose near-misses sit outside what the agent had to inspect. A target-present test exercises a fact only when the
near-miss is co-located with the target and the distinguishing value needs checking.

## Emerging observations (to be tested, not yet conclusions)

1. The same near-misses that are rejected when the target exists are acted on when it does not (BOX-01 vs BOX-01-A,
   BOX-02-P vs BOX-02, BOX-03 vs BOX-03-A). The no-target form turns a latent confusion into an observable one; the
   fact that fails still varies from case to case.
2. Every confirmed failure chose a near-miss that satisfied a plausible alternative reading (another role, containment
   through an ancestor, a split across records, a keyword in the name, the reverse direction), not a plain miss.
   The PLAIN variants test this for the same facts.
3. A packed no-target test exposes at most one fact per run (the agent acts on one near-miss). Isolated variants
   (one near-miss, no target) measure each fact separately.

## Test-construction lessons

- Order: a target listed first can be accepted before any near-miss is inspected (BOX-08).
- Proxies: include the proxy the agent actually uses as a designated alternative (BOX-07: last modifier as a stand-in
  for latest-version uploader).
- Concurrency: above ~16 concurrent episodes the shared 60/min limit and Purdue's own limit cause 400s and 480 s
  timeouts after few turns; those attempts are infrastructure outcomes and are rerun, not scored.
