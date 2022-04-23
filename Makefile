install:
	poetry install
test: install
	poetry run pytest
type_check:
	poetry run mypy src