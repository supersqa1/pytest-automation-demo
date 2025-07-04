
import pytest

pytestmark = [pytest.mark.my_account, pytest.mark.regression] 


@pytest.mark.testID6
def test_login_with_valid_credentials(my_account_page):
    my_account_page.visit("http://demostore.supersqa.com/my-account/")
    my_account_page.login("testuser20@upsersqa.com", "simplepasswordno")
    assert "Dashboard" in my_account_page.driver.page_source
