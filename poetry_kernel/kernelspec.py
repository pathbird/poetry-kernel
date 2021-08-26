import json
import os.path
import tempfile

from jupyter_client.kernelspec import KernelSpecManager


def _write_kernelspec(dir):
    spec = {
        "argv": [
            "python", "-m", "poetry_kernel",
            "-f", "{connection_file}",
        ],
        "display_name": "Poetry",
        "language": "python",
    }
    with open(os.path.join(dir, "kernel.json"), "w") as fp:
        json.dump(spec, fp)


def install():
    manager = KernelSpecManager()
    with tempfile.TemporaryDirectory() as tmpdir:
        _write_kernelspec(tmpdir)
        manager.install_kernel_spec(tmpdir, kernel_name="poetry")
