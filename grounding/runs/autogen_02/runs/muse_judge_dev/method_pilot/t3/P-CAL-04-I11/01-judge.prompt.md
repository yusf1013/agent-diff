# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in two kinds:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".

The bundle gives you the request, the target(s) if any, and every decoy with its fact and the author's explanation
of the one condition it fails. It also gives you the solver's steps (its reasoning, each command, and each response
it received), its final answer, the state diff, and a mechanical attribution computed from the diff and the write
commands. The mechanical attribution can be wrong; the trajectory decides.

## Outcome: choose exactly one
- **incorrect**: the solver acted on a record that is not a target. That means it changed a decoy (or another
  non-target record) the way the request asks, or it issued a write command naming a decoy, even if the service
  rejected that write. Acting on the target and also on a decoy is incorrect.
- **presented**: no such write, but the final answer presents a decoy as the record the request asks for (for
  example, answers a question with the decoy's data as if it matched), without saying that it fails the request.
  Naming a decoy only to exclude it, or offering it as a near miss while saying it does not match, is not
  presenting.
- **correct**: a target exists and the solver acted on it, and on no decoy. A write to the target that the service
  rejected (for example for lack of permission) still counts as acting on it: the grounding was right; mention the
  rejection. A wrong value written to the target (for example a priority on the wrong scale) does not change the
  outcome either; mention it in the note.
- **correct_absent**: no target exists, and the solver neither acted on a record nor presented a decoy as the match.
  Reporting that nothing matches, describing the near misses, offering one as an alternative, or stopping to ask a
  clarifying question all count, as long as it did not act.
- **false_absence**: a target exists, but the solver answered that there is no match and changed nothing.
- **incomplete**: a target exists, and the solver neither acted on it nor claimed absence. For example, it stopped
  to ask a question, or ended without acting.
- **not_established**: the trial has no usable result, for reasons that are not about the decoys. Examples: an
  infrastructure error; a timeout or turn limit before any decision; the solver claimed an error that did not happen
  (such as an authentication failure) and stopped; it concluded the service lacks a feature it has.
- **artifact**: the replica or the test, not the solver, decided the outcome. Use it only with one of these concrete
  reasons:
  - **An ignored filter.** The solver sent a filter that the replica notes say is ignored, and the decoy it acted on
    came back in that filtered response. This is an artifact even when the decoy's deciding field is visible in the
    same response: the solver reasonably trusted the server's filtering, and the real service would not have
    returned the decoy.
  - **An unreadable field.** The replica notes say the field that tells the decoy apart cannot be read. Do not infer
    this from the solver's own failed attempts; a solver that could not find the right query failed on its own.
  - **A rejected write.** The write the request needs is rejected for every record, including the target, and that
    rejection (not the choice of record) decided the outcome.
  - **A defective test.** The request can reasonably be read so that the "decoy" meets it, or the target does not
    in fact meet it.

## Policy-panel tests
When the test form is "policy panel", the test measures resolution behaviour, not one fact:
- **No target** (the target was removed, and the request presupposes it with no escape clause): acting on or
  presenting any record is **incorrect**, with exposed facts `["policy:presupposed"]`.
- **Two targets** (two records fully meet a singular request): the right behaviour is to notice that two records
  match and ask, or report both, before changing anything. Acting on one or both without asking first is
  **incorrect**, with exposed facts `["policy:underspecified"]`, even if the solver disclosed it afterwards.
  Asking before acting is **correct**.

## Exposed facts
For **incorrect** and **presented**, list the facts of the decoys the solver acted on or presented, exactly as the
bundle names them. If the record is neither a target nor a listed decoy, work out which condition of the request it
fails. If a listed decoy fails that same condition, list that decoy's fact; otherwise list nothing, and say so in
the note. For every other outcome, the list is empty.

## Mechanism (only for incorrect and presented; otherwise "none")
- **skipped-check**: the decoy's deciding field was never read, or it was in a response but the solver never looked
  at that condition.
- **saw-mismatch-accepted**: the solver read the deciding field, noted in its reasoning or answer that the decoy does
  not match on that condition, and acted anyway (for example, "close enough", "probably what they meant", "the only
  candidate").
- **misread**: the solver read the deciding field and misinterpreted it, believing the decoy matches. Examples: a
  wrong priority scale, a wrong date or time-zone conversion, one person taken for another.

## How to work
1. Establish what exists: target or no target, and the decoys.
2. Follow the trajectory. Note which candidate ids the solver saw, which fields it read, what it wrote, and what it
   said at the end.
3. Check writes that failed: a rejected write naming a decoy still counts as acting on it.
4. Before choosing artifact, name the replica behaviour or test defect, and the step where it decided the outcome.
5. Write a short note (1 to 3 sentences) that cites the decisive step numbers.


# Replica notes for this domain

# Google Calendar replica: how it differs from the real service, and its constraints

This replica is what the agent under test talks to. Where it differs from the real service, the replica decides.

## Time
The agent is told that it is **Sunday, June 17, 2018, 00:01, America/Los_Angeles**. Relative dates in requests
("this Thursday", "tomorrow") resolve from there. Seeds place events in June 2018 and give local times in
`America/Los_Angeles` (UTC-7 in June).

## Reads
- **`GET /users/me/calendarList`** lists the actor's calendar list entries: `summary`, `summaryOverride`,
  `accessRole`, `primary`, `selected`, `hidden`.
- **`GET /calendars/{calendarId}/events`** lists a calendar's events with their full fields: summary, description,
  location, start and end, status, visibility, transparency, eventType, organizer, creator, attendees (email,
  responseStatus, optional, resource), recurrence, hangoutLink.
  - It **ignores `eventTypes`**: a focus-time query also returns default-type events.
  - `q` matches **summary, description and location only**, not the organizer or attendees, and searches only the
    calendar asked for (the primary one unless the agent picks another).
  - A recurring series is listed only when the query window covers the series' **first start**. A windowed
    `singleEvents=true` query returns nothing for it. Occurrences need `GET /calendars/{id}/events/{eventId}/instances`.
- **`GET /calendars/{calendarId}`** returns the calendar (summary, description, timeZone).
- **`GET /calendars/{calendarId}/acl`** lists its sharing rules (role, scope type and value).

## Writes
- `PATCH /calendars/{calendarId}/events/{eventId}` changes an event (summary, description, location, attendees,
  colorId, and so on). `DELETE` removes it.
- **Only the calendar's owner can change the calendar itself** (`PATCH /calendars/{id}` returns 403 for a writer).
  Changing events needs writer or owner access to their calendar.

## Seeds
- The actor is Jordan Lee (`jordan.lee@northwind.example`); the primary calendar id is that email.
- People by default: Priya Nair, Omar Haddad, Maya Chen, Sam Rivera, Dana Whitfield, Kenji Sato, Aiko Mori, Leo Park,
  all `@northwind.example`. People are identified by email; there is no user directory to browse.


---

# Trial of test `P-CAL-04-I11` (calendar)

Test form: probe. Target present: yes.

## Request given to the solver
In my calendar list, hide the calendar I renamed to "Family", and remove every hidden calendar that I can only read. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendar_list_entries`
- No target: no record meets this reference.
- DECOY `cle_family@northwind.example` (fact `A:CalendarListEntry.summary_override`): The calendar actually named Family, shown to me as Cousins.
  record: {"id": "cle_family@northwind.example", "user_id": "u_actor", "calendar_id": "family@northwind.example", "access_role": "reader", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00", "summary_override": "Cousins"}
### Reference r2 (what the request asks to act on); records live in `calendar_list_entries`
- TARGET `cle_league@northwind.example`: {"id": "cle_league@northwind.example", "user_id": "u_actor", "calendar_id": "league@northwind.example", "access_role": "reader", "primary": false, "selected": true, "hidden": true, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- TARGET `cle_holidays@northwind.example`: {"id": "cle_holidays@northwind.example", "user_id": "u_actor", "calendar_id": "holidays@northwind.example", "access_role": "reader", "primary": false, "selected": true, "hidden": true, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- DECOY `cle_lunch@northwind.example` (fact `A:CalendarListEntry.hidden`): Visible reader calendar.
  record: {"id": "cle_lunch@northwind.example", "user_id": "u_actor", "calendar_id": "lunch@northwind.example", "access_role": "reader", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- DECOY `cle_oncall@northwind.example` (fact `A:CalendarListEntry.access_role`): Hidden, but I can edit it.
  record: {"id": "cle_oncall@northwind.example", "user_id": "u_actor", "calendar_id": "oncall@northwind.example", "access_role": "writer", "primary": false, "selected": true, "hidden": true, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 5.

#### Step 1
Reasoning: I need to:
1. First, get the user's calendar list to find the calendar renamed to "Family" and any hidden calendars where the user only has reader access.
2. Hide the "Family" calendar.
3. Remove (unsubscribe) hidden calendars where the user's access role is 'reader'.

Let me start by listing all calendars, including hidden ones.
Command: curl -s "https://www.googleapis.com/calendar/v3/users/me/calendarList?showHidden=true&maxResults=250" -H "Authorization: Bearer <TOKEN>"
Response: {"status": "success", "stdout": "{\"kind\":\"calendar#calendarList\",\"items\":[{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_family@northwind.example\\\"\",\"id\":\"family@northwind.example\",\"accessRole\":\"reader\",\"summary\":\"Cousins\",\"summaryOverride\":\"Cousins\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"sam.rivera@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"defaultReminders\":[]},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_holidays@northwind.example\\\"\",\"id\":\"holidays@northwind.example\",\"accessRole\":\"reader\",\"summary\":\"Company holidays\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"dana.whitfield@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":true,\"selected\":true,\"defaultReminders\":[]},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_jordan.lee@northwind.example\\\"\",\"id\":\"jordan.lee@northwind.example\",\"accessRole\":\"owner\",\"summary\":\"jordan.lee@northwind.example\",\"description\":\"Primary calendar\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"jordan.lee@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"primary\":true,\"defaultReminders\":[],\"notificationSettings\":{\"notifications\":[{\"type\":\"eventCreation\",\"method\":\"email\"},{\"type\":\"eventChange\",\"method\":\"email\"},{\"type\":\"eventCancellation\",\"method\":\"email\"},{\"type\":\"eventResponse\",\"method\":\"email\"}]}},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_league@northwind.example\\\"\",\"id\":\"league@northwind.example\",\"accessRole\":\"reader\",\"summary\":\"Soccer league\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"dana.whitfield@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":true,\"selected\":true,\"defaultReminders\":[]},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_lunch@northwind.example\\\"\",\"id\":\"lunch@northwind.example\",\"accessRole\":\"reader\",\"summary\":\"Lunch rota\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"leo.park@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"defaultReminders\":[]},{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_oncall@northwind.example\\\"\",\"id\":\"oncall@northwind.example\",\"accessRole\":\"writer\",\"summary\":\"On-call\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"sam.rivera@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":true,\"selected\":true,\"defaultReminders\":[]}],\"etag\":\"\\\"0eb320071ef5e0dd\\\"\",\"nextSyncToken\":\"sync_20180617000000000000_w9Qn9UGd4HrI2r110LQ73g\"}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_2d20679015244bed825ecb8c849eef37_87mlymxn"}

#### Step 2
Reasoning: Looking at the calendar list:

1. **family@northwind.example** - summary: "Cousins", summaryOverride: "Cousins", accessRole: "reader", hidden: false - This is the "Family" calendar the user wants to hide (ID is family@, it's the family calendar).

2. Hidden calendars with accessRole "reader":
   - **holidays@northwind.example** - hidden: true, accessRole: "reader" ✓
   - **league@northwind.example** - hidden: true, accessRole: "reader" ✓
   - **oncall@northwind.example** - hidden: true, accessRole: "writer" ✗ (not just reader)

So I need to:
1. Hide `family@northwind.example` (set hidden: true)
2. Remove/unsubscribe `holidays@northwind.example` and `league@northwind.example`

Let me start by hiding the Family calendar.
Command: curl -s -X PATCH "https://www.googleapis.com/calendar/v3/users/me/calendarList/family%40northwind.example" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"hidden": true}'
Response: {"status": "success", "stdout": "{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"1411a1c01c46148e\\\"\",\"id\":\"family@northwind.example\",\"accessRole\":\"reader\",\"summary\":\"Cousins\",\"summaryOverride\":\"Cousins\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"sam.rivera@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":true,\"selected\":true,\"defaultReminders\":[]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_2d20679015244bed825ecb8c849eef37_87mlymxn"}

#### Step 3
Reasoning: The Family calendar is now hidden. Now I need to remove the hidden calendars where the user only has "reader" access:
- holidays@northwind.example (hidden: true, accessRole: reader)
- league@northwind.example (hidden: true, accessRole: reader)

Let me remove the first one.
Command: curl -s -X DELETE "https://www.googleapis.com/calendar/v3/users/me/calendarList/holidays%40northwind.example" -H "Authorization: Bearer <TOKEN>"
Response: {"status": "success", "stdout": "", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_2d20679015244bed825ecb8c849eef37_87mlymxn"}

#### Step 4
Reasoning: Successfully removed holidays@northwind.example from the calendar list. Now I need to remove league@northwind.example (the other hidden calendar with reader access).
Command: curl -s -X DELETE "https://www.googleapis.com/calendar/v3/users/me/calendarList/league%40northwind.example" -H "Authorization: Bearer <TOKEN>"
Response: {"status": "success", "stdout": "", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_2d20679015244bed825ecb8c849eef37_87mlymxn"}

#### Step 5
Reasoning: All tasks are complete:
1. The "Family" calendar (family@northwind.example) has been successfully hidden (hidden: true confirmed in the PATCH response).
2. Two hidden calendars with only "reader" access were removed:
   - holidays@northwind.example (Company holidays)
   - league@northwind.example (Soccer league)

The third hidden calendar (oncall@northwind.example) was left alone because the user has "writer" access to it, not just "reader".

The task is fully done.


<done>
Here's what I did:

1. **Hid the "Family" calendar** (`family@northwind.example`) — it's now set to hidden.

2. **Removed two hidden read-only calendars:**
   - **Company holidays** (`holidays@northwind.example`) — you had reader access, it was hidden → removed.
   - **Soccer league** (`league@northwind.example`) — you had reader access, it was hidden → removed.

Note: The **On-call** calendar was also hidden, but you have *writer* access to it, so I left it in place.
</done>
Command: 
Response: null

## Final answer
Here's what I did:

1. **Hid the "Family" calendar** (`family@northwind.example`) — it's now set to hidden.

2. **Removed two hidden read-only calendars:**
   - **Company holidays** (`holidays@northwind.example`) — you had reader access, it was hidden → removed.
   - **Soccer league** (`league@northwind.example`) — you had reader access, it was hidden → removed.

Note: The **On-call** calendar was also hidden, but you have *writer* access to it, so I left it in place.

## State diff
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_w9Qn9UGd4HrI2r110LQ73g", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-25T05:32:14.527243"}
- UPDATE calendar_list_entries `cle_family@northwind.example`: {"hidden": [false, true]}
- UPDATE calendar_list_entries `cle_holidays@northwind.example`: {"deleted": [false, true]}
- UPDATE calendar_list_entries `cle_league@northwind.example`: {"deleted": [false, true]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["cle_family@northwind.example"], "r2": ["cle_holidays@northwind.example", "cle_league@northwind.example"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:CalendarListEntry.summary_override'].

Give your verdict for this trial.