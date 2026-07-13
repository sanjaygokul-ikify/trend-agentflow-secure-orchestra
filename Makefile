dev-env:
	docker-compose up -d --build

build:
	poetry build

test:
	poetry pytest tests/

clean:
	rm -rf dist/
	rm -rf *.egg-info

format:
	poetry run isort .
	poetry run black .