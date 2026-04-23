from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from page.login import loginpage


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # required for CI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.maximize_window()

    yield driver
    driver.quit()


def test_login(driver):
    login_page = loginpage(driver)

    login_page.open_page("https://www.saucedemo.com/")

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # wait until redirected to inventory page
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url


def test_home(driver):
    # placeholder test
    assert True