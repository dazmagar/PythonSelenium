from pythonselenium import PS

with PS(uc=True, incognito=True, test=True) as ps:
    ps.driver.uc_open_with_reconnect("https://pixelscan.net/", 10)
    ps.remove_elements("jdiv")  # Remove chat widgets
    ps.assert_text("No automation framework detected", "pxlscn-bot-detection")
    not_masking = "You are not masking your fingerprint"
    ps.assert_text(not_masking, "pxlscn-fingerprint-masking")
    ps.highlight("span.text-success", loops=8)
    ps.sleep(1)
    ps.highlight("pxlscn-fingerprint-masking div", loops=9, scroll=False)
    ps.sleep(1)
    ps.highlight("div.bot-detection-context", loops=10, scroll=False)
    ps.sleep(2)
