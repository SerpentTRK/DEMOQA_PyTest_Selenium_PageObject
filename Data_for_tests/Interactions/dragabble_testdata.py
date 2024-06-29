import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/dragabble"

class DragabbleLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_TAB_SEMPLE = (By.CSS_SELECTOR, "")

class DragabbleTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_DROPPED = "Dropped!"