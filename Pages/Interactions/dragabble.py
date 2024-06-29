
import time

from Data_for_tests.Interactions.dragabble_testdata import Url, DragabbleLocators, DragabbleTestdata
from Methods.methods import Methods

class Dragabble(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def lock_and_drop_elements(self):
        self.simple()

    def simple(self):
        pass