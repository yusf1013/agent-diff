# Google Calendar API: calendars

## GET /calendars/{calendarId}
Returns metadata for a calendar.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.
  query:

## POST /calendars
Creates a secondary calendar. The authenticated user for the request is made the data owner of the new calendar.

**Parameters:**
  path:
  query:
  body:
    - `summary` (string, **required**): Title of the calendar.

## PATCH /calendars/{calendarId}
Updates metadata for a calendar (summary, description, location, timezone). Supports patch semantics - only specified fields are updated. Consumes 3 quota units (prefer GET + UPDATE for efficiency).

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
  body:
    - `summary` (string, optional): Title of the calendar.
    - `description` (string, optional): Description of the calendar.
    - `location` (string, optional): Geographic location as free-form text.
    - `timeZone` (string, optional): IANA timezone identifier (e.g., 'Europe/Warsaw', 'Asia/Kolkata').

## DELETE /calendars/{calendarId}
Permanently deletes a secondary calendar. Cannot delete primary calendar - use calendars.clear to remove all events from primary instead. This action is irreversible and removes the calendar for all users who have access.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Cannot be 'primary' - primary calendars cannot be deleted.

## POST /calendars/{calendarId}/clear
Clears a calendar by deleting all events associated with it. The calendar itself is preserved. Designed primarily for primary calendars.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the authenticated user's primary calendar.
  body:
    None - do not supply a request body

## PUT /calendars/{calendarId}
Updates metadata for a calendar by fully replacing it. Unlike PATCH, this replaces the entire calendar metadata. Unspecified fields may be reset to defaults.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier.
  query:
    None
  body:
    - `summary` (string, **required**): Title of the calendar.
    - `description` (string, optional): Description of the calendar.
    - `location` (string, optional): Geographic location of the calendar.
    - `timeZone` (string, optional): IANA timezone (e.g., 'America/Los_Angeles').
