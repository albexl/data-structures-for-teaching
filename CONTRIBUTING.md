# Contribution guidelines

Thank you for contributing to this project! We expect all contributors to have read this file before submitting Pull Requests.

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

We strongly recommend you to read the Issues in the repo as well as the pending Pull Requests so you can focus your energies on something new and don't waste your time. You can also try to reach out to someone who is already working on some task and try to collaborate.

### Create a new Issue

If nobody is working on the task you want to work, then create a new issue explaining the changes you want to make and the reason why you would like to make these changes. We even have some templates you can use to help you write your issues more easily.

### Fork this repo

Fork the repo, because you are going to make your changes on your forked version.

### Submit a Pull Request

To make changes to this repo, submit a Pull Request to the `dev` branch. Once it is reviewed, it will either be merged or some changes will be requested.

As of now, we have a basic CI setup that can be checked here: [check.yaml](./.github/workflows/check.yaml). This setup can help you know if there are some tests failing for your changes and that you need to make some changes before submitting the Pull Request.

#### Notes on commits:

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

## Code of Conduct

We are trying to create a healthy community that thrives on the desire to learn and share knowledge. See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) to check our behavioral rules on this project.
