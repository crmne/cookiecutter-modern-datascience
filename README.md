# Cookiecutter Modern Data Science
[Cookiecutter] template for starting a Data Science project with modern, fast Python tools.

## Features

* [Pipenv] for managing packages and virtualenvs in a modern way.
* [Prefect] for modern pipelines and data workflow.
* [Weights and Biases] for experiment tracking.
* [FastAPI] for self-documenting fast HTTP APIs - on par with NodeJS and Go - based on [asyncio], [ASGI], and [uvicorn].
* Modern CLI with [Typer].
* Batteries included: [Pandas], [numpy], [scipy], and [jupyter] already installed.
* Consistent code quality: [black], [isort], [autoflake], and [pylint] already installed and set up as a git hook.
* [Pytest] for testing.
* [GitHub Pages] for documentation.
* [Git LFS] for large files.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter gh:crmne/cookiecutter-modern-datascience

## Directory structure

This is our your new project will look like:

    ├── LICENSE                 <- Your project's license.
    ├── README.md               <- The top-level README for developers using this project.
    ├── data
    │   ├── 0_raw               <- The original, immutable data dump.
    │   ├── 0_external          <- Data from third party sources.
    │   ├── 1_interim           <- Intermediate data that has been transformed.
    │   └── 2_final             <- The final, canonical data sets for modeling.
    │
    ├── output
    │   ├── features            <- Fitted and serialized features, model predictions, or model summaries
    │   ├── models              <- Trained and serialized models, model predictions, or model summaries
    │   └── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │       └── figures         <- Generated graphics and figures to be used in reporting
    │
    ├── docs                    <- GitHub pages website
    │   ├── data_dicts          <- Data dictionaries
    │   └── references          <- Papers, manuals, and all other explanatory materials.
    │
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                              the creator's initials, and a short `_` delimited description, e.g.
    │                              `01_cp_exploratory_data_analysis`.
    │
    ├── Pipfile                 <- The Pipfile for reproducing the analysis environment
    │
    ├── pipelines               <- Pipelines and data workflows.
    │   ├── Pipfile             <- The Pipfile for reproducing the pipelines environment
    │   ├── pipelines.py        <- The CLI entry point for all the pipelines
    │   ├── test_pipelines.py   <- pytest script for testing pipelines
    │   ├── lib                 <- Code for the various steps of the pipelines
    │   │   ├──  __init__.py
    │   │   ├── etl.py          <- Download, generate, and process data
    │   │   ├── visualize.py    <- Create exploratory and results oriented visualizations
    │   │   ├── features.py     <- Turn raw data into features for modeling
    │   │   └── train.py        <- Train and evaluate models
    │   └── test
    │       ├── fixtures        <- Where to put example inputs and outputs
    │       │   ├── input.json  <- Test input data
    │       │   └── output.json <- Test output data
    │       └── test_app.py     <- Integration tests for the HTTP API
    │
    ├── serve                   <- HTTP API for serving predictions
    │   ├── Dockerfile          <- Dockerfile for HTTP API
    │   ├── Pipfile             <- The Pipfile for reproducing the serving environment
    │   ├── app.py              <- The entry point of the HTTP API
    │   └── test
    │       ├── fixtures        <- Where to put example inputs and outputs
    │       │   ├── input.json  <- Test input data
    │       │   └── output.json <- Test output data
    │       └── test_app.py     <- Integration tests for the HTTP API
    │
    ├── .env                    <- Variables to be exported in the dev environment e.g. `PORT=8080`
    ├── .gitignore              <- GitHub's excellent Python .gitignore customized for this project
    └── .pylintrc               <- Configuration file for pylint


[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Pipenv]: https://pipenv.pypa.io/en/latest/
[Prefect]: https://docs.prefect.io/
[Weights and Biases]: https://www.wandb.com/
[FastAPI]: https://fastapi.tiangolo.com/
[asyncio]: https://docs.python.org/3/library/asyncio.html
[ASGI]: https://asgi.readthedocs.io/en/latest/
[uvicorn]: https://www.uvicorn.org/
[Typer]: https://typer.tiangolo.com/
[Pandas]: https://pandas.pydata.org/
[numpy]: https://numpy.org/
[scipy]: https://www.scipy.org/
[jupyter]: https://jupyter.org/
[black]: https://github.com/psf/black
[isort]: https://github.com/timothycrosley/isort
[autoflake]: https://github.com/myint/autoflake
[pylint]: https://www.pylint.org/
[Pytest]: https://docs.pytest.org/en/latest/
[GitHub Pages]: https://pages.github.com/
[Git LFS]: https://git-lfs.github.com/