# Native Slack construction contract

Use the supplied seven-table schema and API definitions. There is no inherited
benchmark data. The runtime actor ID is supplied separately; create that user and
its workspace membership. Give each user one displayed workspace association unless
the sketch explicitly requires otherwise. Ordinary channels have a workspace.
Use public channels and actor membership for readable scenario content unless a
fixed story fact says otherwise. An access/setup requirement conflicting with a
fixed fact is a design conflict, not authority to change selection. Membership
counts include the actor when present. Do not copy an unrelated baseline seed.

Slack message_id is the actual API timestamp: use unique numeric timestamp strings,
also in reactions/parent links. Set ts to the same value when supplied. Include
ordinary message text and type="message". Use ISO dates for supplied date fields.
ORM Python defaults are not applied by the SQL seed loader; omitted nullable fields
may become null. Provide created_at dates for users and channels. Workspace roles
are owner/admin/member/guest; only admin/owner distinctions are API-readable.

Documented observable identifying facts include names, email, bot flags; channel
name/topic/type; message text, author, location and replies; reaction emoji/reactor;
channel membership and member counts. Profile workspace IDs/admin/owner flags are
visible, but general workspace enumeration, workspace-name lookup, arbitrary job
roles, last-login or membership-join times and edit histories are not selection
evidence. Follow the supplied operation menu. Writes to another person's reactions,
workspace roles, user profiles and channel purpose are unsupported. Message edit/
delete ownership must be arranged consistently with the story. Reaction write names
include thumbsup, thumbsdown, eyes, raised_hands, tada, rocket, heart, fire, check, x.
Do not pre-perform the requested operation in the initial state.

For card annotations, computation attributes supply the answer or new field values
AFTER selection; fields used only to select the referents do not belong there.
Each inner list is an alternative sufficient set, not one step in a pipeline.
Include selected IDs when they supply references written into new records. Written
attributes include those destination references as well as assigned content;
exclude actor fields supplied by authentication. A value entirely supplied by the
request needs no environmental computation input: use [[]]. Pure deletion assigns
no fields: use [] for written attributes.

This contract supplies implementation constraints; you are not being asked to
derive an API access proof or decide which unsupported capabilities to test.
