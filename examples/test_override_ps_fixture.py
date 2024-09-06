"""Overriding the "ps" fixture to override the driver."""

import pytest

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


@pytest.fixture()
def ps(request):
    from selenium import webdriver

    from pythonselenium import BaseCase
    from pythonselenium import config as ps_config
    from pythonselenium.core import session_helper

    class BaseClass(BaseCase):
        def get_new_driver(self, *args, **kwargs):
            """This method overrides get_new_driver() from BaseCase."""
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            if self.headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
            options.add_experimental_option(
                "excludeSwitches",
                ["enable-automation", "enable-logging"],
            )
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            }
            options.add_experimental_option("prefs", prefs)
            return webdriver.Chrome(options=options)

        def setUp(self):
            super().setUp()

        def base_method(self):
            pass

        def tearDown(self):
            self.save_teardown_screenshot()
            super().tearDown()

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


def test_override_fixture_no_class(ps):
    ps.load_html_file("examples/offline_examples/demo_page.html")
    ps.type("#myTextInput", "This is Automated")
    ps.set_value("input#mySlider", "100")
    ps.select_option_by_text("#mySelect", "Set to 100%")
    ps.click("#checkBox1")
    ps.drag_and_drop("img#logo", "div#drop2")
    ps.click('button:contains("Click Me")')


class TestOverride:
    def test_override_fixture_inside_class(self, ps):
        ps.load_html_file("examples/offline_examples/demo_page.html")
        ps.type("#myTextInput", "This is Automated")
        ps.set_value("input#mySlider", "100")
        ps.select_option_by_text("#mySelect", "Set to 100%")
        ps.click("#checkBox1")
        ps.drag_and_drop("img#logo", "div#drop2")
        ps.click('button:contains("Click Me")')
