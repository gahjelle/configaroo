import os

import pytest
from pydantic import BaseModel, SecretStr

from examples.validate import config


@pytest.fixture
def example_secret() -> str:
    """Ensure EXAMPLE_SECRET is set as an environment variable."""
    example_secret = "hush-hush"
    os.environ["EXAMPLE_SECRET"] = example_secret
    return example_secret


def test_config_is_basemodel(example_secret: str) -> None:
    """Test that the configuration has been converted into a proper BaseModel."""
    cfg = config.get_configuration()
    assert isinstance(cfg, BaseModel)
    assert isinstance(cfg, config.ConfigModel)


def test_secret_value(example_secret: str) -> None:
    """Test that the secret value is hidden but recoverable."""
    cfg = config.get_configuration()
    assert isinstance(cfg.server.secret, SecretStr)
    assert cfg.server.secret.get_secret_value() == example_secret
