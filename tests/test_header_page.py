import allure

from pages.header_page import HeaderPage
from urls import Urls


class TestHeaderPage:

    @allure.title(
        'Verify that user is navigated to the "Dzen Main Page" after clicking on the "Yandex Logo" in the header on the "Main Page".')
    def test_check_redirect_yandex_logo_from_main_page_header(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_yandex_logo_header_and_switch_to_new_tab()
        header_page.wait_for_load_yandex_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.YANDEX_REDIRECT_URL

    @allure.title(
        'Verify that user is navigated to the "Dzen Main Page" after clicking on the "Yandex Logo" in the header on the "Order Page".')
    def test_check_redirect_yandex_logo_from_order_page_header(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_page(Urls.ORDER_PAGE_URL)
        header_page.wait_for_load_order_page()
        header_page.click_yandex_logo_header_and_switch_to_new_tab()
        header_page.wait_for_load_yandex_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.YANDEX_REDIRECT_URL

    @allure.title(
        'Verify that user is navigated to the "Order Page" after clicking on the "Order Button" in the header on the "Main Page".')
    def test_check_redirect_order_button_from_main_page_header(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_order_button_header()
        header_page.wait_for_load_order_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.ORDER_PAGE_URL

    @allure.title(
        'Verify that user is navigated to the "Main Page" after clicking on the "Scooter Button" in the header on the "Order Page".')
    def test_check_redirect_scooter_button_from_main_page_header(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_page(Urls.ORDER_PAGE_URL)
        header_page.wait_for_load_order_page()
        header_page.click_scooter_button_header()
        header_page.wait_for_load_main_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.MAIN_PAGE_URL
