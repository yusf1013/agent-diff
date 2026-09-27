# Trial of test `P-AP-CAL-02-I13` (calendar)

Test form: probe. Target present: no.

## Request given to the solver
Hide the Team Calendar that I have writer access to on my calendar list, and that's shared with the design team as a writer. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendars`
- No target: no record meets this reference.
- DECOY `team-launch@northwind.example` (fact `B:AclRule.calendar_id`, family F5): The design team's rule on this calendar is read-only; a separate rule grants writer access only to the product team.
  record: {"id": "team-launch@northwind.example", "summary": "Team Calendar", "time_zone": "America/Los_Angeles", "owner_id": "u_kenji", "data_owner": "kenji.sato@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 4.

#### Step 1
Reasoning: I need to find a "Team Calendar" where the user has writer access. Let me first list the user's calendars to find it.
Command: curl -s -H "Authorization: Bearer <TOKEN>" "https://www.googleapis.com/calendar/v3/users/me/calendarList"
Response: {"status": "success", "stdout": "{\"kind\":\"calendar#calendarList\",\"items\":[{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_jordan.lee@northwind.example\\\"\",\"id\":\"jordan.lee@northwind.example\",\"accessRole\":\"owner\",\"summary\":\"jordan.lee@northwind.example\",\"description\":\"Primary calendar\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"jordan.lee@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"primary\":true,\"defaultReminders\":[],\"notificationSettings\":{\"notifications\":[{\"type\":\"eventCreation\",\"method\":\"email\"},{\"type\":\"eventChange\",\"method\":\"email\"},{\"type\":\"eventCancellation\",\"method\":\"email\"},{\"type\":\"eventResponse\",\"method\":\"email\"}]}},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_marketing-sync@northwind.example\\\"\",\"id\":\"marketing-sync@northwind.example\",\"accessRole\":\"reader\",\"summary\":\"Marketing Sync\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"aiko.mori@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"defaultReminders\":[]},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_team-launch@northwind.example\\\"\",\"id\":\"team-launch@northwind.example\",\"accessRole\":\"writer\",\"summary\":\"Team Calendar\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"kenji.sato@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"defaultReminders\":[]},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_team-sales@northwind.example\\\"\",\"id\":\"team-sales@northwind.example\",\"accessRole\":\"reader\",\"summary\":\"Team Calendar\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"leo.park@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"defaultReminders\":[]}],\"etag\":\"\\\"436f699ed20397f9\\\"\",\"nextSyncToken\":\"sync_20180617000000000000_1XensZtEju3SQ5Ih9tWmIQ\"}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6de2b93cbfc84b659edf8d6f8b01b0c6_mss_myv1"}

#### Step 2
Reasoning: I found two "Team Calendar" entries:
1. `team-launch@northwind.example` - user has "writer" access
2. `team-sales@northwind.example` - user has "reader" access

The user specified they have writer access, so the candidate is `team-launch@northwind.example`. Now I need to check if it's shared with the design team as a writer. Let me check the ACL.
Command: curl -s -H "Authorization: Bearer <TOKEN>" "https://www.googleapis.com/calendar/v3/calendars/team-launch@northwind.example/acl"
Response: {"status": "success", "stdout": "{\"error\":{\"code\":403,\"message\":\"Insufficient permissions for calendar: team-launch@northwind.example\",\"errors\":[{\"domain\":\"calendar\",\"reason\":\"forbidden\",\"message\":\"Insufficient permissions for calendar: team-launch@northwind.example\"}]}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6de2b93cbfc84b659edf8d6f8b01b0c6_mss_myv1"}

#### Step 3
Reasoning: I can't access the ACL with writer permissions. However, among the user's calendar list, there's only one "Team Calendar" where they have writer access: `team-launch@northwind.example`. The other "Team Calendar" (`team-sales@northwind.example`) only has reader access. So this uniquely identifies the calendar the user is referring to. I'll proceed to hide it by patching the calendar list entry.
Command: curl -s -X PATCH -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" "https://www.googleapis.com/calendar/v3/users/me/calendarList/team-launch@northwind.example" -d '{"hidden": true}'
Response: {"status": "success", "stdout": "{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"917665b813b3ee1a\\\"\",\"id\":\"team-launch@northwind.example\",\"accessRole\":\"writer\",\"summary\":\"Team Calendar\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"kenji.sato@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":true,\"selected\":true,\"defaultReminders\":[]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6de2b93cbfc84b659edf8d6f8b01b0c6_mss_myv1"}

#### Step 4
Reasoning: The PATCH request succeeded. The calendar list entry for `team-launch@northwind.example` now shows `"hidden": true`. This was the "Team Calendar" where the user has writer access (the other "Team Calendar" `team-sales@northwind.example` only has reader access). I was unable to verify the ACL due to permission limitations (writer access doesn't allow viewing ACL), but this is the only calendar that matches the "Team Calendar" with writer access criteria.


<done>
I found the "Team Calendar" (`team-launch@northwind.example`) where you have writer access and have hidden it from your calendar list. Note: I couldn't independently verify the ACL to confirm it's shared with the design team as a writer (my access level doesn't allow viewing the calendar's sharing settings), but it was the only "Team Calendar" in your list with writer access. The calendar is now hidden.
</done>
Command: 
Response: null

## Final answer
I found the "Team Calendar" (`team-launch@northwind.example`) where you have writer access and have hidden it from your calendar list. Note: I couldn't independently verify the ACL to confirm it's shared with the design team as a writer (my access level doesn't allow viewing the calendar's sharing settings), but it was the only "Team Calendar" in your list with writer access. The calendar is now hidden.

## State diff
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_1XensZtEju3SQ5Ih9tWmIQ", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-26T13:08:12.829851"}
- UPDATE calendar_list_entries `cle_team-launch@northwind.example`: {"hidden": [false, true]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["team-launch@northwind.example"]}. Provisional outcome: incorrect. Provisional exposed facts: ['B:AclRule.calendar_id'].

Give your verdict for this trial.