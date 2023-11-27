import time

import pytest
from selenium import webdriver

browser = "chrome"

"""
If we want to accept input from the command line, then we have to make use of one pytest function called pytest_addoption(parser),
Once we have to function where it takes the value from the command line, we have to pass that value to the function
this is where we are using the request in the getBrowser function
"""


def pytest_addoption(parser):
    """
    Make use of the parser function in which we pass the cli option (--browser), what action we have to perform (store),
    and default value (chrome)
    :param parser:
    :return:
    """
    parser.addoption("--browser",action="store",default="chrome",help="Please enter the browser name")


@pytest.fixture
def getBrowser(request):
    _browser=request.config.getoption("--browser") #getting the option
    return _browser


"""Let's say we want to make use of the driver variable inside a class, it is not possible at class level Data 
members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that 
class.
We're making use of the request to make a variable at a class level
request.cls.driver - means we are making the driver variable at class level
"""


@pytest.fixture
def getDriver(request, getBrowser):
    _driver = None
    if getBrowser == "chrome":
        _driver = webdriver.Chrome()
    elif getBrowser == "firefox":
        _driver = webdriver.Firefox()
    elif getBrowser == "edge":
        _driver = webdriver.Edge()
    _driver.get("https://www.saucedemo.com/")
    _driver.maximize_window()
    _driver.implicitly_wait(10)

    """A function's execution can be temporarily halted by using the yield statement, which then returns a value 
    to the caller while saving the state of the function for later resumption.
    In the below line of code, we're yielding the driver object meaning the method calling this getdriver, we will 
    execute the lines of code in getDriver but doesn't execute the quit method, the quit method only get execute the
    when the calling function is done
    """
    request.cls.driver = _driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()
