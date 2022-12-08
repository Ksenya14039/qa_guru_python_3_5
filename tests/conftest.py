import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1800
    browser.config.window_height = 1080
    browser.config.timeout = 5.0
    yield

    browser.quit()