from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    SEARCH_INPUT = (By.ID, "id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn")

class ProductPageLocators():
    add_to_basket_button = (By.CSS_SELECTOR, "button.btn-primary")
    check_basket_button = (By.CSS_SELECTOR, 'span > a.btn-default')
    actual_quantity = (By.CSS_SELECTOR, "input[name = 'form-0-quantity']")
    actual_price = (By.CSS_SELECTOR, "p.price_color")
    actual_name = (By.CSS_SELECTOR, "div.col-sm-4 > h3 > a")
    product_img = (By.CSS_SELECTOR, 'article > div.image_container > a > img')
    successful_message = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    add_to_fav = (By.CSS_SELECTOR, "button[type = 'submit'].btn-lg:nth-child(2)")

class LoginPageLocators():
    email_input = (By.ID, 'id_login-username')
    pass_input = (By.ID,'id_login-password')
    submit_button = (By.CSS_SELECTOR, 'button[name = "login_submit"]')

