from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from confest import basepage  # Type hinting tracking

# 1. Direct pytest-bdd to look for your scenarios in the feature file
scenarios('features/dashboard.feature')

# ==========================================
# BACKGROUND / GIVEN STEPS
# ==========================================

@given('the user is authenticated and enters the inventory portal')
def navigate_to_dashboard(basePage: basepage):
    # Navigates directly to the internal inventory page.
    # Cookies from data/session_state.json are injected automatically via conftest!
    basePage.page.goto("https://www.saucedemo.com/inventory.html")


# ==========================================
# WHEN STEPS
# ==========================================

@when('the user adds the first available product to the cart')
def add_item_to_cart(basePage: basepage):
    basePage.dashboard.add_first_item_to_cart()


# ==========================================
# THEN STEPS
# ==========================================

@then('the dashboard welcome message should be visible to the user')
def verify_welcome_message(basePage: basepage):
    expect(basePage.dashboard.welcome_message).to_be_visible()


@then('the shopping cart badge should display "1"')
def verify_cart_badge_count(basePage: basepage):
    expect(basePage.dashboard.cart_badge).to_have_text("1")