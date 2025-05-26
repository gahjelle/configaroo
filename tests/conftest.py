"""Common fixtures and conveniences"""

import json
from pathlib import Path
from types import ModuleType
from typing import Any

import pydantic
import pytest
import tomli_w

from configaroo import Configuration


@pytest.fixture
def config():
    """A test configuration"""
    return Configuration(
        number=42,
        word="platypus",
        phrase="The meaning of life is {number}",
        things=["house", "car", "kayak"],
        nested={"pie": 3.14, "seven": 7, "deep": {"sea": "Marianer"}},
        with_dot={"org.num": 1234},
        paths=Configuration(
            relative="src/configaroo/configuration.py",
            dynamic="{project_path}/tests/test_configuration.py",
            absolute="/home/configaroo",
        ),
    )


@pytest.fixture
def model():
    """A test model"""

    class NestedModel(pydantic.BaseModel):
        pie: float
        seven: int

    # Use create_model() to include a field with a dot in the name
    WithDotModel = pydantic.create_model("WithDotModel", **{"org.num": int})

    class PathsModel(pydantic.BaseModel):
        relative: Path
        dynamic: Path
        absolute: Path

    class ConfigModel(pydantic.BaseModel):
        model_config = pydantic.ConfigDict(extra="forbid")

        number: int
        word: str
        phrase: str
        things: list[str]
        nested: NestedModel
        with_dot: WithDotModel
        paths: PathsModel

    return ConfigModel


@pytest.fixture
def base_path() -> Path:
    """The path to the testing directory"""
    return Path(__file__).parent


@pytest.fixture
def toml_path(base_path, config) -> Path:
    """A path to a TOML file representing the configuration"""
    return write_file(base_path / "files" / "config.toml", tomli_w, config)


@pytest.fixture
def other_toml_path(base_path, config) -> Path:
    """An alternative path to a TOML file representing the configuration"""
    return write_file(base_path / "files" / "tomlfile", tomli_w, config)


@pytest.fixture
def json_path(base_path, config) -> Path:
    """A path to a JSON file representing the configuration"""
    return write_file(base_path / "files" / "config.json", json, config)


@pytest.fixture
def other_json_path(base_path, config) -> Path:
    """A path to a JSON file representing the configuration"""
    return write_file(base_path / "files" / "jsonfile", json, config)


def write_file(path: Path, lib: ModuleType, config: Configuration):
    """Write a configuration to file. Return path for convenience"""
    path.write_text(lib.dumps(config.to_dict()), encoding="utf-8")
    return path
