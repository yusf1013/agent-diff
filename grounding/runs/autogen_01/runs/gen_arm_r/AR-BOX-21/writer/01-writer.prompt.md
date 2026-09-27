Write scenario `AR-BOX-21` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Folder.created_at", "kind": "A", "subkind": "time", "entity": "Folder", "table": "box_folders", "field": "created_at", "evidence": "folder full/item", "mutation": "DROP", "designated_substitutes": ["Folder.modified_at"], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "R:Folder.modified_by_id", "kind": "R", "roles": ["Folder.modified_by_id"], "meaning": "folder last modifier", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Folder.owned_by_id", "Folder.created_by_id"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "R:Folder.collections", "kind": "R", "roles": ["Folder.collections"], "meaning": "folder in collection", "mutation": "SUB_OR_DROP", "designated_substitutes": ["a file inside the folder is in the collection"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "D:Folder.item_count", "kind": "D", "meaning": "folder item count (item_collection.total_count)", "mutation": "VIEW", "designated_substitutes": ["recursive vs direct count; files vs all items"], "suggested_families": ["F6", "F7", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.