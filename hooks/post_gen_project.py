#!/usr/bin/env python
"""Script that runs after the project generation phase."""
import os
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{ cookiecutter.license }}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()

if "{{ cookiecutter.setup_project }}" == "Yes":
    os.system("git init")
    os.system("pipenv install --dev")
    os.system(
        "pipenv run ipython kernel install --name "
        '"py3_{{ cookiecutter.repo_name }}" --user'
    )
