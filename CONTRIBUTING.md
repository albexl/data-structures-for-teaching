# Contribution guidelines

Thank you for contributing to this project! We expect all contributors to have read this file before submitting Pull Requests.

## Environment Setup

## Dependency management

Considering the current development of multiple Dependency Management Tools for Python (Poetry, Pipenv, pyenv, ...), and the benefits of its use, a [Poetry](https://python-poetry.org/docs/basic-usage/) environment was created. For installing Poetry, please visit the [documentation](https://python-poetry.org/docs/#installation) related to this topic, and confirm that it's added to your PATH.

When using Poetry, a virtual environment will be created for this project, isolating all its dependencies.

### About the `pyproject.toml` file

Everything related to the environment configuration could be found on the [pyproject.toml](./pyproject.toml) file. For more detailed information about it, please refer to the Poetry doc. Also, if the `TOML` language is new to you, you can refer to the [spec definition](https://toml.io/en/).

The file is grouped in tables (defined by TOML as `[<table_name>]`). At the moment we have:

1. **tool.poetry**: Basic metadata about the project. It will be used when generating and publishing a package to **PyPi**
2. **tool.poetry.dependencies**: Common dependencies for all environments
3. **tool.poetry.group.test.dependencies**: Test dependencies
4. **tool.poetry.group.dev.dependencies**: Development dependencies
5. **build-system**: Poetry internal configuration

Any table which name follows the format `tool.poetry[.group.{group_name}].dependencies`, defines a [dependency group](https://python-poetry.org/docs/managing-dependencies/#dependency-groups) for Poetry, and it allows the user to install those dependencies under specific groups. For example, those in _test_ and _dev_ groups are not needed for a PyPi deployment. Please, notice than _test_ and _dev_ are just selected names, and not required groups by Poetry.

### Some useful commands

For running any of the following commands, position your shell in the project root, where `pyproject.toml` is located.

```bash
poetry install  # Install all dependencies, including test and dev
poetry install --without test,dev  # Install all dependencies, except those in groups test and dev
poetry shell  # Enters the environment shell
poetry run <command>  # Runs a command in the environment without having to open the shell. For example `poetry run pytest`
poetry update [package_1] [package_2]  # Update all the dependencies, or those specified to the latest compatible version
poetry remove <package> [--group G]  # Remove the listed package, optionally from a specific group
poetry show  # List all dependencies
poetry config --list  # Shows the current Pyproject configuration
poetry export -f requirements.txt --output requirements.txt  # Export all dependencies to requirements.txt file
```

For more detailed use cases, and other commands, please visit the [cli documentation](https://python-poetry.org/docs/cli/).

## Organization

Here is a brief description of the repo's structure, just to get you familiar with it before you can start contributing.

### Data Structures

Each data structure is in the `data_structures` directory. Every subdirectory in it should contain the implementation, client code, and application examples of the specific data structure we want to have.

### Algorithms

Each algorithm is in the `algorithms` directory. Here we are trying to create subdirectories to separate the type of algorithms we are going to have in the repo. Examples of different types could be `sorting` and `searching`.

### Tests

We have a `tests` directory to hold unit tests for every algorithm and data structure implemented. We should try to carefully test all our implementations before we submit them for review.

## Contribution Workflow

These are guidelines for the steps to take to contribute to our project. We recommend following these steps if you want to have the most enjoyable experience while trying to add something new to this repo.

### Read Issues and Pull Requests

We strongly recommend you read the Issues in the repo as well as the pending Pull Requests so you can focus your energies on something new and don't waste your time. You can also try to reach out to someone who is already working on some task and try to collaborate.

### Create a new Issue

If nobody is working on the task you want to work on, then create a new issue explaining the changes you want to make and the reason why you would like to make these changes. We even have some templates you can use to help you write your issues more easily.

### Fork this repo

Fork the repo, because you are going to make your changes on your forked version.

### Submit a Pull Request

To make changes to this repo, submit a Pull Request to the `dev` branch. Once it is reviewed, it will either be merged or some changes will be requested.

As of now, we have a basic CI setup that can be checked here: [check.yaml](./.github/workflows/check.yaml). This setup can help you know if some tests are failing for your changes and that you need to make some changes before submitting the Pull Request.

#### Notes on commits

We would like to have some naming standards on commits. We are going to try as much as we can to use the following format when naming our commits:

```plain
<label>: <brief explanation>

<Optional body to explain your changes in more detail>
```

As of now, the valid labels are:

- `doc` for documentation-related contributions.
- `fix` if you want to fix a bug.
- `feat` if you want to add any new feature. E.g. adding a new algorithm or use case.
- `ref` if you want to refactor some parts of the existing codebase.
- `test` if the change is related to adding tests to our project.

A few good examples are:

```plain
feat: Add implementation of heap data structure
test: Add tests for heap implementation
```

Try to name the Pull Requests you create using the same labels as in the commits.

## Issues

For every bug found, typo or just to suggest some improvement of any kind, create a new issue. You can even solve it yourself.

## Testing

We are trying hard to test every implementation we make. So, add unit tests in the `tests` directory to check the correctness of your changes.

To run the tests, run the following command in the root directory:

```bash
pytest
```

## Formatting

We are trying to make the code as standardized as possible. One way to achieve this is by formatting your code properly. It is recommended to use the `black` formatter after you have made all your changes.

You can format the entire project by running this command on the root directory:

```bash
black .
```

## Imports

The order of the imported libraries is important in Python. Among other things, it makes it easy to identify third-party libraries to include in our `requirements` files. It is recommended to use `isort` to sort libraries properly. It can be done by running this command in the root directory:

```bash
isort .
```

## Linting

Since we are trying to make the codebase as standard as possible, it is a good idea to run the `pylint` linter on the directory of your changes and try to comply with all the suggestions it shows. We can ignore some of them, but trying to fix as many as possible will end up in a codebase that looks like the code of a team, instead of the code of individuals scattered across the repo. To use `pylint` just execute the following command on your terminal:

```shell
pylint {working_directory}
```

Replace `{working_directory}` with the directory that you want to run `pylint` on.

## Code of Conduct

We are trying to create a healthy community that thrives on the desire to learn and share knowledge. See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) to check our behavioral rules on this project.
