import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data_for_tests.Alerts_Frame_Windows.nested_frames_testdata import Url, NestedFramesLocators, NestedFramesTestdata
from Methods.methods import Methods

class NestedFrames(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def nested_iframe_action(self):
        iframe = self.find_element(NestedFramesLocators.LOCATOR_IFRAME)
        self.browser.switch_to.frame(iframe)

        nested_iframe = self.find_element(NestedFramesLocators.LOCATOR_NESTED_IFRAME)
        self.browser.switch_to.frame(nested_iframe)
        # Распеватаем сверва из дочернего iframe
        print(self.find_element(NestedFramesLocators.LOCATOR_IFRAME_TEXT).text)

        self.browser.switch_to.parent_frame()
        # Распечатываем из родильского iframe
        print(self.find_element(NestedFramesLocators.LOCATOR_IFRAME_TEXT).text)
        self.browser.switch_to.default_content()