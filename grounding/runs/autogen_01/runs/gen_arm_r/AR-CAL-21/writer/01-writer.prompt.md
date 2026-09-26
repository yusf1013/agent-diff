Write scenario `AR-CAL-21` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Event.description", "kind": "A", "subkind": "text", "entity": "Event", "table": "calendar_events", "field": "description", "evidence": "event description; q", "mutation": "DROP", "designated_substitutes": ["Event.location"], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:Event.end", "kind": "A", "subkind": "time", "entity": "Event", "table": "calendar_events", "field": "end", "evidence": "end.dateTime/date", "mutation": "DROP", "designated_substitutes": ["Event.start"], "suggested_families": ["F7", "F6", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.