start_dev_container:
	@docker compose up -d --build app

enter_dev_container:
	@docker compose exec app /bin/bash

stop_dev_container:
	@docker compose rm -s app

compile_requirements:
	@docker build -t comp_req -f docker/compilereq.Dockerfile .
	@docker run --rm --mount source=${PWD}/requirements,target=/requirements,type=bind comp_req
