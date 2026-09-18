"""Render and structurally check this domain; not a proof checker."""
from pathlib import Path
import sys
from grounding._analysis_support import run
if __name__ == "__main__":
    run(Path(__file__).resolve().parent)
