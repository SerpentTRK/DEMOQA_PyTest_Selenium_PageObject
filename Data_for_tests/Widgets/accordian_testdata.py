import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/accordian"

class AccordianLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_ACCORDEON_HEADER_1 = (By.CSS_SELECTOR, "#section1Heading")


class AccordianTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """