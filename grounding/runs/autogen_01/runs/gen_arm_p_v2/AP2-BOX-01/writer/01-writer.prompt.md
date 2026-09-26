Write scenario `AP2-BOX-01` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Folder.size", "kind": "A", "subkind": "quantity", "entity": "Folder", "table": "box_folders", "field": "size", "evidence": "folder full", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F0"]}
{"id": "A:Folder.shared_link", "kind": "A", "subkind": "state", "entity": "Folder", "table": "box_folders", "field": "shared_link", "evidence": "folder full; present vs null", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:Folder.modified_at", "kind": "A", "subkind": "time", "entity": "Folder", "table": "box_folders", "field": "modified_at", "evidence": "folder full/item", "mutation": "DROP", "designated_substitutes": ["Folder.created_at"], "suggested_families": ["F7", "F6", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.