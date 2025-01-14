APP_NAME = "wasabiair/ocr_v3"
VERSION = "0.1.0"

.PHONY: build lint update test install_autocompletes clean help docker_build docker_run

# Default target
all: help

build: lint test docker_build

lint:
	black -l 120 src

update: requirements.txt
	pip freeze > requirements.txt

test:
	python -m pytest

docker_build:
	docker build -t $(APP_NAME):latest -t $(APP_NAME):$(VERSION) .

docker_run:
	docker run --rm -it $(APP_NAME):latest

install_autocompletes:
	# Install autocompletes for bash and zsh
	# bash & zsh
	eval "$(python src/main.py -sc install=bash)"

clean:
	rm -rf ./output_folder

help:
	@echo "Available commands:"
	@echo "  build                Run lint, test, and update"
	@echo "  lint                 Run black linter"
	@echo "  update               Update requirements.txt"
	@echo "  test                 Run tests with tox"
	@echo "  install_autocompletes Install autocompletes for bash and zsh"
	@echo "  clean                Clean the output folder"
