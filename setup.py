import os
import shutil
import sys
from glob import glob

from setuptools import setup

setup_args = dict(
    name="poetry-kernel",
    packages=["poetry_kernel"],
)

# Note: this was adapted from the ipython/ipykernel setup.py script
# https://github.com/ipython/ipykernel/blob/abefee4c935ee79d3821dfda02f1511f55d4c996/setup.py#L95
# (Modified BSD License)
if any(a.startswith(('bdist', 'install')) for a in sys.argv):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, current_dir)

    spec_dir = os.path.join(current_dir, "data_kernelspec")
    if os.path.exists(spec_dir):
        shutil.rmtree(spec_dir)
    os.mkdir(spec_dir)
    from poetry_kernel.kernelspec import _write_kernelspec
    _write_kernelspec(spec_dir)

    setup_args["data_files"] = [
        # Extract the kernel.json file relative to the installation root
        # (i.e., the virtual environment or system Python installation).
        (
            os.path.join("share", "jupyter", "kernels", "poetry-kernel"),
            glob(os.path.join(spec_dir, "*")),
        ),
    ]

setup(**setup_args)
