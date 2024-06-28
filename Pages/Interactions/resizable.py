
import time

from selenium.webdriver import ActionChains

from Data_for_tests.Interactions.resizable_testdata import Url, ResizableLocators, ResizableTestdata
from Methods.methods import Methods

class Resizable(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def change_size_of_element(self):
        self.change_window_size(1400, 1080)
        time.sleep(0.5)

        resize_element_1 = self.find_element(ResizableLocators.LOCATOR_RESIZEBLE_BOX_1)

        ActionChains(self.browser).click_and_hold(resize_element_1).move_by_offset(-50, -50).release().perform()
        time.sleep(3)
        ActionChains(self.browser).click_and_hold(resize_element_1).move_by_offset(350, 150).release().perform()
        time.sleep(3)
        ActionChains(self.browser).click_and_hold(resize_element_1).move_by_offset(-300, -100).release().perform()
        time.sleep(5)

        # начальный размер окна 200 х 200 - это move_by_offset(0, 0). Значит для 150 х 150 мы ставим
        # move_by_offset(-50, -50). ТЕПЕРЬ!!! 150 х 150 - это move_by_offset(0, 0).

        resize_element_2 = self.find_element(ResizableLocators.LOCATOR_RESIZEBLE_BOX_2)

        ActionChains(self.browser).click_and_hold(resize_element_2).move_by_offset(-50, -50).release().perform()
        time.sleep(3)
        ActionChains(self.browser).click_and_hold(resize_element_2).move_by_offset(350, 150).release().perform()
        time.sleep(3)
        ActionChains(self.browser).click_and_hold(resize_element_2).move_by_offset(-300, -100).release().perform()
        time.sleep(5)



