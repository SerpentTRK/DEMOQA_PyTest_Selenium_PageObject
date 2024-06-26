
import time
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Widgets.tabs_testdata import Url, TabsLocators, TabsTestdata
from Methods.methods import Methods

class Tab(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def use_tabs(self):
        self.find_element(TabsLocators.LOCATOR_WHAT).click()
        print(f"Заголовок Tab: {self.find_element(TabsLocators.LOCATOR_WHAT).text}")
        time.sleep(2)

        self.find_element(TabsLocators.LOCATOR_ORIGIN).click()
        print(f"Заголовок Tab: {self.find_element(TabsLocators.LOCATOR_ORIGIN).text}")
        time.sleep(2)

        self.find_element(TabsLocators.LOCATOR_USE).click()
        print(f"Заголовок Tab: {self.find_element(TabsLocators.LOCATOR_USE).text}")
        time.sleep(2)
