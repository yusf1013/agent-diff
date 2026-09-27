Write scenario `AR-CAL-23` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:EventAttendee.email", "kind": "A", "subkind": "identity", "entity": "EventAttendee", "table": "calendar_event_attendees", "field": "email", "evidence": "attendees[].email/displayName (person role: attendee)", "mutation": "DROP", "designated_substitutes": ["Event.organizer_email", "Event.creator_email"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:EventAttendee.optional", "kind": "A", "subkind": "state", "entity": "EventAttendee", "table": "calendar_event_attendees", "field": "optional", "evidence": "attendees[].optional", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.