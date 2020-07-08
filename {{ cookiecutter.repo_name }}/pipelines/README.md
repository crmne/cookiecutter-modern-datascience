# {{ cookiecutter.project_name }} - Pipelines and Data Workflows

## Installation

    pip install pipenv  # if you haven't already
    pipenv install
    pipenv run python pipelines.py

## Development

    pipenv install --dev
    pipenv shell

## Test

    pytest

## Directory structure

    ├── Pipfile               <- The Pipfile for reproducing the pipelines environment
    ├── pipelines.py          <- The CLI entry point for all the pipelines
    ├── <repo_name>           <- Code for the various steps of the pipelines
    │   ├──  __init__.py
    │   ├── etl.py            <- Download, generate, and process data
    │   ├── visualize.py      <- Create exploratory and results oriented visualizations
    │   ├── features.py       <- Turn raw data into features for modeling
    │   └── train.py          <- Train and evaluate models
    └── tests
        ├── fixtures          <- Where to put example inputs and outputs
        │   ├── input.json    <- Test input data
        │   └── output.json   <- Test output data
        └── test_pipelines.py <- Integration tests for the HTTP API