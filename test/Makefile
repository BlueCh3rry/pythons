NAME=a_maze_ing.py
CONFIG=config.txt

all: ${NAME}

install-poetry:
	@command -v poetry >/dev/null 2>&1 || { \
		curl -sSL https://install.python-poetry.org | python3 -; \
	}

install: install-poetry
	poetry install

run: ${NAME} ${CONFIG}
	poetry run python ${NAME} ${CONFIG}

debug: ${NAME}
	python3 -m pdb ${NAME} ${CONFIG}

clean:
	find . -iname "__pycache__" -type d -exec rm -rf "{}" +
	find . -iname ".mypy_cache" -type d -exec rm -rf "{}" +

lint:
	poetry run flake8
	poetry run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	poetry run flake8 .
	poetry run mypy . --strict

.PHONY: install run debug clean lint lint-strict
