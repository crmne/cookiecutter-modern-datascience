# Cookiecutter Modern Data Science
[Cookiecutter] template for starting a Data Science project with modern tools.

* GitHub repo: https://github.com/crmne/cookiecutter-modern-datascience
* Free software: BSD license

## Features

* [Pipenv] for managing packages and virtualenvs in a modern way.
* Batteries included: [Pandas], [numpy], [scipy], and [seaborn] already installed.
* Consistent code quality: [yapf], [isort], [autoflake], and [pylint] already installed and set up as a git hook.
* [Makefile] for local data pipelines.
* [Pytest] for testing.
* [Sphinx] docs: Documentation ready for generation with, for example, [Read the Docs].
* Command line interface using [Click].

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter gh:crmne/cookiecutter-modern-datascience

## Directory structure

This is our your new project will look like:

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── 0_raw          <- The original, immutable data dump.
    │   ├── 0_external     <- Data from third party sources.
    │   ├── 1_interim      <- Intermediate data that has been transformed.
    │   └── 2_final        <- The final, canonical data sets for modeling.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── features           <- Fitted and serialized features, model predictions, or model summaries
    |
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `_` delimited description, e.g.
    │                         `1_jqp_initial_data_exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── Pipfile            <- The Pipfile for reproducing the analysis environment
    │
    ├── src                <- Source code for use in this project.
    │   ├── app.py         <- Flask API that makes predictions using the trained model.
    │   ├── cli.py         <- Entry point for all the scripts described below.
    │   └── test_app.py    <- Flask API intergration tests.
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── make_dataset.py
    │   │   └── split_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Pipenv]: https://pipenv.pypa.io/en/latest/
[Click]: https://click.palletsprojects.com/
[Sphinx]: https://www.sphinx-doc.org/en/master/
[Read the Docs]: https://readthedocs.org/