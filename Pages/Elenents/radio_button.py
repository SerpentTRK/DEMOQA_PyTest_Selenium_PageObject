from selenium.webdriver.common.by import By

from Data_for_tests.Elements.radio_button_testdata import Url, RadioButtonLocators, RadioButtonTestdata
from Methods.methods import Methods

class ElementsRadioButton(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def radio_button(self):
        self.find_element(RadioButtonLocators.LOCATOR_RADIO_YES).click()

    def data_validation(self):
        element = self.find_element(RadioButtonLocators.LOCATOR_RADIO_YES).text

        assert element.split()[-1] == "Yes", f"Ошибка: '{element.split()[-1]}' не совпадает с 'Yes'"