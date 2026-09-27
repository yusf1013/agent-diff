# Google Calendar API: calendar-list

## GET /users/me/calendarList
Returns the calendars on the user's calendar list.

**Parameters:**
  path:
  query:
    - `maxResults` (integer, optional): Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries.
    - `minAccessRole` (string, optional): The minimum access role for the user in the returned entries. The default is no restriction. Acceptable values: 'freeBusyReader', 'owner', 'reader', 'writer'.
    - `pageToken` (string, optional): Token specifying which result page to return.
    - `showDeleted` (boolean, optional): Whether to include deleted calendar list entries in the result. The default is False.
    - `showHidden` (boolean, optional): Whether to show hidden entries. The default is False.
    - `syncToken` (string, optional): Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. Makes the result contain only entries that have changed since then. Cannot be specified together with minAccessRole.

## POST /users/me/calendarList
Inserts an existing calendar into the user's calendar list (subscribes to it). Used for adding shared calendars, public calendars, or resource calendars to your list.

**Parameters:**
  query:
    - `colorRgbFormat` (boolean, optional): Whether to use foregroundColor/backgroundColor fields (RGB hex) instead of colorId. Default: false.
  body:
    - `id` (string, **required**): Identifier of the calendar to subscribe to (calendar ID or email).
    - `colorId` (string, optional): Color ID (1-24) from the calendar colors palette.
    - `backgroundColor` (string, optional): Main color in hex format '#0088aa'. Requires colorRgbFormat=true.
    - `foregroundColor` (string, optional): Text color in hex format '#ffffff'. Requires colorRgbFormat=true.
    - `hidden` (boolean, optional): Whether to hide the calendar from the list. Default: false.
    - `selected` (boolean, optional): Whether calendar content shows in the UI. Default: false.
    - `summaryOverride` (string, optional): Custom display name for this calendar (user-specific).
    - `defaultReminders` (array, optional): Default reminders for events on this calendar.
    - `notificationSettings` (object, optional): Notification preferences for this calendar.

## PATCH /users/me/calendarList/{calendarId}
Updates an existing calendar on the user's calendar list. Supports patch semantics - only specified fields are updated. Consumes 3 quota units (prefer GET + UPDATE for efficiency).

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
  query:
    - `colorRgbFormat` (boolean, optional): Whether to use foregroundColor/backgroundColor fields (RGB hex). Default: false.
  body:
    - `colorId` (string, optional): Color ID (1-24) from the calendar colors palette.
    - `backgroundColor` (string, optional): Main color in hex format '#0088aa'. Requires colorRgbFormat=true.
    - `foregroundColor` (string, optional): Text color in hex format '#ffffff'. Requires colorRgbFormat=true.
    - `hidden` (boolean, optional): Whether to hide the calendar from the list.
    - `selected` (boolean, optional): Whether calendar content shows in the UI.
    - `summaryOverride` (string, optional): Custom display name for this calendar.
    - `defaultReminders` (array, optional): Default reminders. If specified, overwrites existing array.
    - `notificationSettings` (object, optional): Notification preferences.

## DELETE /users/me/calendarList/{calendarId}
Removes a calendar from the user's calendar list (unsubscribes). Does NOT delete the calendar itself - only removes it from the user's view. The calendar and its events remain intact for other users.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier to remove from the list.

## GET /users/me/calendarList/{calendarId}
Returns a specific calendar from the user's calendar list. Use this to check if a user is subscribed to a calendar and view their personalized settings for it (color, visibility, reminders, etc.).

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.

## PUT /users/me/calendarList/{calendarId}
Updates an existing calendar on the user's calendar list by fully replacing the entry. Unlike PATCH, unspecified fields may be reset to defaults. Use GET followed by PUT for atomic updates with etags.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier.
  query:
    - `colorRgbFormat` (boolean, optional): Whether to use backgroundColor/foregroundColor fields (true) or colorId field (false). Default: false.
  body:
    - `summaryOverride` (string, optional): User's custom title for this calendar.
    - `colorId` (string, optional): Color ID from calendar colors palette (1-24).
    - `backgroundColor` (string, optional): Background color as hex (#rrggbb). Requires colorRgbFormat=true.
    - `foregroundColor` (string, optional): Foreground color as hex (#rrggbb). Requires colorRgbFormat=true.
    - `hidden` (boolean, optional): Whether calendar is hidden from the list.
    - `selected` (boolean, optional): Whether calendar content is shown in the calendar UI.
    - `defaultReminders` (array, optional): Default reminders for events. Will be cleared if not specified.
    - `notificationSettings` (object, optional): Notification settings for the calendar.

## POST /users/me/calendarList/watch
Watch for changes to CalendarList resources. Receive push notifications when calendars are added, removed, or modified in the user's calendar list.

**Parameters:**
  path:
    None (account-wide)
  query:
    None
  body:
    - `id` (string, **required**): Unique channel ID (UUID recommended, max 64 chars). Must be unique across all channels.
    - `type` (string, **required**): Type of delivery mechanism. Must be 'web_hook'.
    - `address` (string, **required**): HTTPS URL where notifications are delivered. Must be registered in GCP Console.
    - `token` (string, optional): Arbitrary string for verification (max 256 chars). Returned in X-Goog-Channel-Token header.
    - `params` (object, optional):
