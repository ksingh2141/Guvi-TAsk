Feature: Zen Portal Login Functionality

  Scenario: Successful Login
    Given User launches Zen Portal
    When User enters valid username and password
    And Clicks Login button
    Then User should login successfully

  Scenario: Unsuccessful Login
    Given User launches Zen Portal
    When User enters invalid username and password
    And Clicks Login button
    Then Error message should be displayed

  Scenario: Validate Username and Password Fields
    Given User launches Zen Portal
    Then Username field should be visible
    And Password field should be visible

  Scenario: Validate Login Button
    Given User launches Zen Portal
    Then Login button should be enabled