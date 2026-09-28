# Domain knowledge in the deterministic code (roadmap step 2)

*2026-09-27. For discussion with the PI at step 3; **nothing here has been changed.***

## The question

How much of what the automated system knows about each domain sits in its deterministic code, instead of in its
inputs (the domain model) or in the agents? One way to find out: suppose someone adds a new service to the mock by
following its own instructions (the eight steps under "Adding a New Service" in the repository's `AGENTS.md`), without
knowing our technique. What extra would we have to write before our automation works on it?

## Method

- **Mechanical map** ([domain_touchpoints.py](domain_touchpoints.py), [domain_touchpoints.json](domain_touchpoints.json)).
  Every line in the 32 code files of the generation, check, variant, judging and running path that names a domain,
  one of its tables, or a domain-specific field.
- **Reading.** Each file that has such lines was read, and each touchpoint put in one of three classes:
  - **derived:** computed from the mock automatically (its schema, its seed script, the benchmark's docs);
  - **domain model:** an input by design (the fact catalog and model);
  - **hand-written:** knowledge about the domain written into code or notes.

## Summary

The machinery is generic, and the domain knowledge sits in a few named places.

**Generic:** these files contain no line that names a domain, or only a display name:
- the fact-check query language and checks (`fdc.py`, 288 lines);
- scenario derivation (`derive.py`);
- the orchestrator;
- both judges (`judge.py`, `judge2.py`);
- the policy variants and their sampling (`policy.py`, `reader2.py`, `population.py`, `sampler.py`);
- the catalog-to-writer transformation (`make_facts.py`);
- the solver's episode loop.

**Domain-specific:**

| Where | What it knows | Class | Size | A new domain needs |
|---|---|---|---|---|
| `seedops.py`, generic part | table and column metadata from the mock's seed script; a `row` operation for any table, with neutral defaults | derived | ~170 lines | nothing |
| `seedops.py`, per-domain builders | convenience operations (person, folder, file, event, issue, message ...), their defaults and links, and the default people | hand-written | 65–118 lines per domain | optional: `row` works without them, but writers do better with them |
| `seed_ops.md` per domain | the writer's guide to those operations, and the default people | hand-written | 2.7–3.9 KB | a guide; for `row` alone it could be generated from the schema |
| `preflight.py` `auto_probes` | the read calls that show every seeded record (Box's REST paths, Calendar's lists and ACLs, Linear's 18 list queries; Slack uses its runtime's own probes) | hand-written | ~10–30 lines per domain | yes: a list of read calls |
| `preflight.py` writes | how to perform a write: REST, GraphQL, or Slack's method calls | hand-written by protocol | ~30 lines | nothing, if the service is REST or GraphQL |
| `smoke_runtime.py`, `custom_runtime.py` | the API path prefix, an advisory-lock key, volatile tables (Calendar's sync tokens), one table-order quirk (Linear) | hand-written | ~10 lines | a few constants |
| the seed script (`backend/utils/seed_<service>_template.py`) and the benchmark's docs | the schema, the template, and the solver's API documentation (`api.md`) | derived | – | nothing: the mock's own steps 2 and 6 supply them |
| `make_briefs4.py` | facts to leave out because the replica cannot serve them (Linear projects, Calendar ACLs and recurrence) | hand-written, from runs | 2 tables | an empty list at first; grows with findings |
| `replica.md` per domain | how the mock differs from the service, its rejected values, and the gaps runs found | hand-written | 2.2–3.6 KB | a short start; grows with findings |
| `reader.py`, `variants2.py`, `scenario.py`, `policy.py`, `bundle.py` | the actor of each domain (and Calendar's fixed today), display names, the fields that must stay unique in a clone, Slack's reaction list, identifying fields | hand-written | ~20 lines | 2–5 lines |
| the fact catalog and model (`domains/<d>/model.json`, `catalog/<d>.json`) | the domain's facts, kinds and substitutes | domain model | – | the modeling work: the source inventory is automatic; the conceptual decisions in `model.json` are manual |
| `runtime.py` | Slack's separate path (install, visibility certification), from the Slack campaign | hand-written | 996 lines | nothing: new domains use the custom path |

## A new domain: what we would add

After the mock's eight steps (schema, routes, mount, enum, seed script, seed data, Docker), the new service has a seed
script with `Base.metadata`, and the benchmark lists its API docs. Our additions:
1. **The domain model and fact catalog.** The source inventory and the catalog come from tools
   (`grounding/modeling/inventory`, `catalog/facts.py`). The conceptual decisions in `model.json` are the modeling
   protocol's manual research, measured in days. This is the one large item. It is the intended input, not hidden
   code.
2. **Read probes:** a list of the read calls that show each kind of record. About 30–50 lines, 1–2 hours.
3. **Seed guidance:** a `seed_ops.md` that covers the generic `row` operation, the actor and a handful of default
   people, which is 1–2 hours. Convenience operations like the existing ones are another ~100 lines, and optional.
4. **Runtime constants:** the API path prefix, a lock key and any volatile tables. Under an hour.
5. **Small tables:** the actor line for the reader, the display name, and unique id fields for clones. Minutes.
6. **Replica notes:** a short first version; they grow with what runs find.

The code comes to roughly 50–200 lines on our side, plus two short notes. The domain model is the real cost, and it
is an input by design.

## Findings that could hurt automation

1. **The seed conventions encode decoy design.** The default people include near-miss pairs chosen for F8 decoys,
   such as Box's Maya Chen and Maya Lopez. The writers lean on them, which feeds the copying found in the
   [overfit audit](overfit_audit.md). That is design knowledge hiding in seed defaults.
   - **Proposed:** state in the method that default people are neutral, and have writers create decoy people
     themselves; or keep the pairs and say so in `seed_ops.md`.
2. **The Linear and Slack seed builders run through the hand-made studies' code.** `LinearSeed` and `SlackSeed` wrap
   `Seed` classes from `fact_coverage_01/pilot/cases_linear.py` and `fact_coverage_02/scenarios_slack.py`, so the
   generator depends on modules written for hand-built scenarios.
   - **Proposed:** move those two classes into the kit, unchanged, so that the generator no longer imports study
     code.
3. **The read probes are hand-written API knowledge.** They could be derived from the API docs the solver receives,
   or from the mock's routes. Since a new domain needs only one list of calls, this is an option, not a need.
4. **The fields a clone must change are a hand-written list** (identifier, number, url, slug, ts, iCalUID, ...).
   - **Proposed:** derive them from the schema's unique constraints, which the metadata already holds.
5. **The facts left out for replica gaps are hand-written** from what runs found. The pre-checks already detect an
   unreadable deciding value (the observability check), so the list could be kept from their findings.

None of these blocks adding a domain. Items 2 and 4 are small refactors; items 1, 3 and 5 are choices to discuss.

## The PI's reading (2026-09-27)

- **Inputs:** hand-written lists supplied to the pipeline, such as the read probes (item 3) and the unique fields
  (item 4), count as part of its input, like the domain model.
  - They are small, so they are not a worry.
  - To remove them from the input later, we can test whether simple prompting of an LLM or coding agent, followed by
    some processing of ours, yields the same lists.
- **Derivation:** what can be detected reliably, such as the replica-gap exclusions (item 5), is a quality-of-life
  improvement. It would then be derived as part of the automation instead of being supplied as input.
- **Principles:** communicating through principles, backed by few-shot examples, is fine.
