
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Widgets.select_menu_testdata import Url, SelectMenuLocators, SelectMenuTestdata
from Methods.methods import Methods

class SelectMenu(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def choice_and_validation_menu_elements(self):
        ## Select Value
        # Находим к кликаем на самом меню
        select_value = self.find_element(SelectMenuLocators.LOCATOR_SELECT_VALUE)
        select_value.click()

        # создаем объект ActionChains
        actions = ActionChains(self.browser)

        # нажимаем стрелку вниз и Enter. Выбираем первый сверху элемент.
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        assert select_value.text == SelectMenuTestdata.DATA_SELECT_VALUE_Group1_option1, \
            f"Ошибка: {select_value.text} не совпадает с {SelectMenuTestdata.DATA_SELECT_VALUE_Group1_option1}"

        # выбираем пятый сверху элемент
        for _ in range(4):
            actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER).perform()
        assert select_value.text == SelectMenuTestdata.DATA_SELECT_VALUE_A_root_option, \
            f"Ошибка: {select_value.text} не совпадает с {SelectMenuTestdata.DATA_SELECT_VALUE_A_root_option}"

        ## Select One
        # Находим к кликаем на самом меню
        select_one = self.find_element(SelectMenuLocators.LOCATOR_SELECT_ONE)
        select_one.click()

        # создаем объект ActionChains
        actions = ActionChains(self.browser)

        # нажимаем стрелку вниз и Enter. Выбираем первый сверху элемент.
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        assert select_one.text == SelectMenuTestdata.DATA_SELECT_ONE_Mr, \
            f"Ошибка: {select_one.text} не совпадает с {SelectMenuTestdata.DATA_SELECT_ONE_Mr}"

        # выбираем пятый сверху элемент
        for _ in range(4):
            actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER).perform()
        assert select_one.text == SelectMenuTestdata.DATA_SELECT_ONE_Prof, \
            f"Ошибка: {select_one.text} не совпадает с {SelectMenuTestdata.DATA_SELECT_ONE_Prof}"

        ## Old Style Select Menu
        old_style_menu = self.find_element(SelectMenuLocators.LOCATOR_OLD_STYLE_SELECT_MENU_Voilet)
        old_style_menu.click()
        assert old_style_menu.text == SelectMenuTestdata.DATA_Old_Style_Select_Menu_Voilet, \
            f"Ошибка: {old_style_menu.text} не совпадает с {SelectMenuTestdata.DATA_Old_Style_Select_Menu_Voilet}"

        ## Multiselect drop down
        multiselect = self.find_element(SelectMenuLocators.LOCATOR_MULTISELECT_DROP_DOWN)
        multiselect.click()

        # создаем объект ActionChains
        actions = ActionChains(self.browser)

        # нажимаем стрелку вниз и Enter. Выбираем первый сверху элемент.
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        actions.send_keys(Keys.ENTER).perform()
        actions.send_keys(Keys.ENTER).perform()
        # удилам черный для тренировки
        self.find_element(SelectMenuLocators.LOCATOR_MULTISELECT_DROP_DOWN_Del_Black).click()
        time.sleep(0.5)

        assert multiselect.text.split() == SelectMenuTestdata.DATA_MULTISELECT_DROP_DOWN, \
            f"Ошибка: {multiselect.text.split()} не совпадает с {SelectMenuTestdata.DATA_MULTISELECT_DROP_DOWN}"

        ## Standard multi select
        standard_multi_select = self.find_element(SelectMenuLocators.LOCATOR_STANDARD_MULTI_SELECT)
        standard_multi_select.click()
        standard_multi_select.text
        assert standard_multi_select.text == SelectMenuTestdata.DATA_STANDARD_MULTI_SELECT, \
            f"Ошибка: {standard_multi_select.text} не совпадает с {SelectMenuTestdata.DATA_STANDARD_MULTI_SELECT}"


        time.sleep(3)