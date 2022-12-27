# Contribution guidelines

Thank you for contributing to this project! We expect all contributors to have read this file before submitting Pull Requests.

Each data structure is in the `data_structures` directory. Every subdirectory in it should contain the implementation, client code, application examples, etc...

## Pull Requests

To make changes to `data-structures-for-teaching`, submit a Pull Request to the `dev` branch. Once it is reviewed, it will either be merged or some changes will be requested. As of now, we have a basic CI setup that can be checked here: [workflow](https://github.com/albexl/data-structures-for-teaching/blob/dev/.github/workflows/check.yaml).

#### Notes on commits:

We would like to have some naming standards on commits. We are going to try as much as we can to use the following format when naming our commits:
```plain
<label>: <brief explanation>

<Optional body to explain your changes in more detail>
```

As of now, the valid labels are:
* ```doc``` for documentation-related contributions.
* ```fix``` if you want to fix a bug.
* ```feat``` if you want to add any new feature. E.g. adding a new algorithm or use case.
* ```ref``` if you want to refactor some parts of the existing codebase.
* ```test``` if the change is related to adding tests to our project.

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

We are to make the code as standardized as possible. One way to achieve this is by formatting your code properly. It is recommended to use the `black` formatter after you have made all your changes.

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

We are trying to create a healthy community that thrives on the desire to learn and share knowledge. See [CODE_OF_CONDUCT.md](https://github.com/albexl/data-structures-for-teaching/blob/dev/CODE_OF_CONDUCT.md) to check our behavioral rules on this project.
