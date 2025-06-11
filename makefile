UNAME_S := $(shell uname -s)
ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
    VENV = venv
    PYTHON = $(VENV)/Scripts/python.exe
    PIP = $(VENV)/Scripts/pip.exe
    FLAKE8 = $(VENV)/Scripts/flake8.exe
    COVERAGE = $(VENV)/Scripts/coverage.exe
    BLACK = $(VENV)/Scripts/black.exe
    AUTOFLAKE = $(VENV)/Scripts/autoflake.exe
    ISORT = $(VENV)/Scripts/isort.exe
else
    DETECTED_OS := $(UNAME_S)
    VENV = venv
    PYTHON = $(VENV)/bin/python
    PIP = $(VENV)/bin/pip
    FLAKE8 = $(VENV)/bin/flake8
    COVERAGE = $(VENV)/bin/coverage
    BLACK = $(VENV)/bin/black
    AUTOFLAKE = $(VENV)/bin/autoflake
    ISORT = $(VENV)/bin/isort
endif

.PHONY: help build migrate signup run test lint coverage fix clean

info:
	@echo "Detected OS: $(DETECTED_OS)"

help: info
	@echo "Available commands:"
	@echo "  make build      - Setup virtual environment and install dependencies"
	@echo "  make migrate    - Apply database migrations"
	@echo "  make signup     - Create Django superuser"
	@echo "  make run        - Run Django development server"
	@echo "  make test       - Run Django tests"
	@echo "  make lint       - Run code linting with flake8"
	@echo "  make coverage   - Run tests with coverage reporting"
	@echo "  make lint-fix        - Auto-format and fix lint issues (black, autoflake, isort)"
	@echo "  make clean      - Remove virtual environment and temporary files"

build: info
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

migrate:
	$(PYTHON) manage.py migrate

signup:
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

lint-fix:
	@echo "Running black..."
	$(BLACK) app/
	@echo "Running autoflake..."
	$(AUTOFLAKE) --in-place --remove-unused-variables --remove-all-unused-imports -r app/
	@echo "Running isort..."
	$(ISORT) app/
	@echo "Done fixing lint issues!"

clean: info
	@echo "Removing virtual environment and cache files..."
	rm -rf $(VENV)
	@find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
	@find . -type f -name "*.pyc" -delete 2>/dev/null || powershell -Command "Get-ChildItem -Recurse -Filter '*.pyc' | Remove-Item -Force"
