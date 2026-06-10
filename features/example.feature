Feature: Example page validation
  Verify that the Playwright browser can open a basic page and inspect its title and heading.

    @smoke
  Scenario: Open example.com and verify page content
    Given I open the example page
    When I check the page title
    Then I should see the heading text
