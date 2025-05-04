.PHONY: build up down clean

build:
	@docker compose build

up:
	@docker compose up -d

down:
	@docker compose down --volumes --remove-orphans

clean:
	@docker system prune -a -f --volumes
