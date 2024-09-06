from pythonselenium import PS

with PS(uc=True, test=True, incognito=True, locale_code="en") as ps:
    url = "https://ahrefs.com/website-authority-checker"
    input_field = 'input[placeholder="Enter domain"]'
    submit_button = 'span:contains("Check Authority")'
    ps.uc_open_with_reconnect(url, 2)  # The bot-check is later
    ps.type(input_field, "github.com/SeleniumHQ/selenium")
    ps.reconnect(0.1)
    ps.uc_click(submit_button, reconnect_time=4)
    ps.uc_gui_click_captcha()
    ps.wait_for_text_not_visible("Checking", timeout=10)
    ps.highlight('p:contains("github.com/SeleniumHQ/selenium")')
    ps.highlight('a:contains("Top 100 backlinks")')
    ps.set_messenger_theme(location="bottom_center")
    ps.post_message("PythonSelenium wasn't detected!")
