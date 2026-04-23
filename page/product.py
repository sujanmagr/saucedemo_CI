from selenium.webdriver.common.by import By

import time


class home:
    def __init__(self, driver):
        self.driver=driver
        self.add_to_cart=(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()