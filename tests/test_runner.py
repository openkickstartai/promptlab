"""Tests for assertion checker."""
from promptlab.runner import check_assertions

def test_contains_pass():
    assert check_assertions("Hello world", [{"contains": "hello"}])

def test_contains_fail():
    assert not check_assertions("Goodbye", [{"contains": "hello"}])

def test_not_contains():
    assert check_assertions("Safe output", [{"not_contains": "error"}])
    assert not check_assertions("Has error here", [{"not_contains": "error"}])

def test_matches_regex():
    assert check_assertions("The answer is 42", [{"matches": r"\\d+"}])
    assert not check_assertions("No numbers", [{"matches": r"^\\d+$"}])

def test_max_length():
    assert check_assertions("short", [{"max_length": 100}])
    assert not check_assertions("x" * 200, [{"max_length": 100}])

def test_multiple_assertions():
    assert check_assertions("Hello world 42", [
        {"contains": "hello"},
        {"not_contains": "error"},
        {"matches": r"\\d+"},
    ])

def test_empty_assertions():
    assert check_assertions("anything", [])
