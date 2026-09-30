# One framing for all the test kinds (a proposal, 2026-09-30)

*Drafted by the lead session overnight for the PI's point 5 in [the notes](brain_dump_2026-09-29.md): several-match
tests and capability boundaries "feel like a dangling supplemental". Nothing here is decided. It changes how the
method is presented, not what the pipeline does.*

## The idea in one line

Every test asks the agent to act on the records that a natural request identifies. The facts of the domain model
say **what the agent must get right about each record**; the **relation between the request and the world** says
**what the right action is**. The suite covers facts × relations.

## The relations

A request presumes something about how many records fit it and what can be done to them. The world may or may not
agree. Each disagreement is a class of input in the sense of equivalence partitioning, and each class has one
right behaviour, which is a policy:

| The request presumes | The world holds | Right behaviour | Our name | The construction device |
|---|---|---|---|---|
| one record | exactly one | act on it | regular test (cover, probe, fact probe) | near misses: records that fail one fact in the tempting way (families F1–F8) |
| one record | none | report absence, or ask | absence policy | the target removed; the near misses stay |
| one record | several | ask before changing anything | underspecified policy | a condition dropped, or a second full match added |
| every matching record | several, some hard to reach | act on all of them | several-match test | traps: matches placed where a lazy search misses them (another folder, a hidden calendar, past the first page) |
| a change the actor can make | the change is not allowed to this actor, or not possible | report the limit; substitute nothing | capability-boundary test | the write side of a fact: the operation, its precondition, the actor's rights |

The first three rows are the suite as it stands. The fourth and fifth are not additions to the method; they are
the two columns that were missing from the same table.

## What this settles

- **"Everything is a policy" and "valid versus invalid inputs" are the same view.** The rows are the equivalence
  classes; the right behaviour of each row is its policy. Regular tests are the valid class; absence and
  underspecification are the invalid classes; several-match is the plural class; the boundary is the
  impossible class.
- **The facts are the rows' common currency.** A test in any class is non-trivial only because of a fact: the near
  miss differs in a fact; the missing target was identified by a fact; the second match agrees on every fact but the
  dropped one; the trapped match satisfies the same facts as the visible ones; the boundary is the write side of a
  fact (for each fact: can this actor change it, through which operation, under which precondition; 152 elements,
  93 of them faithful on the replicas). Coverage stays fact-based: which facts are tested in which class.
- **Traps are construction devices, not inputs.** They are to the plural class what near-miss families are to the
  singular one: a catalogue of the ways a lazy strategy fails (the 33 shortcuts over 6 request kinds, 19 of them
  practical). The agent is never told about either. What the agent must reason out is the same in both cases:
  check every condition, search everywhere the request allows.
- **The coverage space of each new class is already defined and finite:** shortcuts × request kinds for several
  matches; the write requirements of the catalog for boundaries. Neither multiplies the fact catalog.
- **What the classes test differs, and the report should say so.** The singular classes test discrimination
  (reading the right record); the plural class tests search completeness (finding every record); the boundary
  class tests restraint (not substituting). The judge already grades each by its own criterion.

## What would change in the paper

- One table like the one above, early, instead of two extensions at the end.
- The policy panel becomes "the invalid classes, tested per fact"; the several-match and boundary results become
  two more columns of the same results table, with their own denominators.
- The name follows the framing: the method tests whether an agent acts on **the right records** (identification,
  completeness, restraint), not "grounding obligations".

## Open

- Whether the plural class should also be tested per fact (as the policy classes are) or per service (as RQ9
  reports it: the misses follow the route, not the fact). The evidence so far says per service.
- Whether the boundary's per-fact write requirements are reported as coverage (80 of 255 facts carry a faithful
  write limit) or kept as their own space.
