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

# Trial of test `SN0M-CAL-T05` (calendar)

Test form: cover (target and all decoys). Target present: yes.

## Request given to the solver
Just for this Tuesday, the team standup will be in Room 9 instead. Please update that, and leave the other weeks as they are.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendar_events`
- TARGET `ev_r9x_20180619T093000Z`: {}
- DECOY `ev_r9x` (fact `D:occurrence`, family F6): the series itself: changing it moves every week, not this Tuesday's
  record: {"id": "ev_r9x", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "ev_r9x@northwind.example", "summary": "Team standup", "location": "Room 2", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-05T09:30:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-05T09:45:00-07:00",…

## Solver steps
Run status: completed; termination: done; steps: 10.

#### Step 1
Reasoning: The user wants to update Google Calendar: this Tuesday (today is Sunday, 2018-06-17), the team standup will be in Room 9 instead of the usual room. Only this Tuesday, don't change other weeks (i.e., just this single event, don't change the entire recurring series).

First, since this falls under the google-calendar skill, I should read the google-calendar skill.
Command: read {"path": "~/.openclaw-state/7d881398dd7848de/workspace-assistant/skills/google-calendar/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: google-calendar\ndescription: \"Google Calendar scheduling and events API. Use it for anything in the user's Google Calendar account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Google Calendar\n\n## Current Session\n- **Service**: Google Calendar\n- **Base URL**: https://www.googleapis.com/calendar/v3\n- **Description**: Google Calendar scheduling and events API\n\n## Environment\n- You are authenticated as a user in the Google Calendar workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Google Calendar API.\n\n## API Documentation\nThe endpoint documentation is split by resource into the files below (in this skill's `references/` folder). Read the file for the resource you need.\n\n- `references/events-1.md`: GET /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events; PATCH /calendars/{calendarId}/events/{eventId}\n- `references/events-2.md`: GET /calendars/{calendarId}/events; DELETE /calendars/{calendarId}/events/{eventId}; GET /calendars/{calendarId}/events/{eventId}/instances; POST /calendars/{calendarId}/events/import; PUT /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events/quickAdd; POST /calendars/{calendarId}/events/watch\n- `references/events-3.md`: POST /calendars/{calendarId}/events/{eventId}/move\n- `references/acl.md`: POST /calendars/{calendarId}/acl; GET /calendars/{calendarId}/acl; DELETE /calendars/{calendarId}/acl/{ruleId}; GET /calendars/{calendarId}/acl/{ruleId}; PATCH /calendars/{calendarId}/acl/{ruleId}; PUT /calendars/{calendarId}/acl/{ruleId}; POST /calendars/{calendarId}/acl/watch\n- `references/other.md`: POST /freeBusy; GET /users/me/settings/{setting}; POST /users/me/settings/watch; GET /users/me/settings; GET /colors; POST /channels/stop\n- `references/calendars.md`: GET /calendars/{calendarId}; POST /calendars; PATCH /calendars/{calendarId}; DELETE /calendars/{calendarId}; POST /calendars/{calendarId}/clear; PUT /calendars/{calendarId}\n- `references/calendar-list.md`: GET /users/me/calendarList; POST /users/me/calendarList; PATCH /users/me/calendarList/{calendarId}; DELETE /users/me/calendarList/{calendarId}; GET /users/me/calendarList/{calendarId}; PUT /users/me/calendarList/{calendarId}; POST /users/me/calendarList/watch\n"}

#### Step 2
Reasoning: Let's check the reference files for the event API, and also get a grasp of the current date/time. The message's timestamp is [Sun 2018-06-17 00:01 PDT] — interestingly, that's the message timestamp. "This Tuesday" would be 2018-06-19. But wait — that timestamp seems odd (2018). Let's confirm the actual current date with session_status.

Actually, the message header says [Sun 2018-06-17 00:01 PDT]. This is the timestamp of the user message. So "this Tuesday" = 2018-06-19. Hmm, but that's 2018. Still, it might be a simulated environment. Let's trust the message's timestamp: Sunday, June 17, 2018. This Tuesday = June 19, 2018.

First, let's read the events reference file.
Command: read {"path": "~/.openclaw-state/7d881398dd7848de/workspace-assistant/skills/google-calendar/references/events-1.md"}
Response: {"status": "success", "stdout": "# Google Calendar API: events-1\n\n## GET /calendars/{calendarId}/events/{eventId}\nReturns an event based on its Google Calendar ID. To retrieve an event using its iCalendar ID, call the events.list method using the iCalUID parameter.\n\n**Parameters:**\n  path:\n    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.\n    - `eventId` (string, **required**): Event identifier.\n  query:\n    - `alwaysIncludeEmail` (boolean, optional): Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available.\n    - `maxAttendees` (integer, optional): The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned.\n    - `timeZone` (string, optional): Time zone used in the response. The default is the time zone of the calendar.\n\n## POST /calendars/{calendarId}/events\nCreates an event.\n\n**Parameters:**\n  path:\n    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.\n  query:\n    - `conferenceDataVersion` (integer, optional): Version number of conference data supported by the API client. Version 0 assumes no conference data support. Version 1 enables support for copying of ConferenceData as well as for creating new conferences. The default is 0. Acceptable values are 0 to 1, inclusive.\n    - `maxAttendees` (integer, optional): The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned.\n    - `sendNotifications` (boolean, optional): Deprecated. Please use sendUpdates instead. Whether to send notifications about the creation of the new event. The default is false.\n    - `sendUpdates` (string, optional): Whether to send notifications about the creation of the new event. Note that some emails might still be sent. The default is false.\n    - `supportsAttachments` (boolean, optional): Whether API client performing operation supports event attachments. The default is False.\n  body:\n    - `start` (object, **required**): The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance.\n    - `end` (object, **required**): The (exclusive) end time of the event. For a recurring event, this is the end time of the first instance.\n    - `summary` (string, optional): Title of the event.\n    - `description` (string, optional): Description of the event. Can contain HTML.\n    - `location` (string, optional): Geographic location of the event as free-form text.\n    - `colorId` (s […5727 chars omitted…] ferring to an entry in the event section of the colors definition.\n    - `reminders` (object, optional): Information about the event's reminders.\n    - `status` (string, optional): Status of the event: 'confirmed', 'tentative', or 'cancelled'.\n    - `visibility` (string, optional): Visibility of the event: 'default', 'public', 'private', or 'confidential'.\n    - `transparency` (string, optional): Whether the event blocks time on the calendar: 'opaque' (busy) or 'transparent' (available).\n"}

#### Step 3
Reasoning: 
Command: read {"path": "~/.openclaw-state/7d881398dd7848de/workspace-assistant/skills/google-calendar/references/events-2.md"}
Response: {"status": "success", "stdout": "# Google Calendar API: events-2\n\n## GET /calendars/{calendarId}/events\nReturns events on the specified calendar.\n\n**Parameters:**\n  path:\n    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.\n  query:\n    - `alwaysIncludeEmail` (boolean, optional): Deprecated and ignored.\n    - `eventTypes` (string, optional): Event types to return. Can be repeated multiple times. Acceptable values: 'birthday', 'default', 'focusTime', 'fromGmail', 'outOfOffice', 'workingLocation'. If unset, returns all event types.\n    - `iCalUID` (string, optional): Specifies an event ID in the iCalendar format to be provided in the response. Use this to search for an event by its iCalendar ID.\n    - `maxAttendees` (integer, optional): The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned.\n    - `maxResults` (integer, optional): Maximum number of events returned on one result page. By default the value is 250 events. The page size can never be larger than 2500 events.\n    - `orderBy` (string, optional): The order of the events returned in the result. Acceptable values: 'startTime' (only available when singleEvents is True), 'updated'. The default is an unspecified, stable order.\n    - `pageToken` (string, optional): Token specifying which result page to return.\n    - `privateExtendedProperty` (string, optional): Extended properties constraint specified as propertyName=value. Matches only private properties. Can be repeated multiple times.\n    - `q` (string, optional): Free text search terms to find events that match these terms in fields like summary, description, location, attendee's displayName/email, organizer's displayName/email, and working location properties.\n    - `sharedExtendedProperty` (string, optional): Extended properties constraint specified as propertyName=value. Matches only shared properties. Can be repeated multiple times.\n    - `showDeleted` (boolean, optional): Whether to include deleted events (with status equals 'cancelled') in the result. The default is False.\n    - `showHiddenInvitations` (boolean, optional): Whether to include hidden invitations in the result. The default is False.\n    - `singleEvents` (boolean, optional): Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. The default is False.\n    - `syncToken` (string, optional): Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. Makes the result contain only entries that have changed since then. Cannot be used with iCalUID, orderBy, privateExtendedProperty, q, sharedExtendedProperty, timeMin, timeMa […7232 chars omitted…] ime, and duration. Useful for quick event creation without structured data.\n\n**Parameters:**\n  path:\n    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.\n  query:\n    - `text` (string, **required**): The text describing the event to be created. Examples: 'Dinner with John tomorrow at 7pm', 'Meeting June 28 at 9:30am for 30 minutes', 'Team standup every Monday at 9am'.\n    - `sendUpdates` (string, optional): Who receives notifications: 'all', 'externalOnly', 'none'.\n    - `sendNotifications` (boolean, optional): Deprecated. Use sendUpdates instead.\n\n## POST /calendars/{calendarId}/events/watch\nCreates a notification channel to watch for changes to events on a calendar. When events are created, updated, or deleted, Google sends a POST  […489 chars omitted…] entifier (UUID recommended). Max 64 characters.\n    - `type` (string, **required**): Must be 'web_hook'.\n    - `address` (string, **required**): HTTPS URL to receive notifications. Must be registered in Google Cloud Console.\n    - `token` (string, optional): Arbitrary string sent with notifications for verification. Max 256 characters.\n    - `expiration` (long, optional): Unix timestamp (ms) when channel expires. Default ~1 week.\n    - `params` (object, optional): Additional parameters.\n"}

#### Step 4
Reasoning: Today is Sunday, June 17, 2018. Wait a minute, the timestamp says "[Sun 2018-06-17 00:01 PDT]" — June 17, 2018 was indeed a Sunday. So "this Tuesday" is June 19, 2018.

The user wants to change only the Tuesday standup this week to Room 9, and leave the other weeks as they are.

Approach: This is probably a recurring event. To change only a single instance of a recurring event, I need to do one of the following:
1. Find the recurring event, get the instance for Tuesday, June 19, and PATCH that instance with the new location (this creates an exception that only affects that single instance).
2. Or use EXDATE/EXRULE... no wait, just PATCHing the instance is the standard way.

First, let's search for the standup event. I'll query events with the search term "standup" within the relevant time period.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?q=standup&timeMin=2018-06-15T00:00:00-07:00&timeMax=2018-06-25T00:00:00-07:00&singleEvents=true&maxAttendees=0" -H "Authorization: Bearer <TOKEN>" | head -c 4000
Response: {"status": "success", "stdout": "{\"kind\":\"calendar#events\",\"items\":[],\"etag\":\"\\\"f8d874c6368b2cbd\\\"\",\"summary\":\"jordan.lee@northwind.example\",\"description\":\"Primary calendar\",\"timeZone\":\"America/Los_Angeles\",\"accessRole\":\"owner\",\"updated\":\"2018-06-17T00:00:00-07:00\",\"nextSyncToken\":\"sync_20180617000000000000_7cAXQyMM8hDH-eKojp8QhA\"}"}

#### Step 5
Reasoning: No results for that query. Let me try a broader search — "standup" might be called "Team standup" or "Daily standup," or it might be under a different calendar. I'll try searching with the "standup" keyword without a time restriction, and also list out the calendar list.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?q=standup&maxAttendees=0&orderBy=startTime" -H "Authorization: Bearer <TOKEN>" | head -c 4000; echo "----"; curl -s "https://www.googleapis.com/calendar/v3/users/me/calendarList" -H "Authorization: Bearer <TOKEN>" | head -c 4000
Response: {"status": "success", "stdout": "{\"error\":{\"code\":400,\"message\":\"orderBy='startTime' is only available when singleEvents is true\",\"errors\":[{\"domain\":\"calendar\",\"reason\":\"invalid\",\"message\":\"orderBy='startTime' is only available when singleEvents is true\"}]}}----\n{\"kind\":\"calendar#calendarList\",\"items\":[{\"kind\":\"calendar#calendarListEntry\",\"etag\":\"\\\"etag_cle_jordan.lee@northwind.example\\\"\",\"id\":\"jordan.lee@northwind.example\",\"accessRole\":\"owner\",\"summary\":\"jordan.lee@northwind.example\",\"description\":\"Primary calendar\",\"timeZone\":\"America/Los_Angeles\",\"conferenceProperties\":{\"allowedConferenceSolutionTypes\":[\"hangoutsMeet\"]},\"dataOwner\":\"jordan.lee@northwind.example\",\"backgroundColor\":\"#9fc6e7\",\"foregroundColor\":\"#000000\",\"hidden\":false,\"selected\":true,\"primary\":true,\"defaultReminders\":[],\"notificationSettings\":{\"notifications\":[{\"type\":\"eventCreation\",\"method\":\"email\"},{\"type\":\"eventChange\",\"method\":\"email\"},{\"type\":\"eventCancellation\",\"method\":\"email\"},{\"type\":\"eventResponse\",\"method\":\"email\"}]}}],\"etag\":\"\\\"40ffe2b9a5419ae2\\\"\",\"nextSyncToken\":\"sync_20180617000000000000_TJLn_XAcyB8QD6FQruXm-A\"}"}

#### Step 6
Reasoning: The q=standup search within the range returned no results. Let me try a broader search: without timeMin/timeMax, search for q=standup across all of them, and also try q=meeting. Note that the current date is 2018-06-17 (Sun) 00:01 PDT. So "this Tuesday" = 2018-06-19.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?q=standup&maxAttendees=0" -H "Authorization: Bearer <TOKEN>" | head -c 6000; echo "----"; curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?q=Team&maxAttendees=0" -H "Authorization: Bearer <TOKEN>" | head -c 6000
Response: {"status": "success", "stdout": "{\"kind\":\"calendar#events\",\"items\":[],\"etag\":\"\\\"5405860effd17a5d\\\"\",\"summary\":\"jordan.lee@northwind.example\",\"description\":\"Primary calendar\",\"timeZone\":\"America/Los_Angeles\",\"accessRole\":\"owner\",\"updated\":\"2018-06-17T00:00:00-07:00\",\"nextSyncToken\":\"sync_20180617000000000000_qqXA68p3IzuSSpVZYEATSw\"}----\n{\"kind\":\"calendar#events\",\"items\":[],\"etag\":\"\\\"9d96defbdb531a04\\\"\",\"summary\":\"jordan.lee@northwind.example\",\"description\":\"Primary calendar\",\"timeZone\":\"America/Los_Angeles\",\"accessRole\":\"owner\",\"updated\":\"2018-06-17T00:00:00-07:00\",\"nextSyncToken\":\"sync_20180617000000000000_EwDvKYnJnSzfs8aU1OGMjQ\"}"}

#### Step 7
Reasoning: I need to investigate this further. Let me check the details.

The search results for "standup" and "Team" are empty. Maybe the event title is different. Let me list all events for the upcoming week and check what's there.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?timeMin=2018-06-17T00:00:00-07:00&timeMax=2018-06-25T00:00:00-07:00&singleEvents=true&maxAttendees=0&orderBy=startTime" -H "Authorization: Bearer <TOKEN>" | python3 -m json.tool | head -c 8000
Response: {"status": "success", "stdout": "{\n    \"kind\": \"calendar#events\",\n    \"items\": [],\n    \"etag\": \"\\\"fbec834b380ef768\\\"\",\n    \"summary\": \"jordan.lee@northwind.example\",\n    \"description\": \"Primary calendar\",\n    \"timeZone\": \"America/Los_Angeles\",\n    \"accessRole\": \"owner\",\n    \"updated\": \"2018-06-17T00:00:00-07:00\",\n    \"nextSyncToken\": \"sync_20180617000000000000_ZvHRBWX3z6kseGwk-mwYfQ\"\n}"}

#### Step 8
Reasoning: No events were found. Let me try checking a broader range — maybe the standup is a recurring event, and the q search should have caught it. To see what's in the calendar, I'll try listing all events over the next few weeks without q.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?timeMin=2018-06-01T00:00:00-07:00&timeMax=2018-07-01T00:00:00-07:00&singleEvents=true&maxAttendees=0&orderBy=startTime" -H "Authorization: Bearer <TOKEN>" | python3 -c "
import json,sys
d=json.load(sys.stdin)
print('count:', len(d['items']))
for e in d['items']:
    print(e.get('id'), '|', e.get('start'), '|', e.get('summary'), '|', e.get('location'), '|', e.get('recurringEventId'))
"
Response: {"status": "success", "stdout": "count: 4\nev_r9x_20180605T093000Z | {'dateTime': '2018-06-05T09:30:00+00:00', 'timeZone': 'America/Los_Angeles'} | Team standup | Room 2 | ev_r9x\nev_r9x_20180612T093000Z | {'dateTime': '2018-06-12T09:30:00+00:00', 'timeZone': 'America/Los_Angeles'} | Team standup | Room 2 | ev_r9x\nev_r9x_20180619T093000Z | {'dateTime': '2018-06-19T09:30:00+00:00', 'timeZone': 'America/Los_Angeles'} | Team standup | Room 2 | ev_r9x\nev_r9x_20180626T093000Z | {'dateTime': '2018-06-26T09:30:00+00:00', 'timeZone': 'America/Los_Angeles'} | Team standup | Room 2 | ev_r9x"}

#### Step 9
Reasoning: Team standups are recurring events (id is ev_r9x), and the instances are on Tuesdays: June 5, June 12, June 19, June 26. Today is Sunday, June 17, 2018, so "this Tuesday" is June 19, 2018. Instance ID: ev_r9x_20180619T093000Z.

PATCH the instance to change the location to "Room 9". Since this only affects that instance, the other weeks will remain unchanged.
Command: curl -s -X PATCH "https://www.googleapis.com/calendar/v3/calendars/primary/events/ev_r9x_20180619T093000Z" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"location":"Room 9"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
print(d.get('id'), '|', d.get('summary'), '|', d.get('start'), '|', d.get('location'), '|', d.get('recurringEventId'))
"
Response: {"status": "success", "stdout": "ev_r9x_20180619T093000Z | Team standup | {'dateTime': '2018-06-19T09:30:00+00:00', 'timeZone': 'America/Los_Angeles'} | Room 9 | ev_r9x"}

#### Step 10
Reasoning: The update succeeded. The June 19 (Tuesday) instance now indicates Room 9. The other weeks remain unchanged (the PATCH only targeted that instance ID, and recurringEventId confirms it's a single instance exception).

I should verify that the other instances haven't been modified. Since PATCH only touched a single instance, they should be fine. I could do a quick check, but the response already confirms the target instance was changed, and other weeks retain Room 2 (the base recurring event is unchanged — I haven't touched the parent event ev_r9x).

Done. Replying concisely.

Done ✅ — Tuesday's standup (Jun 19, 9:30 AM) is now set to **Room 9**, as a one-off exception to the recurring event. All other weeks (Jun 5, 12, 26, and beyond) stay in Room 2.
Command: 
Response: null

## Final answer
Done ✅ — Tuesday's standup (Jun 19, 9:30 AM) is now set to **Room 9**, as a one-off exception to the recurring event. All other weeks (Jun 5, 12, 26, and beyond) stay in Room 2.

## State diff
- INSERT calendar_event_attendees: {"id": 4, "event_id": "ev_r9x_20180619T093000Z", "email": "jordan.lee@northwind.example", "display_name": "Jordan Lee", "organizer": true, "self": false, "resource": false, "optional": false, "response_status": "accepted", "additional_guests": 0}
- INSERT calendar_event_attendees: {"id": 5, "event_id": "ev_r9x_20180619T093000Z", "email": "sam.rivera@northwind.example", "display_name": "Sam Rivera", "organizer": false, "self": false, "resource": false, "optional": false, "response_status": "accepted", "additional_guests": 0}
- INSERT calendar_event_attendees: {"id": 6, "event_id": "ev_r9x_20180619T093000Z", "email": "maya.chen@northwind.example", "display_name": "Maya Chen", "organizer": false, "self": false, "resource": false, "optional": false, "response_status": "accepted", "additional_guests": 0}
- INSERT calendar_events: {"id": "ev_r9x_20180619T093000Z", "calendar_id": "jordan.lee@northwind.example", "status": "confirmed", "summary": "Team standup", "location": "Room 9", "creator_email": "jordan.lee@northwind.example", "organizer_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_display_name": "Jordan Lee", "creator_self": false, "organizer_self": false, "start": {"dateTime": "2018-06-19T09:30:00+00:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-19T09:45:00+00:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-19T09:30:00", "end_datetime": "2018-06-19T09:45:00", "end_time_unspecified": false, "recurring_event_id": "ev_r9x", "origi…
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_7cAXQyMM8hDH-eKojp8QhA", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T15:54:23.084155"}
- INSERT calendar_sync_tokens: {"id": 2, "token": "sync_20180617000000000000_TJLn_XAcyB8QD6FQruXm-A", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T15:54:35.171035"}
- INSERT calendar_sync_tokens: {"id": 3, "token": "sync_20180617000000000000_qqXA68p3IzuSSpVZYEATSw", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T15:54:47.044837"}
- INSERT calendar_sync_tokens: {"id": 4, "token": "sync_20180617000000000000_EwDvKYnJnSzfs8aU1OGMjQ", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T15:54:47.368325"}
- INSERT calendar_sync_tokens: {"id": 5, "token": "sync_20180617000000000000_ZvHRBWX3z6kseGwk-mwYfQ", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T15:54:58.729196"}
- INSERT calendar_sync_tokens: {"id": 6, "token": "sync_20180617000000000000_TXMRzlfPCcwnSm_nn5gSkA", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T15:55:18.040753"}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["ev_r9x_20180619T093000Z"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.