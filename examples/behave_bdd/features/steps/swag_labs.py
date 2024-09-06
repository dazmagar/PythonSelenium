from behave import step


@step("Open the Swag Labs Login Page")
def go_to_swag_labs(context):
    ps = context.ps
    ps.open("https://www.saucedemo.com")
    ps.clear_local_storage()


@step("Login to Swag Labs with {user}")
def login_to_swag_labs(context, user):
    ps = context.ps
    ps.type("#user-name", user)
    ps.type("#password", "secret_sauce\n")


@step("Verify that the current user is logged in")
def verify_logged_in(context):
    ps = context.ps
    ps.assert_element("#header_container")
    ps.assert_element("#react-burger-menu-btn")
    ps.assert_element("#shopping_cart_container")


@step('Add "{item}" to cart')
def add_item_to_cart(context, item):
    context.ps.click('div.inventory_item:contains("%s") button[name*="add"]' % item)


@step('Save price of "{item}" to <{var}>')
def save_price_of_item(context, item, var):
    ps = context.ps
    price = ps.get_text('div.inventory_item:contains("%s") .inventory_item_price' % item)
    ps.variables[var] = price


@step('Remove "{item}" from cart')
def remove_item_to_cart(context, item):
    context.ps.click('div.inventory_item:contains("%s") button[name*="remove"]' % item)


@step("Verify shopping cart badge shows {number} item(s)")
def verify_badge_number(context, number):
    context.ps.assert_exact_text(number, "span.shopping_cart_badge")


@step("Verify shopping cart badge is missing")
def verify_badge_missing(context):
    context.ps.assert_element_not_visible("span.shopping_cart_badge")


@step("Click on shopping cart icon")
def click_shopping_cart(context):
    context.ps.click("#shopping_cart_container a")


@step("Click Checkout")
def click_checkout(context):
    context.ps.click("#checkout")


@step("Enter checkout info: {first_name}, {last_name}, {zip_code}")
def enter_checkout_info(context, first_name, last_name, zip_code):
    ps = context.ps
    ps.type("#first-name", first_name)
    ps.type("#last-name", last_name)
    ps.type("#postal-code", zip_code)


@step("Click Continue")
def click_continue(context):
    context.ps.click("input#continue")


@step('Verify {quantity} "{item}" in cart')
def verify_item_in_cart(context, quantity, item):
    context.ps.assert_exact_text(quantity, 'div.cart_item:contains("%s") div.cart_quantity' % item)


@step('Verify cost of "{item}" is <{var}>')
def verify_cost_of_item(context, item, var):
    ps = context.ps
    earlier_price = ps.variables[var]
    ps.assert_exact_text(
        earlier_price,
        'div.cart_item_label:contains("%s") .inventory_item_price' % item,
    )


@step("Verify item total is {item_total}")
def verify_item_total(context, item_total):
    context.ps.assert_text("Item total: %s" % item_total, "div.summary_subtotal_label", timeout=1)


@step("Verify tax amount is {tax_amount}")
def verify_tax_amount(context, tax_amount):
    context.ps.assert_exact_text("Tax: %s" % tax_amount, "div.summary_tax_label", timeout=1)


@step("Verify total cost is {total_cost}")
def verify_total_cost(context, total_cost):
    context.ps.assert_exact_text("Total: %s" % total_cost, "div.summary_total_label", timeout=1)


@step("Click Finish")
def click_finish(context):
    context.ps.click("button#finish")


@step("Verify order complete")
def verify_order_complete(context):
    ps = context.ps
    ps.assert_exact_text("Thank you for your order!", "h2")
    ps.assert_element('img[alt="Pony Express"]')


@step("Logout from Swag Labs")
def logout_from_swag_labs(context):
    context.ps.js_click("a#logout_sidebar_link")


@step("Verify on Login page")
def verify_on_login_page(context):
    context.ps.assert_element("#login-button")


@step("Sort items from Z to A")
def sort_items_from_z_to_a(context):
    context.ps.select_option_by_text("select.product_sort_container", "Name (Z to A)")


@step('Verify "{item}" on top')
def verify_item_on_top(context, item):
    context.ps.assert_text(item, "div.inventory_item_name")
