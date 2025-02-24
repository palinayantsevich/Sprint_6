import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import DataBasePage


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Click on element: {locator}.')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Wait until the element is displayed: {locator}.')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, DataBasePage.WAIT_TIME).until(EC.visibility_of_element_located(locator))

    @allure.step('Wait until the element is clickable: {locator}.')
    def wait_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, DataBasePage.WAIT_TIME).until(EC.element_to_be_clickable(locator))

    @allure.step('Wait until the page is loaded and check page url: {url}.')
    def wait_load_page_by_checking_url(self, url):
        return WebDriverWait(self.driver, DataBasePage.WAIT_TIME).until(EC.url_to_be(url))

    @allure.step('Get current page url.')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Scroll to the element: {locator}.')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Get text of the element: {locator}.')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Fill the input field {locator} with value: {text}.')
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Open page: {url}.')
    def open_page(self, url):
        self.driver.get(url)

    def click_on_element_and_switch_to_new_tab(self, locator):
        original_window = self.driver.current_window_handle
        self.click_on_element(locator)
        WebDriverWait(self.driver, DataBasePage.WAIT_TIME).until(
            EC.number_of_windows_to_be(DataBasePage.NUMBER_OF_WINDOWS))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def create_action_chain_object(self):
        action = ActionChains(self.driver)
        return action
