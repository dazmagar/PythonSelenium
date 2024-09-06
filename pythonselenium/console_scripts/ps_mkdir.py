"""
Creates a new folder for running PythonSelenium scripts.

Usage:
    pythonselenium mkdir [DIRECTORY] [OPTIONS]
      OR     pysel mkdir [DIRECTORY] [OPTIONS]

Example:
    pysel mkdir ui_tests

Options:
    -b / --basic  (Only config files. No tests added.)

Output:
    Creates a new folder for running pysel scripts.
    The new folder contains default config files,
    sample tests for helping new users get started,
    and Python boilerplates for setting up customized
    test frameworks.
"""
import codecs
import os
import sys

import colorama


def invalid_run_command(msg=None):
    exp = "  ** mkdir **\n\n"
    exp += "  Usage:\n"
    exp += "          pythonselenium mkdir [DIRECTORY] [OPTIONS]\n"
    exp += "            OR     pysel mkdir [DIRECTORY] [OPTIONS]\n"
    exp += "  Example:\n"
    exp += "          pysel mkdir ui_tests\n"
    exp += "  Options:\n"
    exp += "          -b / --basic  (Only config files. No tests added.)\n"
    exp += "  Output:\n"
    exp += "          Creates a new folder for running PySel scripts.\n"
    exp += "          The new folder contains default config files,\n"
    exp += "          sample tests for helping new users get started,\n"
    exp += "          and Python boilerplates for setting up customized\n"
    exp += "          test frameworks.\n"
    if not msg:
        raise Exception("INVALID RUN COMMAND!\n\n%s" % exp)
    elif msg == "help":
        print("\n%s" % exp)
        sys.exit()
    else:
        raise Exception("INVALID RUN COMMAND!\n\n%s\n%s\n" % (exp, msg))


def main():
    c1 = ""
    c5 = ""
    c7 = ""
    cr = ""
    if "linux" not in sys.platform:
        if (
            "win32" in sys.platform
            and hasattr(colorama, "just_fix_windows_console")
        ):
            colorama.just_fix_windows_console()
        else:
            colorama.init(autoreset=True)
        c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
        c5 = colorama.Fore.RED + colorama.Back.LIGHTYELLOW_EX
        c7 = colorama.Fore.BLACK + colorama.Back.MAGENTA
        cr = colorama.Style.RESET_ALL

    basic = False
    help_me = False
    error_msg = None
    invalid_cmd = None

    command_args = sys.argv[2:]
    dir_name = command_args[0]
    if dir_name == "-h" or dir_name == "--help":
        invalid_run_command("help")
    elif len(str(dir_name)) < 2:
        error_msg = "Directory name length must be at least 2 characters long!"
    elif "/" in str(dir_name) or "\\" in str(dir_name):
        error_msg = 'Directory name must not include slashes ("/", "\\")!'
    elif dir_name.startswith("-"):
        error_msg = 'Directory name cannot start with "-"!'
    elif os.path.exists(os.getcwd() + "/" + dir_name):
        error_msg = (
            'Directory "%s" already exists in this directory!' % dir_name
        )
    if error_msg:
        error_msg = c5 + "ERROR: " + error_msg + cr
        invalid_run_command(error_msg)

    if len(command_args) >= 2:
        options = command_args[1:]
        for option in options:
            option = option.lower()
            if option == "-h" or option == "--help":
                help_me = True
            elif option == "-b" or option == "--basic":
                basic = True
            else:
                invalid_cmd = "\n===> INVALID OPTION: >> %s <<\n" % option
                invalid_cmd = invalid_cmd.replace(">> ", ">>" + c5 + " ")
                invalid_cmd = invalid_cmd.replace(" <<", " " + cr + "<<")
                invalid_cmd = invalid_cmd.replace(">>", c7 + ">>" + cr)
                invalid_cmd = invalid_cmd.replace("<<", c7 + "<<" + cr)
                help_me = True
                break
    if help_me:
        invalid_run_command(invalid_cmd)

    os.mkdir(dir_name)

    data = []
    pythonselenium_req = "pythonselenium"
    try:
        from pythonselenium import __version__

        pythonselenium_req = "pythonselenium>=%s" % str(__version__)
    except Exception:
        pass
    data.append(pythonselenium_req)
    data.append("")
    file_path = "%s/%s" % (dir_name, "requirements.txt")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("[pytest]")
    data.append("addopts = --capture=no -p no:cacheprovider")
    data.append("norecursedirs = .* build dist recordings temp assets")
    data.append("filterwarnings =")
    data.append("    ignore::pytest.PytestWarning")
    data.append("    ignore:.*U.*mode is deprecated:DeprecationWarning")
    data.append("junit_family = legacy")
    data.append("python_files = test_*.py *_test.py *_tests.py *_suite.py")
    data.append("python_classes = Test* *Test* *Test *Tests *Suite")
    data.append("python_functions = test_*")
    data.append("markers =")
    data.append("    marker1: custom marker")
    data.append("    marker2: custom marker")
    data.append("    marker3: custom marker")
    data.append("    marker_test_suite: custom marker")
    data.append("    expected_failure: custom marker")
    data.append("    local: custom marker")
    data.append("    remote: custom marker")
    data.append("    offline: custom marker")
    data.append("    develop: custom marker")
    data.append("    qa: custom marker")
    data.append("    ci: custom marker")
    data.append("    e2e: custom marker")
    data.append("    ready: custom marker")
    data.append("    smoke: custom marker")
    data.append("    deploy: custom marker")
    data.append("    active: custom marker")
    data.append("    master: custom marker")
    data.append("    release: custom marker")
    data.append("    staging: custom marker")
    data.append("    production: custom marker")
    data.append("")
    file_path = "%s/%s" % (dir_name, "pytest.ini")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("[flake8]")
    data.append("exclude=recordings,temp")
    data.append("ignore=W503, E501")
    data.append("")
    data.append("[nosetests]")
    data.append("nocapture=1")
    data.append("logging-level=INFO")
    data.append("")
    data.append("[behave]")
    data.append("show_skipped=false")
    data.append("show_timings=false")
    file_path = "%s/%s" % (dir_name, "setup.cfg")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("")
    file_path = "%s/%s" % (dir_name, "__init__.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("*.py[cod]")
    data.append("*.egg")
    data.append("*.egg-info")
    data.append("dist")
    data.append("build")
    data.append(".eggs")
    data.append("eggs")
    data.append("parts")
    data.append("bin")
    data.append("var")
    data.append("sdist")
    data.append("develop-eggs")
    data.append(".installed.cfg")
    data.append("lib")
    data.append("lib64")
    data.append("__pycache__")
    data.append(".env")
    data.append(".venv")
    data.append("env/")
    data.append("venv/")
    data.append("ENV/")
    data.append("VENV/")
    data.append("env.bak/")
    data.append("venv.bak/")
    data.append("pyvenv.cfg")
    data.append(".Python")
    data.append("include")
    data.append("pip-delete-this-directory.txt")
    data.append("pip-selfcheck.json")
    data.append("ipython.1.gz")
    data.append("nosetests.1")
    data.append(".noseids")
    data.append("pip-log.txt")
    data.append(".swp")
    data.append(".coverage")
    data.append(".tox")
    data.append("coverage.xml")
    data.append("nosetests.xml")
    data.append(".cache/*")
    data.append(".pytest_cache/*")
    data.append(".pytest_config")
    data.append("junit")
    data.append("test-results.xml")
    data.append(".idea")
    data.append(".project")
    data.append(".pydevproject")
    data.append(".vscode")
    data.append("chromedriver")
    data.append("geckodriver")
    data.append("msedgedriver")
    data.append("operadriver")
    data.append("uc_driver")
    data.append("MicrosoftWebDriver.exe")
    data.append("headless_ie_selenium.exe")
    data.append("IEDriverServer.exe")
    data.append("chromedriver.exe")
    data.append("geckodriver.exe")
    data.append("msedgedriver.exe")
    data.append("operadriver.exe")
    data.append("uc_driver.exe")
    data.append("logs")
    data.append("latest_logs")
    data.append("log_archives")
    data.append("archived_logs")
    data.append("geckodriver.log")
    data.append("ghostdriver.log")
    data.append("pytestdebug.log")
    data.append("reports/*.xml")
    data.append("latest_report")
    data.append("report_archives")
    data.append("archived_reports")
    data.append("html_report.html")
    data.append("report.html")
    data.append("report.xml")
    data.append("dashboard.html")
    data.append("dashboard.json")
    data.append("dash_pie.json")
    data.append("dashboard.lock")
    data.append("allure_report")
    data.append("allure-report")
    data.append("allure_results")
    data.append("allure-results")
    data.append("saved_charts")
    data.append("saved_presentations")
    data.append("tours_exported")
    data.append("images_exported")
    data.append("saved_cookies")
    data.append("recordings")
    data.append("visual_baseline")
    data.append(".DS_Store")
    data.append("selenium-server-standalone.jar")
    data.append("proxy.zip")
    data.append("proxy.lock")
    data.append("verbose_hub_server.dat")
    data.append("verbose_node_server.dat")
    data.append("ip_of_grid_hub.dat")
    data.append("downloaded_files")
    data.append("archived_files")
    data.append("assets")
    data.append("temp")
    data.append("temp_*/")
    data.append("node_modules")
    file_path = "%s/%s" % (dir_name, ".gitignore")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    if basic:
        data = []
        data.append("  %s/" % dir_name)
        data.append("  ├── __init__.py")
        data.append("  ├── pytest.ini")
        data.append("  ├── requirements.txt")
        data.append("  └── setup.cfg")
        file_path = "%s/%s" % (dir_name, "outline.rst")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()
        os.system("pysel print %s -n" % file_path)
        os.remove(file_path)
        success = (
            "\n" + c1 + '* Directory "' + dir_name + '" was created '
            "with config files! *" + cr + "\n"
        )
        print(success)
        return

    dir_name_2 = dir_name + "/" + "boilerplates"
    os.mkdir(dir_name_2)

    data = []
    data.append("")
    file_path = "%s/%s" % (dir_name_2, "__init__.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("from pythonselenium import BaseCase")
    data.append("BaseCase.main(__name__, __file__)")
    data.append("")
    data.append("")
    data.append("class BaseTestCase(BaseCase):")
    data.append("    def setUp(self):")
    data.append("        super().setUp()")
    data.append("        # <<< Run custom code AFTER the super() line >>>")
    data.append("")
    data.append("    def tearDown(self):")
    data.append("        self.save_teardown_screenshot()")
    data.append("        if self.has_exception():")
    data.append("            # <<< Run custom code if the test failed. >>>")
    data.append("            pass")
    data.append("        else:")
    data.append("            # <<< Run custom code if the test passed. >>>")
    data.append("            pass")
    data.append("        # (Wrap unreliable code in a try/except block.)")
    data.append("        # <<< Run custom code BEFORE the super() line >>>")
    data.append("        super().tearDown()")
    data.append("")
    data.append("    def login(self):")
    data.append("        # <<< Placeholder. Add your code here. >>>")
    data.append("        pass")
    data.append("")
    data.append("    def example_method(self):")
    data.append("        # <<< Placeholder. Add your code here. >>>")
    data.append("        pass")
    data.append("")
    file_path = "%s/%s" % (dir_name_2, "base_test_case.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("class Page(object):")
    data.append('    html = "html"')
    data.append("")
    file_path = "%s/%s" % (dir_name_2, "page_objects.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("from .base_test_case import BaseTestCase")
    data.append("from .page_objects import Page")
    data.append("")
    data.append("")
    data.append("class MyTestClass(BaseTestCase):")
    data.append("    def test_boilerplate(self):")
    data.append("        self.login()")
    data.append("        self.example_method()")
    data.append("        self.assert_element(Page.html)")
    data.append("")
    file_path = "%s/%s" % (dir_name_2, "boilerplate_test.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("from pythonselenium import BaseCase")
    data.append("BaseCase.main(__name__, __file__)")
    data.append("")
    data.append("")
    data.append("class DataPage:")
    data.append("    def go_to_data_url(self, ps):")
    data.append('        ps.open("data:text/html,<p>Hello!</p><input />")')
    data.append("")
    data.append("    def add_input_text(self, ps, text):")
    data.append('        ps.type("input", text)')
    data.append("")
    data.append("")
    data.append("class ObjTests(BaseCase):")
    data.append("    def test_data_url_page(self):")
    data.append("        DataPage().go_to_data_url(self)")
    data.append('        self.assert_text("Hello!", "p")')
    data.append('        DataPage().add_input_text(self, "Goodbye!")')
    data.append("")
    file_path = "%s/%s" % (dir_name_2, "classic_obj_test.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("class DataPage:")
    data.append("    def go_to_data_url(self, ps):")
    data.append('        ps.open("data:text/html,<p>Hello!</p><input />")')
    data.append("")
    data.append("    def add_input_text(self, ps, text):")
    data.append('        ps.type("input", text)')
    data.append("")
    data.append("")
    data.append("class ObjTests:")
    data.append("    def test_data_url_page(self, ps):")
    data.append("        DataPage().go_to_data_url(ps)")
    data.append('        ps.assert_text("Hello!", "p")')
    data.append('        DataPage().add_input_text(ps, "Goodbye!")')
    data.append("")
    file_path = "%s/%s" % (dir_name_2, "ps_fixture_test.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    dir_name_3 = dir_name_2 + "/" + "samples"
    os.mkdir(dir_name_3)

    data = []
    data.append("")
    file_path = "%s/%s" % (dir_name_3, "__init__.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("from pythonselenium import BaseCase")
    data.append("from .google_objects import HomePage, ResultsPage")
    data.append("")
    data.append("")
    data.append("class GoogleTests(BaseCase):")
    data.append("    def test_google_dot_com(self):")
    data.append('        self.open("https://google.com/ncr")')
    data.append('        self.assert_title_contains("Google")')
    data.append("        self.sleep(0.05)")
    data.append("        self.save_screenshot_to_logs()")
    data.append(
        "        self.wait_for_element('iframe[role=\"presentation\"]')"
    )
    data.append("        self.hide_elements('iframe')")
    data.append("        self.sleep(0.05)")
    data.append("        self.save_screenshot_to_logs()")
    data.append('        self.type(HomePage.search_box, "github.com")')
    data.append("        self.assert_element(HomePage.search_button)")
    data.append("        self.assert_element(HomePage.feeling_lucky_button)")
    data.append("        self.click(HomePage.search_button)")
    data.append(
        '        self.assert_text("github.com", ResultsPage.search_results)'
    )
    data.append("")
    file_path = "%s/%s" % (dir_name_3, "google_test.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("class HomePage(object):")
    data.append("    dialog_box = '[role=\"dialog\"] div'")
    data.append("    search_box = '[title=\"Search\"]'")
    data.append("    search_button = 'input[value=\"Google Search\"]'")
    data.append(
        '    feeling_lucky_button = """input[value="I\'m Feeling Lucky"]"""'
    )
    data.append("")
    data.append("")
    data.append("class ResultsPage(object):")
    data.append('    search_results = "div#center_col"')
    data.append("")
    file_path = "%s/%s" % (dir_name_3, "google_objects.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append('""" Classic Page Object Model with BaseCase inheritance """')
    data.append("")
    data.append("from pythonselenium import BaseCase")
    data.append("BaseCase.main(__name__, __file__)")
    data.append("")
    data.append("")
    data.append("class LoginPage:")
    data.append("    def login_to_swag_labs(self, ps, username):")
    data.append('        ps.open("https://www.saucedemo.com/")')
    data.append('        ps.type("#user-name", username)')
    data.append('        ps.type("#password", "secret_sauce")')
    data.append("        ps.click('input[type=\"submit\"]')")
    data.append("")
    data.append("")
    data.append("class MyTests(BaseCase):")
    data.append("    def test_swag_labs_login(self):")
    data.append(
        '        LoginPage().login_to_swag_labs(self, "standard_user")'
    )
    data.append('        self.assert_element("#inventory_container")')
    data.append(
        "        self.assert_element('div:contains(\"Sauce Labs Backpack\")')"
    )
    data.append('        self.js_click("a#logout_sidebar_link")')
    data.append('        self.assert_element("div#login_button_container")')
    data.append("")
    file_path = "%s/%s" % (dir_name_3, "swag_labs_test.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append('""" Classic Page Object Model with the "ps" fixture """')
    data.append("")
    data.append("")
    data.append("class LoginPage:")
    data.append("    def login_to_swag_labs(self, ps, username):")
    data.append('        ps.open("https://www.saucedemo.com/")')
    data.append('        ps.type("#user-name", username)')
    data.append('        ps.type("#password", "secret_sauce")')
    data.append("        ps.click('input[type=\"submit\"]')")
    data.append("")
    data.append("")
    data.append("class MyTests:")
    data.append("    def test_swag_labs_login(self, ps):")
    data.append('        LoginPage().login_to_swag_labs(ps, "standard_user")')
    data.append('        ps.assert_element("div.inventory_list")')
    data.append(
        "        ps.assert_element('div:contains(\"Sauce Labs Backpack\")')"
    )
    data.append('        ps.js_click("a#logout_sidebar_link")')
    data.append('        ps.assert_element("div#login_button_container")')
    data.append("")
    file_path = "%s/%s" % (dir_name_3, "ps_swag_test.py")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()

    data = []
    data.append("  %s/" % dir_name)
    data.append("  ├── __init__.py")
    data.append("  ├── my_first_test.py")
    data.append("  ├── pytest.ini")
    data.append("  ├── requirements.txt")
    data.append("  ├── setup.cfg")
    data.append("  └── boilerplates/")
    data.append("      ├── __init__.py")
    data.append("      ├── base_test_case.py")
    data.append("      ├── boilerplate_test.py")
    data.append("      ├── classic_obj_test.py")
    data.append("      ├── page_objects.py")
    data.append("      ├── ps_fixture_test.py")
    data.append("      └── samples/")
    data.append("          ├── __init__.py")
    data.append("          ├── google_objects.py")
    data.append("          ├── google_test.py")
    data.append("          ├── ps_swag_test.py")
    data.append("          └── swag_labs_test.py")
    file_path = "%s/%s" % (dir_name, "outline.rst")
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()
    if " " not in file_path:
        os.system("pysel print %s -n" % file_path)
    elif '"' not in file_path:
        os.system('pysel print "%s" -n' % file_path)
    else:
        os.system("pysel print '%s' -n" % file_path)
    os.remove(file_path)

    success = (
        "\n" + c1 + '* Directory "' + dir_name + '" was created '
        "with config files and sample tests! *" + cr + "\n"
    )
    print(success)


if __name__ == "__main__":
    invalid_run_command()
