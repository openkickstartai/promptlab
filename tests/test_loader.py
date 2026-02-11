"""Tests for loader module."""
import os
import tempfile
from promptlab.loader import load_test_suite

def test_load_yaml_file():
    content = """system: You are helpful\ntests:\n  - name: greeting\n    prompt: Say hello\n    assertions:\n      - contains: hello\n"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(content)
        f.flush()
        tests = load_test_suite(f.name)
    os.unlink(f.name)
    assert len(tests) == 1
    assert tests[0]["name"] == "greeting"
    assert tests[0]["system"] == "You are helpful"

def test_load_empty_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write("")
        f.flush()
        tests = load_test_suite(f.name)
    os.unlink(f.name)
    assert tests == []

def test_load_directory():
    with tempfile.TemporaryDirectory() as d:
        for i in range(3):
            with open(os.path.join(d, f"test_{i}.yml"), "w") as f:
                f.write(f"tests:\n  - name: t{i}\n    prompt: test {i}\n")
        tests = load_test_suite(d)
        assert len(tests) == 3
