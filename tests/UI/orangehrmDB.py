import re
from playwright.sync_api import Page, expect
import pytest
from pages.orangehrm_Login_Page import LoginPage
from pages.orangehrm_Home_Page import HomePage
from utils.dbUtils import DBUtils
from utils.queries import (GET_USERS_CREDS)



def test_example(page: Page):
    users = DBUtils.fetch_user_credentials(GET_USERS_CREDS)
    for user in users:
        username=user["username"]
        password=user["password"]

        print(f"Testing with username: {username} and password: {password}")

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login(username, password)

    home_page.is_upgrade_button_visible()
    home_page.click_performance_link()
    expect(page).to_have_url(re.compile(r".*/performance.*"))
    home_page.click_dashboard_link()
    expect(page).to_have_url(re.compile(r".*/dashboard.*"))
