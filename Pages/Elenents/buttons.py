import time

from selenium.webdriver import ActionChains

from Data_for_tests.Elements.buttons_testdata import Url, ButtonsLocators, ButtonsTestdata
from Methods.methods import Methods

class Buttons(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def buttons(self):
        # даблклик
        clickable_double = self.find_element(ButtonsLocators.LOCATOR_DOUBLECLICK_BUTTON)
        ActionChains(self.browser).double_click(clickable_double).perform()
        # правый клик
        action_right = self.find_element(ButtonsLocators.LOCATOR_RIGHTCLICK_BUTTON)
        ActionChains(self.browser).context_click(action_right).perform()
        # одиночный клик
        self.find_element(ButtonsLocators.LOCATOR_BUTTON).click()

    def data_validation(self):
        assert self.find_element(ButtonsLocators.LOCATOR_DOUBLECLICK_BUTTON_VALIDATION).text \
               == ButtonsTestdata.DATA_DOUBLECLICK_BUTTON, \
            f"Ошибка: '{self.find_element(ButtonsLocators.LOCATOR_DOUBLECLICK_BUTTON_VALIDATION).text}' " \
            f"не совпадает с '{ButtonsTestdata.DATA_DOUBLECLICK_BUTTON}'"

        assert self.find_element(ButtonsLocators.LOCATOR_RIGHTCLICK_BUTTON_VALIDATION).text \
               == ButtonsTestdata.DATA_RIGHTCLICK_BUTTON, \
            f"Ошибка: '{self.find_element(ButtonsLocators.LOCATOR_RIGHTCLICK_BUTTON_VALIDATION).text}' " \
            f"не совпадает с '{ButtonsTestdata.DATA_RIGHTCLICK_BUTTON}'"

        assert self.find_element(ButtonsLocators.LOCATOR_BUTTON_VALIDATION).text \
               == ButtonsTestdata.DATA_BUTTON, \
            f"Ошибка: '{self.find_element(ButtonsLocators.LOCATOR_BUTTON_VALIDATION).text}' " \
            f"не совпадает с '{ButtonsTestdata.DATA_BUTTON}'"