
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from Data_for_tests.Widgets.date_picker_testdata import Url, DatePickerLocators, DatePickerTestdata
from Methods.methods import Methods

class DatePicker(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def fill_data_picker(self):
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA).click()
        Select(self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_YEAR)).select_by_visible_text(DatePickerTestdata.DATA_SELECT_YEAR)
        Select(self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_MONTH)).select_by_visible_text(DatePickerTestdata.DATA_SELECT_MONTH)
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_DAY).click()

    def data_validation(self):
        entered_date = self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA).get_attribute("value")

        assert entered_date == DatePickerTestdata.DATA_FULL_DATA, \
            f"Ошибка: {entered_date} не совпадает {DatePickerTestdata.DATA_FULL_DATA}"


