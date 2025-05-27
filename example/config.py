"""Example use of a Configaroo configuration.

The example requires the environment variable EXAMPLE_SECRET to be set. If it's
not set, you'll see a validation error. You can also override the board size
setting by setting the BOARD_SIZE environment variable.
"""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, HttpUrl

from configaroo import Configuration


class PlayerConfig(BaseModel):
    color: str


class UserConfig(BaseModel):
    player_x: PlayerConfig
    player_o: PlayerConfig


class ConstantConfig(BaseModel):
    board_size: int


class ServerConfig(BaseModel):
    url: HttpUrl
    secret: str


class ConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    user: UserConfig
    constant: ConstantConfig
    server: ServerConfig


config = Configuration.from_file(
    Path(__file__).parent / "settings.toml",
    envs={"EXAMPLE_SECRET": "server.secret", "BOARD_SIZE": "constant.board_size"},
).with_model(model=ConfigModel)


if __name__ == "__main__":
    print(config)
