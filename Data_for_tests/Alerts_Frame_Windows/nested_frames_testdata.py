import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/nestedframes"

class NestedFramesLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_IFRAME = (By.CSS_SELECTOR, "iframe#frame1")
    LOCATOR_NESTED_IFRAME = (By.CSS_SELECTOR, "body > iframe")

    LOCATOR_IFRAME_TEXT = (By.CSS_SELECTOR, "body")
    LOCATOR_NESTED_IFRAME_TEXT = (By.CSS_SELECTOR, "")


class NestedFramesTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    ALERT_CONFIRM_TEXT = "You selected Ok"