from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page

scenarios("../example.feature")

BASE_URL = "https://example.com"

@given("I open the example page")
def open_example(page: Page):
    page.goto(BASE_URL)

@when("I check the page title")
def check_title(page: Page):
    assert "Example Domain" in page.title()

@then("I should see the heading text")
def should_see_heading(page: Page):
    heading = page.locator("h1").text_content()
    assert heading.strip() == "Example Domain"
