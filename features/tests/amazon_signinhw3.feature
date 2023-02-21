Feature: Test Scenarios for logged out users see "Sign in" functionality

  Scenario: Logged out users see Sign in page when clicking returns and orders
    Given Open Amazon page
    When Click on orders icon
    Then Verify that Sign in is shown
    Then Verify that Email field is present
