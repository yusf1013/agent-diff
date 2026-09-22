# Calendar model source ledger

Revision: `4691d3f076db2cdcccdc840c110aa797fa3196dc`. Scope and mapping discipline: [contextualization](contextualization.md). The full declaration/field index is [source_inventory.json](source_inventory.json), and reviewed decisions are [model.json](model.json).

## Persistence: forward coverage

| Source table | Disposition / destination | Field treatment and reason |
|---|---|---|
| `calendar_users` ([schema.py:104](../../../backend/src/services/calendar/database/schema.py)) | entity → User | Local account identity, email and display name, with a keyed setting-value collection. Identity: `id`; FK roles: —; stored values (including separately interpreted references): `email`, `display_name`, `self_`, `created_at`, `updated_at`. Exact declarations and constraints are in the inventory. |
| `calendars` ([schema.py:141](../../../backend/src/services/calendar/database/schema.py)) | entity → Calendar | Scheduling container with an owning local account and presentation settings. Identity: `id`; FK roles: `owner_id`; stored values (including separately interpreted references): `summary`, `description`, `location`, `time_zone`, `etag`, `conference_properties`, `auto_accept_invitations`, `data_owner`, `created_at`, `updated_at`, `deleted`. Exact declarations and constraints are in the inventory. |
| `calendar_list_entries` ([schema.py:193](../../../backend/src/services/calendar/database/schema.py)) | entity → CalendarListEntry | A user’s inclusion of a calendar in their list, with access role and per-user presentation/preferences. Identity: `id`; FK roles: `user_id`, `calendar_id`; stored values (including separately interpreted references): `etag`, `access_role`, `summary_override`, `description_override`, `color_id`, `background_color`, `foreground_color`, `hidden`, `selected`, `primary`, `deleted`, `default_reminders`, `notification_settings`, `created_at`, `updated_at`. Exact declarations and constraints are in the inventory. |
| `calendar_events` ([schema.py:258](../../../backend/src/services/calendar/database/schema.py)) | entity → Event | Scheduled record, recurring master, or persisted exception; virtual occurrences are derived Event representations. Identity: `id`; FK roles: `calendar_id`, `creator_id`, `organizer_id`; stored values (including separately interpreted references): `etag`, `status`, `html_link`, `summary`, `description`, `location`, `color_id`, `creator_email`, `organizer_email`, `creator_display_name`, `organizer_display_name`, `creator_profile_id`, `organizer_profile_id`, `creator_self`, `organizer_self`, `start`, `end`, `start_datetime`, `end_datetime`, `start_date`, `end_date`, `end_time_unspecified`, `recurrence`, `recurring_event_id`, `original_start_time`, `transparency`, `visibility`, `ical_uid`, `sequence`, `guests_can_invite_others`, `guests_can_modify`, `guests_can_see_other_guests`, `anyone_can_add_self`, `private_copy`, `locked`, `attendees_omitted`, `hangout_link`, `conference_data`, `attachments`, `extended_properties`, `source`, `gadget`, `reminders`, `event_type`, `working_location_properties`, `out_of_office_properties`, `focus_time_properties`, `birthday_properties`, `created_at`, `updated_at`. Exact declarations and constraints are in the inventory. |
| `calendar_event_attendees` ([schema.py:465](../../../backend/src/services/calendar/database/schema.py)) | entity → EventAttendee | Event-specific participation by an email-addressed person/resource, including RSVP state. Not necessarily a local User. Identity: `id`; FK roles: `event_id`; stored values (including separately interpreted references): `email`, `display_name`, `organizer`, `self_`, `resource`, `optional`, `response_status`, `comment`, `additional_guests`, `profile_id`. Exact declarations and constraints are in the inventory. |
| `calendar_event_reminders` ([schema.py:516](../../../backend/src/services/calendar/database/schema.py)) | entity → EventReminder | Stored event-owned reminder record (method and minutes). Separate from the JSON reminder policy used by API responses. Identity: `id`; FK roles: `event_id`; stored values (including separately interpreted references): `method`, `minutes`. Exact declarations and constraints are in the inventory. |
| `calendar_acl_rules` ([schema.py:544](../../../backend/src/services/calendar/database/schema.py)) | entity → AclRule | Calendar access grant to a tagged scope (default, user, group, domain); scope values are not local User foreign keys. Identity: `id`; FK roles: `calendar_id`; stored values (including separately interpreted references): `etag`, `role`, `scope_type`, `scope_value`, `created_at`, `updated_at`, `deleted`. Exact declarations and constraints are in the inventory. |
| `calendar_settings` ([schema.py:593](../../../backend/src/services/calendar/database/schema.py)) | folded_value → User | Unique (user, setting key) values; preserve record id/etag/presence in User.settings. All fields follow this disposition: `id`, `user_id`, `setting_id`, `value`, `etag`. Exact declarations and constraints are in the inventory. |
| `calendar_channels` ([schema.py:621](../../../backend/src/services/calendar/database/schema.py)) | deferred → Channel | Watch-subscription transport state or synchronization cursor; deferred to interface/behavior modeling, not a scheduling referent entity. All fields follow this disposition: `id`, `resource_id`, `resource_uri`, `type`, `address`, `expiration`, `token`, `params`, `payload`, `user_id`, `created_at`. Exact declarations and constraints are in the inventory. |
| `calendar_sync_tokens` ([schema.py:658](../../../backend/src/services/calendar/database/schema.py)) | deferred → SyncToken | Watch-subscription transport state or synchronization cursor; deferred to interface/behavior modeling, not a scheduling referent entity. All fields follow this disposition: `id`, `token`, `user_id`, `resource_type`, `resource_id`, `snapshot_time`, `expires_at`, `created_at`. Exact declarations and constraints are in the inventory. |

ORM reverse relationships are projections of these roles, not extra edges. The full relationship declarations remain in the inventory. Composite pair associations are contracted once; owner-value folds remove only the storage split, preserving all values. No table is silently omitted.

## API: forward coverage

The operation inventory expands HTTP dispatchers by verb or records each actual GraphQL binding. Each operation maps to the families below. Within each handler the inventory retains accessed input keys, constructed object keys, keyword arguments, attribute expressions and helper calls; follow these to the corresponding entity fields/representations. Transport arguments (pagination, cursors, formatting, field selection), error/success envelopes and execution preconditions/effects are deferred to interface/behavior analysis. None establishes another domain entity.

| Family | Domain-bearing inputs/outputs and treatment |
|---|---|
| Calendar metadata and list | Calendar ownership/presentation and current-user CalendarListEntry access/presentation/reminder values; primary alias is contextual identity, not a new entity. |
| Event operations | Event data, recurrence masters/derived occurrences, participants, structured properties and type/status values. Import UID lookup is scoped to calendar; moving preserves stored person fields. |
| ACL | Calendar grant role and tagged scope, with rule identity; scope strings are not User FKs. |
| Settings | Current User keyed settings and computed defaults; watch registration deferred. |
| Colors and free/busy | Fixed palettes and computed busy intervals; no independently stored palette/interval entity. |
| Watch and batch | Channel registration/cancellation, sync cursor and batch transport are accounted for but deferred from scheduling ER graph. |

| Registered operation/binding | Handler evidence |
|---|---|
| `POST /calendars` | `calendars_insert` — [methods.py:525](../../../backend/src/services/calendar/api/methods.py) |
| `GET /calendars/{calendarId}` | `calendars_get` — [methods.py:482](../../../backend/src/services/calendar/api/methods.py) |
| `PUT /calendars/{calendarId}` | `calendars_update` — [methods.py:568](../../../backend/src/services/calendar/api/methods.py) |
| `PATCH /calendars/{calendarId}` | `calendars_patch` — [methods.py:632](../../../backend/src/services/calendar/api/methods.py) |
| `DELETE /calendars/{calendarId}` | `calendars_delete` — [methods.py:698](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/clear` | `calendars_clear` — [methods.py:735](../../../backend/src/services/calendar/api/methods.py) |
| `GET /users/me/calendarList` | `calendar_list_list` — [methods.py:777](../../../backend/src/services/calendar/api/methods.py) |
| `POST /users/me/calendarList` | `calendar_list_insert` — [methods.py:876](../../../backend/src/services/calendar/api/methods.py) |
| `POST /users/me/calendarList/watch` | `calendar_list_watch` — [methods.py:1090](../../../backend/src/services/calendar/api/methods.py) |
| `GET /users/me/calendarList/{calendarId}` | `calendar_list_get` — [methods.py:836](../../../backend/src/services/calendar/api/methods.py) |
| `PUT /users/me/calendarList/{calendarId}` | `calendar_list_update` — [methods.py:929](../../../backend/src/services/calendar/api/methods.py) |
| `PATCH /users/me/calendarList/{calendarId}` | `calendar_list_patch` — [methods.py:987](../../../backend/src/services/calendar/api/methods.py) |
| `DELETE /users/me/calendarList/{calendarId}` | `calendar_list_delete` — [methods.py:1058](../../../backend/src/services/calendar/api/methods.py) |
| `GET /calendars/{calendarId}/events` | `events_list` — [methods.py:1153](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/events` | `events_insert` — [methods.py:1351](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/events/import` | `events_import` — [methods.py:1724](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/events/quickAdd` | `events_quick_add` — [methods.py:1878](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/events/watch` | `events_watch` — [methods.py:2023](../../../backend/src/services/calendar/api/methods.py) |
| `GET /calendars/{calendarId}/events/{eventId}/instances` | `events_instances` — [methods.py:1931](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/events/{eventId}/move` | `events_move` — [methods.py:1815](../../../backend/src/services/calendar/api/methods.py) |
| `GET /calendars/{calendarId}/events/{eventId}` | `events_get` — [methods.py:1294](../../../backend/src/services/calendar/api/methods.py) |
| `PUT /calendars/{calendarId}/events/{eventId}` | `events_update` — [methods.py:1450](../../../backend/src/services/calendar/api/methods.py) |
| `PATCH /calendars/{calendarId}/events/{eventId}` | `events_patch` — [methods.py:1574](../../../backend/src/services/calendar/api/methods.py) |
| `DELETE /calendars/{calendarId}/events/{eventId}` | `events_delete` — [methods.py:1685](../../../backend/src/services/calendar/api/methods.py) |
| `GET /calendars/{calendarId}/acl` | `acl_list` — [methods.py:2097](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/acl` | `acl_insert` — [methods.py:2204](../../../backend/src/services/calendar/api/methods.py) |
| `POST /calendars/{calendarId}/acl/watch` | `acl_watch` — [methods.py:2472](../../../backend/src/services/calendar/api/methods.py) |
| `GET /calendars/{calendarId}/acl/{ruleId}` | `acl_get` — [methods.py:2157](../../../backend/src/services/calendar/api/methods.py) |
| `PUT /calendars/{calendarId}/acl/{ruleId}` | `acl_update` — [methods.py:2284](../../../backend/src/services/calendar/api/methods.py) |
| `PATCH /calendars/{calendarId}/acl/{ruleId}` | `acl_patch` — [methods.py:2358](../../../backend/src/services/calendar/api/methods.py) |
| `DELETE /calendars/{calendarId}/acl/{ruleId}` | `acl_delete` — [methods.py:2432](../../../backend/src/services/calendar/api/methods.py) |
| `POST /channels/stop` | `channels_stop` — [methods.py:2546](../../../backend/src/services/calendar/api/methods.py) |
| `GET /colors` | `colors_get` — [methods.py:2588](../../../backend/src/services/calendar/api/methods.py) |
| `POST /freeBusy` | `freebusy_query` — [methods.py:2605](../../../backend/src/services/calendar/api/methods.py) |
| `GET /users/me/settings` | `settings_list` — [methods.py:2674](../../../backend/src/services/calendar/api/methods.py) |
| `POST /users/me/settings/watch` | `settings_watch` — [methods.py:2777](../../../backend/src/services/calendar/api/methods.py) |
| `GET /users/me/settings/{setting}` | `settings_get` — [methods.py:2718](../../../backend/src/services/calendar/api/methods.py) |
| `POST /batch/calendar/v3` | `batch_handler` — [batch.py:464](../../../backend/src/services/calendar/api/batch.py) |

The 37 batch aliases reuse the direct handlers; the additional registered batch operation is transport. Channel/SyncToken fields, channel response objects and nextSyncToken/watch metadata are deferred interface state. Defaults and virtual instances are derived values, with evidence in operations/serializers/utils.

## Validation scope

The completion audit below records both directions of review, corrections and remaining qualifications. Its manual source decisions are stored in model_audit.json; the earlier broad summary in model.json is not used as a substitute for those checks.

The modeling tools compare inventory with live ORM metadata, check all retained FK targets/cardinalities and operation mappings, and exercise risky serializer/GraphQL shapes offline. Mechanical accounting supplements the manual interpretation; it does not prove runtime correctness.

Route counting excludes repeated entity types, attributes, resolution modes and derived shortcuts. The read screen does not certify whole-route discovery, every attribute, permissions or ordinary-use meaningfulness. No ordinary-request inclusion review is claimed.

## Completion audit: explicit evidence mappings

Completed source-to-model accounting and model-to-source review for the frozen structural model, with the qualifications and validation limits below. No entity, stored attribute, relationship, or published route-count change was adopted.

This section supersedes the earlier broad audit summary. It records manual interpretation; inventories and checks establish accounting, not semantic correctness by themselves.

### Shared API field mappings

| ID | Source witness | Fields, disposition and model destination |
|---|---|---|
| C-A0 | [api/methods.py](../../../backend/src/services/calendar/api/methods.py) — `get_user_id; resolve_calendar_id; api_handler; request parsers` | **Represented:** actor → User; primary alias resolves an existing Calendar for that actor. calendarId/eventId/ruleId select the corresponding entities. **Deferred:** ETag headers, page/sync tokens, maxResults, sorting/time windows, sendUpdates, field/version/format controls and errors. Their being accepted does not imply every advertised effect is implemented. |
| C-A1 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_calendar`; [api/methods.py](../../../backend/src/services/calendar/api/methods.py) — `calendars_insert; calendars_update; calendars_patch` | **Represented:** id/etag/summary/description/location; timeZone → time_zone, conferenceProperties → conference_properties, autoAcceptInvitations → auto_accept_invitations, dataOwner → data_owner. **Derived/fixed:** absent conference properties become allowedConferenceSolutionTypes=[hangoutsMeet]; dataOwner may fall back to owner.email when calendar.id differs. This fallback does not equate arbitrary data_owner with owner_id. kind is a fixed discriminator. |
| C-A2 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_calendar_list_entry` | **Represented:** id is CalendarListEntry.calendar_id, not entry.id; accessRole/colorId/backgroundColor/foregroundColor/hidden/selected/primary/deleted/defaultReminders/notificationSettings/summaryOverride map to their snake_case entry fields. **Derived:** summary prefers summary_override, otherwise Calendar.summary; description/location/timeZone/conferenceProperties/autoAcceptInvitations/dataOwner come from Calendar. description_override is stored but unused here. **Fixed fallback:** colors #9fc6e7/#000000, hidden=false, selected=true, reminders=[], four email-notification kinds for primary entries without settings. No new Notification entity. |
| C-A3 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_event; _convert_time_object; _build_person_object` | **Represented:** id/etag/status/summary/description/location/colorId; created/updated → created_at/updated_at; htmlLink → html_link with generated URL fallback. creator/organizer email/displayName/id/self come from the separate *_email/*_display_name/*_profile_id/*_self fields, not local User FKs. start/end/originalStartTime are structured time values, optionally timezone-formatted. recurringEventId/recurrence retain master/occurrence meaning. iCalUID → ical_uid; sequence and guest/visibility/transparency/privateCopy/locked flags map to stored values with omission/default rules. |
| C-A4 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_event; serialize_attendee`; [database/operations.py](../../../backend/src/services/calendar/database/operations.py) — `create_event; update_event` | **Represented:** attendees are EventAttendee rows; email/responseStatus/displayName/organizer/resource/optional/comment/additionalGuests map to their fields. attendee.id is profile_id, not row id; self may derive from actor email as well as self_. **Derived:** maxAttendees truncation sets attendeesOmitted in addition to the stored flag. reminders, conferenceData, attachments, extendedProperties, source, gadget, hangoutLink and event-type properties remain Event structured/scalar values. Empty reminders serialize as useDefault=true; EventReminder rows are not the source. |
| C-A5 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_events_list; serialize_event_instances; serialize_calendar_list; serialize_acl_list; serialize_settings_list` | **Derived:** items are existing record projections; collection updated is maximum event.updated_at, falling back to current time; summary/description/timeZone/accessRole/defaultReminders come from the calendar/list/access context supplied by the caller. **Deferred:** collection etag, nextPageToken/nextSyncToken and kind are response/interface metadata. Instances reuse Event representation rather than establishing a separate entity type. |
| C-A6 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_acl_rule`; [api/methods.py](../../../backend/src/services/calendar/api/methods.py) — `acl_insert; acl_update; acl_patch` | **Represented:** rule id/etag/role; scope.type/value → scope_type/scope_value. Insert also accepts emailAddress as a scope-value fallback. User/group/domain/default are scope classifications, not guaranteed links to local User/group objects. **Deferred:** permission checking and ACL lifecycle. Group expansion is not implemented. |
| C-A7 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_setting; serialize_settings_list`; [api/methods.py](../../../backend/src/services/calendar/api/methods.py) — `settings_get; settings_list` | **Represented:** id is Setting.setting_id (the key), value and etag belong to the folded User.settings collection; the storage id is preserved separately. **Derived/fixed:** settings_get supplies virtual defaults for autoAddHangouts/dateFieldOrder/defaultEventLength/format24HourTime/hideInvitations/hideWeekends/locale/remindOnRespondedEventsOnly/showDeclinedEvents/timezone/useKeyboardShortcuts/weekStart when applicable; settings_list only returns stored settings. A default response does not prove a stored row exists. |
| C-A8 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_channel`; [api/methods.py](../../../backend/src/services/calendar/api/methods.py) — `calendar_list_watch; events_watch; acl_watch; settings_watch; channels_stop`; [api/batch.py](../../../backend/src/services/calendar/api/batch.py) — `batch_handler` | **Deferred:** Channel id/resourceId/resourceUri/type/address/expiration/token/params/payload and SyncToken cursor/resource/expiry state belong to interface/watch behavior. Batch wraps the registered operations and their same domain inputs/outputs; it adds no scheduling concept. Watch registration is not evidence of implemented push delivery. |
| C-A9 | [core/serializers.py](../../../backend/src/services/calendar/core/serializers.py) — `serialize_free_busy; serialize_colors`; [database/operations.py](../../../backend/src/services/calendar/database/operations.py) — `query_free_busy` | **Derived:** freeBusy timeMin/timeMax and calendars[id].busy start/end intervals from stored events; groups/errors are interface/compatibility structures, not a managed Group entity. The helper does not expand recurring masters. **Fixed:** calendar/event color IDs and background/foreground palette, kind and updated response values; they are display vocabulary, not independent color records. |
| C-A10 | [database/operations.py](../../../backend/src/services/calendar/database/operations.py) — `get_event_instances; move_event; import_event; quick_add_event`; [core/utils.py](../../../backend/src/services/calendar/core/utils.py) — `recurrence/time helpers` | **Derived:** recurring occurrences reuse Event plus originalStartTime/master references and generated instance IDs; persisted exceptions remain Event rows. quickAdd text derives event summary/timing rather than adding an NLP-plan entity. **Represented:** import iCalUID/eventType/sequence and organizer email/displayName payload. Move changes calendar_id without rewriting organizer payload/FK; documents describing organizer change are not authority. |

### Operation-to-field-group coverage

Every registered operation is assigned below. Shared response mappings are recorded once above. Operations retain their exact dispatch/source references in the preceding inventory.

| Operation | Applicable field mappings | Operation-specific qualification |
|---|---|---|
| `POST /calendars` | C-A0, C-A1 | Writes accept summary/description/location/timeZone; clear affects contained Events, not a new entity. |
| `GET /calendars/{calendarId}` | C-A0, C-A1 | Writes accept summary/description/location/timeZone; clear affects contained Events, not a new entity. |
| `PUT /calendars/{calendarId}` | C-A0, C-A1 | Writes accept summary/description/location/timeZone; clear affects contained Events, not a new entity. |
| `PATCH /calendars/{calendarId}` | C-A0, C-A1 | Writes accept summary/description/location/timeZone; clear affects contained Events, not a new entity. |
| `DELETE /calendars/{calendarId}` | C-A0, C-A1 | Writes accept summary/description/location/timeZone; clear affects contained Events, not a new entity. |
| `POST /calendars/{calendarId}/clear` | C-A0, C-A1 | Writes accept summary/description/location/timeZone; clear affects contained Events, not a new entity. |
| `GET /users/me/calendarList` | C-A0, C-A1, C-A2, C-A5 | Current actor scopes entries. Insert/update/patch forward presentation and reminder/notification preferences, not arbitrary Calendar fields. |
| `POST /users/me/calendarList` | C-A0, C-A1, C-A2, C-A5 | Current actor scopes entries. Insert/update/patch forward presentation and reminder/notification preferences, not arbitrary Calendar fields. |
| `POST /users/me/calendarList/watch` | C-A0, C-A8 | Domain fields use the listed shared mapping; CRUD preconditions and transport controls remain deferred. |
| `GET /users/me/calendarList/{calendarId}` | C-A0, C-A1, C-A2, C-A5 | Current actor scopes entries. Insert/update/patch forward presentation and reminder/notification preferences, not arbitrary Calendar fields. |
| `PUT /users/me/calendarList/{calendarId}` | C-A0, C-A1, C-A2, C-A5 | Current actor scopes entries. Insert/update/patch forward presentation and reminder/notification preferences, not arbitrary Calendar fields. |
| `PATCH /users/me/calendarList/{calendarId}` | C-A0, C-A1, C-A2, C-A5 | Current actor scopes entries. Insert/update/patch forward presentation and reminder/notification preferences, not arbitrary Calendar fields. |
| `DELETE /users/me/calendarList/{calendarId}` | C-A0, C-A1, C-A2, C-A5 | Current actor scopes entries. Insert/update/patch forward presentation and reminder/notification preferences, not arbitrary Calendar fields. |
| `GET /calendars/{calendarId}/events` | C-A0, C-A3, C-A4, C-A5 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `POST /calendars/{calendarId}/events` | C-A0, C-A3, C-A4, C-A5 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `POST /calendars/{calendarId}/events/import` | C-A0, C-A3, C-A4, C-A5, C-A10 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `POST /calendars/{calendarId}/events/quickAdd` | C-A0, C-A3, C-A4, C-A5, C-A10 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `POST /calendars/{calendarId}/events/watch` | C-A0, C-A8 | Domain fields use the listed shared mapping; CRUD preconditions and transport controls remain deferred. |
| `GET /calendars/{calendarId}/events/{eventId}/instances` | C-A0, C-A3, C-A4, C-A5, C-A10 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `POST /calendars/{calendarId}/events/{eventId}/move` | C-A0, C-A3, C-A4, C-A5, C-A10 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `GET /calendars/{calendarId}/events/{eventId}` | C-A0, C-A3, C-A4, C-A5 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `PUT /calendars/{calendarId}/events/{eventId}` | C-A0, C-A3, C-A4, C-A5 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `PATCH /calendars/{calendarId}/events/{eventId}` | C-A0, C-A3, C-A4, C-A5 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `DELETE /calendars/{calendarId}/events/{eventId}` | C-A0, C-A3, C-A4, C-A5 | calendarId/eventId select Event context; read controls include recurrence/time windows and attendee truncation. Per-operation write whitelists differ; a serialized field is not automatically writable. |
| `GET /calendars/{calendarId}/acl` | C-A0, C-A6, C-A5 | calendarId/ruleId select scope; insert provides role and scope, update/patch only role. |
| `POST /calendars/{calendarId}/acl` | C-A0, C-A6, C-A5 | calendarId/ruleId select scope; insert provides role and scope, update/patch only role. |
| `POST /calendars/{calendarId}/acl/watch` | C-A0, C-A8 | Domain fields use the listed shared mapping; CRUD preconditions and transport controls remain deferred. |
| `GET /calendars/{calendarId}/acl/{ruleId}` | C-A0, C-A6, C-A5 | calendarId/ruleId select scope; insert provides role and scope, update/patch only role. |
| `PUT /calendars/{calendarId}/acl/{ruleId}` | C-A0, C-A6, C-A5 | calendarId/ruleId select scope; insert provides role and scope, update/patch only role. |
| `PATCH /calendars/{calendarId}/acl/{ruleId}` | C-A0, C-A6, C-A5 | calendarId/ruleId select scope; insert provides role and scope, update/patch only role. |
| `DELETE /calendars/{calendarId}/acl/{ruleId}` | C-A0, C-A6, C-A5 | calendarId/ruleId select scope; insert provides role and scope, update/patch only role. |
| `POST /channels/stop` | C-A0, C-A8 | Domain fields use the listed shared mapping; CRUD preconditions and transport controls remain deferred. |
| `GET /colors` | C-A0, C-A9 | freeBusy items[].id identifies calendars; fixed color palettes carry no persistent identities. |
| `POST /freeBusy` | C-A0, C-A9 | freeBusy items[].id identifies calendars; fixed color palettes carry no persistent identities. |
| `GET /users/me/settings` | C-A0, C-A7, C-A5 | Actor plus setting key identifies the folded value; no general settings write endpoint. |
| `POST /users/me/settings/watch` | C-A0, C-A8 | Domain fields use the listed shared mapping; CRUD preconditions and transport controls remain deferred. |
| `GET /users/me/settings/{setting}` | C-A0, C-A7, C-A5 | Actor plus setting key identifies the folded value; no general settings write endpoint. |
| `POST /batch/calendar/v3` | C-A0, C-A8 | Domain fields use the listed shared mapping; CRUD preconditions and transport controls remain deferred. |

### Model-to-source checks

| Model elements | Source and concrete check | Result / qualification |
|---|---|---|
| All seven entity definitions, 10 table dispositions and 140 columns | schema.py definitions and source inventory; compare each PK/FK/value, composite constraint and enum with metadata; C-A1–C-A10 follow API meaning. | Global Event.id retained; no local Person/Group/File invented from email/scope/attachment values. Settings fold and Channel/SyncToken deferrals have explicit field destinations. |
| Ten relationships and both-end cardinalities | Nine retained FKs; recurring_event_id is interpreted by recurrence helpers but not a database FK. Required/optional targets follow nullability; inverse uniqueness checked against composite constraints. | No local-User relationship inferred from creator/organizer/attendee profile payload. ACL nullable scope_value uniqueness is qualified; an absent owner setting differs from a present null value. |
| Every diagram edge and identity participation | All retained records have their own id PK; none of the retained FKs contributes to that PK. | Corrected dashed non-identifying notation without changing edges or cardinalities. |
| Setting fold; reminder distinction; transport deferrals | C-A4/C-A7/C-A8 trace actual serializer and writer sources. User.settings is keyed by unique (user_id,setting_id); EventReminder remains independently identified. | No conflation of Setting.id with API key, attendee.id with row identity, or Event.reminders JSON with EventReminder table. Deferred transport records remain fully inventoried. |
| C1–C8 qualifications and all derived representations | C-A1–C-A10 plus stored schema; verify aliases, copied/fallback values, recurring instances and free/busy computation. | Calendar.dataOwner and person payloads are not certificates of their local FK values. Snapshot versus computed fields and actor scope are recorded explicitly. |
| Eight enums and open structured classifications | schema AccessRole/EventStatus/EventTransparency/EventVisibility/EventType/AttendeeResponseStatus/AclScopeType/ReminderMethod; handlers/serializers apply _enum_value and defaults. | Values belong to existing entities/attributes; transitions and advertised permission enforcement are not inferred. Structured notification kinds, conference solution defaults and color IDs are values/constants, not new graph nodes. |
| Calendar migration/metadata agreement | 2ac6c433442a_add_calendar_tables.py table/column sets compared with current ORM SQL names; 3d8f1e2a4b5c adds Channel.user_id; a1b2c3d4e5f6 only adds nonunique query indexes. Seeder creates Base.metadata. | Every current table/column is accounted for; Channel.user_id is already in the deferred transport record. No additional domain structure found. |

### Findings and approval boundary

- Diagram notation corrected without changing counts.
- Newly explicit identity qualifications: serialized attendee.id is profile_id; serialized Setting.id is setting_id; list-entry id is calendar_id. All corresponding stored fields already exist in the model.
- API fallback defaults are not persisted records. Interface watch/batch/token machinery remains deferred under the same abstraction rule used for Slack.
