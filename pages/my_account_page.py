from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MyAccountPage(BasePage):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    REGISTER_LINK = (By.LINK_TEXT, 'Register')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.woocommerce-error')

    @allure.step("Entering username: {1}")
    def enter_username(self, username):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    @allure.step("Entering password")
    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step("Clicking the login button")
    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    @allure.step("Clicking the register link")
    def click_register(self):
        self.find_element(self.REGISTER_LINK).click()

    @allure.step("Getting error message")
    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    @allure.step("Logging in with username: {1}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
