.PHONY: install test lint summary

install:
	python -m pip install -e ".[dev]"

test:
	pytest -v

lint:
	ruff check .

summary:
	python -m equity_thesis_tracker
