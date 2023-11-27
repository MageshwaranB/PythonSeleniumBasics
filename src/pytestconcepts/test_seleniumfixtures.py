import pytest
import time
import traceback
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


"""
Instead of passing the fixture function name at function level, we can pass them at class level with the help of 
use-fixtures. We can even further reduce this by creating a separate class that holds this use fixture and an another
class can inherit from that
"""
@pytest.mark.usefixtures("getDriver")
class TestSauceDemo:
    """
    To avoid repetitive lines of code like setting up the driver, we can make use of fixture which will trigger
    before every test
    However, imagine a scenario, where we have to use these setup instruction in different packages and in different
    modules, then we have to keep this setup in a confttest module
    """

    def test_login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    def test_add_product(self):
        driver=self.driver
        self.test_login()  # using this test method for logining into the website
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a").click()
