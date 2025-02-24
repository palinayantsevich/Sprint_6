from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    RENTAL_FORM = (By.XPATH, '//div[@class="Order_Form__17u6u"]')
    DATE_ORDER_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD_FIELD = (By.XPATH, '//div[text()="* Срок аренды"]/parent::div')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    COMPLETE_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    CONFIRMATION_POPUP = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    YES_BUTTON_CONFIRMATION_POPUP = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_ORDER_POPUP = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    HEADING_SUCCESS_ORDER_POPUP = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')

    def build_metro_station_and_rental_period_locator(self, text):
        return (By.XPATH, f'//div[text()="{text}"]')

    def build_scooter_color_locator(self, text):
        return (By.XPATH, f'//label[text()="{text}"]')
