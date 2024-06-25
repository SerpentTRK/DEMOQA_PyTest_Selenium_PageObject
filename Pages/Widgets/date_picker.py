
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from Data_for_tests.Widgets.date_picker_testdata import Url, DatePickerLocators, DatePickerTestdata
from Methods.methods import Methods

class DatePicker(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def fill_data_picker(self):
        # Select Date
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA).click()
        Select(self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_YEAR)).select_by_visible_text(DatePickerTestdata.DATA_SELECT_YEAR)
        Select(self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_MONTH)).select_by_visible_text(DatePickerTestdata.DATA_SELECT_MONTH)
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_DAY).click()

        # Date And Time
        # нашли дата-пикер
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME).click()
        # кликаем на элементе выбора месяца
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME_MONTH_CHOICE).click()
        # выбираем месяц
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME_MONTH).click()
        # кликаем на элементе выбора года
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME_YEAR_CHOICE).click()
        # выбираем нижний элемент открывшегося списка с годами, и прокручиваем спиcок на 4 элемента вниз, чтобы 2015
        # год попал в зону видимости DOM
        skroll_list_down = self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME_YEAR_CHOICE_arrow_down)
        skroll_list_down.click()
        skroll_list_down.click()
        skroll_list_down.click()
        skroll_list_down.click()
        # выбираем 2015 год
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME_YEAR).click()
        # выбираем день 21
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME_DAY).click()
        # выбираем нужное время из списка
        self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA_AND_TIME_TIME).click()

        time.sleep(3)

    def data_validation(self):
        entered_date = self.find_element(DatePickerLocators.LOCATOR_SELECT_DATA).get_attribute("value")

        assert entered_date == DatePickerTestdata.DATA_FULL_DATA, \
            f"Ошибка: {entered_date} не совпадает {DatePickerTestdata.DATA_FULL_DATA}"


