import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/browser-windows"

class BrowserWindowsLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_TAB_BUTTON = (By.CSS_SELECTOR, "button#tabButton")
    LOCATOR_TAB_OR_WINDOWS_TEXT = (By.CSS_SELECTOR, "#sampleHeading")
    LOCATOR_NEW_WINDOW = (By.CSS_SELECTOR, "button#windowButton")
    LOCATOR_NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "button#messageWindowButton")
    LOCATOR_NEW_WINDOW_MESSAGE_TEXT = (By.CSS_SELECTOR, "body")



class BrowserWindowsTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
