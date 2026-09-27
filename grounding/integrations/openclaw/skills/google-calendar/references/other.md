# Google Calendar API: other

## POST /freeBusy
Returns free/busy information for a set of calendars.

**Parameters:**
  path:
  query:
  body:
    - `timeMin` (datetime, optional): The start of the interval for the query formatted as per RFC3339.
    - `timeMax` (datetime, optional): The end of the interval for the query formatted as per RFC3339.
    - `timeZone` (string, optional): Time zone used in the response. The default is UTC.
    - `groupExpansionMax` (integer, optional): Maximal number of calendar identifiers to be provided for a single group. An error is returned for a group with more members than this value. Maximum value is 100.
    - `calendarExpansionMax` (integer, optional): Maximal number of calendars for which FreeBusy information is to be provided. Maximum value is 50.
    - `items` (array, optional): List of calendars and/or groups to query.

## GET /users/me/settings/{setting}
Returns a single user setting by ID. Settings with default values may not be returned.

**Parameters:**
  path:
    - `setting` (string, **required**): Setting ID. Valid values: autoAddHangouts, dateFieldOrder, defaultEventLength, format24HourTime, hideInvitations, hideWeekends, locale, remindOnRespondedEventsOnly, showDeclinedEvents, timezone, useKeyboardShortcuts, weekStart.

## POST /users/me/settings/watch
Watch for changes to user Settings resources. Creates a notification channel that sends push notifications to a webhook URL when settings change. Channels expire (typically ~1 week) and must be renewed.

**Parameters:**
  body:
    - `id` (string, **required**): Unique channel identifier (UUID recommended). Max 64 characters. Echoed in X-Goog-Channel-Id header of notifications.
    - `type` (string, **required**): Must be 'web_hook'.
    - `address` (string, **required**): HTTPS URL to receive notifications. Must have valid SSL certificate.
    - `token` (string, optional): Arbitrary string (max 256 chars) for validation/routing. Echoed in X-Goog-Channel-Token header.
    - `expiration` (long, optional): Unix timestamp (ms) when channel should expire. Server may impose earlier expiration.
    - `params` (object, optional):

## GET /users/me/settings
Returns all user settings for the authenticated user. Settings represent preferences users can change from the Calendar UI, such as timezone, locale, and display options. Note: Settings with default values might not be returned.

**Parameters:**
  query:
    - `maxResults` (integer, optional): Maximum number of settings to return.
    - `pageToken` (string, optional): Token for retrieving next page of results.
    - `syncToken` (string, optional): Token for incremental sync. Returns only settings changed since last sync.

## GET /colors
Returns the color definitions for calendars and events. Provides both calendar colors (for calendarList entries) and event colors (for individual events).

**Parameters:**
  path:
    None
  query:
    None
  body:
    None

## POST /channels/stop
Stop watching resources through a notification channel. Use to cancel push notifications when no longer needed or before channel expiration.

**Parameters:**
  path:
    None
  query:
    None
  body:
    - `id` (string, **required**): The channel ID you specified when creating the watch.
    - `resourceId` (string, **required**): The resourceId returned by the watch method when the channel was created.
