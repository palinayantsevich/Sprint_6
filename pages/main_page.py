import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('Scroll to the "Order Button" on the main page, wait until it is displayed and click on it.')
    def scroll_wait_click_order_button(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON)
        self.wait_visibility_of_element(self.locators.ORDER_BUTTON)
        self.click_on_element(self.locators.ORDER_BUTTON)

    @allure.step('Wait until the "Order Page" is loaded.')
    def wait_for_load_order_page(self):
        self.wait_load_page_by_checking_url(Urls.ORDER_PAGE_URL)

    @allure.step(
        'Scroll to the question "{question_text}" on the main page, wait until it is displayed and click on it.')
    def scroll_wait_click_question(self, question_text):
        self.scroll_to_element(self.locators.build_question_text_locator(question_text))
        self.wait_element_is_clickable(self.locators.build_question_text_locator(question_text))
        self.click_on_element(self.locators.build_question_text_locator(question_text))

    @allure.step(
        'Verify that the question text is: "{question_text}".')
    def get_question_text(self, question_text):
        self.wait_visibility_of_element(self.locators.build_question_text_locator(question_text))
        return self.get_element_text(self.locators.build_question_text_locator(question_text))

    @allure.step(
        'Verify that the answer text is: "{answer_text}".')
    def get_answer_text(self, answer_text):
        self.wait_visibility_of_element(self.locators.build_answer_text_locator(answer_text))
        return self.get_element_text(self.locators.build_answer_text_locator(answer_text))
