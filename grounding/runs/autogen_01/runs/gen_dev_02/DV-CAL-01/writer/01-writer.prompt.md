Write scenario `DV-CAL-01` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Event.status", "kind": "A", "subkind": "state", "entity": "Event", "table": "calendar_events", "field": "status", "evidence": "event status; cancelled visible with showDeleted", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:Event.hangout_link", "kind": "A", "subkind": "state", "entity": "Event", "table": "calendar_events", "field": "hangout_link", "evidence": "video link present", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:EventAttendee.resource", "kind": "A", "subkind": "state", "entity": "EventAttendee", "table": "calendar_event_attendees", "field": "resource", "evidence": "attendees[].resource (room)", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.