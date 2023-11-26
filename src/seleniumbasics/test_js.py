import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_handle_js_functions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/")
    driver.implicitly_wait(10)
    # driver.find_element(By.LINK_TEXT, "SignUp Form").click()

    print("Title of the page using javascript: " + driver.execute_script("return document.title"))

    print("URL of the page using javascript: " + driver.execute_script("return document.URL"))
    print("Is page loaded? ", driver.execute_script("return document.readyState"))

    # identifying the elements using js
    # driver.execute_script("return document.getElementById('username')").click()
    element = driver.execute_script("return document.querySelector(\"[href='/demo/signup']\")")
    # clicking the element
    driver.execute_script("arguments[0].click();", element)
    user_name=driver.find_element(By.ID, "username").text
    print("username: "+user_name)
    # entering a value
    if user_name =="":
        driver.execute_script("return document.getElementById('username').value='tester'")
        time.sleep(3)
        print("entered some input")
    #scrolling to the bottom
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
