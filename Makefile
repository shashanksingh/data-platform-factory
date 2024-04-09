setup:
	python3 -m pip install --upgrade pip

install:
	python3 -m pip install -r src/requirements.txt

test-install:
	python3 -m pip install -r test/requirements.test.txt

test:
	python3 -m pytest test