import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()
