VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
FLAKE8 = $(VENV)/bin/flake8
COVERAGE = $(VENV)/bin/coverage

.PHONY: help build migrate superuser run test lint coverage clean

help:
	@echo "Available commands:"
	@echo "  make build      - Setup virtual environment and install dependencies"
	@echo "  make migrate    - Apply database migrations"
	@echo "  make superuser  - Create Django superuser"
	@echo "  make run        - Run Django development server"
	@echo "  make test       - Run Django tests"
	@echo "  make lint       - Run code linting with flake8"
	@echo "  make coverage   - Run tests with coverage reporting"
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

lint:
	$(FLAKE8) app

coverage:
	$(COVERAGE) run --source=app manage.py test
	$(COVERAGE) report -m
	$(COVERAGE) html

fix:
	@echo "Running black..."
	venv/bin/black app/
	@echo "Running autoflake..."
	venv/bin/autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r app/
	@echo "Running isort..."
	venv/bin/isort app/
	@echo "Done fixing lint issues!"

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
