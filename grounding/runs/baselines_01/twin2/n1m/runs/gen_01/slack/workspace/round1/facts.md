# Facts to test

Together, your tests must check the assistant on each fact below: for every fact, at least one test in which that
fact decides which record is the right one.

The kinds of fact:
- **attribute:** an identifying attribute of a record (identity, text, time, quantity, state);
- **relationship:** a record's related person or record in a given role (a foreign-key role, an association);
- **hierarchy:** a level of a hierarchy or a self-relationship (a parent, a reply's parent);
- **binding:** several conditions that must hold on the same related record, across a to-many relationship;
- **derived value:** a value computed from records (a count, the latest one, a local date, the primary calendar).

| Fact | Kind | Rests on |
|---|---|---|
| `A:Conversation.is_dm` | attribute | `channels.is_dm` |
| `A:Message.blocks` | attribute | `messages.blocks` |
| `A:User.email` | attribute | `users.email` |
| `A:User.is_bot` | attribute | `users.is_bot` |
| `B:message_reactions.message` | binding | `message_reactions.message` |
| `B:messages.channel_id` | binding | `messages.channel_id` |
| `D:dm_with` | derived value | `dm_with` |
| `D:latest_message` | derived value | `latest_message` |
| `D:reaction_count` | derived value | `reaction_count` |
