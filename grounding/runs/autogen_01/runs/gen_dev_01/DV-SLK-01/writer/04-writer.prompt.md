A cold reader, who saw only the request and then the records, reports:
- The reader finds the phrase "Site Reliability Engineer" ambiguous in a way that changes which records match: Strict title match yields Sofia, Lukas, Noah. A looser reading crediting Marta's display_name text would add Marta, tying with Sofia and breaking uniqueness.
- The reader finds the phrase "the active ... Engineer" ambiguous in a way that changes which records match: Strict reading gives one match, Sofia. Combined with the looser SRE reading including Marta, uniqueness breaks.

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.