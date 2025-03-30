import allure
from selenium.webdriver import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def set_metro_station(self, metro_station):
        self.fill_input(self.locators.METRO_FIELD, metro_station)
        self.wait_element_is_clickable(self.locators.build_metro_station_and_rental_period_locator(metro_station))
        self.click_on_element(self.locators.build_metro_station_and_rental_period_locator(metro_station))

    def set_date_order(self, date_order):
        self.fill_input(self.locators.DATE_ORDER_FIELD, date_order)
        action = self.create_action_chain_object()
        action.send_keys(Keys.ENTER).perform()

    def set_rental_period(self, rental_period):
        self.click_on_element(self.locators.RENTAL_PERIOD_FIELD)
        element = self.find_element(self.locators.build_metro_station_and_rental_period_locator(rental_period))
        action = self.create_action_chain_object()
        action.click(on_element=element).perform()

    @allure.step('Fill in personal information: "{name}", "{surname}", "{address}","{metro_station}","{phone_number}".')
    def fill_personal_information(self, name, surname, address, metro_station, phone_number):
        self.fill_input(self.locators.NAME_FIELD, name)
        self.fill_input(self.locators.SURNAME_FIELD, surname)
        self.fill_input(self.locators.ADDRESS_FIELD, address)
        self.set_metro_station(metro_station)
        self.fill_input(self.locators.PHONE_FIELD, phone_number)

    @allure.step('Click on "Далее" button.')
    def click_next_button(self):
        self.wait_element_is_clickable(self.locators.NEXT_BUTTON)
        self.click_on_element(self.locators.NEXT_BUTTON)

    @allure.step('Fill in order information: "{date_order}", "{rental_period}", "{scooter_color}","{comment}".')
    def fill_order_information(self, date_order, rental_period, scooter_color, comment):
        self.set_date_order(date_order)
        self.set_rental_period(rental_period)
        self.click_on_element(self.locators.build_scooter_color_locator(scooter_color))
        self.fill_input(self.locators.COMMENT_FIELD, comment)

    @allure.step('Click on "Заказать" button.')
    def click_complete_order_button(self):
        self.wait_element_is_clickable(self.locators.COMPLETE_ORDER_BUTTON)
        self.click_on_element(self.locators.COMPLETE_ORDER_BUTTON)

    @allure.step('Click on "Да" button.')
    def click_yes_button_confirmation_popup(self):
        self.wait_element_is_clickable(self.locators.YES_BUTTON_CONFIRMATION_POPUP)
        self.click_on_element(self.locators.YES_BUTTON_CONFIRMATION_POPUP)

    @allure.step('Wait until success complete order popup is displayed.')
    def wait_for_load_success_order_popup(self):
        self.wait_visibility_of_element(self.locators.SUCCESS_ORDER_POPUP)

    def check_success_popup_heading(self):
        return self.get_element_text(self.locators.HEADING_SUCCESS_ORDER_POPUP)
