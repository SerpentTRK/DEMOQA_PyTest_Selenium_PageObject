import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/frames"

class FramesLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_IFRAME_1 = (By.CSS_SELECTOR, "iframe#frame1")
    LOCATOR_IFRAME_2 = (By.CSS_SELECTOR, "iframe#frame2")

    LOCATOR_IFRAME_TEXT = By.CSS_SELECTOR, "h1#sampleHeading"


class FramesTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """

