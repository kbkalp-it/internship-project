# Created by krithikabalasundar at 7/16/25
Feature: Test for changing the language

  Scenario: User is able to change the language preference
    Given Open Reelly sign-in page
    When Login to the page
    And Click on the settings option
    And Change Language to Russian
    Then Verify Language is modified