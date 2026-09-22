# Linear modeling contextualization

Apply [the adopted protocol](../../protocols/conceptual_meta_model.md) to repository revision `4691d3f076db2cdcccdc840c110aa797fa3196dc`. The scope is the replica's full domain-bearing persistence and mounted GraphQL API, not only issue/project features used by existing tests.

Authoritative persistence: [database/schema.py](../../../backend/src/services/linear/database/schema.py), including standalone association `Table` definitions and all ORM classes. API mounting in [platform main.py](../../../backend/src/platform/api/main.py) loads [Linear-API.graphql](../../../backend/src/services/linear/api/schema/Linear-API.graphql) with `bindables` from [resolvers.py](../../../backend/src/services/linear/api/resolvers.py). [graphql_linear.py](../../../backend/src/services/linear/api/graphql_linear.py) supplies actor/session context. Supporting documentation: [local API document](../../../examples/linear/testsuites/linear_docs/linear_api_full_docs.json) and schema descriptions.

Required contextual distinctions:

- Inventory the full GraphQL root contract and separately identify explicit resolver bindings. A declared field without a resolver is not implemented merely because it appears in the schema. Object fields may use default attribute resolution; inspect ORM properties, not just decorated resolvers.
- Preserve connection wrappers versus actual relationships. A Python list returned by default resolution does not itself implement a GraphQL connection's `nodes` or `edges` fields. Follow custom connection adapters and nested response dictionaries.
- Plain pair-key association tables become relationships. Independently identified or attributed associations remain candidate entities. Do not create one entity per table automatically.
- Preserve parallel roles such as assignee, creator and delegate, and source versus target. Self-links remain in the model even though the Slack-comparable route enumerator excludes repeated entity types.
- JSON identifier lists and relational associations may coexist without synchronization. Only consolidate when handlers establish equivalent meaning; preserve discrepancies otherwise. Structured content and placeholder fields do not establish missing managed entities.
- A model class with only a few stored fields is not equivalent to the rich public GraphQL object. Account for unimplemented fields, fixed values and incomplete nested representations rather than importing production behavior.
- Inspect shared search/filter/pagination helpers and inline serializers. Follow actual functions called by registered resolvers; unused helper definitions do not establish exposed capabilities.

These contextual rules specialize the adopted mappings without extending the generic protocol. The earlier `grounding/linear.md` public-service draft excludes replica concepts and cannot be adopted unchanged.

Database-definition cross-checks include the migrations for
[relation title snapshots](../../../backend/src/platform/db/migrations/versions/4e7f9b2c1d8a_add_issue_relation_titles.py),
[JSONB storage](../../../backend/src/platform/db/migrations/versions/68296ff4834d_linear_json_to_jsonb.py),
and [query indexes](../../../backend/src/platform/db/migrations/versions/9d2f4ac1cd31_linear_query_indexes.py).
The snapshots already appear in the model; format conversions and nonunique
indexes add no conceptual identity or relationship. The
[seeder](../../../backend/utils/seed_linear_template.py) creates all metadata tables.
The completion audit records these checks and source hashes.
