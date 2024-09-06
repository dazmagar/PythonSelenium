import sys

from pythonselenium import PS

# An incomplete UserAgent forces CAPTCHA-solving on macOS
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0.0.0"
if "linux" in sys.platform or "win32" in sys.platform:
    agent = None  # Use the default UserAgent

with PS(uc=True, test=True, rtf=True, agent=agent) as ps:
    url = "https://gitlab.com/users/sign_in"
    ps.uc_open_with_reconnect(url, 4)
    ps.uc_gui_click_captcha()  # Only if needed
    ps.assert_element('label[for="user_login"]')
    ps.assert_element('input[data-testid*="username"]')
    ps.assert_element('input[data-testid*="password"]')
    ps.set_messenger_theme(location="bottom_center")
    ps.post_message("PythonSelenium wasn't detected!")
