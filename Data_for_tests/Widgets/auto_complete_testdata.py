import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/auto-complete"

class AutoCompleteLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_TYPE_MULTIPLE = (By.CSS_SELECTOR, "#autoCompleteMultipleInput")
    LOCATOR_TYPE_MULTIPLE_DEL_BLACK = (By.CSS_SELECTOR, ".css-xb97g8.auto-complete__multi-value__remove")
    LOCATOR_TYPE_SINGLE = (By.CSS_SELECTOR, "#autoCompleteSingleInput")

    LOCATOR_TYPE_MULTIPLE_TEXT = (By.CSS_SELECTOR, "#autoCompleteMultiple")
    LOCATOR_TYPE_SINGLE_TEXT = (By.CSS_SELECTOR, "#autoCompleteSingle")



class AutoCompleteTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_COLOR_RED = "Red"
    DATA_COLOR_BLACK = "Black"