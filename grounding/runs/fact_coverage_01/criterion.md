# Fact-discrimination coverage (FDC): definition and construction

Evidence for every rule below is in [findings.md](findings.md); the summary is in [report.md](report.md).

## Requirement

A requirement is one **fact of the adopted domain model** that an ordinary request can use to identify something and
the agent can observe through the API:

| Kind | Fact | Designated alternative (how the credit near-miss is built) |
|---|---|---|
| A | identifying attribute (identity, text, time, quantity, state) | a sibling attribute of the same entity and kind stands in (name for description, handle for name, start for end); states: another value |
| R | relationship role (FK role, association, interpreted reference) | a sibling role or short alternative connection holds instead (created for owned, organized for created, assigner for creator, location for author's membership, reversed relation direction) |
| H | hierarchy / self relationship | the other level: nested for direct, ancestor for descendant, reply for root, series for exception |
| B | same-record binding across a to-many relationship | the conditions hold on different related records |
| D | derived representation | the underlying or neighbouring representation (series for one occurrence, UTC for local day, a projection that drops a distinguishing field) |

Catalog sizes: Slack 34, Box 60, Calendar 40, Linear 121 (255 total), built by [catalog/build.py](catalog/build.py)
from [catalog/facts.py](catalog/facts.py). Every stored column of an included entity and every model relationship has
a recorded disposition. The count is linear in the model; it does not multiply facts by routes, modes, or each other.

## Credit rule

A test covers requirement *f* when, for one of its references that uses *f*:

1. **Near-miss through the designated alternative.** The seed contains a record that the reference query mutated by
   *f*'s alternative selects and the intended query does not; all other conditions hold on it. Checked mechanically
   by executing both queries on the seed ([fdc.py](fdc.py)). Witnesses are distinct per requirement.
2. **Fact-sensitive form.** Either the target is present (the near-miss competes with it), or no target exists and
   the request permits reporting absence. A request that presupposes a match which does not exist does not earn fact
   credit: there the agent's choice is governed by a generic no-match policy, not by the fact.

Rule 1 is supported by the alternative/plain contrast: with absence permitted, near-misses through a designated
alternative were acted on, plain near-misses for the same facts almost never. Rule 2 is supported by the isolation and
explicit-absence controls: with a presupposing request, even file type and person name were dropped.

## Policy panel (not multiplied across facts)

Per domain, a small fixed set of tests measures resolution behaviour once:

- presupposed no-match with a one-condition near-miss (does the agent act, and does it disclose the unmet condition?);
- far miss: candidates missing several relational conditions, and one missing a type condition (in the pilot, Qwen
  acted in all 3 completed runs where several relational or secondary attribute conditions were unmet, and was blocked
  by the unmet type condition in its one completed run);
- an unresolved choice (underspecified) and a collection request.

## Construction

- One natural request per test, packing the facts of its identifying path; one designated-alternative near-miss per
  fact, co-located with the target so it must be inspected to be rejected.
- Use no-target-with-permission tests for facts whose alternative is hard to co-locate.
- Phrase relational conditions unambiguously; wording that attaches a relative clause to the wrong noun measures
  reading, not the fact (Slack W08).
- Keep targets from being listed first; avoid write operations the environment cannot perform.
