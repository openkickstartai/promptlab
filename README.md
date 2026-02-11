# promptlab

LLM prompt testing framework. Write test cases in YAML, run against Ollama models.

## Install

```bash
pip install promptlab
```

## Usage

```bash
promptlab run tests/
promptlab run tests/ --model llama3.2
```

## Testing

```bash
pip install -e .
pytest -v
```
