from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class HomePage(BasePage):
    MY_ACCOUNT_LINK = (By.LINK_TEXT, 'My account')
    SEARCH_INPUT = (By.NAME, 's')
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def go_to_my_account(self):
        self.find_element(self.MY_ACCOUNT_LINK).click()

    def search_product(self, product_name):
        self.find_element(self.SEARCH_INPUT).send_keys(product_name)
        self.find_element(self.SEARCH_BUTTON).send_keys(Keys.ENTER)
