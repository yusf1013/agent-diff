# Google Calendar API: acl

## POST /calendars/{calendarId}/acl
Creates an access control rule.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.
  query:
    - `sendNotifications` (boolean, optional): Whether to send notifications about the calendar sharing change. Optional. The default is True.

## GET /calendars/{calendarId}/acl
Returns the rules in the access control list for the calendar. Used to find existing permissions and rule IDs (formatted as 'user:email', 'group:email', 'domain:name', or 'default') for updates/deletes.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
  query:
    - `maxResults` (integer, optional): Maximum number of entries returned.
    - `pageToken` (string, optional): Token for retrieving the next page of results.
    - `showDeleted` (boolean, optional): Whether to include deleted ACL rules (role='none'). Default: false.
    - `syncToken` (string, optional): Token for incremental sync, returning only changed entries since last sync.

## DELETE /calendars/{calendarId}/acl/{ruleId}
Deletes an access control rule, removing a user/group/domain's access to the calendar. Deletion is immediate and permanent. Cannot delete owner's own access.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
    - `ruleId` (string, **required**): ACL rule identifier. Format: 'user:email@example.com', 'group:group@example.com', 'domain:example.com', or 'default'. Obtained from GET /calendars/{calendarId}/acl.

## GET /calendars/{calendarId}/acl/{ruleId}
Returns a specific access control rule for a calendar. Use this to check the role assigned to a particular user, group, or domain without listing all ACL rules.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier. Use 'primary' for the user's primary calendar.
    - `ruleId` (string, **required**): ACL rule identifier. Format: 'user:{email}', 'group:{email}', 'domain:{domain}', or 'default'.

## PATCH /calendars/{calendarId}/acl/{ruleId}
Updates an access control rule using patch semantics. Only specified fields are modified; unspecified fields remain unchanged.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier.
    - `ruleId` (string, **required**): ACL rule identifier (e.g., 'user:email@example.com').
  query:
    - `sendNotifications` (boolean, optional): Whether to send notifications about the sharing change. No notifications on access removal. Default: true.
  body:
    - `role` (string, optional): The role to assign.

## PUT /calendars/{calendarId}/acl/{ruleId}
Updates an access control rule by fully replacing it. Unlike PATCH, this replaces the entire rule. Use for complete rule replacement.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier.
    - `ruleId` (string, **required**): ACL rule identifier (e.g., 'user:salma@test.com').
  query:
    - `sendNotifications` (boolean, optional): Whether to send notifications about the sharing change. No notifications on access removal. Default: true.
  body:
    - `role` (string, **required**): The role to assign.
    - `scope` (object, **required**): The extent to which calendar access is granted.

## POST /calendars/{calendarId}/acl/watch
Watch for changes to ACL resources on a specific calendar. Receive push notifications when access control rules are added, modified, or removed.

**Parameters:**
  path:
    - `calendarId` (string, **required**): Calendar identifier.
  query:
    None
  body:
    - `id` (string, **required**): Unique channel ID (UUID recommended, max 64 chars). Must be unique across all channels.
    - `type` (string, **required**): Type of delivery mechanism. Must be 'web_hook'.
    - `address` (string, **required**): HTTPS URL where notifications are delivered. Must be registered in GCP Console.
    - `token` (string, optional): Arbitrary string for verification (max 256 chars). Returned in X-Goog-Channel-Token header.
    - `params` (object, optional):
