"""Test that PythonSelenium can autodetect and use xpath selectors."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class XPathTests(BaseCase):
    def test_xpath(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        self.assert_element('//h1[(text()="Demo Page")]')
        self.type('//*[@id="myTextInput"]', "XPath Test!")
        self.click('//button[starts-with(text(),"Click Me")]')
        self.assert_element('//button[contains(., "Purple")]')
        self.assert_text("PythonSelenium", "//table/tbody/tr[1]/td[2]/h2")
