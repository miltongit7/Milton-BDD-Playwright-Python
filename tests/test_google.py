import re  #re is used for regular expression operations
from playwright.sync_api import expect #expect is used for making assertions in Playwright tests


def test_google(page):
    page.wait_for_timeout(1000)
    page.goto("https://www.google.com/")
    expect(page).to_have_title(re.compile("Google"))
    page.get_by_role("combobox", name="Search").fill("Playwright")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))