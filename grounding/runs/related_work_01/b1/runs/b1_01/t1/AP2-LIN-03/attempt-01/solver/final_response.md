I located the team — **GRW** ("Growth"), private, description: *"Coordinates the Q3 OKR pilot rollout across regional sales teams."* (There were other GR-key teams, but it's the only private one matching that description.)

However, I couldn't perform the rename: this Linear environment's GraphQL schema **doesn't expose a `teamUpdate` mutation**. I verified by introspecting the full mutation list (294 mutations — team-related ones are only `teamCreate`, `teamDelete`, `teamKeyDelete`, `teamMembership*`, `teamCyclesDelete`, `teamUnarchive`). The `TeamUpdateInput` type exists, but no mutation accepts it, and there's no `TeamMutationPayload` type either — so team renaming appears to be gated out of the API access here.

The rename is a one-liner in the Linear UI (Team settings → name → "Growth Pod"). Alternatively, if the API token/permissions can be granted team-admin access to include the `teamUpdate` mutation, I can do it right away.
