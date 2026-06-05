import os
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from confest import basepage  # Importing your unified manager type for hinting

# 1. Direct pytest-bdd to look for your scenarios in the feature file
scenarios('features/login.feature')

# ==========================================
# SHARED / GIVEN STEPS
# ==========================================

@given('the user navigates to the authentication page')
def navigate_to_login(basepage: basepage):
    # Fixed typo from your snippet: accessing the page via unified instance
    basepage.login_page.navigate()


# ==========================================
# WHEN STEPS
# ==========================================

@when('the user submits valid administrative credentials')
def submit_valid_credentials(basepage: basepage):
    # Fetch values safely from your system environment layer
    username = os.getenv("ENV_USER")
    password = os.getenv("ENV_PASSWORD")
    basepage.login_page.login(username, password)


@when('the user submits invalid credentials from the test registry')
def submit_invalid_credentials(basepage: basepage):
    # Leverage the JSON data loader attached directly to your master manager
    bad_user = basepage.test_data["invalid_user"]
    basepage.login_page.login(bad_user["username"], bad_user["password"])


# ==========================================
# THEN STEPS
# ==========================================

@then('the user should see the dashboard welcome message')
def verify_dashboard_visible(basepage: basepage):
    # Fixed typo from snippet: using unified manager context route
    expect(basepage.dasboardPage.welcome_message).to_be_visible()


@then('the user should see an explicit authentication error message')
def verify_error_message(basepage: basepage):
    bad_user = basepage.test_data["invalid_user"]
    expect(basepage.login_page.error_message).to_have_text(bad_user["expected_error"])