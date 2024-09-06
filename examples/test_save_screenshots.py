import os

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class ScreenshotTests(BaseCase):
    def test_save_screenshot(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        # "./downloaded_files" is a special PythonSelenium folder for downloads
        self.save_screenshot("demo_page.png", folder="./downloaded_files")
        self.assert_downloaded_file("demo_page.png")
        print('\n"%s/%s" was saved!' % ("downloaded_files", "demo_page.png"))

    def test_save_screenshot_to_logs(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        self.save_screenshot_to_logs()
        # "self.log_path" is the absolute path to the "./latest_logs" folder.
        # Each test that generates log files will create a subfolder in there
        test_logpath = os.path.join(self.log_path, self.test_id)
        expected_screenshot = os.path.join(test_logpath, "_1_screenshot.png")
        self.assert_true(os.path.exists(expected_screenshot))
        print('\n"%s" was saved!' % (expected_screenshot))
