# Created by Edwar at 2/21/2023
Feature: Feature: Test Scenarios for users see text "Your Amazon Cart is empty" on page

    Scenario: Users see cart is empty
        Given Open Amazon page
        When Click on cart icon
        Then Verify that text Your Amazon Cart is empty is shown

