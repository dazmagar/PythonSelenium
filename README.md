## Virtual Environment Setup

1. Run `python -m venv venv`.
2. Activate the virtual environment : `.\venv\Scripts\activate` or `source ./venv/bin/activate`
   > To deactivate simply run `deactivate`

## Requirements Setup

After the virtual environment has been setup;

1. Run `python -m pip install --upgrade pip setuptools` This should upgrade pip to the latest version.
2. Run `pip install -e .` This install PythonSelenium in editable mode.

## Linter & Formatter Setup (vs code)
1. Install `Flake8` plugin.
2. Install `Black Formatter` plugin.
