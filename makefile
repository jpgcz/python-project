start_dev_container:
	@docker compose up -d app

enter_dev_container:
	@docker compose exec app /bin/bash

stop_dev_container:
	@docker compose rm -s app

compile_requirements:
	@pip-compile requirements/dev.in -o requirements/dev.txt
