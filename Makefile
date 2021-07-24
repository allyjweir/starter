.PHONY: build console format run test

build: 
	docker build -t starter:local_dev .

console:
	docker run \
		--rm \
		--interactive \
		--tty \
		--volume $${PWD}:/starter \
		--publish 8080:8080 \
		starter:local_dev \
		/bin/bash

run:
	docker run \
		--rm \
		--interactive \
		--tty \
		--volume $${PWD}:/starter \
		--publish 8080:8080 \
		starter:local_dev \
		poetry run uvicorn app:starter --host 0.0.0.0 --port 8080 --app-dir starter/ --reload

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
		poetry run pytest

publish_image:
	/bin/bash scripts/publish_to_dockerhub.sh

deploy_to_minikube:
	/bin/bash scripts/deploy_to_minikube.sh