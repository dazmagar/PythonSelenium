""" The main purpose of this file is to demonstrate running PythonSelenium
    scripts without the use of Pytest by calling the script directly
    with Python or from a Python interactive interpreter. Based on
    whether relative imports work or don't, the script can autodetect
    how this file was run. With pure Python, it will initialize
    all the variables that would've been automatically initialized
    by the Pytest plugin. The setUp() and tearDown() methods are also
    now called from the script itself.

    One big advantage to running tests with Pytest is that most of this
    is done for you automatically, with the option to update any of the
    parameters through command-line parsing. Pytest also provides you
    with other plugins, such as ones for generating test reports,
    handling multithreading, and parametrized tests. Depending on your
    specific needs, you may need to call PythonSelenium commands without
    using Pytest, and this example shows you how.
"""

pure_python = False
try:
    # Running with Pytest / (Finds test methods to run using autodiscovery)
    # Example run command:  "pytest raw_parameter_script.py"
    from .my_first_test import MyTestClass  # (relative imports work: ".~")

except (ImportError, ValueError):
    # Running with pure Python OR from a Python interactive interpreter
    # Example run command:  "python raw_parameter_script.py"
    from my_first_test import MyTestClass  # (relative imports do not work)

    pure_python = True

if pure_python:
    ps = MyTestClass("test_swag_labs")
    ps.browser = "chrome"
    ps.is_behave = False
    ps.headless = False
    ps.headless2 = False
    ps.headed = False
    ps.xvfb = False
    ps.start_page = None
    ps.locale_code = None
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
    ps.env = "test"  # should match ps.environment
    ps.user_agent = None
    ps.incognito = False
    ps.guest_mode = False
    ps.dark_mode = False
    ps.devtools = False
    ps.mobile_emulator = False
    ps.device_metrics = None
    ps.extension_zip = None
    ps.extension_dir = None
    ps.database_env = "test"
    ps.archive_logs = False
    ps.disable_csp = False
    ps.disable_ws = False
    ps.enable_ws = False
    ps.enable_sync = False
    ps.use_auto_ext = False
    ps.undetectable = False
    ps.uc_cdp_events = False
    ps.uc_subprocess = False
    ps.no_sandbox = False
    ps.disable_js = False
    ps.disable_gpu = False
    ps.log_cdp_events = False
    ps._multithreaded = False
    ps._reuse_session = False
    ps._crumbs = False
    ps._final_debug = False
    ps.esc_end = False
    ps.use_wire = False
    ps.enable_3d_apis = False
    ps.window_size = None
    ps.maximize_option = False
    ps.visual_baseline = False
    ps.disable_features = None
    ps._disable_beforeunload = False
    ps.save_screenshot_after_test = False
    ps.no_screenshot_after_test = False
    ps.host_resolver_rules = None
    ps.page_load_strategy = None
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
    ps._dash_initialized = False
    ps.message_duration = None
    ps.binary_location = None
    ps.driver_version = None
    ps.block_images = False
    ps.do_not_track = False
    ps.external_pdf = False
    ps.remote_debug = False
    ps.settings_file = None
    ps.user_data_dir = None
    ps.chromium_arg = None
    ps.firefox_arg = None
    ps.firefox_pref = None
    ps.proxy_string = None
    ps.proxy_bypass_list = None
    ps.proxy_pac_url = None
    ps._swiftshader = False
    ps.multi_proxy = False
    ps.ad_block_on = False
    ps.highlights = None
    ps.interval = None
    ps.cap_file = None
    ps.cap_string = None

    ps.setUp()
    try:
        ps.test_swag_labs()
    finally:
        ps.tearDown()
        del ps
