import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/radio-button"

class RadioButtonLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_RADIO_YES = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > div:nth-child(2) > label")
    LOCATOR_RESULTS = (By.CSS_SELECTOR, ".mt-3")


class RadioButtonTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
