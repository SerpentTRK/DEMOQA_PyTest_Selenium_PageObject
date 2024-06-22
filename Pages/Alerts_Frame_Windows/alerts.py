import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data_for_tests.Alerts_Frame_Windows.alerts_testdata import Url, AlertsLocators, AlertsTestdata
from Methods.methods import Methods

class Alerts(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def click_alerts_button(self):
        # Alert
        self.find_element(AlertsLocators.LOCATOR_ALERT).click()
        alert = self.browser.switch_to.alert
        print(f"Текст на странице ALERT: {alert.text}")
        alert.accept()

        # Alert 5 sec timet
        self.find_element(AlertsLocators.LOCATOR_ALERT_AFTER_5_SEC_TIMER).click()
        time.sleep(5.2)
        alert = self.browser.switch_to.alert
        print(f"Текст на странице ALERT: {alert.text}")
        alert.accept()