# Makefile for Mnemos project

.PHONY: help backend frontend migrate createsuperuser runserver test

help:
	@echo ""
	@echo "Mnemos Project - Available commands:"
	@echo "-------------------------------------"
	@echo "make backend          Run Django backend server (localhost:8000)"
	@echo "make runserver        Run Django backend server (default 127.0.0.1:8000)"
	@echo "make frontend         Run React frontend dev server"
	@echo "make migrate          Apply Django migrations"
	@echo "make createsuperuser  Create Django superuser"
	@echo "make test             Run Django unit tests"
	@echo ""

backend:
	cd mnemos_project && source ../venv/bin/activate && python manage.py runserver localhost:8000

runserver:
	cd mnemos_project && source ../venv/bin/activate && python manage.py runserver

frontend:
	cd mnemos-frontend && npm start

migrate:
	cd mnemos_project && source ../venv/bin/activate && python manage.py migrate

createsuperuser:
	cd mnemos_project && source ../venv/bin/activate && python manage.py createsuperuser

test:
	cd mnemos_project && source ../venv/bin/activate && python manage.py test
