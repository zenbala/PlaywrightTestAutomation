import asyncio
from playwright.async_api import async_playwright, Page

class dashboardPage:
    """
    Page Object Model (POM) class representing the Dashboard / Core Application Landing interface.
    Encapsulates all web element locators and behavioral actions for post-login user workflows.
    """
    def __init__(self, page: Page):
        # Bind the active browser page context instance to the class object
        self.page = page
        
        # Centralized Locator Registry: Instantiated once at runtime initialization.
        # Uses standard semantic W3C ARIA roles for high locator stability.
        self.addtocartButton = page.get_by_role("button", name='Add to cart')
        self.viewdetails = page.get_by_role("button", name='view details button')
        self.cartfeature = page.get_by_placeholder("cart")
        self.backtoshoppingbutton = page.get_by_role("button", name='back to shopping')

    # =====================================================================
    # ACTION METHODS (Atomic, Reusable Page Behaviors)
    # =====================================================================

    def dashboardAccess(self):
        """
        Executes a sequence of functional interactions on the main dashboard portal view.
        Progresses sequentially from checking details, to cart insertion, to navigating inside the cart.
        """
        self.viewdetails.click()
        self.addtocartButton.click()
        self.cartfeature.click()