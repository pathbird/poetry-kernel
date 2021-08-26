# Poetry Kernel

Use per-directory Poetry environments to run Jupyter kernels. No need to install
a Jupyter kernel per Python virtual environment!

The idea behind this project is to allow you to capture the exact state of your
environment. This means you can email your work to your peers and they'll have
_exactly_ the same set of packages that you do! Reproducibility!

## Shameless plug

The reason we created this package was to make sure that the code environments
created for running student code on Pathbird exactly match your development
environment. Interested in developing interactive, engaging, inquiry-based
lessons for your students?
[Check out Pathbird for more information!](https://pathbird.com/)

# Usage

1. [Install Poetry](https://python-poetry.org/docs/#installation) if not yet
   installed.
1. Install this package:
   ```sh
   # NOTE: Do **NOT** install this package in your Poetry project, it should be
   # installed at the system or user level.
   pip3 install poetry-kernel
   ```
1. Initialize a Poetry project (only required if you do not have an existing
   Poetry project ready to use):
   ```sh
   poetry init -n
   ```
1. **IMPORTANT:** Add `ipykernel` to your project's dependencies:
   ```sh
   # In the directory of your Poetry project
   poetry add ipykernel
   ```
1. Start a "Poetry" Jupyter kernel and see it in action!
   ![Jupyter launcher screenshot](.static/jupyter-screenshot.png)

# Troubleshooting

## Kernel isn't starting ("No Kernel" message)

**Pro-tip:** Check the output of the terminal window where you launched Jupyter.
It will usually explain why the kernel is failing to start.

1. Make sure that you are launching a notebook in a directory/folder that
   contains a Poetry project (`pyproject.toml` and `poetry.lock` files). You can
   turn a directory into a Poetry project by running:

```sh
poetry init -n
```

2. Make sure that you've installed `ipykernel` into your project:

```sh
poetry add ipykernel
```

3. Make sure the Poetry project is installed! This is especially important for
   projects that you have downloaded from others (**warning:** installing a
   Poetry project could run arbitrary code on your computer, make sure you trust
   your download first!):

   ```sh
   poetry install
   ```

4. Still can't figure it out? Open an issue!

## A package I added won't import properly

If you added the package **after** starting the kernel, you might need to
restart the kernel for it to see the new package.

# FAQ

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

## Some other question!

Feel free to open an issue to discuss.
