"""Can run with "python" instead of using "pytest" directly.
Usage: "python raw_call.py".
Two examples: pytest.main() and subprocess.call()."""

import subprocess

import pytest

if __name__ == "__main__":
    pytest.main(["examples/github_test.py", "--chrome", "-v"])
    subprocess.call(["pytest", "examples/test_apple_site.py", "--chrome", "-v"])
