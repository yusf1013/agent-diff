# Google Calendar tables

The tables of the workspace, with their columns. Assertions name a table as `entity` and its columns in `where`.

## `calendar_acl_rules`

- `id`: varchar(255), primary key
- `calendar_id`: varchar(255), refers to `calendars.id`
- `etag`: varchar(100)
- `role`: varchar(14)
- `scope_type`: varchar(7)
- `scope_value`: varchar(255)
- `created_at`: datetime
- `updated_at`: datetime
- `deleted`: boolean

## `calendar_channels`

- `id`: varchar(255), primary key
- `resource_id`: varchar(255)
- `resource_uri`: varchar(1000)
- `type`: varchar(50)
- `address`: varchar(1000)
- `expiration`: bigint
- `token`: varchar(500)
- `params`: jsonb
- `payload`: boolean
- `user_id`: varchar(255)
- `created_at`: datetime

## `calendar_event_attendees`

- `id`: integer, primary key
- `event_id`: varchar(1024), refers to `calendar_events.id`
- `email`: varchar(255)
- `display_name`: varchar(255)
- `organizer`: boolean
- `self`: boolean
- `resource`: boolean
- `optional`: boolean
- `response_status`: varchar(11)
- `comment`: text
- `additional_guests`: integer
- `profile_id`: varchar(255)

## `calendar_event_reminders`

- `id`: integer, primary key
- `event_id`: varchar(1024), refers to `calendar_events.id`
- `method`: varchar(5)
- `minutes`: integer

## `calendar_events`

- `id`: varchar(1024), primary key
- `calendar_id`: varchar(255), refers to `calendars.id`
- `etag`: varchar(100)
- `status`: varchar(9)
- `html_link`: varchar(500)
- `summary`: varchar(1000)
- `description`: text
- `location`: varchar(1000)
- `color_id`: varchar(10)
- `creator_id`: varchar(255), refers to `calendar_users.id`
- `organizer_id`: varchar(255), refers to `calendar_users.id`
- `creator_email`: varchar(255)
- `organizer_email`: varchar(255)
- `creator_display_name`: varchar(255)
- `organizer_display_name`: varchar(255)
- `creator_profile_id`: varchar(255)
- `organizer_profile_id`: varchar(255)
- `creator_self`: boolean
- `organizer_self`: boolean
- `start`: jsonb
- `end`: jsonb
- `start_datetime`: datetime
- `end_datetime`: datetime
- `start_date`: varchar(10)
- `end_date`: varchar(10)
- `end_time_unspecified`: boolean
- `recurrence`: jsonb
- `recurring_event_id`: varchar(1024)
- `original_start_time`: jsonb
- `transparency`: varchar(11)
- `visibility`: varchar(12)
- `ical_uid`: varchar(1024)
- `sequence`: integer
- `guests_can_invite_others`: boolean
- `guests_can_modify`: boolean
- `guests_can_see_other_guests`: boolean
- `anyone_can_add_self`: boolean
- `private_copy`: boolean
- `locked`: boolean
- `attendees_omitted`: boolean
- `hangout_link`: varchar(500)
- `conference_data`: jsonb
- `attachments`: jsonb
- `extended_properties`: jsonb
- `source`: jsonb
- `gadget`: jsonb
- `reminders`: jsonb
- `event_type`: varchar(15)
- `working_location_properties`: jsonb
- `out_of_office_properties`: jsonb
- `focus_time_properties`: jsonb
- `birthday_properties`: jsonb
- `created_at`: datetime
- `updated_at`: datetime

## `calendar_list_entries`

- `id`: varchar(255), primary key
- `user_id`: varchar(255), refers to `calendar_users.id`
- `calendar_id`: varchar(255), refers to `calendars.id`
- `etag`: varchar(100)
- `access_role`: varchar(14)
- `summary_override`: varchar(255)
- `description_override`: text
- `color_id`: varchar(10)
- `background_color`: varchar(10)
- `foreground_color`: varchar(10)
- `hidden`: boolean
- `selected`: boolean
- `primary`: boolean
- `deleted`: boolean
- `default_reminders`: jsonb
- `notification_settings`: jsonb
- `created_at`: datetime
- `updated_at`: datetime

## `calendar_settings`

- `id`: integer, primary key
- `user_id`: varchar(255), refers to `calendar_users.id`
- `setting_id`: varchar(100)
- `value`: text
- `etag`: varchar(100)

## `calendar_sync_tokens`

- `id`: integer, primary key
- `token`: varchar(255)
- `user_id`: varchar(255), refers to `calendar_users.id`
- `resource_type`: varchar(50)
- `resource_id`: varchar(255)
- `snapshot_time`: datetime
- `expires_at`: datetime
- `created_at`: datetime

## `calendar_users`

- `id`: varchar(255), primary key
- `email`: varchar(255)
- `display_name`: varchar(255)
- `self`: boolean
- `created_at`: datetime
- `updated_at`: datetime

## `calendars`

- `id`: varchar(255), primary key
- `summary`: varchar(255)
- `description`: text
- `location`: varchar(500)
- `time_zone`: varchar(100)
- `etag`: varchar(100)
- `conference_properties`: jsonb
- `auto_accept_invitations`: boolean
- `owner_id`: varchar(255), refers to `calendar_users.id`
- `data_owner`: varchar(255)
- `created_at`: datetime
- `updated_at`: datetime
- `deleted`: boolean
