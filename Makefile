install:
	@poetry install

start:
	@poetry run uvicorn run:app --reload --host 127.0.0.1 --port 80

lint:
	@poetry run flake8 app