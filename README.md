# promptlab

LLM prompt testing framework. Write test cases in YAML, run against Ollama models.

## Install from source

```bash
git clone https://github.com/openkickstartai/promptlab.git
cd promptlab
pip install -e .
```

## Usage

```bash
promptlab run tests/
promptlab run tests/ --model llama3.2
```

## Testing

```bash
pip install pytest
pytest -v
```
