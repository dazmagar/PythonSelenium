<!-- PythonSelenium Docs -->

## PythonSelenium Behave GUI / Commander 🐝🎖️

🐝🎖️ The <b>PythonSelenium Behave GUI</b> lets you run <code>behave</code> scripts from a Desktop GUI.<br>

🐝🎖️ To launch it, call ``pysel behave-gui`` or ``pysel gui-behave``:

```bash
> pysel behave-gui
* Starting the PythonSelenium Behave Commander GUI App...
```

🐝🎖️ <b>PythonSelenium Behave GUI</b> loads the same tests that are found by:

```bash
behave -d
```

🐝🎖️ You can customize which tests are loaded by passing additional args:

```bash
pysel behave-gui [OPTIONAL PATH or TEST FILE]
```

🐝🎖️ Here are examples of customizing test collection:

```bash
pysel behave-gui  # all tests
pysel behave-gui -i=swag  # tests with "swag" in the name
pysel behave-gui features/  # tests located in the "features/" folder
pysel behave-gui features/swag_labs.feature  # tests in that feature
```

🐝🎖️ Once launched, you can further customize which tests to run and what settings to use. There are various controls for changing settings, modes, and other "behave" command line options that are specific to PythonSelenium. You can also set additional options that don't have a visible toggle. When you're ready to run the selected tests with the specified options, click on the <code>Run Selected Tests</code> button.

--------
