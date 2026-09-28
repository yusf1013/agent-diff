# boundary_02: a meaningful, failure-exposing coverage space for capability boundaries, and its size

*Started 2026-09-28. A manual investigation: hand-built catalog and tests, hand analysis, the self-hosted solver, no
Muse. It runs in cycles; [log.md](log.md) records each one. This plan states the question and the method; findings go
in the log, and the report at the end.*

## The question

The PI: "how do we form a coverage space, and the numbers, what number of tests would be required to cover them",
where the space "should be meaningful and it should also be exposing failures".

A capability boundary is a request the service will not carry out for this actor: the actor lacks the permission,
the record is in the wrong state, the field cannot be written, the value breaks a limit, or no operation does it.
The questions:
1. **Meaningful:** what are the space's elements, and where do they come from? They must be derived from the domain
   model and the services' contracts, as the fact catalog is, and not from what the replica happens to implement.
2. **Exposing failures:** which dimensions of the space decide whether an agent fails? A space whose cells do not
   separate failing from passing behaviour is not useful for testing.
3. **The numbers:** how many elements (N), how many cells (M), and whether one test per cell suffices. That holds only
   if behaviour is uniform within a cell. Otherwise it takes up to one test per element.

## The space

**Elements** come from two sources, both part of the domain model:
- **The fact catalog** (255 facts; `fact_coverage_01/catalog/`). For each attribute or relation: can the actor
  change it through a documented operation, and under what conditions? A fact nothing can change (a creation time,
  an author, an identifier, a derived count) gives a read-only or no-operation element.
- **The write operations' documented preconditions**, per service: the role an operation needs, the state it
  requires, and the limits on its values.

**Inclusion rule:** an element counts only if a well-formed, natural request runs into it, because of permission,
state, the field's nature or a value limit. Malformed input (missing arguments, bad JSON) does not count.

**Dimensions**, each defined from the domain and not from any agent's behaviour:

| Dimension | Values | Why it may matter |
|---|---|---|
| Class | permission, state precondition, read-only field, value limit, no operation | how the refusal arises |
| Workaround | yes / no: a documented operation that changes something else so the request goes through (unarchive first, move the issues first, a personal display name) | the boundary_01 pilot's 9 failures were all workarounds |
| Discoverable before acting | yes / no: is the blocking condition visible in a normal read (an access role, `is_archived`), or found only by trying? | tests whether the agent checks, or how it reacts |
| Refusal | loud (an error) / silent (success returned, change ignored) | silent refusals are where false success claims can come from; the pilot tested only loud ones |

**Faithfulness filter,** applied after the space is derived: each element is probed on the replica with a field-level
diff. Refused loudly, refused silently, or not refused at all (unfaithful, so left out and counted). The pilot's two
"unfaithful" silent candidates, the Calendar organizer patch and the Box modified-time update, are checked at field
level first.

## Method, per cycle

1. **Derive the catalog** of elements with their dimension tags ([catalog.py](catalog.py) → `catalog.json`), and
   count N and the non-empty cells M.
2. **Probe** every element on the replica ([probe_elements.py](probe_elements.py)).
3. **Test:** 2–3 elements per cell, where the cell has them.
   - Each test is an impossible request. Its decoy is the element's workaround where one exists, otherwise a nearby
     record.
   - Controls are the possible version, where one exists.
   - Run on the self-host: 3 trials each, at most 12 in flight.
4. **Analyze.** Grade by hand from the diff, the final answer and the trajectory, with boundary_01's outcomes
   (reported, transparent, substituted, side effect, false claim), plus one decided in advance:
   - a timeout on an impossible request counts as "no answer", a failure to report;
   - it is kept apart from the mistakes that change state.

   Then measure agreement within each cell and exposure by dimension, and iterate.

## What would answer the question

- **The catalog,** with its source for every element, its N, and its cell counts M, per service.
- **Per cell:**
  - how often agents fail;
  - whether different elements of the same cell behave alike (uniformity);
  - which dimensions separate failure from success.
- **The number of tests the space needs:**
  - M, if cells are uniform;
  - more, where they are not;
  - fewer, if some cells never expose a failure (with the evidence).
