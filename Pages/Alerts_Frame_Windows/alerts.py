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

        # Alert с задержкой в 5 секунд
        self.find_element(AlertsLocators.LOCATOR_ALERT_AFTER_5_SEC_TIMER).click()
        time.sleep(5.2)  #ждем, когда кнопка станет активной
        alert = self.browser.switch_to.alert
        print(f"Текст на странице ALERT: {alert.text}")
        alert.accept()

        # Confirm
        self.find_element(AlertsLocators.LOCATOR_ALERT_CONFIRM).click()
        confirm = self.browser.switch_to.alert
        confirm.accept()  # .dismiss() нажимает кнопку Отмена
        assert self.find_element(AlertsLocators.LOCATOR_ALERT_CONFIRM_VALIDATION).text == AlertsTestdata.ALERT_CONFIRM_TEXT

        #Prompt
        self.find_element(AlertsLocators.LOCATOR_ALERT_PROMPT).click()
        prompt = self.browser.switch_to.alert
        prompt.send_keys("Вальдемар")
        prompt.accept()
        assert self.find_element(AlertsLocators.LOCATOR_ALERT_PROMPT_VALIDATION).text == AlertsTestdata.ALERT_PROMPT_TEXT