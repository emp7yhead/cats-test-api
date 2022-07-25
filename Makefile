start:
	@poetry run uvicorn run:app --reload

lint:
	@poetry run flake8 app