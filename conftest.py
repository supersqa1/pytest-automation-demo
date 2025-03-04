import os
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage
from config.config import Config

# Validate required environment variables before tests start
def pytest_configure(config):
    Config.validate()

@pytest.fixture(scope="module")
def browser():
    if Config.BROWSER.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        if Config.HEADLESS:
            options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif Config.BROWSER.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception(f"The requested browser '{Config.BROWSER}' is not supported.")
    
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_config():
    """Fixture to provide API configuration"""
    return {
        'url': Config.WC_URL,
        'consumer_key': Config.WC_CONSUMER_KEY,
        'consumer_secret': Config.WC_CONSUMER_SECRET,
        'timeout': Config.API_TIMEOUT
    }

@pytest.fixture(scope="module")
def home_page(browser):
    return HomePage(browser)

@pytest.fixture(scope="module")
def my_account_page(browser):
    return MyAccountPage(browser)
