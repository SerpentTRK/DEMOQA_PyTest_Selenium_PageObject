
import time
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Widgets.menu_testdata import Url, MenuLocators, MenuTestdata
from Methods.methods import Methods

class Menu(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def check_full_menu(self):
        # Увеличение ширины окна браузера
        self.change_window_size(1400, 800)

        # Первое меню
        main_item_1 = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_1)
        main_item_1.click()
        print(f"Заголовок меню #1: {main_item_1.text}")
        time.sleep(0.5)

        # Второе меню
        main_item_2 = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_2)
        main_item_2.click()
        print(f"Заголовок меню #2: {main_item_2.text}")
        time.sleep(0.5)

        main_item_2_sub_item_1 = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_2_sub_item_1)
        main_item_2_sub_item_1.click()
        print(f"Заголовок меню #2/элемент 1: {main_item_2_sub_item_1.text}")
        time.sleep(0.5)

        main_item_2_sub_item_2 = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_2_sub_item_2)
        main_item_2_sub_item_2.click()
        print(f"Заголовок меню #2/элемент 2: {main_item_2_sub_item_2.text}")
        time.sleep(0.5)

        main_item_2_sub_sub_list = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_2_SUB_SUB_LIST)
        main_item_2_sub_sub_list.click()
        print(f"Заголовок меню #2/Подменю: {main_item_2_sub_sub_list.text}")
        time.sleep(0.5)

        main_item_2_sub_sub_list_sub_sub_item_1 = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_2_SUB_SUB_LIST_Sub_Sub_Item_1)
        main_item_2_sub_sub_list_sub_sub_item_1.click()
        print(f"Заголовок меню #2/Подменю/элемент 1: {main_item_2_sub_sub_list_sub_sub_item_1.text}")
        time.sleep(0.5)

        main_item_2_sub_sub_list_sub_sub_item_2 = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_2_SUB_SUB_LIST_Sub_Sub_Item_2)
        main_item_2_sub_sub_list_sub_sub_item_2.click()
        print(f"Заголовок меню #2/Подменю/элемент 2: {main_item_2_sub_sub_list_sub_sub_item_2.text}")
        time.sleep(0.5)

        # Третье меню
        main_item_3 = self.find_element(MenuLocators.LOCATOR_MAIN_ITEM_3)
        main_item_3.click()
        print(f"Заголовок меню #1: {main_item_3.text}")
        time.sleep(0.5)