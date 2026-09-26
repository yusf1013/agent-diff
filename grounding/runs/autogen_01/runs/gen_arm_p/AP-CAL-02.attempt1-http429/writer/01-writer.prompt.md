Write scenario `AP-CAL-02` for the calendar domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:CalendarListEntry.calendar_id", "kind": "R", "roles": ["CalendarListEntry.calendar_id"], "meaning": "calendar on the actor's calendar list", "mutation": "SUB_OR_DROP", "designated_substitutes": ["ACL grant on the calendar", "Calendar.data_owner"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "B:AclRule.calendar_id", "kind": "B", "meaning": "scope and role conditions hold on one grant", "parent": "Calendar", "child": "AclRule", "mutation": "SPLIT", "designated_substitutes": [], "suggested_families": ["F5"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.