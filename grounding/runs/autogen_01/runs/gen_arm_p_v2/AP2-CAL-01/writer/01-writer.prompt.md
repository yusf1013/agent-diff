Write scenario `AP2-CAL-01` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Calendar.summary", "kind": "A", "subkind": "identity", "entity": "Calendar", "table": "calendars", "field": "summary", "evidence": "calendars.get/calendarList summary", "mutation": "DROP", "designated_substitutes": ["Calendar.data_owner"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:CalendarListEntry.selected", "kind": "A", "subkind": "state", "entity": "CalendarListEntry", "table": "calendar_list_entries", "field": "selected", "evidence": "calendarList selected", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.