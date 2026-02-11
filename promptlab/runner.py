"""Run prompt tests against Ollama."""
import requests
import re
from typing import List, Dict, Any

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_tests(tests: List[Dict], model: str = "llama3.2", verbose: bool = False) -> List[Dict[str, Any]]:
    results = []
    for test in tests:
        result = run_single(test, model=test.get("model") or model, verbose=verbose)
        results.append(result)
    return results

def run_single(test: Dict, model: str, verbose: bool = False) -> Dict[str, Any]:
    result = {"name": test.get("name", "unnamed"), "passed": False, "output": ""}
    try:
        resp = requests.post(OLLAMA_URL, json={
            "model": model,
            "system": test.get("system", ""),
            "prompt": test["prompt"],
            "stream": False,
        }, timeout=60)
        resp.raise_for_status()
        output = resp.json().get("response", "")
        result["output"] = output
        result["passed"] = check_assertions(output, test.get("assertions", []))
    except Exception as e:
        result["error"] = str(e)
    return result

def check_assertions(output: str, assertions: List[Dict]) -> bool:
    for a in assertions:
        if "contains" in a:
            if a["contains"].lower() not in output.lower():
                return False
        if "not_contains" in a:
            if a["not_contains"].lower() in output.lower():
                return False
        if "matches" in a:
            if not re.search(a["matches"], output, re.IGNORECASE):
                return False
        if "max_length" in a:
            if len(output) > a["max_length"]:
                return False
    return True
