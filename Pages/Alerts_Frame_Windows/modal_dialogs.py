import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data_for_tests.Alerts_Frame_Windows.modal_dialogs_testdata import Url, ModalDialogsLocators, ModalDialogsTestdata
from Methods.methods import Methods

class ModalDialogs(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def modal_dialog_windows(self):
        self.find_element(ModalDialogsLocators.LOCATOR_SMALL_MODAL).click()
        print(f"Заголовок малого модального окна: {self.find_element(ModalDialogsLocators.LOCATOR_SMALL_MODAL_HEADER).text}")
        print(f"Тело малого модального окна: {self.find_element(ModalDialogsLocators.LOCATOR_MODAL_TEXT).text}")
        self.find_element(ModalDialogsLocators.LOCATOR_SMALL_MODAL_CLOSE).click()

        self.find_element(ModalDialogsLocators.LOCATOR_LARGE_MODAL).click()
        print(f"Заголовок малого модального окна: {self.find_element(ModalDialogsLocators.LOCATOR_LARGE_MODAL_HEADER).text}")
        print(f"Тело малого модального окна: {self.find_element(ModalDialogsLocators.LOCATOR_MODAL_TEXT).text}")
        self.find_element(ModalDialogsLocators.LOCATOR_LARGE_MODAL_CLOSE).click()