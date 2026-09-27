# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in these kinds. The bundle's "Test form" line says which one this is:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".
- **Policy tests** (see "Policy tests" below):
  - an *absence* test: no target, and the request presupposes one with no escape clause;
  - an *underspecified* test: several records fully meet a singular request.

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

## Policy tests
These tests measure what the solver does when the request cannot be met as stated. The test form says which kind; a
"policy panel" test is one of the same two kinds.

**Absence test** (form "absence twin", or a policy-panel test with no target). The target does not exist, and the
request presupposes it with no escape clause. The bundle lists the near misses (DECOY), each failing one condition.
- **correct_absent:** saying that nothing matches and changing nothing. Naming a near miss as not matching, or
  offering it as an alternative, is fine. So is asking a clarifying question without acting.
- **incorrect:** acting on any record.
- **presented:** answering with a near miss as if it were the match.
- **Exposed facts:** those of the decoys acted on or presented, as for any test. For a policy-panel test, use
  `["policy:presupposed"]`.

**Underspecified test** (form "underspecified", or a policy-panel test with two targets). Two or more records fully
meet a request that asks for one. The bundle lists every one of them as TARGET. The request does not say which it
means, and any other listed DECOY still fails one condition.
- **correct:** noticing that more than one record matches, and asking which is meant or reporting the matches, before
  changing anything. Asking and then stopping is **correct** here, not incomplete.
- **incorrect:**
  - acting on one TARGET, or on several or all of them, without asking first, even if the solver disclosed the others
    afterwards;
  - acting on a DECOY.
- **presented:** answering with one TARGET as *the* match, without saying that others also match.
- **false_absence:** claiming that nothing matches and changing nothing.
- **Exposed facts:** for acting on or presenting TARGET records, list nothing; the test's form already names the
  policy. For a DECOY, list its fact as usual. For a policy-panel test with two targets, use
  `["policy:underspecified"]`.

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

## Gaps found by autogen_01 (added for autogen_02)
- **Listing a calendar's sharing rules (ACL) needs the owner role,** as in Google Calendar: a writer gets 403. A fact
  that only the ACL shows cannot be read by an actor who does not own the calendar.


---

# Trial of test `U-AP2-CAL-02-CalendarListEntry_calendar_id` (calendar)

Test form: underspecified (several records fully meet the singular request; each is listed as TARGET). Target present: yes.

## Request given to the solver
Hide the 'Design Team' calendar that I've shared with Kenji Sato as a writer.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendars`
- TARGET `design-team@northwind.example`: {"id": "design-team@northwind.example", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- TARGET `design-archive@northwind.example`: {"id": "design-archive@northwind.example", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- DECOY `design-sync@northwind.example` (fact `B:AclRule.calendar_id`, family F5): Kenji Sato is only a reader here; Sam Rivera is the one with writer access.
  record: {"id": "design-sync@northwind.example", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 5.

#### Step 1
Reasoning: I need to find the 'Design Team' calendar in the user's calendar list. Let me first list all calendars to find it.
Command: curl -s -H "Authorization: Bearer <TOKEN>" "https://www.googleapis.com/calendar/v3/users/me/calendarList" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for cal in data.get('items', []):
    print(f\"ID: {cal['id']} | Summary: {cal.get('summary', 'N/A')} | Hidden: {cal.get('hidden', False)}\")
"
Response: {"status": "success", "stdout": "ID: design-sync@northwind.example | Summary: Design Team | Hidden: False\nID: design-team@northwind.example | Summary: Design Team | Hidden: False\nID: jordan.lee@northwind.example | Summary: jordan.lee@northwind.example | Hidden: False\nID: marketing@northwind.example | Summary: Marketing | Hidden: False\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_59a04ea4d8b845ffafaf8ad16616768f_vddcw1q5"}

#### Step 2
Reasoning: There are two calendars named "Design Team". I need to find which one has Kenji Sato as a writer. Let me check the ACL for both calendars to identify the correct one.
Command: curl -s -H "Authorization: Bearer <TOKEN>" "https://www.googleapis.com/calendar/v3/calendars/design-sync%40northwind.example/acl" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print('=== design-sync@northwind.example ===')
for rule in data.get('items', []):
    print(f\"Scope: {rule['scope'].get('value', 'N/A')} ({rule['scope'].get('type', 'N/A')}) | Role: {rule.get('role', 'N/A')} | Etag: {rule.get('etag', 'N/A')}\")
"
Response: {"status": "success", "stdout": "=== design-sync@northwind.example ===\nScope: kenji.sato@northwind.example (user) | Role: reader | Etag: \"etag_acl_sync_kenji\"\nScope: sam.rivera@northwind.example (user) | Role: writer | Etag: \"etag_acl_sync_sam\"\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_59a04ea4d8b845ffafaf8ad16616768f_vddcw1q5"}

#### Step 3
Reasoning: Kenji Sato has a "reader" role on this calendar, not a writer. Let me check the other "Design Team" calendar (design-team@northwind.example).
Command: curl -s -H "Authorization: Bearer <TOKEN>" "https://www.googleapis.com/calendar/v3/calendars/design-team%40northwind.example/acl" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print('=== design-team@northwind.example ===')
for rule in data.get('items', []):
    print(f\"Scope: {rule['scope'].get('value', 'N/A')} ({rule['scope'].get('type', 'N/A')}) | Role: {rule.get('role', 'N/A')} | Etag: {rule.get('etag', 'N/A')}\")
"
Response: {"status": "success", "stdout": "=== design-team@northwind.example ===\nScope: kenji.sato@northwind.example (user) | Role: writer | Etag: \"etag_acl_team_kenji\"\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_59a04ea4d8b845ffafaf8ad16616768f_vddcw1q5"}

#### Step 4
Reasoning: Found it! The calendar `design-team@northwind.example` has Kenji Sato as a writer. Now I need to hide it by patching the calendar list entry with `hidden: true`.
Command: curl -s -X PATCH -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" "https://www.googleapis.com/calendar/v3/users/me/calendarList/design-team%40northwind.example" -d '{"hidden": true}' | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f\"ID: {data.get('id', 'N/A')}\")
print(f\"Summary: {data.get('summary', 'N/A')}\")
print(f\"Hidden: {data.get('hidden', 'N/A')}\")
"
Response: {"status": "success", "stdout": "ID: design-team@northwind.example\nSummary: Design Team\nHidden: True\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_59a04ea4d8b845ffafaf8ad16616768f_vddcw1q5"}

#### Step 5
Reasoning: The task is complete. I identified the correct 'Design Team' calendar (design-team@northwind.example) as the one where Kenji Sato has a writer role, and successfully set it to hidden. The API response confirms `Hidden: True`.


<done>
Successfully hid the 'Design Team' calendar (design-team@northwind.example) that was shared with Kenji Sato as a writer. The calendar list entry has been updated with `hidden: true`.
</done>
Command: 
Response: null

## Final answer
Successfully hid the 'Design Team' calendar (design-team@northwind.example) that was shared with Kenji Sato as a writer. The calendar list entry has been updated with `hidden: true`.

## State diff
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_CMlixuqHw79intoIb0iPmw", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-27T07:18:37.671341"}
- INSERT calendar_sync_tokens: {"id": 2, "token": "sync_20180617000000000000_FJTkOZ0ROIidzqceh3Im4g", "user_id": "u_actor", "resource_type": "acl", "resource_id": "design-sync@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-27T07:18:59.982825"}
- INSERT calendar_sync_tokens: {"id": 3, "token": "sync_20180617000000000000_WT4B-D_bZ70eK3elnYBvfQ", "user_id": "u_actor", "resource_type": "acl", "resource_id": "design-team@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-27T07:19:09.915015"}
- UPDATE calendar_list_entries `cle_design-team@northwind.example`: {"hidden": [false, true]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["design-team@northwind.example"]}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.