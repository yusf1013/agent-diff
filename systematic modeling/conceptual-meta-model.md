# Conceptual modeling meta-model

Use the implementation as the specification, and derive a simpler model from it
through explicit mapping rules. This document records the method for building the
conceptual model; it does not describe the domain itself.

Completeness is relative to the implemented Slack replica at a recorded revision.
The mappings below are an initial set for this system, not a universal catalog.
Extend them only when inspection finds an uncovered construct with domain meaning.

## 1. Inputs and authority

| Input | Purpose |
|---|---|
| Database definitions | Extract candidate entities, attributes, identities, relationships, cardinalities, and states from tables, columns, keys, and constraints. |
| API implementation | Complete and interpret the structural model by inspecting registered endpoints and the executable paths they call, including any additional storage they use. |
| API documentation (supporting) | Clarify the meaning of endpoint inputs and outputs, domain terminology, and documented relationships or classifications; check those interpretations against implementation. |

The first two inputs are authoritative. Documentation helps interpret them but
does not establish implemented support. Record disagreements rather than silently
adopting documented or assumed behavior.

## 2. Contextualization before extraction

Before producing the conceptual model or coverage ledger, inspect the system's
database definitions, API implementation, and API documentation to contextualize
this method. Establish the authoritative source locations, how registered API
operations lead to their implementations, and the documentation's interpretive
role. Check whether the mapping rules cover the constructs actually used.

Treat every edit as expensive: change the method only when inspection reveals
something it would otherwise miss or interpret ambiguously. Another instance of
an already-covered construct requires no addition. Record only necessary source
locations and system-specific instructions, without embedding entity or endpoint
inventories. Review the contextualized method before using it to produce the
conceptual model and ledger.

## 3. Database-to-model mapping

Start with the database ER structure. Treat each interpretation as a candidate;
preserve domain meaning without requiring one conceptual entity per table.

| Database construct | Initial conceptual interpretation |
|---|---|
| Table with its own identity | Candidate entity |
| Foreign key | Candidate relationship |
| Association table | Relationship, possibly with attributes |
| Ordinary column | Candidate attribute |
| Enum or status flag | Candidate state or classification |
| Primary or unique key | Identity or uniqueness information |
| Nullability and foreign-key uniqueness | Evidence for relationship optionality and cardinality |

Database constraints describe what storage enforces. Any stronger conceptual
cardinality needs implementation evidence or an explicit unresolved qualification.

## 4. API-to-model mapping

For each registered operation, ask: **What domain object, attribute, relationship,
or state does this operation receive, reference, or return?**

| API construct | Initial conceptual interpretation |
|---|---|
| Domain objects and fields in inputs or outputs | Candidate concepts and attributes, mapped to existing candidates where possible |
| Object identifiers and references | Identity information and candidate relationships |
| Interpretation of stored flags or values | Meanings of states and classifications |
| Information computed from records | Derived attributes, relationships, or groupings |
| Domain information represented outside the database | Candidate additions to the structural model |
| Fixed domain values in responses | Represented constants; do not infer variable state or implemented capability |

Action preconditions, effects, and errors belong in the behavior model. Interface
mechanics such as pagination belong there when relevant to agent observation;
they do not automatically become domain concepts.

## 5. Coverage ledger

Keep one working ledger separate from the conceptual model:

| Source element | Disposition | Model destination or reason |
|---|---|---|
| Exact source reference | Represented / derived / deferred / omitted | Conceptual location, derivation, later artifact, or omission rationale |

Account for every database table and registered endpoint. Within each, account for
domain-bearing fields and relationships; group fields with the same treatment.
Endpoint-level mapping alone is insufficient when individual fields introduce
additional domain meaning. A row for every line of code is unnecessary.

### Bidirectional coverage and dedicated reverse audit

- **Source to model:** Check that the complete scoped source inventory has a
  disposition and review its mappings. Deferrals and omissions need a short reason;
  derivations identify their basis. Enumeration checks establish that elements are
  accounted for, not that their interpretations are correct.
- **Model to source:** After drafting, perform a dedicated reverse audit starting
  from every model element: vocabulary, entities, identities, attributes,
  relationships, cardinalities, states, classifications, and derived representations.
  Check that the cited implementation supports each statement's meaning and strength,
  including the diagram and its notation. A source reference alone is insufficient.

Correct, remove, or explicitly qualify claims that exceed their evidence. Record
the reviewed model elements, source support, corrections, and remaining
qualifications in the existing ledger; no additional artifact is required. Claim
audited bidirectional coverage only after both passes are complete. This establishes
coverage within the recorded implementation scope, not proof of runtime correctness.

## 6. Conceptual model structure

| Section | Contents |
|---|---|
| Scope | Implemented replica, implementation revision, and abstraction boundary |
| Vocabulary | Concise domain definitions and mappings between domain and implementation terminology |
| Entity–relationship model | Entities, identities, attributes, relationships, and cardinalities, together with the ER diagram and necessary qualifications |
| States and classifications | Relevant values and meanings, distinguishing stored from derived information; transitions belong in the behavior model |

Vocabulary defines terms; the ER section owns their structural detail. Do not add
separate sections for descriptive information or supporting concepts.

## 7. Simplification and validation

**Retain domain distinctions; consolidate their representations.** A derived
grouping need not become an independent entity, and a computed attribute need not
be represented as independently stored state. Storage optimizations and interface
packaging need no conceptual counterpart unless they carry domain meaning.

Record implementation inconsistencies rather than making the model silently more
consistent than the system. Use targeted concrete situations to validate mappings
where consolidation or derivation could lose meaning. These checks supplement the
coverage ledger; they do not substitute for systematic coverage.

## 8. Stopping condition

The extraction is complete when:

- All persistence structures and registered API paths have been inspected.
- Their conceptual information has a disposition in the ledger.
- Every model element has source support or an explicitly marked interpretation.
- Both coverage passes, including the dedicated reverse audit, are complete and
  recorded in the ledger.
- Unresolved interpretations and implementation discrepancies are recorded.
- Mappings at risk of losing domain meaning have received targeted validation.

Recorded unresolved issues qualify the result; they are not evidence that an
interpretation has been validated.

This establishes a bounded, reviewable completeness argument: the model preserves
the domain information in the chosen implementation while deliberately simplifying
how that information is represented.
