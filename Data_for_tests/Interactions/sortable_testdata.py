import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/sortable"

class SortableLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")

    LOCATOR_line_ONE = (By.CSS_SELECTOR, "#demo-tabpane-list > div > div:nth-child(1)")
    LOCATOR_line_FIVE = (By.CSS_SELECTOR, "#demo-tabpane-list > div > div:nth-child(5)")
    LOCATOR_line_ONE_VALIDATON_new_position = (By.CSS_SELECTOR, "#demo-tabpane-list > div > div:nth-child(5)")

    LOCATOR_TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")

    LOCATOR_BOX_ONE = (By.CSS_SELECTOR, "#demo-tabpane-grid > div > div > div:nth-child(1)")
    LOCATOR_BOX_FIVE = (By.CSS_SELECTOR, "#demo-tabpane-grid > div > div > div:nth-child(5)")
    LOCATOR_BOX_ONE_VALIDATON_new_position = (By.CSS_SELECTOR, "#demo-tabpane-grid > div > div > div:nth-child(5)")

class SortableTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_ELEMENT_ONE = "One"
