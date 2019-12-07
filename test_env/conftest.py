import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language en or ru")

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if language == "en":
        language = 'en-gb'
    elif language == "ru":
        language = 'ru'
    else:
        raise pytest.UsageError("--language should be ru or en")
