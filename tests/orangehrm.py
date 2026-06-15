import re
from playwright.sync_api import Page, expect
from pages.orangehrm_Login_Page import LoginPage
from pages.orangehrm_Home_Page import HomePage


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("Admin", "admin123")
    
    expect(home_page.upgrade_button).to_be_visible()
    home_page.click_performance_link()
    expect(page).to_have_url(re.compile(r".*/performance.*"))
    home_page.click_dashboard_link()
    expect(page).to_have_url(re.compile(r".*/dashboard.*"))
