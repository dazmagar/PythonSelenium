"""PS Manager using UC Mode for evading bot-detection."""

from pythonselenium import PS

with PS(uc=True, test=True, disable_csp=True) as ps:
    url = "https://steamdb.info/"
    ps.uc_open_with_reconnect(url, 3)
    ps.uc_click("a.header-login span", 3)
    ps.uc_gui_click_captcha()
    ps.assert_text("Sign in", "button#js-sign-in", timeout=3)
    ps.uc_click("button#js-sign-in", 2)
    ps.highlight("div.page_content form")
    ps.highlight('button:contains("Sign in")', scroll=False)
    ps.set_messenger_theme(location="top_center")
    ps.post_message("PythonSelenium wasn't detected", duration=4)
