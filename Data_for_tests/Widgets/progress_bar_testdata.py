import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/progress-bar"

class ProgressBarLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_START_AND_STOP_BUTTON = (By.CSS_SELECTOR, "button#startStopButton")
    LOCATOR_FILLING_PROGRESS_BAR = (By.CLASS_NAME, "progress-bar")
    LOCATOR_RESET_BUTTON = (By.CSS_SELECTOR, "#resetButton")

class ProgressBarTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_FOR_PRESS_STOP_BUTTON_75 = "75"
    DATA_FOR_PRESS_STOP_BUTTON_100 = "100"