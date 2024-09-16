"""
The PythonSelenium-Behave Connector configures command-line options.
******************************************************************
Examples:
behave -D browser=edge -D dashboard -D headless
behave -D rs -D dashboard
behave -D agent="User Agent String" -D demo
****************************************************************
-D browser=BROWSER  (The web browser to use. Default: "chrome".)
-D chrome  (Shortcut for "-D browser=chrome". Default.)
-D edge  (Shortcut for "-D browser=edge".)
-D firefox  (Shortcut for "-D browser=firefox".)
-D safari  (Shortcut for "-D browser=safari".)
-D settings-file=FILE  (Override default PythonSelenium settings.)
-D env=ENV  (Set the test env. Access with "self.env" in tests.)
-D account=STR  (Set account. Access with "self.account" in tests.)
-D data=STRING  (Extra test data. Access with "self.data" in tests.)
-D var1=STRING  (Extra test data. Access with "self.var1" in tests.)
-D var2=STRING  (Extra test data. Access with "self.var2" in tests.)
-D var3=STRING  (Extra test data. Access with "self.var3" in tests.)
-D variables=DICT  (A test var dict. Access with "self.variables".)
-D user-data-dir=DIR  (Set the Chrome user data directory to use.)
-D protocol=PROTOCOL  (The Selenium Grid protocol: http|https.)
-D server=SERVER  (The Selenium Grid server/IP used for tests.)
-D port=PORT  (The Selenium Grid port used by the test server.)
-D cap-file=FILE  (The web browser's desired capabilities to use.)
-D cap-string=STRING  (The web browser's desired capabilities to use.)
-D proxy=SERVER:PORT  (Connect to a proxy server:port as tests are running)
-D proxy=USERNAME:PASSWORD@SERVER:PORT  (Use an authenticated proxy server)
-D proxy-bypass-list=STRING (";"-separated hosts to bypass, Eg "*.foo.com")
-D proxy-pac-url=URL  (Connect to a proxy server using a PAC_URL.pac file.)
-D proxy-pac-url=USERNAME:PASSWORD@URL  (Authenticated proxy with PAC URL.)
-D multi-proxy  (Allow multiple authenticated proxies when multi-threaded.)
-D agent=STRING  (Modify the web browser's User-Agent string.)
-D mobile  (Use the mobile device emulator while running tests.)
-D metrics=STRING  (Set mobile metrics: "CSSWidth,CSSHeight,PixelRatio".)
-D chromium-arg=ARG  (Add a Chromium arg for Chrome/Edge, comma-separated.)
-D firefox-arg=ARG  (Add a Firefox arg for Firefox, comma-separated.)
-D firefox-pref=SET  (Set a Firefox preference:value set, comma-separated.)
-D extension-zip=ZIP  (Load a Chrome Extension .zip|.crx, comma-separated.)
-D extension-dir=DIR  (Load a Chrome Extension directory, comma-separated.)
-D binary-location=PATH  (Set path of the Chromium browser binary to use.)
-D driver-version=VER  (Set the chromedriver or uc_driver version to use.)
-D sjw  (Skip JS Waits for readyState to be "complete" or Angular to load.)
-D pls=PLS  (Set pageLoadStrategy on Chrome: "normal", "eager", or "none".)
-D headless  (Run tests in headless mode. The default arg on Linux OS.)
-D headless2  (Use the new headless mode, which supports extensions.)
-D headed  (Run tests in headed/GUI mode on Linux OS, where not default.)
-D xvfb  (Run tests using the Xvfb virtual display server on Linux OS.)
-D locale=LOCALE_CODE  (Set the Language Locale Code for the web browser.)
-D pdb  (Activate Post Mortem Debug Mode if a test fails.)
-D interval=SECONDS  (The autoplay interval for presentations & tour steps)
-D start-page=URL  (The starting URL for the web browser when tests begin.)
-D archive-logs  (Archive existing log files instead of deleting them.)
-D archive-downloads  (Archive old downloads instead of deleting them.)
-D time-limit=SECONDS  (Safely fail any test that exceeds the time limit.)
-D slow  (Slow down the automation. Faster than using Demo Mode.)
-D demo  (Slow down and visually see test actions as they occur.)
-D demo-sleep=SECONDS  (Set the wait time after Slow & Demo Mode actions.)
-D highlights=NUM  (Number of highlight animations for Demo Mode actions.)
-D message-duration=SECONDS  (The time length for Messenger alerts.)
-D check-js  (Check for JavaScript errors after page loads.)
-D ad-block  (Block some types of display ads from loading.)
-D block-images  (Block images from loading during tests.)
-D do-not-track  (Indicate to websites that you don't want to be tracked.)
-D verify-delay=SECONDS  (The delay before MasterQA verification checks.)
-D recorder  (Enables the Recorder for turning browser actions into code.)
-D rec-behave  (Same as Recorder Mode, but also generates behave-gherkin.)
-D rec-sleep  (If the Recorder is enabled, also records self.sleep calls.)
-D rec-print  (If the Recorder is enabled, prints output after tests end.)
-D disable-js  (Disable JavaScript on Chromium. May break websites!)
-D disable-csp  (Disable the Content Security Policy of websites.)
-D disable-ws  (Disable Web Security on Chromium-based browsers.)
-D enable-ws  (Enable Web Security on Chromium-based browsers.)
-D enable-sync  (Enable "Chrome Sync".)
-D uc | -D undetected  (Use undetected-chromedriver to evade bot-detection)
-D uc-cdp-events  (Capture CDP events when running in "-D undetected" mode)
-D log-cdp  ("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
-D remote-debug  (Sync to Chrome Remote Debugger chrome://inspect/#devices)
-D dashboard  (Enable the PythonSelenium Dashboard. Saved at: dashboard.html)
-D dash-title=STRING  (Set the title shown for the generated dashboard.)
-D enable-3d-apis  (Enables WebGL and 3D APIs.)
-D swiftshader  (Use Chrome's SwiftShader Graphics Library.)
-D incognito  (Enable Chrome's Incognito mode.)
-D guest  (Enable Chrome's Guest mode.)
-D dark  (Enable Chrome's Dark mode.)
-D devtools  (Open Chrome's DevTools when the browser opens.)
-D rs | -D reuse-session  (Reuse browser session for all tests.)
-D rcs | -D reuse-class-session  (Reuse session for tests in class/feature)
-D crumbs  (Delete all cookies between tests reusing a session.)
-D disable-beforeunload  (Disable the "beforeunload" event on Chrome.)
-D window-size=WIDTH,HEIGHT  (Set the browser's starting window size.)
-D maximize  (Start tests with the browser window maximized.)
-D screenshot  (Save a screenshot at the end of each test.)
-D no-screenshot  (No screenshots saved unless tests directly ask it.)
-D visual-baseline  (Set the visual baseline for Visual/Layout tests.)
-D wire  (Use selenium-wire's webdriver for replacing selenium webdriver.)
-D external-pdf  (Set Chromium "plugins.always_open_pdf_externally":True.)
-D timeout-multiplier=MULTIPLIER  (Multiplies the default timeout values.)
"""

import ast
import os
import re
import sys

import colorama

from pythonselenium import config as ps_config
from pythonselenium.config import settings
from pythonselenium.core import (
    download_helper,
    log_helper,
    proxy_helper,
    session_helper,
)
from pythonselenium.fixtures import constants, shared_utils

is_linux = shared_utils.is_linux()
is_windows = shared_utils.is_windows()
ps_config.__base_class = None


def set_base_class(base_class):
    """
    # You can override the base class from Behave's environment.py file.
    # If not using PythonSelenium's BaseCase class, then use a subclass.
        from pythonselenium import BaseCase
        from pythonselenium.plugins import behave_plugin
        behave_plugin.set_base_class(BaseCase)
    """
    ps_config.__base_class = base_class


def get_configured_PS(context):
    if not ps_config.__base_class:
        from pythonselenium import BaseCase

        ps_config.__base_class = BaseCase
    ps_config.__base_class.test_method = {}
    ps = ps_config.__base_class("test_method")

    # Set default values
    ps.browser = "chrome"
    ps.is_behave = True
    ps.headless = False
    ps.headless2 = False
    ps.headless_active = False
    ps.headed = False
    ps.xvfb = False
    ps.start_page = None
    ps.locale_code = None
    ps.pdb_option = False
    ps.protocol = "http"
    ps.servername = "localhost"
    ps.port = 4444
    ps.data = None
    ps.var1 = None
    ps.var2 = None
    ps.var3 = None
    ps.variables = {}
    ps.account = None
    ps.environment = "test"
    ps.env = "test"
    ps.user_agent = None
    ps.incognito = False
    ps.guest_mode = False
    ps.dark_mode = False
    ps.devtools = False
    ps.mobile_emulator = False
    ps.device_metrics = None
    ps.extension_zip = None
    ps.extension_dir = None
    ps.binary_location = None
    ps.driver_version = None
    ps.page_load_strategy = None
    ps.database_env = "test"
    ps.log_path = constants.Logs.LATEST + os.sep
    ps.archive_logs = False
    ps.disable_js = False
    ps.disable_csp = False
    ps.disable_ws = False
    ps.enable_ws = False
    ps.enable_sync = False
    ps.use_auto_ext = False
    ps.undetectable = False
    ps.uc_cdp_events = False
    ps.uc_subprocess = False
    ps.log_cdp_events = False
    ps.no_sandbox = False
    ps.disable_gpu = False
    ps._multithreaded = False
    ps._reuse_session = False
    ps._reuse_class_session = False
    ps._crumbs = False
    ps._disable_beforeunload = False
    ps.visual_baseline = False
    ps.use_wire = False
    ps.window_size = None
    ps.maximize_option = False
    ps.is_context_manager = False
    ps.save_screenshot_after_test = False
    ps.no_screenshot_after_test = False
    ps.timeout_multiplier = None
    ps.pytest_html_report = None
    ps.with_db_reporting = False
    ps.with_s3_logging = False
    ps.js_checking_on = False
    ps.recorder_mode = False
    ps.recorder_ext = False
    ps.record_sleep = False
    ps.rec_behave = False
    ps.rec_print = False
    ps.report_on = False
    ps.is_pytest = False
    ps.slow_mode = False
    ps.demo_mode = False
    ps.time_limit = None
    ps.demo_sleep = None
    ps.dashboard = False
    ps.dash_title = None
    ps._dash_initialized = False
    ps.message_duration = None
    ps.block_images = False
    ps.do_not_track = False
    ps.external_pdf = False
    ps.remote_debug = False
    ps.settings_file = None
    ps.user_data_dir = None
    ps.chromium_arg = None
    ps.firefox_arg = None
    ps.firefox_pref = None
    ps.disable_features = None
    ps.proxy_string = None
    ps.proxy_bypass_list = None
    ps.proxy_pac_url = None
    ps.multi_proxy = False
    ps.host_resolver_rules = None
    ps.enable_3d_apis = False
    ps.swiftshader = False
    ps.ad_block_on = False
    ps.is_nosetest = False
    ps.highlights = None
    ps.interval = None
    ps.cap_file = None
    ps.cap_string = None

    # Set a few ps_config vars early in case parsing args fails
    ps_config.dashboard = None
    ps_config._has_logs = None
    ps_config._has_exception = None
    ps_config.save_screenshot = None
    ps_config.reuse_class_session = None

    browsers = set()  # To error if selecting more than one
    valid_browsers = constants.ValidBrowsers.valid_browsers
    valid_envs = constants.ValidEnvs.valid_envs
    # Process command-line options
    userdata = context.config.userdata
    for key in userdata.keys():
        # Convert --ARG to ARG, etc.
        if key.startswith("--"):
            key = key[2:]
        if key.startswith("-"):
            key = key[1:]
        low_key = key.lower()
        # Handle: -D browser=BROWSER
        if low_key == "browser":
            browser = userdata[key].lower()
            if browser in valid_browsers:
                ps.browser = browser
                browsers.add(browser)
            elif browser == "true":
                raise Exception('\nThe "browser" argument requires a value!' "\nChoose from %s." '\nEg. -D browser="edge"' % valid_browsers)
            else:
                raise Exception('\n"%s" is not a valid "browser" selection!' "\nChoose from %s." '\nEg. -D browser="edge"' % (browser, valid_browsers))
            continue
        # Handle: -D BROWSER
        if low_key in valid_browsers:
            browser = low_key
            ps.browser = browser
            browsers.add(browser)
            continue
        # Handle: -D headless
        if low_key == "headless":
            ps.headless = True
            continue
        # Handle: -D headless2
        if low_key == "headless2":
            ps.headless2 = True
            continue
        # Handle: -D headed / gui
        if low_key in ["headed", "gui"]:
            ps.headed = True
            continue
        # Handle: -D xvfb
        if low_key == "xvfb":
            ps.xvfb = True
            continue
        # Handle: -D start-page=URL / start_page=URL / url=URL
        if low_key in ["start-page", "start_page", "url"]:
            start_page = userdata[key]
            if start_page == "true":
                start_page = ps.start_page  # revert to default
            ps.start_page = start_page
            continue
        # Handle: -D locale-code=CODE / locale_code=CODE / locale=CODE
        if low_key in ["locale-code", "locale_code", "locale"]:
            ps.start_page = userdata[key]
            continue
        # Handle: -D pdb / ipdb
        if low_key in ["pdb", "ipdb"]:
            ps.pdb_option = True
            continue
        # Handle: -D protocol=PROTOCOL
        if low_key == "protocol":
            protocol = userdata[key].lower()
            if protocol in ["http", "https"]:
                ps.protocol = protocol
            elif protocol == "true":
                raise Exception('\nThe Selenium Grid "protocol" argument requires a value!' '\nChoose from ["http", "https"]' '\nEg. -D protocol="https"')
            else:
                raise Exception('\n"%s" is not a valid Selenium Grid "protocol" selection!' '\nChoose from ["http", "https"]' '\nEg. -D protocol="https"' % protocol)
            continue
        # Handle: -D server=SERVERNAME / servername=SERVERNAME
        if low_key in ["server", "servername"]:
            servername = userdata[key]
            if servername == "true":
                servername = ps.servername  # revert to default
            ps.servername = servername
            continue
        # Handle: -D port=PORT
        if low_key == "port":
            port = int(userdata[key])
            if port == "true":
                port = ps.port  # revert to default
            ps.port = port
            continue
        # Handle: -D data=DATA
        if low_key == "data":
            ps.data = userdata[key]
            continue
        # Handle: -D var1=DATA
        if low_key == "var1":
            ps.var1 = userdata[key]
            continue
        # Handle: -D var2=DATA
        if low_key == "var2":
            ps.var2 = userdata[key]
            continue
        # Handle: -D var3=DATA
        if low_key == "var3":
            ps.var3 = userdata[key]
            continue
        # Handle: -D variables="{'KEY':'VALUE','KEY2':'VALUE2'}"
        if low_key == "variables":
            variables = userdata[key]
            if variables and isinstance(variables, str) and len(variables) > 0:
                bad_input = False
                if not variables.startswith("{") or not variables.endswith("}"):
                    bad_input = True
                else:
                    try:
                        variables = ast.literal_eval(variables)
                        if not isinstance(variables, dict):
                            bad_input = True
                    except Exception:
                        bad_input = True
                if bad_input:
                    raise Exception('\nExpecting a Python dictionary for "variables"!' "\nEg. -D variables=\"{'KEY':'VALUE', 'KEY2':123}\"")
            else:
                variables = {}
            continue
        # Handle: -D account=ACCOUNT
        if low_key == "account":
            ps.account = userdata[key]
            continue
        # Handle: -D env=ENVIRONMENT
        if low_key == "environment":
            environment = userdata[key].lower()
            if environment in valid_envs:
                ps.environment = environment
                ps.env = environment
            elif environment == "true":
                raise Exception('\nThe "env" argument requires a value!' "\nChoose from %s." '\nEg. -D env="production"' % valid_envs)
            else:
                raise Exception('\n"%s" is not a valid "env" selection!' "\nChoose from %s." '\nEg. -D env="production"' % (environment, valid_envs))
            continue
        # Handle: -D user-agent=STRING / user_agent=STRING / agent=STRING
        if low_key in ["user-agent", "user_agent", "agent"]:
            user_agent = userdata[key]
            if user_agent == "true":
                user_agent = ps.user_agent  # revert to default
            ps.user_agent = user_agent
            continue
        # Handle: -D incognito / incognito-mode / incognito_mode
        if low_key in ["incognito", "incognito-mode", "incognito_mode"]:
            ps.incognito = True
            continue
        # Handle: -D guest / guest-mode / guest_mode
        if low_key in ["guest", "guest-mode", "guest_mode"]:
            ps.guest_mode = True
            continue
        # Handle: -D dark / dark-mode / dark_mode
        if low_key in ["dark", "dark-mode", "dark_mode"]:
            ps.dark_mode = True
            continue
        # Handle: -D devtools / open-devtools / open_devtools
        if low_key in ["devtools", "open-devtools", "open_devtools"]:
            ps.devtools = True
            continue
        # Handle: -D mobile / mobile-emulator / mobile_emulator
        if low_key in ["mobile", "mobile-emulator", "mobile_emulator"]:
            ps.mobile_emulator = True
            continue
        # Handle: -D metrics=STR / device-metrics=STR / device_metrics=STR
        if low_key in ["metrics", "device-metrics", "device_metrics"]:
            device_metrics = userdata[key]
            if device_metrics == "true":
                device_metrics = ps.device_metrics  # revert to default
            ps.device_metrics = device_metrics
            continue
        # Handle: -D crx=ZIP / extension-zip=ZIP / extension_zip=ZIP
        if low_key in ["crx", "extension-zip", "extension_zip"]:
            extension_zip = userdata[key]
            if extension_zip == "true":
                extension_zip = ps.extension_zip  # revert to default
            ps.extension_zip = extension_zip
            continue
        # Handle: -D extension-dir=DIR / extension_dir=DIR
        if low_key in ["extension-dir", "extension_dir"]:
            extension_dir = userdata[key]
            if extension_dir == "true":
                extension_dir = ps.extension_dir  # revert to default
            ps.extension_dir = extension_dir
            continue
        # Handle: -D binary-location=PATH / binary_location=PATH
        if low_key in ["binary-location", "binary_location"]:
            binary_location = userdata[key]
            if binary_location == "true":
                binary_location = ps.binary_location  # revert to default
            ps.binary_location = binary_location
            continue
        # Handle: -D driver-version=VER / driver_version=VER
        if low_key in ["driver-version", "driver_version"]:
            driver_version = userdata[key]
            if driver_version == "true":
                driver_version = ps.driver_version  # revert to default
            ps.driver_version = driver_version
            continue
        # Handle: -D pls=PLS / page-load-strategy=PLS / page_load_strategy=PLS
        if low_key in ["pls", "page-load-strategy", "page_load_strategy"]:
            page_load_strategy = userdata[key].lower()
            if page_load_strategy in ["normal", "eager", "none"]:
                ps.page_load_strategy = page_load_strategy
            elif page_load_strategy == "true":
                raise Exception('\nThe "pls" / "page-load-strategy" arg requires a value!' '\nChoose from ["normal", "eager", "none"]' '\nEg. -D pls="none"')
            else:
                raise Exception('\n"%s" is not a valid "pls" / "page-load-strategy" value!' '\nChoose from ["normal", "eager", "none"]' '\nEg. -D pls="none"' % page_load_strategy)
            continue
        # Handle: -D database-env=ENVIRONMENT / database_env=ENVIRONMENT
        if low_key in ["database-env", "database_env"]:
            database_env = userdata[key].lower()
            if database_env in valid_envs:
                ps.database_env = database_env
            elif database_env == "true":
                raise Exception('\nThe "database-env" argument requires a value!' "\nChoose from %s." '\nEg. -D database-env="production"' % valid_envs)
            else:
                raise Exception('\n"%s" is not a valid "database-env" selection!' "\nChoose from %s." '\nEg. -D database-env="production"' % (environment, valid_envs))
            continue
        # Handle: -D archive-logs / archive_logs
        if low_key in ["archive-logs", "archive_logs"]:
            ps.archive_logs = True
            continue
        # Handle: -D disable-js / disable_js
        if low_key in ["disable-js", "disable_js"]:
            ps.disable_js = True
            continue
        # Handle: -D disable-csp / disable_csp
        if low_key in ["disable-csp", "disable_csp"]:
            ps.disable_csp = True
            continue
        # Handle: -D disable-ws / disable_ws
        if low_key in ["disable-ws", "disable_ws"]:
            ps.disable_ws = True
            continue
        # Handle: -D enable-ws / enable_ws
        if low_key in ["enable-ws", "enable_ws"]:
            ps.enable_ws = True
            continue
        # Handle: -D enable-sync / enable_sync
        if low_key in ["enable-sync", "enable_sync"]:
            ps.enable_sync = True
            continue
        # Handle: -D use-auto-ext / use_auto_ext / auto-ext
        if low_key in ["use-auto-ext", "use_auto_ext", "auto-ext"]:
            ps.use_auto_ext = True
            continue
        # Handle: -D undetected / undetectable / uc
        if low_key in ["undetected", "undetectable", "uc"]:
            ps.undetectable = True
            continue
        # Handle: -D uc-cdp-events / uc_cdp_events / uc-cdp
        if low_key in ["uc-cdp-events", "uc_cdp_events", "uc-cdp"]:
            ps.uc_cdp_events = True
            ps.undetectable = True
            continue
        # Handle: -D uc-subprocess / uc_subprocess / uc-sub
        if low_key in ["uc-subprocess", "uc_subprocess", "uc-sub"]:
            ps.uc_subprocess = True
            ps.undetectable = True
            continue
        # Handle: -D log-cdp-events / log_cdp_events / log-cdp
        if low_key in ["log-cdp-events", "log_cdp_events", "log-cdp"]:
            ps.log_cdp_events = True
            continue
        # Handle: -D no-sandbox / no_sandbox
        if low_key in ["no-sandbox", "no_sandbox"]:
            ps.no_sandbox = True
            continue
        # Handle: -D disable-gpu / disable_gpu
        if low_key in ["disable-gpu", "disable_gpu"]:
            ps.disable_gpu = True
            continue
        # Handle: -D rs / reuse-session / reuse_session
        if low_key in ["rs", "reuse-session", "reuse_session"]:
            ps._reuse_session = True
            continue
        # Handle: -D rcs / rfs / reuse-class-session / reuse-feature-session
        if low_key in ["rcs", "rfs", "reuse-class-session", "reuse-feature-session"]:
            ps._reuse_session = True
            ps._reuse_class_session = True
            continue
        # Handle: -D crumbs
        if low_key == "crumbs":
            ps._crumbs = True
            continue
        # Handle: -D disable-beforeunload / disable_beforeunload
        if low_key in ["disable-beforeunload", "disable_beforeunload"]:
            ps._disable_beforeunload = True
            continue
        # Handle: -D sjw / skip-js-waits / skip_js_waits
        if low_key in ["sjw", "skip-js-waits", "skip_js_waits"]:
            settings.SKIP_JS_WAITS = True
            continue
        # Handle: -D visual-baseline / visual_baseline
        if low_key in ["visual-baseline", "visual_baseline"]:
            ps.visual_baseline = True
            continue
        # Handle: -D wire
        if low_key == "wire":
            ps.use_wire = True
            continue
        # Handle: -D window-size=Width,Height / window_size=Width,Height
        if low_key in ["window-size", "window_size"]:
            window_size = userdata[key]
            if window_size == "true":
                window_size = ps.window_size  # revert to default
            ps.window_size = window_size
            continue
        # Handle: -D maximize / fullscreen / maximize-window
        if low_key in ["maximize", "fullscreen", "maximize-window", "maximize_window"]:
            ps.maximize_option = True
            continue
        # Handle: -D screenshot / save-screenshot / save_screenshot / ss
        if low_key in ["screenshot", "save-screenshot", "save_screenshot", "ss"]:
            ps.save_screenshot_after_test = True
            continue
        # Handle: -D no-screenshot / no_screenshot / ns
        if low_key in ["no-screenshot", "no_screenshot", "ns"]:
            ps.no_screenshot_after_test = True
            continue
        # Handle: -D timeout-multiplier=FLOAT / timeout_multiplier=FLOAT
        if low_key in ["timeout-multiplier", "timeout_multiplier"]:
            timeout_multiplier = userdata[key]
            if timeout_multiplier == "true":
                timeout_multiplier = ps.timeout_multiplier  # revert to default
            ps.timeout_multiplier = timeout_multiplier
            continue
        # Handle: -D with-db-reporting / with-db_reporting
        if low_key in ["with-db-reporting", "with-db_reporting"]:
            ps.with_db_reporting = True
            continue
        # Handle: -D with-s3-logging / with-s3_logging
        if low_key in ["with-s3-logging", "with-s3_logging"]:
            ps.with_s3_logging = True
            continue
        # Handle: -D check-js / check_js
        if low_key in ["check-js", "check_js"]:
            ps.js_checking_on = True
            continue
        # Handle: -D recorder / record / rec / codegen
        if low_key in ["recorder", "record", "rec", "codegen"]:
            ps.recorder_mode = True
            ps.recorder_ext = True
            continue
        # Handle: -D rec-behave / rec-gherkin
        if low_key in ["rec-behave", "rec-gherkin"]:
            ps.rec_behave = True
            ps.recorder_mode = True
            ps.recorder_ext = True
            continue
        # Handle: -D record-sleep / record_sleep / rec-sleep / rec_sleep
        if low_key in ["record-sleep", "rec-sleep"]:
            ps.record_sleep = True
            ps.recorder_mode = True
            ps.recorder_ext = True
            continue
        # Handle: -D rec-print
        if low_key in ["rec-print"]:
            ps.rec_print = True
            ps.recorder_mode = True
            ps.recorder_ext = True
            continue
        # Handle: -D slow / slowmo / slow-mode / slow_mode
        if low_key in ["slow", "slowmo", "slow-mode", "slow_mode"]:
            ps.slow_mode = True
            continue
        # Handle: -D demo / demo-mode / demo_mode
        if low_key in ["demo", "demo-mode", "demo_mode"]:
            ps.demo_mode = True
            continue
        # Handle: -D time-limit / time_limit / timelimit
        if low_key in ["time-limit", "time_limit", "timelimit"]:
            time_limit = userdata[key]
            if time_limit == "true":
                time_limit = ps.time_limit  # revert to default
            ps.time_limit = time_limit
            continue
        # Handle: -D demo-sleep / demo_sleep
        if low_key in ["demo-sleep", "demo_sleep"]:
            demo_sleep = userdata[key]
            if demo_sleep == "true":
                demo_sleep = ps.demo_sleep  # revert to default
            ps.demo_sleep = demo_sleep
            continue
        # Handle: -D dashboard
        if low_key == "dashboard":
            ps.dashboard = True
            continue
        # Handle: -D dash-title=TITLE / dash_title=TITLE
        if low_key in ["dash-title", "dash_title"]:
            ps.dash_title = userdata[key]
            continue
        # Handle: -D message-duration / message_duration
        if low_key in ["message-duration", "message_duration"]:
            message_duration = userdata[key]
            if message_duration == "true":
                message_duration = ps.message_duration  # revert to default
            ps.message_duration = message_duration
            continue
        # Handle: -D block-images / block_images
        if low_key in ["block-images", "block_images"]:
            ps.block_images = True
            continue
        # Handle: -D do-not-track / do_not_track
        if low_key in ["do-not-track", "do_not_track"]:
            ps.do_not_track = True
            continue
        # Handle: -D external-pdf / external_pdf
        if low_key in ["external-pdf", "external_pdf"]:
            ps.external_pdf = True
            continue
        # Handle: -D remote-debug / remote_debug / remote-debugger
        if low_key in ["remote-debug", "remote_debug", "remote-debugger"]:
            ps.remote_debug = True
            continue
        # Handle: -D settings=FILE / settings-file=FILE / settings_file=FILE
        if low_key in ["settings", "settings-file", "settings_file"]:
            settings_file = userdata[key]
            if settings_file == "true":
                settings_file = ps.settings_file  # revert to default
            ps.settings_file = settings_file
            continue
        # Handle: -D user-data-dir=DIR / user_data_dir=DIR
        if low_key in ["user-data-dir", "user_data_dir"]:
            user_data_dir = userdata[key]
            if user_data_dir == "true":
                user_data_dir = ps.user_data_dir  # revert to default
            ps.user_data_dir = user_data_dir
            continue
        # Handle: -D chromium-arg="ARG=N,ARG2" / chromium_arg="ARG=N,ARG2"
        if low_key in ["chromium-arg", "chromium_arg"]:
            chromium_arg = userdata[key]
            if chromium_arg == "true":
                chromium_arg = ps.chromium_arg  # revert to default
            ps.chromium_arg = chromium_arg
            continue
        # Handle: -D firefox-arg="ARG=N,ARG2" / firefox_arg="ARG=N,ARG2"
        if low_key in ["firefox-arg", "firefox_arg"]:
            firefox_arg = userdata[key]
            if firefox_arg == "true":
                firefox_arg = ps.firefox_arg  # revert to default
            ps.firefox_arg = firefox_arg
            continue
        # Handle: -D firefox-pref="PREF:VAL" / firefox_pref="PREF:VAL"
        if low_key in ["firefox-pref", "firefox_pref"]:
            firefox_pref = userdata[key]
            if firefox_pref == "true":
                firefox_pref = ps.firefox_pref  # revert to default
            ps.firefox_pref = firefox_pref
            continue
        # Handle: -D disable-features="F1,F2" / disable_features="F1,F2"
        if low_key in ["disable-features", "disable_features"]:
            disable_features = userdata[key]
            if disable_features == "true":
                disable_features = ps.disable_features  # revert to default
            ps.disable_features = disable_features
            continue
        # Handle: -D proxy=SERVER:PORT / proxy=USERNAME:PASSWORD@SERVER:PORT
        if low_key in ["proxy", "proxy-server", "proxy-string"]:
            proxy_string = userdata[key]
            if proxy_string == "true":
                proxy_string = ps.proxy_string  # revert to default
            ps.proxy_string = proxy_string
            continue
        # Handle: -D proxy-bypass-list="DOMAIN1;D2" / proxy_bypass_list="D1;D2"
        if low_key in ["proxy-bypass-list", "proxy_bypass_list"]:
            proxy_bypass_list = userdata[key]
            if proxy_bypass_list == "true":
                proxy_bypass_list = ps.proxy_bypass_list  # revert to default
            ps.proxy_bypass_list = proxy_bypass_list
            continue
        # Handle: -D proxy-pac-url=URL / proxy-pac-url=USERNAME:PASSWORD@URL
        if low_key in ["proxy-pac-url", "pac-url"]:
            proxy_pac_url = userdata[key]
            if proxy_pac_url == "true":
                proxy_pac_url = ps.proxy_pac_url  # revert to default
            ps.proxy_pac_url = proxy_pac_url
            continue
        # Handle: -D multi-proxy / multi_proxy
        if low_key in ["multi-proxy", "multi_proxy"]:
            ps.multi_proxy = True
            continue
        # Handle: -D host-resolver-rules=RULES / host_resolver_rules=RULES
        if low_key in ["host-resolver-rules", "host_resolver_rules"]:
            host_resolver_rules = userdata[key]
            if host_resolver_rules == "true":
                host_resolver_rules = ps.host_resolver_rules
            ps.host_resolver_rules = host_resolver_rules
            continue
        # Handle: -D enable-3d-apis / enable_3d_apis
        if low_key in ["enable-3d-apis", "enable_3d_apis"]:
            ps.enable_3d_apis = True
            continue
        # Handle: -D swiftshader
        if low_key == "swiftshader":
            ps.swiftshader = True
            continue
        # Handle: -D adblock / ad-block / ad_block / block-ads / block_ads
        if low_key in ["adblock", "ad-block", "ad_block", "block-ads", "block_ads"]:
            ps.ad_block_on = True
            continue
        # Handle: -D highlights=NUM
        if low_key == "highlights":
            highlights = userdata[key]
            if highlights == "true":
                highlights = ps.highlights  # revert to default
            ps.highlights = highlights
            continue
        # Handle: -D interval=SECONDS
        if low_key == "interval":
            interval = userdata[key]
            if interval == "true":
                interval = ps.interval  # revert to default
            ps.interval = interval
            continue
        # Handle: -D cap-file=FILE / cap_file=FILE
        if low_key in ["cap-file", "cap_file"]:
            cap_file = userdata[key]
            if cap_file == "true":
                cap_file = ps.cap_file  # revert to default
            ps.cap_file = cap_file
            continue
        # Handle: -D cap-string=STRING / cap_string=STRING
        if low_key == "cap_string":
            cap_string = userdata[key]
            if cap_string == "true":
                cap_string = ps.cap_string  # revert to default
            ps.cap_string = cap_string
            continue

    # Fail immediately if trying to set more than one default browser.
    if len(browsers) > 1:
        raise Exception("\nOnly ONE default browser is allowed!\n" "%s browsers were selected: %s" % (len(browsers), browsers))
    # Recorder Mode can still optimize scripts in "-D headless2" mode.
    if ps.recorder_ext and ps.headless:
        ps.headless = False
        ps.headless2 = True
    if ps.headless2 and ps.browser == "firefox":
        ps.headless2 = False  # Only for Chromium browsers
        ps.headless = True  # Firefox has regular headless
    elif ps.browser not in ["chrome", "edge"]:
        ps.headless2 = False  # Only for Chromium browsers
    # Recorder Mode only supports Chromium browsers.
    if ps.recorder_ext and (ps.browser not in ["chrome", "edge"]):
        raise Exception("\n\n  Recorder Mode ONLY supports Chrome and Edge!" '\n  (Your browser choice was: "%s")\n' % ps.browser)
    # The Xvfb virtual display server is for Linux OS Only.
    if ps.xvfb and not is_linux:
        ps.xvfb = False
    if is_linux and not ps.headed and not ps.headless and not ps.headless2 and not ps.xvfb:
        if not ps.undetectable:
            print('(Linux uses "-D headless" by default. ' 'To override, use "-D headed" / "-D gui". ' 'For Xvfb mode instead, use "-D xvfb". ' "Or you can hide this info by using" '"-D headless" / "-D headless2" / "-D uc".)')
            ps.headless = True
        else:
            ps.xvfb = True
    # Recorder Mode can still optimize scripts in --headless2 mode.
    if ps.recorder_mode and ps.headless:
        ps.headless = False
        ps.headless2 = True
    if not ps.headless and not ps.headless2:
        ps.headed = True
    if ps.browser == "safari" and ps.headless:
        ps.headless = False  # Safari doesn't support headless mode
    if ps.save_screenshot_after_test and ps.no_screenshot_after_test:
        ps.save_screenshot_after_test = False  # "no_screenshot" has priority
    if ps.servername != "localhost":
        # Using Selenium Grid
        # (Set -D server="127.0.0.1" for localhost Grid)
        # If the port is "443", the protocol is "https"
        if str(ps.port) == "443":
            ps.protocol = "https"
    if ps.window_size:
        window_size = ps.window_size
        if window_size.count(",") != 1:
            message = '\n\n  window_size expects a "width,height" string!' '\n  (Your input was: "%s")\n' % window_size
            raise Exception(message)
        window_size = window_size.replace(" ", "")
        width = None
        height = None
        try:
            width = int(window_size.split(",")[0])
            height = int(window_size.split(",")[1])
        except Exception:
            message = '\n\n  Expecting integer values for "width,height"!' '\n  (window_size input was: "%s")\n' % window_size
            raise Exception(message)
        settings.CHROME_START_WIDTH = width
        settings.CHROME_START_HEIGHT = height
        settings.HEADLESS_START_WIDTH = width
        settings.HEADLESS_START_HEIGHT = height

    # Set ps_config
    ps_config.browser = ps.browser
    ps_config.headless = ps.headless
    ps_config.headless_active = False
    ps_config.headed = ps.headed
    ps_config.is_behave = True
    ps_config.is_pytest = False
    ps_config.is_nosetest = False
    ps_config.is_context_manager = False
    ps_config.window_size = ps.window_size
    ps_config.maximize_option = ps.maximize_option
    ps_config.xvfb = ps.xvfb
    ps_config.reuse_class_session = ps._reuse_class_session
    ps_config.save_screenshot = ps.save_screenshot_after_test
    ps_config.no_screenshot = ps.no_screenshot_after_test
    ps_config._has_logs = False
    ps_config.variables = ps.variables
    ps_config.dashboard = ps.dashboard
    ps_config.dash_title = ps.dash_title
    ps_config.pdb_option = ps.pdb_option
    ps_config.rec_behave = ps.rec_behave
    ps_config.rec_print = ps.rec_print
    ps_config.disable_js = ps.disable_js
    ps_config.disable_csp = ps.disable_csp
    ps_config.record_sleep = ps.record_sleep
    ps_config._is_timeout_changed = False
    ps_config._SMALL_TIMEOUT = settings.SMALL_TIMEOUT
    ps_config._LARGE_TIMEOUT = settings.LARGE_TIMEOUT
    ps_config._recorded_actions = {}
    ps_config._behave_recorded_actions = {}
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

    if ps_config.dash_title:
        constants.Dashboard.TITLE = ps_config.dash_title.replace("_", " ")

    log_helper.log_folder_setup(constants.Logs.LATEST + "/", ps.archive_logs)
    download_helper.reset_downloads_folder()
    proxy_helper.remove_proxy_zip_if_present()
    return ps


def calculate_test_id(file_name, scenario_name):
    file_name = file_name.replace("/", ".").replace("\\", ".")
    scenario_name = re.sub(r"[^\w" + r"_ " + r"]", "", scenario_name)
    scenario_name = scenario_name.replace(" ", "_")
    if " -- @" in scenario_name:
        scenario_name = scenario_name.split(" # ")[0].rstrip()
    test_id = "%s.%s" % (file_name, scenario_name)
    return test_id


def calculate_display_id(file_name, line_num, scenario_name):
    if " -- @" in scenario_name:
        scenario_name = scenario_name.split(" # ")[0].rstrip()
    display_id = "%s:%s => %s" % (file_name, line_num, scenario_name)
    return display_id


def get_test_id():
    file_name = ps_config.behave_scenario.filename
    file_name = file_name.replace("/", ".").replace("\\", ".")
    scenario_name = ps_config.behave_scenario.name
    if " -- @" in scenario_name:
        scenario_name = scenario_name.split(" # ")[0].rstrip()
    scenario_name = re.sub(r"[^\w" + r"_ " + r"]", "", scenario_name)
    scenario_name = scenario_name.replace(" ", "_")
    test_id = "%s.%s" % (file_name, scenario_name)
    return test_id


def get_display_id():
    file_name = ps_config.behave_scenario.filename
    line_num = str(ps_config.behave_scenario.line)
    scenario_name = ps_config.behave_scenario.name
    if " -- @" in scenario_name:
        scenario_name = scenario_name.split(" # ")[0].rstrip()
    display_id = "%s:%s => %s" % (file_name, line_num, scenario_name)
    return display_id


def _get_test_ids_():
    test_id = get_test_id()
    display_id = get_display_id()
    return test_id, display_id


def dashboard_pre_processing():
    import subprocess

    command_args = sys.argv[1:]
    command_string = " ".join(command_args)
    command_string = command_string.replace("--quiet", "")
    command_string = command_string.replace("-q", "")
    proc = subprocess.Popen(
        "behave -d %s --show-source" % command_string,
        stdout=subprocess.PIPE,
        shell=True,
    )
    (output, error) = proc.communicate()
    filename_count = 0
    filename_list = []
    feature_count = 0
    feature_list = []
    scenario_count = 0
    scenario_list = []
    ps_config.item_count = 0
    ps_config.item_count_passed = 0
    ps_config.item_count_failed = 0
    ps_config.item_count_skipped = 0
    ps_config.item_count_untested = 0
    filename = None
    feature_name = None
    scenario_name = None
    if is_windows:
        output = output.decode("latin1")
    else:
        output = output.decode("utf-8")
    for row in output.replace("\r", "").split("\n"):
        if row.startswith("Feature: "):
            filename_count += 1
            feature_count += 1
            feature_name = row.split("Feature: ")[1]
            if " # features/" in feature_name:
                filename = feature_name.split(" # features/")[-1]
                filename = "features/" + filename.split(":")[0]
                feature_name = feature_name.split(" # features/")[0]
            elif " # features\\" in feature_name:
                filename = feature_name.split(" # features\\")[-1]
                filename = "features\\" + filename.split(":")[0]
                feature_name = feature_name.split(" # features\\")[0]
            else:
                filename = feature_name.split(" # ")[-1]
                filename = filename.split(":")[0]
                feature_name = feature_name.split(" # ")[-1]
            filename = filename.strip()
            filename_list.append(filename)
            feature_name = feature_name.strip()
            feature_list.append(feature_name)  # Maybe filename is good enough
        elif row.startswith("  Scenario: ") or row.startswith("  Scenario Outline: "):
            line_num = row.split(":")[-1]
            scenario_count += 1
            scenario_name = None
            if row.startswith("  Scenario: "):
                scenario_name = row.split("  Scenario: ")[-1]
            else:
                scenario_name = row.split("  Scenario Outline: ")[-1]
            if " -- @" in scenario_name:
                scenario_name = scenario_name.split(" # ")[0].rstrip()
            elif " # features/" in scenario_name:
                scenario_name = scenario_name.split(" # features/")[0]
            else:
                scenario_name = scenario_name.split(" # ")[0]
            scenario_name = scenario_name.strip()
            scenario_list.append(scenario_name)
            # Dashboard row preparation
            test_id = calculate_test_id(filename, scenario_name)
            display_id = calculate_display_id(filename, line_num, scenario_name)
            ps_config._results[test_id] = "Untested"
            ps_config._duration[test_id] = "-"
            ps_config._display_id[test_id] = display_id
            ps_config._d_t_log_path[test_id] = None
    # Set the total number of dashboard entries
    ps_config.item_count = scenario_count


def _create_dashboard_assets_():
    import codecs

    from pythonselenium.core.style_sheet import get_pytest_style
    from pythonselenium.js_code.live_js import live_js

    abs_path = os.path.abspath(".")
    assets_folder = os.path.join(abs_path, "assets")
    if not os.path.exists(assets_folder):
        os.makedirs(assets_folder)
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


def behave_dashboard_prepare():
    """Print the dashboard path if at least one test runs."""
    if ps_config.item_count > 0:
        _create_dashboard_assets_()
        # Output Dashboard info to the console
        ps_config.item_count_untested = ps_config.item_count
        dash_path = os.path.join(os.getcwd(), "dashboard.html")
        star_len = len("Dashboard: ") + len(dash_path)
        try:
            terminal_size = os.get_terminal_size().columns
            if terminal_size > 30 and star_len > terminal_size:
                star_len = terminal_size
        except Exception:
            pass
        stars = "*" * star_len
        c1 = ""
        cr = ""
        if not is_linux:
            if is_windows and hasattr(colorama, "just_fix_windows_console"):
                colorama.just_fix_windows_console()
            else:
                colorama.init(autoreset=True)
            c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
            cr = colorama.Style.RESET_ALL
        print("Dashboard: %s%s%s\n%s" % (c1, dash_path, cr, stars))


def _perform_behave_unconfigure_():
    if hasattr(ps_config, "multi_proxy") and not ps_config.multi_proxy:
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
    if hasattr(ps_config, "archive_logs"):
        log_helper.archive_logs_if_set(constants.Logs.LATEST + "/", ps_config.archive_logs)
    log_helper.clear_empty_logs()
    # Dashboard post-processing: Disable time-based refresh and stamp complete
    if not hasattr(ps_config, "dashboard") or not ps_config.dashboard:
        # Done with "behave_unconfigure" unless using the Dashboard
        return
    stamp = "\n<!--Test Run Complete-->"
    find_it = constants.Dashboard.META_REFRESH_HTML
    swap_with = ""  # Stop refreshing the page after the run is done
    find_it_2 = "Awaiting results... (Refresh the page for updates)"
    swap_with_2 = "Test Run ENDED: Some results UNREPORTED due to skipped tearDown()"
    find_it_3 = '<td class="col-result">Untested</td>'
    swap_with_3 = '<td class="col-result">Unreported</td>'
    if sys.version_info[0] >= 3:
        # These use caching to prevent extra method calls
        DASH_PIE_PNG_1 = constants.Dashboard.get_dash_pie_1()
        DASH_PIE_PNG_2 = constants.Dashboard.get_dash_pie_2()
    else:
        from pythonselenium.core import encoded_images

        DASH_PIE_PNG_1 = encoded_images.get_dash_pie_png1()
        DASH_PIE_PNG_2 = encoded_images.get_dash_pie_png2()
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
            if ps_config._multithreaded and "-c" in sys.argv:
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
            with open(dashboard_path, "w", encoding="utf-8") as f:
                f.write(the_html_d)  # Finalize the dashboard
    except KeyboardInterrupt:
        pass
    except Exception:
        pass


def do_final_driver_cleanup_as_needed():
    try:
        if hasattr(ps_config, "last_driver") and ps_config.last_driver:
            if not is_windows or ps_config.browser == "ie" or ps_config.last_driver.service.process:
                ps_config.last_driver.quit()
    except Exception:
        pass


def _perform_behave_terminal_summary_():
    latest_logs_dir = os.path.join(os.getcwd(), constants.Logs.LATEST + os.sep)
    dash_path = os.path.join(os.getcwd(), "dashboard.html")
    equals_len = len("Dashboard: ") + len(dash_path)
    try:
        terminal_size = os.get_terminal_size().columns
        if terminal_size > 30 and equals_len > terminal_size:
            equals_len = terminal_size
    except Exception:
        pass
    equals = "=" * (equals_len + 2)
    c2 = ""
    cr = ""
    if not is_linux:
        if is_windows and hasattr(colorama, "just_fix_windows_console"):
            colorama.just_fix_windows_console()
        else:
            colorama.init(autoreset=True)
        c2 = colorama.Fore.MAGENTA + colorama.Back.LIGHTYELLOW_EX
        cr = colorama.Style.RESET_ALL
    if ps_config.dashboard:
        # Print link a second time because the first one may be off-screen
        print("%s- Dashboard:%s %s" % (c2, cr, dash_path))
    if ps_config._has_exception or ps_config.save_screenshot or ps_config._has_logs:
        # Log files are generated during test failures and Screenshot Mode
        print("%s--- LogPath:%s %s" % (c2, cr, latest_logs_dir))
    if ps_config.dashboard and not (ps_config._has_exception or ps_config.save_screenshot):
        print("%s" % equals)
    elif not ps_config.dashboard and (ps_config._has_exception or ps_config.save_screenshot):
        print("%s" % equals[2:])
    elif ps_config.dashboard and (ps_config._has_exception or ps_config.save_screenshot):
        print("%s" % equals[2:])


###########################################


def before_all(context):
    context.ps = get_configured_PS(context)
    if context.ps.dashboard:
        dashboard_pre_processing()
        behave_dashboard_prepare()


def before_feature(context, feature):
    ps_config.behave_feature = feature
    session_helper.end_reused_class_session_as_needed()


def before_scenario(context, scenario):
    ps_config.behave_context = context
    ps_config.behave_scenario = scenario
    ps_config.behave_line_num = scenario.line
    ps_config.behave_step_count = 0
    context.ps.setUp()


def before_step(context, step):
    ps_config.behave_step_count += 1
    ps_config.behave_step = step
    context.behave_step = step


def after_step(context, step):
    ps_config.behave_step = step
    if step.status == "failed":
        number = ps_config.behave_step_count
        print(">>> STEP FAILED:  (#%s) %s" % (number, step.name))
        print("Class / Feature: ", ps_config.behave_feature.name)
        print("Test / Scenario: ", ps_config.behave_scenario.name)


def after_scenario(context, scenario):
    ps = context.ps
    ps_config.last_driver = ps.driver
    ps_config.behave_context = context
    ps_config.behave_scenario = scenario
    ps.tearDown()


def after_feature(context, feature):
    ps_config.feature = feature
    session_helper.end_reused_class_session_as_needed()


def after_all(context):
    _perform_behave_unconfigure_()
    do_final_driver_cleanup_as_needed()
    _perform_behave_terminal_summary_()
