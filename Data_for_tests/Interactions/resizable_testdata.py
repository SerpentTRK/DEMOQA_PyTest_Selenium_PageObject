import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/resizable"

class ResizableLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_RESIZEBLE_BOX_1 = (By.CSS_SELECTOR, "#resizableBoxWithRestriction > span")
    LOCATOR_RESIZEBLE_BOX_2 = (By.CSS_SELECTOR, "#resizable > span")

class ResizableTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
