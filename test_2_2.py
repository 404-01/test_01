import pytest

from selene.support.shared import browser
from selene import be, have

browser.config.hold_browser_open = True

@pytest.fixture()
def open_browser():
    browser.config.window_height = 720
    browser.config.window_width = 1280
    browser.open('https://google.com')

def test_search_site(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_nosearch_site(open_browser):
    browser.element('[name="q"]').should(be.blank).type('fdkgmifdg8sdksdfjks').press_enter()
    browser.element('[id="search"]').should(have.no.text('Other text no search'))