# Google Calendar API: events-3

## POST /calendars/{calendarId}/events/{eventId}/move
Moves an event to another calendar, changing the event's organizer to the destination calendar owner. Only default events can be moved; birthday, focusTime, fromGmail, outOfOffice, and workingLocation events cannot be moved.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier of the SOURCE calendar where the event currently resides.
    - `eventId` (string, **required**): Event identifier to move.
  query:
    - `destination` (string, **required**): Calendar identifier of the TARGET calendar where the event will be moved to.
    - `sendUpdates` (string, optional): Guests who should receive notifications about the move.
