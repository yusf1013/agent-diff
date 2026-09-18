# Independently review one constructed grounding case

Review the final request, concrete environment, cards, task specification, declared coverage assignment and mechanical findings. Construction claims are hypotheses, not authority. You have no solver response and must not estimate whether a particular agent will fail. Return JSON only.

First state your interpretation of the actual request: its focal entity, selection meaning and resolution mode. Then compare that interpretation against the construction. Check:

- The ordinary wording really uses the declared focal path/field; relational bindings and scope are preserved, and count refers to the intended distinct entities. A long route is not credited merely because those tables happen to exist.
- Single, multiple, absent and underspecified follow the request's intended selection, not raw match count. Ambiguity permits clarification or alternatives, not unilateral choice. All reported target/candidate sets agree with the full environment. No incidental filler changes them.
- Each claimed focal negative satisfies the auxiliary conditions but fails the focal condition. Could a reasonable reading legitimately include it? Relevant people/content connected in the wrong role can be good negatives. Equally legitimate ambiguous alternatives are not negatives.
- The focal distinction does useful work among plausible candidates. IDs, names, order, text or empty early anchors do not give away the answer. Requests and background are ordinary, coherent and sufficiently specified for the intended action. Do not demand extra difficulty, giant seeds or a negative for every auxiliary.
- Facts needed for this supported-route case are accessible through the supplied API for its actor and scope. Respect known profile/workspace and membership limitations. Do not certify absence from an incomplete search population.
- Cards obey the fixed schema, include the actual requested reference subjects, consolidate repetition, and preserve the request's quantities/discretion. Task lines preserve requested actions, branches and sequence, with direct links. Do not impose a particular solver search strategy or grade downstream semantic quality.
- For mutations, the focal path/entity and requested operation are preserved. Enrichment adds natural qualifiers without deliberate negatives; near-miss stages preserve the supplied request and modify only the environment as declared. No invented easy counterparts.

Explain concrete defects with record IDs/fields and the affected phrase. Do not reject a coherent case because you personally prefer another ordinary scenario. Report uncertain semantic conflicts as unresolved rather than silently approving them. Mechanical checks and your review have different limits; a passing query does not prove that prose means that query.

Return:
{"interpretation":{"referent_entity":"...","mode":"single|multiple|absent|underspecified","selection":"..."},"checks":[{"name":"prompt_path_fidelity|resolution|negatives|realism_and_hints|api_scope|cards_and_spec|mutation_integrity","status":"pass|fail|unresolved","evidence":"..."}],"decision":"pass|fail|unresolved","issues":["specific correction or uncertainty"]}

Include each of the seven named checks once. Pass requires all seven pass. For an initial enrichment where no negative is required, explain that the negative requirement is not applicable and mark that check pass. For clean generation, mutation_integrity checks the locked assignment and absence of extra counterparts. No new output fields.
