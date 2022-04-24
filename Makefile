install:
	poetry install

test:
	poetry run pytest tests/

type_check:
	poetry run mypy src

lint:
	poetry run flake8 --ignore=E501