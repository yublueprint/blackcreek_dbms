VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: build run migrate superuser clean

build:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run: migrate
	$(PYTHON) manage.py runserver

clean:
	rm -rf $(VENV)
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
