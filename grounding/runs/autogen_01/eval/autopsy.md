# Arm R autopsy: decoys and wording, exemplar vs generated

## BOX-21 vs AR-BOX-21

**`A:Folder.created_at`**: exemplar exposed: no
- exemplar decoy (F7), probe failed 0/3: Created on September 1, the day after August.
- exemplar decoy (F0), probe failed 0/3: Created in March.
- generated decoy (F1), probe failed 0/3: It was created on May 20, but Priya last modified it on June 3 -- the modified date lands on June 3, not the created date.
- generated decoy (F7), probe failed 0/3: Created June 2, the day before the requested date; everything else about it matches.

**`D:Folder.item_count`**: exemplar exposed: no
- exemplar decoy (F7), probe failed 0/3: Holds three files, one more than asked.
- generated decoy (F6), probe failed 0/3: It has 0 files directly in it (only a subfolder, Vendor Filings 2023); that subfolder holds the 3 files, not the folder itself.

**`R:Folder.collections`**: exemplar exposed: no
- exemplar decoy (F2), probe failed 0/3: Audit prep is inside Compliance, which is in Favorites; the folder itself is not.
- generated decoy (F2), probe failed 0/3: The folder itself is in no collection, but a file directly inside it, Insurance A.pdf, is in the Legal Hold collection.
- generated decoy (F0), probe failed 0/3: It isn't in any collection at all, unlike the folder in Legal Hold.

**`R:Folder.modified_by_id`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Leo created Audit notes; Maya modified it last.
- generated decoy (F1), probe failed 0/3: Priya Nair owns this folder, but Dana Whitfield modified it last.
- generated decoy (F1), probe failed 0/3: Priya Nair created this folder, but Sam Rivera modified it last.

## BOX-22 vs AR-BOX-22

**`A:File.name`**: exemplar exposed: yes
- exemplar decoy (F8), probe failed 3/3: Renewals includes Pricing sheet 2025.xlsx.
- generated decoy (F8), probe failed 0/3: 'Vendor Agreement Draft.pdf' is also a file item of the Client Docs hub that Dana Whitfield last updated, but it is not named 'Vendor Agreement.pdf'.

**`R:Hub.updated_by_id`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Dana created Deal desk; Leo updated it last.
- generated decoy (F1), probe failed 0/3: This file named 'Vendor Agreement.pdf' sits in a second hub also titled Client Docs, which Dana Whitfield created but Sam Rivera updated last.

**`R:HubItem.file`**: exemplar exposed: yes
- exemplar decoy (F2), probe failed 3/3: Sales hub includes the Sales folder, which contains Pricing sheet.xlsx; not the file itself.
- generated decoy (F2), probe failed 2/3 (exposed after adjudication): This file named 'Vendor Agreement.pdf' sits in a folder called Client Docs that Dana Whitfield last modified, but it was never added as an item of the Client Docs hub.

## BOX-23 vs AR-BOX-23

**`A:File.description`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: The name says Initech renewal; the description does not.
- generated decoy (F1), probe failed 0/3: Tagged mobile-redesign, but its description talks about Q4 roadmap priorities, not the mobile redesign.

**`A:File.extension`**: exemplar exposed: no
- exemplar decoy (F0), probe failed 0/3: A Word document, not a PDF.
- generated decoy (F0), probe failed 0/3: Same folder, description text and 3 comments, but it's a spreadsheet (.xlsx), not a PDF.

**`A:File.size`**: exemplar exposed: no
- exemplar decoy (F7), probe failed 0/3: 1.95 MB, just under 2 MB.
- generated decoy (F7), probe failed 0/3: Same folder, description and comment count, but at 2.1 MB it is just over the 2 MB limit.

**`D:File.comment_count`**: exemplar exposed: no
- exemplar decoy (F7), probe failed 0/3: Two comments, one short of three.
- generated decoy (F6), probe failed 0/3: It has 3 comments in total, but one of them is a reply to another, so only 2 are top-level comments.

## BOX-24 vs AR-BOX-24

**`A:Task.created_at`**: exemplar exposed: yes
- exemplar decoy (F7), probe failed 1/3: Created on September 15, the next day.
- generated decoy (F7), probe failed 2/3 (exposed after adjudication): Created June 4, the day after the requested date.
- generated decoy (F6), probe failed 2/3 (exposed after adjudication): It was created on May 20; its due date, not its created date, falls on June 3.

**`A:Task.message`**: exemplar exposed: yes
- exemplar decoy (F1), probe failed 0/3: The file is the indemnity clause review; the task asks about payment terms.
- exemplar decoy (F0), probe failed 0/3: Asks to approve the invoice.
- generated decoy (F2), probe failed 0/3: The task itself just says 'review the updated draft'; it's a comment on Vendor Agreement.pdf that mentions redoing the pricing table.
- generated decoy (F0), probe failed 0/3: Asks to add a missing signature page, not to redo the pricing table.

**`A:User.login`**: exemplar exposed: yes
- exemplar decoy (F8), probe failed 3/3: Created by pat.kimura@, not pat.kim@.
- generated decoy (F8), probe failed 0/3: Dana White, not Dana Whitfield, created it; dana.white@northwind.example shares 'dana.whit' with the requested login.
- generated decoy (F0), probe failed 0/3: Leo Park created it, not the person at dana.whitfield@northwind.example.

## CAL-21 vs AR-CAL-21

**`A:Event.description`**: exemplar exposed: yes
- exemplar decoy (F1), probe failed 3/3: The title mentions the Q4 roadmap; the description does not.
- exemplar decoy (F0), probe failed 0/3: About the hiring plan.
- generated decoy (F1), probe failed 1/3 (exposed after adjudication): Its description is about the hiring pipeline; "Meridian contract" is only in the location field, not the description.
- generated decoy (F0), probe failed 0/3: Its description is about an onboarding checklist, unrelated to the Meridian contract.

**`A:Event.end`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Starts at 5pm on Thursday; it ends at 6pm.
- exemplar decoy (F7), probe failed 0/3: Ends at 5:30pm, the nearest wrong end time.
- generated decoy (F7), probe failed 0/3: It is about the Meridian contract, but it ends at 3:00 pm, half an hour before the requested time.
- generated decoy (F1), probe failed 0/3: It is about the Meridian contract, but 3:30 pm is when it starts, not when it ends; it ends at 4:00 pm.

## CAL-22 vs AR-CAL-22

**`A:Calendar.description`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Named London office; its description says Paris.
- exemplar decoy (F1), probe failed 0/3: Located in London; its description says Berlin.
- exemplar decoy (F0), probe failed 0/3: For the Madrid office.
- generated decoy (F1), probe failed 2/3 (exposed after adjudication): The EMEA calendar's location line mentions weekend on-call coverage; its own description talks about staffing schedules instead.
- generated decoy (F2), probe failed 0/3: The APAC calendar's own description covers daytime shift scheduling; it is a reminder event on that calendar whose description mentions weekend on-call coverage.
- generated decoy (F0), probe failed 0/3: Same name pattern and ownership, but its description tracks LATAM data-center maintenance windows, with no mention of weekend on-call coverage.

## CAL-23 vs AR-CAL-23

**`A:EventAttendee.email`**: exemplar exposed: yes
- exemplar decoy (F8), probe failed 1/3: The optional guest is kenji.satou@, not kenji.sato@.
- generated decoy (F1), probe failed 0/3: Dana Whitfield organizes this vendor sync but is not on the attendee list; Kenji Sato is the optional attendee.
- generated decoy (F8), probe failed 0/3: The optional attendee is Dana White, not Dana Whitfield.

**`A:EventAttendee.optional`**: exemplar exposed: yes
- exemplar decoy (F0), probe failed 1/3: Kenji is a required attendee.
- generated decoy (F0), probe failed 0/3: Dana Whitfield attends, but as a required attendee, not optional.

## CAL-24 vs AR-CAL-24

**`A:Calendar.location`**: exemplar exposed: yes
- exemplar decoy (F1), probe failed 0/3: Its description says Tokyo; it is located in Osaka.
- exemplar decoy (F1), probe failed 3/3: Named Tokyo; located in Singapore.
- exemplar decoy (F6), probe failed 0/3: Uses Tokyo time; located in Seoul.
- exemplar decoy (F0), probe failed 0/3: Located in Sydney.
- generated decoy (F1), probe failed 0/3: Its own location is Building 2, 1st Floor; the description just mentions Building 4, 3rd Floor as the building being repainted.
- generated decoy (F2), probe failed 0/3: The calendar itself is at Building 7, Ground Floor; only its Quarterly Town Hall event is held at Building 4, 3rd Floor.
- generated decoy (F0), probe failed 0/3: It's the Front Desk calendar for Building 9, 2nd Floor, not Building 4.

## LIN-21 vs AR-LIN-21

**`A:Issue.createdAt`**: exemplar exposed: yes
- exemplar decoy (F7), probe failed 1/3: Created on September 11, the next day.
- generated decoy (F7), probe failed 0/3: Maya Chen created it, but on June 4th, the day after.
- generated decoy (F1), probe failed 0/3: It was created on May 20th; June 3rd is only its due date.

**`R:Issue.creatorId`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Omar is the assignee; Dana created it.
- generated decoy (F1), probe failed 1/3 (exposed after adjudication): Leo Park created it; Maya Chen is only its assignee.
- generated decoy (F2), probe failed 0/3: Priya Nair created it; Maya Chen only subscribes to it.

**`R:Issue.teamId`**: exemplar exposed: no
- exemplar decoy (F8), probe failed 0/3: In the Web Platform team, not Web.
- exemplar decoy (F0), probe failed 0/3: In the Mobile team.
- generated decoy (F2), probe failed 0/3: Its actual team is API; a workspace label named Web is attached to it, not the team.
- generated decoy (F2), probe failed 0/3: It belongs to Web Mobile, a sub-team of Web, not to Web itself.

## LIN-22 vs AR-LIN-22

**`R:Document.projectId`**: exemplar exposed: no
- exemplar decoy (F2), probe failed 0/3: Attached to the Commerce initiative, which contains the project; not to the project.
- exemplar decoy (F8), probe failed 0/3: In Checkout Redesign v2.
- exemplar decoy (F0), probe failed 0/3: In Payments Revamp.
- generated decoy (F1), probe failed 0/3: It belongs to the Platform Migration project; it is only linked to the Mobile Redesign initiative, not the Mobile Redesign project.
- generated decoy (F8), probe failed 0/3: Its project is Mobile App Redesign, not Mobile Redesign.

**`R:Document.updatedById`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Leo created Checkout rollout; Sam edited it last.
- generated decoy (F1), probe failed 0/3: Leo Park created it, but Maya Chen edited it last.
- generated decoy (F8), probe failed 0/3: It was last edited by Leo Parker, not Leo Park.

## LIN-23 vs AR-LIN-23

**`R:Comment.resolvingUserId`**: exemplar exposed: yes
- exemplar decoy (F1), probe failed 2/3: Maya started this thread; Dana resolved it.
- exemplar decoy (F0), probe failed 1/3: Resolved by Dana.
- generated decoy (F1), probe failed 3/3 (exposed after adjudication): Sam Rivera wrote this comment, but Priya Nair is the one who resolved the thread.

## LIN-24 vs AR-LIN-24

**`A:Cycle.number`**: exemplar exposed: no
- exemplar decoy (F7), probe failed 0/3: Cycle 16, the next one.
- generated decoy (F1), probe failed 3/3: This cycle is literally named "Cycle 4", but its number field is 11; the real fourth cycle (number 4) has been renamed "Sprint Nova".
- generated decoy (F0), probe failed 1/3 (exposed after adjudication): Same title, assignee and team, but it sits in Cycle 5, not Cycle 4.

## LIN-25 vs AR-LIN-25

**`H:IssueLabel.parentId`**: exemplar exposed: yes
- exemplar decoy (F4), probe failed 0/3: A top-level Regression label, in no group.
- exemplar decoy (F8), probe failed 2/3: The Regression label in the Bug triage group.
- generated decoy (F4), probe failed 0/3: The issue is tagged Enterprise, a specific tier nested under the Customer Tier group, not the bare Customer Tier label itself; team and assignee still match.

## LIN-26 vs AR-LIN-26

**`R:issue_subscriber_user_association`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/2: Dana is the assignee, not a subscriber.
- exemplar decoy (F1), probe failed 0/3: Dana created it; she is not subscribed.
- exemplar decoy (F0), probe failed 0/2: Only Sam is subscribed.
- generated decoy (F1), probe failed 0/3: Sam Rivera is the assignee of this issue, not a subscriber; he never subscribed to it.
- generated decoy (F1), probe failed 1/3: Sam Rivera created this issue but did not subscribe to it.
- generated decoy (F0), probe failed 0/3: Dana Whitfield is the subscriber on this issue, not Sam Rivera.

## SLK-21 vs AR-SLK-21

**`A:Message.created_at`**: exemplar exposed: yes
- exemplar decoy (F7), probe failed 3/3: Posted on September 22.
- generated decoy (F7), probe failed 0/3: Leo Park posted this in #incidents, but on Wednesday, the day after.

**`R:messages.channel_id`**: exemplar exposed: no
- exemplar decoy (F8), probe failed 0/3: Posted in #deploys-staging.
- exemplar decoy (F0), probe failed 0/3: Posted in #general.
- generated decoy (F2), probe failed 0/3: Leo Park posted this on Tuesday in #eng-standup, a channel he belongs to, not in #incidents.
- generated decoy (F2), probe failed 0/3: Leo Park posted this on Tuesday in #war-room; Diego Alvarez, who reacted to it, belongs to #incidents, but the message itself is not there.

**`R:messages.user_id`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Diego posted it; it mentions Priya.
- generated decoy (F1), probe failed 0/3: Diego Alvarez posted this message in #incidents on Tuesday; Leo Park only reacted to it with a thumbs-up.
- generated decoy (F2), probe failed 0/3: Omar Haddad posted this in #incidents on Tuesday; Leo Park is a member of #incidents but did not write it.

## SLK-23 vs AR-SLK-23

**`A:Conversation.is_private`**: exemplar exposed: yes
- exemplar decoy (F0), probe failed 1/3: A public channel with that purpose.
- generated decoy (F0), probe failed 1/3: new-hires has the right purpose and member, but it is a public channel, not a private one.
- generated decoy (F1), probe failed 0/3: onboarding-design-pod is a group DM Diego belongs to with the right purpose text, but its is_private flag is false; only is_gc is set.

**`A:Conversation.purpose_text`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Its topic, not its purpose, is about vendor contracts.
- exemplar decoy (F1), probe failed 0/3: Named vendor-contracts; its purpose is an archive of signed agreements.
- generated decoy (F1), probe failed 2/3 (exposed after adjudication): hr-general's topic mentions onboarding new hires, but its purpose is about general HR announcements; the request asks about the purpose.
- generated decoy (F0), probe failed 0/3: Same privacy and membership, but hr-benefits' purpose is about benefits enrollment, not onboarding.

## SLK-24 vs AR-SLK-24

**`R:channel_members`**: exemplar exposed: no
- exemplar decoy (F1), probe failed 0/3: Leo posted there but is not a member.
- exemplar decoy (F8), probe failed 0/3: The member is Leo Parker, not Leo Park.
- exemplar decoy (F0), probe failed 0/3: Priya and Omar are members; Leo is not.
- generated decoy (F1), probe failed 0/0: Diego once posted a message in #payments-oncall, but he isn't a current member of that channel; Aisha is.
- generated decoy (F2), probe failed 0/0: Leo reacted to a message inside #payments-oncall, but he isn't a member of that channel.
- generated decoy (F8), probe failed 0/0: Omar is a member of #payments-oncall-eu, not #payments-oncall.
- generated decoy (F0), probe failed 0/0: Maya has never posted, reacted, or held membership in #payments-oncall at all.

## Wording

| Scenario | Exemplar request | chars / conditions / field words | Generated request | chars / conditions / field words |
|---|---|---|---|---|
| BOX-21 | In my Favorites, add the tag audit-ready to the folder Leo Park last modified that was created in August 2026 and holds exactly two files. | 138 / 6 / 2 | Add the tag archive-ready to the folder that was created on June 3, 2026, that Priya Nair modified last, that's in the Legal Hold collection, and that has exactly 3 items directly in it. | 186 / 7 / 2 |
| BOX-22 | Add the Discount policy file to the hub Dana Whitfield last updated that already includes the Pricing sheet file. | 113 / 6 / 1 | In the Client Docs hub that Dana Whitfield last updated, add the tag 'renewed' to the file named 'Vendor Agreement.pdf'. | 120 / 7 / 2 |
| BOX-23 | Add the tag renewal to the contract PDF whose description mentions the Initech renewal, that is larger than 2 MB and has at least three comments. | 145 / 4 / 2 | Add the tag design-review to the PDF in the Product Specs folder whose description mentions the mobile redesign, is under 2 MB, and has exactly 3 comments on it, not counting replies. | 183 / 7 / 2 |
| BOX-24 | Move the due date to October 20, 2026 on the task pat.kim@northwind.example created on September 14 asking to check the indemnity clause. | 137 / 4 / 2 | On Vendor Agreement.pdf, push the due date to July 15 for the task dana.whitfield@northwind.example created on June 3 asking for the pricing table to be redone. | 160 / 7 / 2 |
| CAL-21 | Move the planning session that ends at 5pm on Thursday and whose description mentions the Q4 roadmap to Room 2B. | 112 / 3 / 2 | Move the client sync about finalizing the Meridian contract that ends at 3:30 pm to Room 4C. | 92 / 3 / 0 |
| CAL-22 | Give Sam Rivera (sam.rivera@northwind.example) read access to the calendar whose description says it is for the London office. | 126 / 1 / 2 | Change the time zone to America/New_York on the Ops Rotation calendar I own whose description mentions weekend on-call coverage. | 128 / 3 / 2 |
| CAL-23 | Delete Friday's architecture review that Kenji Sato (kenji.sato@northwind.example) attends as an optional guest. | 112 / 6 / 0 | Move the vendor sync on Thursday that has Dana Whitfield as an optional attendee to Room 2C. | 92 / 6 / 0 |
| CAL-24 | Set the description of my calendar located in Tokyo to "APAC offsite planning". | 79 / 1 / 1 | Update the description of the Front Desk calendar located at Building 4, 3rd Floor to say that badge access is required after 6 pm. | 131 / 2 / 1 |
| LIN-21 | Assign to Priya Nair the Web team issue about the login redirect that Omar Haddad created on September 10. | 106 / 6 / 2 | Set the priority to Urgent on the Web team's issue about the login timeout that Maya Chen created on June 3rd. | 110 / 7 / 3 |
| LIN-22 | Rename the doc Leo Park last edited in the Checkout Redesign project to "Checkout QA plan". | 91 / 4 / 0 | Update the title of the roadmap document in the Mobile Redesign project that Leo Park last edited to "Mobile Redesign Roadmap v2". | 130 / 5 / 0 |
| LIN-23 | Reopen the comment thread on WEB-5 that Maya Chen resolved. | 59 / 5 / 0 | Reopen the comment thread on WEB-7 about payment retries timing out that Sam Rivera resolved. | 93 / 5 / 0 |
| LIN-24 | Move ENG-9 into cycle 15 of the Engineering team. | 49 / 3 / 0 | Set the priority to Urgent on the issue about checkout hangs for guest users on Safari that's assigned to Priya Nair in the Web Platform team's Cycle 4. | 152 / 7 / 1 |
| LIN-25 | Add the Regression label from the Bug group to MOB-3. | 53 / 3 / 0 | In the Support team, set priority to Urgent for the issue assigned to Priya Nair that's tagged Customer Tier. | 109 / 6 / 2 |
| LIN-26 | Set the priority to Low on the Web team issue that Dana Whitfield is subscribed to. | 83 / 5 / 1 | In the Web team, set the priority to Urgent for the Design system audit issue that Sam Rivera is subscribed to. | 111 / 6 / 1 |
| SLK-21 | Add a :thumbsup: reaction to the message Priya Sharma posted in #deploys on September 23 about the rollback. | 108 / 6 / 0 | React with :eyes: to the message Leo Park posted in #incidents on Tuesday. | 74 / 6 / 0 |
| SLK-23 | Set the topic of the private channel whose purpose is coordinating vendor contracts to "Renewals due Oct 31". | 109 / 2 / 4 | Archive the private channel whose purpose mentions onboarding new hires and that has Diego Alvarez as a member. | 111 / 5 / 2 |
| SLK-24 | Post "Reminder: expense reports are due Friday" in the private channel that both Priya Sharma and Leo Park are members of. | 122 / 7 / 1 | React with the eyes emoji on the message in #incidents about the payment gateway timeout that was posted by someone who's a member of #payments-oncall. | 151 / 6 / 0 |
