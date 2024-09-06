"""Testing the self.choose_file() and self.assert_attribute() methods."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class FileUploadButtonTests(BaseCase):
    def test_file_upload_button(self):
        self.open("https://cgi-lib.berkeley.edu/ex/fup.html")
        self.assert_attribute("//form", "method", "post")
        input_xpath = "input[type='file']"
        self.add_css_style(input_xpath + "{zoom: 1.6;-moz-transform: scale(1.6);}")
        self.highlight(input_xpath)
        self.choose_file(input_xpath, "examples/example_logs/basic_test_info.txt")
        self.click("input[type='submit']")
        self.highlight("h1")
        self.highlight("""p:contains("The file's contents are:")""")
