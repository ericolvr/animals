SHELL:=/bin/bash
ENV_NAME ?= dev


upgrade-pip:
	pip install --upgrade pip

dependencies:
	pip install -r requirements.txt

docker-dev:
	docker compose up -d

docker-tests:
	docker build -t tests ./docker/tests && docker run -d -p 3307:3306 --name tests -e MYSQL_ROOT_PASSWORD=secret tests

unit:
	python -m pytest -s -v

run:
	uvicorn src.run:app --reload 

.PHONY: upgrade-pip, dependencies, docker-dev, docker-tests, unit, run