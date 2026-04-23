from selenium import webdriver
import time
from page.login import loginpage
from page.product import home
import pytest
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_home(driver):
    home_page=home(driver)
    login_page=loginpage(driver)
    
    home_page.click_add_to_cart()



    