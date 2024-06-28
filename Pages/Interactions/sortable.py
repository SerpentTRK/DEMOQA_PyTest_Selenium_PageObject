
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Interactions.sortable_testdata import Url, SortableLocators, SortableTestdata
from Methods.methods import Methods

class Sortable(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def choice_replace_and_validation(self):
        ## List Переключаемся в Tab List
        self.find_element(SortableLocators.LOCATOR_TAB_LIST).click()

        line_one = self.find_element(SortableLocators.LOCATOR_line_ONE)
        line_five = self.find_element(SortableLocators.LOCATOR_line_FIVE)

        ActionChains(self.browser).click_and_hold(line_one).move_to_element(line_five).release().perform()

        # надо убедиться, что линия ONE находится на позиции пятого элемента
        element_one_new_position = self.find_element(SortableLocators.LOCATOR_line_ONE_VALIDATON_new_position)

        assert element_one_new_position.text == SortableTestdata.DATA_ELEMENT_ONE, \
            f"Ошибка: {element_one_new_position.text} не совпадает с {SortableTestdata.DATA_ELEMENT_ONE}"

        ## Grid Переключаемся в Tab Grid
        self.find_element(SortableLocators.LOCATOR_TAB_GRID).click()

        box_one = self.find_element(SortableLocators.LOCATOR_BOX_ONE)
        box_five = self.find_element(SortableLocators.LOCATOR_BOX_FIVE)

        ActionChains(self.browser).click_and_hold(box_one).move_to_element(box_five).release().perform()

        # надо убедиться, что коробка ONE находится на позиции пятого элемента
        box_one_new_position = self.find_element(SortableLocators.LOCATOR_BOX_ONE_VALIDATON_new_position)

        assert box_one_new_position.text == SortableTestdata.DATA_ELEMENT_ONE, \
            f"Ошибка: {box_one_new_position.text} не совпадает с {SortableTestdata.DATA_ELEMENT_ONE}"




