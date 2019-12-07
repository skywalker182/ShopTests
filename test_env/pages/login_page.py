from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def login(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.email_input)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.pass_input)
        pass_input.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.submit_button)
        submit_button.click()
