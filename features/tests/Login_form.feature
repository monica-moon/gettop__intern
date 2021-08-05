# Created by mun at 8/5/21
Feature: # Clicking on Account icon opens Login form
  Scenario: Login form opens when clicking on "user" icon
    Given Open Gettop page
    When Click on "USER" icon
    Then Verify log in form opens

