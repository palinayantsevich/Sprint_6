from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]')

    def build_question_text_locator(self, text):
        return (By.XPATH, f'//div[text()="{text}"]')

    def build_answer_text_locator(self, text):
        return (By.XPATH, f'//p[text()="{text}"]')
