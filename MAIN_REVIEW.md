# Formatting conventions

Please check the [PEP-8](https://peps.python.org/pep-0008/) Style Guide for more details
Using the IDE formatter is recommended, or even better, check out [Black](https://github.com/psf/black)

- Function/method names should use snake_case
- Single quotes are preferred over double quotes, besides for single characters
- Comments are defined by a single #
- Multiline comments should be defined by triple quotes
- We can define at the top of the file a docstring with a short description
- Prefer docstrings over comments on the file root level

# SQL Review

Everything seems good in this aspect.
Just one minor change:

- Avoid saving rounded values that will be used as sources
- Take a look at the other possible approach for window function usage in the "Share by Store" section