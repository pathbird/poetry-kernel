import os.path
import signal
import subprocess
import sys

import colorama


def main():
    colorama.init()

    if not os.path.exists("pyproject.toml"):
        print(
            colorama.Fore.RED + colorama.Style.BRIGHT +
            "\n" +
            "!" * 80 + "\n" +
            "!! Cannot start Poetry kernel: expected pyproject.toml in notebook directory\n" +
            "!! Do you need to run `poetry init`?\n" +
            "!" * 80 + "\n" +
            colorama.Style.RESET_ALL,
            file=sys.stderr,
            sep="\n",
        )
        raise RuntimeError("Cannot start Poetry kernel: expected pyproject.toml")

    cmd = [
        "poetry", "run",
        "python", "-m", "ipykernel_launcher",
        *sys.argv[1:],
    ]
    proc = subprocess.Popen(cmd)

    forward_signals = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}

    def handle_signal(sig, _frame):
        proc.send_signal(sig)

    for sig in forward_signals:
        signal.signal(sig, handle_signal)

    exit_code = proc.wait()
    if exit_code == 0:
        print("ipykernel_launcher exited", file=sys.stderr)
    else:
        print("ipykernel_launcher exited with error code:", exit_code, file=sys.stderr)


if __name__ == "__main__":
    main()
