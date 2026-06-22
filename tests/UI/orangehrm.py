import re
from playwright.sync_api import Page, expect
import pytest
from pages.orangehrm_Login_Page import LoginPage
from pages.orangehrm_Home_Page import HomePage
from utils.csvReader import CSVReader

# Parametrize with dict rows to tolerate changing CSV headers
_rows = CSVReader.read_csv("testData/testData.csv")
_ids = [r.get("test_name") or "@".join([str(v) for v in r.values()]) for r in _rows]

@pytest.mark.parametrize("row", _rows, ids=_ids)
def test_example(page: Page, row: dict) -> None:
    username = row.get("username")
    uid=row.get("UID")
    password = row.get("password") 
    pwd=row.get("PWD")
    print(f"Running test with UID: {username},{uid} PWD: {password} {pwd}")

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login(uid, pwd)

    home_page.is_upgrade_button_visible()
    home_page.click_performance_link()
    expect(page).to_have_url(re.compile(r".*/performance.*"))
    home_page.click_dashboard_link()
    expect(page).to_have_url(re.compile(r".*/dashboard.*"))
