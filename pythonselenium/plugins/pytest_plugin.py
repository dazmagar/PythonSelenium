"""This is the pytest configuration file for setting test options."""

import os
import sys
import time

import colorama
import pytest

from pythonselenium import config as ps_config
from pythonselenium.config import settings
from pythonselenium.core import log_helper
from pythonselenium.fixtures import constants, shared_utils

is_windows = shared_utils.is_windows()
python3_11_or_newer = False
if sys.version_info >= (3, 11):
    python3_11_or_newer = True
py311_patch2 = constants.PatchPy311.PATCH
sys_argv = sys.argv
pytest_plugins = ["pytester"]  # Adds the "testdir" fixture


def pytest_addoption(parser):
    """This plugin adds the following command-line options to pytest:
    --browser=BROWSER  (The web browser to use. Default: "chrome".)
    --chrome  (Shortcut for "--browser=chrome". Default.)
    --edge  (Shortcut for "--browser=edge".)
    --firefox  (Shortcut for "--browser=firefox".)
    --safari  (Shortcut for "--browser=safari".)
    --settings-file=FILE  (Override default PythonSelenium settings.)
    --env=ENV  (Set the test env. Access with "self.env" in tests.)
    --account=STR  (Set account. Access with "self.account" in tests.)
    --data=STRING  (Extra test data. Access with "self.data" in tests.)
    --var1=STRING  (Extra test data. Access with "self.var1" in tests.)
    --var2=STRING  (Extra test data. Access with "self.var2" in tests.)
    --var3=STRING  (Extra test data. Access with "self.var3" in tests.)
    --variables=DICT  (Extra test data. Access with "self.variables".)
    --user-data-dir=DIR  (Set the Chrome user data directory to use.)
    --protocol=PROTOCOL  (The Selenium Grid protocol: http|https.)
    --server=SERVER  (The Selenium Grid server/IP used for tests.)
    --port=PORT  (The Selenium Grid port used by the test server.)
    --cap-file=FILE  (The web browser's desired capabilities to use.)
    --cap-string=STRING  (The web browser's desired capabilities to use.)
    --proxy=SERVER:PORT  (Connect to a proxy server:port as tests are running)
    --proxy=USERNAME:PASSWORD@SERVER:PORT  (Use an authenticated proxy server)
    --proxy-bypass-list=STRING (";"-separated hosts to bypass, Eg "*.foo.com")
    --proxy-pac-url=URL  (Connect to a proxy server using a PAC_URL.pac file.)
    --proxy-pac-url=USERNAME:PASSWORD@URL  (Authenticated proxy with PAC URL.)
    --proxy-driver  (If a driver download is needed, will use: --proxy=PROXY.)
    --multi-proxy  (Allow multiple authenticated proxies when multi-threaded.)
    --agent=STRING  (Modify the web browser's User-Agent string.)
    --mobile  (Use the mobile device emulator while running tests.)
    --metrics=STRING  (Set mobile metrics: "CSSWidth,CSSHeight,PixelRatio".)
    --chromium-arg="ARG=N,ARG2" (Set Chromium args, ","-separated, no spaces.)
    --firefox-arg="ARG=N,ARG2" (Set Firefox args, comma-separated, no spaces.)
    --firefox-pref=SET  (Set a Firefox preference:value set, comma-separated.)
    --extension-zip=ZIP  (Load a Chrome Extension .zip|.crx, comma-separated.)
    --extension-dir=DIR  (Load a Chrome Extension directory, comma-separated.)
    --disable-features="F1,F2" (Disable features, comma-separated, no spaces.)
    --binary-location=PATH  (Set path of the Chromium browser binary to use.)
    --driver-version=VER  (Set the chromedriver or uc_driver version to use.)
    --sjw  (Skip JS Waits for readyState to be "complete" or Angular to load.)
    --pls=PLS  (Set pageLoadStrategy on Chrome: "normal", "eager", or "none".)
    --headless  (Run tests in headless mode. The default arg on Linux OS.)
    --headless2  (Use the new headless mode, which supports extensions.)
    --headed  (Run tests in headed/GUI mode on Linux OS, where not default.)
    --xvfb  (Run tests using the Xvfb virtual display server on Linux OS.)
    --locale=LOCALE_CODE  (Set the Language Locale Code for the web browser.)
    --interval=SECONDS  (The autoplay interval for presentations & tour steps)
    --start-page=URL  (The starting URL for the web browser when tests begin.)
    --archive-logs  (Archive existing log files instead of deleting them.)
    --archive-downloads  (Archive old downloads instead of deleting them.)
    --time-limit=SECONDS  (Safely fail any test that exceeds the time limit.)
    --slow  (Slow down the automation. Faster than using Demo Mode.)
    --demo  (Slow down and visually see test actions as they occur.)
    --demo-sleep=SECONDS  (Set the wait time after Slow & Demo Mode actions.)
    --highlights=NUM  (Number of highlight animations for Demo Mode actions.)
    --message-duration=SECONDS  (The time length for Messenger alerts.)
    --check-js  (Check for JavaScript errors after page loads.)
    --ad-block  (Block some types of display ads from loading.)
    --host-resolver-rules=RULES  (Set host-resolver-rules, comma-separated.)
    --block-images  (Block images from loading during tests.)
    --do-not-track  (Indicate to websites that you don't want to be tracked.)
    --verify-delay=SECONDS  (The delay before MasterQA verification checks.)
    --ee / --esc-end  (Lets the user end the current test via the ESC key.)
    --recorder  (Enables the Recorder for turning browser actions into code.)
    --rec-behave  (Same as Recorder Mode, but also generates behave-gherkin.)
    --rec-sleep  (If the Recorder is enabled, also records self.sleep calls.)
    --rec-print  (If the Recorder is enabled, prints output after tests end.)
    --disable-js  (Disable JavaScript on websites. Pages might break!)
    --disable-csp  (Disable the Content Security Policy of websites.)
    --disable-ws  (Disable Web Security on Chromium-based browsers.)
    --enable-ws  (Enable Web Security on Chromium-based browsers.)
    --enable-sync  (Enable "Chrome Sync" on websites.)
    --uc | --undetected  (Use undetected-chromedriver to evade bot-detection.)
    --uc-cdp-events  (Capture CDP events when running in "--undetected" mode.)
    --log-cdp  ("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    --remote-debug  (Sync to Chrome Remote Debugger chrome://inspect/#devices)
    --ftrace | --final-trace  (Debug Mode after each test. Don't use with CI!)
    --dashboard  (Enable the PythonSelenium Dashboard. Saved at: dashboard.html)
    --dash-title=STRING  (Set the title shown for the generated dashboard.)
    --enable-3d-apis  (Enables WebGL and 3D APIs.)
    --swiftshader  (Chrome "--use-gl=angle" / "--use-angle=swiftshader-webgl")
    --incognito  (Enable Chrome's Incognito mode.)
    --guest  (Enable Chrome's Guest mode.)
    --dark  (Enable Chrome's Dark mode.)
    --devtools  (Open Chrome's DevTools when the browser opens.)
    --rs | --reuse-session  (Reuse browser session for all tests.)
    --rcs | --reuse-class-session  (Reuse session for tests in class.)
    --crumbs  (Delete all cookies between tests reusing a session.)
    --disable-beforeunload  (Disable the "beforeunload" event on Chrome.)
    --window-size=WIDTH,HEIGHT  (Set the browser's starting window size.)
    --maximize  (Start tests with the browser window maximized.)
    --screenshot  (Save a screenshot at the end of each test.)
    --no-screenshot  (No screenshots saved unless tests directly ask it.)
    --visual-baseline  (Set the visual baseline for Visual/Layout tests.)
    --wire  (Use selenium-wire's webdriver for replacing selenium webdriver.)
    --external-pdf  (Set Chromium "plugins.always_open_pdf_externally":True.)
    --timeout-multiplier=MULTIPLIER  (Multiplies the default timeout values.)
    --list-fail-page  (After each failing test, list the URL of the failure.)
    """
    c1 = ""
    c2 = ""
    c3 = ""
    cr = ""
    if "linux" not in sys.platform:
        # This will be seen when typing "pytest --help" on the command line.
        if is_windows and hasattr(colorama, "just_fix_windows_console"):
            colorama.just_fix_windows_console()
        else:
            colorama.init(autoreset=True)
        c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
        c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
        c3 = colorama.Fore.MAGENTA + colorama.Back.LIGHTYELLOW_EX
        cr = colorama.Style.RESET_ALL
    s_str = "PythonSelenium"
    s_str = s_str.replace("PythonSelenium", c1 + "Python" + c2 + "Selenium" + cr)
    s_str = s_str + cr + " " + c3 + "command-line options for pytest" + cr
    parser = parser.getgroup("PythonSelenium", s_str)
    parser.addoption(
        "--browser",
        action="store",
        dest="browser",
        type=str.lower,
        choices=constants.ValidBrowsers.valid_browsers,
        default=constants.Browser.GOOGLE_CHROME,
        help="""Specifies the web browser to use. Default: Chrome.
                Examples: (--browser=edge OR --browser=firefox)""",
    )
    parser.addoption(
        "--chrome",
        action="store_true",
        dest="use_chrome",
        default=False,
        help="""Shortcut for --browser=chrome (Default)""",
    )
    parser.addoption(
        "--edge",
        action="store_true",
        dest="use_edge",
        default=False,
        help="""Shortcut for --browser=edge""",
    )
    parser.addoption(
        "--firefox",
        action="store_true",
        dest="use_firefox",
        default=False,
        help="""Shortcut for --browser=firefox""",
    )
    parser.addoption(
        "--ie",
        action="store_true",
        dest="use_ie",
        default=False,
        help="""Shortcut for --browser=ie""",
    )
    parser.addoption(
        "--safari",
        action="store_true",
        dest="use_safari",
        default=False,
        help="""Shortcut for --browser=safari""",
    )
    parser.addoption(
        "--with-selenium",
        action="store_true",
        dest="with_selenium",
        default=True,
        help="""(DEPRECATED) Start tests with an open web browser.
                (This is ALWAYS True now when importing BaseCase)""",
    )
    parser.addoption(
        "--env",
        action="store",
        dest="environment",
        type=str.lower,
        choices=(
            constants.Environment.QA,
            constants.Environment.RC,
            constants.Environment.STAGING,
            constants.Environment.DEVELOP,
            constants.Environment.PRODUCTION,
            constants.Environment.PERFORMANCE,
            constants.Environment.REPLICA,
            constants.Environment.FEDRAMP,
            constants.Environment.OFFLINE,
            constants.Environment.ONLINE,
            constants.Environment.MASTER,
            constants.Environment.REMOTE,
            constants.Environment.LEGACY,
            constants.Environment.LOCAL,
            constants.Environment.ALPHA,
            constants.Environment.BETA,
            constants.Environment.DEMO,
            constants.Environment.GDPR,
            constants.Environment.MAIN,
            constants.Environment.TEST,
            constants.Environment.GOV,
            constants.Environment.NEW,
            constants.Environment.OLD,
            constants.Environment.UAT,
        ),
        default=constants.Environment.TEST,
        help="""This option sets a test env from a list of choices.
                Access using "self.env" or "self.environment".""",
    )
    parser.addoption(
        "--account",
        dest="account",
        default=None,
        help="""This option sets a test account string.
                In tests, use "self.account" to get the value.""",
    )
    parser.addoption(
        "--data",
        dest="data",
        default=None,
        help="Extra data to pass to tests from the command line.",
    )
    parser.addoption(
        "--var1",
        dest="var1",
        default=None,
        help="Extra data to pass to tests from the command line.",
    )
    parser.addoption(
        "--var2",
        dest="var2",
        default=None,
        help="Extra data to pass to tests from the command line.",
    )
    parser.addoption(
        "--var3",
        dest="var3",
        default=None,
        help="Extra data to pass to tests from the command line.",
    )
    parser.addoption(
        "--variables",
        dest="variables",
        default=None,
        help="""A var dict to pass to tests from the command line.
                Example usage:
                ----------------------------------------------
                Option: --variables='{"special":123}'
                Access: self.variables["special"]  # (123)
                ----------------------------------------------
                Option: --variables='{"color":"red","num":42}'
                Access: self.variables["color"]  # ("red")
                Access: self.variables["num"]  # (42)
                ----------------------------------------------""",
    )
    parser.addoption(
        "--cap_file",
        "--cap-file",
        dest="cap_file",
        default=None,
        help="""The file that stores browser desired capabilities
                for BrowserStack, Sauce Labs, or other grids.""",
    )
    parser.addoption(
        "--cap_string",
        "--cap-string",
        dest="cap_string",
        default=None,
        help="""The string that stores browser desired capabilities
                for BrowserStack, Sauce Labs, or other grids.
                Enclose cap-string in single quotes.
                Enclose parameter keys in double quotes.
                Example: --cap-string='{"name":"test1","v":"42"}'""",
    )
    parser.addoption(
        "--settings_file",
        "--settings-file",
        "--settings",
        action="store",
        dest="settings_file",
        default=None,
        help="""The file that stores key/value pairs for
                overriding values in the
                pythonselenium/config/settings.py file.""",
    )
    parser.addoption(
        "--user_data_dir",
        "--user-data-dir",
        dest="user_data_dir",
        default=None,
        help="""The Chrome User Data Directory to use. (Profile)
                If the directory doesn't exist, it'll be created.""",
    )
    parser.addoption(
        "--with-testing_base",
        "--with-testing-base",
        action="store_true",
        dest="with_testing_base",
        default=True,
        help="""(DEPRECATED) - This option is always enabled now.
                Use for saving logs & screenshots when tests fail.
                The following options are now active by default
                with --with-testing_base (which is always on now):
                --with-screen_shots ,
                --with-basic_test_info ,
                --with-page_source
            """,
    )
    parser.addoption(
        "--log_path",
        "--log-path",
        dest="log_path",
        default=constants.Logs.LATEST + "/",
        help="""(DEPRECATED) - This value is NOT EDITABLE anymore.
                Log files are saved to the "latest_logs/" folder.""",
    )
    parser.addoption(
        "--archive_logs",
        "--archive-logs",
        action="store_true",
        dest="archive_logs",
        default=False,
        help="Archive old log files instead of deleting them.",
    )
    parser.addoption(
        "--archive_downloads",
        "--archive-downloads",
        action="store_true",
        dest="archive_downloads",
        default=False,
        help="Archive old downloads instead of deleting them.",
    )
    parser.addoption(
        "--sjw",
        "--skip_js_waits",
        "--skip-js-waits",
        action="store_true",
        dest="skip_js_waits",
        default=False,
        help="""Skip all calls to wait_for_ready_state_complete()
                and wait_for_angularjs(), which are part of many
                PythonSelenium methods for improving reliability.""",
    )
    parser.addoption(
        "--with-db_reporting",
        "--with-db-reporting",
        action="store_true",
        dest="with_db_reporting",
        default=False,
        help="Use to record test data in the MySQL database.",
    )
    parser.addoption(
        "--database_env",
        "--database-env",
        action="store",
        dest="database_env",
        choices=(
            constants.Environment.QA,
            constants.Environment.RC,
            constants.Environment.STAGING,
            constants.Environment.DEVELOP,
            constants.Environment.PRODUCTION,
            constants.Environment.PERFORMANCE,
            constants.Environment.REPLICA,
            constants.Environment.FEDRAMP,
            constants.Environment.OFFLINE,
            constants.Environment.ONLINE,
            constants.Environment.MASTER,
            constants.Environment.REMOTE,
            constants.Environment.LEGACY,
            constants.Environment.LOCAL,
            constants.Environment.ALPHA,
            constants.Environment.BETA,
            constants.Environment.DEMO,
            constants.Environment.GDPR,
            constants.Environment.MAIN,
            constants.Environment.TEST,
            constants.Environment.GOV,
            constants.Environment.NEW,
            constants.Environment.OLD,
            constants.Environment.UAT,
        ),
        default=constants.Environment.TEST,
        help="The database environment to run the tests in.",
    )
    parser.addoption(
        "--with-s3_logging",
        "--with-s3-logging",
        action="store_true",
        dest="with_s3_logging",
        default=False,
        help="Use to save test log files in Amazon S3.",
    )
    parser.addoption(
        "--with-screen_shots",
        "--with-screen-shots",
        action="store_true",
        dest="with_screen_shots",
        default=False,
        help="""(DEPRECATED) - Screenshots are always saved now.
                This option saves screenshots during test failures.
                Screenshots are saved in the "latest_logs/" folder.
                (Automatically on when using --with-testing_base)""",
    )
    parser.addoption(
        "--with-basic_test_info",
        "--with-basic-test-info",
        action="store_true",
        dest="with_basic_test_info",
        default=False,
        help="""(DEPRECATED) - Info files are always saved now.
                This option saves basic test info on test failures.
                These files are saved in the "latest_logs/" folder.
                (Automatically on when using --with-testing_base)""",
    )
    parser.addoption(
        "--with-page_source",
        "--with-page-source",
        action="store_true",
        dest="with_page_source",
        default=False,
        help="""(DEPRECATED) - Page source is saved by default.
                This option saves page source files on test failures.
                (Automatically on when using --with-testing_base)""",
    )
    parser.addoption(
        "--protocol",
        action="store",
        dest="protocol",
        choices=(
            constants.Protocol.HTTP,
            constants.Protocol.HTTPS,
        ),
        default=constants.Protocol.HTTP,
        help="""Designates the Selenium Grid protocol to use.
                Default: http.""",
    )
    parser.addoption(
        "--server",
        action="store",
        dest="servername",
        default="localhost",
        help="""Designates the Selenium Grid server to use.
                Use "127.0.0.1" to connect to a localhost Grid.
                If unset or set to "localhost", Grid isn't used.
                Default: "localhost".""",
    )
    parser.addoption(
        "--port",
        action="store",
        dest="port",
        default="4444",
        help="""Designates the Selenium Grid port to use.
                Default: 4444. (If 443, protocol becomes "https")""",
    )
    parser.addoption(
        "--proxy",
        "--proxy-server",
        "--proxy-string",
        action="store",
        dest="proxy_string",
        default=None,
        help="""Designates the proxy server:port to use.
                Format: servername:port.  OR
                        username:password@servername:port  OR
                        A dict key from proxy_list.PROXY_LIST
                Default: None.""",
    )
    parser.addoption(
        "--proxy-bypass-list",
        "--proxy_bypass_list",
        action="store",
        dest="proxy_bypass_list",
        default=None,
        help="""Designates the hosts, domains, and/or IP addresses
                to bypass when using a proxy server with "--proxy".
                Format: A ";"-separated string.
                Example usage:
                    pytest
                        --proxy="username:password@servername:port"
                        --proxy-bypass-list="*.foo.com;github.com"
                    pytest
                        --proxy="servername:port"
                        --proxy-bypass-list="127.0.0.1:8080"
                Default: None.""",
    )
    parser.addoption(
        "--proxy-pac-url",
        "--pac-url",
        action="store",
        dest="proxy_pac_url",
        default=None,
        help="""Designates the proxy PAC URL to use.
                Format: A URL string  OR
                        A username:password@URL string
                Default: None.""",
    )
    parser.addoption(
        "--proxy-driver",
        "--proxy_driver",
        action="store_true",
        dest="proxy_driver",
        default=False,
        help="""If a driver download is needed for tests,
                uses proxy settings set via --proxy=PROXY.""",
    )
    parser.addoption(
        "--multi-proxy",
        "--multi_proxy",
        action="store_true",
        dest="multi_proxy",
        default=False,
        help="""If you need to run multi-threaded tests with
                multiple proxies that require authentication,
                set this to allow multiple configurations.""",
    )
    parser.addoption(
        "--agent",
        "--user-agent",
        "--user_agent",
        action="store",
        dest="user_agent",
        default=None,
        help="""Designates the User-Agent for the browser to use.
                Format: A string.
                Default: None.""",
    )
    parser.addoption(
        "--mobile",
        "--mobile-emulator",
        "--mobile_emulator",
        action="store_true",
        dest="mobile_emulator",
        default=False,
        help="""If this option is enabled, the mobile emulator
                will be used while running tests.""",
    )
    parser.addoption(
        "--metrics",
        "--device-metrics",
        "--device_metrics",
        action="store",
        dest="device_metrics",
        default=None,
        help="""Designates the three device metrics of the mobile
                emulator: CSS Width, CSS Height, and Pixel-Ratio.
                Format: A comma-separated string with the 3 values.
                Examples: "375,734,5" or "411,731,3" or "390,715,3"
                Default: None. (Will use default values if None)""",
    )
    parser.addoption(
        "--chromium_arg",
        "--chromium-arg",
        action="store",
        dest="chromium_arg",
        default=None,
        help="""Add a Chromium argument for Chrome/Edge browsers.
                Format: A comma-separated list of Chromium args.
                If an arg doesn't start with "--", that will be
                added to the beginning of the arg automatically.
                Default: None.""",
    )
    parser.addoption(
        "--firefox_arg",
        "--firefox-arg",
        action="store",
        dest="firefox_arg",
        default=None,
        help="""Add a Firefox argument for Firefox browser runs.
                Format: A comma-separated list of Firefox args.
                If an arg doesn't start with "--", that will be
                added to the beginning of the arg automatically.
                Default: None.""",
    )
    parser.addoption(
        "--firefox_pref",
        "--firefox-pref",
        action="store",
        dest="firefox_pref",
        default=None,
        help="""Set a Firefox preference:value combination.
                Format: A comma-separated list of pref:value items.
                Example usage:
                    --firefox-pref="browser.formfill.enable:True"
                    --firefox-pref="pdfjs.disabled:False"
                    --firefox-pref="abc.def.xyz:42,hello.world:text"
                Boolean and integer values to the right of the ":"
                will be automatically converted into proper format.
                If there's no ":" in the string, then True is used.
                Default: None.""",
    )
    parser.addoption(
        "--extension_zip",
        "--extension-zip",
        "--crx",
        action="store",
        dest="extension_zip",
        default=None,
        help="""Designates the Chrome Extension ZIP file to load.
                Format: A comma-separated list of .zip or .crx files
                containing the Chrome extensions to load.
                Default: None.""",
    )
    parser.addoption(
        "--extension_dir",
        "--extension-dir",
        action="store",
        dest="extension_dir",
        default=None,
        help="""Designates the Chrome Extension folder to load.
                Format: A directory containing the Chrome extension.
                (Can also be a comma-separated list of directories.)
                Default: None.""",
    )
    parser.addoption(
        "--disable_features",
        "--disable-features",
        action="store",
        dest="disable_features",
        default=None,
        help="""Disable Chromium features from Chrome/Edge browsers.
                Format: A comma-separated list of Chromium features.
                Default: None.""",
    )
    parser.addoption(
        "--binary_location",
        "--binary-location",
        action="store",
        dest="binary_location",
        default=None,
        help="""Sets the path of the Chromium browser binary to use.
                Uses the default location if not os.path.exists(PATH)""",
    )
    parser.addoption(
        "--driver_version",
        "--driver-version",
        action="store",
        dest="driver_version",
        default=None,
        help="""Setting this overrides the default driver version,
                which is set to match the detected browser version.
                Major version only. Example: "--driver-version=114"
                (Only chromedriver and uc_driver are affected.)""",
    )
    parser.addoption(
        "--pls",
        "--page_load_strategy",
        "--page-load-strategy",
        action="store",
        dest="page_load_strategy",
        type=str.lower,
        choices=(
            constants.PageLoadStrategy.NORMAL,
            constants.PageLoadStrategy.EAGER,
            constants.PageLoadStrategy.NONE,
        ),
        default=None,
        help="""This option sets Chrome's pageLoadStrategy.
                List of choices: "normal", "eager", "none".""",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        dest="headless",
        default=False,
        help="""Using this option activates headless mode,
                which is required on headless machines
                UNLESS using a virtual display with Xvfb.
                Default: False on Mac/Windows. True on Linux.""",
    )
    parser.addoption(
        "--headless2",
        action="store_true",
        dest="headless2",
        default=False,
        help="""This option activates the new headless mode,
                which supports Chromium extensions, and more,
                but is slower than the standard headless mode.""",
    )
    parser.addoption(
        "--headed",
        "--gui",
        action="store_true",
        dest="headed",
        default=False,
        help="""Using this makes Webdriver run web browsers with
                a GUI when running tests on Linux machines.
                (The default setting on Linux is headless.)
                (The default setting on Mac or Windows is headed.)""",
    )
    parser.addoption(
        "--xvfb",
        action="store_true",
        dest="xvfb",
        default=False,
        help="""Using this makes tests run headlessly using Xvfb
                instead of the browser's built-in headless mode.
                When using "--xvfb", the "--headless" option
                will no longer be enabled by default on Linux.
                Default: False. (Linux-ONLY!)""",
    )
    parser.addoption(
        "--locale_code",
        "--locale-code",
        "--locale",
        action="store",
        dest="locale_code",
        default=None,
        help="""Designates the Locale Code for the web browser.
                A Locale is a specific version of a spoken Language.
                The Locale alters visible text on supported websites.
                Default: None. (The web browser's default mode.)""",
    )
    parser.addoption(
        "--interval",
        action="store",
        dest="interval",
        default=None,
        help="""This globally overrides the default interval,
                (in seconds), of features that include autoplay
                functionality, such as tours and presentations.
                Overrides from methods take priority over this.
                (Headless Mode skips tours and presentations.)""",
    )
    parser.addoption(
        "--start_page",
        "--start-page",
        "--url",
        action="store",
        dest="start_page",
        default=None,
        help="""Designates the starting URL for the web browser
                when each test begins.
                Default: None.""",
    )
    parser.addoption(
        "--is_pytest",
        "--is-pytest",
        action="store_true",
        dest="is_pytest",
        default=True,
        help="""This is used by the BaseCase class to tell apart
                pytest runs from nosetest runs. (Automatic)""",
    )
    parser.addoption(
        "--all-scripts",
        "--all_scripts",
        action="store_true",
        dest="all_scripts",
        default=False,
        help="""Use this to run `PS()`, `DriverContext()` and
                `Driver()` scripts that are discovered during
                the pytest collection phase.""",
    )
    parser.addoption(
        "--time_limit",
        "--time-limit",
        "--timelimit",
        action="store",
        dest="time_limit",
        default=None,
        help="""Use this to set a time limit per test, in seconds.
                If a test runs beyond the limit, it fails.""",
    )
    parser.addoption(
        "--slow_mode",
        "--slow-mode",
        "--slowmo",
        "--slow",
        action="store_true",
        dest="slow_mode",
        default=False,
        help="""Using this slows down the automation.""",
    )
    parser.addoption(
        "--demo_mode",
        "--demo-mode",
        "--demo",
        action="store_true",
        dest="demo_mode",
        default=False,
        help="""Using this slows down the automation and lets you
                visually see what the tests are actually doing.""",
    )
    parser.addoption(
        "--demo_sleep",
        "--demo-sleep",
        action="store",
        dest="demo_sleep",
        default=None,
        help="""Setting this overrides the Demo Mode sleep
                time that happens after browser actions.""",
    )
    parser.addoption(
        "--highlights",
        action="store",
        dest="highlights",
        default=None,
        help="""Setting this overrides the default number of
                highlight animation loops to have per call.""",
    )
    parser.addoption(
        "--message_duration",
        "--message-duration",
        action="store",
        dest="message_duration",
        default=None,
        help="""Setting this overrides the default time that
                messenger notifications remain visible when
                reaching assert statements during Demo Mode.""",
    )
    parser.addoption(
        "--check_js",
        "--check-js",
        action="store_true",
        dest="js_checking_on",
        default=False,
        help="""The option to check for JavaScript errors after
                every page load.""",
    )
    parser.addoption(
        "--adblock",
        "--ad_block",
        "--ad-block",
        "--block_ads",
        "--block-ads",
        action="store_true",
        dest="ad_block_on",
        default=False,
        help="""Using this makes WebDriver block display ads
                that are defined in ad_block_list.AD_BLOCK_LIST.""",
    )
    parser.addoption(
        "--host_resolver_rules",
        "--host-resolver-rules",
        action="store",
        dest="host_resolver_rules",
        default=None,
        help="""Use this option to set "host-resolver-rules".
                This lets you re-map traffic from any domain.
                Eg. "MAP www.google-analytics.com 0.0.0.0".
                Eg. "MAP * ~NOTFOUND , EXCLUDE myproxy".
                Eg. "MAP * 0.0.0.0 , EXCLUDE 127.0.0.1".
                Eg. "MAP *.google.com myproxy".
                Find more examples on these pages:
                (https://www.electronjs.org/docs/
                 latest/api/command-line-switches)
                (https://www.chromium.org/developers/
                 design-documents/network-stack/socks-proxy/)
                Use comma-separation for multiple host rules.""",
    )
    parser.addoption(
        "--block_images",
        "--block-images",
        action="store_true",
        dest="block_images",
        default=False,
        help="""Using this makes WebDriver block images from
                loading on web pages during tests.""",
    )
    parser.addoption(
        "--do_not_track",
        "--do-not-track",
        action="store_true",
        dest="do_not_track",
        default=False,
        help="""Indicate to websites that you don't want to be
                tracked. The browser will send an extra HTTP
                header each time it requests a web page.
                https://support.google.com/chrome/answer/2790761""",
    )
    parser.addoption(
        "--verify_delay",
        "--verify-delay",
        action="store",
        dest="verify_delay",
        default=None,
        help="""Setting this overrides the default wait time
                before each MasterQA verification pop-up.""",
    )
    parser.addoption(
        "--esc-end",
        "--esc_end",
        "--ee",
        action="store_true",
        dest="esc_end",
        default=False,
        help="""End the current test early via the ESC key.
                The test will be marked as skipped.""",
    )
    parser.addoption(
        "--recorder",
        "--record",
        "--rec",
        "--codegen",
        action="store_true",
        dest="recorder_mode",
        default=False,
        help="""Using this enables the PythonSelenium Recorder,
                which records browser actions for converting
                into PythonSelenium scripts.""",
    )
    parser.addoption(
        "--rec-behave",
        "--rec-gherkin",
        action="store_true",
        dest="rec_behave",
        default=False,
        help="""Not only enables the PythonSelenium Recorder,
                but also saves recorded actions into the
                behave-gerkin format, which includes a
                feature file, an imported steps file,
                and the environment.py file.""",
    )
    parser.addoption(
        "--rec-sleep",
        "--record-sleep",
        action="store_true",
        dest="record_sleep",
        default=False,
        help="""If Recorder Mode is enabled,
                records sleep(seconds) calls.""",
    )
    parser.addoption(
        "--rec-print",
        action="store_true",
        dest="rec_print",
        default=False,
        help="""If Recorder Mode is enabled,
                prints output after tests end.""",
    )
    parser.addoption(
        "--disable_js",
        "--disable-js",
        action="store_true",
        dest="disable_js",
        default=False,
        help="""The option to disable JavaScript on web pages.
                Warning: Most web pages will stop working!""",
    )
    parser.addoption(
        "--disable_csp",
        "--disable-csp",
        "--no_csp",
        "--no-csp",
        "--dcsp",
        action="store_true",
        dest="disable_csp",
        default=False,
        help="""Using this disables the Content Security Policy of
                websites, which may interfere with some features of
                PythonSelenium, such as loading custom JavaScript
                libraries for various testing actions.
                Setting this to True (--disable-csp) overrides the
                value set in pythonselenium/config/settings.py""",
    )
    parser.addoption(
        "--disable_ws",
        "--disable-ws",
        "--disable-web-security",
        action="store_true",
        dest="disable_ws",
        default=False,
        help="""Using this disables the "Web Security" feature of
                Chrome and Chromium-based browsers such as Edge.""",
    )
    parser.addoption(
        "--enable_ws",
        "--enable-ws",
        "--enable-web-security",
        action="store_true",
        dest="enable_ws",
        default=False,
        help="""Using this enables the "Web Security" feature of
                Chrome and Chromium-based browsers such as Edge.""",
    )
    parser.addoption(
        "--enable_sync",
        "--enable-sync",
        action="store_true",
        dest="enable_sync",
        default=False,
        help="""Using this enables the "Chrome Sync" feature.""",
    )
    parser.addoption(
        "--use_auto_ext",
        "--use-auto-ext",
        "--auto-ext",
        action="store_true",
        dest="use_auto_ext",
        default=False,
        help="""(DEPRECATED) - Enable the automation extension.
                It's not required, but some commands & advanced
                features may need it.""",
    )
    parser.addoption(
        "--undetected",
        "--undetectable",
        "--uc",  # undetected-chromedriver
        action="store_true",
        dest="undetectable",
        default=False,
        help="""Using this option makes chromedriver undetectable
                to websites that use anti-bot services to block
                automation tools from navigating them freely.""",
    )
    parser.addoption(
        "--uc_cdp_events",
        "--uc-cdp-events",
        "--uc-cdp",  # For capturing CDP events during UC Mode
        action="store_true",
        dest="uc_cdp_events",
        default=None,
        help="""Captures CDP events during Undetectable Mode runs.
                Then you can add a listener to perform actions on
                received data, such as printing it to the console:
                    from pprint import pformat
                    self.driver.add_cdp_listener(
                        "*", lambda data: print(pformat(data))
                    )
                    self.open(URL)""",
    )
    parser.addoption(
        "--uc_subprocess",
        "--uc-subprocess",
        "--uc-sub",  # undetected-chromedriver subprocess mode
        action="store_true",
        dest="uc_subprocess",
        default=None,
        help="""(DEPRECATED) - (UC Mode always uses this now.)
                Use undetectable-chromedriver as a subprocess,
                which can help avoid issues that might result.""",
    )
    parser.addoption(
        "--no_sandbox",
        "--no-sandbox",
        action="store_true",
        dest="no_sandbox",
        default=False,
        help="""(DEPRECATED) - "--no-sandbox" is always used now.
                Using this enables the "No Sandbox" feature.
                (This setting is now always enabled by default.)""",
    )
    parser.addoption(
        "--disable_gpu",
        "--disable-gpu",
        action="store_true",
        dest="disable_gpu",
        default=False,
        help="""(DEPRECATED) - GPU is disabled if no swiftshader.
                Using this enables the "Disable GPU" feature.
                (GPU is disabled by default if swiftshader off.)""",
    )
    parser.addoption(
        "--log_cdp",
        "--log-cdp",
        "--log_cdp_events",
        "--log-cdp-events",
        action="store_true",
        dest="log_cdp_events",
        default=None,
        help="""Capture CDP events. Then you can print them.
                Eg. print(driver.get_log("performance"))""",
    )
    parser.addoption(
        "--remote_debug",
        "--remote-debug",
        "--remote-debugger",
        "--remote_debugger",
        action="store_true",
        dest="remote_debug",
        default=False,
        help="""This syncs the browser to Chromium's remote debugger.
                To access the remote debugging interface, go to:
                chrome://inspect/#devices while tests are running.
                The previous URL was at: http://localhost:9222/
                Info: chromedevtools.github.io/devtools-protocol/""",
    )
    parser.addoption(
        "--final-debug",
        "--final-trace",
        "--fdebug",
        "--ftrace",
        action="store_true",
        dest="final_debug",
        default=False,
        help="""Enter Debug Mode at the end of each test.
                To enter Debug Mode only on failures, use "--pdb".
                If using both "--final-debug" and "--pdb" together,
                then Debug Mode will activate twice on failures.""",
    )
    parser.addoption(
        "--dashboard",
        action="store_true",
        dest="dashboard",
        default=False,
        help="""Using this enables the PythonSelenium Dashboard.
                To access the PythonSelenium Dashboard interface,
                open the dashboard.html file located in the same
                folder that the pytest command was run from.""",
    )
    parser.addoption(
        "--dash_title",
        "--dash-title",
        dest="dash_title",
        default=None,
        help="Set the title shown for the generated dashboard.",
    )
    parser.addoption(
        "--enable_3d_apis",
        "--enable-3d-apis",
        action="store_true",
        dest="enable_3d_apis",
        default=False,
        help="""Using this enables WebGL and 3D APIs.""",
    )
    parser.addoption(
        "--swiftshader",
        action="store_true",
        dest="swiftshader",
        default=False,
        help="""Using this enables the "--use-gl=swiftshader"
                feature when running tests on Chrome.""",
    )
    parser.addoption(
        "--incognito",
        "--incognito_mode",
        "--incognito-mode",
        action="store_true",
        dest="incognito",
        default=False,
        help="""Using this enables Chrome's Incognito mode.""",
    )
    parser.addoption(
        "--guest",
        "--guest_mode",
        "--guest-mode",
        action="store_true",
        dest="guest_mode",
        default=False,
        help="""Using this enables Chrome's Guest mode.""",
    )
    parser.addoption(
        "--dark",
        "--dark_mode",
        "--dark-mode",
        action="store_true",
        dest="dark_mode",
        default=False,
        help="""Using this enables Chrome's Dark mode.""",
    )
    parser.addoption(
        "--devtools",
        "--open_devtools",
        "--open-devtools",
        action="store_true",
        dest="devtools",
        default=False,
        help="""Using this opens Chrome's DevTools.""",
    )
    parser.addoption(
        "--rs",
        "--reuse_session",
        "--reuse-session",
        action="store_true",
        dest="reuse_session",
        default=False,
        help="""The option to reuse the selenium browser window
                session for all tests.""",
    )
    parser.addoption(
        "--rcs",
        "--reuse_class_session",
        "--reuse-class-session",
        action="store_true",
        dest="reuse_class_session",
        default=False,
        help="""The option to reuse the selenium browser window
                session for all tests within the same class.""",
    )
    parser.addoption(
        "--crumbs",
        action="store_true",
        dest="crumbs",
        default=False,
        help="""The option to delete all cookies between tests
                that reuse the same browser session. This option
                is only useful if using "--reuse-session"/"--rs"
                or "--reuse-class-session"/"--rcs" because tests
                use a new clean browser if not reusing sessions.""",
    )
    parser.addoption(
        "--disable-beforeunload",
        "--disable_beforeunload",
        action="store_true",
        dest="_disable_beforeunload",
        default=False,
        help="""The option to disable the "beforeunload" event
                on Chromium browsers (Chrome or Edge).
                This is already the default Firefox option.""",
    )
    parser.addoption(
        "--window-size",
        "--window_size",
        action="store",
        dest="window_size",
        default=None,
        help="""The option to set the default window "width,height".
                Format: A comma-separated string with the 2 values.
                Example: "1200,800"
                Default: None. (Will use default values if None)""",
    )
    parser.addoption(
        "--maximize_window",
        "--maximize-window",
        "--maximize",
        "--fullscreen",
        action="store_true",
        dest="maximize_option",
        default=False,
        help="""The option to start with a maximized browser window.
                (Overrides the "window-size" option if used.)""",
    )
    parser.addoption(
        "--screenshot",
        "--save_screenshot",
        "--save-screenshot",
        "--ss",
        action="store_true",
        dest="save_screenshot",
        default=False,
        help="""Save a screenshot at the end of every test.
                By default, this is only done for failures.
                Will be saved in the "latest_logs/" folder.""",
    )
    parser.addoption(
        "--no-screenshot",
        "--no_screenshot",
        "--ns",
        action="store_true",
        dest="no_screenshot",
        default=False,
        help="""No screenshots saved unless tests directly ask it.
                This changes default behavior where screenshots are
                saved for test failures and pytest-html reports.""",
    )
    parser.addoption(
        "--visual_baseline",
        "--visual-baseline",
        action="store_true",
        dest="visual_baseline",
        default=False,
        help="""Setting this resets the visual baseline for
                Automated Visual Testing with PythonSelenium.
                When a test calls self.check_window(), it will
                rebuild its files in the visual_baseline folder.""",
    )
    parser.addoption(
        "--wire",
        action="store_true",
        dest="use_wire",
        default=False,
        help="""Use selenium-wire's webdriver for selenium webdriver.""",
    )
    parser.addoption(
        "--external_pdf",
        "--external-pdf",
        action="store_true",
        dest="external_pdf",
        default=False,
        help="""This option sets the following on Chromium:
                "plugins.always_open_pdf_externally": True,
                which causes opened PDF URLs to download immediately,
                instead of being displayed in the browser window.""",
    )
    parser.addoption(
        "--timeout_multiplier",
        "--timeout-multiplier",
        action="store",
        dest="timeout_multiplier",
        default=None,
        help="""Setting this overrides the default timeout
                by the multiplier when waiting for page elements.
                Unused when tests override the default value.""",
    )
    parser.addoption(
        "--lfp",
        "--list-fail-page",
        "--list-fail-pages",
        action="store_true",
        dest="fail_page",
        default=False,
        help="""(For debugging) After each failing test, list the URL
                where the failure occurred.
                Useful when you don't have access to the latest_logs/
                folder, such as when running tests in GitHub Actions.""",
    )

    arg_join = " ".join(sys_argv)
    ps_config._browser_shortcut = None

    # PythonSelenium does not support pytest-timeout due to hanging browsers.
    for arg in sys_argv:
        if "--timeout=" in arg:
            raise Exception("\n  Don't use --timeout=s from pytest-timeout! " "\n  It's not thread-safe for WebDriver processes! " "\n  Use --time-limit=s from PythonSelenium instead!\n")

    # Dashboard Mode does not support tests using forked subprocesses.
    if "--forked" in sys_argv and "--dashboard" in sys_argv:
        raise Exception("\n  Dashboard Mode does NOT support forked subprocesses!" '\n  (*** DO NOT combine "--forked" with "--dashboard"! ***)\n')

    # Reuse-Session Mode does not support tests using forked subprocesses.
    if "--forked" in sys_argv and ("--rs" in sys_argv or "--reuse-session" in sys_argv):
        raise Exception("\n  Reuse-Session Mode does NOT support forked subprocesses!" '\n  (DO NOT combine "--forked" with "--rs"/"--reuse-session"!)\n')

    # Recorder Mode does not support multi-threaded / multi-process runs.
    if "--recorder" in sys_argv or "--record" in sys_argv or "--rec" in sys_argv:
        if ("-n" in sys_argv) or (" -n=" in arg_join) or ("-c" in sys_argv):
            raise Exception("\n  Recorder Mode does NOT support multi-process mode (-n)!" '\n  (DO NOT combine "--recorder" with "-n NUM_PROCESSES"!)\n')

    using_recorder = False
    if "--recorder" in sys_argv or "--record" in sys_argv or "--rec" in sys_argv:
        using_recorder = True

    # As a shortcut, you can use "--edge" instead of "--browser=edge", etc,
    # but you can only specify one default browser for tests. (Default: chrome)
    browser_changes = 0
    browser_set = None
    browser_text = None
    browser_list = []
    if "--browser=chrome" in sys_argv or "--browser chrome" in sys_argv:
        browser_changes += 1
        browser_set = "chrome"
        browser_list.append("--browser=chrome")
    if "--browser=edge" in sys_argv or "--browser edge" in sys_argv:
        browser_changes += 1
        browser_set = "edge"
        browser_list.append("--browser=edge")
    if "--browser=firefox" in sys_argv or "--browser firefox" in sys_argv:
        browser_changes += 1
        browser_set = "firefox"
        browser_list.append("--browser=firefox")
    if "--browser=safari" in sys_argv or "--browser safari" in sys_argv:
        browser_changes += 1
        browser_set = "safari"
        browser_list.append("--browser=safari")
    if "--browser=ie" in sys_argv or "--browser ie" in sys_argv:
        browser_changes += 1
        browser_set = "ie"
        browser_list.append("--browser=ie")
    if "--browser=remote" in sys_argv or "--browser remote" in sys_argv:
        browser_changes += 1
        browser_set = "remote"
        browser_list.append("--browser=remote")
    browser_text = browser_set
    if "--chrome" in sys_argv and not browser_set == "chrome":
        browser_changes += 1
        browser_text = "chrome"
        ps_config._browser_shortcut = "chrome"
        browser_list.append("--chrome")
    if "--edge" in sys_argv and not browser_set == "edge":
        browser_changes += 1
        browser_text = "edge"
        ps_config._browser_shortcut = "edge"
        browser_list.append("--edge")
    if "--firefox" in sys_argv and not browser_set == "firefox":
        browser_changes += 1
        browser_text = "firefox"
        ps_config._browser_shortcut = "firefox"
        browser_list.append("--firefox")
    if "--ie" in sys_argv and not browser_set == "ie":
        browser_changes += 1
        browser_text = "ie"
        ps_config._browser_shortcut = "ie"
        browser_list.append("--ie")
    if "--safari" in sys_argv and not browser_set == "safari":
        browser_changes += 1
        browser_text = "safari"
        ps_config._browser_shortcut = "safari"
        browser_list.append("--safari")
    if browser_changes > 1:
        message = "\n  TOO MANY browser types were entered!"
        message += "\n  There were %s found:\n  >  %s" % (
            browser_changes,
            ", ".join(browser_list),
        )
        message += "\n  ONLY ONE default browser is allowed!"
        message += "\n  Select a single browser & try again!\n"
        raise Exception(message)
    if using_recorder and browser_changes == 1 and browser_text not in ["chrome", "edge"]:
        message = "\n  Recorder Mode ONLY supports Chrome and Edge!" '\n  (Your browser choice was: "%s")\n' % browser_list[0]
        raise Exception(message)
    undetectable = False
    if "--undetected" in sys_argv or "--undetectable" in sys_argv or "--uc" in sys_argv or "--uc-cdp-events" in sys_argv or "--uc_cdp_events" in sys_argv or "--uc-cdp" in sys_argv or "--uc-subprocess" in sys_argv or "--uc_subprocess" in sys_argv or "--uc-sub" in sys_argv:
        undetectable = True
    if browser_changes == 1 and browser_text not in ["chrome"] and undetectable:
        message = "\n  Undetected-Chromedriver Mode ONLY supports Chrome!" '\n  ("--uc" / "--undetected" / "--undetectable")' '\n  (Your browser choice was: "%s")\n' % browser_list[0]
        raise Exception(message)
    if undetectable and "--wire" in sys_argv:
        raise Exception("\n  PythonSelenium doesn't support mixing --uc with --wire mode!" "\n  If you need both, override get_new_driver() from BaseCase")


def pytest_configure(config):
    """This runs after command-line options have been parsed."""
    ps_config.item_count = 0
    ps_config.item_count_passed = 0
    ps_config.item_count_failed = 0
    ps_config.item_count_skipped = 0
    ps_config.item_count_untested = 0
    ps_config.is_pytest = True
    ps_config.is_behave = False
    ps_config.is_nosetest = False
    ps_config.is_context_manager = False
    ps_config.pytest_config = config
    ps_config.browser = config.getoption("browser")
    if ps_config._browser_shortcut:
        ps_config.browser = ps_config._browser_shortcut
    ps_config.account = config.getoption("account")
    ps_config.data = config.getoption("data")
    ps_config.var1 = config.getoption("var1")
    ps_config.var2 = config.getoption("var2")
    ps_config.var3 = config.getoption("var3")
    ps_config.variables = config.getoption("variables")
    ps_config.environment = config.getoption("environment")
    ps_config.with_selenium = config.getoption("with_selenium")
    ps_config.user_agent = config.getoption("user_agent")
    ps_config.mobile_emulator = config.getoption("mobile_emulator")
    ps_config.device_metrics = config.getoption("device_metrics")
    ps_config.headless = config.getoption("headless")
    ps_config.headless2 = config.getoption("headless2")
    if ps_config.headless2 and ps_config.browser == "firefox":
        ps_config.headless2 = False  # Only for Chromium browsers
        ps_config.headless = True  # Firefox has regular headless
    elif ps_config.browser not in ["chrome", "edge"]:
        ps_config.headless2 = False  # Only for Chromium browsers
    ps_config.headed = config.getoption("headed")
    ps_config.xvfb = config.getoption("xvfb")
    ps_config.locale_code = config.getoption("locale_code")
    ps_config.interval = config.getoption("interval")
    ps_config.start_page = config.getoption("start_page")
    ps_config.chromium_arg = config.getoption("chromium_arg")
    ps_config.firefox_arg = config.getoption("firefox_arg")
    ps_config.firefox_pref = config.getoption("firefox_pref")
    ps_config.extension_zip = config.getoption("extension_zip")
    ps_config.extension_dir = config.getoption("extension_dir")
    ps_config.disable_features = config.getoption("disable_features")
    ps_config.binary_location = config.getoption("binary_location")
    ps_config.driver_version = config.getoption("driver_version")
    ps_config.page_load_strategy = config.getoption("page_load_strategy")
    ps_config.with_testing_base = config.getoption("with_testing_base")
    ps_config.with_db_reporting = config.getoption("with_db_reporting")
    ps_config.with_s3_logging = config.getoption("with_s3_logging")
    ps_config.with_screen_shots = config.getoption("with_screen_shots")
    ps_config.with_basic_test_info = config.getoption("with_basic_test_info")
    ps_config.with_page_source = config.getoption("with_page_source")
    ps_config.protocol = config.getoption("protocol")
    ps_config.servername = config.getoption("servername")
    ps_config.port = config.getoption("port")
    if ps_config.servername != "localhost":
        # Using Selenium Grid
        # (Set --server="127.0.0.1" for localhost Grid)
        if str(ps_config.port) == "443":
            ps_config.protocol = "https"
    ps_config.proxy_string = config.getoption("proxy_string")
    ps_config.proxy_bypass_list = config.getoption("proxy_bypass_list")
    ps_config.proxy_pac_url = config.getoption("proxy_pac_url")
    ps_config.proxy_driver = config.getoption("proxy_driver")
    ps_config.multi_proxy = config.getoption("multi_proxy")
    ps_config.cap_file = config.getoption("cap_file")
    ps_config.cap_string = config.getoption("cap_string")
    ps_config.settings_file = config.getoption("settings_file")
    ps_config.user_data_dir = config.getoption("user_data_dir")
    ps_config.database_env = config.getoption("database_env")
    ps_config.log_path = constants.Logs.LATEST + "/"
    ps_config.archive_logs = config.getoption("archive_logs")
    if config.getoption("archive_downloads"):
        settings.ARCHIVE_EXISTING_DOWNLOADS = True
    if config.getoption("skip_js_waits"):
        settings.SKIP_JS_WAITS = True
    ps_config.all_scripts = config.getoption("all_scripts")
    ps_config._time_limit = config.getoption("time_limit")
    ps_config.time_limit = config.getoption("time_limit")
    ps_config.slow_mode = config.getoption("slow_mode")
    ps_config.demo_mode = config.getoption("demo_mode")
    ps_config.demo_sleep = config.getoption("demo_sleep")
    ps_config.highlights = config.getoption("highlights")
    ps_config.message_duration = config.getoption("message_duration")
    ps_config.js_checking_on = config.getoption("js_checking_on")
    ps_config.ad_block_on = config.getoption("ad_block_on")
    ps_config.host_resolver_rules = config.getoption("host_resolver_rules")
    ps_config.block_images = config.getoption("block_images")
    ps_config.do_not_track = config.getoption("do_not_track")
    ps_config.verify_delay = config.getoption("verify_delay")
    ps_config.esc_end = config.getoption("esc_end")
    ps_config.recorder_mode = config.getoption("recorder_mode")
    ps_config.recorder_ext = config.getoption("recorder_mode")  # Again
    ps_config.rec_behave = config.getoption("rec_behave")
    ps_config.rec_print = config.getoption("rec_print")
    ps_config.record_sleep = config.getoption("record_sleep")
    if ps_config.rec_print and not ps_config.recorder_mode:
        ps_config.recorder_mode = True
        ps_config.recorder_ext = True
    elif ps_config.rec_behave and not ps_config.recorder_mode:
        ps_config.recorder_mode = True
        ps_config.recorder_ext = True
    elif ps_config.record_sleep and not ps_config.recorder_mode:
        ps_config.recorder_mode = True
        ps_config.recorder_ext = True
    ps_config.disable_js = config.getoption("disable_js")
    ps_config.disable_csp = config.getoption("disable_csp")
    ps_config.disable_ws = config.getoption("disable_ws")
    ps_config.enable_ws = config.getoption("enable_ws")
    if not ps_config.disable_ws:
        ps_config.enable_ws = True
    ps_config.enable_sync = config.getoption("enable_sync")
    ps_config.use_auto_ext = config.getoption("use_auto_ext")
    ps_config.undetectable = config.getoption("undetectable")
    ps_config.uc_cdp_events = config.getoption("uc_cdp_events")
    if ps_config.uc_cdp_events and not ps_config.undetectable:
        ps_config.undetectable = True
    ps_config.uc_subprocess = config.getoption("uc_subprocess")
    if ps_config.uc_subprocess and not ps_config.undetectable:
        ps_config.undetectable = True
    ps_config.no_sandbox = config.getoption("no_sandbox")
    ps_config.disable_gpu = config.getoption("disable_gpu")
    ps_config.log_cdp_events = config.getoption("log_cdp_events")
    ps_config.remote_debug = config.getoption("remote_debug")
    ps_config.final_debug = config.getoption("final_debug")
    ps_config.dashboard = config.getoption("dashboard")
    ps_config.dash_title = config.getoption("dash_title")
    ps_config.enable_3d_apis = config.getoption("enable_3d_apis")
    ps_config.swiftshader = config.getoption("swiftshader")
    ps_config.incognito = config.getoption("incognito")
    ps_config.guest_mode = config.getoption("guest_mode")
    ps_config.dark_mode = config.getoption("dark_mode")
    ps_config.devtools = config.getoption("devtools")
    ps_config.reuse_session = config.getoption("reuse_session")
    ps_config.reuse_class_session = config.getoption("reuse_class_session")
    if ps_config.reuse_class_session:
        ps_config.reuse_session = True
    ps_config.shared_driver = None  # The default driver for session reuse
    ps_config.crumbs = config.getoption("crumbs")
    ps_config._disable_beforeunload = config.getoption("_disable_beforeunload")
    ps_config.window_size = config.getoption("window_size")
    ps_config.maximize_option = config.getoption("maximize_option")
    ps_config.save_screenshot = config.getoption("save_screenshot")
    ps_config.no_screenshot = config.getoption("no_screenshot")
    ps_config.visual_baseline = config.getoption("visual_baseline")
    ps_config.use_wire = config.getoption("use_wire")
    ps_config.external_pdf = config.getoption("external_pdf")
    ps_config.timeout_multiplier = config.getoption("timeout_multiplier")
    ps_config.list_fp = config.getoption("fail_page")
    ps_config._is_timeout_changed = False
    ps_config._has_logs = False
    ps_config._fail_page = None
    ps_config._SMALL_TIMEOUT = settings.SMALL_TIMEOUT
    ps_config._LARGE_TIMEOUT = settings.LARGE_TIMEOUT
    ps_config.pytest_html_report = config.getoption("htmlpath")  # --html=FILE
    ps_config._ps_class = None  # (Used with the ps fixture for "--rcs")
    ps_config._ps_node = {}  # ps node dictionary (Used with the ps fixture)
    # Dashboard-specific variables
    ps_config._results = {}  # PySel Dashboard test results
    ps_config._duration = {}  # PySel Dashboard test duration
    ps_config._display_id = {}  # PySel Dashboard display ID
    ps_config._d_t_log_path = {}  # PySel Dashboard test log path
    ps_config._dash_html = None  # PySel Dashboard HTML copy
    ps_config._test_id = None  # PySel Dashboard test id
    ps_config._latest_display_id = None  # The latest PySel display id
    ps_config._dashboard_initialized = False  # Becomes True after init
    ps_config._has_exception = False  # This becomes True if any test fails
    ps_config._multithreaded = False  # This becomes True if multithreading
    ps_config._only_unittest = True  # If any test uses BaseCase, becomes False
    ps_config._pysel_detected = False  # Becomes True during PythonSelenium tests
    ps_config._extra_dash_entries = []  # Dashboard entries for non-PySel tests
    ps_config._using_html_report = False  # Becomes True when using html report
    ps_config._dash_is_html_report = False  # Dashboard becomes the html report
    ps_config._saved_dashboard_pie = None  # Copy of pie chart for html report
    ps_config._dash_final_summary = None  # Dash status to add to html report
    ps_config._html_report_name = None  # The name of the pytest html report

    arg_join = " ".join(sys_argv)
    if "-n" in sys_argv or " -n=" in arg_join or " -n" in arg_join or "-c" in sys_argv or ("addopts" in config.inicfg.keys() and ("-n=" in config.inicfg["addopts"] or "-n " in config.inicfg["addopts"] or "-n" in config.inicfg["addopts"])):
        ps_config._multithreaded = True
    if "--html" in sys_argv or " --html=" in arg_join or ("addopts" in config.inicfg.keys() and ("--html=" in config.inicfg["addopts"] or "--html " in config.inicfg["addopts"])):
        ps_config._using_html_report = True
        ps_config._html_report_name = config.getoption("htmlpath")
        if ps_config.dashboard:
            if ps_config._html_report_name == "dashboard.html":
                ps_config._dash_is_html_report = True

    # Recorder Mode does not support multi-threaded / multi-process runs.
    if ps_config.recorder_mode and ps_config._multithreaded:
        # At this point, the user likely put a "-n NUM" in the pytest.ini file.
        # Since raising an exception in pytest_configure raises INTERNALERROR,
        # print a message here instead and cancel Recorder Mode.
        print("\n  Recorder Mode does NOT support multi-process mode (-n)!" '\n  (DO NOT combine "--recorder" with "-n NUM_PROCESSES"!)' "\n  (The Recorder WILL BE DISABLED during this run!)\n")
        ps_config.recorder_mode = False
        ps_config.recorder_ext = False

    if ps_config.xvfb and "linux" not in sys.platform:
        # The Xvfb virtual display server is for Linux OS Only!
        ps_config.xvfb = False
    if "linux" in sys.platform and not ps_config.headed and not ps_config.headless and not ps_config.headless2 and not ps_config.xvfb:
        if not ps_config.undetectable:
            print("(Linux uses --headless by default. " "To override, use --headed / --gui. " "For Xvfb mode instead, use --xvfb. " "Or you can hide this info by using " "--headless / --headless2 / --uc.)")
            ps_config.headless = True
        else:
            ps_config.xvfb = True

    # Recorder Mode can still optimize scripts in --headless2 mode.
    if ps_config.recorder_mode and ps_config.headless:
        ps_config.headless = False
        ps_config.headless2 = True

    if not ps_config.headless and not ps_config.headless2:
        ps_config.headed = True

    if config.getoption("use_chrome"):
        ps_config.browser = "chrome"
    elif config.getoption("use_edge"):
        ps_config.browser = "edge"
    elif config.getoption("use_firefox"):
        ps_config.browser = "firefox"
    elif config.getoption("use_ie"):
        ps_config.browser = "ie"
    elif config.getoption("use_safari"):
        ps_config.browser = "safari"
    else:
        pass  # Use the browser specified by "--browser=BROWSER"

    if ps_config.browser == "safari" and ps_config.headless:
        ps_config.headless = False  # Safari doesn't support headless mode

    if ps_config.dash_title:
        constants.Dashboard.TITLE = ps_config.dash_title.replace("_", " ")

    if ps_config.save_screenshot and ps_config.no_screenshot:
        ps_config.save_screenshot = False  # "no_screenshot" has priority

    if "-v" in sys_argv and not ps_config._multithreaded or (hasattr(config, "invocation_params") and "-v" in config.invocation_params.args and ("-n=1" in config.invocation_params.args or "-n1" in config.invocation_params.args or "-n 1" in " ".join(config.invocation_params.args))):
        ps_config.list_fp = True  # List the fail pages in console output

    if ps_config._multithreaded and "--co" not in sys_argv and "--collect-only" not in sys_argv:
        from pythonselenium.core import download_helper, proxy_helper

        log_helper.log_folder_setup(constants.Logs.LATEST + "/", ps_config.archive_logs)
        download_helper.reset_downloads_folder()
        proxy_helper.remove_proxy_zip_if_present()


def pytest_sessionstart(session):
    pass


def _get_test_ids_(the_item):
    test_id = the_item.nodeid
    if not test_id:
        test_id = "unidentified_TestCase"
    display_id = test_id
    r"""
    # Now using the nodeid for both the test_id and display_id.
    # (This only impacts tests using The Dashboard.)
    # If there are any issues, we'll revert back to the old code.
    test_id = the_item.nodeid.split("/")[-1].replace(" ", "_")
    if "[" in test_id:
        test_id_intro = test_id.split("[")[0]
        parameter = test_id.split("[")[1]
        parameter = re.sub(re.compile(r"\W"), "", parameter)
        test_id = test_id_intro + "__" + parameter
    display_id = test_id
    test_id = test_id.replace("/", ".").replace("\\", ".")
    test_id = test_id.replace("::", ".").replace(".py", "")
    """
    return test_id, display_id


def _create_dashboard_assets_():
    import codecs

    from pythonselenium.core.style_sheet import get_pytest_style
    from pythonselenium.js_code.live_js import live_js

    abs_path = os.path.abspath(".")
    assets_folder = os.path.join(abs_path, "assets")
    if not os.path.exists(assets_folder):
        try:
            os.makedirs(assets_folder, exist_ok=True)
        except Exception:
            pass
    pytest_style_css = os.path.join(assets_folder, "pytest_style.css")
    add_pytest_style_css = True
    if os.path.exists(pytest_style_css):
        existing_pytest_style = None
        with open(pytest_style_css, "r") as f:
            existing_pytest_style = f.read()
        if existing_pytest_style == get_pytest_style():
            add_pytest_style_css = False
    if add_pytest_style_css:
        out_file = codecs.open(pytest_style_css, "w+", encoding="utf-8")
        out_file.writelines(get_pytest_style())
        out_file.close()
    live_js_file = os.path.join(assets_folder, "live.js")
    add_live_js_file = True
    if os.path.exists(live_js_file):
        existing_live_js = None
        with open(live_js_file, "r") as f:
            existing_live_js = f.read()
        if existing_live_js == live_js:
            add_live_js_file = False
    if add_live_js_file:
        out_file = codecs.open(live_js_file, "w+", encoding="utf-8")
        out_file.writelines(live_js)
        out_file.close()


def pytest_itemcollected(item):
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    ps_config.item_count += 1
    if ps_config.dashboard:
        test_id, display_id = _get_test_ids_(item)
        ps_config._results[test_id] = "Untested"
        ps_config._duration[test_id] = "-"
        ps_config._display_id[test_id] = display_id
        ps_config._d_t_log_path[test_id] = None


def pytest_deselected(items):
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    if ps_config.dashboard:
        ps_config.item_count -= len(items)
        for item in items:
            test_id, display_id = _get_test_ids_(item)
            if test_id in ps_config._results.keys():
                ps_config._results.pop(test_id)


def pytest_collection_finish(session):
    """This runs after item collection is finalized.
    https://docs.pytest.org/en/stable/reference.html"""
    ps_config._context_of_runner = False  # Context Manager Compatibility
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    if len(session.items) > 0 and not ps_config._multithreaded:
        from pythonselenium.core import download_helper, proxy_helper

        log_helper.log_folder_setup(constants.Logs.LATEST + "/", ps_config.archive_logs)
        download_helper.reset_downloads_folder()
        proxy_helper.remove_proxy_zip_if_present()
    if ps_config.dashboard and len(session.items) > 0:
        _create_dashboard_assets_()
        # Print the Dashboard path if at least one test runs.
        ps_config.item_count_untested = ps_config.item_count
        dash_path = os.path.join(os.getcwd(), "dashboard.html")
        dash_url = "file://" + dash_path.replace("\\", "/")
        star_len = len("Dashboard: ") + len(dash_url)
        try:
            terminal_size = os.get_terminal_size().columns
            if terminal_size > 30 and star_len > terminal_size:
                star_len = terminal_size
        except Exception:
            pass
        stars = "*" * star_len
        c1 = ""
        cr = ""
        if "linux" not in sys.platform:
            if is_windows and hasattr(colorama, "just_fix_windows_console"):
                colorama.just_fix_windows_console()
            else:
                colorama.init(autoreset=True)
            c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
            cr = colorama.Style.RESET_ALL
        if ps_config._multithreaded:
            if hasattr(session.config, "workerinput") and session.config.workerinput["workerid"] == "gw0":
                sys.stderr.write("\nDashboard: %s%s%s\n%s\n" % (c1, dash_url, cr, stars))
        else:
            print("Dashboard: %s%s%s\n%s" % (c1, dash_url, cr, stars))


def pytest_runtest_setup(item):
    """This runs before every test with pytest."""
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    if ps_config.dashboard:
        ps_config._pysel_detected = False
        ps_config._pdb_failure = False
    ps_config._fail_page = None
    test_id, display_id = _get_test_ids_(item)
    ps_config._test_id = test_id
    ps_config._latest_display_id = display_id


def pytest_runtest_teardown(item):
    """This runs after every test with pytest.
    Make sure that webdriver and headless displays have exited.
    (Has zero effect on tests using --reuse-session / --rs)"""
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    try:
        if hasattr(item, "_testcase") or hasattr(ps_config, "_ps_pdb_driver"):
            if hasattr(item, "_testcase"):
                self = item._testcase
                try:
                    if hasattr(self, "driver") and self.driver and "--pdb" not in sys_argv:
                        if not (is_windows or self.driver.service.process):
                            self.driver.quit()
                except Exception:
                    pass
            elif hasattr(ps_config, "_ps_pdb_driver") and ps_config._ps_pdb_driver:
                try:
                    if not is_windows or ps_config._ps_pdb_driver.service.process:
                        ps_config._ps_pdb_driver.quit()
                        ps_config._ps_pdb_driver = None
                except Exception:
                    pass
        try:
            if hasattr(self, "_xvfb_display") and self._xvfb_display and hasattr(self._xvfb_display, "stop"):
                self.headless_active = False
                ps_config.headless_active = False
                self._xvfb_display.stop()
                self._xvfb_display = None
            if hasattr(ps_config, "_virtual_display") and ps_config._virtual_display and hasattr(ps_config._virtual_display, "stop"):
                ps_config._virtual_display.stop()
                ps_config._virtual_display = None
        except Exception:
            pass
    except Exception:
        pass
    if (ps_config._has_exception or (python3_11_or_newer and py311_patch2) or "--pdb" in sys_argv) and ps_config.list_fp and ps_config._fail_page:
        if "-s" in sys_argv or "--capture=no" in sys_argv or (hasattr(ps_config.pytest_config, "invocation_params") and ("-s" in ps_config.pytest_config.invocation_params.args or "--capture=no" in (ps_config.pytest_config.invocation_params.args))):
            print("\n=> Fail Page: %s" % ps_config._fail_page)
        else:
            sys.stdout.write("\n=> Fail Page: %s\n" % ps_config._fail_page)


def pytest_sessionfinish(session):
    pass


def pytest_terminal_summary(terminalreporter):
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    if not hasattr(terminalreporter, "stats") or not hasattr(terminalreporter.stats, "keys"):
        return
    if len(terminalreporter.stats.keys()) == 0:
        return
    if not ps_config._multithreaded and not ps_config._pysel_detected:
        return
    latest_logs_dir = os.path.join(os.getcwd(), constants.Logs.LATEST) + os.sep
    if "failed" in terminalreporter.stats.keys() and os.path.exists(latest_logs_dir) and os.listdir(latest_logs_dir):
        ps_config._has_exception = True
    if ps_config._multithreaded:
        if os.path.exists(latest_logs_dir) and os.listdir(latest_logs_dir):
            ps_config._has_exception = True
        if ps_config.dashboard:
            abs_path = os.path.abspath(".")
            dash_lock = constants.Dashboard.LOCKFILE
            dash_lock_path = os.path.join(abs_path, dash_lock)
            if os.path.exists(dash_lock_path):
                ps_config._only_unittest = False
    if ps_config._has_exception and (ps_config.dashboard and not ps_config._only_unittest):
        # Print link a second time because the first one may be off-screen
        dashboard_file = os.path.join(os.getcwd(), "dashboard.html")
        dashboard_url = "file://" + dashboard_file.replace("\\", "/")
        terminalreporter.write_sep("-", "Dashboard = %s" % dashboard_url)
    if ps_config._has_exception or ps_config.save_screenshot or ps_config._has_logs:
        # Log files are generated during test failures and Screenshot Mode
        terminalreporter.write_sep("-", "Latest Logs dir: %s" % latest_logs_dir)


def _perform_pytest_unconfigure_():
    from pythonselenium.core import proxy_helper

    if (hasattr(ps_config, "multi_proxy") and not ps_config.multi_proxy) or not hasattr(ps_config, "multi_proxy"):
        proxy_helper.remove_proxy_zip_if_present()
    if hasattr(ps_config, "reuse_session") and ps_config.reuse_session:
        # Close the shared browser session
        if ps_config.shared_driver:
            try:
                if not is_windows or ps_config.browser == "ie" or ps_config.shared_driver.service.process:
                    ps_config.shared_driver.quit()
            except AttributeError:
                pass
            except Exception:
                pass
        ps_config.shared_driver = None
    if hasattr(ps_config, "log_path") and ps_config.item_count > 0:
        log_helper.archive_logs_if_set(constants.Logs.LATEST + "/", ps_config.archive_logs)
    log_helper.clear_empty_logs()
    # Dashboard post-processing: Disable time-based refresh and stamp complete
    if not hasattr(ps_config, "dashboard") or not ps_config.dashboard:
        # Done with "pytest_unconfigure" unless using the Dashboard
        return
    stamp = ""
    if ps_config._dash_is_html_report:
        # (If the Dashboard URL is the same as the HTML Report URL:)
        # Have the html report refresh back to a dashboard on update
        stamp += '\n<script type="text/javascript" src="%s">' "</script>" % constants.Dashboard.LIVE_JS
    stamp += "\n<!--Test Run Complete-->"
    find_it = constants.Dashboard.META_REFRESH_HTML
    swap_with = ""  # Stop refreshing the page after the run is done
    find_it_2 = "Awaiting results... (Refresh the page for updates)"
    swap_with_2 = "Test Run ENDED: Some results UNREPORTED due to skipped tearDown()"
    find_it_3 = '<td class="col-result">Untested</td>'
    swap_with_3 = '<td class="col-result">Unreported</td>'
    # These use caching to prevent extra method calls
    DASH_PIE_PNG_1 = constants.Dashboard.get_dash_pie_1()
    DASH_PIE_PNG_2 = constants.Dashboard.get_dash_pie_2()
    DASH_PIE_PNG_3 = constants.Dashboard.get_dash_pie_3()
    find_it_4 = 'href="%s"' % DASH_PIE_PNG_1
    swap_with_4 = 'href="%s"' % DASH_PIE_PNG_2
    try:
        abs_path = os.path.abspath(".")
        dashboard_path = os.path.join(abs_path, "dashboard.html")
        # Part 1: Finalizing the dashboard / integrating html report
        if os.path.exists(dashboard_path):
            the_html_d = None
            with open(dashboard_path, "r", encoding="utf-8") as f:
                the_html_d = f.read()
            if ps_config._multithreaded and "-c" in sys_argv:
                # Threads have "-c" in sys.argv, except for the last
                raise Exception('Break out of "try" block.')
            if ps_config._multithreaded:
                dash_pie_loc = constants.Dashboard.DASH_PIE
                pie_path = os.path.join(abs_path, dash_pie_loc)
                if os.path.exists(pie_path):
                    import json

                    with open(pie_path, "r") as f:
                        dash_pie = f.read().strip()
                    ps_config._saved_dashboard_pie = json.loads(dash_pie)
            # If the test run doesn't complete by itself, stop refresh
            the_html_d = the_html_d.replace(find_it, swap_with)
            the_html_d = the_html_d.replace(find_it_2, swap_with_2)
            the_html_d = the_html_d.replace(find_it_3, swap_with_3)
            the_html_d = the_html_d.replace(find_it_4, swap_with_4)
            the_html_d += stamp
            if ps_config._dash_is_html_report and (ps_config._saved_dashboard_pie):
                the_html_d = the_html_d.replace(
                    "<h1>dashboard.html</h1>",
                    ps_config._saved_dashboard_pie,
                )
                the_html_d = the_html_d.replace(
                    "</head>",
                    '</head><link rel="shortcut icon" ' 'href="%s">' % DASH_PIE_PNG_3,
                )
                the_html_d = the_html_d.replace("<html>", '<html lang="en">')
                the_html_d = the_html_d.replace(
                    "<head>",
                    '<head><meta http-equiv="Content-Type" ' 'content="text/html, charset=utf-8;">' '<meta name="viewport" content="shrink-to-fit=no">',
                )
                if ps_config._dash_final_summary:
                    the_html_d += ps_config._dash_final_summary
                time.sleep(0.1)  # Add time for "livejs" to detect changes
                with open(dashboard_path, "w", encoding="utf-8") as f:
                    f.write(the_html_d)  # Finalize the dashboard
                time.sleep(0.1)  # Add time for "livejs" to detect changes
                the_html_d = the_html_d.replace("</head>", "</head><!-- Dashboard Report Done -->")
            with open(dashboard_path, "w", encoding="utf-8") as f:
                f.write(the_html_d)  # Finalize the dashboard
            # Part 2: Appending a pytest html report with dashboard data
            html_report_path = None
            if ps_config._html_report_name:
                html_report_path = os.path.join(abs_path, ps_config._html_report_name)
            if ps_config._using_html_report and html_report_path and os.path.exists(html_report_path) and not ps_config._dash_is_html_report:
                # Add the dashboard pie to the pytest html report
                the_html_r = None
                with open(html_report_path, "r", encoding="utf-8") as f:
                    the_html_r = f.read()
                if ps_config._saved_dashboard_pie:
                    h_r_name = ps_config._html_report_name
                    if "/" in h_r_name and h_r_name.endswith(".html"):
                        h_r_name = h_r_name.split("/")[-1]
                    elif "\\" in h_r_name and h_r_name.endswith(".html"):
                        h_r_name = h_r_name.split("\\")[-1]
                    the_html_r = the_html_r.replace(
                        "<h1>%s</h1>" % h_r_name,
                        ps_config._saved_dashboard_pie,
                    )
                    the_html_r = the_html_r.replace(
                        "</head>",
                        '</head><link rel="shortcut icon" href=' '"%s">' % DASH_PIE_PNG_3,
                    )
                    if ps_config._dash_final_summary:
                        the_html_r += ps_config._dash_final_summary
                with open(html_report_path, "w", encoding="utf-8") as f:
                    f.write(the_html_r)  # Finalize the HTML report
    except KeyboardInterrupt:
        pass
    except Exception:
        pass


def pytest_unconfigure(config):
    """This runs after all tests have completed with pytest."""
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    if hasattr(ps_config, "_multithreaded") and ps_config._multithreaded:
        import fasteners

        dash_lock = fasteners.InterProcessLock(constants.Dashboard.LOCKFILE)
        if hasattr(ps_config, "dashboard") and ps_config.dashboard:
            # Multi-threaded tests with the Dashboard
            abs_path = os.path.abspath(".")
            dash_lock_file = constants.Dashboard.LOCKFILE
            dash_lock_path = os.path.join(abs_path, dash_lock_file)
            if os.path.exists(dash_lock_path):
                ps_config._only_unittest = False
                dashboard_path = os.path.join(abs_path, "dashboard.html")
                with dash_lock:
                    if ps_config._dash_html and config.getoption("htmlpath") == "dashboard.html":
                        # Dash is HTML Report (Multithreaded)
                        ps_config._dash_is_html_report = True
                        with open(dashboard_path, "w", encoding="utf-8") as f:
                            f.write(ps_config._dash_html)
                    # Dashboard Multithreaded
                    _perform_pytest_unconfigure_()
                    return
            else:
                # Dash Lock is missing
                _perform_pytest_unconfigure_()
                return
        with dash_lock:
            # Multi-threaded tests
            _perform_pytest_unconfigure_()
            return
    else:
        # Single-threaded tests
        _perform_pytest_unconfigure_()
        return


@pytest.fixture()
def ps(request):
    """PythonSelenium as a pytest fixture.
    Usage example: "def test_one(ps):"
    You may need to use this for tests that use other pytest fixtures."""
    from pythonselenium import BaseCase
    from pythonselenium.core import session_helper

    class BaseClass(BaseCase):
        def setUp(self):
            super().setUp()

        def tearDown(self):
            self.save_teardown_screenshot()
            super().tearDown()

        def base_method(self):
            pass

    if request.cls:
        if ps_config.reuse_class_session:
            the_class = str(request.cls).split(".")[-1].split("'")[0]
            if the_class != ps_config._ps_class:
                session_helper.end_reused_class_session_as_needed()
                ps_config._ps_class = the_class
        request.cls.ps = BaseClass("base_method")
        request.cls.ps.setUp()
        request.cls.ps._needs_tearDown = True
        request.cls.ps._using_ps_fixture = True
        request.cls.ps._using_ps_fixture_class = True
        ps_config._ps_node[request.node.nodeid] = request.cls.ps
        yield request.cls.ps
        if request.cls.ps._needs_tearDown:
            request.cls.ps.tearDown()
            request.cls.ps._needs_tearDown = False
    else:
        ps = BaseClass("base_method")
        ps.setUp()
        ps._needs_tearDown = True
        ps._using_ps_fixture = True
        ps._using_ps_fixture_no_class = True
        ps_config._ps_node[request.node.nodeid] = ps
        yield ps
        if ps._needs_tearDown:
            ps.tearDown()
            ps._needs_tearDown = False


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    if "--co" in sys_argv or "--collect-only" in sys_argv:
        return
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    if ps_config._multithreaded:
        ps_config._using_html_report = True  # For Dashboard use
    if pytest_html and report.when == "call" and hasattr(ps_config, "dashboard"):
        if ps_config.dashboard and not ps_config._pysel_detected:
            test_id, display_id = _get_test_ids_(item)
            r_outcome = report.outcome
            if len(r_outcome) > 1:
                r_outcome = r_outcome[0].upper() + r_outcome[1:]
            ps_config._results[test_id] = r_outcome
            ps_config._duration[test_id] = "*****"
            ps_config._display_id[test_id] = display_id
            ps_config._d_t_log_path[test_id] = ""
            if test_id not in ps_config._extra_dash_entries:
                ps_config._extra_dash_entries.append(test_id)
        elif ps_config._pysel_detected and ((python3_11_or_newer and py311_patch2) or "--pdb" in sys_argv) and (report.outcome == "failed" or "AssertionError" in str(call)) and not ps_config._has_exception:
            # Handle a bug on Python 3.11 where exceptions aren't seen
            log_path = ""
            ps_config._has_logs = True
            if hasattr(ps_config, "_test_logpath"):
                log_path = ps_config._test_logpath
            if ps_config.dashboard:
                ps_config._process_dashboard_entry(True)
            if hasattr(ps_config, "_add_pytest_html_extra"):
                ps_config._add_pytest_html_extra()
            if hasattr(ps_config, "_visual_baseline_copies"):
                ps_config._process_v_baseline_logs()
            ps_config._excinfo_value = call.excinfo.value
            ps_config._excinfo_tb = call.excinfo.tb
            if "pytest_plugin.BaseClass.base_method" not in log_path:
                source = None
                if hasattr(ps_config, "_last_page_source"):
                    source = ps_config._last_page_source
                if log_path and source:
                    log_helper.log_page_source(log_path, None, source)
                last_page_screenshot_png = None
                if hasattr(ps_config, "_last_page_screenshot_png"):
                    last_page_screenshot_png = ps_config._last_page_screenshot_png
                if log_path and last_page_screenshot_png:
                    log_helper.log_screenshot(log_path, None, last_page_screenshot_png)
                if log_path:
                    ps_config._log_fail_data()
        try:
            extra_report = None
            if hasattr(item, "_testcase"):
                extra_report = item._testcase._html_report_extra
            elif hasattr(item.instance, "ps") or (item.nodeid in ps_config._ps_node):
                if not hasattr(item.instance, "ps"):
                    ps_node = ps_config._ps_node[item.nodeid]
                else:
                    ps_node = item.instance.ps
                test_id = item.nodeid
                if not test_id:
                    test_id = "unidentified_TestCase"
                r"""
                # Now using the nodeid for both the test_id and display_id.
                # (This only impacts tests using The Dashboard.)
                # If there are any issues, we'll revert back to the old code.
                test_id = test_id.split("/")[-1].replace(" ", "_")
                if "[" in test_id:
                    test_id_intro = test_id.split("[")[0]
                    parameter = test_id.split("[")[1]
                    parameter = re.sub(re.compile(r"\W"), "", parameter)
                    test_id = test_id_intro + "__" + parameter
                test_id = test_id.replace("/", ".").replace("\\", ".")
                test_id = test_id.replace("::", ".").replace(".py", "")
                """
                ps_node._ps_test_identifier = test_id
                if ps_node._needs_tearDown:
                    ps_node.tearDown()
                    ps_node._needs_tearDown = False
                extra_report = ps_node._html_report_extra
            else:
                return
            extra = getattr(report, "extra", [])
            if len(extra_report) > 1 and extra_report[1]["content"]:
                report.extra = extra + extra_report
            if ps_config._dash_is_html_report:
                # If the Dashboard URL is the same as the HTML Report URL,
                # have the html report refresh back to a dashboard on update.
                refresh_updates = '<script type="text/javascript" src="%s">' "</script>" % constants.Dashboard.LIVE_JS
                report.extra.append(pytest_html.extras.html(refresh_updates))
        except Exception:
            pass