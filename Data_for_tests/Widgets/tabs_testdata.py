import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/tabs"

class TabsLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_WHAT = (By.CSS_SELECTOR, "#demo-tab-what")
    LOCATOR_ORIGIN = (By.CSS_SELECTOR, "#demo-tab-origin")
    LOCATOR_USE = (By.CSS_SELECTOR, "#demo-tab-use")

class TabsTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
