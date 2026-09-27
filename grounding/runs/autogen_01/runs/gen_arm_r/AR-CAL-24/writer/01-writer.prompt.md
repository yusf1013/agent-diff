Write scenario `AR-CAL-24` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Calendar.location", "kind": "A", "subkind": "text", "entity": "Calendar", "table": "calendars", "field": "location", "evidence": "calendar", "mutation": "DROP", "designated_substitutes": ["Calendar.description"], "suggested_families": ["F1", "F2", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.