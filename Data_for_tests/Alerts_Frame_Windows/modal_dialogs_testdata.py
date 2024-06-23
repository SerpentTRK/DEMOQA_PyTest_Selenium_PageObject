import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/modal-dialogs"

class ModalDialogsLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_SMALL_MODAL = (By.CSS_SELECTOR, "button#showSmallModal")
    LOCATOR_LARGE_MODAL = (By.CSS_SELECTOR, "button#showLargeModal")
    LOCATOR_SMALL_MODAL_HEADER = (By.CSS_SELECTOR, "#example-modal-sizes-title-sm")
    LOCATOR_MODAL_TEXT = (By.CSS_SELECTOR, "div.modal-body")
    LOCATOR_SMALL_MODAL_CLOSE = (By.CSS_SELECTOR, "button.close")
    LOCATOR_LARGE_MODAL_HEADER = (By.CSS_SELECTOR, "div#example-modal-sizes-title-lg")
    LOCATOR_LARGE_MODAL_CLOSE = (By.CSS_SELECTOR, "button#closeLargeModal")



class ModalDialogsTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    ALERT_CONFIRM_TEXT = "You selected Ok"