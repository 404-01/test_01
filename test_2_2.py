import pytest

from selene.support.shared import browser
from selene import be, have

@pytest.fixture()
def open_browser():
    browser.config.window_height = 480
    browser.config.window_width = 640
    browser.open('https://google.com')
    yield


def search_site(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))