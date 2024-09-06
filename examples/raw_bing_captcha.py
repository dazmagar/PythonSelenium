from pythonselenium import PS

with PS(uc=True, test=True) as ps:
    url = "https://www.bing.com/turing/captcha/challenge"
    ps.uc_open_with_reconnect(url, 4)
    ps.uc_gui_click_captcha()
