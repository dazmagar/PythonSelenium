<!-- PythonSelenium Docs -->

<a id="feature_list"></a>

## PythonSelenium Features: 🏰

* A powerful Python framework for browser automation and E2E UI testing.
* Includes [Recorder Mode](/help_docs/recorder_mode.md) for instantly generating browser tests in Python.
* Supports multiple browsers, tabs, iframes, and proxies in the same test.
* Includes [Test Case Management Software](/help_docs/case_plans.md) with Markdown technology.
* Automatic smart-waiting improves reliability and prevents flaky tests.
* Supports [pytest](https://docs.pytest.org/en/latest/), [unittest](https://docs.python.org/3/library/unittest.html), [nose](http://nose.readthedocs.io/en/latest/), and [behave](https://behave.readthedocs.io/en/stable/index.html) for finding/running tests.
* All the code is open source. Look inside to learn about any feature.
* Powerful logging tools for [dashboards, reports, and screenshots](/examples/example_logs/ReadMe.md).
* Can run tests in Headless Mode to hide the browser. (``--headless``)
* Can run tests multithreaded from parallel browsers. (``-n NUM_THREADS``)
* Can run tests from a shared browser session. (``--reuse-session``/``--rs``)
* Can run tests using [Chromium's mobile device emulator](/help_docs/mobile_testing.md). (``--mobile``)
* Can run tests through a proxy server. (``--proxy=IP_ADDRESS:PORT``)
* Can run tests with proxy settings via PAC URL. (``--proxy-pac-url=URL.pac``)
* Can run tests through an authenticated proxy server. (``--proxy=USER:PASS@HOST:PORT``)
* Can run tests with proxy+auth via PAC URL. (``--proxy-pac-url=USER:PASS@URL.pac``)
* Can run tests with a customized browser user agent. (``--agent=USER_AGENT_STRING``)
* Can set a Chromium User Data Directory/Profile to load. (``--user-data-dir=DIR``)
* Can [avoid detection](/help_docs/uc_mode.md) by sites that try to block Selenium. (``--undetected``/``--uc``)
* Can integrate with [selenium-wire](https://github.com/wkeeling/selenium-wire) for inspecting browser requests. (``--wire``)
* Can load Chrome Extension ZIP files. (``--extension-zip=ZIP``)
* Can load Chrome Extension folders. (``--extension-dir=DIR``)
* Powerful [console scripts](/pythonselenium/console_scripts/ReadMe.md). (Type **``pythonselenium``** or **``pysel``** to use.)
* Has the ability to translate tests into [multiple spoken languages](https://github.com/pythonselenium/PythonSelenium/tree/master/examples/translations).
* Has a flexible [command-line interface](/help_docs/customizing_test_runs.md) for customizing test runs.
* Has a [global config file](/pythonselenium/config/settings.py) for configuring settings as needed.
* Includes a tool for [creating interactive web presentations](/examples/presenter/ReadMe.md).
* Includes [Chart Maker](/examples/chart_maker/ReadMe.md), a tool for creating interactive charts.
* Includes a [dialog box builder](/examples/dialog_boxes/ReadMe.md) to allow user-input during automation.
* Includes a [website tour builder](/examples/tour_examples/ReadMe.md) for creating interactive walkthroughs.
* Includes a GUI for running pytest scripts: [PythonSelenium Commander](/help_docs/commander.md).
* Includes integrations for [GitHub Actions](/integrations/github/workflows/ReadMe.md), [Google Cloud](/integrations/google_cloud/ReadMe.md), [Azure](/integrations/azure/jenkins/ReadMe.md), [S3](/pythonselenium/plugins/s3_logging_plugin.py), and [Docker](/integrations/docker/ReadMe.md).
* Can handle Google Authenticator logins with [Python's one-time password library](https://pyotp.readthedocs.io/en/latest/).
* Can load and make assertions on PDF files from websites or the local file system.
* Can inspect HTML to find issues and points of interest with the [HTML Inspector](/help_docs/html_inspector.md).
* Is backwards-compatible with Python [WebDriver](https://www.selenium.dev/projects/) methods. (Use: ``self.driver``)
* Can execute JavaScript code from Python calls. (Use: ``self.execute_script()``)
* Can pierce through [Shadow DOM selectors](/help_docs/shadow_dom.md). (Add ``::shadow`` to CSS fragments.)
* Includes a hybrid-automation solution, [MasterQA](/pythonselenium/masterqa/ReadMe.md), to speed up manual testing.
* Includes useful [Python decorators and password obfuscation methods](/pythonselenium/common/ReadMe.md).

--------
