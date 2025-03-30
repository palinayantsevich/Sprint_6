import allure

from pages.base_page import BasePage
from urls import Urls
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderPageLocators()

    @allure.step('Click on the "Order Button" in the page header.')
    def click_order_button_header(self):
        self.click_on_element(self.locators.ORDER_BUTTON_HEADER)

    @allure.step('Wait until the "Order Page" is loaded.')
    def wait_for_load_order_page(self):
        self.wait_load_page_by_checking_url(Urls.ORDER_PAGE_URL)

    @allure.step('Click on the "Yandex Logo" in the page header. Check the opened tab')
    def click_yandex_logo_header_and_switch_to_new_tab(self):
        self.click_on_element_and_switch_to_new_tab(self.locators.YANDEX_LOGO_HEADER)

    @allure.step('Wait until the "Dzen Main Page" is loaded.')
    def wait_for_load_yandex_page(self):
        self.wait_load_page_by_checking_url(Urls.YANDEX_REDIRECT_URL)

    @allure.step('Click on the "Scooter Button" in the page header.')
    def click_scooter_button_header(self):
        self.click_on_element(self.locators.SCOOTER_BUTTON_HEADER)

    @allure.step('Wait until the "Main Page" is loaded.')
    def wait_for_load_main_page(self):
        self.wait_load_page_by_checking_url(Urls.MAIN_PAGE_URL)
