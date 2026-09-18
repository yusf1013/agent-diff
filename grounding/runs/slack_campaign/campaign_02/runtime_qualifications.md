# Runtime qualifications found during campaign validation

These are manual engineering probes in disposable local clones. They are not
solver experiments or automatically generated capability-coverage successes.
No benchmark cards or solver results are inferred from a failed call alone.

| Question | Observed result | Consequence |
|---|---|---|
| Can the actor remove another user's reaction? | With a supported `thumbsup` name, `reactions.remove` returned `no_reaction` and preserved the other user's row. | Ordinary generation must not promise removal of another user's reaction. |
| Is every readable reaction name writable? | A seeded `white_check_mark` reaction was readable, but removal returned `invalid_name`. A narrow inspection of the endpoint's validation confirmed a restricted write vocabulary (`check`, rather than `white_check_mark`, is supported). | Source reactions can identify records without implying those names can be written. |
| Does search recover non-member channel history? | `search.messages` for `CDN` and `in:product-growth` returned no matches in the tested non-member setup; an empty query was rejected. | These probes did not remove the observed access gap. Do not infer that empty search means the seed lacks such messages. |
| Does `users.conversations` enumerate the actor's other workspaces? | In a two-workspace membership setup it returned only the selected workspace's conversations. | Added actor memberships alone do not establish cross-workspace discovery. |
| Does an explicit `team_id` switch channel-listing workspace? | Both `users.conversations` and `conversations.list` ignored the supplied secondary-workspace ID in this setup and still listed the selected workspace. | A known-ID channel anchor may work, but these list calls are not a verified workspace-switch interface. |

Evidence:

- [Other user's reaction, supported name](capability-probes/reactions-remove-other-supported-name.json)
- [Unsupported reaction name](capability-probes/reactions-remove-other.json)
- [Query/form encoding checks](capability-probes/reactions-remove-other-query-form.json)
- [Search observations](capability-probes/search-nonmember-channel.json)
- [User conversations across workspaces](capability-probes/users-conversations-multiworkspace.json)
- [Explicit workspace list parameters](capability-probes/explicit-workspace-channel-listing.json)

The reaction diagnosis used a narrow implementation inspection after black-box
calls, rather than treating public Slack behavior as proof of this replica's
behavior. This is runtime engineering evidence; it is not an expansion of the
fixed evidence policy for extracting baseline grounding cards.
