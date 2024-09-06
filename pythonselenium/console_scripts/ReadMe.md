<!-- PythonSelenium Docs -->

## Console Scripts 🌠

🌟 PythonSelenium console scripts can do many things, such as downloading web drivers, creating test directories with config files, activating the PythonSelenium Recorder, launching the PythonSelenium Commander, translating tests into other languages, running a Selenium Grid, and more.

* Usage: ``pythonselenium [COMMAND] [PARAMETERS]``

* (simplified): ``pysel [COMMAND] [PARAMETERS]``

* To list all commands: ``pythonselenium --help``

(<i>For running tests, use <b>pytest</b> with pythonselenium.</i>)

```bash
COMMANDS:
      get / install    [DRIVER] [OPTIONS]
      methods          (List common Python methods)
      options          (List common pytest options)
      behave-options   (List common behave options)
      gui / commander  [OPTIONAL PATH or TEST FILE]
      behave-gui       (pysel Commander for Behave)
      caseplans        [OPTIONAL PATH or TEST FILE]
      mkdir            [DIRECTORY] [OPTIONS]
      mkfile           [FILE.py] [OPTIONS]
      mkrec / codegen  [FILE.py] [OPTIONS]
      recorder         (Open Recorder Desktop App.)
      record           (If args: mkrec. Else: App.)
      mkchart          [FILE.py] [LANG]
      print            [FILE] [OPTIONS]
      convert          [WEBDRIVER_UNITTEST_FILE.py]
      extract-objects  [PS_FILE.py]
      inject-objects   [PS_FILE.py] [OPTIONS]
      objectify        [PS_FILE.py] [OPTIONS]
      revert-objects   [PS_FILE.py] [OPTIONS]
      encrypt / obfuscate
      decrypt / unobfuscate
      proxy            (Start a basic proxy server)
      download server  (Get Selenium Grid JAR file)
      grid-hub         [start|stop] [OPTIONS]
      grid-node        [start|stop] --hub=[HOST/IP]
 * (EXAMPLE: "pysel get chromedriver") *

    Type "pysel help [COMMAND]" for specific command info.
    For info on all commands, type: "pythonselenium --help".
    Use "pytest" for running tests.
```

<h3>get / install</h3>

* Usage:

```bash
pysel get [DRIVER] [OPTIONS]
pysel install [DRIVER] [OPTIONS]
```

* Examples:

```bash
pysel get chromedriver
pysel get geckodriver
pysel get edgedriver
pysel get chromedriver 114
pysel get chromedriver 114.0.5735.90
pysel get chromedriver stable
pysel get chromedriver beta
pysel get chromedriver -p
```

(Drivers:  ``chromedriver``, ``geckodriver``, ``edgedriver``,
           ``iedriver``, ``uc_driver``)

(Options:  A specific driver version or major version integer.
           If not set, the driver version matches the browser.
           ``-p`` / ``--path``: Also copy to "/usr/local/bin".)

* Output:

Downloads the webdriver to ``pythonselenium/drivers/``
(``chromedriver`` is required for Chrome automation)
(``geckodriver`` is required for Firefox automation)
(``edgedriver`` is required for MS__Edge automation)

<h3>methods</h3>

* Usage:

```bash
pysel methods
```

* Output:

Displays common PythonSelenium methods.

<h3>options</h3>

* Usage:

```bash
pysel options
```

* Output:

Displays common pytest command-line options
that are available when using PythonSelenium.

```bash
--browser=BROWSER  (The web browser to use. Default is "chrome")
--edge / --firefox / --safari  (Shortcut for browser selection.)
--headless  (Run tests headlessly. Default mode on Linux OS.)
--demo  (Slow down and visually see test actions as they occur.)
--slow  (Slow down the automation. Faster than using Demo Mode.)
--rs / --reuse-session  (Reuse browser session between tests.)
--crumbs  (Clear all cookies between tests reusing a session.)
--maximize  (Start tests with the web browser window maximized.)
--dashboard  (Enable PythonSelenium\'s Dashboard at dashboard.html)
--incognito  (Enable Chromium\'s Incognito mode.)
--guest  (Enable Chromium\'s Guest Mode.)
--dark  (Enable Chromium\'s Dark Mode.)
--uc  (Use undetected-chromedriver to evade detection.)
-m=MARKER  (Run tests with the specified pytest marker.)
-n=NUM  (Multithread the tests using that many threads.)
-v  (Verbose mode. Print the full names of each test run.)
--html=report.html  (Create a detailed pytest-html report.)
--collect-only / --co  (Only show discovered tests. No run.)
--co -q  (Only show full names of discovered tests. No run.)
-x  (Stop running tests after the first failure is reached.)
--pdb  (Enter the Post Mortem Debug Mode after any test fails.)
--trace  (Enter Debug Mode immediately after starting any test.)
      | Debug Mode Commands  >>>   help / h: List all commands. |
      |   n: Next line of method. s: Step through. c: Continue. |
      |  return / r: Run until method returns. j: Jump to line. |
      | where / w: Show stack spot. u: Up stack. d: Down stack. |
      | longlist / ll: See code. dir(): List namespace objects. |
--help / -h  (Display list of all available pytest options.)
--final-debug  (Enter Final Debug Mode after each test ends.)
--recorder / --rec  (Save browser actions as Python scripts.)
--rec-behave / --rec-gherkin  (Save actions as Gherkin code.)
--rec-print  (Display recorded scripts when they are created.)
--save-screenshot  (Save a screenshot at the end of each test.)
--archive-logs  (Archive old log files instead of deleting them.)
--check-js  (Check for JavaScript errors after page loads.)
--start-page=URL  (The browser start page when tests begin.)
--agent=STRING  (Modify the web browser\'s User-Agent string.)
--mobile  (Use Chromium\'s mobile device emulator during tests.)
--metrics=STRING  (Set mobile "CSSWidth,CSSHeight,PixelRatio".)
--ad-block  (Block some types of display ads after page loads.)
--settings-file=FILE  (Override default PythonSelenium settings.)
--env=ENV  (Set the test env. Access with "self.env" in tests.)
--data=DATA  (Extra test data. Access with "self.data" in tests.)
--disable-csp  (Disable the Content Security Policy of websites.)
--remote-debug  (Sync to Ch-R-Debugger chrome://inspect/#devices)
--server=SERVER  (The Selenium Grid server/IP used for tests.)
--port=PORT  (The Selenium Grid port used by the test server.)
--proxy=SERVER:PORT  (Connect to a proxy server:port for tests.)
--proxy=USER:PASS@SERVER:PORT  (Use authenticated proxy server.)

For the full list of command-line options, type: "pytest --help".
```

<h3>behave-options</h3>

* Usage:

```bash
pysel behave-options
```

* Output:

Displays common Behave command-line options
that are available when using PythonSelenium.

```bash
-D browser=BROWSER  (The web browser to use. Default is "chrome")
-D headless  (Run tests headlessly. Default mode on Linux OS.)
-D demo  (Slow down and visually see test actions as they occur.)
-D slow  (Slow down the automation. Faster than using Demo Mode.)
-D reuse-session / -D rs  (Reuse browser session between tests.)
-D crumbs  (Clear all cookies between tests reusing a session.)
-D maximize  (Start tests with the web browser window maximized.)
-D dashboard  (Enable PythonSelenium\'s Dashboard at dashboard.html)
-D incognito  (Enable Chromium\'s Incognito Mode.)
-D guest  (Enable Chromium\'s Guest Mode.)
-D dark  (Enable Chromium\'s Dark Mode.)
-D uc  (Use undetected-chromedriver to evade detection.)
--no-snippets / -q  (Quiet mode. Don\'t print snippets.)
--dry-run / -d  (Dry run. Only show discovered tests.)
--stop  (Stop running tests after the first failure is reached.)
-D pdb  (Enter the Post Mortem Debug Mode after any test fails.)
      | Debug Mode Commands  >>>   help / h: List all commands. |
      |   n: Next line of method. s: Step through. c: Continue. |
      |  return / r: Run until method returns. j: Jump to line. |
      | where / w: Show stack spot. u: Up stack. d: Down stack. |
      | longlist / ll: See code. dir(): List namespace objects. |
-D recorder  (Record browser actions to generate test scripts.)
-D rec-print  (Display recorded scripts when they are created.)
-D save-screenshot  (Save a screenshot at the end of each test.)
-D archive-logs  (Archive old log files instead of deleting them.)
-D check-js  (Check for JavaScript errors after page loads.)
-D start-page=URL  (The browser start page when tests begin.)
-D agent=STRING  (Modify the web browser\'s User-Agent string.)
-D mobile  (Use Chromium\'s mobile device emulator during tests.)
-D metrics=STRING  (Set mobile "CSSWidth,CSSHeight,PixelRatio".)
-D ad-block  (Block some types of display ads after page loads.)
-D settings-file=FILE  (Override default PythonSelenium settings.)
-D env=ENV  (Set the test env. Access with "self.env" in tests.)
-D data=DATA  (Extra test data. Access with "self.data" in tests.)
-D disable-csp  (Disable the Content Security Policy of websites.)
-D remote-debug  (Sync to Ch-R-Debugger chrome://inspect/#devices)
-D server=SERVER  (The Selenium Grid server/IP used for tests.)
-D port=PORT  (The Selenium Grid port used by the test server.)
-D proxy=SERVER:PORT  (Connect to a proxy server:port for tests.)
-D proxy=USER:PASS@SERVER:PORT  (Use authenticated proxy server.)

For the full list of command-line options, type: "behave --help".
```

<h3>gui / commander</h3>

* Usage:

```bash
pysel gui [OPTIONAL PATH or TEST FILE]
pysel commander [OPTIONAL PATH or TEST FILE]
```

<h3>behave-gui</h3>

* Usage:

```bash
pysel behave-gui [OPTIONAL PATH or TEST FILE]
pysel gui-behave [OPTIONAL PATH or TEST FILE]
```

* Examples:

```bash
pysel behave-gui
pysel behave-gui -i=swag
pysel behave-gui features/
pysel behave-gui features/swag_labs.feature
```

* Output:

Launches PythonSelenium Commander / GUI for Behave.

<h3>caseplans</h3>

* Usage:

```bash
pysel caseplans [OPTIONAL PATH or TEST FILE]
```

* Examples:

```bash
pysel caseplans
pysel caseplans -k agent
pysel caseplans -m marker2
pysel caseplans test_suite.py
pysel caseplans offline_examples/
```

* Output:

Launches the PythonSelenium Case Plans Generator.

<h3>mkdir</h3>

* Usage:

```bash
pysel mkdir [DIRECTORY] [OPTIONS]
```

* Example:

```bash
pysel mkdir ui_tests
```

* Options:

``-b`` / ``--basic``  (Only config files. No tests added.)

* Output:

Creates a new folder for running pysel scripts.
The new folder contains default config files,
sample tests for helping new users get started,
and Python boilerplates for setting up customized
test frameworks.

```bash
ui_tests/
├── __init__.py
├── my_first_test.py
├── parameterized_test.py
├── pytest.ini
├── requirements.txt
├── setup.cfg
├── test_demo_site.py
└── boilerplates/
    ├── __init__.py
    ├── base_test_case.py
    ├── boilerplate_test.py
    ├── classic_obj_test.py
    ├── page_objects.py
    ├── ps_fixture_test.py
    └── samples/
        ├── __init__.py
        ├── google_objects.py
        ├── google_test.py
        ├── ps_swag_test.py
        └── swag_labs_test.py
```

If running with the ``-b`` or ``--basic`` option:

```bash
ui_tests/
├── __init__.py
├── pytest.ini
├── requirements.txt
└── setup.cfg
```

<h3>mkfile</h3>

* Usage:

```bash
pysel mkfile [FILE.py] [OPTIONS]
```

* Example:

```bash
pysel mkfile new_test.py
```

* Options:

`-b` / `--basic`  (Basic boilerplate / single-line test)
`-r` / `--rec`  (adds Pdb+ breakpoint for Recorder Mode)
``--url=URL``  (makes the test start on a specific page)

* Language Options:

``--en`` / ``--English``

* Syntax Formats:

``--bc`` / ``--basecase``      (BaseCase class inheritance)
``--pf`` / ``--pytest-fixture``         (ps pytest fixture)
``--cf`` / ``--class-fixture``  (class + ps pytest fixture)
``--cm`` / ``--context-manager``       (PS context manager)
``--dc`` / ``--driver-context``     (DriverContext manager)
``--dm`` / ``--driver-manager``            (Driver manager)

* Output:

Creates a new pysel test file with boilerplate code.
If the file already exists, an error is raised.
By default, uses English with BaseCase inheritance,
and creates a boilerplate with common PythonSelenium
methods: "open", "type", "click", "assert_element",
and "assert_text". If using the basic boilerplate
option, only the "open" method is included. Only the
BaseCase format supports Languages or Recorder Mode.

<h3>mkrec / record / codegen</h3>

* Usage:

```bash
pysel mkrec [FILE.py] [OPTIONS]
pysel codegen [FILE.py] [OPTIONS]
```

* Examples:

```bash
pysel mkrec new_test.py
pysel mkrec new_test.py --url=wikipedia.org
pysel codegen new_test.py
pysel codegen new_test.py --url=wikipedia.org
```

* Options:

``--url=URL``  (Sets the initial start page URL.)
``--edge``  (Use Edge browser instead of Chrome.)
``--gui`` / ``--headed``  (Use headed mode on Linux.)
``--uc`` / ``--undetected``  (Use undetectable mode.)
``--ee``  (Use SHIFT + ESC to end the recording.)
``--overwrite``  (Overwrite file when it exists.)
``--behave``  (Also output Behave/Gherkin files.)

* Output:

Creates a new PythonSelenium test using the Recorder.
If the filename already exists, an error is raised.

<h3>recorder</h3>

* Usage:

```bash
pysel recorder [OPTIONS]
```

* Options:

``--uc`` / ``--undetected``  (Use undetectable mode.)
``--behave``  (Also output Behave/Gherkin files.)

* Output:

Launches the PythonSelenium Recorder Desktop App.

<h3>mkchart</h3>

* Usage:

```bash
pysel mkchart [FILE.py] [LANG]
```

* Example:

```bash
pysel mkchart new_chart.py --en
```

* Language Options:

``--en`` / ``--English``

* Output:

Creates a new PythonSelenium chart presentation.
If the file already exists, an error is raised.
By default, the slides are written in English,
and use a "sky" theme with "slide" transition.
The chart can be used as a basic boilerplate.

<h3>print</h3>

* Usage:

```bash
pysel print [FILE] [OPTIONS]
```

* Options:

``-n`` (Add line Numbers to the rows)

* Output:

Prints the code/text of any file
with syntax-highlighting.

<h3>extract-objects</h3>

* Usage:

```bash
pysel extract-objects [PS_FILE.py]
```

* Output:

Creates page objects based on selectors found in a
PythonSelenium Python file and saves those objects to the
"page_objects.py" file in the same folder as the tests.

<h3>inject-objects</h3>

* Usage:

```bash
pysel inject-objects [PS_FILE.py] [OPTIONS]
```

* Options:

``-c``, ``--comments``  (Add object selectors to the comments.)

* Output:

Takes the page objects found in the "page_objects.py"
file and uses those to replace matching selectors in
the selected PythonSelenium Python file.

<h3>objectify</h3>

* Usage:

```bash
pysel objectify [PS_FILE.py] [OPTIONS]
```

* Options:

``-c``, ``--comments``  (Add object selectors to the comments.)

* Output:

A modified version of the file where the selectors
have been replaced with variable names defined in
"page_objects.py", supporting the Page Object Pattern.
(This has the same outcome as combining
``extract-objects`` with ``inject-objects``)

<h3>revert-objects</h3>

* Usage:

```bash
pysel revert-objects [PS_FILE.py] [OPTIONS]
```

* Options:

``-c``, ``--comments``  (Keep existing comments for the lines.)

* Output:

Reverts the changes made by ``pythonselenium objectify ...`` or
``pythonselenium inject-objects ...`` when run against a
PythonSelenium file. Objects will get replaced by
selectors stored in the "page_objects.py" file.

<h3>convert</h3>

* Usage:

```bash
pysel convert [WEBDRIVER_UNITTEST_FILE.py]
```

* Output:

Converts a Selenium IDE exported WebDriver unittest
file into a PythonSelenium file. Adds ``_PS`` to the
new filename while keeping the original file intact.
Works on both Selenium IDE & Katalon Recorder scripts.

<h3>encrypt / obfuscate</h3>

* Usage:

``pysel encrypt``  OR  ``pysel obfuscate``

* Output:

Runs the password encryption/obfuscation tool.
(Where you can enter a password to encrypt/obfuscate.)

<h3>decrypt / unobfuscate</h3>

* Usage:

``pysel decrypt``  OR  ``pysel unobfuscate``

* Output:

Runs the password decryption/unobfuscation tool.
(Where you can enter an encrypted password to decrypt.)

<h3>proxy</h3>

* Usage:

```bash
pysel proxy [OPTIONS]
```

* Options:

``--hostname=HOSTNAME``  (Set ``hostname``) (Default: ``127.0.0.1``)
``--port=PORT``          (Set ``port``)     (Default: ``8899``)
``--help`` / ``-h``      (Display list of all available ``proxy`` options.)

* Output:

Launch a basic proxy server on the current machine.
(Uses ``127.0.0.1:8899`` as the default address.)

<h3>download</h3>

* Usage:

```bash
pysel download server
```

* Output:

Downloads the Selenium Server JAR file for Grid usage.
(That JAR file is required when using a Selenium Grid)

<h3>grid-hub</h3>

* Usage:

```bash
pysel grid-hub {start|stop|restart} [OPTIONS]
```

* Options:

``-v``, ``--verbose``  (Increases verbosity of logging output.)
``--timeout=TIMEOUT``  (Close idle browser windows after TIMEOUT seconds.)

* Output:

Controls the Selenium Grid Hub server, which allows
for running tests on multiple machines in parallel
to speed up test runs and reduce the total time
of test suite execution.
You can start, restart, or stop the Grid Hub server.

<h3>grid-node</h3>

* Usage:

```bash
pysel grid-node {start|stop|restart} [OPTIONS]
```

* Options:

``--hub=HUB_IP`` (The Grid Hub IP Address to connect to.) (Default: ``127.0.0.1``)
``-v``, ``--verbose``  (Increases verbosity of logging output.)

* Output:

Controls the Selenium Grid node, which serves as a
worker machine for your Selenium Grid Hub server.
You can start, restart, or stop the Grid node.

--------
