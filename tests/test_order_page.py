import pytest
import allure

from helper import Helper
from pages.order_page import OrderPage
from data import DataOrderPage
from urls import Urls


class TestOrderPage:
    @allure.title(
        'Verify user can complete the order successfully.')
    @pytest.mark.parametrize(
        'name,surname,address,metro_station,phone_number,date_order,rental_period,scooter_color,comment',
        [
            [DataOrderPage.NAME_1_SET,
             DataOrderPage.SURNAME_1_SET,
             DataOrderPage.ADDRESS_1_SET,
             DataOrderPage.METRO_STATION_1_SET,
             DataOrderPage.PHONE_NUMBER_1_SET,
             Helper.generate_date_order_next_day_1_set(),
             DataOrderPage.RENTAL_PERIOD_1_SET,
             DataOrderPage.SCOOTER_COLOR_1_SET,
             DataOrderPage.COMMENT_1_SET],
            [DataOrderPage.NAME_2_SET,
             DataOrderPage.SURNAME_2_SET,
             DataOrderPage.ADDRESS_2_SET,
             DataOrderPage.METRO_STATION_2_SET,
             DataOrderPage.PHONE_NUMBER_2_SET,
             Helper.generate_date_order_in_2_weeks_2_set(),
             DataOrderPage.RENTAL_PERIOD_2_SET,
             DataOrderPage.SCOOTER_COLOR_2_SET,
             DataOrderPage.COMMENT_2_SET]
        ]
    )
    def test_complete_order(self, driver, name, surname, address, metro_station, phone_number, date_order,
                            rental_period, scooter_color, comment):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE_URL)
        order_page.fill_personal_information(name, surname, address, metro_station, phone_number)
        order_page.click_next_button()
        order_page.fill_order_information(date_order, rental_period, scooter_color, comment)
        order_page.click_complete_order_button()
        order_page.click_yes_button_confirmation_popup()
        order_page.wait_for_load_success_order_popup()
        current_heading_success_popup = order_page.check_success_popup_heading()
        assert DataOrderPage.HEADING_SUCCESS_ORDER_POPUP in current_heading_success_popup
