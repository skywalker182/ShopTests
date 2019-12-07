from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEARCH_INPUT = (By.ID, "id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn")

class ProductPageLocators():
    add_to_basket_button = (By.CSS_SELECTOR, "button.btn-primary")
    check_basket_button = (By.CSS_SELECTOR, 'a.btn-default')
    actual_quantity = (By.CSS_SELECTOR, "input[name = 'form-0-quantity']")
    actual_price = (By.CSS_SELECTOR, "input[name = 'form-0-quantity']")
    actual_name = (By.CSS_SELECTOR, "div.col-sm-4 > h3 > a")


