"""PS Manager using UC Mode for evading bot-detection."""

from pythonselenium import PS

with PS(uc=True, test=True) as ps:
    url = "https://gitlab.com/users/sign_in"
    ps.uc_open_with_reconnect(url, 4)
    ps.uc_gui_click_captcha()
    ps.assert_text("Username", '[for="user_login"]', timeout=3)
    ps.assert_element('label[for="user_login"]')
    ps.highlight('button:contains("Sign in")')
    ps.highlight('h1:contains("GitLab.com")')
    ps.post_message("PythonSelenium wasn't detected", duration=4)
