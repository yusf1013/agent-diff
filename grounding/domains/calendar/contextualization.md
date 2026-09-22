# Calendar modeling contextualization

Apply [the adopted protocol](../../protocols/conceptual_meta_model.md) to repository revision `4691d3f076db2cdcccdc840c110aa797fa3196dc`. Scope is the implemented replica, including stored but unexposed concepts; source-based modeling does not certify runtime correctness.

Authoritative persistence: [database/schema.py](../../../backend/src/services/calendar/database/schema.py), its Base and template creation. Registered operations come from [api/__init__.py](../../../backend/src/services/calendar/api/__init__.py), which combines [methods.py](../../../backend/src/services/calendar/api/methods.py) and [batch.py](../../../backend/src/services/calendar/api/batch.py). Expand multi-method dispatchers to their verb-specific handlers. Follow [operations.py](../../../backend/src/services/calendar/database/operations.py), [serializers.py](../../../backend/src/services/calendar/core/serializers.py), and [utils.py](../../../backend/src/services/calendar/core/utils.py). Supporting documentation: [local API document](../../../examples/calendar/testsuites/calendar_docs/calendar_api_full_docs.json).

Required contextual distinctions:

- Enumerate metadata, not seed insertion lists. Watch channels and sync tokens must receive explicit ledger dispositions even where they are interface infrastructure rather than scheduling entities.
- Batch routes are aliases to existing handlers, not new domain concepts. Check their registry against direct routes rather than double-counting operations.
- Stored Event identity is a global primary key; URL calendar scope does not establish a composite database key. CalendarListEntry's internal ID differs from the calendar ID returned by its serializer.
- Creator/organizer User foreign keys and the separately stored person payloads can disagree. Serialization uses the payload fields, not a join through those foreign keys. Attendee email and ACL scope values do not enforce membership in the local User table.
- Recurring occurrences may be virtual or persisted exceptions. Preserve the master relationship and original start while treating virtual instances as a derived representation of Event, not a new independent entity type.
- Structured reminders, conferencing, attachments, guest settings and type-specific properties are values. A referenced external file does not imply a managed local File entity. The separate reminder table must not be conflated with the JSON reminder policy actually serialized.
- User settings are an owner-indexed set of setting values. Retain stored record identity/presence in the ledger while folding that value collection into User; API setting keys are not independently related domain objects.

These specialize existing protocol mappings; the generic protocol remains unchanged. The public-service `grounding/google-calendar.md` draft is not an implementation model.

Database-definition cross-checks also cover the migrations for
[Calendar tables](../../../backend/src/platform/db/migrations/versions/2ac6c433442a_add_calendar_tables.py),
[watch-channel ownership](../../../backend/src/platform/db/migrations/versions/3d8f1e2a4b5c_add_channel_user_id.py),
and [query indexes](../../../backend/src/platform/db/migrations/versions/a1b2c3d4e5f6_calendar_composite_indexes.py).
Their column sets agree with current metadata after the ownership addition;
the extra indexes are nonunique. The [seeder](../../../backend/utils/seed_calendar_template.py)
creates the full metadata, rather than defining the model by populated rows.
These checks and their source hashes are recorded in the completion audit.
