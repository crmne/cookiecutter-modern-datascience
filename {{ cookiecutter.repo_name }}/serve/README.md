# {{ cookiecutter.project_name }} - HTTP API

HTTP API for serving predictions.

## Installation

    pip install pipenv  # if you haven't already
    pipenv install
    pipenv run python app.py

## Development

    pipenv install --dev
    pipenv shell

## Test

    pytest

## Directory structure

    ├── Dockerfile            <- Dockerfile for HTTP API
    ├── Pipfile               <- The Pipfile for reproducing the serving environment
    ├── app.py                <- The entry point of the HTTP API
    └── tests
        ├── fixtures          <- Where to put example inputs and outputs
        │   ├── input.json    <- Test input data
        │   └── output.json   <- Test output data
        └── test_app.py       <- Integration tests for the HTTP API
