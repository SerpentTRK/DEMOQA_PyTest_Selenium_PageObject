
import time

from selenium.webdriver import Keys

from Data_for_tests.Widgets.auto_complete_testdata import Url, AutoCompleteLocators, AutoCompleteTestdata
from Methods.methods import Methods

class AutoComplete(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def auto_complete_menu(self):
        multiple_color_names = self.find_element(AutoCompleteLocators.LOCATOR_TYPE_MULTIPLE)
        multiple_color_names.send_keys(AutoCompleteTestdata.DATA_COLOR_RED)
        multiple_color_names.send_keys(Keys.RETURN)
        multiple_color_names.send_keys(AutoCompleteTestdata.DATA_COLOR_BLACK)
        multiple_color_names.send_keys(Keys.RETURN)

        single_color_names = self.find_element(AutoCompleteLocators.LOCATOR_TYPE_SINGLE)
        single_color_names.send_keys(AutoCompleteTestdata.DATA_COLOR_BLACK)
        single_color_names.send_keys(Keys.RETURN)
        single_color_names.send_keys(AutoCompleteTestdata.DATA_COLOR_RED)
        single_color_names.send_keys(Keys.RETURN)

    def data_validation(self):
        multiple_color_data = self.find_element(AutoCompleteLocators.LOCATOR_TYPE_MULTIPLE_TEXT).text
        assert AutoCompleteTestdata.DATA_COLOR_RED in multiple_color_data
        assert AutoCompleteTestdata.DATA_COLOR_BLACK in multiple_color_data

        single_color_names = self.find_element(AutoCompleteLocators.LOCATOR_TYPE_SINGLE_TEXT).text
        assert AutoCompleteTestdata.DATA_COLOR_RED in single_color_names


