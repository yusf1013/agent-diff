Compile the supplied conceptual sketch into a fresh executable Slack environment.
The assignment, exact request, selection-condition text and table facts are fixed.
You supply native records and a faithful structured selector, not a new test design.
Domain capabilities and setup requirements are supplied; do not independently
investigate API accessibility or invent new prerequisites.

Work in this order:

1. Translate the stated selection conditions to the supplied restricted selector
   syntax, using the assigned native route and real fields. Keep conditions on a
   shared record bound together. Use visible identifying values, not target IDs
   or a scope limited to the desired answers. Do not add restrictions missing from
   the condition text. If it conflicts with the request or table, report the
   specific design conflict; do not silently reconcile them. For semantic text
   conditions, a substring is only a concrete encoding to review, not a proof of
   equivalent meaning. Python cannot repair an inaccurate interpretation for you.
2. Instantiate every table row in one fresh environment. Bind each row number to
   its selected root and supporting records. Distinct roots stay distinct; shared
   people/messages retain the same facts throughout. Supply the runtime actor and
   necessary workspace, users, channels and memberships under the domain contract.
   Count setup records when they participate in a condition. For a negative,
   preserve all its specified passing conditions and its specified failure.
3. Add ordinary background activity without additional matching roots or new
   competing interpretations. Keep content plausible and varied, with ordinary
   names and neutral IDs. Do not expose row labels, match status, answer hints or
   test-construction commentary in solver-visible data. Do not make one target
   conspicuously richer than its near misses. Preserve literal names, topics and
   relationships from the sketch; fill unspecified details coherently. Background
   volume need not be large, but the world should not be just a displayed answer
   table. Keep dates, reply order and membership facts consistent.
4. Recompute the selection across ALL constructed records, including setup and
   filler. Repair accidental relationships or content that you introduced while
   preserving the sketch. If the requested distinctions cannot coexist, report a
   design conflict. Never weaken the selector, discard a required row, alter the
   intended count or relabel a nonmatch to make a failing compilation pass.

Return JSON with exactly these four fields:
- seed: the complete fresh data, mapping the seven supplied table names to arrays
  of native rows. Use required fields and fields needed by the story; omit unused
  optional fields. Native identifiers are strings. Supply timestamps where needed.
- row_bindings: one entry per numbered story row, in order:
  {"row":1,"referent":native_handle,"support":[{"table":"users","handle":"native ID"}]}.
  A single-key handle is a string; an association handle contains exactly its PK
  fields. Support lists the concrete records realizing the row's facts. A referent
  may be null only for a negative supporting chain whose root does not exist.
  Do not return your own match/negative labels; code obtains those from the story.
- selector: the supplied restricted query object. This is private metadata,
  never solver context. Once a structurally valid selector has been returned,
  repair turns must preserve it exactly. A necessary selector revision is reported
  as a conflict for separate review, not made to force agreement with your seed.
- annotation: {"name":"brief obligation name","scope":"scope stated by the request",
  "task_type":"read-only|state-changing","computation_attributes":[["table.column"]],
  "written_attributes":["table.column"]}. These are minimal semantic inputs for
  mechanical card assembly, not complete cards. Read actions use [] for written
  attributes. Include only substantive requested writes, excluding authentication-
  supplied actor fields. Attribute names contain no literal values or assignments.

Alternatively return only {"design_defect":"specific conflicting requirements"}.
The adapter attaches the exact request, assignment, intended sets, task line and
fixed card fields. Do not repeat them or write oracle/evaluation criteria. Return
one complete JSON object, without a long audit. Validation feedback, if any, will
be a continuation of this conversation; make only the required concrete repairs.
