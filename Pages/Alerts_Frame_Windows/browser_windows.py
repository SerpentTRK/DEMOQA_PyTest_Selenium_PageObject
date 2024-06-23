import os
import time


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data_for_tests.Alerts_Frame_Windows.browser_windows_testdata import Url, BrowserWindowsLocators, BrowserWindowsTestdata
from Methods.methods import Methods

class BrowserWindows(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def open_new_tabs_and_windows(self):
        original_window = self.browser.current_window_handle  # сохранили дискриптор главного окна
        wait = WebDriverWait(self.browser, 10)  # нужно подготовиться к тому, что придется ждать прогруза нового окна

        # TAB
        self.find_element(BrowserWindowsLocators.LOCATOR_TAB_BUTTON).click()
        wait.until(EC.number_of_windows_to_be(2))  # ждем пока окно гарантированно прогрузится
        self.browser.switch_to.window(self.browser.window_handles[1])  # переключились на новый таб

        print(f"Текст на странице нового таба: {self.find_element(BrowserWindowsLocators.LOCATOR_TAB_OR_WINDOWS_TEXT).text}")

        self.browser.close()  # закрываем новый таб
        self.browser.switch_to.window(original_window)  # переключились на главное по дискриптору

        # NEW WINDOW
        self.find_element(BrowserWindowsLocators.LOCATOR_NEW_WINDOW).click()
        wait.until(EC.number_of_windows_to_be(2))
        self.browser.switch_to.window(self.browser.window_handles[1])

        # если попытаться достать текст из открывшегося окна - скрипт подвисает.
        # print(f"Текст на странице нового окна: {self.find_element(BrowserWindowsLocators.LOCATOR_TAB_OR_WINDOWS_TEXT).text}")

        self.browser.close()  # закрываем новый таб
        self.browser.switch_to.window(original_window)  # переключились на главное по дискриптору

        # NEW WINDOW MESSAGE
        self.find_element(BrowserWindowsLocators.LOCATOR_NEW_WINDOW_MESSAGE).click()
        wait.until(EC.number_of_windows_to_be(2))
        self.browser.switch_to.window(self.browser.window_handles[1])

        # информационное окно открывается, мы на него переключаемся, закрываем.. но достать оттуда текст пока
        # не получается. Я не знаю как. LOCATOR_NEW_WINDOW_MESSAGE_TEXT = (By.CSS_SELECTOR, "body")
        # print(f"Текст на странице информационного окна: {self.find_element(BrowserWindowsLocators.LOCATOR_NEW_WINDOW_MESSAGE_TEXT).text}")

        self.browser.close()  # закрываем новый таб
        self.browser.switch_to.window(original_window)  # переключились на главное по дискриптору