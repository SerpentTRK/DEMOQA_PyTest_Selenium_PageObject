
import time
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Widgets.slider_testdata import Url, SliderLocators, SliderTestdata
from Methods.methods import Methods

class Slider(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def move_slider(self):
        pass