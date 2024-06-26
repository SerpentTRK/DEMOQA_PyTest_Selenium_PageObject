
import time
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Widgets.progress_bar_testdata import Url, ProgressBarLocators, ProgressBarTestdata
from Methods.methods import Methods

class ProgressBar(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def start_and_stop(self):
        # запускаем прогресс бар
        self.find_element(ProgressBarLocators.LOCATOR_START_AND_STOP_BUTTON).click()

        while True:
            progress_value = self.find_element(ProgressBarLocators.LOCATOR_FILLING_PROGRESS_BAR).get_attribute("aria-valuenow")
            if progress_value == ProgressBarTestdata.DATA_FOR_PRESS_STOP_BUTTON_75:
                self.find_element(ProgressBarLocators.LOCATOR_START_AND_STOP_BUTTON).click()
                break

        print(self.find_element(ProgressBarLocators.LOCATOR_FILLING_PROGRESS_BAR).get_attribute("aria-valuenow"))
        self.find_element(ProgressBarLocators.LOCATOR_START_AND_STOP_BUTTON).click()

        while True:
            progress_value = self.find_element(ProgressBarLocators.LOCATOR_FILLING_PROGRESS_BAR).get_attribute("aria-valuenow")
            if progress_value == ProgressBarTestdata.DATA_FOR_PRESS_STOP_BUTTON_100:
                break

        print(self.find_element(ProgressBarLocators.LOCATOR_FILLING_PROGRESS_BAR).get_attribute("aria-valuenow"))
        time.sleep(3)

        self.find_element(ProgressBarLocators.LOCATOR_RESET_BUTTON).click()

        time.sleep(1)
