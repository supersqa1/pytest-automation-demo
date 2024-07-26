from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyAccountPage(BasePage):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    REGISTER_LINK = (By.LINK_TEXT, 'Register')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.woocommerce-error')

    def enter_username(self, username):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def click_register(self):
        self.find_element(self.REGISTER_LINK).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
