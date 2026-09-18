"""JSON-lines bridge to the repository's BashExecutorProxy, inside Docker."""
import json
import os
import sys

from code_executor import BashExecutorProxy

executor = BashExecutorProxy(
    os.environ["EVAL_ENV_ID"], base_url=os.environ["EVAL_BASE_URL"]
)
try:
    for line in sys.stdin:
        request = json.loads(line)
        result = executor.execute(request["command"], timeout=request.get("timeout", 30))
        print(json.dumps(result), flush=True)
finally:
    executor.destroy_workspace()
