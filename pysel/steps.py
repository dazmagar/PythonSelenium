from behave import step


def normalize_text(text):
    text = text.replace("\\\\", "\\").replace("\\t", "\t").replace("\\n", "\n")
    text = text.replace('\\"', '"').replace("\\'", "'")
    return text


@step("Open '{url}'")
@step('Open "{url}"')
@step("Open URL '{url}'")
@step('Open URL "{url}"')
@step("User opens '{url}'")
@step('User opens "{url}"')
@step("User opens URL '{url}'")
@step('User opens URL "{url}"')
@step("User goes to '{url}'")
@step('User goes to "{url}"')
@step("User goes to URL '{url}'")
@step('User goes to URL "{url}"')
def open_url(context, url):
    ps = context.ps
    ps.open(url)


@step("Click '{selector}'")
@step('Click "{selector}"')
@step("Click element '{selector}'")
@step('Click element "{selector}"')
@step("User clicks '{selector}'")
@step('User clicks "{selector}"')
@step("User clicks element '{selector}'")
@step('User clicks element "{selector}"')
def click_element(context, selector):
    ps = context.ps
    ps.click(selector)


@step("Type text '{text}' into '{selector}'")
@step('Type text "{text}" into "{selector}"')
@step("Type text '{text}' into \"{selector}\"")
@step('Type text "{text}" into \'{selector}\'')
@step("Type text '{text}' in '{selector}'")
@step('Type text "{text}" in "{selector}"')
@step("Type text '{text}' in \"{selector}\"")
@step('Type text "{text}" in \'{selector}\'')
@step("Type '{text}' into '{selector}'")
@step('Type "{text}" into "{selector}"')
@step("Type '{text}' into \"{selector}\"")
@step('Type "{text}" into \'{selector}\'')
@step("Type '{text}' in '{selector}'")
@step('Type "{text}" in "{selector}"')
@step("Type '{text}' in \"{selector}\"")
@step('Type "{text}" in \'{selector}\'')
@step("In '{selector}' type '{text}'")
@step('In "{selector}" type "{text}"')
@step("In '{selector}' type \"{text}\"")
@step('In "{selector}" type \'{text}\'')
@step("Into '{selector}' type '{text}'")
@step('Into "{selector}" type "{text}"')
@step("Into '{selector}' type \"{text}\"")
@step('Into "{selector}" type \'{text}\'')
@step("Find '{selector}' and type '{text}'")
@step('Find "{selector}" and type "{text}"')
@step("Find '{selector}' and type \"{text}\"")
@step('Find "{selector}" and type \'{text}\'')
@step("User types '{text}' in '{selector}'")
@step('User types "{text}" in "{selector}"')
@step("User types '{text}' in \"{selector}\"")
@step('User types "{text}" in \'{selector}\'')
@step("User types '{text}' into '{selector}'")
@step('User types "{text}" into "{selector}"')
@step("User types '{text}' into \"{selector}\"")
@step('User types "{text}" into \'{selector}\'')
def type_text(context, selector, text):
    ps = context.ps
    text = normalize_text(text)
    ps.type(selector, text)


@step("Add text '{text}' into '{selector}'")
@step('Add text "{text}" into "{selector}"')
@step("Add text '{text}' into \"{selector}\"")
@step('Add text "{text}" into \'{selector}\'')
@step("Add text '{text}' in '{selector}'")
@step('Add text "{text}" in "{selector}"')
@step("Add text '{text}' in \"{selector}\"")
@step('Add text "{text}" in \'{selector}\'')
@step("Add '{text}' into '{selector}'")
@step('Add "{text}" into "{selector}"')
@step("Add '{text}' into \"{selector}\"")
@step('Add "{text}" into \'{selector}\'')
@step("Add '{text}' in '{selector}'")
@step('Add "{text}" in "{selector}"')
@step("Add '{text}' in \"{selector}\"")
@step('Add "{text}" in \'{selector}\'')
@step("Into '{selector}' add '{text}'")
@step('Into "{selector}" add "{text}"')
@step("Into '{selector}' add \"{text}\"")
@step('Into "{selector}" add \'{text}\'')
@step("In '{selector}' add '{text}'")
@step('In "{selector}" add "{text}"')
@step("In '{selector}' add \"{text}\"")
@step('In "{selector}" add \'{text}\'')
@step("User adds '{text}' in '{selector}'")
@step('User adds "{text}" in "{selector}"')
@step("User adds '{text}' in \"{selector}\"")
@step('User adds "{text}" in \'{selector}\'')
@step("User adds '{text}' into '{selector}'")
@step('User adds "{text}" into "{selector}"')
@step("User adds '{text}' into \"{selector}\"")
@step('User adds "{text}" into \'{selector}\'')
def add_text(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.add_text(selector, text)


@step("Assert element '{selector}'")
@step('Assert element "{selector}"')
@step("Assert element '{selector}' is visible")
@step('Assert element "{selector}" is visible')
@step("Element '{selector}' should be visible")
@step('Element "{selector}" should be visible')
def assert_element(context, selector):
    ps = context.ps
    ps.assert_element(selector)


@step("Assert text '{text}' in '{selector}'")
@step('Assert text "{text}" in "{selector}"')
@step("Assert text '{text}' in \"{selector}\"")
@step('Assert text "{text}" in \'{selector}\'')
@step("Text in '{selector}' should contain '{text}'")
@step('Text in "{selector}" should contain "{text}"')
@step("Text in '{selector}' should contain \"{text}\"")
@step('Text in "{selector}" should contain \'{text}\'')
def assert_text_in_element(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_text(text, selector)


@step("Assert text '{text}'")
@step('Assert text "{text}"')
@step("Assert text '{text}' is visible")
@step('Assert text "{text}" is visible')
@step("Text '{text}' should be visible")
@step('Text "{text}" should be visible')
def assert_text(context, text):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_text(text)


@step("Assert exact text '{text}' in '{selector}'")
@step('Assert exact text "{text}" in "{selector}"')
@step("Assert exact text '{text}' in \"{selector}\"")
@step('Assert exact text "{text}" in \'{selector}\'')
@step("Text in '{selector}' should be '{text}'")
@step('Text in "{selector}" should be "{text}"')
@step("Text in '{selector}' should be \"{text}\"")
@step('Text in "{selector}" should be \'{text}\'')
def assert_exact_text(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_exact_text(text, selector)


@step("Assert non-empty text in '{selector}'")
@step('Assert non-empty text in "{selector}"')
@step("Assert text in '{selector}' is not empty")
@step('Assert text in "{selector}" is not empty')
@step("Text in '{selector}' should be non-empty")
@step('Text in "{selector}" should be non-empty')
@step("Text in '{selector}' should not be empty")
@step('Text in "{selector}" should not be empty')
def assert_non_empty_text(context, selector):
    ps = context.ps
    ps.assert_non_empty_text(selector)


@step("Highlight '{selector}'")
@step('Highlight "{selector}"')
@step("Highlight element '{selector}'")
@step('Highlight element "{selector}"')
@step("Use JS to highlight '{selector}'")
@step('Use JS to highlight "{selector}"')
def highlight_element(context, selector):
    ps = context.ps
    ps.highlight(selector)


@step("Click link '{link}'")
@step('Click link "{link}"')
@step("User clicks link '{link}'")
@step('User clicks link "{link}"')
def click_link(context, link):
    ps = context.ps
    ps.click_link(link)


@step("JS click '{selector}'")
@step('JS click "{selector}"')
@step("JS click element '{selector}'")
@step('JS click element "{selector}"')
@step("Use JS to click '{selector}'")
@step('Use JS to click "{selector}"')
def js_click(context, selector):
    ps = context.ps
    ps.js_click(selector)


@step("Save screenshot as '{name}'")
@step('Save screenshot as "{name}"')
@step("User saves screenshot as '{name}'")
@step('User saves screenshot as "{name}"')
def save_screenshot_as(context, name):
    ps = context.ps
    name = normalize_text(name)
    ps.save_screenshot(name)


@step("Save screenshot to '{folder}' as '{name}'")
@step('Save screenshot to "{folder}" as "{name}"')
@step("Save screenshot to '{folder}' as \"{name}\"")
@step('Save screenshot to "{folder}" as \'{name}\'')
@step("User saves screenshot to '{folder}' as '{name}'")
@step('User saves screenshot to "{folder}" as "{name}"')
@step("User saves screenshot to '{folder}' as \"{name}\"")
@step('User saves screenshot to "{folder}" as \'{name}\'')
def save_screenshot_to_folder_as(context, name, folder):
    ps = context.ps
    name = normalize_text(name)
    ps.save_screenshot(name, folder)


@step("Save screenshot to logs")
@step("Save a screenshot to the logs")
@step("User saves screenshot to logs")
@step("User saves a screenshot to the logs")
def save_screenshot_to_logs(context):
    ps = context.ps
    ps.save_screenshot_to_logs()


@step("Refresh page")
@step("Reload page")
@step("User refreshes the page")
@step("User reloads the page")
def refresh_page(context):
    ps = context.ps
    ps.refresh_page()


@step("Go back")
@step("User goes back")
@step("User navigates back")
def go_back(context):
    ps = context.ps
    ps.go_back()


@step("Go forward")
@step("User goes forward")
@step("User navigates forward")
def go_forward(context):
    ps = context.ps
    ps.go_forward()


@step("Set value of '{selector}' to '{text}'")
@step('Set value of "{selector}" to "{text}"')
@step("Set value of \"{selector}\" to '{text}'")
@step('Set value of \'{selector}\' to "{text}"')
@step("User sets value of '{selector}' to '{text}'")
@step('User sets value of "{selector}" to "{text}"')
@step("User sets value of \"{selector}\" to '{text}'")
@step('User sets value of \'{selector}\' to "{text}"')
def set_value(context, selector, text):
    ps = context.ps
    text = normalize_text(text)
    ps.set_value(selector, text)


@step("Switch to iframe '{frame}'")
@step('Switch to iframe "{frame}"')
@step("Switch to frame '{frame}'")
@step('Switch to frame "{frame}"')
@step("User switches to iframe '{frame}'")
@step('User switches to iframe "{frame}"')
@step("User switches to frame '{frame}'")
@step('User switches to frame "{frame}"')
def switch_to_frame(context, frame):
    ps = context.ps
    ps.switch_to_frame(frame)


@step("Switch to default content")
@step("Exit from iframes")
@step("Exit from frames")
@step("User switches to default content")
@step("User exits from iframes")
@step("User exits from frames")
def switch_to_default_content(context):
    ps = context.ps
    ps.switch_to_default_content()


@step("Switch to parent frame")
@step("Exit current iframe")
@step("Exit current frame")
@step("User switches to parent frame")
@step("User exits current iframe")
@step("User exits current frame")
def switch_to_parent_frame(context):
    ps = context.ps
    ps.switch_to_parent_frame()


@step("Into '{selector}' enter MFA code '{totp_key}'")
@step('Into "{selector}" enter MFA code "{totp_key}"')
@step("Into '{selector}' enter MFA code \"{totp_key}\"")
@step('Into "{selector}" enter MFA code \'{totp_key}\'')
@step("Into '{selector}' do MFA '{totp_key}'")
@step('Into "{selector}" do MFA "{totp_key}"')
@step("Into '{selector}' do MFA \"{totp_key}\"")
@step('Into "{selector}" do MFA \'{totp_key}\'')
@step("Do MFA '{totp_key}' into '{selector}'")
@step('Do MFA "{totp_key}" into "{selector}"')
@step("Do MFA \"{totp_key}\" into '{selector}'")
@step('Do MFA \'{totp_key}\' into "{selector}"')
@step("Enter MFA code '{totp_key}' into '{selector}'")
@step('Enter MFA code "{totp_key}" into "{selector}"')
@step("Enter MFA code \"{totp_key}\" into '{selector}'")
@step('Enter MFA code \'{totp_key}\' into "{selector}"')
@step("User enters MFA code '{totp_key}' into '{selector}'")
@step('User enters MFA code "{totp_key}" into "{selector}"')
@step("User enters MFA code \"{totp_key}\" into '{selector}'")
@step('User enters MFA code \'{totp_key}\' into "{selector}"')
def enter_mfa_code(context, selector, totp_key):
    ps = context.ps
    ps.enter_mfa_code(selector, totp_key)


@step("Open if not '{url}'")
@step('Open if not "{url}"')
@step("Open if not URL '{url}'")
@step('Open if not URL "{url}"')
@step("User opens '{url}' if not on page")
@step('User opens "{url}" if not on page')
@step("User opens URL '{url}' if not on page")
@step('User opens URL "{url}" if not on page')
def open_if_not_url(context, url):
    ps = context.ps
    ps.open_if_not_url(url)


@step("Select if unselected '{selector}'")
@step('Select if unselected "{selector}"')
@step("Select '{selector}' if unselected")
@step('Select "{selector}" if unselected')
@step("User selects '{selector}' if unselected")
@step('User selects "{selector}" if unselected')
def select_if_unselected(context, selector):
    ps = context.ps
    ps.select_if_unselected(selector)


@step("Unselect if selected '{selector}'")
@step('Unselect if selected "{selector}"')
@step("Unselect '{selector}' if selected")
@step('Unselect "{selector}" if selected')
@step("User unselects '{selector}' if selected")
@step('User unselects "{selector}" if selected')
def unselect_if_selected(context, selector):
    ps = context.ps
    ps.unselect_if_selected(selector)


@step("Check if unchecked '{selector}'")
@step('Check if unchecked "{selector}"')
@step("Check '{selector}' if unchecked")
@step('Check "{selector}" if unchecked')
@step("User checks '{selector}' if unchecked")
@step('User checks "{selector}" if unchecked')
def check_if_unchecked(context, selector):
    ps = context.ps
    ps.check_if_unchecked(selector)


@step("Uncheck if checked '{selector}'")
@step('Uncheck if checked "{selector}"')
@step("Uncheck '{selector}' if checked")
@step('Uncheck "{selector}" if checked')
@step("User unchecks '{selector}' if checked")
@step('User unchecks "{selector}" if checked')
def uncheck_if_checked(context, selector):
    ps = context.ps
    ps.uncheck_if_checked(selector)


@step("Drag '{drag_selector}' into '{drop_selector}'")
@step('Drag "{drag_selector}" into "{drop_selector}"')
@step("Drag '{drag_selector}' into \"{drop_selector}\"")
@step('Drag "{drag_selector}" into \'{drop_selector}\'')
@step("User drags '{drag_selector}' into '{drop_selector}'")
@step('User drags "{drag_selector}" into "{drop_selector}"')
@step("User drags '{drag_selector}' into \"{drop_selector}\"")
@step('User drags "{drag_selector}" into \'{drop_selector}\'')
def drag_and_drop(context, drag_selector, drop_selector):
    ps = context.ps
    ps.drag_and_drop(drag_selector, drop_selector)


@step("Hover '{hover_selector}' and click '{click_selector}'")
@step('Hover "{hover_selector}" and click "{click_selector}"')
@step("Hover '{hover_selector}' and click \"{click_selector}\"")
@step('Hover "{hover_selector}" and click \'{click_selector}\'')
@step("User hovers '{hover_selector}' and clicks '{click_selector}'")
@step('User hovers "{hover_selector}" and clicks "{click_selector}"')
@step("User hovers '{hover_selector}' and clicks \"{click_selector}\"")
@step('User hovers "{hover_selector}" and clicks \'{click_selector}\'')
def hover_and_click(context, hover_selector, click_selector):
    ps = context.ps
    ps.hover_and_click(hover_selector, click_selector)


@step("Find '{selector}' and select '{text}'")
@step('Find "{selector}" and select "{text}"')
@step("Find '{selector}' and select \"{text}\"")
@step('Find "{selector}" and select \'{text}\'')
@step("User selects '{text}' in '{selector}'")
@step('User selects "{text}" in "{selector}"')
@step("User selects \"{text}\" in '{selector}'")
@step('User selects \'{text}\' in "{selector}"')
@step("User finds '{selector}' and selects '{text}'")
@step('User finds "{selector}" and selects "{text}"')
@step("User finds '{selector}' and selects \"{text}\"")
@step('User finds "{selector}" and selects \'{text}\'')
def select_option_by_text(context, selector, text):
    ps = context.ps
    text = normalize_text(text)
    ps.select_option_by_text(selector, text)


@step("Find '{selector}' and select '{text}' by {option}")
@step('Find "{selector}" and select "{text}" by {option}')
@step("Find '{selector}' and select \"{text}\" by {option}")
@step('Find "{selector}" and select \'{text}\' by {option}')
@step("User finds '{selector}' and selects '{text}' by {option}")
@step('User finds "{selector}" and selects "{text}" by {option}')
@step("User finds '{selector}' and selects \"{text}\" by {option}")
@step('User finds "{selector}" and selects \'{text}\' by {option}')
def select_option_by_option(context, selector, text, option):
    ps = context.ps
    text = normalize_text(text)
    if option.startswith("'") or option.startswith('"'):
        option = option[1:]
    if option.endswith("'") or option.endswith('"'):
        option = option[:-1]
    if option == "text":
        ps.select_option_by_text(selector, text)
    elif option == "index":
        ps.select_option_by_index(selector, text)
    elif option == "value":
        ps.select_option_by_value(selector, text)
    else:
        raise Exception("Unknown option: %s" % option)


@step("Wait for '{selector}' to be visible")
@step('Wait for "{selector}" to be visible')
@step("Wait for element '{selector}'")
@step('Wait for element "{selector}"')
@step("User waits for '{selector}' to be visible")
@step('User waits for "{selector}" to be visible')
@step("User waits for element '{selector}'")
@step('User waits for element "{selector}"')
def wait_for_element(context, selector):
    ps = context.ps
    ps.wait_for_element(selector)


@step("Wait for text '{text}' in '{selector}'")
@step('Wait for text "{text}" in "{selector}"')
@step("Wait for text '{text}' in \"{selector}\"")
@step('Wait for text "{text}" in \'{selector}\'')
@step("Wait for '{selector}' to have text '{text}'")
@step('Wait for "{selector}" to have text "{text}"')
@step('Wait for "{selector}" to have text \'{text}\'')
@step("Wait for '{selector}' to have text \"{text}\"")
@step("User waits for text '{text}' in '{selector}'")
@step('User waits for text "{text}" in "{selector}"')
@step("User waits for text '{text}' in \"{selector}\"")
@step('User waits for text "{text}" in \'{selector}\'')
@step("User waits for '{selector}' to have text '{text}'")
@step('User waits for "{selector}" to have text "{text}"')
@step('User waits for "{selector}" to have text \'{text}\'')
@step("User waits for '{selector}' to have text \"{text}\"")
def wait_for_text_in_element(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.wait_for_text(text, selector)


@step("Wait for exact text '{text}' in '{selector}'")
@step('Wait for exact text "{text}" in "{selector}"')
@step("Wait for exact text '{text}' in \"{selector}\"")
@step('Wait for exact text "{text}" in \'{selector}\'')
@step("Wait for '{selector}' to have exact text '{text}'")
@step('Wait for "{selector}" to have exact text "{text}"')
@step('Wait for "{selector}" to have exact text \'{text}\'')
@step("Wait for '{selector}' to have exact text \"{text}\"")
@step("User waits for exact text '{text}' in '{selector}'")
@step('User waits for exact text "{text}" in "{selector}"')
@step("User waits for exact text '{text}' in \"{selector}\"")
@step('User waits for exact text "{text}" in \'{selector}\'')
@step("User waits for '{selector}' to have exact text '{text}'")
@step('User waits for "{selector}" to have exact text "{text}"')
@step('User waits for "{selector}" to have exact text \'{text}\'')
@step("User waits for '{selector}' to have exact text \"{text}\"")
def wait_for_exact_text_in_element(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.wait_for_exact_text(text, selector)


@step("Wait for non-empty text in '{selector}'")
@step('Wait for non-empty text in "{selector}"')
@step("Wait for '{selector}' to have non-empty text")
@step('Wait for "{selector}" to have non-empty text')
@step("User waits for non-empty text in '{selector}'")
@step('User waits for non-empty text in "{selector}"')
@step("User waits for '{selector}' to have non-empty text")
@step('User waits for "{selector}" to have non-empty text')
@step("Wait for '{selector}' to not have text")
@step('Wait for "{selector}" to not have text')
@step("Wait for text in '{selector}' to not be empty")
@step('Wait for text in "{selector}" to not be empty')
@step("User waits for '{selector}' to not have text")
@step('User waits for "{selector}" to not have text')
@step("User waits for text in '{selector}' to not be empty")
@step('User waits for text in "{selector}" to not be empty')
def wait_for_non_empty_text_in_element(context, selector):
    ps = context.ps
    ps.wait_for_non_empty_text(selector)


@step("Wait for text '{text}'")
@step('Wait for text "{text}"')
@step("User waits for text '{text}'")
@step('User waits for text "{text}"')
def wait_for_text(context, text):
    ps = context.ps
    text = normalize_text(text)
    ps.wait_for_text(text)


@step("Double click '{selector}'")
@step('Double click "{selector}"')
@step("Double click element '{selector}'")
@step('Double click element "{selector}"')
@step("User double clicks '{selector}'")
@step('User double clicks "{selector}"')
@step("User double clicks element '{selector}'")
@step('User double clicks element "{selector}"')
def double_click_element(context, selector):
    ps = context.ps
    ps.double_click(selector)


@step("Slow click '{selector}'")
@step('Slow click "{selector}"')
@step("Slow click element '{selector}'")
@step('Slow click element "{selector}"')
@step("User slow clicks '{selector}'")
@step('User slow clicks "{selector}"')
@step("User slow clicks element '{selector}'")
@step('User slow clicks element "{selector}"')
def slow_click_element(context, selector):
    ps = context.ps
    ps.slow_click(selector)


@step("Clear text field '{selector}'")
@step('Clear text field "{selector}"')
@step("Clear text in '{selector}'")
@step('Clear text in "{selector}"')
@step("User clears text field '{selector}'")
@step('User clears text field "{selector}"')
@step("User clears text in '{selector}'")
@step('User clears text in "{selector}"')
def clear_text_field(context, selector):
    ps = context.ps
    ps.clear(selector)


@step("Maximize window")
@step("Maximize the window")
@step("User maximizes window")
@step("User maximizes the window")
def maximize_window(context):
    ps = context.ps
    ps.maximize_window()


@step("Get new driver")
@step("User gets new driver")
def get_new_driver(context):
    ps = context.ps
    ps.get_new_driver()


@step("Switch to default driver")
@step("User switches to default driver")
def switch_to_default_driver(context):
    ps = context.ps
    ps.switch_to_default_driver()


@step("Press up arrow")
@step("User presses up arrow")
def press_up_arrow(context):
    ps = context.ps
    ps.press_up_arrow()


@step("Press down arrow")
@step("User presses down arrow")
def press_down_arrow(context):
    ps = context.ps
    ps.press_down_arrow()


@step("Press left arrow")
@step("User presses left arrow")
def press_left_arrow(context):
    ps = context.ps
    ps.press_left_arrow()


@step("Press right arrow")
@step("User presses right arrow")
def press_right_arrow(context):
    ps = context.ps
    ps.press_right_arrow()


@step("Clear all cookies")
@step("Delete all cookies")
@step("User clears all cookies")
@step("User deletes all cookies")
def delete_all_cookies(context):
    ps = context.ps
    ps.delete_all_cookies()


@step("Clear Local Storage")
@step("Delete Local Storage")
@step("User clears Local Storage")
@step("User deletes Local Storage")
def clear_local_storage(context):
    ps = context.ps
    ps.clear_local_storage()


@step("Clear Session Storage")
@step("Delete Session Storage")
@step("User clears Session Storage")
@step("User deletes Session Storage")
def clear_session_storage(context):
    ps = context.ps
    ps.clear_session_storage()


@step("JS click all '{selector}'")
@step('JS click all "{selector}"')
@step("Use JS to click all '{selector}'")
@step('Use JS to click all "{selector}"')
def js_click_all(context, selector):
    ps = context.ps
    ps.js_click_all(selector)


@step("Click '{selector}' at ({px},{py})")
@step('Click "{selector}" at ({px},{py})')
@step("Click '{selector}' at ({px}, {py})")
@step('Click "{selector}" at ({px}, {py})')
@step("User clicks '{selector}' at ({px},{py})")
@step('User clicks "{selector}" at ({px},{py})')
@step("User clicks '{selector}' at ({px}, {py})")
@step('User clicks "{selector}" at ({px}, {py})')
def click_with_offset(context, selector, px, py):
    ps = context.ps
    ps.click_with_offset(selector, px, py)


@step("In '{selector}' choose file '{file_path}'")
@step('In "{selector}" choose file "{file_path}"')
@step("In '{selector}' choose file \"{file_path}\"")
@step('In "{selector}" choose file \'{file_path}\'')
@step("Into '{selector}' choose file '{file_path}'")
@step('Into "{selector}" choose file "{file_path}"')
@step("Into '{selector}' choose file \"{file_path}\"")
@step('Into "{selector}" choose file \'{file_path}\'')
@step("User chooses file '{file_path}' for '{selector}'")
@step('User chooses file "{file_path}" for "{selector}" ')
@step("User chooses file \"{file_path}\" for '{selector}' ")
@step('User chooses file \'{file_path}\' for "{selector}" ')
def choose_file(context, selector, file_path):
    ps = context.ps
    ps.choose_file(selector, file_path)


@step("Set content to frame '{frame}'")
@step('Set content to frame "{frame}"')
@step("User sets content to frame '{frame}'")
@step('User sets content to frame "{frame}"')
def set_content_to_frame(context, frame):
    ps = context.ps
    ps.set_content_to_frame(frame)


@step("Set content to default")
@step("User sets content to default")
def set_content_to_default(context):
    ps = context.ps
    ps.set_content_to_default()


@step("Set content to parent")
@step("User sets content to parent")
def set_content_to_parent(context):
    ps = context.ps
    ps.set_content_to_parent()


@step("Assert element present '{selector}'")
@step('Assert element present "{selector}"')
@step("Element '{selector}' should be present")
@step('Element "{selector}" should be present')
def assert_element_present(context, selector):
    ps = context.ps
    ps.assert_element_present(selector)


@step("Assert element not visible '{selector}'")
@step('Assert element not visible "{selector}"')
@step("Element '{selector}' should not be visible")
@step('Element "{selector}" should not be visible')
def assert_element_not_visible(context, selector):
    ps = context.ps
    ps.assert_element_not_visible(selector)


@step("Assert link text '{text}'")
@step('Assert link text "{text}"')
@step("Link text '{text}' should be visible")
@step('Link text "{text}" should be visible')
def assert_link_text(context, text):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_link_text(text)


@step("Assert title '{title}'")
@step('Assert title "{title}"')
@step("The title should be '{title}'")
@step('The title should be "{title}"')
def assert_title(context, title):
    ps = context.ps
    title = normalize_text(title)
    ps.assert_title(title)


@step("Assert downloaded file '{file}'")
@step('Assert downloaded file "{file}"')
@step("File '{file}' should be in downloads")
@step('File "{file}" should be in downloads')
def assert_downloaded_file(context, file):
    ps = context.ps
    ps.assert_downloaded_file(file)


@step("Download '{file}' to downloads")
@step('Download "{file}" to downloads')
@step("Download file '{file}' to downloads")
@step('Download file "{file}" to downloads')
@step("User downloads '{file}' to downloads")
@step('User downloads "{file}" to downloads')
def download_file(context, file):
    ps = context.ps
    ps.download_file(file)


@step("Download '{file}' to '{destination}'")
@step('Download "{file}" to "{destination}"')
@step("Download file '{file}' to '{destination}'")
@step('Download file "{file}" to "{destination}"')
@step("User downloads '{file}' to '{destination}'")
@step('User downloads "{file}" to "{destination}"')
def download_file_to_destination(context, file, destination):
    ps = context.ps
    ps.download_file(file, destination)


@step("In '{selector}' assert attribute \'{attribute}\'")
@step('In "{selector}" assert attribute \"{attribute}\"')
@step("In \"{selector}\" assert attribute '{attribute}'")
@step('In \'{selector}\' assert attribute "{attribute}"')
def assert_attribute(context, selector, attribute):
    ps = context.ps
    ps.assert_attribute(selector, attribute)


@step("In '{selector}' assert attribute/value '{attribute}'/'{value}'")
@step('In "{selector}" assert attribute/value "{attribute}"/"{value}"')
@step("In \"{selector}\" assert attribute/value '{attribute}'/\"{value}\"")
@step('In \'{selector}\' assert attribute/value "{attribute}"/\'{value}\'')
@step("In '{selector}' assert attribute/value '{attribute}'/\"{value}\"")
@step('In "{selector}" assert attribute/value "{attribute}"/\'{value}\'')
@step("In \"{selector}\" assert attribute/value '{attribute}'/'{value}'")
@step('In \'{selector}\' assert attribute/value "{attribute}"/"{value}"')
def assert_attribute_has_value(context, selector, attribute, value):
    ps = context.ps
    value = normalize_text(value)
    ps.assert_attribute(selector, attribute, value)


@step("Show file choosers")
@step("Show hidden file choosers")
@step("Use JS to show file choosers")
@step("Use JS to show hidden file choosers")
def show_file_choosers(context):
    ps = context.ps
    ps.show_file_choosers()


@step("Sleep for {seconds} seconds")
@step("Wait for {seconds} seconds")
@step("User sleeps for {seconds} seconds")
@step("User waits for {seconds} seconds")
def sleep(context, seconds):
    ps = context.ps
    ps.sleep(float(seconds))


@step("Activate Demo Mode")
@step("User activates Demo Mode")
def activate_demo_mode(context):
    ps = context.ps
    ps.activate_demo_mode()


@step("Deactivate Demo Mode")
@step("User deactivates Demo Mode")
def deactivate_demo_mode(context):
    ps = context.ps
    ps.deactivate_demo_mode()


@step("Deferred assert element '{selector}'")
@step('Deferred assert element "{selector}"')
def deferred_assert_element(context, selector):
    ps = context.ps
    ps.deferred_assert_element(selector)


@step("Deferred assert element present '{selector}'")
@step('Deferred assert element present "{selector}"')
def deferred_assert_element_present(context, selector):
    ps = context.ps
    ps.deferred_assert_element_present(selector)


@step("Deferred assert text '{text}' in '{selector}'")
@step('Deferred assert text "{text}" in "{selector}"')
@step("Deferred assert text '{text}' in \"{selector}\"")
@step('Deferred assert text "{text}" in \'{selector}\'')
def deferred_assert_text_in_element(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.deferred_assert_text(text, selector)


@step("Deferred assert text '{text}'")
@step('Deferred assert text "{text}"')
def deferred_assert_text(context, text):
    ps = context.ps
    text = normalize_text(text)
    ps.deferred_assert_text(text)


@step("Deferred assert exact text '{text}' in '{selector}'")
@step('Deferred assert exact text "{text}" in "{selector}"')
@step("Deferred assert exact text '{text}' in \"{selector}\"")
@step('Deferred assert exact text "{text}" in \'{selector}\'')
def deferred_assert_exact_text(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.deferred_assert_exact_text(text, selector)


@step("Deferred assert non-empty text in '{selector}'")
@step('Deferred assert non-empty text in "{selector}"')
def deferred_assert_non_empty_text(context, selector):
    ps = context.ps
    ps.deferred_assert_non_empty_text(selector)


@step("Process deferred asserts")
def process_deferred_asserts(context):
    ps = context.ps
    ps.process_deferred_asserts()


@step("Assert text not visible '{text}' in '{selector}'")
@step('Assert text not visible "{text}" in "{selector}"')
@step("Assert text not visible '{text}' in \"{selector}\"")
@step('Assert text not visible "{text}" in \'{selector}\'')
@step("Text '{text}' should not be visible in '{selector}'")
@step('Text "{text}" should not be visible in "{selector}"')
@step("Text '{text}' should not be visible in \"{selector}\"")
@step('Text "{text}" should not be visible in \'{selector}\'')
def assert_text_not_visible_in_element(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_text_not_visible(text, selector)


@step("Assert text not visible '{text}'")
@step('Assert text not visible "{text}"')
@step("Text '{text}' should not be visible")
@step('Text "{text}" should not be visible')
def assert_text_not_visible(context, text):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_text_not_visible(text)


@step("Assert exact text not visible '{text}' in '{selector}'")
@step('Assert exact text not visible "{text}" in "{selector}"')
@step("Assert exact text not visible '{text}' in \"{selector}\"")
@step('Assert exact text not visible "{text}" in \'{selector}\'')
@step("Exact text '{text}' should not be visible in '{selector}'")
@step('Exact text "{text}" should not be visible in "{selector}"')
@step("Exact text '{text}' should not be visible in \"{selector}\"")
@step('Exact text "{text}" should not be visible in \'{selector}\'')
def assert_exact_text_not_visible_in_element(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_exact_text_not_visible(text, selector)


@step("Assert exact text not visible '{text}'")
@step('Assert exact text not visible "{text}"')
@step("Exact text '{text}' should not be visible")
@step('Exact text "{text}" should not be visible')
def assert_exact_text_not_visible(context, text):
    ps = context.ps
    text = normalize_text(text)
    ps.assert_exact_text_not_visible(text)


@step("Assert title contains '{substring}'")
@step('Assert title contains "{substring}"')
@step("The title should contain '{substring}'")
@step('The title should contain "{substring}"')
def assert_title_contains(context, substring):
    ps = context.ps
    substring = normalize_text(substring)
    ps.assert_title_contains(substring)


@step("Open new tab")
@step("Open new window")
@step("User opens new tab")
@step("User opens new window")
def open_new_window(context):
    ps = context.ps
    ps.open_new_window()


@step("Accept alert")
@step("User accepts alert")
def accept_alert(context):
    ps = context.ps
    ps.accept_alert()


@step("Dismiss alert")
@step("User dismisses alert")
def dismiss_alert(context):
    ps = context.ps
    ps.dismiss_alert()


@step("Assert URL '{url}'")
@step('Assert URL "{url}"')
@step("The URL should be '{url}'")
@step('The URL should be "{url}"')
def assert_url(context, url):
    ps = context.ps
    url = normalize_text(url)
    ps.assert_url(url)


@step("Assert URL contains '{substring}'")
@step('Assert URL contains "{substring}"')
@step("The URL should contain '{substring}'")
@step('The URL should contain "{substring}"')
def assert_url_contains(context, substring):
    ps = context.ps
    substring = normalize_text(substring)
    ps.assert_url_contains(substring)


@step("Hover '{selector}'")
@step('Hover "{selector}"')
@step("Hover over '{selector}'")
@step('Hover over "{selector}"')
@step("Hover element '{selector}'")
@step('Hover element "{selector}"')
@step("User hovers over '{selector}'")
@step('User hovers over "{selector}"')
@step("User hovers over element '{selector}'")
@step('User hovers over element "{selector}"')
def hover(context, selector):
    ps = context.ps
    ps.hover(selector)


@step("Context click '{selector}'")
@step('Context click "{selector}"')
@step("Context click element '{selector}'")
@step('Context click element "{selector}"')
@step("Right click '{selector}'")
@step('Right click "{selector}"')
@step("Right click element '{selector}'")
@step('Right click element "{selector}"')
@step("User right clicks '{selector}'")
@step('User right clicks "{selector}"')
@step("User right clicks element '{selector}'")
@step('User right clicks element "{selector}"')
def context_click(context, selector):
    ps = context.ps
    ps.context_click(selector)


@step("JS type '{text}' in '{selector}'")
@step('JS type "{text}" in "{selector}"')
@step("JS type '{text}' in \"{selector}\"")
@step('JS type "{text}" in \'{selector}\'')
@step("JS type '{text}' into '{selector}'")
@step('JS type "{text}" into "{selector}"')
@step("JS type '{text}' into \"{selector}\"")
@step('JS type "{text}" into \'{selector}\'')
@step("JS type text '{text}' in '{selector}'")
@step('JS type text "{text}" in "{selector}"')
@step("JS type text '{text}' in \"{selector}\"")
@step('JS type text "{text}" in \'{selector}\'')
@step("JS type text '{text}' into '{selector}'")
@step('JS type text "{text}" into "{selector}"')
@step("JS type text '{text}' into \"{selector}\"")
@step('JS type text "{text}" into \'{selector}\'')
@step("Use JS to type '{text}' in '{selector}'")
@step('Use JS to type "{text}" in "{selector}"')
@step("Use JS to type '{text}' in \"{selector}\"")
@step('Use JS to type "{text}" in \'{selector}\'')
@step("Use JS to type '{text}' into '{selector}'")
@step('Use JS to type "{text}" into "{selector}"')
@step("Use JS to type '{text}' into \"{selector}\"")
@step('Use JS to type "{text}" into \'{selector}\'')
def js_type(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.js_type(selector, text)


@step("jQuery click '{selector}'")
@step('jQuery click "{selector}"')
@step("jQuery click element '{selector}'")
@step('jQuery click element "{selector}"')
@step("Use jQuery to click '{selector}'")
@step('Use jQuery to click "{selector}"')
def jquery_click(context, selector):
    ps = context.ps
    ps.jquery_click(selector)


@step("jQuery click all '{selector}'")
@step('jQuery click all "{selector}"')
@step("Use jQuery to click all '{selector}'")
@step('Use jQuery to click all "{selector}"')
def jquery_click_all(context, selector):
    ps = context.ps
    ps.jquery_click_all(selector)


@step("jQuery type '{text}' in '{selector}'")
@step('jQuery type "{text}" in "{selector}"')
@step("jQuery type '{text}' in \"{selector}\"")
@step('jQuery type "{text}" in \'{selector}\'')
@step("jQuery type '{text}' into '{selector}'")
@step('jQuery type "{text}" into "{selector}"')
@step("jQuery type '{text}' into \"{selector}\"")
@step('jQuery type "{text}" into \'{selector}\'')
@step("jQuery type text '{text}' in '{selector}'")
@step('jQuery type text "{text}" in "{selector}"')
@step("jQuery type text '{text}' in \"{selector}\"")
@step('jQuery type text "{text}" in \'{selector}\'')
@step("jQuery type text '{text}' into '{selector}'")
@step('jQuery type text "{text}" into "{selector}"')
@step("jQuery type text '{text}' into \"{selector}\"")
@step('jQuery type text "{text}" into \'{selector}\'')
@step("Use jQuery to type '{text}' in '{selector}'")
@step('Use jQuery to type "{text}" in "{selector}"')
@step("Use jQuery to type '{text}' in \"{selector}\"")
@step('Use jQuery to type "{text}" in \'{selector}\'')
@step("Use jQuery to type '{text}' into '{selector}'")
@step('Use jQuery to type "{text}" into "{selector}"')
@step("Use jQuery to type '{text}' into \"{selector}\"")
@step('Use jQuery to type "{text}" into \'{selector}\'')
def jquery_type(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.jquery_type(selector, text)


@step("Press keys '{text}' in '{selector}'")
@step('Press keys "{text}" in "{selector}"')
@step("Press keys '{text}' in \"{selector}\"")
@step('Press keys "{text}" in \'{selector}\'')
@step("Press keys '{text}' into '{selector}'")
@step('Press keys "{text}" into "{selector}"')
@step("Press keys '{text}' into \"{selector}\"")
@step('Press keys "{text}" into \'{selector}\'')
@step("In '{selector}' press keys '{text}'")
@step('In "{selector}" press keys "{text}"')
@step("In '{selector}' press keys \"{text}\"")
@step('In "{selector}" press keys \'{text}\'')
@step("Into '{selector}' press keys '{text}'")
@step('Into "{selector}" press keys "{text}"')
@step("Into '{selector}' press keys \"{text}\"")
@step('Into "{selector}" press keys \'{text}\'')
@step("Find '{selector}' and press keys '{text}'")
@step('Find "{selector}" and press keys "{text}"')
@step("Find '{selector}' and press keys \"{text}\"")
@step('Find "{selector}" and press keys \'{text}\'')
@step("User presses keys '{text}' in '{selector}'")
@step('User presses keys "{text}" in "{selector}"')
@step("User presses keys '{text}' in \"{selector}\"")
@step('User presses keys "{text}" in \'{selector}\'')
@step("User presses keys '{text}' into '{selector}'")
@step('User presses keys "{text}" into "{selector}"')
@step("User presses keys '{text}' into \"{selector}\"")
@step('User presses keys "{text}" into \'{selector}\'')
def press_keys(context, text, selector):
    ps = context.ps
    text = normalize_text(text)
    ps.press_keys(selector, text)


@step("Find '{selector}' and set {attribute} to '{value}'")
@step('Find "{selector}" and set {attribute} to "{value}"')
@step("Find '{selector}' and set {attribute} to \"{value}\"")
@step('Find "{selector}" and set {attribute} to \'{value}\'')
def set_attribute(context, selector, attribute, value):
    ps = context.ps
    value = normalize_text(value)
    if attribute.startswith("'") or attribute.startswith('"'):
        attribute = attribute[1:]
    if attribute.endswith("'") or attribute.endswith('"'):
        attribute = attribute[:-1]
    ps.set_attribute(selector, attribute, value)


@step("Find all '{selector}' and set {attribute} to '{value}'")
@step('Find all "{selector}" and set {attribute} to "{value}"')
@step("Find all '{selector}' and set {attribute} to \"{value}\"")
@step('Find all "{selector}" and set {attribute} to \'{value}\'')
def set_attributes(context, selector, attribute, value):
    ps = context.ps
    value = normalize_text(value)
    if attribute.startswith("'") or attribute.startswith('"'):
        attribute = attribute[1:]
    if attribute.endswith("'") or attribute.endswith('"'):
        attribute = attribute[:-1]
    ps.set_attributes(selector, attribute, value)
