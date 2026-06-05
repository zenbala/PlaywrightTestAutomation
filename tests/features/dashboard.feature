Feature: Dashboard and Inventory Interactions
  As an authenticated user
  I want to interact with the inventory dashboard
  So that I can manage my shopping cart metrics

  Background:
    Given the user is authenticated and enters the inventory portal

  Scenario: View dashboard performance metrics
    Then the dashboard welcome message should be visible to the user

  Scenario: Successfully add an item to the shopping cart
    When the user adds the first available product to the cart
    Then the shopping cart badge should display "1"