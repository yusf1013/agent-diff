# Slack tables

The tables of the workspace, with their columns. Assertions name a table as `entity` and its columns in `where`.

## `channel_members`

- `channel_id`: varchar(50), primary key, refers to `channels.channel_id`
- `user_id`: varchar(50), primary key, refers to `users.user_id`
- `joined_at`: datetime

## `channels`

- `channel_id`: varchar(50), primary key
- `channel_name`: varchar(100)
- `team_id`: varchar(50), refers to `teams.team_id`
- `topic_text`: text
- `purpose_text`: text
- `is_private`: boolean
- `is_dm`: boolean
- `is_gc`: boolean
- `created_at`: datetime
- `is_archived`: boolean

## `file_messages`

- `file_message_id`: varchar(50), primary key
- `file_id`: varchar(50), refers to `files.file_id`
- `message_id`: varchar(50), refers to `messages.message_id`

## `files`

- `file_id`: varchar(50), primary key
- `user_id`: varchar(50), refers to `users.user_id`
- `file_name`: varchar(255)
- `file_size`: integer
- `file_type`: varchar(50)
- `file_url`: varchar(255)
- `created_at`: datetime

## `message_edits`

- `edit_id`: varchar(50), primary key
- `message_id`: varchar(50), refers to `messages.message_id`
- `edited_text`: text
- `edited_at`: datetime

## `message_reactions`

- `message_id`: varchar(50), primary key, refers to `messages.message_id`
- `user_id`: varchar(50), primary key, refers to `users.user_id`
- `reaction_type`: varchar(50), primary key
- `created_at`: datetime

## `messages`

- `message_id`: varchar(50), primary key
- `parent_id`: varchar(50), refers to `messages.message_id`
- `channel_id`: varchar(50), refers to `channels.channel_id`
- `user_id`: varchar(50), refers to `users.user_id`
- `message_text`: text
- `type`: varchar(50)
- `ts`: varchar(50)
- `blocks`: jsonb
- `created_at`: datetime

## `team_roles`

- `role_id`: varchar(50), primary key
- `team_id`: varchar(50), refers to `teams.team_id`
- `role_name`: varchar(100)

## `team_settings`

- `team_id`: varchar(50), primary key, refers to `teams.team_id`
- `default_channel_id`: varchar(50), refers to `channels.channel_id`
- `allow_file_uploads`: boolean

## `teams`

- `team_id`: varchar(50), primary key
- `team_name`: varchar(100)
- `created_at`: datetime

## `user_mentions`

- `mention_id`: varchar(50), primary key
- `message_id`: varchar(50), refers to `messages.message_id`
- `user_id`: varchar(50), refers to `users.user_id`
- `mentioned_at`: datetime

## `user_roles`

- `user_id`: varchar(50), primary key, refers to `users.user_id`
- `role_id`: varchar(50), primary key, refers to `team_roles.role_id`
- `assigned_at`: datetime

## `user_settings`

- `user_id`: varchar(50), primary key, refers to `users.user_id`
- `notification_level`: varchar(8)

## `user_teams`

- `user_id`: varchar(50), primary key, refers to `users.user_id`
- `team_id`: varchar(50), primary key, refers to `teams.team_id`
- `role`: varchar(6)

## `users`

- `user_id`: varchar(50), primary key
- `username`: varchar(50)
- `email`: varchar(100)
- `real_name`: varchar(100)
- `display_name`: varchar(80)
- `timezone`: varchar(64)
- `title`: varchar(120)
- `created_at`: datetime
- `last_login`: datetime
- `is_active`: boolean
- `is_bot`: boolean
