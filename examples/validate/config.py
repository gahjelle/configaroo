"""Example use of a Configaroo configuration.

The example requires the environment variable EXAMPLE_SECRET to be set. If it's
not set, you'll see a validation error. You can also override the board size
setting by setting the BOARD_SIZE environment variable.
"""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, HttpUrl, SecretStr

from configaroo import Configuration, print_configuration


class ExactBaseModel(BaseModel):
    """Enforce that models contain the exact fields listed."""

    model_config = ConfigDict(extra="forbid")


class PlayerConfig(ExactBaseModel):
    color: str


class UserConfig(ExactBaseModel):
    player_x: PlayerConfig
    player_o: PlayerConfig


class ConstantConfig(ExactBaseModel):
    board_size: int


class ServerConfig(ExactBaseModel):
    url: HttpUrl
    secret: SecretStr


class ConfigModel(ExactBaseModel):
    user: UserConfig
    constant: ConstantConfig
    server: ServerConfig


def get_configuration() -> ConfigModel:
    """Read and validate the configuration."""
    return (
        Configuration.from_file(Path(__file__).parent / "settings.toml")
        .add_envs(
            {"EXAMPLE_SECRET": "server.secret", "BOARD_SIZE": "constant.board_size"}
        )
        .with_model(model=ConfigModel)
    )


if __name__ == "__main__":
    print_configuration(get_configuration())
