"""Repository locations and lookup for paths retained in historical evidence."""
from pathlib import Path
import json

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = REPO_ROOT / 'grounding'
PROMPTS = PROJECT_ROOT / 'prompts'
RUNS = PROJECT_ROOT / 'runs'
CONFIG = json.loads((PROJECT_ROOT / 'configs/current.json').read_text())
SLACK = REPO_ROOT / CONFIG['paths']['slack_domain']


def configured_path(key):
    return REPO_ROOT / CONFIG['paths'][key]


def relocate(value):
    """Resolve a current/old repo path without changing the recorded evidence."""
    path = Path(value)
    if path.is_absolute():
        try:
            relative = path.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            return path
    else:
        relative = path.as_posix()
    rules = json.loads((PROJECT_ROOT / 'relocation.json').read_text())['paths']
    for old, new in sorted(rules.items(), key=lambda pair: len(pair[0]), reverse=True):
        if relative == old or relative.startswith(old + '/'):
            return REPO_ROOT / (new + relative[len(old):])
    return REPO_ROOT / relative


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path')
    print(relocate(parser.parse_args().path))
