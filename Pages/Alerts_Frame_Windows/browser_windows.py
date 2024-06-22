import os
import time

from Data_for_tests.Elements.dynamic_properties_testdata import Url, DynamicPropertiesLocators, DynamicPropertiesTestdata
from Methods.methods import Methods

class DynamicProperties(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def push_dynamic_buttons(self):
        self.find_element(DynamicPropertiesLocators.LOCATOR_ENEBLE_AFTER_BUTTON).click()