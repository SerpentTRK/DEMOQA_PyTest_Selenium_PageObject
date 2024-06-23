import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data_for_tests.Alerts_Frame_Windows.frames_testdata import Url, FramesLocators, FramesTestdata
from Methods.methods import Methods

class Frames(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def iframe_action(self):
        iframe_1 = self.find_element(FramesLocators.LOCATOR_IFRAME_1)
        self.browser.switch_to.frame(iframe_1)
        print(self.find_element(FramesLocators.LOCATOR_IFRAME_TEXT).text)
        self.browser.switch_to.default_content()

        iframe_2 = self.find_element(FramesLocators.LOCATOR_IFRAME_2)
        self.browser.switch_to.frame(iframe_2)
        print(self.find_element(FramesLocators.LOCATOR_IFRAME_TEXT).text)
        self.browser.switch_to.default_content()