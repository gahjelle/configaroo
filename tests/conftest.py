"""Common fixtures and conveniences."""

import json
from pathlib import Path

import pytest
import tomli_w

from configaroo import Configuration
from tests.schema import ConfigSchema


def toml_dumps(config: Configuration) -> str:
    """Dump a configuration to a TOML string."""
    return tomli_w.dumps(config.to_dict())


def json_dumps(config: Configuration) -> str:
    """Dump a configuration to a JSON string. Include a final newline."""
    return json.dumps(config.to_dict(), indent=4) + "\n"


@pytest.fixture
def model() -> type[ConfigSchema]:
    """Return a schema for the test configuration."""
    return ConfigSchema


@pytest.fixture
def config() -> Configuration:
    """Return a test configuration."""
    return Configuration(
        number=42,
        word="platypus",
        phrase="The meaning of life is {number}",
        things=["house", "car", "kayak"],
        nested={"pie": 3.14, "seven": 7, "deep": {"sea": "Marianer"}},
        log={"level": "info", "format": "<level>{level:<8} {message}</level>"},
        with_dot={"org.num": 1234},
        paths=Configuration(
            relative="src/configaroo/configuration.py",
            dynamic="{project_path}/tests/test_dynamic.py",
            absolute="/home/configaroo",
            directory="{project_path}/tests",
            nested="{paths.directory}/test_dynamic.py",
        ),
    )


@pytest.fixture
def base_path() -> Path:
    """Return the path to the testing directory."""
    return Path(__file__).parent


@pytest.fixture
def toml_path(base_path: Path, config: Configuration) -> Path:
    """Return a path to a TOML file representing the configuration."""
    return write_file(base_path / "files" / "config.toml", toml_dumps(config))


@pytest.fixture
def other_toml_path(base_path: Path, config: Configuration) -> Path:
    """Return an alternative path to a TOML file representing the configuration."""
    return write_file(base_path / "files" / "tomlfile", toml_dumps(config))


@pytest.fixture
def json_path(base_path: Path, config: Configuration) -> Path:
    """Return a path to a JSON file representing the configuration."""
    return write_file(base_path / "files" / "config.json", json_dumps(config))


@pytest.fixture
def other_json_path(base_path: Path, config: Configuration) -> Path:
    """Return a path to a JSON file representing the configuration."""
    return write_file(base_path / "files" / "jsonfile", json_dumps(config))


def write_file(path: Path, text: str) -> Path:
    """Write a configuration to file. Return path for convenience."""
    path.write_text(text, encoding="utf-8")
    return path
