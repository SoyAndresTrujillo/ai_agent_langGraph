## Init project
```bash
uv init
uv venv
```
## Add dependencies
```bash
uv add --pre langgraph langchain langchain-openai
uv add "langgraph-cli[inmem]" --dev
```

## Add ipykernel for jupyter
```bash
uv add ipykernel --dev
```

## Run the agent
```bash
uv run langgraph dev
```


## Before organize our project and compile the project
```toml
[tool.setuptools.packages.find]
where = ["src"]
include = ["*"]
```
```bash
uv pip install -e .
```