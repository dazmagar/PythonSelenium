<!-- PythonSelenium Docs -->

## UC Mode 👤

👤 <b>PythonSelenium</b> <b>UC Mode</b> (Undetected-Chromedriver Mode) allows bots to appear human, which lets them evade detection from anti-bot services that try to block them or trigger CAPTCHAs on various websites.

----

👤 <b>UC Mode</b> is based on [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver), but includes multiple updates, fixes, and improvements, such as:

* Automatically changing user agents to prevent detection.
* Automatically setting various chromium args as needed.
* Has special `uc_*()` methods.

👤 Here's a simple example with the <b><code>Driver</code></b> manager:

```python
from pythonselenium import Driver

driver = Driver(uc=True)
url = "https://gitlab.com/users/sign_in"
driver.uc_open_with_reconnect(url, 4)
driver.quit()
```

👤 Here's an example with the <b><code>PS</code></b> manager (which has more methods and functionality than the <b><code>Driver</code></b> format):

```python
from pythonselenium import PS

with PS(uc=True) as ps:
    url = "https://gitlab.com/users/sign_in"
    ps.uc_open_with_reconnect(url, 4)
```

(Note: If running UC Mode scripts on headless Linux machines, then you'll need to use the <b><code>PS</code></b> manager instead of the <b><code>Driver</code></b> manager because the <b><code>PS</code></b> manager includes a special virtual display that allows for <b><code>PyAutoGUI</code></b> actions.)

👤 Here's a longer example, which includes a special <b><code>PyAutoGUI</code></b> click if the CAPTCHA isn't bypassed on the initial page load:

```python
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
```

👤 Here's an example <b>where clicking the checkbox is required</b>, even for humans:<br />(Commonly seen on forms that are CAPTCHA-protected.)

```python
from pythonselenium import PS

with PS(uc=True, test=True) as ps:
    url = "https://seleniumbase.io/apps/turnstile"
    ps.uc_open_with_reconnect(url, reconnect_time=2)
    ps.uc_gui_handle_captcha()
    ps.assert_element("img#captcha-success", timeout=3)
    ps.set_messenger_theme(location="top_left")
    ps.post_message("PythonSelenium wasn't detected", duration=3)
```

If running on a Linux server, `uc_gui_handle_captcha()` might not be good enough. Switch to `uc_gui_click_captcha()` to be more stealthy. Note that these methods auto-detect between CF Turnstile and Google reCAPTCHA.

Sometimes you need to add `incognito=True` with `uc=True` to maximize your anti-detection abilities. (Some websites can detect you if you don't do that.)

👤 Here's an example <b>where the CAPTCHA appears after submitting a form</b>:

```python
from pythonselenium import PS

with PS(uc=True, test=True, incognito=True, locale_code="en") as ps:
    url = "https://ahrefs.com/website-authority-checker"
    input_field = 'input[placeholder="Enter domain"]'
    submit_button = 'span:contains("Check Authority")'
    ps.uc_open_with_reconnect(url, 2)  # The bot-check is later
    ps.type(input_field, "github.com/pythonselenium/PythonSelenium")
    ps.reconnect(0.1)
    ps.uc_click(submit_button, reconnect_time=4)
    ps.uc_gui_click_captcha()
    ps.wait_for_text_not_visible("Checking", timeout=10)
    ps.highlight('p:contains("github.com/pythonselenium/PythonSelenium")')
    ps.highlight('a:contains("Top 100 backlinks")')
    ps.set_messenger_theme(location="bottom_center")
    ps.post_message("PythonSelenium wasn't detected!")
```

👤 Here, <b>the CAPTCHA appears after clicking to go to the sign-in screen</b>:

```python
from pythonselenium import PS

with PS(uc=True, test=True, ad_block=True) as ps:
    url = "https://www.thaiticketmajor.com/concert/"
    ps.uc_open_with_reconnect(url, 6.111)
    ps.uc_click("button.btn-signin", 4.1)
    ps.uc_gui_click_captcha()
```

👤 <b>On Linux</b>, use `ps.uc_gui_click_captcha()` to handle CAPTCHAs (Cloudflare Turnstiles):

```python
from pythonselenium import PS

with PS(uc=True, test=True) as ps:
    url = "https://www.virtualmanager.com/en/login"
    ps.uc_open_with_reconnect(url, 4)
    print(ps.get_page_title())
    ps.uc_gui_click_captcha()  # Only if needed
    print(ps.get_page_title())
    ps.assert_element('input[name*="email"]')
    ps.assert_element('input[name*="login"]')
    ps.set_messenger_theme(location="bottom_center")
    ps.post_message("PythonSelenium wasn't detected!")
```

The 2nd `print()` should output "Virtual Manager", which means that the automation successfully passed the Turnstile.

--------

👤 In <b>UC Mode</b>, <code>driver.get(url)</code> has been modified from its original version: If anti-bot services are detected from a <code>requests.get(url)</code> call that's made before navigating to the website, then <code>driver.uc_open_with_reconnect(url)</code> will be used instead. To open a URL normally in <b>UC Mode</b>, use <code>driver.default_get(url)</code>.

--------

### 👤 Here are some examples that use UC Mode:
* [PythonSelenium/examples/verify_undetected.py](/examples/verify_undetected.py)
* [PythonSelenium/examples/raw_bing_captcha.py](/examples/raw_bing_captcha.py)
* [PythonSelenium/examples/raw_uc_mode.py](/examples/raw_uc_mode.py)
* [PythonSelenium/examples/raw_pixelscan.py](/examples/raw_pixelscan.py)

### 👤 Here are some UC Mode examples that bypass CAPTCHAs when clicking is required:
* [PythonSelenium/examples/raw_pyautogui.py](/examples/raw_pyautogui.py)
* [PythonSelenium/examples/raw_turnstile.py](/examples/raw_turnstile.py)
* [PythonSelenium/examples/raw_form_turnstile.py](/examples/raw_form_turnstile.py)
* [PythonSelenium/examples/uc_cdp_events.py](/examples/uc_cdp_events.py)

### 👤 Here are the <b><code>driver</code></b>-specific methods added by PythonSelenium for UC Mode: `--uc` / <b><code>uc=True</code></b>

```python
driver.uc_open(url)

driver.uc_open_with_tab(url)

driver.uc_open_with_reconnect(url, reconnect_time=None)

driver.uc_open_with_disconnect(url, timeout=None)

driver.reconnect(timeout)

driver.disconnect()

driver.connect()

driver.uc_click(
    selector, by="css selector",
    timeout=settings.SMALL_TIMEOUT, reconnect_time=None)

driver.uc_gui_press_key(key)

driver.uc_gui_press_keys(keys)

driver.uc_gui_write(text)

driver.uc_gui_click_x_y(x, y, timeframe=0.25)

driver.uc_gui_click_captcha(frame="iframe", retry=False, blind=False)
# driver.uc_gui_click_cf(frame="iframe", retry=False, blind=False)
# driver.uc_gui_click_rc(frame="iframe", retry=False, blind=False)

driver.uc_gui_handle_captcha(frame="iframe")
# driver.uc_gui_handle_cf(frame="iframe")
# driver.uc_gui_handle_rc(frame="iframe")
```

(Note that the <b><code>reconnect_time</code></b> is used to specify how long the driver should be disconnected from Chrome to prevent detection before reconnecting again.)

👤 Since <b><code>driver.get(url)</code></b> is slower in UC Mode for bypassing detection, use <b><code>driver.default_get(url)</code></b> for a standard page load instead:

```python
driver.default_get(url)  # Faster, but Selenium can be detected
```

👤 Here are some examples of using those special <b>UC Mode</b> methods: (Use <b><code>self.driver</code></b> for <b><code>BaseCase</code></b> formats. Use <b><code>ps.driver</code></b> for <b><code>PS()</code></b> formats):

```python
url = "https://gitlab.com/users/sign_in"
driver.uc_open_with_reconnect(url, reconnect_time=3)
driver.uc_open_with_reconnect(url, 3)

driver.reconnect(5)
driver.reconnect(timeout=5)
```

👤 You can also set the <b><code>reconnect_time</code></b> / <b><code>timeout</code></b> to <b><code>"breakpoint"</code></b> as a valid option. This allows the user to perform manual actions (until typing <b><code>c</code></b> and pressing <b><code>ENTER</code></b> to continue from the breakpoint):

```python
url = "https://gitlab.com/users/sign_in"
driver.uc_open_with_reconnect(url, reconnect_time="breakpoint")
driver.uc_open_with_reconnect(url, "breakpoint")

driver.reconnect(timeout="breakpoint")
driver.reconnect("breakpoint")
```

(Note that while the special <b><code>UC Mode</code></b> breakpoint is active, you can't use <b><code>Selenium</code></b> commands in the browser, and the browser can't detect <b><code>Selenium</code></b>.)

👤 On Linux, you may need to use `uc_gui_click_captcha()` to successfully bypass a Cloudflare CAPTCHA. If there's more than one Cloudflare iframe on that website, then put the CSS Selector of an element that's above the iframe as the first arg to `uc_gui_click_captcha()`. This method uses `pyautogui`. In order for `pyautogui` to focus on the correct element, use `xvfb=True` / `--xvfb` to activate a special virtual display on Linux.

👤 `uc_gui_click_captcha()` auto-detects the CAPTCHA type before trying to click it. This is a generic method for both CF Turnstile and Google reCAPTCHA. It will use the code from `uc_gui_click_cf()` and `uc_gui_click_rc()` as needed.

👤 `uc_gui_click_cf(frame="iframe", retry=False, blind=False)` has three args. (All optional). The first one, `frame`, lets you specify the selector above the iframe in case the CAPTCHA is not located in the first iframe on the page. The second one, `retry`, lets you retry the click after reloading the page if the first one didn't work (and a CAPTCHA is still present after the page reload). The third arg, `blind`, (if `True`), will retry after a page reload (if the first click failed) by clicking at the last known coordinates of the CAPTCHA checkbox without confirming first with Selenium that a CAPTCHA is still on the page.

👤 `uc_gui_click_rc(frame="iframe", retry=False, blind=False)` is for reCAPTCHA. This may only work a few times before not working anymore... not because Selenium was detected, but because reCAPTCHA uses advanced AI to detect unusual activity, unlike the CF Turnstile, which only uses basic detection.

👤 To find out if <b>UC Mode</b> will work at all on a specific site (before adjusting for timing), load your site with the following script:

```python
from pythonselenium import PS

with PS(uc=True) as ps:
    ps.uc_open_with_reconnect(URL, reconnect_time="breakpoint")
```

(If you remain undetected while loading the page and performing manual actions, then you know you can create a working script once you swap the breakpoint with a time and add special methods like <b><code>ps.uc_click</code></b> as needed.)

👤 <b>Multithreaded UC Mode:</b>

If you're using <b><code>pytest</code></b> for multithreaded <b>UC Mode</b> (which requires using one of the <b><code>pytest</code></b> [syntax formats](/help_docs/syntax_formats.md)), then all you have to do is set the number of threads when your script runs. (`-n NUM`) Eg:

```bash
pytest --uc -n 4
```

(Then <b><code>pytest-xdist</code></b> is automatically used to spin up and process the threads.)

If you don't want to use <b><code>pytest</code></b> for multithreading, then you'll need to do a little more work. That involves using a different multithreading library, (eg. <b><code>concurrent.futures</code></b>), and making sure that thread-locking is done correctly for processes that share resources. To handle that thread-locking, include <b><code>sys.argv.append("-n")</code></b> in your <b>PythonSelenium</b> file.

Here's a sample script that uses <b><code>concurrent.futures</code></b> for spinning up multiple processes:

```python
import sys
from concurrent.futures import ThreadPoolExecutor
from pythonselenium import Driver
sys.argv.append("-n")  # Tell PythonSelenium to do thread-locking as needed

def launch_driver(url):
    driver = Driver(uc=True)
    try:
        driver.get(url=url)
        driver.sleep(2)
    finally:
        driver.quit()

urls = ['https://wikipedia.org/' for i in range(3)]
with ThreadPoolExecutor(max_workers=len(urls)) as executor:
    for url in urls:
        executor.submit(launch_driver, url)
```

--------

👤 <b>What makes UC Mode work?</b>

Here are the 3 primary things that <b>UC Mode</b> does to make bots appear human:

<ul>
<li>Modifies <b><code>chromedriver</code></b> to rename <b>Chrome DevTools Console</b> variables.</li>
<li>Launches <b>Chrome</b> browsers before attaching <b><code>chromedriver</code></b> to them.</li>
<li>Disconnects <b><code>chromedriver</code></b> from <b>Chrome</b> during stealthy actions.</li>
</ul>

For example, if the <b>Chrome DevTools Console</b> variables aren't renamed, you can expect to find them easily when using <b><code>selenium</code></b> for browser automation:

(If those variables are still there, then websites can easily detect your bots.)

If you launch <b>Chrome</b> using <b><code>chromedriver</code></b>, then there will be settings that make your browser look like a bot. (Instead, <b>UC Mode</b> connects <b><code>chromedriver</code></b> to <b>Chrome</b> after the browser is launched, which makes <b>Chrome</b> look like a normal, human-controlled web browser.)

While <b><code>chromedriver</code></b> is connected to <b>Chrome</b>, website services can detect it. Thankfully, raw <b><code>selenium</code></b> already includes <b><code>driver.service.stop()</code></b> for stopping the <b><code>chromedriver</code></b> service, <b><code>driver.service.start()</code></b> for starting the <b><code>chromedriver</code></b> service, and <b><code>driver.start_session(capabilities)</code></b> for reviving the active browser session with the given capabilities. (<b><code>PythonSelenium</code> UC Mode</b> methods automatically use those raw <b><code>selenium</code></b> methods as needed.)

Links to those <a href="https://github.com/SeleniumHQ/selenium">raw <b>Selenium</b></a> method definitions have been provided for reference (but you don't need to call those methods directly):

<ul>
<li><b><code><a href="https://github.com/SeleniumHQ/selenium/blob/9c6ccdbf40356284fad342f70fbdc0afefd27bd3/py/selenium/webdriver/common/service.py#L135">driver.service.stop()</a></code></b></li>
<li><b><code><a href="https://github.com/SeleniumHQ/selenium/blob/9c6ccdbf40356284fad342f70fbdc0afefd27bd3/py/selenium/webdriver/common/service.py#L91">driver.service.start()</a></code></b></li>
<li><b><code><a href="https://github.com/SeleniumHQ/selenium/blob/9c6ccdbf40356284fad342f70fbdc0afefd27bd3/py/selenium/webdriver/remote/webdriver.py#L284">driver.start_session(capabilities)</a></code></b></li>
</ul>

Also note that <b><code>chromedriver</code></b> isn't detectable in a browser tab if it never touches that tab. Here's a JS command that lets you open a URL in a new tab (from your current tab):

<ul>
<li><b><code>window.open("URL");</code></b> --> (Info: <a href="https://www.w3schools.com/jsref/met_win_open.asp" target="_blank">W3Schools</a>)</li>
</ul>

The above JS method is used within <b><code>PythonSelenium</code></b> <b>UC Mode</b> methods for opening URLs in a stealthy way. Since some websites try to detect if your browser is a bot on the initial page load, this allows you to bypass detection in those situations. After a few seconds (customizable), <b>UC Mode</b> tells <b><code>chromedriver</code></b> to connect to that tab so that automated commands can now be issued. At that point, <b><code>chromedriver</code></b> could be detected if websites are looking for it (but generally websites only look for it during specific events, such as page loads, form submissions, and button clicks).

Avoiding detection while clicking is easy if you schedule your clicks to happen at a future point when the <b><code>chromedriver</code></b> service has been stopped. Here's a JS command that lets you schedule events (such as clicks) to happen in the future:

<li><b><code>window.setTimeout(function() { SCRIPT }, MS);</code></b> --> (Info: <a href="https://www.w3schools.com/jsref/met_win_settimeout.asp" target="_blank">W3Schools</a>)</li>

The above JS method is used within the <b><code>PythonSelenium</code></b> <b>UC Mode</b> method: <b><code>ps.uc_click(selector)</code></b> so that clicking can be done in a stealthy way. <b>UC Mode</b> schedules your click, disconnects <b><code>chromedriver</code></b> from <b>Chrome</b>, waits a little (customizable), and reconnects.

--------

🏆 <b>Choosing the right CAPTCHA service</b> for your business / website

As an ethical hacker / cybersecurity researcher who builds bots that bypass CAPTCHAs for sport, <b>the CAPTCHA service that I personally recommend</b> for keeping bots out is <b>Google's reCAPTCHA</b>

Since Google makes Chrome, Google's own <b>reCAPTCHA</b> service has access to more data than other CAPTCHA services (eg. hCaptcha, CloudFlare, DataDome, etc.), and can therefore use that data to make better decisions about whether or not web activity is coming from real humans or automated bots.

--------

⚖️ <b>Legal implications of web-scraping</b>:

Based on the following article, https://nubela.co/blog/meta-lost-the-scraping-legal-battle-to-bright-data/, (which outlines a court case where social-networking company: Meta lost the legal battle to data-scraping company: Bright Data), it was determined that web scraping is 100% legal in the eyes of the courts as long as:
1. The scraping is only done with <b>public data</b> and <b>not private data</b>.
2. The scraping isn’t done while logged in on the site being scraped.

If the above criteria are met, then scrape away! (According to the article)

(Note: I'm not a lawyer, so I can't officially offer legal advice, but I can direct people to existing articles online where people can find their own answers.)

--------
