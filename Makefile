init:
	pip install pipenv
	pipenv install --dev

test:
	pytest

build:
	python3 setup.py sdist bdist_wheel

.PHONY: all build
