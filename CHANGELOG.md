# Changelog - Configaroo

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html).

The file uses standardized headers (Added, Changed, Fixed, and Removed) to
indicate changes.

## [Unreleased]

## [0.1.1] - 2025-05-26

### Added

- MIT License file
- Changelog file
- Github workflows to automatically lint and test code
- Github workflow to automate publishing of new releases
- `.__version__` attribute

### Fixed

- Dynamic `project_path` variable
- Placeholders `{field}` do not raise an error when parsing dynamic values


## [0.1.0] - 2025-05-26

### Added

- The first version of Configaroo including:
    - dotted access to configuration values
    - environment variable support
    - TOML-file support
    - JSON-file support
    - Configuration validation based on Pydantic
    - Type conversion of configuration values based on Pydantic

[unreleased]: https://github.com/gahjelle/configaroo/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/gahjelle/configaroo/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/gahjelle/configaroo/releases/tag/v0.1.0
