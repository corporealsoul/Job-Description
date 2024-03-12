install:
	# Install Commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	# Format Code
	black *.py lib/*.py

lint:
	# Flake8 or Pylint
	pylint --disable=R,C *.py lib/*.py

test:
	# Test
	# python -m pytest -vv --cov=lib ./lib/test_logic.py
	# python -m pytest -vv --cov=lib --cov=main test_*.py
	# python -m pytest -vv --cov=lib --cov=main test_*.py
	python -m pytest -vv --cov=lib --cov=main test_*.py

build:
	# Build Container
	# docker build -t deploy-fastapi .

run:
	# Run
	# docker run -p 127.0.0.1:8080:8080 "container id"

deploy:
	# Deploy

all: install format lint test deploy