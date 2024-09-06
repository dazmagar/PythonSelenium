from pythonselenium import PS

with PS(enable_3d_apis=True, test=True) as ps:
    ps.open("threejs.org/examples/#webgl_animation_skinning_morph")
    iframe = ps.locator("iframe#viewer")
    ps.switch_to_frame(iframe)
    ps.set_text_content("#info p", "Hi")
    ps.add_css_style("#info p{zoom: 2.54}")
    ps.sleep(0.8)
    ps.click('button:contains("Wave")')
    ps.highlight("#info p")
    ps.select_option_by_text("select", "Idle")
    ps.click('button:contains("ThumbsUp")')
    ps.set_text_content("#info p", "How are you?")
    ps.highlight("#info p")
    ps.sleep(0.8)
    ps.click('button:contains("Jump")')
    ps.sleep(1.5)
