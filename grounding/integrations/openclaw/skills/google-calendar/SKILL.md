---
name: google-calendar
description: "Google Calendar scheduling and events API. Use it for anything in the user's Google Calendar account."
metadata: {"openclaw": {"requires": {"bins": ["curl"]}}}
---

# Google Calendar

## Current Session
- **Service**: Google Calendar
- **Base URL**: https://www.googleapis.com/calendar/v3
- **Description**: Google Calendar scheduling and events API

## Environment
- You are authenticated as a user in the Google Calendar workspace/account.
- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.
- You execute bash commands (primarily curl) to interact with the Google Calendar API.

## API Documentation
The endpoint documentation is split by resource into the files below (in this skill's `references/` folder). Read the file for the resource you need.

- `references/events-1.md`: GET /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events; PATCH /calendars/{calendarId}/events/{eventId}
- `references/events-2.md`: GET /calendars/{calendarId}/events; DELETE /calendars/{calendarId}/events/{eventId}; GET /calendars/{calendarId}/events/{eventId}/instances; POST /calendars/{calendarId}/events/import; PUT /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events/quickAdd; POST /calendars/{calendarId}/events/watch
- `references/events-3.md`: POST /calendars/{calendarId}/events/{eventId}/move
- `references/acl.md`: POST /calendars/{calendarId}/acl; GET /calendars/{calendarId}/acl; DELETE /calendars/{calendarId}/acl/{ruleId}; GET /calendars/{calendarId}/acl/{ruleId}; PATCH /calendars/{calendarId}/acl/{ruleId}; PUT /calendars/{calendarId}/acl/{ruleId}; POST /calendars/{calendarId}/acl/watch
- `references/other.md`: POST /freeBusy; GET /users/me/settings/{setting}; POST /users/me/settings/watch; GET /users/me/settings; GET /colors; POST /channels/stop
- `references/calendars.md`: GET /calendars/{calendarId}; POST /calendars; PATCH /calendars/{calendarId}; DELETE /calendars/{calendarId}; POST /calendars/{calendarId}/clear; PUT /calendars/{calendarId}
- `references/calendar-list.md`: GET /users/me/calendarList; POST /users/me/calendarList; PATCH /users/me/calendarList/{calendarId}; DELETE /users/me/calendarList/{calendarId}; GET /users/me/calendarList/{calendarId}; PUT /users/me/calendarList/{calendarId}; POST /users/me/calendarList/watch
