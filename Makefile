.PHONY: build console format run test

build: 
	docker build -t starter:local_dev .

console:
	docker run \
		--rm \
		--interactive \
		--tty \
		--volume $${PWD}:/starter \
		--publish 8000:8000 \
		starter:local_dev \
		/bin/bash

run:
	docker run \
		--rm \
		--interactive \
		--tty \
		--volume $${PWD}:/starter \
		--publish 8000:8000 \
		starter:local_dev \
		poetry run uvicorn app:starter --host 0.0.0.0  --reload

format:
	docker run \
		--rm \
		--interactive \
		--tty \
		--volume $${PWD}:/starter \
		starter:local_dev \
		poetry run black .

test:
	docker run \
		--rm \
		--interactive \
		--tty \
		--volume $${PWD}:/starter \
		starter:local_dev \
		poetry run python -m unittest -v