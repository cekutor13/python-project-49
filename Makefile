install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv venv
	uv pip install dist/*.whl
lint:
	uv run ruff check brain_games

build:
	uv build

package-install:
	uv pip install dist/*.whl
