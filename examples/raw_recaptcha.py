from pythonselenium import PS

with PS(uc=True, test=True) as ps:
    url = "https://www.google.com/recaptcha/api2/demo"
    ps.uc_open_with_reconnect(url)
    ps.uc_gui_handle_captcha()  # Try with TAB + SPACEBAR
    ps.assert_element("span[class*='recaptcha-checkbox-checked']", timeout=3)
    ps.set_messenger_theme(location="top_left")
    ps.post_message("PythonSelenium wasn't detected", duration=3)

with PS(uc=True, test=True) as ps:
    url = "https://www.google.com/recaptcha/api2/demo"
    ps.uc_open_with_reconnect(url)
    ps.uc_gui_click_captcha()  # Try with PyAutoGUI Click
    ps.assert_element("span[class*='recaptcha-checkbox-checked']", timeout=3)
    ps.set_messenger_theme(location="top_left")
    ps.post_message("PythonSelenium wasn't detected", duration=3)
