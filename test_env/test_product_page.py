import pytest
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.test_data import ProductTestData, LoginTestData

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
        page = ProductPage(browser, link)
        main_page = MainPage(browser, link)
        page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.login(LoginTestData.email, LoginTestData.password)
        page.search(ProductTestData.expected_name)
        page.add_product_to_basket()
        page.should_be_successful_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
        page = ProductPage(browser, link)
        page.open()
        page.search(ProductTestData.expected_name)
        page.add_product_to_basket()
        page.should_be_successful_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        page = ProductPage(browser, link)
        page.open()
        page.search(ProductTestData.expected_name)
        page.open_basket()
        page.should_not_be_expected_name(ProductTestData.expected_name)

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
        page = ProductPage(browser, link)
        page.open()
        page.search(ProductTestData.expected_name)
        page.open_product()
        main_page = MainPage(browser, link)
        main_page.should_be_login_link()

@pytest.mark.need_review_custom_scenarios
def test_user_should_see_fav_button(browser):
        page = ProductPage(browser, link)
        main_page = MainPage(browser, link)
        page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.login(LoginTestData.email, LoginTestData.password)
        page.search(ProductTestData.expected_name)
        page.open_product()
        page.should_be_fav_button()