Write scenario `G4-CAL-05` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:CalendarListEntry.access_role", "kind": "A", "subkind": "state", "entity": "CalendarListEntry", "table": "calendar_list_entries", "field": "access_role", "evidence": "calendarList accessRole", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:CalendarListEntry.summary_override", "kind": "A", "subkind": "identity", "entity": "CalendarListEntry", "table": "calendar_list_entries", "field": "summary_override", "evidence": "calendarList summaryOverride vs calendar summary", "mutation": "DROP", "designated_substitutes": ["Calendar.summary"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:CalendarListEntry.hidden", "kind": "A", "subkind": "state", "entity": "CalendarListEntry", "table": "calendar_list_entries", "field": "hidden", "evidence": "calendarList hidden; showHidden", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.