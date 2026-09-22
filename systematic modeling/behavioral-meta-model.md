# Behavioral modeling meta-model

Describe how the implemented system responds to actions, using the conceptual
model's vocabulary. An operation relates actor/context, input, and initial state
to an observation and resulting state. Read operations belong here too: their
selection and returned information are behavior even when domain state is unchanged.

Completeness is relative to the recorded implementation revision and request
boundary. This is an initial method to contextualize before extraction.

## 1. Inputs and authority

| Input | Purpose |
|---|---|
| Reviewed conceptual model and its ledger | Reuse entities, identities, relationships, and states; take up behavior-related deferrals and qualifications. Do not repeat the ER model. |
| Executable implementation | Establish actual behavior through dispatch, handlers, called helpers, queries, serializers, and relevant middleware, transaction handling, database constraints, and ORM cascades. These are parts of one implementation input. |
| API documentation (supporting) | Interpret operation intent and parameters; identify discrepancies with implementation. Documented behavior alone does not establish support. |

The conceptual model guides interpretation; executable implementation remains the
authority. If behavioral inspection exposes a conceptual omission or overstatement,
record and resolve it explicitly rather than silently inventing a parallel concept.
Conceptual classifications do not themselves establish permissions or transitions.

## 2. Contextualization before extraction

Inspect the inputs to locate the complete operation boundary and determine whether
the mappings below need additions or clarification. For each proposed change ask:
**What would we miss or interpret ambiguously without this change?** Another instance
of an already-covered construct requires no addition.

Record contextualization separately, labeling findings as **source instruction**,
**candidate mapping addition**, or **existing mapping clarified**. Keep the generic
method unchanged. Review contextualization before producing the behavioral model
and its ledger.

## 3. Implementation-to-model mapping

| Implementation construct | Initial behavioral interpretation |
|---|---|
| Dispatch entry and request context | Operation identity, accepted entry forms, actor, and relevant configuration |
| Parameter reads, defaults, parsing, and reference resolution | Accepted inputs, normalization, omitted-value handling, and target selection |
| Guards, permission checks, and validation | Conditions for success or failure; preserve evaluation order when it changes the observable outcome |
| Queries, filters, ordering, and pagination | Which domain objects are observable, in what order, and how results are bounded or continued |
| Writes, database constraints, and ORM cascades | State effects, indirect effects, and failures imposed by persistence |
| Returns, serialization, and exception handling | Returned observations, derived/constant/transient values, and error outcomes |
| Commit, rollback, and multi-item processing | Which effects persist for each outcome, including partial success, failure, or no change |

Trace each operation through its effective call path. A handler returning an error
does not by itself establish rollback. A familiar operation name does not establish
permissions, idempotency, or any other unstated contract.

## 4. Behavioral model structure

| Section | Contents |
|---|---|
| Scope | Implementation revision, referenced conceptual model, request boundary, and relevant configuration assumptions |
| Shared rules | Reused parsing, lookup, visibility, serialization, error, or persistence rules, defined once and explicitly referenced by applicable operations |
| Operation contracts | Inputs/context, target selection and guards, outcome cases, and source evidence for each distinct operation |

Within an operation contract, an outcome case has this compact form:

| Condition | Returned observation | Resulting domain state |
|---|---|---|
| Input/state/context condition selecting this case | Relevant success/error response and information exposed | Changes, indirect effects, or no change, including what is committed |

Use parameterized rules for collections and values rather than enumerating every
possible input. Include failure and already-satisfied cases where implemented.
Describe repeat-call behavior when it follows from these cases; do not assume that
repeating a successful action is harmless. Separate state-transition diagrams or
error catalogs are optional views, not required additional sections.

## 5. Coverage ledger and bidirectional audit

Maintain one behavioral ledger with **source element**, **disposition**, and
**model destination or reason**. Reuse the dispositions represented, derived,
deferred, and omitted. Reference the conceptual ledger rather than copying it.

**Source to model:** Account for every registered operation and its materially
distinct implemented cases. A distinction matters when it changes request acceptance,
target selection, returned information, or persistent effects. Include shared rules
and indirect effects on those paths. Every behavior-related conceptual deferral
must have a destination or an explicit reason it is outside the behavioral scope.

An operation name alone is insufficient coverage. Conversely, equivalent branches
can share a rule when their conditions and outcomes are preserved. Coverage concerns
rules and cases, not every possible data value or execution sequence. Unreachable
helpers do not establish public operations, and a stored entity creates no obligation
to invent CRUD capabilities; constraints and indirect effects involving it still count.

**Model to source:** After drafting, perform a dedicated reverse audit of every
contract and shared rule. Verify conditions, permissions, observations, transitions,
failure effects, and claims of no change, atomicity, or repeat-call behavior against
the implementation. A claimed global invariant requires support across all relevant
operations; otherwise state its narrower applicability. References alone do not
establish correctness.

Record audit results, corrections, and remaining qualifications in the same ledger.
This establishes model coverage of implementation behavior, not test-suite coverage
or proof of runtime correctness.

## 6. Simplification and validation

Retain distinctions an agent can observe or that affect domain state. Consolidate
repeated implementation into shared rules without erasing operation-specific
differences. Do not reproduce source control flow, entire JSON payload templates,
or conceptual entity definitions when a referenced rule expresses their meaning.

Use targeted source checks or isolated execution where interpretation is uncertain,
particularly for indirect effects, error/commit boundaries, and repeat calls.
Validation supplements systematic coverage; it does not substitute for it. Record
implementation inconsistencies rather than replacing them with intended behavior.

## 7. Stopping condition

- All scoped operations, meaningful cases, and shared rules have ledger dispositions.
- Behavior-related conceptual deferrals have been reconciled.
- Every behavioral claim has reviewed source support or an explicit qualification.
- Both coverage passes, including the dedicated reverse audit, are recorded.
- Interpretations at risk of losing observable behavior have received targeted checks.

Unresolved issues qualify the result; recording them does not validate the disputed
behavior. Task design, scenario selection, and evaluation assertions belong to the
subsequent testing model.
