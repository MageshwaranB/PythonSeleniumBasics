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


def test_handle_test_action():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/delay/")
    driver.find_element(By.NAME, "commit").click()
    # is_displayed,text= handle_with_hard_wait(driver)
    # print(is_displayed)
    # print(text)
    # assert is_displayed==True and text=="I am here!"

    # is_displayed, text = handle_with_explicit_wait(driver, 10)
    # print(is_displayed, " ", text)
    # assert is_displayed == True and text == "I am here!"

    print(handle_with_explicit_wait_custom_logic(driver, 6, (By.ID, "two"), "here"))


def handle_with_hard_wait(driver: WebDriver) -> Tuple[bool, str]:
    time.sleep(5)
    return driver.find_element(By.ID, "two").is_displayed(), driver.find_element(By.ID, "two").text


def handle_with_explicit_wait(driver: WebDriver, wait_for: int):
    wait = WebDriverWait(driver, wait_for)
    test = (By.ID, "two")
    ele = wait.until(expected_conditions.visibility_of_element_located(test))
    return ele.is_displayed, ele.text


def handle_with_explicit_wait_custom_logic(driver: WebDriver, wait: int, locator, text) -> (bool, str):
    return WebDriverWait(driver, wait).until(wait_till_text_appears(locator, text))


"""
Instead of using the predefined methods provided by until function, we can create our own class with our custom logic
"""


class wait_till_text_appears(object):
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    """The call special function in general used to  The main idea of __call__ method is to write a class and invoke 
    it like a function. You can refer to it as callable object.
    The most common way is defining the function body that's executed when an instance is used as a function.
    In the below call function, we are asking the call function is to find the element for the given time
    """

    def __call__(self, driver: WebDriver):
        try:
            ele = driver.find_element(*self.locator)
            return self.text in ele.text
        except TimeoutException:
            print(traceback.format_exc())
            return False


"""
Stale Element Exception
The chance of getting stale element exception is more when the dom refreshes a lot, one of the ways to handle is to use
surround the exception line with try and except block and manually rewrite the same line of code to identify those elements 
again, another way is shown below, where we have written individual action methods and asking the user to pass the 
locator every single time, in this way we avoid the use of try and except w.r.to stale element exception
"""


def test_handle_stale_element_exception():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    send_text((By.ID,"username"),driver,"Test")
    driver.refresh()
    send_text((By.ID, "username"), driver, "Test")
    send_text((By.ID, "email"), driver, "Test@test.com")
    perform_click((By.ID,"submit"),driver)
    driver.switch_to.alert.accept()
    send_text((By.ID, "username"), driver, "Test")
def perform_click(locator, driver: WebDriver):
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator)).click()

def send_text(locator,driver:WebDriver,text):
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator)).clear()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator)).send_keys(text)
