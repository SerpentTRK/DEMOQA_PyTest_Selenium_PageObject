
import time

from selenium.webdriver import ActionChains

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
        self.axis_restricted()
        self.container_restricted()
        self.cursor_style()

    def simple(self):
        self.find_element(DragabbleLocators.LOCATOR_TAB_SIMPLE)
        drad_me = self.find_element(DragabbleLocators.LOCATOR_TAB_SIMPLE_drad_me)

        ActionChains(self.browser).click_and_hold(drad_me).move_by_offset(0, 200).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(drad_me).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(drad_me).move_by_offset(0, -200).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(drad_me).move_by_offset(-300, 0).release().perform()
        time.sleep(1)

    def axis_restricted(self):
        self.find_element(DragabbleLocators.LOCATOR_TAB_AXIS_RESTRICTED).click()
        only_x = self.find_element(DragabbleLocators.LOCATOR_TAB_AXIS_RESTRICTED_Only_X)
        only_y = self.find_element(DragabbleLocators.LOCATOR_TAB_AXIS_RESTRICTED_Only_Y)

        # тут будет системой будет игнорировтаься изменение координат по оси Y
        ActionChains(self.browser).click_and_hold(only_x).move_by_offset(100, 100).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(only_x).move_by_offset(-100, -100).release().perform()
        time.sleep(1)
        # тут будет системой будет игнорировтаься изменение координат по оси X
        ActionChains(self.browser).click_and_hold(only_y).move_by_offset(100, 100).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(only_y).move_by_offset(-100, -100).release().perform()
        time.sleep(1)

    def container_restricted(self):
        self.find_element(DragabbleLocators.LOCATOR_TAB_CONTAINER_RESTRICTED).click()

        contained_within_the_box = self.find_element(DragabbleLocators.LOCATOR_TAB_CONTAINER_RESTRICTED_contained_within_the_box)
        contained_within_my_parent = self.find_element(DragabbleLocators.LOCATOR_TAB_CONTAINER_RESTRICTED_contained_within_my_parent)

        ActionChains(self.browser).click_and_hold(contained_within_the_box).move_by_offset(300, 300).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(contained_within_my_parent).move_by_offset(50, 100).release().perform()
        time.sleep(1)

    def cursor_style(self):
        self.find_element(DragabbleLocators.LOCATOR_TAB_CURSOR_STYLE).click()

        cursorCenter = self.find_element(DragabbleLocators.LOCATOR_TAB_CURSOR_STYLE_cursorCenter)
        cursorTopLeft = self.find_element(DragabbleLocators.LOCATOR_TAB_CURSOR_STYLE_cursorTopLeft)
        cursorBottom = self.find_element(DragabbleLocators.LOCATOR_TAB_CURSOR_STYLE_cursorBottom)

        ActionChains(self.browser).click_and_hold(cursorCenter).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(cursorTopLeft).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(cursorBottom).move_by_offset(300, 0).release().perform()
        time.sleep(1)