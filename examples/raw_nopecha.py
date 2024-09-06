from pythonselenium import PS

with PS(uc=True, test=True) as ps:
    ps.uc_open_with_reconnect("nopecha.com/demo/turnstile", 3.2)
    ps.uc_gui_click_captcha("#example-container0")
    ps.uc_gui_click_captcha("#example-container5")
    ps.sleep(3)
