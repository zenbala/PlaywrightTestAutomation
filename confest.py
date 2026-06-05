import pytest
import os
import json
from playwright.sync_api import Page
from dotenv import load_dotenv
from pages.login_Page import LoginPage
from pages.dashboard_Page import dashboardPage
from services.globalauth import globalAuth
load_dotenv()

AUTH_STATE_PATH = "data/session_state.json"

def pytest_sessionstart(session):
    """
    Executes automatically ONCE before any test begins.
    Calls your modular utility service function to handle authentication.
    """
    # 1. Trigger your utility function
    globalAuth.generate_auth_state()


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    """
    Automatically injects the saved session tokens generated 
    by your service function into every test case context.
    """
    if os.path.exists(AUTH_STATE_PATH):
        return {
            **browser_context_args,
            "storage_state": AUTH_STATE_PATH
        }
    return browser_context_args

class basepage: 
    def __init__(self,page: Page):
        self.page= page
        self.loginpage= LoginPage(page)
        self.dasboardPage = dashboardPage(page)

@pytest.fixture(scope="session")
def test_data():
    """Fixture to load static JSON test data."""
    with open("data/test_data.json") as f:
        return json.load(f)

# 2. Expose it as a single fixture
@pytest.fixture
def app(page: Page) -> basepage:
    return basepage(page)