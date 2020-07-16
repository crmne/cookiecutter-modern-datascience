#!/usr/bin/env python
"""Script that runs after the project generation phase."""
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{ cookiecutter.license }}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()
