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
