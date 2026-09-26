"""Write inputs/<domain>/api.md: the API documentation part of the solver's own system prompt, verbatim.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.inputs.make_api
"""
from __future__ import annotations

from pathlib import Path

from grounding.integrations.agentdiff import smoke_runtime as smoke

HERE = Path(__file__).resolve().parent
MARK = "## API Documentation"


def main():
    for domain in ("box", "calendar", "linear", "slack"):
        text = smoke.official_prompt(domain)
        docs = text[text.index(MARK) + len(MARK):].lstrip()
        (HERE / domain / "api.md").write_text("# API documentation given to the solver\n\n"
                                              "The solver receives exactly this documentation in its system prompt, "
                                              "with instructions to use curl against the base URL.\n\n" + docs + "\n")
        print(domain, len(docs))


if __name__ == "__main__":
    main()
