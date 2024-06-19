import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/text-box"

class TextBoxLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_FULL_NAME = (By.CSS_SELECTOR, "#userForm #userName")
    LOCATOR_EMAIL = (By.ID, "userEmail")
    LOCATOR_CURRENT_ADDRESS = (By.ID, "currentAddress")
    LOCATOR_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    LOCATOR_BUTTON_SUBMIT = (By.ID, "submit")

    LOCATOR_FULL_DATA = (By.CSS_SELECTOR, "#output > div")

class TextBoxTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_FULL_NAME = "Василий Алибабаевич"
    DATA_EMAIL = "test@test.ru"
    DATA_CURRENT_ADDRESS = "А/Я 000001, На деревню Дедушке"
    DATA_PERMANENT_ADDRESS = "Коробка от холодильника"
