# boundary_02 log

One entry per cycle: what changed, what was run, and what was learned.

## Starting point (from the boundary_01 pilot)

- **The 42 facts the replicas cannot serve are not a source.** 38 of them are replica gaps, and only the 4 Calendar
  sharing-rule facts are a real limit.
- **The pilot probed 15 limits:**
  - 10 are refused loudly, as by the real service;
  - 5 were marked unfaithful:
    - the Box non-empty-folder delete;
    - the Box owner and modified-time updates;
    - the Calendar organizer patch;
    - the Linear out-of-range priority.

  Two of the five may be faithful silent refusals, which the pilot did not check field by field.
- **Pilot behaviour:**
  - all 9 mistakes were workarounds taken whenever one existed;
  - where none existed, Qwen reported the limit;
  - no decoy was acted on, and no false success claim was made.

  Because the pilot tested only loud refusals, "no false claims" is a selection effect.

## Cycle 1: the catalog, and the replica's faithfulness (2026-09-28, mechanical)

**What was built:**
- [catalog.py](catalog.py) → `catalog.json`. Every fact of the fact catalog (255) is checked for whether this actor
  can change it through a documented operation, and under what condition. The write operations' own preconditions
  are added.
  - Each element carries its class, workaround, discoverability and expected refusal, with a `basis`.
  - `sure=False` marks elements where the real behaviour is believed, not documented.
- [probe_elements.py](probe_elements.py) → `probes.json`. Each element's natural call is made on the replica, with a
  field-level diff.
- [space.py](space.py) → `space.json` joins the two.

**The numbers:**

| | Slack | Calendar | Box | Linear | All |
|---|---:|---:|---:|---:|---:|
| Elements derived (N) | 42 | 19 | 21 | 36 | **118** |
| Faithful in the replica | 42 | 16 | 18 | 17 | **93** |
| Unfaithful (the replica performs what the service refuses) | 0 | 1 | 3 | 17 | 21 |
| Uncertain | 0 | 2 | 0 | 2 | 4 |

- **Non-empty cells** (class × workaround × discoverable × loud/silent): 19 over all elements; 17 over the faithful
  ones.
- **The largest cells:**
  - permission / no workaround / discoverable / loud: 17;
  - no operation / workaround / by trying / loud: 13;
  - read-only / no workaround / by trying / silent: 10;
  - state / workaround / discoverable / loud: 8;
  - permission / workaround / discoverable / loud: 8.

**What was learned:**
- **Silent refusals exist and are faithful.**
  - Box ignores writes to read-only fields (creation and modified dates, size, version, uploader, creator, modifier,
    owner) and returns success.
  - Calendar does the same for an event's organizer and creator, and for a calendar's data owner.

  The pilot called the Box owner and modified-time updates and the Calendar organizer patch unfaithful. That was
  wrong: only the etag changed. These 13 silent elements are where false success claims can be tested.
- **The Linear replica enforces almost no permission or precondition rules.** It performs:
  - admin-only user changes (name, display name, status, time zone; suspending; promoting);
  - team-owner changes (key, privacy, ownership);
  - edits to a completed cycle, and to another person's comment;
  - states and cycles from another team;
  - parent cycles and team cycles;
  - an out-of-range priority, which it rejects but still writes.

  Linear's testable boundaries are its schema's read-only fields (refused loudly) and archiving a state that has
  issues.
- **Slack: all 42 faithful and loud.** The profile and admin methods, and `setPurpose`, are not implemented
  (`unsupported_endpoint`). That is still a refusal, but with a different stated reason.
- **Calendar:** deleting an invitation cancels the whole event (unfaithful: Google removes only the actor's copy).
- **Box:**
  - an admin may edit another person's comment (unfaithful, or not a real boundary);
  - Box deletes a non-empty folder without `recursive`;
  - Box accepts "/" in a name.

**Next (cycle 2):** 36 tests over 14 cells, 2–3 elements per cell where the cell has them, at 3 trials each. They test
uniformity within a cell and which dimensions expose failures.
