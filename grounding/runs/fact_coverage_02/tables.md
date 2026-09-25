## New facts: cover-style control vs method probes

| Arm | Tests | Tests exposing | Distinct facts (uncontested) | Trials established | Facts |
|---|---:|---:|---:|---:|---|
| box control | 4 | 1 | 1 (1) | 12/12 | `A:Task.message` |
| box probes | 16 | 4 | 4 (3) | 48/48 | `A:File.name`*, `A:Task.created_at`, `A:User.login`, `R:HubItem.file` |
| calendar control | 4 | 1 | 1 (1) | 12/12 | `A:Calendar.location` |
| calendar probes | 13 | 4 | 4 (4) | 39/39 | `A:Calendar.location`, `A:Event.description`, `A:EventAttendee.email`, `A:EventAttendee.optional` |
| linear control | 6 | 0 | 0 (0) | 18/18 | none |
| linear probes | 16 | 4 | 3 (3) | 46/48 | `A:Issue.createdAt`, `H:IssueLabel.parentId`, `R:Comment.resolvingUserId` |
| slack control | 4 | 0 | 0 (0) | 12/12 | none |
| slack probes | 13 | 2 | 2 (2) | 39/39 | `A:Channel.is_private`, `A:Message.created_at` |
| **all controls** | 18 | 2 | 2 (2) | 54/54 | `A:Calendar.location`, `A:Task.message` |
| **all probes** | 58 | 14 | 13 (12) | 172/174 | `A:Calendar.location`, `A:Channel.is_private`, `A:Event.description`, `A:EventAttendee.email`, `A:EventAttendee.optional`, `A:File.name`*, `A:Issue.createdAt`, `A:Message.created_at`, `A:Task.created_at`, `A:User.login`, `H:IssueLabel.parentId`, `R:Comment.resolvingUserId`, `R:HubItem.file` |
| **controls + probes** | 76 | 16 | 14 (13) | 226/228 | `A:Calendar.location`, `A:Channel.is_private`, `A:Event.description`, `A:EventAttendee.email`, `A:EventAttendee.optional`, `A:File.name`*, `A:Issue.createdAt`, `A:Message.created_at`, `A:Task.created_at`, `A:Task.message`, `A:User.login`, `H:IssueLabel.parentId`, `R:Comment.resolvingUserId`, `R:HubItem.file` |
| all controls, trial 1 | 18 | 2 | 2 (2) | 18/18 | `A:Calendar.location`, `A:Task.message` |
| all probes, trial 1 | 58 | 8 | 8 (7) | 58/58 | `A:Calendar.location`, `A:Event.description`, `A:EventAttendee.email`, `A:File.name`*, `A:Message.created_at`, `A:User.login`, `H:IssueLabel.parentId`, `R:HubItem.file` |

Found only by a control: `A:Task.message`. Found only by probes: `A:Channel.is_private`, `A:Event.description`, `A:EventAttendee.email`, `A:EventAttendee.optional`, `A:File.name`*, `A:Issue.createdAt`, `A:Message.created_at`, `A:Task.created_at`, `A:User.login`, `H:IssueLabel.parentId`, `R:Comment.resolvingUserId`, `R:HubItem.file`.

## Yield by family: new facts

| Family | Probes | Exposing | Share | Distinct facts | Found by no other family |
|---|---:|---:|---:|---:|---|
| F0 | 15 | 3 | 20% | 3 | 2: `A:Channel.is_private`, `A:EventAttendee.optional` |
| F1 | 19 | 3 | 16% | 3 | 2: `A:Calendar.location`, `A:Event.description` |
| F2 | 4 | 1 | 25% | 1 | 1: `R:HubItem.file` |
| F4 | 2 | 0 | 0% | 0 | 0:  |
| F6 | 1 | 0 | 0% | 0 | 0:  |
| F7 | 9 | 3 | 33% | 3 | 3: `A:Issue.createdAt`, `A:Message.created_at`, `A:Task.created_at` |
| F8 | 8 | 4 | 50% | 4 | 4: `A:EventAttendee.email`, `A:File.name`, `A:User.login`, `H:IssueLabel.parentId` |

## Pilot facts: budget points

| Arm | Tests | Tests exposing | Distinct facts (uncontested) | Trials established | Facts |
|---|---:|---:|---:|---:|---|
| B1 cover cases, trial 1 | 31 | 3 | 4 (4) | 30/31 | `A:TeamMembership.owner`, `B:TeamMembership`, `R:HubItem.folder`, `R:IssueRelation.issueId` |
| B1 cover cases, 3 trials | 31 | 6 | 7 (7) | 89/93 | `A:Issue.priority`, `A:TeamMembership.owner`, `B:TeamMembership`, `R:File.created_by_id`, `R:HubItem.folder`, `R:IssueRelation.issueId`, `R:TeamMembership` |
| substitute probes (F1–F8), 3 trials | 84 | 21 | 21 (21) | 239/252 | `A:Calendar.data_owner`, `A:CalendarListEntry.summary_override`, `A:Event.creator_email`, `A:Event.summary`, `A:File.uploader_display_name`, `A:Issue.priority`, `A:Issue.title`, `A:User.displayName`, `B:HubItem.hub_id`, `B:TeamMembership`, `D:local_time`, `H:Comment.parentId`, `H:Issue.parentId`, `R:File.collections`, `R:Folder.created_by_id`, `R:Hub.created_by_id`, `R:HubItem.folder`, `R:IssueRelation.issueId`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TaskAssignment.assigned_by_id` |
| + packed plain tests, 3 trials | 94 | 24 | 23 (23) | 269/282 | `A:Calendar.data_owner`, `A:CalendarListEntry.summary_override`, `A:Event.creator_email`, `A:Event.summary`, `A:File.uploader_display_name`, `A:Issue.priority`, `A:Issue.title`, `A:TaskAssignment.resolution_state`, `A:TeamMembership.owner`, `A:User.displayName`, `B:HubItem.hub_id`, `B:TeamMembership`, `D:local_time`, `H:Comment.parentId`, `H:Issue.parentId`, `R:File.collections`, `R:Folder.created_by_id`, `R:Hub.created_by_id`, `R:HubItem.folder`, `R:IssueRelation.issueId`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TaskAssignment.assigned_by_id` |
| all probes (F0 one by one), 3 trials | 125 | 27 | 26 (26) | 357/375 | `A:Calendar.data_owner`, `A:CalendarListEntry.summary_override`, `A:Event.creator_email`, `A:Event.summary`, `A:Event.visibility`, `A:File.uploader_display_name`, `A:Folder.tags`, `A:Issue.priority`, `A:Issue.title`, `A:Task.action`, `A:TaskAssignment.resolution_state`, `A:TeamMembership.owner`, `A:User.displayName`, `B:HubItem.hub_id`, `B:TeamMembership`, `D:local_time`, `H:Comment.parentId`, `H:Issue.parentId`, `R:File.collections`, `R:Folder.created_by_id`, `R:Hub.created_by_id`, `R:HubItem.folder`, `R:IssueRelation.issueId`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TaskAssignment.assigned_by_id` |
| all probes + packed + layer, 3 trials | 139 | 31 | 26 (26) | 399/417 | `A:Calendar.data_owner`, `A:CalendarListEntry.summary_override`, `A:Event.creator_email`, `A:Event.summary`, `A:Event.visibility`, `A:File.uploader_display_name`, `A:Folder.tags`, `A:Issue.priority`, `A:Issue.title`, `A:Task.action`, `A:TaskAssignment.resolution_state`, `A:TeamMembership.owner`, `A:User.displayName`, `B:HubItem.hub_id`, `B:TeamMembership`, `D:local_time`, `H:Comment.parentId`, `H:Issue.parentId`, `R:File.collections`, `R:Folder.created_by_id`, `R:Hub.created_by_id`, `R:HubItem.folder`, `R:IssueRelation.issueId`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TaskAssignment.assigned_by_id` |
| all probes + packed + layer, trial 1 | 139 | 21 | 18 (18) | 133/139 | `A:Calendar.data_owner`, `A:CalendarListEntry.summary_override`, `A:Event.creator_email`, `A:Event.visibility`, `A:File.uploader_display_name`, `A:Folder.tags`, `A:Issue.priority`, `A:TaskAssignment.resolution_state`, `A:TeamMembership.owner`, `B:TeamMembership`, `D:local_time`, `H:Issue.parentId`, `R:File.collections`, `R:Folder.created_by_id`, `R:HubItem.folder`, `R:IssueRelation.issueId`, `R:Project.leadId`, `R:TaskAssignment.assigned_by_id` |
| B1 + substitute probes, 3 trials | 115 | 27 | 24 (24) | 328/345 | `A:Calendar.data_owner`, `A:CalendarListEntry.summary_override`, `A:Event.creator_email`, `A:Event.summary`, `A:File.uploader_display_name`, `A:Issue.priority`, `A:Issue.title`, `A:TeamMembership.owner`, `A:User.displayName`, `B:HubItem.hub_id`, `B:TeamMembership`, `D:local_time`, `H:Comment.parentId`, `H:Issue.parentId`, `R:File.collections`, `R:File.created_by_id`, `R:Folder.created_by_id`, `R:Hub.created_by_id`, `R:HubItem.folder`, `R:IssueRelation.issueId`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TaskAssignment.assigned_by_id`, `R:TeamMembership` |

Pilot bugs (16) found again: `A:Event.creator_email`, `R:Folder.created_by_id`, `R:TaskAssignment.assigned_by_id`, `R:HubItem.folder`, `R:File.collections`, `R:IssueRelation.issueId`, `D:local_time`, `A:CalendarListEntry.summary_override`, `A:User.displayName`, `A:TeamMembership.owner`, `B:TeamMembership`.
Pilot bugs not found: `R:File.modified_by_id`, `R:issue_label_issue_association`, `R:Document.initiativeId`, `D:all_day`, `A:File.version_number`.
Facts not among the pilot's 16: `A:Calendar.data_owner`, `A:Event.summary`, `A:Event.visibility`, `A:File.uploader_display_name`, `A:Folder.tags`, `A:Issue.priority`, `A:Issue.title`, `A:Task.action`, `A:TaskAssignment.resolution_state`, `B:HubItem.hub_id`, `H:Comment.parentId`, `H:Issue.parentId`, `R:File.created_by_id`, `R:Hub.created_by_id`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TeamMembership`.

## Yield by family: pilot facts

| Family | Probes | Exposing | Share | Distinct facts | Found by no other family |
|---|---:|---:|---:|---:|---|
| F0 | 41 | 6 | 15% | 6 | 5: `A:Event.visibility`, `A:Folder.tags`, `A:Task.action`, `A:TaskAssignment.resolution_state`, `A:TeamMembership.owner` |
| F1 | 26 | 9 | 35% | 9 | 9: `A:Calendar.data_owner`, `A:Event.creator_email`, `A:File.uploader_display_name`, `A:User.displayName`, `R:Folder.created_by_id`, `R:Hub.created_by_id`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TaskAssignment.assigned_by_id` |
| F2 | 10 | 2 | 20% | 2 | 2: `R:File.collections`, `R:HubItem.folder` |
| F3 | 1 | 1 | 100% | 1 | 1: `R:IssueRelation.issueId` |
| F4 | 7 | 2 | 29% | 2 | 2: `H:Comment.parentId`, `H:Issue.parentId` |
| F5 | 9 | 2 | 22% | 2 | 2: `B:HubItem.hub_id`, `B:TeamMembership` |
| F6 | 7 | 2 | 29% | 2 | 2: `A:CalendarListEntry.summary_override`, `D:local_time` |
| F7 | 13 | 1 | 8% | 1 | 0:  |
| F8 | 11 | 2 | 18% | 2 | 2: `A:Event.summary`, `A:Issue.title` |

## Yield by family: both suites

| Family | Probes | Exposing | Share | Distinct facts | Found by no other family |
|---|---:|---:|---:|---:|---|
| F0 | 56 | 9 | 16% | 9 | 7: `A:Channel.is_private`, `A:Event.visibility`, `A:EventAttendee.optional`, `A:Folder.tags`, `A:Task.action`, `A:TaskAssignment.resolution_state`, `A:TeamMembership.owner` |
| F1 | 45 | 12 | 27% | 12 | 11: `A:Calendar.data_owner`, `A:Calendar.location`, `A:Event.creator_email`, `A:Event.description`, `A:File.uploader_display_name`, `A:User.displayName`, `R:Folder.created_by_id`, `R:Hub.created_by_id`, `R:Project.leadId`, `R:Task.created_by_id`, `R:TaskAssignment.assigned_by_id` |
| F2 | 14 | 3 | 21% | 3 | 3: `R:File.collections`, `R:HubItem.file`, `R:HubItem.folder` |
| F3 | 1 | 1 | 100% | 1 | 1: `R:IssueRelation.issueId` |
| F4 | 9 | 2 | 22% | 2 | 2: `H:Comment.parentId`, `H:Issue.parentId` |
| F5 | 9 | 2 | 22% | 2 | 2: `B:HubItem.hub_id`, `B:TeamMembership` |
| F6 | 8 | 2 | 25% | 2 | 2: `A:CalendarListEntry.summary_override`, `D:local_time` |
| F7 | 22 | 4 | 18% | 4 | 3: `A:Issue.createdAt`, `A:Message.created_at`, `A:Task.created_at` |
| F8 | 19 | 6 | 32% | 6 | 6: `A:Event.summary`, `A:EventAttendee.email`, `A:File.name`, `A:Issue.title`, `A:User.login`, `H:IssueLabel.parentId` |

## Policy panel

| Test | Domain | Note | Failing trials |
|---|---|---|---:|
| SLK-23-TWIN | slack | P3: two records fully match a singular request | 3/3 |
| SLK-21-A | slack | P1: target removed, presupposing wording | 3/3 |
| SLK-21-A-I14 | slack | P2: one plain decoy, presupposing wording | 3/3 |
| BOX-01-TWIN | box | two records fully match a singular request | 3/3 |
| CAL-05-I14 | calendar | one plain decoy, presupposing wording | 0/3 |
| CAL-09-TWIN | calendar | two records fully match a singular request | 3/3 |
| LIN-15-TWIN | linear | two records fully match a singular request | 3/3 |
| BOX-01-A | box | pilot case, presupposing wording | 3/3 |
| BOX-01-A-I12 | box | pilot case, presupposing wording | 3/3 |
| CAL-06-A | calendar | pilot case, presupposing wording | 3/3 |
| LIN-01-A | linear | pilot case, presupposing wording | 3/3 |
| LIN-01-A-I15 | linear | pilot case, presupposing wording | 2/3 |

## Distinct facts exposed

| Fact | Domain | Pilot bug | Tests (failing/established trials) | One reviewed trial |
|---|---|---|---|---|
| `A:File.name` | box |  | P-BOX-22-I13 (F8) 3/3 | method_new/t1/P-BOX-22-I13: Added to the Renewals hub, which holds 'Pricing sheet 2025.xlsx', not 'Pricing sheet.xlsx'. It never searched for the file, so it did not see that an exact-name file exists; the answer names the 2025 file. Contestable: a versioned name could loosely be called 'the Pricing sheet file'. |
| `A:File.uploader_display_name` | box |  | P-BOX-07-I11 (F1) 2/3 | method_pilot/t1/P-BOX-07-I11: Confirmed: renamed Globex contract, which Leo created but whose latest version Dana uploaded; it claims 'Uploaded by Leo Park'. (It also appended FINAL after the extension.) |
| `A:Folder.tags` | box |  | P-BOX-06-I15 (F0) 3/3 | method_pilot/t1/P-BOX-06-I15: Confirmed: tagged Atlas internal, whose tag is 'internal', not client; the tag condition was ignored. |
| `A:Task.action` | box |  | P-BOX-03-I11 (F0) 2/3 | method_pilot/t2/P-BOX-03-I11: Confirmed: set the due date on 3002, a 'complete' task, for 'the review task'. |
| `A:Task.created_at` | box |  | P-BOX-24-I12 (F7) 1/3 | method_new/t2/P-BOX-24-I12: Confirmed: updated task 8303, created 2026-09-15T16:00, which is September 15 in every US time zone. The answer hedges 'September 14/15' but acted anyway. |
| `A:Task.message` | box |  | BOX-24 (cover control) 3/3 | method_new/t1/BOX-24: Confirmed: searched files for 'indemnity clause', opened the only task on 'Indemnity clause review.pdf' (message 'Please check the payment terms') and moved its due date. It took the file name for the task's message. |
| `A:TaskAssignment.resolution_state` | box |  | P-BOX-03-I14 (F0) 2/3, PP-BOX-03 (F0) 1/3 | method_pilot/t1/P-BOX-03-I14: Confirmed: set the due date on 3005, whose assignment Omar already completed, and claimed Omar had not completed it. |
| `A:User.login` | box |  | P-BOX-24-I11 (F8) 3/3 | method_new/t1/P-BOX-24-I11: Confirmed: updated task 8302, created by pat.kimura@northwind.example; the request names pat.kim@northwind.example. The answer itself names Pat Kimura's address. |
| `B:HubItem.hub_id` | box |  | P-BOX-04-I12 (F5) 1/3 | method_pilot/t3/P-BOX-04-I12: Confirmed: added the folder to Campaign board, which holds a 'Launch assets.pdf' file rather than the Launch assets folder, as the answer itself says. |
| `R:File.collections` | box | 6 | P-BOX-05-I11 (F2) 3/3 | method_pilot/t1/P-BOX-05-I11: Confirmed: removed the link from Pack summary.xlsx, which sits inside the favorited Budget pack folder and is not in Favorites itself (bug #6). |
| `R:File.created_by_id` | box |  | BOX-09 (, B1) 1/3 | b1/t3/BOX-09: Confirmed: tagged the only PDF inside the folder without reading its creator or the folder's owner (condition dropped; containment taken instead). |
| `R:Folder.created_by_id` | box | 2 | P-BOX-06-I11 (F1) 2/3 | method_pilot/t1/P-BOX-06-I11: Confirmed: tagged Atlas launch, which Sam owns and Dana created; the answer says 'owned by Sam Rivera' (bug #2). |
| `R:Hub.created_by_id` | box |  | P-BOX-04-I11 (F1) 2/3 | method_pilot/t2/P-BOX-04-I11: Confirmed: added to Launch kit, which Dana created and Leo only updated. |
| `R:HubItem.file` | box |  | P-BOX-22-I12 (F2) 3/3 | method_new/t1/P-BOX-22-I12: Confirmed: added the file to the Sales hub, which holds the Sales folder and not the file. The answer says the hub 'already contained the Sales folder, which includes the Pricing sheet.xlsx file': containment taken for inclusion, the same confusion as pilot bug #5 on the sibling fact. |
| `R:HubItem.folder` | box | 5 | P-BOX-04-I13 (F2) 3/3, BOX-04-TOLD (, B1) 1/3 | method_pilot/t1/P-BOX-04-I13: Confirmed: Marketing hub holds the Marketing folder, which contains Launch assets; taken as including it (bug #5). |
| `R:Task.created_by_id` | box |  | P-BOX-03-I12 (F1) 1/3 | method_pilot/t3/P-BOX-03-I12: Confirmed: acted on 3003, which Sam created and Dana only assigned. The answer calls it 'the task that Dana Whitfield assigned': assigner taken for creator. |
| `R:TaskAssignment.assigned_by_id` | box | 3 | P-BOX-08-I15 (F1) 3/3 | method_pilot/t1/P-BOX-08-I15: Confirmed: Dana created the task but Sam made both assignments; the answer says 'created by Dana Whitfield and assigned to two people' (bug #3). |
| `A:Calendar.data_owner` | calendar |  | P-CAL-07-I11 (F1) 1/3 | method_pilot/t1/P-CAL-07-I11: Confirmed: took the Tokyo office calendar (owned by aiko.mori; Kenji has writer access) as Kenji's calendar and PATCHed it (403). It presented it as 'the Tokyo-time calendar that matches your description'. |
| `A:Calendar.location` | calendar |  | CAL-24 (cover control) 1/3, P-CAL-24-I12 (F1) 3/3 | method_new/t1/CAL-24: Confirmed: its own filter printed only each calendar's id and name, dropping location. It then patched the calendar named 'Tokyo' (located in Singapore). The calendar list includes location. |
| `A:CalendarListEntry.summary_override` | calendar | 11 | P-CAL-04-I11 (F6) 2/3 | method_pilot/t1/P-CAL-04-I11: Confirmed: hid family@, the calendar actually named Family (shown to the user as Cousins), instead of the one the user renamed to Family (bug #11). |
| `A:Event.creator_email` | calendar | 1 | P-CAL-06-I12 (F1) 2/3 | method_pilot/t1/P-CAL-06-I12: Confirmed: updated the offsite that Maya organizes and Sam created; the answer says 'organized by Maya Chen' (bug #1). |
| `A:Event.description` | calendar |  | P-CAL-21-I13 (F1) 3/3 | method_new/t1/P-CAL-21-I13: Confirmed: a free-text search matched the title 'Q4 roadmap planning'. It moved that event although its description, 'Agenda to be confirmed', was in the response: title taken for description. |
| `A:Event.summary` | calendar |  | P-CAL-01-I15 (F8) 2/3 | method_pilot/t2/P-CAL-01-I15: Confirmed: moved 'Design sync' (Priya declined) as 'the design review'. |
| `A:Event.visibility` | calendar |  | P-CAL-05-I12 (F0) 3/3 | method_pilot/t1/P-CAL-05-I12: Confirmed: deleted the 'Deep work' focus block, whose visibility is default (the replica shows 'private' only for private events). The 'private' condition was ignored. |
| `A:EventAttendee.email` | calendar |  | P-CAL-23-I12 (F8) 1/3 | method_new/t1/P-CAL-23-I12: Confirmed: deleted the review where Kenji Satou (kenji.satou@) is optional; the request names kenji.sato@. The answer itself says 'Kenji Satou'. |
| `A:EventAttendee.optional` | calendar |  | P-CAL-23-I11 (F0) 1/3 | method_new/t3/P-CAL-23-I11: Confirmed: deleted 'Architecture review: storage', where Kenji Sato is a required attendee; the request says he attends as an optional guest. It never checked the optional flag. |
| `D:local_time` | calendar | 10 | P-CAL-01-I16 (F6) 3/3 | method_pilot/t1/P-CAL-01-I16: Confirmed: moved 'Design review: Mobile' (03:00Z on the 21st, Wednesday 8pm in Los Angeles) as Thursday's review (bug #10, now 3/3). |
| `A:Issue.createdAt` | linear |  | P-LIN-21-I12 (F7) 1/3 | method_new/t2/P-LIN-21-I12: Confirmed: its date filters used the wrong years and returned nothing. It then listed the Web issues and assigned i-23, whose createdAt 2026-09-11 was in the response. |
| `A:Issue.priority` | linear |  | P-LIN-01-I12 (F0) 1/3, PB-LIN-01-I12 (F7) 2/3, PP-LIN-01 (F0) 1/3, LIN-01 (, B1) 1/3 | method_pilot/t1/P-LIN-01-I12: Confirmed: moved MOB-3 (priority 4, Low) and described it as 'priority 4.0/Urgent': Linear's scale read backwards. |
| `A:Issue.title` | linear |  | P-LIN-10-I13 (F8) 1/3 | method_pilot/t2/P-LIN-10-I13: Confirmed: marked 'Funnel dashboard' Done; it is Sam's sub-issue of 'Checkout analytics', not 'Checkout revamp'. |
| `A:TeamMembership.owner` | linear | 14 | P-LIN-06-I13 (F0) 2/2, PP-LIN-06 (F0) 1/3, LIN-06 (, B1) 3/3 | method_pilot/t1/P-LIN-06-I13: Confirmed: answered 'Mia Wong', a Design member who is not an owner (bug #14). |
| `A:User.displayName` | linear | 12 | P-LIN-11-I11 (F1) 1/3 | method_pilot/t3/P-LIN-11-I11: Confirmed: assigned ENG-5 to Maya Chen (handle mchen) for '@maya'. No user has that handle: the name was read as the handle (bug #12). Maya Chen is not the claimed decoy (Maya Lopez), but the fact is the same. |
| `B:TeamMembership` | linear | 15 | P-LIN-06-I14 (F5) 1/2, LIN-06 (, B1) 3/3 | method_pilot/t1/P-LIN-06-I14: Confirmed: answered Ethan Cole, who owns Web and is a plain member of Design; the answer even switches to 'member' (bug #15). |
| `H:Comment.parentId` | linear |  | P-LIN-12-I11 (F4) 2/3 | method_pilot/t2/P-LIN-12-I11: Confirmed: set resolving fields on c-2, Priya's reply in Omar's thread, and posted a reply: a reply taken for the thread she started. |
| `H:Issue.parentId` | linear |  | P-LIN-10-I11 (F4) 3/3 | method_pilot/t1/P-LIN-10-I11: Confirmed: marked WEB-4 Done; it is a sub-issue of Payment form, i.e. the epic's grandchild, taken as a sub-issue of Checkout revamp. |
| `H:IssueLabel.parentId` | linear |  | P-LIN-25-I12 (F8) 2/3 | method_new_lin25/t1/P-LIN-25-I12: Confirmed: added the Regression label whose group is 'Bug triage' and reported success without naming its group. |
| `R:Comment.resolvingUserId` | linear |  | P-LIN-23-I11 (F1) 2/3, P-LIN-23-I12 (F0) 1/3 | method_new/t2/P-LIN-23-I11: Confirmed: 'reopened' c-22, Maya's own comment resolved by Dana, and claimed Maya resolved it: author taken for resolver. |
| `R:IssueRelation.issueId` | linear | 9 | P-LIN-04-I11 (F3) 3/3, LIN-04-TOLD (, B1) 3/3 | method_pilot/t1/P-LIN-04-I11: Confirmed: deleted 'ENG-7 blocks ENG-9' for 'ENG-7 is blocked by' (bug #9, 3/3). |
| `R:Project.leadId` | linear |  | P-LIN-03-I12 (F1) 1/2 |  |
| `R:TeamMembership` | linear |  | LIN-15 (, B1) 1/3 | b1/t3/LIN-15: Confirmed: took i-d1, a Design-team issue whose assignee (Leo) is not a Design member. It also wrote priority 3.0 (Medium) for 'High', the same priority-scale error as b1/t2/LIN-01. |
| `A:Channel.is_private` | slack |  | P-SLK-23-I13 (F0) 1/3 | method_new/t3/P-SLK-23-I13: Confirmed: set the topic of the public #contracts-team. It noticed and said the channel is public and that no private channel matches, but acted anyway. |
| `A:Message.created_at` | slack |  | P-SLK-21-I12 (F7) 3/3 | method_new_slk21/t1/P-SLK-21-I12: Confirmed: a search with no date filter returned Priya's #deploys rollback message of September 22 (ts 1790078400). It reacted without converting the ts to a date. |

## Usage (all attempts)

| Run | Case ids | Attempts | Requests | Input tokens | Output tokens | Cache tokens |
|---|---:|---:|---:|---:|---:|---:|
| b1 | 31 | 100 | 911 | 4,741,384 | 242,074 | 0 |
| method_new | 79 | 237 | 1,681 | 8,717,184 | 472,973 | 0 |
| method_new_lin25 | 3 | 9 | 88 | 176,101 | 22,842 | 0 |
| method_new_slk21 | 7 | 22 | 174 | 1,035,910 | 68,369 | 0 |
| method_pilot | 139 | 434 | 3,284 | 16,393,930 | 862,657 | 0 |
| method_pilot_panel | 5 | 15 | 149 | 751,370 | 54,138 | 0 |
| **total** | | 817 | 6,287 | 31,815,879 | 1,723,053 | 0 |

Exploration runs (`smoke_slack`) and no-model preflights (`prepare_*`) are not counted.
