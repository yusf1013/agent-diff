# Google Calendar API: events-2

## GET /calendars/{calendarId}/events
Returns events on the specified calendar.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.
  query:
    - `alwaysIncludeEmail` (boolean, optional): Deprecated and ignored.
    - `eventTypes` (string, optional): Event types to return. Can be repeated multiple times. Acceptable values: 'birthday', 'default', 'focusTime', 'fromGmail', 'outOfOffice', 'workingLocation'. If unset, returns all event types.
    - `iCalUID` (string, optional): Specifies an event ID in the iCalendar format to be provided in the response. Use this to search for an event by its iCalendar ID.
    - `maxAttendees` (integer, optional): The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned.
    - `maxResults` (integer, optional): Maximum number of events returned on one result page. By default the value is 250 events. The page size can never be larger than 2500 events.
    - `orderBy` (string, optional): The order of the events returned in the result. Acceptable values: 'startTime' (only available when singleEvents is True), 'updated'. The default is an unspecified, stable order.
    - `pageToken` (string, optional): Token specifying which result page to return.
    - `privateExtendedProperty` (string, optional): Extended properties constraint specified as propertyName=value. Matches only private properties. Can be repeated multiple times.
    - `q` (string, optional): Free text search terms to find events that match these terms in fields like summary, description, location, attendee's displayName/email, organizer's displayName/email, and working location properties.
    - `sharedExtendedProperty` (string, optional): Extended properties constraint specified as propertyName=value. Matches only shared properties. Can be repeated multiple times.
    - `showDeleted` (boolean, optional): Whether to include deleted events (with status equals 'cancelled') in the result. The default is False.
    - `showHiddenInvitations` (boolean, optional): Whether to include hidden invitations in the result. The default is False.
    - `singleEvents` (boolean, optional): Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. The default is False.
    - `syncToken` (string, optional): Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. Makes the result contain only entries that have changed since then. Cannot be used with iCalUID, orderBy, privateExtendedProperty, q, sharedExtendedProperty, timeMin, timeMax, or updatedMin.
    - `timeMax` (datetime, optional): Upper bound (exclusive) for an event's start time to filter by. Must be an RFC3339 timestamp with mandatory time zone offset. If timeMin is set, timeMax must be greater than timeMin.
    - `timeMin` (datetime, optional): Lower bound (exclusive) for an event's end time to filter by. Must be an RFC3339 timestamp with mandatory time zone offset. If timeMax is set, timeMin must be smaller than timeMax.
    - `timeZone` (string, optional): Time zone used in the response. The default is the time zone of the calendar.
    - `updatedMin` (datetime, optional): Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted.

## DELETE /calendars/{calendarId}/events/{eventId}
Deletes an event.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.
    - `eventId` (string, **required**): Event identifier.
  query:
    - `sendNotifications` (boolean, optional): Deprecated. Please use sendUpdates instead. Whether to send notifications about the deletion of the event. The default is false.
    - `sendUpdates` (string, optional): Guests who should receive notifications about the deletion of the event.

## GET /calendars/{calendarId}/events/{eventId}/instances
Returns instances of a specified recurring event. Use this to get individual occurrences that can then be modified (creating exceptions) or cancelled. Each instance has its own ID for PATCH/DELETE operations.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
    - `eventId` (string, **required**): Recurring event identifier (the parent event ID, not an instance ID).
  query:
    - `timeMin` (datetime, optional): Lower bound (exclusive) for instance start time. RFC3339 timestamp.
    - `timeMax` (datetime, optional): Upper bound (exclusive) for instance start time. RFC3339 timestamp.
    - `timeZone` (string, optional): IANA timezone for times in response. Defaults to calendar timezone.
    - `maxResults` (integer, optional): Maximum number of instances to return.
    - `pageToken` (string, optional): Token for retrieving next page of results.
    - `showDeleted` (boolean, optional): Whether to include cancelled instances. Default: false.
    - `originalStart` (string, optional): Original start time of specific instance to retrieve.
    - `maxAttendees` (integer, optional): Maximum attendees to include per instance.

## POST /calendars/{calendarId}/events/import
Imports an event by adding a private copy of an existing event to a calendar. Used for calendar migration and syncing with external calendaring systems. Unlike 'insert', requires an iCalUID and preserves the event's identity across systems. Only events with eventType 'default' may be imported.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
  query:
    - `conferenceDataVersion` (integer, optional): Version of conference data supported. 0 = no support (default), 1 = enables ConferenceData copying/creation. Values: 0-1.
    - `supportsAttachments` (boolean, optional): Whether client supports event attachments. Default: false.
  body:
    - `iCalUID` (string, **required**): Event unique identifier as defined in RFC5545. Used to uniquely identify events across calendaring systems. Must be supplied when importing. Note: iCalUID and id are not identical - in recurring events, all occurrences share the same iCalUID but have different ids.
    - `start` (object, **required**): Start time of the event.
    - `end` (object, **required**): End time of the event.
    - `summary` (string, optional): Title of the event.
    - `description` (string, optional): Description of the event. Can contain HTML.
    - `location` (string, optional): Geographic location as free-form text.
    - `organizer` (object, optional): Event organizer. Writable only when importing (read-only for insert/update).
    - `attendees` (array, optional): List of attendees.
    - `recurrence` (array, optional): RRULE, EXRULE, RDATE, EXDATE lines per RFC5545 for recurring events.
    - `sequence` (integer, optional): Sequence number as per iCalendar specification.
    - `status` (string, optional): Event status: 'confirmed' (default), 'tentative', 'cancelled'.
    - `transparency` (string, optional): Whether event blocks time: 'opaque' (busy, default), 'transparent' (available).
    - `visibility` (string, optional): Visibility: 'default', 'public', 'private', 'confidential'.
    - `colorId` (string, optional): Color ID from the event colors definition (1-11).
    - `reminders` (object, optional): Reminder settings.

## PUT /calendars/{calendarId}/events/{eventId}
Updates an event by fully replacing the entire event resource. Does NOT support patch semantics - always updates the entire event. Unspecified fields will be cleared/reset. For partial updates, use PATCH or perform GET followed by UPDATE with etags for atomicity.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
    - `eventId` (string, **required**): Event identifier.
  query:
    - `sendUpdates` (string, optional): Who receives notifications: 'all', 'externalOnly', 'none'.
    - `sendNotifications` (boolean, optional): Deprecated. Use sendUpdates instead.
    - `maxAttendees` (integer, optional): Max attendees to include in response.
    - `conferenceDataVersion` (integer, optional): Conference data version: 0 (no support) or 1 (enabled). Default: 0.
    - `supportsAttachments` (boolean, optional): Whether client supports attachments. Default: false.
  body:
    - `start` (object, **required**): Start time (required for full replace).
    - `end` (object, **required**): End time (required for full replace).
    - `summary` (string, optional): Event title. Will be cleared if not provided.
    - `description` (string, optional): Event description. Will be cleared if not provided.
    - `location` (string, optional): Event location. Will be cleared if not provided.
    - `colorId` (string, optional): Event color ID.
    - `attendees` (array, optional): Attendee list. Will be cleared if not provided.
    - `recurrence` (array, optional): RRULE lines for recurring events.
    - `reminders` (object, optional): Reminder settings.
    - `visibility` (string, optional): Visibility: 'default', 'public', 'private', 'confidential'.
    - `transparency` (string, optional): 'opaque' (busy) or 'transparent' (available).
    - `status` (string, optional): 'confirmed', 'tentative', 'cancelled'.

## POST /calendars/{calendarId}/events/quickAdd
Creates an event based on a simple text string using natural language parsing. Google parses the text to extract event details like title, date, time, and duration. Useful for quick event creation without structured data.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
  query:
    - `text` (string, **required**): The text describing the event to be created. Examples: 'Dinner with John tomorrow at 7pm', 'Meeting June 28 at 9:30am for 30 minutes', 'Team standup every Monday at 9am'.
    - `sendUpdates` (string, optional): Who receives notifications: 'all', 'externalOnly', 'none'.
    - `sendNotifications` (boolean, optional): Deprecated. Use sendUpdates instead.

## POST /calendars/{calendarId}/events/watch
Creates a notification channel to watch for changes to events on a calendar. When events are created, updated, or deleted, Google sends a POST to your webhook URL. Notifications indicate something changed but don't include event details - use incremental sync to fetch changes.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
  query:
    - `eventTypes` (array, optional): Filter to specific event types: 'default', 'focusTime', 'outOfOffice', 'workingLocation', 'fromGmail'.
  body:
    - `id` (string, **required**): Unique channel identifier (UUID recommended). Max 64 characters.
    - `type` (string, **required**): Must be 'web_hook'.
    - `address` (string, **required**): HTTPS URL to receive notifications. Must be registered in Google Cloud Console.
    - `token` (string, optional): Arbitrary string sent with notifications for verification. Max 256 characters.
    - `expiration` (long, optional): Unix timestamp (ms) when channel expires. Default ~1 week.
    - `params` (object, optional): Additional parameters.
