# Facts to test

Together, your tests must check the assistant on each fact below: for every fact, at least one test in which that
fact decides which record is the right one.

The kinds of fact:
- **attribute:** an identifying attribute of a record (identity, text, time, quantity, state);
- **relationship:** a record's related person or record in a given role (a foreign-key role, an association);
- **hierarchy:** a level of a hierarchy or a self-relationship (a parent, a reply's parent);
- **binding:** several conditions that must hold on the same related record, across a to-many relationship;
- **derived value:** a value computed from records (a count, the latest one, a local date, the primary calendar).

| Fact | Kind | Rests on |
|---|---|---|
| `A:Calendar.data_owner` | attribute | `calendars.data_owner` |
| `A:Calendar.time_zone` | attribute | `calendars.time_zone` |
| `A:CalendarListEntry.access_role` | attribute | `calendar_list_entries.access_role` |
| `A:CalendarListEntry.hidden` | attribute | `calendar_list_entries.hidden` |
| `A:CalendarListEntry.summary_override` | attribute | `calendar_list_entries.summary_override` |
| `A:Event.creator_email` | attribute | `calendar_events.creator_email` |
| `A:Event.location` | attribute | `calendar_events.location` |
| `A:Event.organizer_email` | attribute | `calendar_events.organizer_email` |
| `A:Event.start` | attribute | `calendar_events.start` |
| `A:Event.summary` | attribute | `calendar_events.summary` |
| `A:Event.transparency` | attribute | `calendar_events.transparency` |
| `A:EventAttendee.response_status` | attribute | `calendar_event_attendees.response_status` |
| `B:EventAttendee.event_id` | binding | `EventAttendee.event_id` |
| `D:local_time` | derived value | `local_time` |
| `D:primary` | derived value | `primary` |
| `R:EventAttendee.event_id` | relationship | `EventAttendee.event_id` |
