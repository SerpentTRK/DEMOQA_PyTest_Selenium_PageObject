import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/buttons"

class ButtonsLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_DOUBLECLICK_BUTTON = (By.ID, "doubleClickBtn")
    LOCATOR_RIGHTCLICK_BUTTON = (By.ID, "rightClickBtn")
    LOCATOR_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    LOCATOR_DOUBLECLICK_BUTTON_VALIDATION = (By.CSS_SELECTOR, "#doubleClickMessage")
    LOCATOR_RIGHTCLICK_BUTTON_VALIDATION = (By.CSS_SELECTOR, "#rightClickMessage")
    LOCATOR_BUTTON_VALIDATION = (By.CSS_SELECTOR, "#dynamicClickMessage")


class ButtonsTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_DOUBLECLICK_BUTTON = "You have done a double click"
    DATA_RIGHTCLICK_BUTTON = "You have done a right click"
    DATA_BUTTON = "You have done a dynamic click"

