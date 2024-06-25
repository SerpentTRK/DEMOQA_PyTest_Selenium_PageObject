import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/date-picker"

class DatePickerLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_SELECT_DATA = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
    LOCATOR_SELECT_DATA_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    LOCATOR_SELECT_DATA_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    LOCATOR_SELECT_DATA_DAY = (By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day--021")


    LOCATOR_SELECT_DATA_AND_TIME = (By.CSS_SELECTOR, "#dateAndTimePickerInput")
    LOCATOR_SELECT_DATA_AND_TIME_MONTH_CHOICE = (By.CSS_SELECTOR, ".react-datepicker__month-read-view")
    LOCATOR_SELECT_DATA_AND_TIME_MONTH = (By.CSS_SELECTOR, "div.react-datepicker__month-dropdown > div:nth-child(4)")

    LOCATOR_SELECT_DATA_AND_TIME_YEAR_CHOICE = (By.CSS_SELECTOR, ".react-datepicker__year-read-view--selected-year")
    LOCATOR_SELECT_DATA_AND_TIME_YEAR_CHOICE_arrow_down = (By.CSS_SELECTOR, "div.react-datepicker__year-dropdown > div:nth-child(13)")
    LOCATOR_SELECT_DATA_AND_TIME_YEAR = (By.CSS_SELECTOR, "div.react-datepicker__year-dropdown > div:nth-child(12)")

    LOCATOR_SELECT_DATA_AND_TIME_DAY = (By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day--021")
    LOCATOR_SELECT_DATA_AND_TIME_TIME = (By.CSS_SELECTOR, "div.react-datepicker__time > div > ul > li:nth-child(73)")



class DatePickerTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_SELECT_YEAR = "2015"
    DATA_SELECT_MONTH = "April"
    DATA_SELECT_DAY = "21"
    DATA_SELECT_TIME = "18:00"
    DATA_FULL_DATA = "04/21/2015"
    DATA_FULL_DATA_AND_TIME = "04/21/2015 6:00 PM"