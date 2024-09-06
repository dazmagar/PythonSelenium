<!-- PythonSelenium Docs -->

## PythonSelenium Installation

<h4>If installing <code>pythonselenium</code> from a Git clone, use:</h4>

```bash
git clone https://<repo>/PythonSelenium.git
cd PythonSelenium/
pip install .
```

<h4>For a development mode install in editable mode, use:</h4>

```bash
git clone https://<repo>/PythonSelenium.git
cd PythonSelenium/
pip install -e .
```

<h4>To upgrade an existing <code>pythonselenium</code> install from GitHub:</h4>

```bash
git pull  # To pull the latest version
pip install -e .  # Or "pip install ."
```

<h3><code>pip install</code> can be customized:</h3>

* (Add ``--upgrade`` OR ``-U`` to upgrade PythonSelenium.)
* (Add ``--force-reinstall`` to upgrade indirect libraries.)
* (Use ``pip3`` if multiple versions of Python are present.)

(If you're not using a virtual environment, you may need to add ``--user`` to your ``pip`` command if you're seeing errors during installation.)

--------
