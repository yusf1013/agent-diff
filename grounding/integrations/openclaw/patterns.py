"""Reply patterns shared by the OpenClaw runner and its analysis (no heavy imports)."""
import re

# The reply asks the user something: a proposal to confirm or a clarifying question.
QUESTION = re.compile(r"\?\s*(\*|_|`)*\s*$|\?\s*\n|\bshould I\b|\bwould you like\b|\bdo you want\b|\bshall I\b|"
                      r"\bplease confirm\b|\bconfirm\b[^.]*\?", re.I)
