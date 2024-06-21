import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/broken"

class BrokenLinksImagesLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_VALID_IMAGE = (By.CSS_SELECTOR, "img[src*='.jpg']")
    LOCATOR_VALID_LINKS = (By.XPATH, "//a[contains(text(), 'Link')]")


class BrokenLinksImagesTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_LINKS_RESPONSE = ""