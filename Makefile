install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv venv
	uv tool install dist/*.whl
