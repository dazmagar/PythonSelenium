"""Use PythonSelenium methods to interact with iframes."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class FrameTests(BaseCase):
    def open_iframe_page(self):
        self.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*googlesyndication.com*", "*doubleclick.net*", "*adsafeprotected.com*", "*2mdn.net*", "*googletagmanager.com*", "*adsafeprotected.com*", "*snigelweb.com*", "*fastclick.net*", "*amazon-adsystem.com*", "*google-analytics.com*"]})
        self.execute_cdp_cmd("Network.enable", {})
        self.open("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_frameborder")
        self.assert_title("W3Schools Tryit Editor")

    def test_iframe_basics(self):
        self.open_iframe_page()
        self.click("button#runbtn")
        self.switch_to_frame("iframeResult")  # Enter the iframe
        self.assert_text("Remove the Iframe Border", "h2")
        self.switch_to_frame('[title*="Iframe"]')  # Enter iframe inside iframe
        self.assert_text("This page is displayed in an iframe", "h1")
        self.switch_to_parent_frame()  # Exit only the inner iframe
        self.assert_text("To remove the default border of the iframe, use CSS:", "p")
        self.switch_to_frame('[title*="Iframe"]')  # Enter iframe inside iframe
        self.assert_text("This page is displayed in an iframe", "h1")
        self.switch_to_default_content()  # Exit all iframes
        self.click("button#runbtn")
        self.switch_to_frame("iframeResult")  # Go back inside 1st iframe
        self.highlight('iframe[title="Iframe Example"]')

    def test_iframes_with_context_manager(self):
        self.open_iframe_page()
        self.click("button#runbtn")
        with self.frame_switch("iframeResult"):
            self.assert_text("Remove the Iframe Border", "h2")
            with self.frame_switch('[title*="Iframe"]'):
                self.assert_text("This page is displayed in an iframe", "h1")
            self.assert_text("To remove the default border of the iframe, use CSS:", "p")
            with self.frame_switch('[title*="Iframe"]'):
                self.assert_text("This page is displayed in an iframe", "h1")
        self.click("button#runbtn")
        with self.frame_switch("iframeResult"):
            self.highlight('iframe[title="Iframe Example"]')

    def test_set_content_to_frame(self):
        self.open_iframe_page()
        self.click("button#runbtn")
        self.set_content_to_frame("iframeResult")
        self.highlight('iframe[title="Iframe Example"]')
        self.set_content_to_frame("iframe")
        self.assert_element_not_visible("iframe")
        self.highlight("body")
        self.set_content_to_parent()
        self.highlight('iframe[title="Iframe Example"]')
        self.set_content_to_default()
        self.click("button#runbtn")
        self.highlight("#iframeResult")
