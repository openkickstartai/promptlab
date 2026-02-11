"""CLI entry point."""
import click
from promptlab.runner import run_tests
from promptlab.loader import load_test_suite

@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--model", default="llama3.2", help="Ollama model")
@click.option("--verbose", "-v", is_flag=True)
def main(path, model, verbose):
    """Run prompt tests."""
    suite = load_test_suite(path)
    results = run_tests(suite, model=model, verbose=verbose)
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    click.echo(f"\n{passed}/{total} tests passed")
    raise SystemExit(0 if passed == total else 1)
