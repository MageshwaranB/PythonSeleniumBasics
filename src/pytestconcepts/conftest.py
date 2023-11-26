import time

import pytest
from selenium import webdriver

browser = "chrome"


@pytest.fixture
def getBrowser():
    return browser


@pytest.fixture
def getDriver(self, getBrowser):
    driver = None
    if getBrowser == "chrome":
        driver = webdriver.Chrome()
    elif getBrowser == "firefox":
        driver = webdriver.Firefox()
    elif getBrowser == "edge":
        driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    """A function's execution can be temporarily halted by using the yield statement, which then returns a value 
    to the caller while saving the state of the function for later resumption.
    In the below line of code, we're yielding the driver object meaning the method calling this getdriver, we will 
    execute the lines of code in getDriver but doesn't execute the quit method, the quit method only get execute the
    when the calling function is done
    """
    yield driver
    time.sleep(2)
    driver.quit()
