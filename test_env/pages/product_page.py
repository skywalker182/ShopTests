from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_to_basket_button.click()

    def should_be_expected_quantity(self, expected_quantity):
         # we add only one book
        actual_quantity = self.browser.find_element(*ProductPageLocators.actual_quantity)
        assert expected_quantity == actual_quantity.text, "expected {expected_quantity}"

    def should_be_expected_price(self, expected_price):
        # with price 9.99
        expected_price = self.browser.find_element(*ProductPageLocators.actual_price)
        assert expected_price == ProductPageLocators.actual_price.text, "expected {expected_price}"

    def should_be_expected_name(self, expected_name):
        # with the same name
        expected_name = self.browser.find_element(*ProductPageLocators.actual_name)
        assert expected_name == ProductPageLocators.actual_name.text, "expected {expected_name}"

    def search(self, searching_name):
        search_input =  self.browser.find_element(*MainPageLocators.SEARCH_INPUT)
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_input.send_keys(searching_name)
        search_button.click()

    def open_basket(self):
        check_basket_button = self.browser.find_element(*ProductPageLocators.check_basket_button)

    def add_ti_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_to_basket_button.click()