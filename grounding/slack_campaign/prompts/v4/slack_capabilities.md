# Slack capabilities for conceptual authoring

This brief qualifies the conceptual model. Stored attributes are not automatically
observable. There is an acting user; use “I/my” for that actor when relevant.

- Supported identifying facts include user names/email and bot status; channel
  name, topic, archived/type flags; message text, author, location and replies;
  reaction emoji and reactor; channel membership and distinct member counts;
  the workspace association displayed on a user's profile and its admin/owner
  flags. Do not distinguish ordinary members from guests using unexposed flags.
- Public channels and users in the actor's selected workspace can be discovered;
  channel histories, members and reactions can be read with appropriate access.
  A compiler can arrange required read access in the environment. Do not supply
  a menu of candidate answers as a discovery shortcut.
- General workspace enumeration, workspace-name lookup and switching list/search
  to a different workspace are unavailable. Visible profile/channel associations
  can supply workspace IDs. For workspace-membership roots, limit the population
  to the association displayed on discoverable users' profiles; do not assume
  every stored workspace membership is exposed. Do not invent human job titles,
  private intentions, last-login times, membership join times or edit history as
  observable selection criteria.
- Supported writes: post/reply to a message, edit/delete a message, add a reaction;
  create/archive/unarchive/rename a channel, set its topic; invite/remove a channel
  member; open a DM and message a user. Arrange actor-owned messages for edits or
  deletion when needed. Supply the intended new content or communication purpose.
- A reaction can be removed only by its own reactor: “remove my reactions” is
  supported; removing another person's reaction is not. A reaction referent is
  one person–message–emoji identity, not just its message. Supported emoji writes
  include thumbsup, thumbsdown, eyes, raised_hands, tada, rocket, heart, fire,
  check and x. Do not assume an arbitrary readable emoji is writable.
- Workspace changes, workspace-role changes, user-profile changes and named-role
  management have no supported write API. For roots requiring those operations,
  use an explicit read fallback about observable facts and state the limitation
  briefly. Do not replace the assigned root with another entity to obtain a write.

The compiler constructs and checks a fresh seed under the supplied domain contract.
API accessibility is supplied domain knowledge, not a separate compiler investigation.
This stage designs the story; it does not claim a validated runnable test.
