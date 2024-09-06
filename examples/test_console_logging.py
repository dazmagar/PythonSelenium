"""Use PythonSelenium methods to interact with console logs."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class TestConsoleLogging(BaseCase):
    def test_console_logging(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        self.wait_for_element_visible("h2")
        self.start_recording_console_logs()
        self.console_log_string("Hello World!")
        self.console_log_script('document.querySelector("h2").textContent')
        console_logs = [log[0] for log in self.get_recorded_console_logs()]
        self.assert_in("Hello World!", console_logs)
        self.assert_in("PythonSelenium", console_logs)
