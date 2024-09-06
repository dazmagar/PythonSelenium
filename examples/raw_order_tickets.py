from pythonselenium import PS

with PS(uc=True, test=True, ad_block=True) as ps:
    url = "https://www.thaiticketmajor.com/concert/"
    ps.uc_open_with_reconnect(url, 6.111)
    ps.uc_click("button.btn-signin", 4.1)
    ps.uc_gui_click_captcha()
