Feature: User Authentication Flow
  As a registered user
  I want to authenticate securely into the application
  So that I can access my dashboard metrics

  Scenario: Successful login with valid credentials
    Given the user navigates to the authentication page
    When the user submits valid administrative credentials
    Then the user should see the dashboard welcome message

  Scenario: Failed login with invalid credentials
    Given the user navigates to the authentication page
    When the user submits invalid credentials from the test registry
    Then the user should see an explicit authentication error message