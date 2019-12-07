from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_to_basket_button.click()

    def should_not_be_expected_name(self, expected_name):
        assert self.is_not_element_present(*ProductPageLocators.expected_name), "Product is presented, but should not be"

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

    def should_be_fav_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_fav), "Add to favourite button is not presented"
