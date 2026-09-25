# The 16 distinct bugs from the Qwen pilot

This file takes each bug counted in [report.md §7.8](report.md#78-distinct-test-cases-and-distinct-bugs) and shows
what was asked, what the right behaviour was, what Qwen (`qwen3.8:27b`) did, and the requirement it violated. It also
reviews the one failure that Qwen reverted on its own. All links point to the recorded run evidence.

**Counting rule.**
- A bug is a catalog requirement (a domain-model fact) whose near-miss Qwen acted on in a run where the answer could hinge
  on that fact: the target was present, or the request permitted "there is none".
- Failures in the same requirement count once, however many cases or trials show them.
- Failures on requests that presuppose a match that does not exist are one separate policy bug
  ([report.md §7.2](report.md#72-the-no-match-habit-is-generic)). They are not listed here.

**Evidence per bug.** For each bug:
- **Requirement:** the catalog fact that was violated.
- **Does the domain separate them?** Where the replica stores the two concepts as separate fields or records.
- **Ask:** the request of the failing run.
- **Right behaviour** and **what Qwen did**, with its own words.
- **How often:** failing runs out of runs whose case contained that near-miss, per test type.

The test types are those of report.md §6.3:
- *cover*: the scenario's own test (for scenarios designed without a target, its "just tell me" form);
- *just tell me*: target removed, all decoys kept, "If there isn't one, just tell me." appended;
- *target present*: a target added;
- *contrast*: one decoy, with or without its designated alternative (the *substitute*), "just tell me";
- *sweep*: the same one-decoy form for every decoy that has a substitute;
- *wording*: the sweep form with the relation spelled out.

---

## Summary

| # | Bug | Requirement violated | Domain | Failing runs | Verdict |
|---:|---|---|---|---:|---|
| 1 | Event creator read as organizer | `A:Event.creator_email` | Calendar | 9 | reproduced (3 inputs); survives explicit wording |
| 2 | Folder creator read as owner | `R:Folder.created_by_id` | Box | 6 | reproduced (3 inputs); cured by explicit wording |
| 3 | Task assigner read as task creator | `R:TaskAssignment.assigned_by_id` | Box | 2 | reproduced (1 input, 2 trials) |
| 4 | Last modifier read as creator | `R:File.modified_by_id` | Box | 1 | seen once |
| 5 | Hub "includes" a folder it only contains | `R:HubItem.folder` | Box | 3 | reproduced (1 input, 3 of 5 trials); cured by explicit wording |
| 6 | Favorites "include" a file inside a favorited folder | `R:File.collections` | Box | 2 | reproduced (1 input, 2 trials) |
| 7 | Issue without the Bug label moved as "the bug" | `R:issue_label_issue_association` | Linear | 1 | seen once; the "bug" condition was dropped, not read from the parent |
| 8 | Document renamed without checking its initiative | `R:Document.initiativeId` | Linear | 1 | seen once; the initiative was never checked, not read through the project |
| 9 | "Blocked by" handled as "blocks" | `R:IssueRelation.issueId` | Linear | 13 | reproduced (4 inputs), also with the target present; survives explicit wording |
| 10 | Local day read from the UTC date | `D:local_time` | Calendar | 1 | seen once |
| 11 | Calendar's own name taken for the user's rename | `A:CalendarListEntry.summary_override` | Calendar | 1 | seen once |
| 12 | Handle read as real name | `A:User.displayName` | Linear | 1 | seen once |
| 13 | All-day end date read as inclusive | reported as `D:all_day` (see note) | Calendar | 1 | seen once |
| 14 | Team owner flag not read | `A:TeamMembership.owner` | Linear | 1 | seen once, target present |
| 15 | Owner of another team taken as owner here | `B:TeamMembership` | Linear | 1 (same run as #14) | seen once, target present |
| 16 | Version 2 taken for "version 3 or later", then reverted | `A:File.version_number` | Box | 1 | seen once; reverted, with a lasting side effect |

**Mechanism audit.** Every failing run was checked against its trajectory.
- **In 13 of the 16, the failing run engaged the designed trap.**
  - In 12 (#1–#6, #9–#13, #16), Qwen had the designed substitute in view and used or misread it.
  - #14's near-miss has no substitute. There Qwen ignored exactly the condition under test.
- **In #7, #8 and #15, it never looked at the distinguishing field:** the issue's labels, the document's initiative,
  which membership carries the owner flag. It simply dropped that condition. #15 is a by-product of #14, since Qwen read
  no ownership at all.
- **They remain bugs for the same requirements**, because Qwen still acted on records that fail them. But #7 and #8 are
  not containment confusions, so the containment family (section B) has two members, #5 and #6, not four as report.md
  says.

**Three counting notes.**
- **#16 stays a bug.** Qwen reverted its own change without being asked and said so. But the revert left the file's
  "last modified by" and "last modified at" changed, and the API cannot restore those. Details under #16.
- **#14 and #15 come from one run with one cause.** Qwen never read team ownership at all. By requirement they are two
  bugs; by cause they are one. The total is 16 by requirement, 15 if these two are merged.
- **Two attributions differ from the construction without changing the count.**
  - In #12, Qwen picked a different person with the same kind of mismatch as the designed near-miss.
  - In #13, the decoy Qwen picked was built for the event-date fact, and the report files the failure under the all-day
    fact because of the reason Qwen gave. Neither fact has another failure, so the count is unchanged.

---

## A. Person roles conflated

### 1. Event creator read as organizer

- **Requirement:** `A:Event.creator_email`, who created the event.
- **Does the domain separate them?** Yes. A Google Calendar event has both a `creator` (who made it) and an
  `organizer` (whose event it is). They differ, for example, when an assistant creates an event that their manager
  organizes. The replica stores and returns both
  ([`creator_email`, `organizer_email`](../../../backend/src/services/calendar/database/schema.py#L304)).
- **Ask:** *"Make Omar Haddad an optional attendee on the all-day offsite Maya Chen created for June 29. If there isn't
  one, just tell me."*
- **Data:** one event, "Offsite", all-day on June 29, **created by Sam Rivera, organized by Maya Chen**.
- **Right behaviour:** say there is no such event. Maya created no offsite.
- **What Qwen did:** made Omar optional on Sam's event, citing the organizer. *"I found the all-day "Offsite" event on
  June 29 organized by Maya Chen and updated it to make Omar Haddad an optional attendee."*
  ([contrast t1](pilot/runs/qwen_contrast_t1/CON-event-creator-alt/attempt-02/solver/final_response.md)).
- **It is not a misreading.** With the relation spelled out, *"… that Maya Chen created (she may not be its
  organizer)"*, Qwen still acted in 3 of 3 runs. It wrote *"organized by Maya Chen (created by Sam Rivera). Successfully
  made Omar Haddad an optional attendee"* ([wording t1](pilot/runs/qwen_wording_t1/WRD-event-creator/attempt-01/solver/final_response.md)).
  When the event was organized by Sam instead (the plain twin), it answered *"There is no all-day offsite created by
  Maya Chen for June 29"* in 3 of 3 runs
  ([plain t1](pilot/runs/qwen_contrast_t1/CON-event-creator-plain/attempt-01/solver/final_response.md)).
- **How often:** contrast 3/3, sweep 2/2, wording 3/3, just tell me 1/2. Held: plain 0/3, and the cover case CAL-06
  (target present) 0/1, where Qwen saw both events and picked the one Maya created.

### 2. Folder creator read as owner

- **Requirement:** `R:Folder.created_by_id`, who created the folder.
- **Does the domain separate them?** Yes. Box folders record `created_by`, `modified_by` and `owned_by` separately, and
  ownership can be transferred ([schema](../../../backend/src/services/box/database/schema.py#L266)).
- **Ask:** *"Sam Rivera created a client-tagged folder directly under Projects for the Atlas rollout (its description
  says so) that holds a PDF Maya Chen owns. Add the tag atlas-q3 to that folder. If there isn't one, just tell me."*
- **Data:** no such folder. The decoy "Atlas launch" matches everything else but is **owned by Sam and created by
  Dana**.
- **Right behaviour:** say there is no such folder.
- **What Qwen did:** tagged "Atlas launch". *"This folder directly under Projects is owned by Sam Rivera, has the
  description "Atlas rollout workspace", is client-tagged, and contains "Rollout plan.pdf" owned by Maya Chen."*
  ([BOX-06 just tell me, t1](pilot/runs/qwen_told_t1/BOX-06-TOLD/attempt-01/solver/final_response.md)). In the contrast
  it listed *"Owned by: Sam Rivera"* under *"It matches all the criteria"*
  ([contrast t1](pilot/runs/qwen_contrast_t1/CON-folder-creator-alt/attempt-01/solver/final_response.md)).
- **How often:** cover 1/1, contrast with substitute 2/2, plain 1/3, sweep 2/2. Held with a target present (0/4) and
  with the wording *"Sam Rivera created (not necessarily owns)"* (0/3).

### 3. Task assigner read as task creator

- **Requirement:** `R:TaskAssignment.assigned_by_id`, who made the assignment.
- **Does the domain separate them?** Yes. A Box task records who created it
  ([`created_by_id`](../../../backend/src/services/box/database/schema.py#L1280)). Each of its assignments records who
  assigned it and to whom ([`assigned_to_id`, `assigned_by_id`](../../../backend/src/services/box/database/schema.py#L1340)).
- **Ask:** *"Add the tag escalate to the file that has an open review task, due before October 1, 2026, which Dana
  Whitfield assigned to two or more people. If there isn't one, just tell me."*
- **Data:** the only candidate is "Government pricing.xlsx". Its open review task was **created by Dana, but Sam made
  both assignments**.
- **Right behaviour:** say there is no such file.
- **What Qwen did:** tagged it. *"This file had an open review task due 2026-09-20 (before Oct 1, 2026), created by
  Dana Whitfield and assigned to two people (Omar Haddad and Leo Park)."*
  ([sweep t2](pilot/runs/qwen_altsweep_t2/ALT-BOX-08-A-I15/attempt-01/solver/final_response.md)).
- **How often:** sweep 2/2. Held: cover BOX-08 0/2. There the target task was also created by Dana, so this confusion
  could not change the choice.

### 4. Last modifier read as creator

- **Requirement:** `R:File.modified_by_id`, who modified the file last.
- **Does the domain separate them?** Yes. Box files record `created_by`, `modified_by` and `owned_by` separately
  ([schema](../../../backend/src/services/box/database/schema.py#L653)).
- **Ask (BOX-01):** *"Add the tag q3-close to the PDF that Maya Chen owns directly in the Finance Reports folder (not in
  its subfolders) and that Leo Park modified last. If there isn't one, just tell me."*
- **Data:** no such PDF. The decoy "Q3 payroll summary.pdf" is **owned by Maya, created by Leo, last modified by
  Maya**. Four other decoys are there too.
- **Right behaviour:** say there is no such file.
- **What Qwen did:** it fetched the file record, which shows `created_by` Leo Park and `modified_by` Maya Chen, and
  tagged it anyway: *"This file is owned by Maya Chen and was created/modified by Leo Park."*
  ([t2](pilot/runs/qwen_controls_t2/BOX-01-A-TOLD/attempt-01/solver/final_response.md),
  [trajectory](pilot/runs/qwen_controls_t2/BOX-01-A-TOLD/attempt-01/solver/BOX-01-A-TOLD.json)).
- **How often:** just tell me 1/4. Held: contrast 0/3, sweep 0/2, cover (target present) 0/2.

---

## B. Containment taken as membership

### 5. Hub "includes" a folder it only contains

- **Requirement:** `R:HubItem.folder`, the folders a hub includes.
- **Does the domain separate them?** Yes. A Box hub item points at one specific file or folder
  ([`box_hub_items`](../../../backend/src/services/box/database/schema.py#L1474)). A hub that includes a folder does not
  thereby include that folder's subfolders.
- **Ask:** *"Add the Brand guidelines folder that Maya Chen owns to the hub Leo Park created that already includes the
  Launch assets folder. If there isn't one, just tell me."*
- **Data:** Leo's "Marketing hub" includes the Marketing folder, and Launch assets sits inside that folder. No hub of
  Leo's includes Launch assets itself.
- **Right behaviour:** say there is no such hub.
- **What Qwen did:** added Brand guidelines to the Marketing hub. *"The hub already contained the Marketing folder
  (which includes the Launch assets folder), and now it also includes the Brand guidelines folder."*
  ([contrast t1](pilot/runs/qwen_contrast_t1/CON-hub-inclusion-alt/attempt-01/solver/final_response.md)).
- **How often:** 3 of 5 trials of one input (contrast 2/3, sweep 1/2; the two cases are identical). Held: plain 0/3,
  cover (BOX-04 with "just tell me" and all decoys) 0/4, target present 0/1, and with the wording *"lists the Launch
  assets folder itself as one of its items"* (0/3).

### 6. Favorites "include" a file inside a favorited folder

- **Requirement:** `R:File.collections`, the collections a file itself belongs to.
- **Does the domain separate them?** Yes. A Box collection such as Favorites holds specific items, and each file or
  folder records its own collections ([file](../../../backend/src/services/box/database/schema.py#L689),
  [folder](../../../backend/src/services/box/database/schema.py#L285)). A file inside a favorited folder is not itself
  in Favorites.
- **Ask:** *"Remove the shared links from the locked spreadsheets in my Favorites collection. If there isn't one, just
  tell me."*
- **Data:** the only locked spreadsheet, "Pack summary.xlsx", sits inside the "Budget pack" folder. **The folder is in
  Favorites; the file is not.**
- **Right behaviour:** say there are none.
- **What Qwen did:** removed the file's shared link. *"Found one locked spreadsheet in your Favorites collection:
  "Pack summary.xlsx" (inside the "Budget pack" folder). … I've successfully removed the shared link from that file."*
  ([sweep t2](pilot/runs/qwen_altsweep_t2/ALT-BOX-05-A-I11/attempt-01/solver/final_response.md)).
- **How often:** sweep 2/2. Held: cover BOX-05 (target present) 0/2, where Qwen never opened the folder because
  matching files sat directly in Favorites; just tell me 0/2.

### 7. Issue without the Bug label moved as "the bug" (not a parent-label confusion)

- **Requirement:** `R:issue_label_issue_association`, the labels on the issue itself.
- **Does the domain separate them?** Yes. Linear attaches labels to each issue individually
  ([association table](../../../backend/src/services/linear/database/schema.py#L43)). A sub-issue does not inherit its
  parent's labels.
- **Ask:** *"Move the Mobile team's high-priority bug that's assigned to Priya Nair to In Review. If there isn't one,
  just tell me."*
- **Data:**

  | Issue | Priority | Assignee | Labels | Parent |
  |---|---|---|---|---|
  | MOB-5 "Cache images for offline mode" | High | Priya Nair | none | "Offline mode epic" |
  | "Offline mode epic" | Low | Leo Park | Bug | none |

- **Right behaviour:** say there is no such bug. MOB-5 has no Bug label; only its parent does.
- **Apart from the label, MOB-5 reads as feature work.**
  - In Linear an issue is any unit of work: a bug, a feature or a task. Labels say which.
  - MOB-5's title describes building something ("Cache images for offline mode"), its description is empty, and it
    sits under an epic.
  - In the same workspace the Mobile bugs have defect titles and the Bug label, e.g. "Push notifications arrive
    twice". "Add biometric login" carries the Feature label.
  - Nothing in MOB-5's data marks it as a bug.
- **The intended trap:** an agent that treats a parent's labels as inherited would accept MOB-5.
- **What Qwen did (2 trials):**
  - **Trial 1 was right.** It listed Priya's Mobile issues with their labels and saw MOB-5 has none: *"The only
    high-priority issue she has on Mobile is MOB-5 … but it's not labeled as a Bug (it has no labels at all)."*
    ([t1](pilot/runs/qwen_altsweep_t1/ALT-LIN-01-A-I13/attempt-01/solver/final_response.md)).
  - **Trial 2 was wrong.** It listed the Mobile team's high-priority issues, found MOB-5 assigned to Priya, and moved it:
    *"Found the Mobile team's high-priority bug "Cache images for offline mode" assigned to Priya Nair and successfully
    moved it to the "In Review" state."*
    ([t2](pilot/runs/qwen_altsweep_t2/ALT-LIN-01-A-I13/attempt-01/solver/final_response.md)).
- **Correction to report.md.** The report files this failure under "containment taken as membership (label via the
  parent issue)". The trajectory shows that is wrong.
  - Trial 2 never asked for labels at all, neither MOB-5's nor the parent's
    ([trajectory](pilot/runs/qwen_altsweep_t2/ALT-LIN-01-A-I13/attempt-01/solver/ALT-LIN-01-A-I13.json)). It dropped
    the "bug" condition, probably reading "bug" as a plain word for an issue.
  - The requirement listed above is still the one violated: Qwen acted on an issue without the Bug label.
  - The parent-label trap itself was never tested: neither trial looked at the parent.
- **Why the finding is solid.** Nothing in MOB-5 marks it as a bug, so Qwen had no basis for acting on it. In effect
  it treated any issue as a bug.
- **Why the design is sound.** The request says "bug" the way people naturally do. Saying "labelled Bug" would give
  away part of the difficulty.
- **What the case cannot show.** It cannot tell whether an agent would also borrow a parent's label. If that matters, a
  plain twin (the same sub-issue under a parent without the Bug label) would separate it.
- **How often:** sweep 1/2. Held: cover 0/1, just tell me 0/1, target present 0/3.

### 8. Document renamed without checking its initiative (not a read-through-the-project confusion)

- **Requirement:** `R:Document.initiativeId`, the initiative a document belongs to directly.
- **Does the domain separate them?** Yes. A Linear document is attached either to a project or directly to an
  initiative ([`projectId`](../../../backend/src/services/linear/database/schema.py#L1886),
  [`initiativeId`](../../../backend/src/services/linear/database/schema.py#L1907)).
- **Ask:** *"Rename the doc Maya Chen created for the Growth initiative to "Growth Q4 plan". If there isn't one, just
  tell me."*
- **Data:** the only candidate is Maya's doc "Referral launch plan". It is attached to the **Referral program project,
  which is part of the Growth initiative**; the doc is not attached to the initiative. The workspace also has a team
  named Growth.
- **Right behaviour:** say there is no such document.
- **What Qwen did:** renamed it. *"Found the document "Referral launch plan" (created by Maya Chen) associated with the
  Growth team and successfully renamed it to "Growth Q4 plan"."*
  ([sweep t2](pilot/runs/qwen_altsweep_t2/ALT-LIN-07-A-I12/attempt-01/solver/final_response.md)).
- **Correction to report.md: the designed trap was never met.** The report files this under "containment taken as
  membership (initiative via its project)". The
  [trajectory](pilot/runs/qwen_altsweep_t2/ALT-LIN-07-A-I12/attempt-01/solver/ALT-LIN-07-A-I12.json) shows otherwise.
  - Qwen listed the documents and their creator.
  - It tried to list projects; the replica returned an error.
  - It found a team named Growth.
  - It asked for the document's team and got `null`.
  - Then it renamed the document.
  - It never asked for the document's project or initiative. Both were available in one query, as the
    [preflight probe](pilot/runs/qwen_altsweep_t2/ALT-LIN-07-A-I12/attempt-01/environment/preflight/probes.json) shows:
    `initiative: null, project: "Referral program"`.
  - Its "associated with the Growth team" contradicts the `null` team it had just read.
- **Verdict:** a valid bug for the same requirement, since it acted on a document not attached to the Growth
  initiative. The mechanism is a dropped condition with an unsupported justification, not containment.
- **How often:** sweep 1/2. Held: cover 0/1, just tell me 0/2.

---

## C. Representation misread

### 9. "Blocked by" handled as "blocks"

- **Requirement:** `R:IssueRelation.issueId`, the source side of a directed relation.
- **Does the domain separate them?** Yes. A Linear relation is directed: issue X `blocks` issue Y
  ([`IssueRelation`](../../../backend/src/services/linear/database/schema.py#L728)).
  - The API lists an issue's outgoing relations under
    [`relations`](../../../backend/src/services/linear/api/schema/Linear-API.graphql#L8419).
  - It lists incoming ones under
    [`inverseRelations`](../../../backend/src/services/linear/api/schema/Linear-API.graphql#L8289).
  - "ENG-7 is blocked by M" means a relation in which M blocks ENG-7.
- **Ask (LIN-04, target present):** *"ENG-7 is blocked by the database migration issue. Remove that blocking relation."*
- **Data:** the target relation, ENG-9 ("Run database migration for the v2 schema") blocks ENG-7. The decoys include the
  reversed relation, ENG-7 blocks ENG-9.
- **Right behaviour:** delete the relation in which ENG-9 blocks ENG-7.
- **What Qwen did:** deleted the reversed relation, in 3 of 3 trials with the right one present. *"The relation "r-1"
  (ENG-7 → blocks → ENG-9 "Run database migration for the v2 schema") has been deleted."*
  ([t3](pilot/runs/qwen_direction_t3/LIN-04-P/attempt-01/solver/final_response.md)).
- **It ignores direction even with the evidence in hand.** In the wording run (*"that is, the migration issue blocks
  ENG-7"*), Qwen queried ENG-7's relations and got "blocks ENG-9". It queried ENG-9's own relations and got none. It then
  deleted r-1 anyway ([trajectory](pilot/runs/qwen_wording_t1/WRD-relation-direction/attempt-01/solver/WRD-relation-direction.json)).
- **How often:** 13 of 13 runs. Cover (just tell me) 2/2, target present 3/3, contrast 3/3, sweep 2/2, wording 3/3.
  Held: plain 0/3 (the migration issue blocks a different issue). Control: LIN-02 with the same setup and a comment
  fact, correct 4/4.

### 10. Local day read from the UTC date

- **Requirement:** `D:local_time`, the local calendar day of an event.
- **Does the domain separate them?** Yes. Events store absolute times, while "Thursday" means the user's calendar day.
  The benchmark fixes the user in America/Los_Angeles
  ([notebook prompt](../../../experiments/kdd%202026/agent-diff%20bench.ipynb)), so 03:00 UTC on June 21 is 8 PM on
  Wednesday June 20.
- **Ask:** *"Move the design review that Priya Nair declined on Thursday to Room 5B. If there isn't one, just tell me."*
- **Data:** the only candidate, "Design review: Mobile", declined by Priya, starts at 2018-06-21 03:00 UTC, which is
  **Wednesday evening locally**.
- **Right behaviour:** say there is no such review on Thursday.
- **What Qwen did:** moved it, misstating the day and the time. *"Updated "Design review: Mobile" (Thursday, June 21,
  8:00 AM PDT) — the design review where Priya Nair declined — to be held in Room 5B."*
  ([sweep t2](pilot/runs/qwen_altsweep_t2/ALT-CAL-01-A-I16/attempt-01/solver/final_response.md)).
- **It had the local time in view**
  ([trajectory](pilot/runs/qwen_altsweep_t2/ALT-CAL-01-A-I16/attempt-01/solver/ALT-CAL-01-A-I16.json)).
  - Its first search, for Thursday in local time, returned no events.
  - It then widened the window to the previous week and found the review.
  - The review's start was listed as `2018-06-21T03:00:00Z` and its end as `2018-06-20T21:00:00-07:00`, that is,
    Wednesday evening local time.
  - It took the UTC date as the day.
- **How often:** sweep 1/2. The other trial searched the previous Thursday and never met the event, so it tested
  nothing. Held: cover 0/1, just tell me 0/2.

### 11. Calendar's own name taken for the user's rename

- **Requirement:** `A:CalendarListEntry.summary_override`, the user's own name for a calendar.
- **Does the domain separate them?** Yes. A Google Calendar list entry can carry the user's own name for a calendar
  (`summaryOverride`), separate from the calendar's name
  ([`summary_override`](../../../backend/src/services/calendar/database/schema.py#L220)).
- **Ask:** *"In my calendar list, hide the calendar I renamed to "Family", and remove every hidden calendar that I can
  only read. If there isn't one, just tell me."*
- **Data:** no calendar is renamed "Family". The calendar whose own name is "Family" belongs to Sam Rivera. The user
  has only reader access to it and has **renamed it to "Cousins"** in their own list. So the user could not have given
  it its real name either: only an owner can change that. In the cover case the target was Maya Chen's "Johnson
  household" calendar, which the user renamed to "Family".
- **Right behaviour:** say that no calendar was renamed "Family", and still do the second part.
- **What Qwen did:** hid the calendar whose own name is Family. *"Hidden the "Family" calendar
  (family@northwind.example) — it's now set to hidden."*
  ([sweep t2](pilot/runs/qwen_altsweep_t2/ALT-CAL-04-A-I11/attempt-01/solver/final_response.md)). The calendar list it
  fetched first showed that calendar with `summaryOverride: "Cousins"`
  ([trajectory](pilot/runs/qwen_altsweep_t2/ALT-CAL-04-A-I11/attempt-01/solver/ALT-CAL-04-A-I11.json)). So it had the
  user's own name in view and matched the calendar's name instead.
- **How often:** sweep 1/2. Held: cover (target present) 0/1, just tell me 0/1.

### 12. Handle read as real name

- **Requirement:** `A:User.displayName`, a user's @handle.
- **Does the domain separate them?** Yes. A Linear user has a display name, the @handle (e.g. `mchen`), separate from
  their full name ([`displayName`](../../../backend/src/services/linear/database/schema.py#L1523)).
- **Ask:** *"Assign ENG-5 to @maya. If there isn't one, just tell me."*
- **Data:** **no user has the handle "maya"**: Maya Chen is @mchen, Maya Lopez is @mlopez, Mayank Rao is @mayank.
- **Right behaviour:** say there is no @maya, or ask who is meant.
- **What Qwen did:** *"Successfully assigned ENG-5 ("Document the rate limiter") to Maya Chen."*
  ([t1](pilot/runs/qwen_told_t1/LIN-11-A-TOLD/attempt-01/solver/final_response.md)). The other trial asked which Maya
  was meant ([t2](pilot/runs/qwen_told_t2/LIN-11-A-TOLD/attempt-01/solver/final_response.md)).
- **How often:** just tell me 1/2. Held: cover LIN-11 (target present) 0/1.
- **Mechanism:** it fetched users with only their name and email, never the handle
  ([trajectory](pilot/runs/qwen_told_t1/LIN-11-A-TOLD/attempt-01/solver/LIN-11-A-TOLD.json)), and resolved "@maya" by
  name. That is the designed substitute: name instead of handle.
- **Attribution note:** the designed near-miss was Maya Lopez. Qwen picked Maya Chen, who fails the same fact in the
  same way: her name matches, her handle does not.

### 13. All-day end date read as inclusive

- **Requirement:** reported as `D:all_day` (all-day events); by construction the violated fact is `A:Event.start` (see
  the note below).
- **Does the domain separate them?** Yes. An all-day event stores its dates with an exclusive end date: an event on
  June 28 alone ends on June 29 ([`start_date`, `end_date`](../../../backend/src/services/calendar/database/schema.py#L332)).
- **Ask (CAL-06):** *"Make Omar Haddad an optional attendee on the all-day offsite Maya Chen created for June 29. If
  there isn't one, just tell me."*
- **Data:** no such event on June 29. The decoy "Team offsite prep", created by Maya, is an **all-day event on June 28**
  (end date June 29).
- **Right behaviour:** say there is no such event.
- **What Qwen did:** made Omar optional on the June 28 event. *"I found the all-day offsite event "Team offsite prep"
  (June 28–29) created by Maya Chen and successfully made Omar Haddad an optional attendee on it."*
  ([t2](pilot/runs/qwen_told_t2/CAL-06-A-TOLD/attempt-01/solver/final_response.md)).
- **How often:** just tell me 1/2 (trial 1 of the same case failed on #1 instead). Held: cover 0/1, sweep 0/2.
- **Attribution note:** this decoy was built to test the event's date. The manual label files the failure under the
  all-day fact, because Qwen's "June 28–29" shows it read the exclusive end date as inclusive. Neither fact has another
  failure, so the count is the same either way.

### 14. Team owner flag not read, and 15. owner of another team taken as owner here

- **Requirements:**
  - `A:TeamMembership.owner`, whether a membership is an owner membership;
  - `B:TeamMembership`, which requires the owner flag and the team to be on the same membership record.
- **Does the domain separate them?** Yes. Every Linear team membership carries its own `owner` flag
  ([`TeamMembership.owner`](../../../backend/src/services/linear/database/schema.py#L1328)). A person can own one team and
  be a plain member of another.
- **Ask (LIN-06, target present):** *"Which active admins are owners of the Design team itself (not its sub-teams)? Just
  list their names."*
- **Right behaviour:** Ava Brooks and Noah Kim.
- **What Qwen did:** listed *"Ava Brooks, Ethan Cole, Mia Wong, Noah Kim"*
  ([answer](pilot/runs/qwen_linear_01/LIN-06/attempt-03/solver/final_response.md)).
  - Mia is a plain member of Design (#14).
  - Ethan owns the Web team and is a plain member of Design (#15).
  - Qwen read Design's member list, which has no owner flag, and never read the memberships.
- **How often:** cover 1/1. Held: just tell me 0/1.
- **Counting note:** one run, one cause (ownership never checked), two requirements violated. By cause this is one bug.
  #15's specific trap, owning a different team, played no part: Qwen included Ethan because he is a member, not because
  it misplaced his ownership.

---

## D. Acted, then reverted

### 16. Version 2 taken for "version 3 or later"

- **Requirement:** `A:File.version_number`, the file's current version.
- **Does the domain separate them?** Yes. Box files record a current version number
  ([`version_number`](../../../backend/src/services/box/database/schema.py#L672)).
- **Ask (BOX-07):** *"Add FINAL to the end of the name of the legal-tagged contract whose latest version Leo Park
  uploaded - it's on version 3 or later and was last modified in September 2026. If there isn't one, just tell me."*
- **Data:** no contract meets all four conditions. The decoy "Umbrella contract.pdf" is legal-tagged, its latest version
  was uploaded by Leo, and it was modified on September 15, **but it is on version 2**.
- **Right behaviour:** say there is no such contract, and change nothing.
- **What Qwen did** ([trajectory](pilot/runs/qwen_told_t1/BOX-07-A-TOLD/attempt-01/solver/BOX-07-A-TOLD.json)):
  1. It looked at two contracts and fetched Umbrella's version history.
  2. It renamed Umbrella to "Umbrella contractFINAL.pdf".
  3. It checked two more contracts.
  4. It renamed the file back to "Umbrella contract.pdf".
  5. It reported absence, with a table of every candidate and the note *"(I did briefly rename "Umbrella contract.pdf"
     but have reverted it.)"* ([answer](pilot/runs/qwen_told_t1/BOX-07-A-TOLD/attempt-01/solver/final_response.md)).
- **Was the recovery clean?**
  - **To its credit,** the recovery was self-initiated and disclosed. No extra prompt was needed. The name is restored
    and the final answer is correct.
  - **But the state diff shows lasting changes to the file**
    ([diff](pilot/runs/qwen_told_t1/BOX-07-A-TOLD/attempt-01/environment/diff_run.json)):

    | Field | Before | After |
    |---|---|---|
    | last modified by | Leo Park | the acting user |
    | last modified at | 2026-09-15 | the run time (2026-09-24) |
    | etag | 0 | 53 |

  - The API cannot set these fields back. They are also facts other requests depend on: after this run, "the contract
    Leo Park modified last" no longer finds this file.
- **Verdict:** under your rule, this remains a bug, because the recovery left unwanted changes that cannot be undone.
  It is the mildest of the 16, seen once. Held: cover BOX-07 (target present) 0/2.

---

## Corrections to report.md

This review changes the following statements in [report.md](report.md). The report carries pointers to this section,
and the counts of 16 bugs and one policy bug stand.

| Where in report.md | What it says | Corrected |
|---|---|---|
| §7.4, §9 | the containment family includes "label via the parent issue" and "initiative via its project" | both are dropped conditions (#7, #8): Qwen never looked at the parent's label or the document's initiative. Containment has two members, #5 and #6 |
| §7.8 | 179 distinct test cases | 179 case IDs but 168 distinct inputs. Eight sweep cases repeat a contrast case exactly; three Calendar variants isolate nothing (ALT-CAL-02-A-I11 and -I12 equal CAL-02-A-TOLD, ALT-CAL-04-A-I11 equals CAL-04-A-TOLD) |
| §7.8 | 44 failing runs in 25 distinct cases | 25 case IDs, 21 distinct inputs |
| §7.8, §10 | four bugs recurred across cases, or "failed in two or more independent designs": relation direction, event creator, folder creator, hub inclusion | three. Hub inclusion's failures are 3 of 5 trials of one input |
| §7.6, Appendix D | Box folder listings show the creator and last modifier but not the owner | listings return only names and ids, so every person condition needs a per-item fetch. Fixed in place |
| §7.8 table | #13 is filed under `D:all_day` | by construction the violated fact is the event date (`A:Event.start`); the reason Qwen gave points to the all-day end date. The count is unchanged |
| §7.8 | #14 and #15 are two bugs | two requirements, but one run and one cause. The total is 15 if they are merged |

Corrections to the evidence that facts *held* (43 of 59 becoming 38 of 54) were made separately, in the OpenClaw
study's `corrections.md`, which is not part of this branch.

---

## Sources

- Counts per bug and test type are recomputed from [pilot/results.json](pilot/results.json), with the manual labels in
  [pilot/manual_labels.json](pilot/manual_labels.json) applied, and from the case files in [pilot/cases/](pilot/cases/).
- `python3 -m grounding.runs.fact_coverage_01.pilot.report_data` prints every failing run's path.
- The OpenClaw study's `corrections.md` (not part of this branch) lists runs that tested nothing, such as the #10 trial
  noted above. None of the failures listed here is affected.
