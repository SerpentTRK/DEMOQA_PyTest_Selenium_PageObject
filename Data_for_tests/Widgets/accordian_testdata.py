import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/accordian"

class AccordianLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_1_HEADER = (By.CSS_SELECTOR, "#section1Heading")
    LOCATOR_1_BODY = (By.CSS_SELECTOR, "#section1Content")
    LOCATOR_2_HEADER = (By.CSS_SELECTOR, "#section2Heading")
    LOCATOR_2_BODY = (By.CSS_SELECTOR, "#section2Content")
    LOCATOR_3_HEADER = (By.CSS_SELECTOR, "#section3Heading")
    LOCATOR_3_BODY = (By.CSS_SELECTOR, "#section3Content")




class AccordianTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """