.PHONY: setup-env
setup-env:
	cp .env.example .env

.PHONY: project
project: build up

.PHONY: build
build:
	docker compose build

.PHONY: up
up:
	docker compose up -d 

.PHONY: run-server
run-server:
	docker compose up -d

.PHONY: stop-server
stop-server:
	docker compose down

.PHONY: migrate
migrate:
	docker compose exec app python manage.py migrate

.PHONY: migrations
migrations:
	docker compose exec app python manage.py makemigrations

.PHONY: superuser
superuser:
	docker compose exec app python manage.py createsuperuser

.PHONY: logs
logs:
	docker compose logs -f

.PHONY: rebuild
rebuild:
	docker compose down && docker compose up --build -d

.PHONY: app
app:
	@if [ -z "$(app)" ]; then \
		echo "provide an app name e.g., make app app=api"; \
	else \
		docker-compose exec app python manage.py startapp $(app); \
	fi