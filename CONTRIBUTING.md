# Contribution guidelines

Thank you for contributing to this project! We expect all contributors to have read this file before submitting Pull Requests.

Each data structure is on the `data_structures` directory. Every subdirectory in it should contain the implementation, client code, application examples, etc...

## Pull Requests

To make changes to `data-structures-for-teaching`, submit a Pull Request to the `dev` branch. Once it is reviewed, it will either be merged or some changes will be requested. As of now, we have a basic CI setup that can be checked here: [workflow](https://github.com/albexl/data-structures-for-teaching/blob/dev/.github/workflows/check.yaml).

## Issues

For every bug found, typo or just to suggest some improvement of any kind, create a new issue. You can even solve it your yourself.

## Testing

We are trying hard to test every implementation we make. So, add a unit tests in the `tests` directory checking the correctness of your changes.

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
