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

# conftest.py

def pytest_addoption(parser):
    """
    Adds the --tcid command-line option for specifying a test case ID.
    """
    parser.addoption(
        "--tcid", action="store", default=None, help="Run test by a specific test case ID."
    )

def pytest_collection_modifyitems(config, items):
    """
    Deselects tests that do not match the --tcid option.
    """
    tcid_to_run = config.getoption("--tcid")

    # If the --tcid option is not provided, do nothing.
    if not tcid_to_run:
        return

    selected_items = []
    deselected_items = []

    for item in items:
        # Check if the test item has the 'tcid' marker
        tcid_marker = item.get_closest_marker("tcid")
        if tcid_marker:
            # Get the ID from the marker's argument
            test_case_id = tcid_marker.args[0]
            # If the test's ID matches the one we want to run, keep it.
            if test_case_id == tcid_to_run:
                selected_items.append(item)
                continue
        
        # If the test doesn't have the marker or the ID doesn't match, deselect it.
        deselected_items.append(item)
    
    # Update the list of items to run with only our selected tests.
    items[:] = selected_items