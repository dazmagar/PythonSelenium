"""Test double_click() after switching into iframes."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class DoubleClickTests(BaseCase):
    def login_w3school(self):
        self.execute_cdp_cmd(
            "Network.setBlockedURLs",
            {
                "urls": [
                    "*googlesyndication.com*",
                    "*doubleclick.net*",
                    "*adsafeprotected.com*",
                    "*2mdn.net*",
                    "*googletagmanager.com*",
                    "*adsafeprotected.com*",
                    "*snigelweb.com*",
                    "*fastclick.net*",
                    "*amazon-adsystem.com*",
                    "*google-analytics.com*",
                ]
            },
        )
        self.execute_cdp_cmd("Network.enable", {})
        self.open("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
        self.assert_title("W3Schools Tryit Editor")

    def test_switch_to_frame_and_double_click(self):
        self.login_w3school()
        self.click("button#runbtn")
        self.switch_to_frame("iframe#iframeResult")
        self.double_click('[ondblclick="myFunction()"]')
        self.assert_text("Hello World", "#demo")

    def test_switch_to_frame_of_element_and_double_click(self):
        self.login_w3school()
        self.click("button#runbtn")
        self.switch_to_frame_of_element('[ondblclick="myFunction()"]')
        self.double_click('[ondblclick="myFunction()"]')
        self.assert_text("Hello World", "#demo")
