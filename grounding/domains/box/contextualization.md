# Box modeling contextualization

Apply [the adopted protocol](../../protocols/conceptual_meta_model.md) to repository revision `4691d3f076db2cdcccdc840c110aa797fa3196dc`. Scope is the implemented replica, not production Box or just populated benchmark records. This is source analysis, not a certification of runtime behavior.

Authoritative persistence: [database/schema.py](../../../backend/src/services/box/database/schema.py), its service Base, and template creation. Enumerate all metadata tables, including content, versions and assignments. Follow [api/routes.py](../../../backend/src/services/box/api/routes.py)'s registered `routes` through [database/operations.py](../../../backend/src/services/box/database/operations.py), including each called serializer on the ORM classes. Supporting documentation is [the local API document](../../../examples/box/testsuites/box_docs/box_api_full_docs.json). The platform mounts this router at `/services/box/2.0`; platform environment records are outside the domain.

Required contextual distinctions:

- Structured JSON remains an attribute unless implementation interprets it as a relationship. File/folder collection IDs are actually queried as collection membership, so foreign keys alone are not a complete relationship inventory.
- `HubItem.item_type/item_id` and `Comment.item_type/item_id` are interpreted tagged references, not unconstrained links to every modeled entity. Preserve subtype conditions and absence of FK enforcement.
- Fold the unique version-owned binary content record into an optional FileVersion content value, retaining record presence, MIME type, and implementation identity. Do not add a graph node for a storage split with no independent domain lifecycle.
- Follow the serializer actually called. A defined `to_full_dict` method or database helper does not establish a dispatched read operation. Mini users, versions, and hub items expose only subsets of their stored records.
- Folder ancestor paths and the selected latest version are derived representations. Keep separately stored cached values when storage does not enforce equivalence; do not infer extra independent domain entities from response wrappers.
- Enum declarations, shared-link permissions and collaboration flags do not establish collaboration/group APIs or enforcement. Account for their stored or represented meaning without importing the public-service model.

These specialize existing protocol mappings; the generic protocol is unchanged. The earlier `grounding/box.md` public-service draft is not the authority for this extraction.
