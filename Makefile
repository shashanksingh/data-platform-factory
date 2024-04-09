setup:
	python3 -m pip install --upgrade pip

install:
	python3 -m pip install -r src/requirements.txt

test-install:
	python3 -m pip install -r test/requirements.test.txt

dev-install:
	python3 -m pip install -r src/requirements.dev.txt

test:
	python3 -m pytest test



#toml_sort:
#	python3 -m toml-sort toml/*.toml --all --in-place

isort:
	python3 -m  isort .

ruff:
	python3 -m ruff format

flake8:
	python3 -m flake8 .

pylint:
	python3 -m pylint src