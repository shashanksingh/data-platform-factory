.DEFAULT_GOAL := all

setup:
	python3 -m pip install --upgrade pip
	brew install astro



install:
	python3 -m pip install -r src/requirements.txt

test-install:
	python3 -m pip install -r tests/requirements.test.txt

dev-install:
	python3 -m pip install -r src/requirements.dev.txt

unittest:
	python3 -m pytest tests

unittest-coverge:
	python3 -m pytest  tests/ -p no:sugar

unittest-verbose:
	python3 -m pytest tests -p no:sugar -s -vv

generate-dags:
	 python3 -m src.generate_dags --directory definitions

test-dags:
	astro dev parse

toml_sort:
	toml-sort  definitions/**/*.toml  --all --in-place

isort:
	python3 -m  isort .

ruff:
	python3 -m ruff format src/ tests/

flake8:
	python3 -m flake8 src/ tests/

pylint:
	python3 -m pylint src/

mypy:
	python3 -m mypy --install-types --non-interactive src/


generate-package-from-cli:
	cd src && python3 setup.py sdist && python3 -m pip install dist/generate_dags-0.1.tar.gz



lint: ruff  mypy flake8
tests: unittest
all: setup install lint tests generate-dags test-dags