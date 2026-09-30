The mechanical checks of scenario.json found these problems:
- Reference query or mutation cannot be evaluated: a row has no column 'table'. A query's `key` must be the root table's primary key (for example `user_id` for Slack users, `channel_id` for channels, `message_id` for messages), and every `field` or join column must exist in its table.

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.