
import pytest

pytestmark = [pytest.mark.home_page, pytest.mark.regression] 

@pytest.mark.testID1
@pytest.mark.smoke
def test_home_page_title(browser, home_page):
    home_page.visit("http://demostore.supersqa.com")
    assert 'Demo eCom Store – Just another WordPress site' == browser.title

@pytest.mark.testID2
def test_navigation_to_my_account(home_page):
    home_page.visit("http://demostore.supersqa.com")
    home_page.go_to_my_account()
    assert "My account" in home_page.driver.title

@pytest.mark.testID3
@pytest.mark.smoke
def test_search_product(home_page):
    home_page.visit("http://demostore.supersqa.com")
    home_page.search_product("T-shirt")
    assert 'Search results: “T-shirt”' in home_page.driver.page_source

@pytest.mark.testID4
def test_home_page_elements(home_page):
    home_page.visit("http://demostore.supersqa.com")
    assert home_page.find_element(home_page.MY_ACCOUNT_LINK).is_displayed()
    assert home_page.find_element(home_page.SEARCH_INPUT).is_displayed()
    assert home_page.find_element(home_page.SEARCH_BUTTON).is_displayed()
