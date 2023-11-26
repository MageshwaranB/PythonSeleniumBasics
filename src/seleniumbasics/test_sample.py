import time

from selenium import webdriver
from selenium.webdriver.common.by import By


"""
We created a class Test_Selenium, and declared driver variable
test_go_page will start first and once it gets complete, it will test_signup"""

class Test_Selenium:
    driver = None


def test_go_page():
    Test_Selenium.driver = webdriver.Chrome()
    Test_Selenium.driver.maximize_window()
    Test_Selenium.driver.implicitly_wait(10)
    Test_Selenium.driver.get("https://qavbox.github.io/demo/")
    assert "QAVBOX" in Test_Selenium.driver.title



def test_signup():
    Test_Selenium.driver.find_element(By.LINK_TEXT, "SignUp Form").click()
    Test_Selenium.driver.save_screenshot(r"C:\Users\mages\PycharmProjects\PythonSeleniumBasics\src\Screenshots\screen.png")
    time.sleep(3)
    Test_Selenium.driver.quit()

"""To export the required libraries use
    pip freeze > filename.txt
We're mainly using this to avoid the libraries getting downloading during cloning the repository since that'll
occupy a lot of space, so the person who clones the repo, can simply clone project without needing to
download libraries. Once cloned, we can import the libraries present in the requirements.txt by using 
pip install -r requirements.txt"""
