
import pytest
import sys
import allure
pytestmark = [pytest.mark.my_account, pytest.mark.regression] 


@pytest.mark.testID7
@pytest.mark.xfail(reason="This test is expected to fail")
def test_my_account_page_title(browser, my_account_page):
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    # This test is expected to fail as per xfail marker
    assert "My account" in browser.title


@pytest.mark.testID8
@pytest.mark.skip(reason="This test is temporarily disabled")
@allure.title("Testing visibility of several components in my-account page")
@allure.description("This test verifies that the my-account page has the user name, password and login buttons are displayed.")
@allure.feature("Authentication")
def test_my_account_page_elements(my_account_page):
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    assert my_account_page.find_element(my_account_page.USERNAME_INPUT).is_displayed()
    assert my_account_page.find_element(my_account_page.PASSWORD_INPUT).is_displayed()
    assert my_account_page.find_element(my_account_page.LOGIN_BUTTON).is_displayed()


@pytest.mark.testID9
@pytest.mark.skipif(sys.version_info > (3, 7), reason="requires python3.7 or higher")
@allure.title("Testing conditional skip based on Python version")
@allure.description("This test demonstrates skipif functionality - will skip if Python version > 3.7")
@allure.feature("Test Control Flow")
def test_conditional_skip_example(my_account_page):
    """This test demonstrates the skipif marker functionality"""
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    # This test will be skipped if Python version is greater than 3.7
    assert my_account_page.find_element(my_account_page.USERNAME_INPUT).is_displayed()
