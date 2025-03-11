SHELL := /bin/bash

.PHONY: banner
banner:
	@echo "make setup"
	@echo "make test build"
	@echo "make clean"


.PHONY: setup
setup:
	python3 -m venv venv
	. venv/bin/activate && pip install hatchling twine build pytest
	. venv/bin/activate && pip install -e .


.PHONY: test
test:
	. venv/bin/activate && . ./.env && pytest

.PHONY: build
build: test
	rm -f dist/*
	. venv/bin/activate && python3 -m build

.PHONY: release-test
release-test: build
	python -m twine upload --repository testpypi dist/*

.PHONY: release
release: build
	python -m twine upload dist/*


.PHONY: clean
clean:
	rm -rf venv/
	rm -rf dist/

