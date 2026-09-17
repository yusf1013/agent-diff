You design one realistic assistant task for a benchmark. Produce a short test sketch, not a database or an assessment of a solver. Your assignment fixes the referent entity, complete identifying route and resolution mode. A compiler will instantiate your sketch in an existing environment and code will assemble its grounding cards. An independent reviewer will examine the final result. Use only the supplied domain/API capabilities.

Follow these steps:
1. Read the assigned route from the requested subject through its relationships. Choose ordinary identifying conditions on attributes or relations along that route. Explain the same-record bindings in one sentence when needed. Make path conditions do real identifying work: do not pre-resolve a person by a unique full name while stating the intended role as background, or substitute a root-topic query inside an already fixed workspace for identifying channels by their workspace. The whole route must help select the subject; displaying a related fact after independently identifying it does not exercise that route.
2. Choose a natural user purpose. Prefer a consequential supported operation, or a concrete open-ended question whose answer depends on the selected records. For example, ask which locations a set of messages names rather than merely “find messages.” Association entities may be reported as person–channel/workspace/emoji relationships. Do not disguise a different referent as the assigned entity.
3. Establish the intended selection. single requests one entity (or explicitly delegates choosing one); multiple requests a jointly intended collection, even when this particular seed supplies only one match; never add a positive to a mutation just to make that count exceed one; absent has no match; underspecified leaves the user's intended selection unresolved, with no delegated choice. For underspecified, supply partial identifying information on an actual path field (e.g. a shared first name within full names), and design at least two distinct possible referent sets. Ambiguity alternatives are not negatives. Do not announce ambiguity in the user's prompt.
4. Sketch matching or competing records, then plausible negatives that challenge conditions along the path: different value, missing relationship, wrong relationship role, or conditions split across different joined records. There is no fixed count of conditions/negatives. Include a few useful distinctions without enumerating combinations. Every negative must really be excluded by the ordinary request. Negation alone does not establish exclusion: a canceled meeting can still concern meeting confirmation/status. An office-move announcement used as a negative for deployment must not also discuss deployment.
5. Write one short natural request. Use ordinary plural wording for a collection, no emphatic ALL/EVERY. Avoid answer-revealing labels, test terminology, hinted decoys, candidate menus, or suggested search steps. A decoy must not say “not the answer,” “ignore this,” or similar guidance. Exact #channel names have literal identity; vague organizational words can be broader. Avoid gray exclusions. Lock this prompt for compilation.
6. Check discoverability and seed interaction. The supplied base seed remains; add coherent ordinary records and necessary access memberships. Existing records may also match, so account for them. Preserve base content/identities unless an explicit justified change is necessary. Channel list/history/reaction/member/user information can support open-ended discovery. Only if no supported discovery route exists may the request supply a candidate scope; record the limitation and scope explicitly. Do not introduce a candidate list just to simplify authoring.
7. Record minimal grounding and action metadata so the compiler binds roles rather than reinventing the task. Consolidate repeated references. Include independently needed destinations/people as additional obligations; don't split every intermediate relation into a separate obligation. The main obligation is first. Action lines retain the prompt's work, branches and necessary sequencing, with direct one-based obligation links. No implementation search/read steps unless separately requested.

Return JSON:
{
 "prompt":"exact final user request",
 "binding_note":"brief relevant binding or ambiguity explanation",
 "roles":[{"role":"stable semantic label","entity":"native table name (e.g. users, not USER)","facts":"short concrete environment sketch","selection":"match|alternative|negative|support","reason":"why"}],
 "obligations":[{
  "name":"short reference name","description":"what is selected and used for; express selection constraints",
  "table":"native referent table","mode":"single|multiple|absent|underspecified",
  "task_type":"read-only|state-changing","scope":"ordinary requested scope",
  "target_roles":["role labels"],"candidate_role_sets":null,
  "selection":"one|set",
  "answer_attributes":[["table.real_field"]],
  "change_attributes":[[]],"written_attributes":[]
 }],
 "task_spec":[{"line":1,"text":"requested work","obligations":[1]}],
 "scope_exception":null,
 "access_plan":"brief documented way to discover the population and identifying evidence"
}
For underspecified use concrete candidate_role_sets as a list of role-label sets; target_roles is their union. All target_roles and candidate_role_sets contain ONLY roles of that obligation’s referent table, not intermediate supporting records. Absent target_roles is empty. Roles are conceptual construction handles, not names revealed to the solver. Use real source fields; descriptions carry semantic information that isn't a field. Computation attributes are nested alternative sets; use null where unestablished. Written attributes describe task-directed assignments, [] for removal. For read-only omit change_attributes/written_attributes; for state-changing omit answer_attributes. If a required capability is genuinely unavailable, return {"unrealized_reason":"specific explanation"} instead of pretending.

Calibration examples (style and principles, not cases to copy):
- Message → Reaction → User. “Add a star to messages Tom reacted to with a thumbs up.” Two Tom👍 matches; Tom👀, Tim👍, no reaction, and Tom👀 plus Tim👍 are plausible negatives. All conditions must bind the same reaction. Message content remains ordinary.
- User → Reaction → Message. “DM the person who reacted with ✅ to the deployment announcement: ‘Ready for the review?’” Maya✅deployment matches; Omar👍deployment, Lara✅office move, and Tim merely authoring deployment do not. Never let the office-move text incidentally become deployment-related.
- Conversation → Message → Reaction → User. “Which channel has the deployment announcement Alex reacted to with 👍?” Alex Chen and Alex Patel in different channels give unresolved alternatives. Reporting both mapped alternatives or asking which Alex is appropriate. Do not announce the two people in the request.
