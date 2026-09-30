Write scenario `G4-CAL-06` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Calendar.time_zone", "kind": "A", "subkind": "state", "entity": "Calendar", "table": "calendars", "field": "time_zone", "evidence": "calendar timeZone", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:Calendar.data_owner", "kind": "A", "subkind": "identity", "entity": "Calendar", "table": "calendars", "field": "data_owner", "evidence": "dataOwner; may differ from owner FK (C2)", "mutation": "DROP", "designated_substitutes": ["CalendarListEntry.access_role=owner", "AclRule owner scope", "Calendar.summary"], "suggested_families": ["F8", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.