<!-- PythonSelenium Docs -->

## Logs, The Dashboard, and Reports:

🔵 During test failures, logs and screenshots from the most recent test run will get saved to the ``latest_logs/`` folder. If ``--archive-logs`` is specified (or if ARCHIVE_EXISTING_LOGS is set to True in [settings.py](/pythonselenium/config/settings.py)), test logs will also get archived to the ``archived_logs/`` folder. Otherwise, the log files will be cleaned out when the next test run begins (by default).

```bash
pytest test_fail.py
```

(Log files in [PythonSelenium/examples/example_logs](/examples/example_logs) were generated when [test_fail.py](/examples/test_fail.py) ran and failed.)

<b>Examples of expected log files generated during failures:</b>

* [basic_test_info.txt](/examples/example_logs/basic_test_info.txt)
* [page_source.html](/examples/example_logs/page_source.html)
* [screenshot.png](/examples/example_logs/screenshot.png)


<b>In addition to log files, you can also generate dashboards and test reports.</b>

--------

<h3>The PythonSelenium Dashboard:</h3>

🔵 The ``--dashboard`` option for pytest generates a PythonSelenium Dashboard located at ``dashboard.html``, which updates automatically as tests run and produce results. Example:

```bash
pytest --dashboard --rs --headless
```

🔵 Additionally, you can host your own PythonSelenium Dashboard Server on a port of your choice. Here's an example of that using Python 3's ``http.server``:

```bash
python -m http.server 1948
```

🔵 Now you can navigate to ``http://localhost:1948/dashboard.html`` in order to view the dashboard as a web app. This requires two different terminal windows: one for running the server, and another for running the tests, which should be run from the same directory. (Use <kbd>Ctrl+C</kbd> to stop the http server.)

🔵 Here's a full example of what the PythonSelenium Dashboard may look like:

```bash
pytest test_suite.py test_image_saving.py --dashboard --rs --headless
```

--------

<h3>Pytest Reports:</h3>

🔵 Using ``--html=report.html`` gives you a fancy report of the name specified after your test suite completes.

```bash
pytest test_suite.py --html=report.html
```

🔵 When combining pytest html reports with PythonSelenium Dashboard usage, the pie chart from the Dashboard will get added to the html report. Additionally, if you set the html report URL to be the same as the Dashboard URL when also using the dashboard, (example: ``--dashboard --html=dashboard.html``), then the Dashboard will become an advanced html report when all the tests complete.

🔵 Here's an example of an upgraded html report:

```bash
pytest test_suite.py --dashboard --html=report.html
```

--------

If viewing ``pytest-html`` reports in [Jenkins](https://www.jenkins.io/), you may need to [configure Jenkins settings](https://stackoverflow.com/a/46197356) for the HTML to render correctly. This is due to [Jenkins CSP changes](https://www.jenkins.io/doc/book/security/configuring-content-security-policy/). That setting can be changed from ``Manage Jenkins`` > ``Script Console`` by running:

```
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
```

--------

You can also use ``--junit-xml=report.xml`` to get an xml report instead. Jenkins can use this file to display better reporting for your tests.

```bash
pytest test_suite.py --junit-xml=report.xml
```

--------

<h3>pynose Test Reports:</h3>

The ``pynose`` ``--report`` option gives you a fancy report after your tests complete.

```bash
pynose test_suite.py --report
```

(NOTE: You can add ``--show-report`` to immediately display pynose reports after the test suite completes. Only use ``--show-report`` when running tests locally because it pauses the test run.)

--------

<h3>🐝⚪ Behave Dashboard & Reports:</h3>

(The [behave_bdd/](/examples/behave_bdd) folder can be found in the [examples/](/examples) folder.)

```bash
behave behave_bdd/features/ -D dashboard -D headless
```

You can also use ``--junit`` to get ``.xml`` reports for each Behave feature. Jenkins can use these files to display better reporting for your tests.

```bash
behave behave_bdd/features/ --junit -D rs -D headless
```

--------
