<!-- PythonSelenium Docs -->

## Example Tests:

* <b>PythonSelenium</b> tests are run with <b>pytest</b>.
* Chrome is the default browser if not specified.
* Tests are structured using [14 unique syntax formats](/help_docs/syntax_formats.md).
* Logs from test failures are saved to ``./latest_logs/``.
* Tests can be run with [multiple command-line options](/help_docs/customizing_test_runs.md).
* Examples can be found in: **[PythonSelenium/examples/](/examples)**.

(NOTE: Some example tests fail on purpose to demonstrate [logging features](/examples/example_logs/ReadMe.md).)

--------

<h3>Example tests with run commands to help you get started:</h3>

--------

Run an [example test](/examples/my_first_test.py): (Default option: ``--chrome``)

```bash
pytest my_first_test.py
```

--------

Here's one way of changing the browser to Firefox:

```bash
pytest my_first_test.py --firefox
```

--------

Another [example test](/examples/offline_examples/test_demo_page.py) for a web page that has lots of different HTML items:

```bash
pytest test_demo_page.py
```

--------

Run an example test in ``--demo`` mode: (highlight assertions)

```bash
pytest test_swag_labs.py --demo
```

--------

Run [test_coffee_cart.py](/examples/test_coffee_cart.py) to test the [Coffee Cart](https://coffee-cart.app/) app:

```bash
pytest test_coffee_cart.py --demo
```

--------

Run a [Wordle-solver example](/examples/wordle_test.py):

```bash
pytest wordle_test.py
```

--------

Run a [example test](/examples/my_first_test.py) in ``--headless`` mode: (invisible browser)

```bash
pytest my_first_test.py --headless
```

--------

Run an [example test](/examples/test_swag_labs.py) using Chrome's mobile device emulator: (default settings)

```bash
pytest test_swag_labs.py --mobile
```

--------

Run an [example test](/examples/test_xkcd.py) in ``--demo`` mode: (highlight assertions)

```bash
pytest test_xkcd.py --demo
```

--------

Run a [test suite](/examples/test_suite.py) with verbose output: (see more details)

```bash
pytest test_suite.py -v
```

--------

Run a test suite using multiple parallel processes (``-n=NUM``):

```bash
pytest test_suite.py -n=8
```

--------

Run a [parameterized test](/examples/parameterized_test.py): (Generates multiple tests from one)

```bash
pytest parameterized_test.py -v
```

--------

Run a test suite and generate a PythonSelenium Dashboard:

```bash
pytest test_suite.py --dashboard
```

--------

Run a test suite and generate a ``pytest`` report:

```bash
pytest test_suite.py --html=report.html
```

--------

Run a [failing test](/examples/test_fail.py): (See the ``latest_logs/`` folder for logs and screenshots)

```bash
pytest test_fail.py
```

--------

Run a failing test that activates ``pdb`` debug mode on failure:

```bash
pytest test_fail.py --pdb -s
```

> (**``pdb``** commands: ``n``, ``c``, ``s``, ``u``, ``d`` => ``next``, ``continue``, ``step``, ``up``, ``down``)

--------

Run a test suite that demonstrates the use of ``pytest`` markers:

```bash
pytest -m marker_test_suite -v
```

--------

Run a test suite that reuses the browser session between tests:

```bash
pytest test_suite.py --rs
```

--------

Run an [example test](/examples/rate_limiting_test.py) demonstrating the ``rate_limited`` Python decorator:

```bash
pytest rate_limiting_test.py
```

--------

Run an [example test](/examples/upload_file_test.py) that demonstrates how to upload a file to a website:

```bash
pytest upload_file_test.py
```

--------

🎖️  **PythonSelenium Commander** is a GUI for ``pytest``:

```bash
pysel gui
```

--------

<b>PythonSelenium tests can also be run with ``pynose``:</b>

```bash
pynose my_first_test.py
```

--------

Run an example test suite and generate a ``pynose`` test report:

```bash
pynose test_suite.py --report --show-report
```

--------

Run an example test using a ``pynose`` configuration file:

```bash
pynose my_first_test.py --config=example_config.cfg
```

--------

For more advanced **run commands**, such as using a proxy server, see [help_docs/customizing_test_runs.md](/help_docs/customizing_test_runs.md)

--------

If you just need to perform some quick website verification on various devices, you can use the <a href="">PythonSelenium Device Farm</a>. Just plug in a website URL, and it will display how the website looks on four different devices.

--------

To make things easier, here's a **simple GUI program** that allows you to run a few example tests by pressing a button:

```bash
python gui_test_runner.py
```

(The newer **[PythonSelenium Commander](/help_docs/commander.md/)** improves on that.)

--------
