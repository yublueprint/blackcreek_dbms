# Makefile for Django Project

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: help build run migrate superuser test clean
help:
	@echo "Available commands:"
	@echo "  make build      - Setup virtual environment and install dependencies"
	@echo "  make migrate    - Apply database migrations"
	@echo "  make superuser  - Create Django superuser"
	@echo "  make run        - Run Django development server"
	@echo "  make test       - Run Django tests"
	@echo "  make clean      - Remove virtual environment and temporary files"

build:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

migrate:
	$(PYTHON) manage.py migrate

superuser:
	$(PYTHON) manage.py createsuperuser

run:
	$(PYTHON) manage.py runserver

test:
	$(PYTHON) manage.py test

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
