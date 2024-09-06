<!-- PythonSelenium Docs -->

## PythonSelenium Commander 🎖️

🎖️ <b>PythonSelenium Commander</b> lets you run <code>pytest</code> scripts from a Desktop GUI.<br>

🎖️ To launch it, call ``pysel commander`` or ``pysel gui``:

```bash
pysel gui
* Starting the PythonSelenium Commander Desktop App...
```

🎖️ <b>PythonSelenium Commander</b> loads the same tests that are found by:

```bash
pytest --co -q
```

🎖️ You can customize which tests are loaded by passing additional args:

```bash
pysel commander [OPTIONAL PATH or TEST FILE]
pysel gui [OPTIONAL PATH or TEST FILE]
```

🎖️ Here are examples of customizing test collection:

```bash
pysel gui
pysel gui -k agent
pysel gui -m marker2
pysel gui test_suite.py
pysel gui offline_examples/
```

🎖️ Once launched, you can further customize which tests to run and what settings to use. There are various controls for changing settings, modes, and other pytest command line options that are specific to PythonSelenium. You can also set additional options that don't have a visible toggle. When you're ready to run the selected tests with the specified options, click on the <code>Run Selected Tests</code> button.

--------

<h3>Other PythonSelenium Commanders:</h3>

* 🐝🎖️ [PythonSelenium Behave GUI / Commander](/help_docs/behave_gui.md)

--------
