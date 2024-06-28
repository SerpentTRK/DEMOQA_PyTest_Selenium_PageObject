
import time

from Data_for_tests.Interactions.selectable_testdata import Url, SelectableLocators, SelectableTestdata
from Methods.methods import Methods

class Selectable(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def choice_and_check(self):
        ## Tab LIST
        self.find_element(SelectableLocators.LOCATOR_TAB_LIST).click()

        cras_justo_odio = self.find_element(SelectableLocators.LOCATOR_cras_justo_odi)
        cras_justo_odio.click()
        check_choise_cras_justo_odio = self.find_element(SelectableLocators.LOCATOR_cras_justo_odi_selected_validation)
        assert check_choise_cras_justo_odio.text == SelectableTestdata.DATA_cras_justo_odio, \
            f"Ошибка. {check_choise_cras_justo_odio.text} не совпадает с {SelectableTestdata.DATA_cras_justo_odio}"

        ## Tab GRID
        self.find_element(SelectableLocators.LOCATOR_TAB_GRID).click()

        box_one = self.find_element(SelectableLocators.LOCATOR_BOX_ONE)
        box_one.click()
        check_choise_box_one = self.find_element(SelectableLocators.LOCATOR_BOX_ONE_selected_validation)
        assert check_choise_box_one.text == SelectableTestdata.DATA_box_one, \
            f"Ошибка. {check_choise_box_one.text} не совпадает с {SelectableTestdata.DATA_box_one}"

