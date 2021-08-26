import json
import os.path
import tempfile

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
    # Make this import inside the install function because this file is used
    # during package install and we don't necessarily have jupyter_client
    # installed yet
    from jupyter_client.kernelspec import KernelSpecManager

    manager = KernelSpecManager()
    with tempfile.TemporaryDirectory() as tmpdir:
        _write_kernelspec(tmpdir)
        manager.install_kernel_spec(tmpdir, kernel_name="poetry")
