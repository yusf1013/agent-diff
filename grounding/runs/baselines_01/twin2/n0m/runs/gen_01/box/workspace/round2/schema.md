# Box tables

The tables of the workspace, with their columns. Assertions name a table as `entity` and its columns in `where`.

## `box_collections`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `name`: varchar(50)
- `collection_type`: varchar(50)

## `box_comments`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `message`: text
- `tagged_message`: text
- `file_id`: varchar(20), refers to `box_files.id`
- `item_id`: varchar(20)
- `item_type`: varchar(20)
- `is_reply_comment`: boolean
- `created_by_id`: varchar(20), refers to `box_users.id`
- `created_at`: datetime
- `modified_at`: datetime

## `box_file_contents`

- `id`: varchar(20), primary key
- `version_id`: varchar(20), refers to `box_file_versions.id`
- `content`: blob
- `content_type`: varchar(255)

## `box_file_versions`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `file_id`: varchar(20), refers to `box_files.id`
- `version_number`: integer
- `sha_1`: varchar(40)
- `size`: bigint
- `name`: varchar(255)
- `uploader_display_name`: varchar(255)
- `modified_by_id`: varchar(20), refers to `box_users.id`
- `trashed_by_id`: varchar(20), refers to `box_users.id`
- `trashed_at`: datetime
- `restored_by_id`: varchar(20), refers to `box_users.id`
- `restored_at`: datetime
- `purged_at`: datetime
- `created_at`: datetime
- `modified_at`: datetime

## `box_files`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `name`: varchar(255)
- `description`: varchar(255)
- `size`: bigint
- `item_status`: varchar(20)
- `parent_id`: varchar(20), refers to `box_folders.id`
- `path`: varchar(500)
- `created_by_id`: varchar(20), refers to `box_users.id`
- `modified_by_id`: varchar(20), refers to `box_users.id`
- `owned_by_id`: varchar(20), refers to `box_users.id`
- `etag`: varchar(10)
- `sequence_id`: varchar(10)
- `sha_1`: varchar(40)
- `file_version_id`: varchar(20)
- `version_number`: varchar(20)
- `comment_count`: integer
- `extension`: varchar(50)
- `lock`: jsonb
- `tags`: jsonb
- `collections`: jsonb
- `shared_link`: jsonb
- `permissions`: jsonb
- `is_package`: boolean
- `is_accessible_via_shared_link`: boolean
- `is_externally_owned`: boolean
- `has_collaborations`: boolean
- `is_associated_with_app_item`: boolean
- `allowed_invitee_roles`: jsonb
- `shared_link_permission_options`: jsonb
- `expiring_embed_link`: jsonb
- `watermark_info`: jsonb
- `box_metadata`: jsonb
- `representations`: jsonb
- `classification`: jsonb
- `uploader_display_name`: varchar(255)
- `created_at`: datetime
- `modified_at`: datetime
- `trashed_at`: datetime
- `purged_at`: datetime
- `content_created_at`: datetime
- `content_modified_at`: datetime
- `expires_at`: datetime
- `disposition_at`: datetime

## `box_folders`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `name`: varchar(255)
- `description`: varchar(256)
- `size`: bigint
- `item_status`: varchar(20)
- `parent_id`: varchar(20), refers to `box_folders.id`
- `path`: varchar(500)
- `created_by_id`: varchar(20), refers to `box_users.id`
- `modified_by_id`: varchar(20), refers to `box_users.id`
- `owned_by_id`: varchar(20), refers to `box_users.id`
- `etag`: varchar(10)
- `sequence_id`: varchar(10)
- `tags`: jsonb
- `collections`: jsonb
- `shared_link`: jsonb
- `folder_upload_email`: jsonb
- `created_at`: datetime
- `modified_at`: datetime
- `trashed_at`: datetime
- `purged_at`: datetime
- `content_created_at`: datetime
- `content_modified_at`: datetime
- `sync_state`: varchar(20)
- `has_collaborations`: boolean
- `can_non_owners_invite`: boolean
- `is_externally_owned`: boolean
- `is_collaboration_restricted_to_enterprise`: boolean
- `can_non_owners_view_collaborators`: boolean
- `is_accessible_via_shared_link`: boolean
- `is_associated_with_app_item`: boolean
- `permissions`: jsonb
- `allowed_shared_link_access_levels`: jsonb
- `allowed_invitee_roles`: jsonb
- `watermark_info`: jsonb
- `classification`: jsonb
- `box_metadata`: jsonb

## `box_hub_items`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `hub_id`: varchar(20), refers to `box_hubs.id`
- `item_id`: varchar(20)
- `item_type`: varchar(20)
- `item_name`: varchar(255)
- `position`: integer
- `added_by_id`: varchar(20), refers to `box_users.id`
- `added_at`: datetime

## `box_hubs`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `title`: varchar(255)
- `description`: text
- `is_ai_enabled`: boolean
- `is_collaboration_restricted_to_enterprise`: boolean
- `can_non_owners_invite`: boolean
- `can_shared_link_be_created`: boolean
- `view_count`: integer
- `created_by_id`: varchar(20), refers to `box_users.id`
- `updated_by_id`: varchar(20), refers to `box_users.id`
- `created_at`: datetime
- `updated_at`: datetime

## `box_task_assignments`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `task_id`: varchar(20), refers to `box_tasks.id`
- `item_id`: varchar(20), refers to `box_files.id`
- `item_type`: varchar(20)
- `assigned_to_id`: varchar(20), refers to `box_users.id`
- `assigned_by_id`: varchar(20), refers to `box_users.id`
- `message`: text
- `resolution_state`: varchar(20)
- `assigned_at`: datetime
- `reminded_at`: datetime
- `completed_at`: datetime

## `box_tasks`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `message`: text
- `action`: varchar(20)
- `is_completed`: boolean
- `completion_rule`: varchar(20)
- `item_id`: varchar(20), refers to `box_files.id`
- `item_type`: varchar(20)
- `due_at`: datetime
- `created_by_id`: varchar(20), refers to `box_users.id`
- `created_at`: datetime

## `box_users`

- `id`: varchar(20), primary key
- `type`: varchar(20)
- `name`: varchar(255)
- `login`: varchar(255)
- `status`: varchar(50)
- `job_title`: varchar(100)
- `phone`: varchar(100)
- `address`: text
- `avatar_url`: text
- `language`: varchar(50)
- `timezone`: varchar(100)
- `space_amount`: bigint
- `space_used`: bigint
- `max_upload_size`: bigint
- `notification_email`: jsonb
- `role`: varchar(20)
- `enterprise`: jsonb
- `tracking_codes`: jsonb
- `can_see_managed_users`: boolean
- `is_sync_enabled`: boolean
- `is_external_collab_restricted`: boolean
- `is_exempt_from_device_limits`: boolean
- `is_exempt_from_login_verification`: boolean
- `is_platform_access_only`: boolean
- `my_tags`: jsonb
- `hostname`: varchar(255)
- `external_app_user_id`: varchar(255)
- `created_at`: datetime
- `modified_at`: datetime
