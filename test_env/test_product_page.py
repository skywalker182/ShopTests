from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        expected_quantity = '1'
        expected_price = '9,99 £'
        expected_name = "The shellcoder's handbook"
        page.search(expected_name)
        page.add_product_to_basket()
        time.sleep(3)
        page.open_basket()
        page.should_be_expected_quantity(expected_quantity)
        page.should_be_expected_price(expected_price)
        page.should_be_expected_name(expected_name)


