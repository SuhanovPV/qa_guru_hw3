from selenium.webdriver import Firefox
from pytest import fixture
from selene import browser, be, have


@fixture(scope="session")
def browser_size():
    browser.config.driver = Firefox()
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'


def test_search_with_success_result(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_without_results(browser_size):
    search_text = 'sdfkljkhrbtgl'
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(search_text).press_enter()
    browser.element('div[class="card-section"]   p').should(have.text(f'По запросу {search_text} ничего не найдено.'))
