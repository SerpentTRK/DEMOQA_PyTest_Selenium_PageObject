
import time

from Data_for_tests.Widgets.accordian_testdata import Url, AccordianLocators, AccordianTestdata
from Methods.methods import Methods

class Accordian(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def modal_dialog_windows(self):
        self.find_element().click()