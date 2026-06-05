import asyncio
from playwright.async_api import Page

class LoginPage:
    """
    Page Object Model (POM) class representing the Authentication / Login Page interface.
    Encapsulates all web element locators and behavioral actions for the login screen.
    """
    def __init__(self, page: Page):
        self.page = page
        
        # Centralized Locator Registry: Instantiated once at runtime initialization.
        # Uses semantic Playwright locators for highly resilient element target selection.
        self.username_input = page.get_by_placeholder('Username')
        self.password_input = page.get_by_placeholder('password')
        self.loginbutton = page.get_by_role("button", name='login-button') # Changed role from 'input' to 'button' for standard validation

    # =====================================================================
    # ACTION METHODS (Atomic, Reusable Page Behaviors)
    # =====================================================================

    def navigate(self):
        """
        Directs the browser instance context to the targeted application landing URL page.
        """
        self.page.goto("https://www.saucedemo.com/")

    def loginflow(self, username: str, password: str):
        """
        Consolidates and orchestrates the complete sequential end-to-end login transaction.
        Fills out credential forms and performs the submission action.
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.loginbutton.click()