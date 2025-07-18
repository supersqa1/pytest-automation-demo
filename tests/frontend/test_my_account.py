
import pytest
import sys
pytestmark = [pytest.mark.my_account, pytest.mark.regression] 



@pytest.mark.testID5
@pytest.mark.skip
def test_login_with_valid_credentials(my_account_page):
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    my_account_page.login("testuser20@upsersqa.com", "simplepasswordno")
    my_account_page.login("testuser20@upsersqa.com", "simplepasswordno")
    assert "Dashboard" in my_account_page.driver.page_source

@pytest.mark.testID6
@pytest.mark.skipif(sys.version_info > (3, 7), reason="requires python3.7 or higher")
def test_login_with_invalid_credentials(my_account_page):
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    my_account_page.login("invalid_username", "invalid_password")
    assert "Error: The username invalid_username is not registered on this site" in my_account_page.get_error_message()


@pytest.mark.testID7
@pytest.mark.xfail(reason="This test is expected to fail")
def test_my_account_page_title(browser, my_account_page):
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    assert "My account" in browser.title


@pytest.mark.testID8
def test_my_account_page_elements(my_account_page):
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    assert my_account_page.find_element(my_account_page.USERNAME_INPUT).is_displayed()
    assert my_account_page.find_element(my_account_page.PASSWORD_INPUT).is_displayed()
    assert my_account_page.find_element(my_account_page.LOGIN_BUTTON).is_displayed()
