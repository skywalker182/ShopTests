from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_to_basket_button.click()

    def should_be_expected_quantity(self, expected_quantity):
         # we add only one book
        actual_quantity = self.browser.find_element(*ProductPageLocators.actual_quantity).text
        assert expected_quantity == actual_quantity, f'expected {expected_quantity}, actual {actual_quantity}'

    def should_be_expected_price(self, expected_price):
        # with price 9.99S
        actual_price = self.browser.find_element(*ProductPageLocators.actual_price)
        assert expected_price == actual_price, f"expected {expected_price}, actual {actual_price}"

    def should_be_expected_name(self, expected_name):
        # with the same name
        actual_name = self.browser.find_element(*ProductPageLocators.actual_name).text
        assert expected_name == actual_name, f"expected {expected_name}, actual {actual_name}"

    def search(self, searching_name):
        search_input =  self.browser.find_element(*MainPageLocators.SEARCH_INPUT)
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_input.send_keys(searching_name)
        search_button.click()

    def open_basket(self):
        check_basket_button = self.browser.find_element(*ProductPageLocators.check_basket_button)
        check_basket_button.click()

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_to_basket_button.click()

    def open_product(self):
        open_product_button = self.browser.find_element(*ProductPageLocators.product_img)
        open_product_button.click()

    def should_be_successful_message(self):
         assert self.is_element_present(*ProductPageLocators.successful_message), "Successful message is not presented"

    def add_product_to_fav(self):
        add_to_fav_button = self.browser.find_element(*ProductPageLocators.add_to_fav)
        add_to_fav_button .click()
