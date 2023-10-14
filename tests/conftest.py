import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    chrome =  selenium.webdriver.Chrome()
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()

