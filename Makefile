install:
	@poetry install

start:
	@poetry run uvicorn run:app --reload

lint:
	@poetry run flake8 app

test:
	@poetry run python -m pytest

coverage:
	@poetry run python -m pytest --cov=app

coverage-report:
	@poetry run python -m pytest --cov=app --cov-report xml