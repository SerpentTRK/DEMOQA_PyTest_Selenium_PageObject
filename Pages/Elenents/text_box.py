import time

from selenium.webdriver.common.by import By

from Data_for_tests.Elements.text_box_testdata import Url, TextBoxLocators, TextBoxTestdata
from Methods.methods import Methods

class ElementsTextBox(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # наверное тут его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def text_box(self):
        self.find_element(TextBoxLocators.LOCATOR_FULL_NAME).send_keys(TextBoxTestdata.DATA_FULL_NAME)
        self.find_element(TextBoxLocators.LOCATOR_EMAIL).send_keys(TextBoxTestdata.DATA_EMAIL)
        self.find_element(TextBoxLocators.LOCATOR_CURRENT_ADDRESS).send_keys(TextBoxTestdata.DATA_CURRENT_ADDRESS)
        self.find_element(TextBoxLocators.LOCATOR_PERMANENT_ADDRESS).send_keys(TextBoxTestdata.DATA_PERMANENT_ADDRESS)
        self.find_element(TextBoxLocators.LOCATOR_BUTTON_SUBMIT).click()


    def data_validation(self):
        assert self.find_element((By.ID, "name")).text.split(":")[-1] == TextBoxTestdata.DATA_FULL_NAME, \
            f"Ошибка: {self.find_element((By.ID, 'name')).text.split(':')[-1]} не совпадает с {TextBoxTestdata.DATA_FULL_NAME}"

        assert self.find_element((By.ID, "email")).text.split(":")[-1] == TextBoxTestdata.DATA_EMAIL, \
            f"Ошибка: {self.find_element((By.ID, 'email')).text.split(':')[-1]} не совпадает с {TextBoxTestdata.DATA_EMAIL}"

        assert self.find_element((By.CSS_SELECTOR, "#output #currentAddress")).text.split(":")[-1] == TextBoxTestdata.DATA_CURRENT_ADDRESS, \
            f"Ошибка: {self.find_element((By.CSS_SELECTOR, '#output #currentAddress')).text.split(':')[-1]} не совпадает с {TextBoxTestdata.DATA_CURRENT_ADDRESS}"

        assert self.find_element((By.CSS_SELECTOR, "#output #permanentAddress")).text.split(":")[-1] == TextBoxTestdata.DATA_PERMANENT_ADDRESS, \
            f"Ошибка: {self.find_element((By.CSS_SELECTOR, '#output #permanentAddress')).text.split(':')[-1]} не совпадает с {TextBoxTestdata.DATA_PERMANENT_ADDRESS}"














