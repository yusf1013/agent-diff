"""New stage-separated runs, with read compatibility for saved writer pilots."""
from pathlib import Path


def case_root(folder, case_id):
    return Path(folder) / 'cases' / case_id


def writer_root(folder, case_id):
    current = case_root(folder, case_id) / 'generation'
    historical = Path(folder) / case_id
    if not current.exists() and historical.exists():
        return historical
    return current
