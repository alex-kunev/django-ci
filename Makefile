.PHONY: help install test coverage lint migrate shell clean

help:
	@echo "Django CI Project - Available Commands"
	@echo "======================================"
	@echo "  make install      - Install dependencies"
	@echo "  make migrate      - Run database migrations"
	@echo "  make test         - Run tests"
	@echo "  make coverage     - Run tests with coverage report"
	@echo "  make lint         - Run flake8 linting"
	@echo "  make shell        - Open Django shell"
	@echo "  make runserver    - Start development server"
	@echo "  make clean        - Clean up .pyc files and __pycache__"
	@echo "  make help         - Show this help message"

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage report
	coverage html

lint:
	flake8 . --exclude=migrations,venv,__pycache__ --max-line-length=100 --ignore=E501

shell:
	python manage.py shell

runserver:
	python manage.py runserver

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '.pytest_cache' -delete
	rm -rf htmlcov/
	rm -f .coverage

createsuperuser:
	python manage.py createsuperuser
