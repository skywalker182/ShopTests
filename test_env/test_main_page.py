from .pages.main_page import MainPage

@pytest.mark.need_review_custom_scenarios
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина логина

@pytest.mark.need_review_custom_scenarios
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()