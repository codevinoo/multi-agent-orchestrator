.PHONY: install demo test clean

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

demo: install
	$(PYTHON) -m orchestrator run --goal "Research and summarize distributed consensus"

test: install
	$(PYTHON) -m pytest tests/ -v

clean:
	rm -rf .venv __pycache__ **/__pycache__
