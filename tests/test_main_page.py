import pytest

import allure

from pages.main_page import MainPage
from data import DataMainPage
from urls import Urls


class TestMainPage:

    @allure.title(
        'Verify that user is navigated to the "Order Page" after clicking on the "Order Button" in the "Main Page".')
    def test_click_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_wait_click_order_button()
        main_page.wait_for_load_order_page()
        current_url = main_page.get_current_url()
        assert current_url == Urls.ORDER_PAGE_URL

    @allure.title(
        'Verify that each question text and answer is correct on the "Main Page".')
    @pytest.mark.parametrize(
        'question_text,answer_text',
        [
            [DataMainPage.QUESTION_1_TEXT, DataMainPage.QUESTION_1_ANSWER],
            [DataMainPage.QUESTION_2_TEXT, DataMainPage.QUESTION_2_ANSWER],
            [DataMainPage.QUESTION_3_TEXT, DataMainPage.QUESTION_3_ANSWER],
            [DataMainPage.QUESTION_4_TEXT, DataMainPage.QUESTION_4_ANSWER],
            [DataMainPage.QUESTION_5_TEXT, DataMainPage.QUESTION_5_ANSWER],
            [DataMainPage.QUESTION_6_TEXT, DataMainPage.QUESTION_6_ANSWER],
            [DataMainPage.QUESTION_7_TEXT, DataMainPage.QUESTION_7_ANSWER],
            [DataMainPage.QUESTION_8_TEXT, DataMainPage.QUESTION_8_ANSWER]
        ]
    )
    def test_question_text_and_answer(self, driver, question_text, answer_text):
        main_page = MainPage(driver)
        main_page.scroll_wait_click_question(question_text)
        current_question_text = main_page.get_question_text(question_text)
        current_question_answer = main_page.get_answer_text(answer_text)
        assert current_question_text == question_text and current_question_answer == answer_text
