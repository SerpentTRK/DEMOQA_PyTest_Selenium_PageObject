import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/dynamic-properties"

class DynamicPropertiesLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_ENEBLE_AFTER_BUTTON = (By.CSS_SELECTOR, "button#enableAfter")
    LOCATOR_COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button#colorChange")
    LOCATOR_VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, "button#visibleAfter")



class DynamicPropertiesTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
