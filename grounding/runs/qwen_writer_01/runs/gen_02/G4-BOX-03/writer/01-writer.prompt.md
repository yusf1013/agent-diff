Write scenario `G4-BOX-03` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:File.shared_link", "kind": "A", "subkind": "state", "entity": "File", "table": "box_files", "field": "shared_link", "evidence": "file full; present vs null", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:File.uploader_display_name", "kind": "A", "subkind": "identity", "entity": "File", "table": "box_files", "field": "uploader_display_name", "evidence": "file full; stored name snapshot, not a User role", "mutation": "DROP", "designated_substitutes": ["File.name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:File.modified_at", "kind": "A", "subkind": "time", "entity": "File", "table": "box_files", "field": "modified_at", "evidence": "file full/item", "mutation": "DROP", "designated_substitutes": ["File.created_at"], "suggested_families": ["F7", "F6", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.