"""Load test suites from YAML files."""
import os
import yaml
from typing import List, Dict, Any

def load_test_suite(path: str) -> List[Dict[str, Any]]:
    """Load all .yml/.yaml test files from path."""
    tests = []
    if os.path.isfile(path):
        tests.extend(_load_file(path))
    elif os.path.isdir(path):
        for f in sorted(os.listdir(path)):
            if f.endswith((".yml", ".yaml")):
                tests.extend(_load_file(os.path.join(path, f)))
    return tests

def _load_file(path: str) -> List[Dict[str, Any]]:
    with open(path) as f:
        data = yaml.safe_load(f)
    if not data or "tests" not in data:
        return []
    suite_defaults = {"model": data.get("model"), "system": data.get("system", "")}
    tests = []
    for t in data["tests"]:
        test = {**suite_defaults, **t, "source_file": path}
        tests.append(test)
    return tests
