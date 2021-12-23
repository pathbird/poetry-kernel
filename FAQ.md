# Frequently asked questions

## Why do I have to install `ipykernel` manually?

The IPython kernel runs as part of the same process as all your other Python
code. This means we can't install our own version of it outside of your Poetry
project.

Trying to install it automatically runs the risk of accidentally breaking
something in your project by accidentally upgrading a dependency (or transitive
dependency). That would go against the whole point of trying to recreate the
exact set of packages that were being used to create the notebook!

## Why won't Poetry Kernel automatically run `poetry install`?

Doing so has the possibility to run arbitrary Python code on your computer
(since most packages are allowed to run arbitrary Python code during their
install). It should generally be safe to open a notebook file even if it's
untrusted, so we don't take the risk.

## Why does my dependency (e.g., numpy) fail to install?

Usually, the output from `poetry add` is pretty informative and will tell you
how to resolve the issue.

Oftentimes (especially with `numpy`), Poetry fails to install a package because
of conflicts in the supported Python versions. When initializing a project,
Poetry sets the supported Python range to `^3.9` (if you're using Python 3.9)
which means any Python version in the range `[3.9, 4)`. Some packages, including
numpy, restrict the maximum Python range that they'll support (e.g., numpy
1.21.5 requires Python `>=3.7,<3.11`). Poetry doesn't allow this since
hypothetically the environment could be recreated with Python 3.11 which is not
allowed by the numpy dependency.

The solution in this case is usually to simply set the Python version in the
`pyproject.toml` file to the version of Python that you're using (e.g. just
`3.9` if using Python 3.9):

```
# pyproject.toml
# ...
[tool.poetry.dependencies]
python = "3.9"
# ...
```

## Some other question!

Feel free to open an issue to discuss.
