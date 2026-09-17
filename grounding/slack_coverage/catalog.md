# Operational Slack coverage catalog

The [machine-readable catalog](catalog.json) fixes **174 complete routes, 26
identifying attributes, 28 entity–resolution-mode requirements, and 25
representative capability boundaries**. These are four separate linear
inventories, not a Cartesian product or a required number of tests. The catalog
is source-derived manual design; the script only projects its explicit choices.

The entity/attribute inventory comes from the adopted conceptual model and its
API exposure ledger. Each exposed modeled scalar identity or attribute appears
once; representation aliases are normalized and unavailable observations/effects
move into a small limitation inventory. This is the extraction discipline, not
an inventory reverse-engineered from baseline frequency.

The 174/38 route inclusion decisions are unchanged. Join fields express their
relationships; using a foreign key internally does not cover a direct-ID
attribute. Identifying text inside a message block covers the one blocks family,
not an invented entity or a cross-product of block types. Counts and existence
are predicates over relationships, not new stored attributes.

Capability rows define the representative required effect/information, including
permitted alternatives. Some require careful ordinary-language realization,
especially stored attachments/mentions; an unfaithful or contrived attempt stays
unrealized rather than being used to inflate coverage. These 25 rows implement
the agreed grouped-boundary approach, not exhaustive CRUD coverage.

Cases earn credit only for conditions they actually use to identify the
referent. Report generated assignments, validated realizations, API limitations,
and supplied-candidate-scope exceptions separately. A long path does not
implicitly cover all shorter paths. One test may cover a route, several
attributes, and one entity/mode cell simultaneously.
