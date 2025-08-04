"""Configuration schema used in tests."""

from pathlib import Path

import pydantic


# Configuration schema
class StrictSchema(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class DeeplyNestedSchema(StrictSchema):
    sea: str


class NestedSchema(StrictSchema):
    pie: float
    seven: int
    deep: DeeplyNestedSchema


class LogSchema(StrictSchema):
    level: str
    format: str


class WithDotSchema(StrictSchema):
    org_num: int = pydantic.Field(alias="org.num")


class PathsSchema(StrictSchema):
    relative: Path
    dynamic: Path
    absolute: Path
    directory: Path
    nested: Path


class ConfigSchema(StrictSchema):
    number: int
    word: str
    phrase: str
    things: list[str]
    nested: NestedSchema
    log: LogSchema
    with_dot: WithDotSchema
    paths: PathsSchema
