"""Render and structurally check this domain; not a proof checker."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _analysis_support import run
if __name__ == "__main__":
    run(Path(__file__).resolve().parent)
