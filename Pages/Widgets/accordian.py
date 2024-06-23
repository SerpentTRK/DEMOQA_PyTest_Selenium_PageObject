
import time

from Data_for_tests.Widgets.accordian_testdata import Url, AccordianLocators, AccordianTestdata
from Methods.methods import Methods

class Accordian(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def accordian_menu(self):
        self.find_element(AccordianLocators.LOCATOR_1_HEADER).click()
        print(f"Заголовок первого меню: {self.find_element(AccordianLocators.LOCATOR_1_HEADER).text}")
        print(f"Тело первого раздела меню: {self.find_element(AccordianLocators.LOCATOR_1_BODY).text}")
        self.find_element(AccordianLocators.LOCATOR_2_HEADER).click()
        print(f"Заголовок второго меню: {self.find_element(AccordianLocators.LOCATOR_2_HEADER).text}")
        print(f"Тело второго раздела меню: {self.find_element(AccordianLocators.LOCATOR_2_BODY).text}")
        self.find_element(AccordianLocators.LOCATOR_3_HEADER).click()
        print(f"Заголовок второго меню: {self.find_element(AccordianLocators.LOCATOR_3_HEADER).text}")
        print(f"Тело второго раздела меню: {self.find_element(AccordianLocators.LOCATOR_3_BODY).text}")