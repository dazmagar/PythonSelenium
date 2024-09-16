## Virtual Environment Setup

1. Run `python -m venv venv`.
2. Activate the virtual environment : `.\venv\Scripts\activate` or `source ./venv/bin/activate`
   > To deactivate simply run `deactivate`

## Requirements Setup
After the virtual environment has been setup:
1. Run `python -m pip install --upgrade pip setuptools` This should upgrade pip to the latest version.
2. Run `pip install -e .` This install PythonSelenium in editable mode.
To install additional dependencies from `pyproject.toml` file, you can run following commands:
3. `pip install -e .[allure]` This install allure dependencies
4. `pip install -e .[flake8]` This install flake8 dependencies

## Linter & Formatter Setup (vs code)
1. Install `Flake8` plugin.
2. Install `Black Formatter` plugin.

## Help commands

### Clean `__pycache__` and `.pytest_cache` folders using `git clear`:

To clean up cache directories add the following alias:

```bash
git config alias.clear "!f() { python ./examples/clean_pycache.py; }; f"
