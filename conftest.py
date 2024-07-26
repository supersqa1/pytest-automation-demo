import os
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage

@pytest.fixture(scope="module")
def browser():

    browser = os.environ.get('BROWSER', 'chrome')
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f"The requested 'browser = {browser}' is not supported.")
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def home_page(browser):
    return HomePage(browser)

@pytest.fixture(scope="module")
def my_account_page(browser):
    return MyAccountPage(browser)
