import pytest
import os
import json
from playwright.sync_api import Page
from dotenv import load_dotenv

# Page Object Model (POM) imports
from pages.login_Page import LoginPage
from pages.dashboard_Page import dashboardPage

# Service layer import handling one-time global authentication logic
from services.globalauth import globalAuth

# Automatically parse and load system environment variables from the root .env file
load_dotenv()

# Central repository path where the authenticated browser cookies/localStorage will be stored
AUTH_STATE_PATH = "data/session_state.json"


# ==========================================
# TEST SESSION LIFECYCLE HOOKS
# ==========================================

def pytest_sessionstart(session):
    """
    Pytest lifecycle hook that executes automatically ONCE before any test begins.
    Delegates authentication mechanics to our isolated services layer to generate
    a reusable browser state session file.
    """
    # Triggers the standalone automated utility function to handle the corporate login workflow
    globalAuth.generate_auth_state()


# ==========================================
# PLAYWRIGHT BROWSER CONTEXT OPTIONS
# ==========================================

@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    """
    Overrides Playwright's native browser context initialization arguments.
    Intercepts context creation per test function and automatically injects 
    the pre-saved global authentication session tokens (bypassing the login page).
    """
    if os.path.exists(AUTH_STATE_PATH):
        return {
            **browser_context_args,
            "storage_state": AUTH_STATE_PATH  # Seeds the fresh browser context with active session cookies
        }
    return browser_context_args


# ==========================================
# UNIFIED PAGE OBJECT MANAGER (CONTAINER)
# ==========================================

class basepage: 
    """
    The Master Page Object Wrapper (Page Object Manager Pattern).
    Acts as a single point of entry for all pages in the application. This prevents 
    individual test files from suffering from import bloat or redundant page instantiation.
    """
    def __init__(self, page: Page):
        self.page = page
        self.loginpage = LoginPage(page)
        self.dasboardPage = dashboardPage(page)


# ==========================================
# CORE PYTEST FIXTURES
# ==========================================

@pytest.fixture(scope="session")
def test_data():
    """
    Session-scoped fixture to cleanly load and parse the static JSON test data registry.
    Caches the payload file in memory across the entire run to optimize I/O performance.
    """
    with open("data/test_data.json") as f:
        return json.load(f)


@pytest.fixture
def app(page: Page) -> basepage:
    """
    Function-scoped fixture that instantiates and exposes the master 'basepage' container.
    Tests can request this single fixture and smoothly navigate pages via dot-notation
    (e.g., app.loginpage or app.dasboardPage).
    """
    return basepage(page)